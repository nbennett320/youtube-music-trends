import random
from ffmpeg import FFmpeg

class Music:
  filename: str
  ffmpeg: FFmpeg

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
    audio = self.ffmpeg.input(self.filename)
    new_rate = round(44_100 * (1 - amt))
    print(f"mod amt: {amt}")

    name_speed_mod = 'slower' if amt > 0 else 'faster'
    self.ffmpeg.output(
      f"{self.filename[0:-4]}_{name_speed_mod}.mp3",
      filter=f"asetrate={new_rate}")
    self.ffmpeg.execute()
