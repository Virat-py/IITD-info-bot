from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("MIRA_API_KEY")
USERNAME = "virat"  # Replace with your Mira username
DATASET_NAME = f"{USERNAME}/data-iitd"

# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

try:
    print("🔹 Creating dataset...")
    client.dataset.create(DATASET_NAME, "IIT Delhi College FAQ Dataset")
    client.dataset.add_source(DATASET_NAME, file_path="data.txt")
    print("✅ Dataset uploaded successfully!")

except Exception as e:
    error_message = str(e)
    
    # ✅ If dataset already exists, continue without failing
    if "already exists" in error_message:
        print("⚠️ Dataset already exists. Skipping creation...")
    else:
        print(f"❌ Error creating dataset: {error_message}")
