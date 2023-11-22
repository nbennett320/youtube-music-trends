import random
import subprocess
import os
from ffmpeg import FFmpeg
from scipy.io import wavfile

class Song:
  filename: str
  ffmpeg: FFmpeg
  sample_rate = 44_100
  file_extension = 'wav'

  def __init__(self, filename: str):
    self.filename = filename
    self.ffmpeg = FFmpeg()
  
  def mod_random_tempo(self):
    amt: float
    if(random.uniform(0, 1) < .5):
      amt = random.uniform(.8, .12)
    else:
      amt = random.uniform(-1.1, -.15)
    self.mod_tempo(amt)

  def mod_tempo(self, amt: float):
    self.ffmpeg.input(self.filename)

    new_rate = round(self.sample_rate * (1 - amt))
    self.sample_rate = new_rate
    print(f"mod amt: {amt}")

    name_speed_mod = 'slower' if amt > 0 else 'faster'
    new_filename = f"{self.filename[0:-4]}_{name_speed_mod}.{self.file_extension}"
    self.ffmpeg.output(
      new_filename,
      filter=f"asetrate={new_rate}")
    self.ffmpeg.execute()
    self.filename = new_filename

  def len(self):
    sample_rate, samples = wavfile.read(self.filename)
    n_samples = len(samples)
    
    self.sample_rate = sample_rate

    return n_samples

  def dur(self):
    time = int(self.len() / self.sample_rate)
    h = time // 3600
    time %= 3600
    m = time // 60
    time %= 60
    s = time
  
    return h, m, s 
  
  def format_dur(self):
    h, m, s = self.dur()
    return f"{h}:{m}:{s}"
