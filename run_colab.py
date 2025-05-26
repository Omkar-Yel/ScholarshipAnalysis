import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate and connect to Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("NotebookCommunication")
input_sheet = sheet.worksheet("NotebookInput")
output_sheet = sheet.worksheet("NotebookOutput")

# Read input
input_val = input_sheet.acell("A1").value
print("Input:", input_val)

# Process
try:
    result = int(input_val) * 10
except:
    result = "Invalid"

# Write output
output_sheet.update("A1", str(result))
print("Output written:", result)
