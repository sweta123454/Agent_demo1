

import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Set your Gemini API key
os.environ["API_KEY"] = ""
# 2. Initialize the current version model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Simple loop to retry if the server is busy
print("Sending request to gemini-1.5-flash...")
for attempt in range(3):
    try:
        response = llm.invoke("What is the meaning of life?")
        print("\nSuccess! Response:")
        print(response.content)
        break
    except Exception as e:
        # Check if the error is a 503 high demand spike
        if "503" in str(e) and attempt < 2:
            print(f"Server busy (503). Retrying in 5 seconds (Attempt {attempt + 1}/3)...")
            time.sleep(5)
        else:
            print("\nAn error occurred:")
            raise e

