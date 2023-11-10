# build.py
import subprocess
import sys

def run_tests():
    subprocess.run([sys.executable, '-m', 'pytest', 'tests'])

def build_package():
    subprocess.run([sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])

if __name__ == '__main__':
    run_tests()
    build_package()
