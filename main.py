import ast
import subprocess
import os


def check_syntax(code: str) -> str:
    """Check syntax errors using the ast module."""
    try:
        ast.parse(code)
        return "✅ No syntax errors detected."
    except SyntaxError as e:
        return f"❌ Syntax Error: {e.msg} (Line {e.lineno}, Column {e.offset})"


def run_pylint(code: str) -> str:
    """Run pylint on the given code to detect issues."""
    temp_file = "temp_script.py"
    
    try:
        # Save code to a temporary file
        with open(temp_file, "w") as f:
            f.write(code)

        # Run pylint on the temporary file
        result = subprocess.run(
            ["python3", "-m", "pylint", temp_file, "--disable=all", "--enable=E"],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() if result.stdout else "✅ No pylint errors detected."
    
    except FileNotFoundError:
        return "❌ Error: Pylint is not installed or not found. Install it using `pip install pylint`."
    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)


if __name__ == "__main__":
    sample_code = """ 
def add_numbers(a, b)
    return a + b
    """
    
    print("🔍 Checking syntax...")
    print(check_syntax(sample_code))
    
    print("\n🚀 Running pylint...")
    print(run_pylint(sample_code))
