echo "BUILD START"

# Set MARIADB_CONFIG environment variable
export MARIADB_CONFIG="C:\\Program Files\\MariaDB 11.2\\bin\\mysql_config.pl"

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
python -m pip install -r requirements.txt

echo "BUILD END"
