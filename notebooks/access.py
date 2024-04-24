import msal

# Set up authentication
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
TENANT_ID = 'your_tenant_id'

authority = f'https://login.microsoftonline.com/{TENANT_ID}'
app = msal.ConfidentialClientApplication(CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET)

result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
access_token = result['access_token']
