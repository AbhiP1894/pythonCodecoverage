#!/bin/bash

set -euo pipefail

servicesPath="./tests/myFunction_test"
#controllerPath="./test/controller"
exit_code=0

coverage erase

if [ -d "$servicesPath" ]; then
    echo "Running services tests..."
    coverage run --parallel-mode --source utils,services -m unittest discover -s "$servicesPath"
else
    echo "Services test directory not found: $servicesPath"
fi

# if [ -d "$controllerPath" ]; then
#     echo "Running controller tests..."
#     coverage run --parallel-mode --source controller -m unittest discover -s "$controllerPath"
# else
#     echo "Controller test directory not found: $controllerPath"
# fi

echo "Combining Coverages..."
coverage combine

coverage report

echo "Generating htmlcov files....."

#coverage html
coverage xml

exit $exit_code