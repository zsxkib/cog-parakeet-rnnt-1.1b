#!/bin/bash

# This script exists to clean up files before we push to Replicate
# Run it before we run `sudo cog push r8.im/zsxkib/...`

# Check if the weights directory exists
if [ -d "./weights" ]; then
    # Remove the directory
    rm -r ./weights
    echo "Weights directory removed."
else
    echo "Weights directory not found."
fi