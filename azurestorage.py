from datetime import datetime, timedelta
import io
import os
import sys
import time
from azure.storage.fileshare import ShareServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions,ShareClient,ShareFileClient
import config

sas_token = generate_account_sas(
    account_name=config._STORAGE_ACCOUNT_NAME,
    account_key=config._STORAGE_ACCOUNT_KEY,
    resource_types=ResourceTypes(service=True),
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)

share_service_client = ShareServiceClient(account_url="https://"+config._STORAGE_ACCOUNT_NAME+".file.core.windows.net", credential=sas_token)


connection_string = "DefaultEndpointsProtocol=https;AccountName="+config._STORAGE_ACCOUNT_NAME+";AccountKey="+config._STORAGE_ACCOUNT_KEY+";EndpointSuffix=core.windows.net"
service = ShareServiceClient.from_connection_string(conn_str=connection_string)

dict_properties=[]
dict_properties = service.get_service_properties()
print(dict_properties)

share = ShareClient.from_connection_string(conn_str=connection_string, share_name="rrd-share")
#share.create_share()

file_client = ShareFileClient.from_connection_string(conn_str=connection_string, share_name="rrd-share", file_path="rrd-file")

with open(os.path.join(sys.path[0], 'taskdata0.txt'), "rb") as source_file:
    file_client.upload_file(source_file)