import requests
import pandas as pd  # Add new imports to the top of `assets.py`

from io import StringIO

from dagster import (
    AssetExecutionContext,
    MetadataValue,
    asset,
    get_dagster_logger,
)


@asset
def test_csv(
    context: AssetExecutionContext,
) -> pd.DataFrame:  # modify return type signature
    logger = get_dagster_logger()
    test_csv_url = "https://raw.githubusercontent.com/vmware/versatile-data-kit/main/examples/ingest-csv-file-example/csv_example.csv"
    # broken_csv_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    input = StringIO(requests.get(test_csv_url).text)
    df = pd.read_csv(input)
    df.dropna(how="all", inplace=True)

    context.add_output_metadata(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        }
    )
    return df
    
