# IR-Lab1
(by Krishna Kalyan and Sebastian Stobiecki)

To create an index run the following command 

`export CLASSPATH=lucene-core-3.6.2-SNAPSHOT.jar:lucene-demo-3.6.2-SNAPSHOT.jar`
`echo $CLASSPATH`
`java org.apache.lucene.demo.IndexFiles -docs novels`

Check if the indexes are generated well

`java -jar $LUKEDIR/lukeall-3.5.0.jar -index ./index`

