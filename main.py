import requests
from playlist_fetch import PlaylistFetch
from youtube_search import YoutubeSearch
from music import Music

def build_search_term(item: dict[str, any]):
  track = item['track']
  title = track['name']
  artists = track['artists']
  artist = ''

  i = 0
  for contributor in artists:
    artist = artist + contributor['name']
    if i < len(artists) - 1:
      artist = f"{artist} and "
  
  return f"{artist} {title}"

def main():
  playlist_fetcher = PlaylistFetch()
  playlist_items = playlist_fetcher.get_playlist()

  search_query = build_search_term(playlist_items['tracks']['items'][10])
  yt_searcher = YoutubeSearch(search_query)

  print(f"search_query: {search_query}")

  yt_searcher.download_file()
  filename = f"{yt_searcher.download_filename}.mp3"

  music_modifier = Music(filename)
  music_modifier.mod_random_tempo()

main()
