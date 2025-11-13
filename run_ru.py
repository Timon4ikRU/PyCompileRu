from pycompileru import compile_file
import sys
import os
import subprocess

def run_russian_file(ru_file):
    """Compiles and runs Russian .ru.py file"""
    if not ru_file.endswith('.ru.py'):
        print(f"Error: {ru_file} must be .ru.py file")
        return
    
    # First compile Russian code to Python
    py_file = compile_file(ru_file)
    
    # Then execute the compiled Python file using python3
    try:
        subprocess.run(["python3", py_file])
    except FileNotFoundError:
        print("Error: python3 not found. Trying python...")
        subprocess.run(["python", py_file])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_russian_file(sys.argv[1])
    else:
        print("Usage: python3 run_ru.py program.ru.py")
