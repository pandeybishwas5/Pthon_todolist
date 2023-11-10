# build.py
import subprocess
import sys

# Install pytest and setuptools
def install_dependencies():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pytest", "setuptools"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def run_tests():
    try:
        subprocess.run([sys.executable, '-m', 'pytest', 'tests'])
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        sys.exit(1)

def build_package():
    try:
        subprocess.run([sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])
    except subprocess.CalledProcessError as e:
        print(f"Error building package: {e}")
        sys.exit(1)

if __name__ == '__main__':
    install_dependencies()
    run_tests()
    build_package()