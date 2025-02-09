from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("MIRA_API_KEY")
USERNAME = "virat"
FLOW_NAME = f"{USERNAME}/iitd-info-bot"

# Initialize Mira Client
client = MiraClient(config={"API_KEY": API_KEY})

print("\n🤖 College Chatbot is Ready! Type 'exit' to quit.")

while True:
    question = input("\nYou: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Exiting chatbot. Have a great day!")
        break

    try:
        response = client.flow.execute(FLOW_NAME, {"input1": question})

        # ✅ Debug: Print Retrieved Documents
        if "retrieved_docs" in response:
            print("🔍 Retrieved Documents:", response["retrieved_docs"])

        # ✅ Print the final response
        if "result" in response:
            print("Bot:", response["result"])
        else:
            print("⚠️ No valid response. Please check the flow.")
    
    except Exception as e:
        print(f"⚠️ Error fetching response: {e}")
