# Azure Medallion Data Product

## Objective

Build a Bronze → Silver → Gold pipeline that ingests university chapter data from a public ArcGIS API and publishes a clean, reliable data product.

## Technologies

- Python
- PySpark
- Delta Lake
- Databricks / Local Spark


## Pipeline

ArcGIS API
↓
Bronze (Raw)
↓
Silver (Validation, Deduplication, DQ)
↓
Gold (Consumer Data Product)

## Data Quality Rules

DQ-Q1
- Invalid coordinates are quarantined.

DQ-W1
- Missing or UNKNOWN city is flagged as WARNING.

## How to Run

python ingest_bronze.py

python transform_silver.py

python transform_gold.py

pytest tests_data_quality.py