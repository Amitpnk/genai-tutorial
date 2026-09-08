from langchain_openai import ChatAntropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
result = llm.invoke("What is the capital of France?")


# llm = OpenAI(model_name="gpt-4", temperature=1.5, max_completion_tokens=10)
# result = llm("What a 5 line poem on cricket")

print(result)
print(result.content)