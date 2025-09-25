import os
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_container_sas, ContainerSasPermissions, BlobClient
from dotenv import load_dotenv, set_key

load_dotenv(".env")

#This generate the SAS Token for 12 hours

sas_token = generate_container_sas(
    account_name=os.getenv('ACCOUNT_NAME'),
    container_name=os.getenv('CONTAINER_NAME'),
    account_key=os.getenv('ACCOUNT_KEY'),
    permission=ContainerSasPermissions(read=True, write=True, list=True, add=True, create=True),
    expiry=datetime.utcnow() + timedelta(hours=12)
)

set_key('.env','SAS_TOKEN', 'lolerones')