import requests
import urllib
from spotify_client import Spotify

class PlaylistFetch:
  playlist_id = '3CV4m7gpnCjTYPqcPoI2dc'
  playlist_url: str

  field_structure = {
    'tracks': {
      'href': 'href',
      'name': 'name',
      'items': {
        'track': {
          'name': 'name',
          'artists': {
            'name': 'name',
          }
        }
      }
    }
  }

  _field = ''
  _token: str
  _spotify: Spotify

  def __init__(self):
    self.playlist_url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}"
    self._spotify = Spotify()
    self._token = self._spotify.new_token()

  def get_playlist(self):
    access_token = self._token['access_token']

    self._build_request_fields()

    headers = {
      'Authorization': f"Bearer {access_token}",
    }

    req = requests.get(
      self.playlist_url,
      headers=headers)

    print(f"fields: {self._field}")
    print(f"url: {self.playlist_url}")
    # print(access_token)
    # print(req)
    print(req.json())

  # PRIVATE METHODS

  # build request param from self.field_structure
  # ex: tracks(href,name,items(track(name)))
  def _build_request_fields(self):
    # format spotify field
    def traverse(root):
      items = root.items()
      i = 0
      for key, val in items:
        if type(val) == dict:
          self._field = self._field + key + '('
          traverse(root[key])
        else: 
          self._field = self._field + val
        if(i == len(items) - 1):
          self._field = self._field + ')'
        else:
          self._field = self._field + ','
        i = i + 1
        
    traverse(self.field_structure)

    # trim trailing parenthesis
    self._field = self._field[0:-1]

    # format and set url    
    field_param = urllib.parse.quote(self._field)
    print(field_param)
    self.playlist_url = f"{self.playlist_url}?fields={field_param}"

