import subprocess
import sys
import os
import json
from google.colab import drive

def install_private_library(path_to_config, repo_name, branch='main'):
    with open(path_to_config, 'r') as f:
        github_config = json.load(f)
        access_token = github_config['access_token']
        username = github_config['username']
    # TODO add branch stuff, add gitlab functionality
    git_link = f'git+https://{access_token}@github.com/{username}/{repo_name}.git@{branch}'
    try:
      output = subprocess.check_output([sys.executable, '-m', 'pip', 'install', git_link]) # security risk, output not encrypted
    except subprocess.CalledProcessError as e:
      # TODO improve security
      e.cmd[-1] = e.cmd[-1].replace(access_token, '****')
      raise e

def install_tradegpt_ai():
    drive.mount('/content/drive')
    drive_path = "/content/drive/MyDrive/"
    ## NEED THIS FILE TO WOKR!!!
    path_to_json = "GithubToken/git_access_token.json"
    git_access_token_json_path = os.path.join(drive_path, path_to_json)
    install_private_library(git_access_token_json_path, "tradegpt-ai")
    print("from tradegptlib.util.colab_helper_functions import copy_model")