from ollama import chat
import json 

# Prompt for LLM
prompt = """Give me the information about python pprogramming language.
Return the result as JSON with these keys : 
language
type
creator
"""

# Execute LLM

response = chat(
    model = "llama3.2:1b",
    messages = [
    {
        "role" : "User",
        "content" : prompt
    }
],format = "json"
)

answer = response.message.content

print("LLM response : ")
print(answer)