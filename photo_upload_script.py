import os
from dotenv import load_dotenv
from azure.storage.blob import BlobClient

from iptcinfo3 import IPTCInfo

load_dotenv(".env")
# Aseta tiedot
local_folder = os.getenv('LOCAL_FOLDER')

#käydään läpi kuvat
for filename in os.listdir(local_folder):
    file_path = os.path.join(local_folder, filename)


    if os.path.isfile(file_path) and filename.lower().endswith(('.jpeg','.jpg','.png')):
      identification_code = None

      #etsitään identifiointi koodi
      try:
        info = IPTCInfo(file_path)
        identification_code = info['object name'].decode("utf-8")
          
      except Exception as e:
        print(f"⚠️ EXIF-luku epäonnistui tiedostolle {filename}: {e}")
        #asetetaaan identifikaatioksi kuvan nimi, ehkä kandee muutta ajaksi tai lisätä aika metadataan
        identification_code=filename
        
      # Luo blobin URL
    blob_name = filename
    blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    blob_client = BlobClient.from_blob_url(blob_url)
    
    with open(file_path, "rb") as data:
      metadata = {
              "identification_code": identification_code,
              "category": "Photoboot_test",
              "uploaded_by": "Otto"
          }
      blob_client.upload_blob(data, overwrite=True, metadata=metadata)

    print(f"✅ Tiedosto {filename} with identification_code: {identification_code} ladattu")