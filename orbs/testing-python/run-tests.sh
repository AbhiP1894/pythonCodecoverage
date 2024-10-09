#!/bin/bash

# Check if test directory is provided
TEST_DIR=${1:-tests}

echo "Running tests in directory: $TEST_DIR"
mkdir -p test-results  # Create results directory
python -m unittest discover -s $TEST_DIR -p "*.py" -v | tee test-results/unittest_results.log
