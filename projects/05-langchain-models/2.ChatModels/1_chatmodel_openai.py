from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
result = llm.invoke("What is the capital of France?")


# llm = OpenAI(model_name="gpt-4", temperature=1.5, max_completion_tokens=10)
# result = llm("What a 5 line poem on cricket")

print(result)
print(result.text)