
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def get_drive_service(api_key):
    return build("drive", "v3", developerKey=api_key)

def list_files_in_folder(service, folder_id):
    results = service.files().list(q=f"'{folder_id}' in parents").execute()
    return results.get("files", [])

def download_file_content(service, file_id):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk()
    return fh.getvalue().decode("utf-8")
