from pyspark import SparkContext
# # Create SparkSession and sparkcontext
# from pyspark.sql import SparkSession
#
# def main():
#    spark = SparkSession.builder\
#                        .master("local")\
#                        .appName('SparkWordCount')\
#                        .getOrCreate()
#    sc=spark.sparkContext
# #    sc = SparkContext(appName='SparkWordCount')
#    input_file = sc.textFile('datafile.txt')
#    counts = input_file.flatMap(lambda line: line.split()) \
#                      .map(lambda word: (word, 1)) \
#                      .reduceByKey(lambda a, b: a + b)
#    counts.saveAsTextFile('output')
#
#    sc.stop()
#
# if __name__ == '__main__':
#    main()


# for pyspark
sc = SparkContext()
# # The WordCounts Spark program
textFile = sc.textFile("datafile.txt")
wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word:     (word, 1)).reduceByKey(lambda a, b: a+b)
wordCounts.saveAsTextFile('output')







