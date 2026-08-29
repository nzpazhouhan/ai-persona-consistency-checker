from ollama import chat


def ask_llm(system_prompt, user_message):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        options={
            "num_predict": 100
        }
    )

    return response["message"]["content"]
