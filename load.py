import subprocess
import json
from google.cloud import bigquery

def decrypt_payload(encrypted_payload):
    # Prepare the command to run the Java JAR with Shenandoah GC
    command = [
        'java',
        '-XX:+UseShenandoahGC',
        '-XX:+UnlockExperimentalVMOptions',
        '-jar',
        'decrypter.jar',
        encrypted_payload
    ]

    # Run the Java process and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Handle errors if the Java process fails
    if process.returncode != 0:
        raise Exception(f"Java Error: {stderr.decode()}")

    # Parse the JSON output from Java (assuming it returns JSON data)
    decrypted_data = json.loads(stdout.decode())
    return decrypted_data

def save_to_bigquery(decrypted_data, table_id):
    client = bigquery.Client()
    table = client.get_table(table_id)
    
    # Convert decrypted data to BigQuery compatible format
    rows_to_insert = [decrypted_data]  # assuming decrypted_data is a dictionary

    # Insert rows into BigQuery
    errors = client.insert_rows_json(table, rows_to_insert)
    if errors:
        raise Exception(f"BigQuery Error: {errors}")

def process_transaction(encrypted_payload, table_id):
    decrypted_data = decrypt_payload(encrypted_payload)
    save_to_bigquery(decrypted_data, table_id)
    print("Data saved to BigQuery successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt payload and save to BigQuery")
    parser.add_argument("encrypted_payload", help="The encrypted payload to decrypt")
    parser.add_argument("bigquery_table_id", help="BigQuery table ID where decrypted data should be saved")

    args = parser.parse_args()
    encrypted_payload = args.encrypted_payload
    bigquery_table_id = args.bigquery_table_id

    process_transaction(encrypted_payload, bigquery_table_id)
