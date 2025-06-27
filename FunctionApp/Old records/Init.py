import logging
import azure.functions as func
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient
import json
import datetime

def main(mytimer: func.TimerRequest) -> None:
    cosmos_client = CosmosClient("<COSMOS-URI>", credential="<KEY>")
    database = cosmos_client.get_database_client("<DATABASE>")
    container = database.get_container_client("<CONTAINER>")

    blob_service_client = BlobServiceClient.from_connection_string("<BLOB-CONNECTION-STRING>")
    container_client = blob_service_client.get_container_client("billing-archive")

    cutoff_date = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).isoformat()

    for item in container.query_items(
        query=f"SELECT * FROM c WHERE c.date < '{cutoff_date}'",
        enable_cross_partition_query=True
    ):
        blob_name = f"{item['id']}.json"
        container_client.upload_blob(blob_name, json.dumps(item), overwrite=True)
        container.delete_item(item, partition_key=item['partitionKey'])
      
