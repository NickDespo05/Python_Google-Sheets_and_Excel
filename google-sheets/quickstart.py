from __future__ import print_function
# https://www.youtube.com/watch?v=4ssigWmExak
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account

creds = None
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1GEt6opLnfiOmpJXWBmFMcc8XqRBJPmsKrs4ZR9YB5xg'

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
service = build('sheets', 'v4', credentials=creds)
     # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="A1:F31").execute()
values = result.get('values', [])

# if not values:
#    print('No data found.')
            
# print('Name, Major:')
# for row in values:
#             # Print columns A and E, which correspond to indices 0 and 4.
#    print('%s, %s' % (row[0], row[4]))

aoa = [["1/1/2020", 4000], ["4/4/2022", 3000], ["3/3/2020", 2000]]

request = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                                range="A32", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()

print(request)