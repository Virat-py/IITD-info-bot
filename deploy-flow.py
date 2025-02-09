from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("MIRA_API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

# Deploy Flow
flow = Flow(source="flow.yaml")
client.flow.deploy(flow)

print("✅ Flow deployed successfully!")
