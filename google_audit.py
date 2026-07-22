import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_FILE = 'google-credentials.json'

def main():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"File {CREDENTIALS_FILE} not found.")
        return

    print("Authenticating with Google APIs...")
    try:
        creds = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, 
            scopes=['https://www.googleapis.com/auth/webmasters.readonly']
        )
        
        print("\n--- Google Search Console ---")
        gsc_service = build('webmasters', 'v3', credentials=creds)
        sites = gsc_service.sites().list().execute()
        site_list = sites.get('siteEntry', [])
        
        if not site_list:
            print("No sites found.")
            return
            
        site_url = "https://voilier-neuchatel.ch/"
        print(f"Fetching data for {site_url}...")
        
        # Top Keywords
        request = {
            'startDate': '2026-06-01',
            'endDate': '2026-07-20',
            'dimensions': ['query'],
            'rowLimit': 10
        }
        response = gsc_service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        print("\nTop 10 Keywords (Last 30 Days):")
        for row in response.get('rows', []):
            print(f"- {row['keys'][0]} (Clicks: {row['clicks']}, Impressions: {row['impressions']})")
            
        # Top Pages
        request['dimensions'] = ['page']
        response = gsc_service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        print("\nTop 10 Pages (Last 30 Days):")
        for row in response.get('rows', []):
            print(f"- {row['keys'][0]} (Clicks: {row['clicks']}, Impressions: {row['impressions']})")
             
    except Exception as e:
        print(f"Error during API connection: {e}")

if __name__ == '__main__':
    main()
