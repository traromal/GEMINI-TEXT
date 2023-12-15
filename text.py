import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

API = "YOUR API KEY"

genai.configure(api_key=API)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Tell me about the beginning of time?")
print(response.text)
