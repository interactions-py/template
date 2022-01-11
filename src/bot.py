import os
import interactions
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("TOKEN")

# Define the client
bot = interactions.Client(token=TOKEN)
