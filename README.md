# 🚀 Automated C++ & DSA Learning Tracker

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-blue?logo=github-actions)
![C++](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B)
![Gemini AI](https://img.shields.io/badge/Powered_by-Gemini_AI-8E75B2?logo=google-gemini)

## 📖 Overview
This repository serves as an **automated daily learning log** for Data Structures and Algorithms (DSA) in C++. 

It leverages **GitHub Actions** and **Google's Gemini AI** to generate concise, high-quality study notes, code snippets, and explanations for various DSA topics. The system automatically commits these updates to the repository twice a day, maintaining an active and consistent contribution graph.

## ⚙️ How It Works
The automation pipeline runs on a scheduled cron job (**2 times daily**) and performs the following steps:

1.  **Topic Selection:** The script reads a `progress.json` file to pick the next topic from a curated DSA roadmap (e.g., *Arrays, Linked Lists, DP, Graphs*).
2.  **AI Generation:** It sends a prompt to the **Gemini 2.5 Flash API**, requesting a definition, importance, and a C++ code example for the topic.
3.  **Note Logging:** The generated content is appended to `cpp_notes.md`.
4.  **Smart Commits:** The system commits the changes with a randomized message (e.g., *"Learned a new DSA concept"*) and pushes them to the repository.
5.  **Progress Tracking:** The `progress.json` index is incremented to ensure the next run covers a new topic.

## 🛠️ Tech Stack
* **Automation:** GitHub Actions (Ubuntu Runner)
* **Scripting:** Python 3 (`requests`, `json`, `os`)
* **AI Engine:** Google Gemini 2.5 Flash
* **Version Control:** Git (Automated Pull/Rebase/Push)

## 📅 Schedule
The workflow is configured to trigger automatically at the following times:
* **Morning:** 11:30 AM IST (06:00 UTC)
* **Evening:** 07:20 PM IST (13:50 UTC)

## 📂 Repository Structure
* `cpp_notes.md`: The main file containing the accumulated learning notes.
* `notes_generator.py`: The Python script responsible for AI interaction and file handling.
* `.github/workflows/daily-activity.yml`: The configuration file for the automation schedule.
* `progress.json`: Tracks the current position in the DSA roadmap.

---
*Created by [Akshat Verma](https://github.com/Akshatverma79)*