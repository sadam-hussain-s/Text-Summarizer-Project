import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = {
    ".github.com/workflows/.gitkeep",
        #In this folder, we have yaml file related to CI CD deployment. 
        #If we commit the code in github then it will automatically do deployment. 
        #Empty folder won't be uploaded that's why we create .gitkeep file.
    f"src/{project_name}/__init__.py", #init file indicates that it is local package.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", #used to create config related thing. yaml file is superset of JSON file.
    "params.yaml", #used to create parameters
    "app.py",
    "main.py", #this is main file 
    "Dockerfile", 
    "requirements.txt", #this file have the all requirements like library or enviroment setup
    "setup.py",
    "research/trials.ipynb" #To do some experimental codes
}


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists")

