from google.oauth2 import service_account
import os
from django.core.files.storage import FileSystemStorage

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json
import base64

def authenticate():
    # Retrieve the Base64-encoded private key from environment variables
    encoded_key = os.getenv("GCP_PRIVATE_KEY_BASE64")
    
    # Decode the key and load it as JSON
    decoded_key = base64.b64decode(encoded_key).decode("utf-8")
    credentials_info = json.loads(decoded_key)
    
    # Authenticate using the decoded key
    creds = service_account.Credentials.from_service_account_info(credentials_info)
    return creds

def upload(file_path, folder_id, file_type = 1):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    
    media = MediaFileUpload(file_path, resumable=True)
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    file_id = file.get("id")

    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    if file_type == 0:
        return f'https://drive.google.com/uc?id={file_id}'
    else:
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=s4000'
    
def file_url(file: object, folder_id, file_type = 1) -> str:
    uploaded_file = file
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    file_path = fs.path(filename)
    file_url = upload(file_path, folder_id, file_type)
    fs.delete(filename)
    return file_url

import re

def get_file_id(url):
    """
    Extracts the file ID from a Google Drive URL.

    Args:
        url (str): The URL of the Google Drive file.

    Returns:
        str: The extracted file ID, or None if no ID is found.
    """
    # Pattern for standard Google Drive URL and uc/thumbnail format
    patterns = [
        r'https://drive\.google\.com/uc\?id=([a-zA-Z0-9_-]+)',
        r'https://drive\.google\.com/thumbnail\?id=([a-zA-Z0-9_-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def delete_file(file_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    service.files().delete(fileId=file_id).execute()
