import os
import json
import random
from datetime import datetime
import requests

# ---------------------------
# 1. DSA Topic Roadmap
# ---------------------------
dsa_topics = [
    # --- PHASE 1: BASICS & FOUNDATION (Existing) ---
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
    "Sliding Window Techniques",

    # --- PHASE 2: INTERMEDIATE ALGORITHMS ---
    "Two Pointer Technique",
    "Binary Search Basics",
    "Binary Search on Answer",
    "Sorting Algorithms (Merge Sort, Quick Sort)",
    "Hashing and HashMaps",
    "String Manipulation Basics",
    "String Matching (KMP, Rabin-Karp)",
    "Backtracking Basics",
    "N-Queens & Sudoku Solver",
    
    # --- PHASE 3: ADVANCED DATA STRUCTURES ---
    "Heaps and Priority Queues",
    "Trie Data Structure",
    "Disjoint Set Union (DSU)",
    "Segment Trees",
    "Fenwick Trees (Binary Indexed Tree)",
    
    # --- PHASE 4: ADVANCED GRAPHS ---
    "Shortest Path (Dijkstra's Algorithm)",
    "Bellman-Ford Algorithm",
    "Floyd-Warshall Algorithm",
    "Minimum Spanning Tree (Prim's & Kruskal's)",
    "Topological Sort (Kahn's Algorithm)",
    "Strongly Connected Components (Kosaraju/Tarjan)",
    "Bridges and Articulation Points",
    
    # --- PHASE 5: ADVANCED DP & MATH ---
    "Longest Common Subsequence (LCS)",
    "Longest Increasing Subsequence (LIS)",
    "Matrix Chain Multiplication",
    "DP on Trees",
    "DP on Bitmasks",
    "Bit Manipulation Basics",
    "Math for DSA (GCD, Primes, Sieve of Eratosthenes)",
    "Game Theory Basics"
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

# Clean the key (remove accidental spaces)
api_key = api_key.strip()

# ✅ UPDATED MODEL: Using gemini-2.5-flash which we confirmed is available
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

response = requests.post(
    url,
    json={"contents": [{"parts": [{"text": prompt}]}]},
    headers={"Content-Type": "application/json"}
)

result = response.json()

# Error Handling: Check if Google sent an error
if "error" in result:
    raise Exception(f"❌ Google API Error: {result['error']['message']}")

# Extract the note
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