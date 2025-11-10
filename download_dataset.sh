#!/bin/bash
set -e

echo "📥 Downloading Pima Indians Diabetes dataset from Kaggle..."

# Create a data folder if it doesn't exist
mkdir -p /app/data
cd /app/data

# Download from Kaggle
kaggle datasets download -d uciml/pima-indians-diabetes-database -p .

# Unzip and clean up
unzip -o pima-indians-diabetes-database.zip
rm pima-indians-diabetes-database.zip

echo "✅ Dataset downloaded to /app/data"

