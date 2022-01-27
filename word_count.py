from pyspark import SparkContext
# # Create SparkSession and sparkcontext
# for pyspark
sc = SparkContext()
# # The WordCounts Spark program
textFile = sc.textFile("datafile.txt")
wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word:     (word, 1)).reduceByKey(lambda a, b: a+b)
wordCounts.saveAsTextFile('output')







