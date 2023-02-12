#!/bin/bash

# Check if Homebrew is already installed
if [ -z "$(which brew)" ]; then
  echo "Homebrew is not installed. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
else
  echo "Homebrew is already installed."
fi

# Install Python using Homebrew
brew install python3

# Verify the installation
python3 --version

## chmod +x ipython.sh && ./ipython.sh && pip install -r requirements.txt && python3 HealthPyProcess.py