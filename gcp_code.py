from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"

def analysis(request):
  request_data = request.form.get('sentiment')
  sentiment = None
  
  if request_data != None:
    sentiment = request_data
  else:
      return f'Sentiment is required'
    
  sentiment = "What a great car, it stopped working in the second day"

  template = """Classify the sentiment of this post between 'Positive' or 'Negative. Step by step. {sentiment}"""

  prompt = PromptTemplate(template=template,
  input_variables=["sentiment"])

  llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.2, "max_length":64}))
  return llm_chain.run(sentiment)



# def analysis(request):
#     request_data = request.form.get('sentiment')
#     sentiment = None
    
#     if request_data != None:
#       sentiment = request_data
#     else:
#        return f'Sentiment is required'

# sentiment = "What a great car, it stopped working in the second day"

# template = """Classify the sentiment of this post between 'Positive' or 'Negative. Step by step. {sentiment}"""

# prompt = PromptTemplate(template=template,
# input_variables=["sentiment"])

# llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.2, "max_length":64}))

# print(llm_chain.run(sentiment))
