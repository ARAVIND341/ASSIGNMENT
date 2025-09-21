from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
print("Spark started ✓")

# simple test
df = spark.range(5)
df.show()

spark.stop()
