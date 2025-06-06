from ollama import chat

# 1 Prompt für die Analyse vorbereiten
if risk_comm := input("Enter the sentence containing risk communication: "):
    prompt = f"""
You are a risk communication analysis assistant.

Please analyze the following risk communication text:

"{risk_comm}"

"""


# 2 Request an das LLM senden
    response = chat(
        model="mistral:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={"temperature": 0.7},  # ausprobieren, wie sich Ergebnisse verhalten
    )

    print(response)

# example1: The risk of heart failure is 10%. By taking our medication, it decreases to 5%. 
# example2: The risk of heart failure is 10 in 200 people. By taking our medication, it is 50% smaller.
