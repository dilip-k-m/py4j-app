# py4j-app
A high TPS (1000 per sec) python application decrypts payload of each transaction using a java decrypter jar

# steps to execute
1. run: `mvn clean package` to build the JAR will be in the target directory, named decryptor-1.0.0.jar
2. `python decrypt_and_save.py "your_encrypted_payload" "your_project.your_dataset.your_table"`




