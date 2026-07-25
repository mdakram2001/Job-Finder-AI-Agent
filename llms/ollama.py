from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


# -----------------------------
# Ollama Model:
# -----------------------------


if "OLLAMA_API_KEY" in os.environ:
    print("Ollama token loaded successfully!")
else:
    print("Warning: Ollama token not found.")

model = ChatOpenAI(
    model="gpt-oss:120b-cloud",
    base_url="https://ollama.com/v1",
    api_key=os.environ["OLLAMA_API_KEY"],
    temperature=0,
)
