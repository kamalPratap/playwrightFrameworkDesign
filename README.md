# playwrightFrameworkDesign
playwrightFrameworkDesign
# update pip using below command
python.exe -m pip install --upgrade pip
# Intall all the prerequisit using requiremenrt txt file
pip install -r requirements.txt
# Run test with default browser i.e Chromium browser that also create report
pytest --headed --template=html1/index.html --report=report.html