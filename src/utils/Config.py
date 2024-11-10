import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("STORAGE-CONNECTION-STRING")
    CONTAINER_NAME = os.getenv("CONTAINER-NAME")
    