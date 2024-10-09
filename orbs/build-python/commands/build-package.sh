#!/bin/bash

echo "Building Python package..."

# Ensure the requirements are installed
pip install build

# Build the package
python -m build

echo "Package built successfully!"
