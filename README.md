# micropython-template

This is a template project for MicroPython projects. 

- use mpremote to upload code to the device
- linting using pylance or pyright
- code formatting using black and isort 

## Setup after cloning this repo for VSCode 

1. Open the repo using VSCode `code .`
2. Edit `requirements-dev.txt` to select the micropython `port` and version you want to develop for.
3. Create a virtual environment for the project	
    - using VSCode `F1 or Ctrl-Shift-P`  
      - `Python: Create Environment` 
      - Select the `venv` environment tyep and the Python interpreter 
      - Select the requirements-dev.txt file.
    - or manually using:
      - `python -m venv .venv`
      - Activate the virtual environment using `source .venv/bin/activate` (Linux) or `.venv\Scripts\activate` (Windows)
      - `pip install -r requirements-dev.txt`
4. 