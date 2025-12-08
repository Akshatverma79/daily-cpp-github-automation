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
    print("❌ Error: API Key is missing.")
    exit(1)

# Clean the key
api_key = api_key.strip()

print(f"🔑 Checking Key: {api_key[:5]}... (hidden)")

# 1. Ask Google to list ALL available models for this key
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print(f"\n❌ API CONNECTION FAILED:")
        print(f"Error Code: {data['error']['code']}")
        print(f"Message: {data['error']['message']}")
    else:
        print("\n✅ API CONNECTION SUCCESSFUL!")
        print("Your key has access to these models:")
        available_models = [m['name'] for m in data.get('models', [])]
        
        found_flash = False
        for model in available_models:
            print(f" - {model}")
            if "gemini-1.5-flash" in model:
                found_flash = True
        
        print("\n-----------------------------------")
        if found_flash:
            print("🎉 GOOD NEWS: 'models/gemini-1.5-flash' IS available!")
            print("If you see this, the error might be a typo in your previous URL.")
        else:
            print("⚠️ BAD NEWS: 'gemini-1.5-flash' is NOT in the list.")
            print("This means your Project (in Google AI Studio) does not have 1.5 Flash enabled.")
            print("Try using 'models/gemini-pro' instead, as it is usually available.")

except Exception as e:
    print(f"❌ Script crashed: {e}")

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
