# Python-Unittest-Code-Coverage-Example


**Step:**

1. install package nose and mock by command
```
pip install -r requirements.txt
```
2. run test by command    
```
nosetest tests
```
3. run bash file
```
./bash.sh
```
To generate codecoverage report for unittest framework on sonarqube dashboard
```
coverage run -m unittest discover -s "$servicesPath" -p "*.py"
coverage report
coverage xml
sonar-scanner
```



