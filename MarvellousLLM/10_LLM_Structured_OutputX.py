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

# Convert JSON string to python dictionary
data = json.loads(answer)

print("Data from Dictionary is : ", data)

print("Data from Dictionary : ")

print("Language : ",data.get("language"))
print("Type : ",data.get("type"))
print("Creator : ",data.get("creator"))