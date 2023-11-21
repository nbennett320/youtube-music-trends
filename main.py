import requests
from playlist_fetch import PlaylistFetch

def main():
  playlist_fetcher = PlaylistFetch()

  playlist_fetcher.get_playlist()

main()
