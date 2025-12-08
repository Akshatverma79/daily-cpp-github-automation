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
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + api_key

prompt = f"""
Generate a clean and simple DSA learning note.

Topic: {topic}
Language: C++

Explain:
- What the concept means
- Why it matters
- 1 example problem (small)
- 1 simple C++ implementation

Keep the style short and friendly.
"""

response = requests.post(
    url,
    json={"contents": [{"parts": [{"text": prompt}]}]},
    headers={"Content-Type": "application/json"}
)

result = response.json()
note = result["candidates"][0]["content"]["parts"][0]["text"]

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
