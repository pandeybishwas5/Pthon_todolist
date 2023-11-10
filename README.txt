# Python TodoList

Welcome to the Python TodoList repository! This project is designed to help you manage your tasks efficiently.
It uses build automation to create a script to compile and test the
application as well as making a deployable package or executable for the application

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

git clone https://github.com/pandeybishwas5/Python_todolist.git

### 2. Navigate to the Working Directory

cd Python_todolist

### 3. Run the Build Script

python build.py

### 4. Run Application

python main.py

#The application will run on 
http://127.0.0.1:5000


#The build script automates the installation of required dependencies, packages the application, and runs tests.
#Note that one test intentionally fails as part of the project

Troubleshooting
If the build script encounters issues, you can follow these manual steps:

### 1. Remove Existing Virtual Environment

rm -r venv

### 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Linux or MacOS
venv\Scripts\activate      # On Windows (use 'source venv/Scripts/activate' with Git Bash)


### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Tests

pytest tests

### 5. Run Application

python main.py

#The application will run on 
http://127.0.0.1:5000