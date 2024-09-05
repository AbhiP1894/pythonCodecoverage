# Python-Unittest-Code-Coverage-Example

To render codecoverage report for unittest framework on sonarqube dashboard byscript

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

OR

To render codecoverage report for unittest framework on sonarqube dashboard byscript by manually
```
coverage run -m unittest discover -s tests -p "*.py"
coverage report
coverage xml
sonar-scanner
```



