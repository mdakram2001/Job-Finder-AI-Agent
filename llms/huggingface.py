import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# HuggingFace Model:
# -----------------------------

if "HUGGINGFACEHUB_API_TOKEN" in os.environ:
    print("HuggingFace token loaded successfully!")
else:
    print("Warning: HuggingFace token not found.")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)