import dropbox

app_key="sliifxgyvx9xyb9"
app_secret="y0jcz0elb6zyie9"

flow=dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url=flow.start()
print(authorize_url)
print('2. Click "Allow" (you might have to log in first)')
print('3. Copy the authorization code.')
code =input("Enter the authorization code here: ").strip()


access_token,user_id=flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
print('linked account: ', client.account_info())

