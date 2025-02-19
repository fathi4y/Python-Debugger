# 🛠️ AI-Powered Bug Detection Tool

This Python script detects syntax errors and critical issues in Python code using `ast` and `pylint`.  
It provides a **quick and lightweight** way to analyze Python code for potential bugs.  

## 🚀 Features
- **Syntax Checking**: Uses Python's built-in `ast` module to catch syntax errors.
- **Static Code Analysis**: Runs `pylint` with error (`E`) checks enabled.
- **User-Friendly Output**: Clear error messages with line numbers and emoji indicators.
- **Temporary File Handling**: Automatically cleans up after analysis.

---

## 📌 How It Works
1. **Checks for syntax errors** using the `ast` module.
2. **Writes the code to a temporary file** (`temp_script.py`).
3. **Runs `pylint`** on the file to detect static errors.
4. **Deletes the temporary file** to keep the system clean.

---

## 🔧 Installation
Make sure you have Python installed. You also need `pylint`:  

```sh
pip install pylint
```

---

## 🏷️ Usage
Save the script as `bug_detector.py` and run it:

```sh
python bug_detector.py
```

### Example Code Check:
```python
sample_code = """
def add_numbers(a, b)
    return a + b
"""
```
Output:
```
🔍 Checking syntax...
❌ Syntax Error: invalid syntax (Line 2, Column 22)

🚀 Running pylint...
❌ Error: Pylint is not installed or not found. Install it using `pip install pylint`.
```

---

## 🛠️ Implementation Details
### ✅ **Syntax Checking (`ast`)**
- The script uses `ast.parse()` to detect syntax errors **without running the code**.
- This prevents accidental execution of malicious code.

### ✅ **Static Code Analysis (`pylint`)**
- `pylint` runs only **error (`E`) checks** for a **focused bug detection** approach.
- The script disables all other checks (`--disable=all`).
- If `pylint` is **not installed**, the script provides a **clear error message**.

### ✅ **Temporary File Handling**
- Code is written to `temp_script.py` to allow `pylint` to analyze it.
- The file is **deleted** after analysis to **prevent clutter**.

---

## ⚠️ Limitations
- ❌ **Does not catch runtime errors** (`ZeroDivisionError`, `NameError`, etc.).
- ❌ **Relies on `pylint`**, which must be installed separately.
- ❌ **Only detects critical errors (`E`)**—warnings and best practices are not checked.
- ❌ **Slightly slower due to file writing**, but ensures compatibility with `pylint`.

---

## 🔮 Future Improvements
✅ **Extend to Full Static Analysis**: Enable warnings (`W`) and conventions (`C`).  
✅ **Detect Runtime Errors**: Use `exec()` in a sandboxed environment.  
✅ **Web or GUI Integration**: Build a **VS Code extension** or **web-based tool**.

---

## 🎯 Conclusion
This **lightweight** bug detection tool helps developers **quickly catch syntax and static errors** before execution.  
It’s perfect for **automated code reviews, debugging, and CI/CD integration**.

🚀 **Next Steps**: Expand to detect **runtime errors** and provide **AI-powered fixes**.

---
📌 **Author**: Fathi Ali
📅 **Last Updated**: February 2025  
🔗 **License**: MIT  

