from persona import load_persona
from prompt_builder import build_persona_prompt
from llm import ask_llm


persona = load_persona("personas/sherlock.json")

system_prompt = build_persona_prompt(persona)


question = input("Ask Sherlock: ")

answer = ask_llm(system_prompt, question)

print("\nSherlock:")
print(answer)
