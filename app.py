import os
import subprocess

subprocess.call(["bash", "install_conda.sh"])
os.system("sh install_env.sh")
os.system("conda activate codiff && python server.py")
