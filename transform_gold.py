from pyspark.sql import SparkSession

from config.config import *

spark = SparkSession.builder.appName("Gold").getOrCreate()

gold = (
    spark.read
    .format("delta")
    .load(SILVER_PATH)
    .select(
        "chapter_id",
        "chapter_name",
        "city",
        "state",
        "longitude",
        "latitude",
        "dq_status",
        "dq_warning"
    )
)

gold.write.format("delta").mode("overwrite").save(GOLD_PATH)