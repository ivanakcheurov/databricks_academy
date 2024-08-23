# Databricks notebook source
# MAGIC %md
# MAGIC ### another cell

# COMMAND ----------

# Import necessary libraries
import seaborn as sns
import pandas as pd
from pyspark.sql import SparkSession

# Load the Iris dataset from seaborn
iris_pd = sns.load_dataset('iris')

# Convert the pandas DataFrame to a Spark DataFrame
iris_df = spark.createDataFrame(iris_pd)

# Display the Iris dataset
display(iris_df)

# COMMAND ----------

from pyspark.sql import Row

# Create a list of Row objects
cars_list = [Row(make="Toyota", model="Corolla", year=2020), Row(make="Honda", model="Civic", year=2018)]

# Convert the list to a Spark DataFrame
cars_df = spark.createDataFrame(cars_list)

# Display the DataFrame
display(cars_df)
