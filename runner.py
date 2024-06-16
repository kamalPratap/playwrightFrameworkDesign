import os
import subprocess
import time

current_work_dir = os.getcwd()
# Install dependency
os.system('python -m pip install --upgrade pip')
os.system("python -m pip install -r " + os.path.join(current_work_dir, "requirements.txt"))

time.sleep(10)
subprocess.run(["pytest --headed --template=html1/index.html --report=report.html"])