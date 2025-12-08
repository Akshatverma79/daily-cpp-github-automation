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

topic = random.choice(topics)
explanation = random.choice(explanations)
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"""

## 🧠 {topic}

🕒 {time_now}

{explanation}

### Example
```cpp
#include <iostream>
using namespace std;

int main() {{
    cout << "Daily C++ practice builds mastery!";
    return 0;
}}
```

---
"""

with open("cpp_notes.md", "a", encoding="utf-8") as file:
    file.write(content)
