import os
import json
import random
from datetime import datetime
import requests

# ---------------------------
# 1. DSA Topic Roadmap
# ---------------------------
dsa_topics = [
    "Arrays Basics",
    "Arrays Problems",
    "Time and Space Complexity",
    "Pointers in C++",
    "Recursion Basics",
    "Recursion Problems",
    "Linked List Basics",
    "Doubly Linked List",
    "Stacks Implementation",
    "Queues Implementation",
    "Binary Trees Basics",
    "Tree Traversals",
    "Binary Search Tree",
    "Graphs Basics",
    "Graph Traversals (BFS/DFS)",
    "Dynamic Programming Intro",
    "Knapsack Problems",
    "Greedy Algorithms",
    "Sliding Window Techniques"
]

# ---------------------------
# 2. Progress Tracking
# ---------------------------
if not os.path.exists("progress.json"):
    with open("progress.json", "w") as f:
        json.dump({"index": 0}, f)

with open("progress.json", "r") as f:
    progress = json.load(f)

index = progress["index"]
topic = dsa_topics[index % len(dsa_topics)]

# ---------------------------
# 3. Generate Notes with Gemini API
# ---------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ API Key is missing! Check your GitHub Secrets.")

# FIX: Remove accidental spaces/newlines from the key
api_key = api_key.strip() 

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

prompt = f"""
Generate a clean and simple DSA learning note.
Topic: {topic}
Language: C++
Explain: concept, importance, small example, C++ implementation.
Keep it short.
"""

# Safety check for the 'requests' library
try:
    import requests
except ImportError:
    raise ImportError("❌ The 'requests' library is missing. You need to install it in your YAML file.")

response = requests.post(
    url,
    json={"contents": [{"parts": [{"text": prompt}]}]},
    headers={"Content-Type": "application/json"}
)

result = response.json()

# FIX: Check if Google sent an error instead of crashing
if "error" in result:
    raise Exception(f"❌ Google API Error: {result['error']['message']}")

# Proceed only if successful
if "candidates" in result:
    note = result["candidates"][0]["content"]["parts"][0]["text"]
else:
    raise Exception("❌ Unexpected response format from Google (No candidates found).")

# ---------------------------
# 4. Save notes
# ---------------------------
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"""

# 📘 DSA Learning Note  
### 🧠 Topic: {topic}  
🕒 {time_now}

{note}

---
"""

with open("cpp_notes.md", "a", encoding="utf-8") as file:
    file.write(content)

# ---------------------------
# 5. Update progress
# ---------------------------
progress["index"] = index + 1
with open("progress.json", "w") as f:
    json.dump(progress, f)
