import random
from datetime import datetime

topics = [
    "C++ Variables and Data Types",
    "Pointers and Memory Management",
    "Difference between Stack and Heap",
    "Object-Oriented Programming Concepts",
    "Constructors and Destructors",
    "Virtual Functions and Polymorphism",
    "Pass by Value vs Pass by Reference",
    "STL: vector, map, set",
    "Exception Handling in C++",
    "Namespaces and Their Importance"
]

explanations = [
    "This concept plays a crucial role in efficient C++ programming.",
    "Understanding this helps avoid memory leaks and segmentation faults.",
    "It is frequently used in real-world and competitive programming.",
    "This improves code structure and maintainability.",
    "A strong grasp of this topic makes debugging much easier."
]

intros = [
    "Today I focused on",
    "I spent time understanding",
    "Revising the concept of",
    "Learning about",
    "Exploring"
]

# ✅ Learning progression
day = datetime.now().day
if day <= 10:
    level = "Beginner"
elif day <= 20:
    level = "Intermediate"
else:
    level = "Advanced"

# ✅ Variable content size
sentence_count = random.randint(1, 3)

topic = random.choice(topics)
base_explanation = random.choice(explanations)

explanation = ""
for _ in range(sentence_count):
    explanation += base_explanation + " "

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"""

## 🧠 Level: {level}
### Topic: {topic}

{random.choice(intros)} {topic}. {explanation}

🕒 {time_now}

### Example
```cpp
#include <iostream>
using namespace std;

int main() {{
    cout << "Daily C++ practice builds mastery!";
    return 0;
}}
---
"""

with open("cpp_notes.md", "a", encoding="utf-8") as file:
    file.write(content)
