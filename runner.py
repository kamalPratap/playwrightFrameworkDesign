import os
import shutil
from datetime import datetime
import time

current_work_dir = os.getcwd()
del_old_report = os.path.join(os.getcwd(), "reports")
if os.path.isdir(del_old_report):
    shutil.rmtree(del_old_report)

current_work_dir = os.getcwd()
# Install dependency
os.system('python -m pip install --upgrade pip')
os.system("python -m pip install -r " + os.path.join(current_work_dir, "requirements.txt"))

# os.system("pytest --headed --template=html1/index.html --report=report.html")

os.system("pytest --headed --template=html1/index.html --report=reports/" + datetime.now().strftime(
    "%d-%m-%Y-%H-%M-%S") + ".html")

time.sleep(5)
# UnInstall dependency
# os.system("python -m pip uninstall -r " + os.path.join(current_work_dir, "requirements.txt") + " -y")
