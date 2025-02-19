# 🛠️ Python Code Bug Detection Tool

This script detects **syntax errors** and **static code issues** in Python using `ast` and `pylint`.  
It is a lightweight tool for **quick debugging and automated checks** before execution.

---

## 🚀 Features

✔ **Syntax Checking**: Detects syntax errors without running the code.  
✔ **Static Code Analysis**: Uses `pylint` to detect major issues.  
✔ **Automatic File Cleanup**: Prevents clutter by deleting temporary files.  
✔ **User-Friendly Output**: Clear messages with line numbers and emoji indicators.  
✔ **Lightweight & Fast**: No external dependencies except `pylint`.  

---

## 📌 How It Works

1. **Checks for syntax errors** using Python’s built-in `ast` module.  
2. **Writes the code to a temporary file** (`temp_script.py`).  
3. **Runs `pylint`** to detect major errors.  
4. **Deletes the temporary file** after analysis.  

---

## 🔧 Installation

You need Python installed. Install `pylint` if you haven't already:

```sh
pip install pylint
