from dagster import Definitions, load_assets_from_modules
from dagster_duckdb_pandas import DuckDBPandasIOManager

from . import assets

all_assets = load_assets_from_modules([assets])
database_io_manager = DuckDBPandasIOManager(database="analytics.csv_example")

defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": database_io_manager,  # Define the I/O manager here
    }
)