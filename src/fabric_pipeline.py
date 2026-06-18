from pyspark.sql import DataFrame,functions as F

def silver_sales(df:DataFrame)->DataFrame:
 return (df.dropDuplicates(["sale_id"]).filter((F.col("quantity")>0)&(F.col("unit_price")>=0))
  .withColumn("sale_date",F.to_date("sale_ts")).withColumn("revenue",F.round(F.col("quantity")*F.col("unit_price"),2)))
def gold_daily(df:DataFrame)->DataFrame:
 return df.groupBy("sale_date","store_id").agg(F.sum("revenue").alias("revenue"),F.sum("quantity").alias("units"))