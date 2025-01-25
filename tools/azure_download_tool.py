"""
================================== CONFIDENTIEL - PROTECH © ==================================
@Author: Sijie Hu

@Description: This script is used to download files from Azure Blob Storage through Azure CLI credentials.
@Requirements:
    1. Install Azure CLI: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    2. Install Azure SDK for Python: pip install azure-storage-blob
    3. Install Azure Identity: pip install azure-identity
@Usage:
"""


import os
import time
from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Download files from Azure Blob Storage")
    parser.add_argument("--download_prefix", "-p", type=str, required=True, help="Prefix of the files to download")
    parser.add_argument("--download_suffix", "-s", type=str, default="", help="Suffix of the files to download")
    parser.add_argument("--save_dir", "-o", type=str, required=True, help="Local folder to save the downloaded files")
    parser.add_argument("--replace", "-r", action="store_true", help="Replace the existing files")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # Use Azure CLI credentials (need to login Azure CLI first)
    credential = AzureCliCredential()

    # Fill in the storage account name (replace with your storage account name)
    account_name = "manazgdatasciencedevsto"
    account_url = f"https://{account_name}.blob.core.windows.net"

    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

    # Specify container name and folder prefix
    container_name = "protech"
    download_prefix = args.download_prefix  # e.g. "Dataset_IntegraliteDesDonnees/rosbag2_2025_01"
    local_download_folder = args.save_dir

    # Get container client
    container_client = blob_service_client.get_container_client(container_name)

    # List all blobs with the specified prefix and download
    blob_list = container_client.list_blobs(name_starts_with=download_prefix)

    for blob in blob_list:
        # Check suffix
        if not blob.name.endswith(args.download_suffix):
            continue

        # Construct local file path
        local_file_path = os.path.join(local_download_folder, blob.name)
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

        # Check exists
        if os.path.exists(local_file_path) and not args.replace:
            print(f"Skipped: {local_file_path}")
            continue
        
        t_start = time.time()
        print(f"Downloading: {blob.name}")
        
        # Download blob to local file
        blob_client = container_client.get_blob_client(blob.name)
        with open(local_file_path, "wb") as f:
            download_stream = blob_client.download_blob()
            f.write(download_stream.readall())
        
        print(f"Download complete: {local_file_path}, Duration: {(time.time()-t_start)/60:.2f}min")
