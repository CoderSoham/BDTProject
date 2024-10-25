
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder \
    .appName("Credit Card Fraud Detection") \
    .getOrCreate()

df = spark.read.csv("creditcard.csv", header=True, inferSchema=True)

df.printSchema()

df = df.dropna()

df.groupBy("Class").count().show()

df = df.withColumn("new_feature", col("V1") - col("V2"))  

feature_columns = [col for col in df.columns if col not in ["Class"]]  
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
df = assembler.transform(df)

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(featuresCol='features', labelCol='Class')
model = lr.fit(train_df)

predictions = model.transform(test_df)

evaluator = BinaryClassificationEvaluator(labelCol="Class")
accuracy = evaluator.evaluate(predictions)
print(f"Model Accuracy: {accuracy}")

predictions.select("features", "Class", "prediction").show()

model.write().overwrite().save("fraud_detection_model_spark")

spark.stop()
