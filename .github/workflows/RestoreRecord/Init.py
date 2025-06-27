# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    record_id = req.route_params.get('id')
    blob_service_client = BlobServiceClient.from_connection_string("<BLOB-CONNECTION-STRING>")
    container_client = blob_service_client.get_container_client("billing-archive")
    
    try:
        blob_client = container_client.get_blob_client(f"{record_id}.json")
        blob_data = blob_client.download_blob().readall()
        return func.HttpResponse(blob_data, mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Record not found: {str(e)}", status_code=404)
