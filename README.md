## PROTECH Project Tools (CONFIDENTIEL)

### Description
This repository contains tools for the PROTECH project. The tools are designed to facilitate various tasks, including:
1. [Downloading files from Azure Blob Storage](#1-azure-download-tool)
2. Comming soon...

### Tools
#### 1. **Azure Download Tool**
The `azure_download_tool.py` script is used to download files from Azure Blob Storage using Azure CLI credentials.

#### Requirements
To use the Azure Download Tool, you need to have the following installed (ubuntu Debian):
1. **Azure CLI**: 
    ```sh
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    ```
    After installation, log in to Azure CLI (this will open a browser window):
    ```sh
    az login
    ```
    check your ID and MDP in your email (if you are using a shared account)
    For LAAS (CONFIDENTIEL):
      - ID: f.lerasle.ext@manitou-group.com
      - mdp = *********
    
2. **Azure SDK for Python**:
    ```sh
    pip install azure-storage-blob
    ```

3. **Azure Identity**:
    ```sh
    pip install azure-identity
    ```

#### Usage
**Note**: Before running the Azure Download Tool, make sure you have logged in to Azure CLI using the `az login` command.

To use the Azure Download Tool, run the following command:
```sh
python tools/azure_download_tool.py --download_prefix <prefix> --save_dir <local_directory> [--download_suffix <suffix>] [--replace]
```
> **Arguments**:
> - --download_prefix (-p): Prefix of the files to download (required).
> - --download_suffix (-s): Suffix of the files to download (optional).
> - --save_dir (-o): Local folder to save the downloaded files (required).
> - --replace (-r): Replace the existing files (optional).


#### Example
```sh
# Download all files with the prefix 'Dataset_IntegraliteDesDonnees/rosbag2_2025_01' to the local directory './PROTECH/MANITOU/Dataset202501'
python tools/azure_download_tool.py -p Dataset_IntegraliteDesDonnees/rosbag2_2025_01 -o ./PROTECH/MANITOU/Dataset202501
# If you only want to download files with the suffix '.avi', you can add the --download_suffix (-s) argument
python tools/azure_download_tool.py -p Dataset_IntegraliteDesDonnees/rosbag2_2025_01 -o ./PROTECH/MANITOU/Dataset202501 -s .avi
```