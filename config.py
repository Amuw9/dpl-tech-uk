BRONZE_PATH = "data/bronze"
SILVER_PATH = "data/silver"
GOLD_PATH = "data/gold"
QUARANTINE_PATH = "data/quarantine"

SOURCE_SYSTEM = "ArcGIS"

API_URL = "https://services.arcgis.com/example/FeatureServer/0/query"

API_PARAMS = {
    "where": "STATE IN ('CA','OR','WA')",
    "outFields": "*",
    "f": "json"
}