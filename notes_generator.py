import os
import json
import time
import random
from datetime import datetime
import requests

# ---------------------------
# 1. DSA Topic Roadmap
# ---------------------------
dsa_topics = [
    "Arrays Basics", "Arrays Problems", "Time and Space Complexity",
    "Pointers in C++", "Recursion Basics", "Recursion Problems",
    "Linked List Basics", "Doubly Linked List", "Stacks Implementation",
    "Queues Implementation", "Binary Trees Basics", "Tree Traversals",
    "Binary Search Tree", "Graphs Basics", "Graph Traversals (BFS/DFS)",
    "Dynamic Programming Intro", "Knapsack Problems", "Greedy Algorithms",
    "Sliding Window Techniques",
    "Two Pointer Technique", "Binary Search Basics", "Binary Search on Answer",
    "Sorting Algorithms (Merge Sort, Quick Sort)", "Hashing and HashMaps",
    "String Manipulation Basics", "String Matching (KMP, Rabin-Karp)",
    "Backtracking Basics", "N-Queens & Sudoku Solver",
    "Heaps and Priority Queues", "Trie Data Structure", "Disjoint Set Union (DSU)",
    "Segment Trees", "Fenwick Trees (Binary Indexed Tree)",
    "Shortest Path (Dijkstra's Algorithm)", "Bellman-Ford Algorithm",
    "Floyd-Warshall Algorithm", "Minimum Spanning Tree (Prim's & Kruskal's)",
    "Topological Sort (Kahn's Algorithm)", "Strongly Connected Components",
    "Bridges and Articulation Points", "Longest Common Subsequence (LCS)",
    "Longest Increasing Subsequence (LIS)", "Matrix Chain Multiplication",
    "DP on Trees", "DP on Bitmasks", "Bit Manipulation Basics",
    "Math for DSA (GCD, Primes)", "Game Theory Basics"
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
# 3. Generate Notes with Gemini API (Now with RETRY Logic)
# ---------------------------
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ API Key is missing! Check your GitHub Secrets.")

api_key = api_key.strip()
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

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

# ✅ NEW: Retry Loop (Tries 3 times if Google is busy)
max_retries = 3
note = None

for attempt in range(max_retries):
    try:
        response = requests.post(
            url,
            json={"contents": [{"parts": [{"text": prompt}]}]},
            headers={"Content-Type": "application/json"}
        )
        
        result = response.json()
        
        # Check for success
        if "candidates" in result:
            note = result["candidates"][0]["content"]["parts"][0]["text"]
            break  # Success! Exit the loop
            
        # Check for specific "Overloaded" error
        if "error" in result:
            error_msg = result['error']['message']
            print(f"⚠️ Attempt {attempt + 1} failed: {error_msg}")
            if "overloaded" in error_msg.lower() or "503" in str(result):
                print("⏳ Waiting 10 seconds before retrying...")
                time.sleep(10)  # Wait 10 seconds
            else:
                # If it's a different error (like Bad Key), crash immediately
                raise Exception(f"❌ Google API Error: {error_msg}")
                
    except Exception as e:
        print(f"⚠️ Network error on attempt {attempt + 1}: {e}")
        time.sleep(5)

# If after 3 tries we still have no note, then fail
if not note:
    raise Exception("❌ Failed to generate note after 3 attempts. Google servers are too busy.")

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