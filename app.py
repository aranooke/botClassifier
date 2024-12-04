import telebot
from PIL import Image
import io,os
from dotenv import load_dotenv


load_dotenv();

api_key=os.getenv("TELEGRAM_API_KEY");



# Set up the bot with your token (replace 'YOUR_BOT_API_KEY' with your actual bot token)
bot = telebot.TeleBot(api_key)


# Function to handle image messages
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Get the image from the message
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Open the image using PIL
    img = Image.open(io.BytesIO(downloaded_file))

    # Process the image (you can add additional code here if you want to manipulate the image)
    # For now, we'll just send a confirmation message

    response = "Image received! Processing complete."
    bot.reply_to(message, response)

# Start polling
bot.polling()
