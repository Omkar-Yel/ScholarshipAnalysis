import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Setup credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\Admin\Downloads\analysisautomator-9789a0aeb982.json", scope)
client = gspread.authorize(creds)

# Open sheet
sheet_name = "NotebookCommunication"
try:
    sheet = client.open(sheet_name)
    print(f"✅ Opened Google Sheet: {sheet_name}")
except Exception as e:
    print(f"❌ Failed to open sheet: {e}")
    exit(1)

# Access worksheet
try:
    input_sheet = sheet.worksheet("NotebookInput")
    val = input_sheet.acell("A1").value
    print(f"📥 Value in A1: {val if val else '[Empty]'}")
except Exception as e:
    print(f"❌ Error accessing worksheet or cell: {e}")

# Keep window open (for double-click runs)
print("\nScript finished. Press Ctrl+C to exit or wait 10 seconds.")
time.sleep(10)
