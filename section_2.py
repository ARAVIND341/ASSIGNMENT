from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local[*]").getOrCreate()
print("Spark:", spark.version)
spark.range(5).show()
spark.stop()