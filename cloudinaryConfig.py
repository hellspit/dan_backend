import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloudName = os.getenv("CLOUDINARY_CLOUD_NAME"),
    apiKey = os.getenv("CLOUDINARY_API_KEY"),
    apiSecretKey = os.getenv("CLOUDINARY_API_SECRET")
)