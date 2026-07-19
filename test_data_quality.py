from pyspark.sql.functions import col


def test_no_invalid_coordinates(gold_df):

    assert gold_df.filter(
        col("longitude").isNull()
    ).count() == 0


def test_warning_exists(silver_df):

    assert silver_df.filter(
        col("dq_status") == "WARNING"
    ).count() > 0