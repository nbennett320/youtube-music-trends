import requests
import os, base64

class Spotify:
  env_file = 'config.env'
  token_url = 'https://accounts.spotify.com/api/token'
  client_id: str
  client_secret: str

  def __init__(self):
    with open(self.env_file) as f:
      for line in f:
        if line.startswith('#') or not line.strip():
          continue
        key, value = line.strip().split('=', 1)
        match key:
          case 'CLIENT_ID':
            self.client_id = value
          case 'CLIENT_SECRET':
            self.client_secret = value
    print(f"id: {self.client_id}, secret: {self.client_secret}")


  def new_token(self) -> dict:
    join = f"{self.client_id}:{self.client_secret}"
    auth = base64.b64encode(bytes(join, 'utf-8')).decode('utf-8')
    
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic ' + auth,
    }
    
    data = {
      'grant_type': 'client_credentials'
    }

    req = requests.post(
      self.token_url, 
      headers=headers,
      data=data)

    if req.status_code == 200:
      return req.json()
    
    return None
