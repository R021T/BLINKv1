echo "BUILD START"

# Create virtual environment
python3.9 -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt

# Set MARIADB_CONFIG environment variable
export MARIADB_CONFIG="\mysql_config.pl"  # Replace with the correct path

echo "BUILD END"
