import requests
from playlist_fetch import PlaylistFetch

def main():
  playlist_fetcher = PlaylistFetch()

  playlist_fetcher.build_request_fields()
  playlist_fetcher.get_playlist()

main()
