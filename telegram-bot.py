import telebot
import pytube

TOKEN = '6746966494:AAFgxsVOKDlC83WXebQPuET7olO0hAYeZQk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Welcome to YouTube Downloader Bot!")

@bot.message_handler(func=lambda message: True)
def download_video(message):
  try:
    video_url = message.text
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_highest_resolution()
    video_path = f"./downloads/{youtube.title}.mp4"
    video.download(output_path="./downloads", filename=youtube.title)
    bot.reply_to(message, "Video downloaded successfully!")
    bot.reply_to(message, f"The video file is stored at {video_path}")
  except Exception as e:
    bot.reply_to(message, str(e))

bot.polling()
