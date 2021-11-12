from time import time
import numpy as np
from random import random
from operator import add

from pyspark.sql import SparkSession


def naive_method_time(n):
    inside = 0

    t_0 = time()
    for _ in range(n):
        x, y = random(), random()
        if x**2 + y**2 < 1:
            inside += 1
    return(np.round(time()-t_0, 3))


def spark_method_time(n):

    def is_point_inside_unit_circle(p):
        x, y = random(), random()
        return 1 if x*x + y*y < 1 else 0

    t_0 = time()

    sc.parallelize(range(0, n)) .map(is_point_inside_unit_circle).reduce(add)
    return(np.round(time()-t_0, 3))


N = [100000, 100000000, 100000000000, 100000000000000]

N = [10000000, 100000000, 200000000]


time_native = []
time_spark = []

spark = SparkSession.builder.master(
    'spark://spark:7077').appName('CalculatePi').getOrCreate()
sc = spark.sparkContext

for n in N:
    time_native.append(naive_method_time(n))
    time_spark.append(spark_method_time(n))

spark.stop()

print('time native', time_native)
print('time spark', time_spark)
