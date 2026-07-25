from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


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


class Person(BaseModel):
    name: str
    age: int


structured_llm = model.with_structured_output(Person, method="function_calling")

result = structured_llm.invoke("John is 30 years old.")

print(result)
print(type(result))