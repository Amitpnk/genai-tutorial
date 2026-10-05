from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation", pipeline_kwargs=dict(max_length=512, temperature=0.7))

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?")

print(result)
print(result.text)