import os

os.system("sh install_conda.sh")
os.system("sh install_env.sh")
os.system("conda activate codiff && python server.py")