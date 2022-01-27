Please follow these steps to run the spark job
1. sudo service docker start
2. Go to Pyspark shell: pyspark
3. Run the code from word_count.py inside pyshark shell
4. For submitting the spark job run :  spark-submit --master local word_count.py

## Prerequisite for running this demo    
The following tools needs to be installed in your machine         
- JDK 11     
- Scala : https://www.scala-lang.org/download/     
- Spark 3.2.0 : https://spark.apache.org/downloads.html     

## About the demo     
The Spark application that reads the text from datafile.txt file
and generates an output file with total count for each word. The output will be generated in output folder after running this application.

      
## How to run this example?    
## To run this example using docker, do the following
Here are the various ways:    
## To run this example in spark local mode, do the following
```
1. sudo service docker start
2. Go to Pyspark shell: pyspark
3. Run the code from word_count.py inside pyshark shell
4. For submitting the spark job run :  spark-submit --master local word_count.py 
```


