from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import DoubleType

from dq import quarantine_records, add_warning
from config.config import *

spark = SparkSession.builder.appName("Silver").getOrCreate()

bronze = spark.read.format("delta").load(BRONZE_PATH)

silver = (
    bronze
    .withColumn("longitude", col("longitude").cast(DoubleType()))
    .withColumn("latitude", col("latitude").cast(DoubleType()))
    .dropDuplicates(["chapter_id"])
)

quarantine = quarantine_records(silver)

silver = silver.join(
    quarantine.select("chapter_id"),
    "chapter_id",
    "left_anti"
)

silver = add_warning(silver)

silver = silver.withColumn(
    "dq_status",
    when(col("dq_warning").isNull(), "OK")
    .otherwise("WARNING")
)

silver.write.format("delta").mode("overwrite").save(SILVER_PATH)

quarantine.write.format("delta").mode("overwrite").save(QUARANTINE_PATH)