from ffmpeg import FFmpeg

class Music:
  filename: str
  ffmpeg: FFmpeg

  def __init__(self, filename: str):
    self.filename = filename
    self.ffmpeg = FFmpeg()
  
  def slow_down(self, amount: float):
    audio = self.ffmpeg.input(self.filename)
    # audio.audio.filter('atempo', amount)

    new_rate = round(44_100 * amount)

    self.ffmpeg.output(
      f"{self.filename[0:-4]}_slower.mp3",
      filter=f"asetrate={new_rate}")
    self.ffmpeg.execute()
