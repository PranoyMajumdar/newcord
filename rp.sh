#!/bin/bash

# Find and remove all __pycache__ folders in the current directory and its subdirectories
find . -type d -name "__pycache__" -exec rm -r {} \;

echo "All __pycache__ folders and their contents have been removed."