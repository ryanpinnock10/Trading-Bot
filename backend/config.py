# API_KEY = "PKQBQNZ5UE5V81TGITGN"
# SECRET_KEY = "ceSxlGQPKbjEF37i2uywLE7AqXWjRMd/a7Sc7fOZ"
import os

def get_credentials(key_id=None, secret_key=None, oauth=None):
    oauth = oauth or os.environ.get('APCA_API_OAUTH_TOKEN')

    key_id = key_id or os.environ.get('APCA_API_KEY_ID')
    if key_id is None and oauth is None:
        raise ValueError('Key ID must be given to access Alpaca trade API',
                         ' (env: APCA_API_KEY_ID)')

    secret_key = secret_key or os.environ.get('APCA_API_SECRET_KEY')
    if secret_key is None and oauth is None:
        raise ValueError('Secret key must be given to access Alpaca trade API'
                         ' (env: APCA_API_SECRET_KEY')

    return key_id, secret_key, oauth

get_credentials()