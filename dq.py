from pyspark.sql.functions import *


def quarantine_records(df):

    return df.filter(
        col("longitude").isNull()
        | col("latitude").isNull()
        | (col("longitude") < -180)
        | (col("longitude") > 180)
        | (col("latitude") < -90)
        | (col("latitude") > 90)
    )


def add_warning(df):

    return df.withColumn(
        "dq_warning",
        when(
            col("city").isNull()
            | (trim(col("city")) == "")
            | (upper(col("city")) == "UNKNOWN"),
            "DQ-W1"
        )
    )