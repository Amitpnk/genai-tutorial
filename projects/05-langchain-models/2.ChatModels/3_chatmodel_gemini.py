from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
result = llm.invoke("What is the capital of France?")

# llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=1.5)
# result = llm.invoke("What a 5 line poem on cricket")

print(result)
print(result.text)