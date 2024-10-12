# py4j-app
A high TPS (1000 per sec) python application decrypts payload of each transaction using a java decrypter jar

# steps to execute
1. run: `mvn clean package` to build the JAR will be in the target directory, named decryptor-1.0.0.jar
2. python load.py "your_encrypted_payload" "your_bq_project.your_bq_dataset.your_bq_table"



