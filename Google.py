import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def Create_Service(client_secret_file, api_name, api_version, scopes):
    """Initializes and returns an authorized service connection."""
    creds = None
    pickle_file = f'token_{api_name}_{api_version}.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            creds = flow.run_local_server(port=0)

        with open(pickle_file, 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build(api_name, api_version, credentials=creds)
        print(f"🎉 {api_name} v{api_version} service created successfully.")
        return service
    except Exception as e:
        print(f"Failed to create service: {e}")
        return None