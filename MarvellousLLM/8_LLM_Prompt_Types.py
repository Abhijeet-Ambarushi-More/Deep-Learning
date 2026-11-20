from ollama import chat

# Select the local LLM
Model = "llama3.2:1b"

# Define prompts
prompts = [
    "Explain recursion",

    "Explain recursion in python in 3 simple points",

    """You are experianced python teacher.
    explain recursion for beginner.
    Give one simple example""",

    """Covert programming languages to uppercase.
    Example 1 : 
    Input : python
    Output : PYTHON
    
    Example 2 : 
    Input : java
    Output : JAVA

    Input : javascript
    Output : """
]

# Execute every prompt

for index,prompt in enumerate(prompts, start=1):
    print("-"*30)
    print("Prompt number : ",index)
    print("Input prompt : ",prompt)

    response = chat(
        model = Model,
        messages = [
        {
            "role" : "User",
            "content" : prompt
        }
    ])

    print("\nResponse from LLM is : ")
    print(response.message.content)