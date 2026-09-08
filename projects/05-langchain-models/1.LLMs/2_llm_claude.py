from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-4-5-20251001", max_tokens=1024)

result = llm.invoke("What is the capital of France?")

print(result.content)
