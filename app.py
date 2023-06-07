import os
import subprocess

subprocess.call(["bash", "install_conda.sh"])
subprocess.call(["bash", "install_env.sh"])
subprocess.call(["bash", "conda activate codiff && python server.py"])
