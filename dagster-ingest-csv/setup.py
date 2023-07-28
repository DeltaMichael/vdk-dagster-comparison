from setuptools import find_packages, setup

setup(
    name="dagster_ingest_csv",
    packages=find_packages(exclude=["dagster_ingest_csv_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
