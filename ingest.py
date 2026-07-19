from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit

from utils import fetch_api_data
from logger import logger
from config.config import *

spark = (
    SparkSession.builder
    .appName("BronzeLayer")
    .getOrCreate()
)

data = fetch_api_data()

df = spark.createDataFrame(data)

bronze = (
    df
    .withColumn("ingest_timestamp", current_timestamp())
    .withColumn("source_system", lit(SOURCE_SYSTEM))
)

bronze.write.format("delta").mode("overwrite").save(BRONZE_PATH)

logger.info("Bronze layer created successfully.")