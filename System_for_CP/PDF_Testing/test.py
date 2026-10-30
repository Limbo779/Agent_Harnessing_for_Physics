from ollama import chat

response = chat(
  model='aiden_lu/minicpm-v2.6:Q4_K_M',
  messages=[{'role': 'user', 'content': 'Tell me about Canada.'}],
  format='json'
)
print(response.message.content)