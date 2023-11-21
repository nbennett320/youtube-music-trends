import requests
import urllib
import util
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from youtube_dl import YoutubeDL

class YoutubeSearch:
  search_base_url = 'https://www.youtube.com/results'
  query: str
  search_url: str
  dl_url: str
  download_filename: str
  downloader: YoutubeDL

  def __init__(self, query: str):
    self.query = query
    self.download_filename = util.to_snake_case(query)

    download_config = {
      'format': 'bestaudio/best',
      'keepvideo': False,
      'outtmpl': f"{self.download_filename}.mp3",
    }

    self.downloader = YoutubeDL(download_config)
  
  def download_file(self):
    self._get_url()
    self._download_mp3()

  # PRIVATE METHODS

  def _build_url(self):
    param = urllib.parse.quote(self.query)
    self.search_url = f"{self.search_base_url}?search_query={param}"

  def _get_url(self):
    self._build_url()

    req = requests.get(self.search_url)  
    self._parse_page_content(req.text)

  def _parse_page_content(self, html_text: str):
    soup = BeautifulSoup(html_text, 'html.parser')

    browser = webdriver.Firefox()
    browser.get(self.search_url)

    browser.implicitly_wait(5)

    selector = 'a#video-title>yt-formatted-string'
    target: WebElement = browser.find_elements(By.CSS_SELECTOR, selector)[0]
    target.click()
    
    self.dl_url = browser.current_url

    browser.close()
  
  def _download_mp3(self):
    print(f"filename: {self.download_filename}")

    with self.downloader as ydl:
      ydl.download([self.dl_url])
    
    return f"{self.download_filename}.mp3"
    