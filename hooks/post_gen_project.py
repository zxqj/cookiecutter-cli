import os
import subprocess
import sys

def main():
    project_dir = os.getcwd()
    venv_dir = os.path.join(project_dir, "venv")
    prompt = "{{cookiecutter.hyphenated}}"

    # Create the virtual environment
    subprocess.run([sys.executable, "-m", "venv", "--prompt", prompt, venv_dir], check=True)

    # Activate the virtual environment
    if os.name == "nt":  # Windows
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:  # Unix-based systems
        activate_script = os.path.join(venv_dir, "bin", "activate")

    # Install the required packages
    pip_executable = os.path.join(venv_dir, "bin", "pip") if os.name != "nt" else os.path.join(venv_dir, "Scripts", "pip")
    subprocess.run([pip_executable, "install", "--upgrade", "pip"], check=True)
    subprocess.run([pip_executable, "install", "click", "sh", "PyYAML", "rich"], check=True)

if __name__ == "__main__":
    main()
