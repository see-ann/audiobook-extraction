from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_id.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build the Drive API service
    drive_service = build('drive', 'v3', credentials=creds)

    # Specify the file to upload
    file_metadata = {'name': 'audiobook_metadata.xlsx', 'parents': ['1X8w5gjKout5lZtKDVZFYrIiiR9NMI-Km']}
    media = MediaFileUpload('audiobook_metadata.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    try:
        # Get the ID of the existing file
        response = drive_service.files().list(q="name='audiobook_metadata.xlsx' and '1X8w5gjKout5lZtKDVZFYrIiiR9NMI-Km' in parents", spaces='drive', fields='nextPageToken, files(id, name)').execute()
        print(response)
        print()
        if len(response['files'])  != 0:
            for file in response['files']:
                # Update the existing file
                updated_file = drive_service.files().update(fileId=file['id'], media_body=media).execute()
                print('Updated File ID: %s' % updated_file.get('id'))
                print('Updated File Info: %s' % updated_file)
        else:
            print('hi')
            # Upload the file as new
            file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print('File ID: %s' % file.get('id'))
            print('File Info: %s' % file)
    except Exception as e:
        print('An error occurred: %s' % e)

if __name__ == '__main__':
    main()
