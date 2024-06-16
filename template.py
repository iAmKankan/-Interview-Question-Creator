import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  # program starting information

list_of_files= [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) # To avoid collisions with windows file paths and unix/linux file paths; 'Path' will detect the OS autometically
    filedir,filename= os.path.split(filepath) # we need to separate the directories from the files; split() returns head and tail of filepath 

# Create foalders
    if filedir!="": # if the variable is not empty, then
        os.makedirs(filedir, exist_ok=True) # making directory
        logging.info(f"Created directory {filedir} for the files{filename}")  # program starting output

# Create files with filepath   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
       with open(filepath,"w") as f:
          pass
          logging.info(f"Created file {filepath}")
    else:
        logging.info(f"File {filepath} already exists")
