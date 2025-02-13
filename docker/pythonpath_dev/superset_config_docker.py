import logging
import os
import sys
import subprocess

logger = logging.getLogger()

# Allow sqlite to be used 
# via https://github.com/apache/superset/issues/9748
# Superset configuration file
PREVENT_UNSAFE_DB_CONNECTIONS=False

# Add DuckDB setup
def setup_duckdb():
    try:
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install", 
            "duckdb-engine>=0.9.5,<0.10",
            "--quiet"
        ])
        logger.info("DuckDB engine installed successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install DuckDB engine: {e}")
        raise

# Install DuckDB when config is loaded
setup_duckdb()

# Update DuckDB configuration to use existing mounted volume
DUCKDB_DATA_PATH = "/var/data/duckdb"  # Using the existing mount point
DUCKDB_CONN_PATH = os.getenv("DUCKDB_CONN_PATH", os.path.join(DUCKDB_DATA_PATH, "superset.db"))

# Ensure the directory exists
os.makedirs(DUCKDB_DATA_PATH, exist_ok=True)

# Add DuckDB to the databases dictionary
DATABASES = {
    'duckdb': {
        'allow_csv_upload': True,
        'allow_ctas': True,
        'allow_cvas': True,
        'allow_dml': True,
        'configuration_method': 'sqlalchemy_form',
        'default_driver': 'duckdb',
    }
}

# Add DuckDB to allowed databases
PREFERRED_DATABASES = ['sqlite', 'postgresql', 'duckdb', 'mssql'] 