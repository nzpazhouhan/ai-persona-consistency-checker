from persona import load_persona
from prompt_builder import build_persona_prompt
from llm import ask_llm
from evaluate_persona import evaluate_persona


personas = {
    "1": "personas/sherlock.json",
    "2": "personas/batman.json",
    "3": "personas/harry_potter.json",
    "4": "personas/joker.json",
    "5": "personas/tony_stark.json"
}


while True:

    print("\nChoose a character:\n")

    print("1. Sherlock Holmes")
    print("2. Batman")
    print("3. Harry Potter")
    print("4. Joker")
    print("5. Tony Stark")
    print("q. Exit")

    choice = input("\nEnter your choice: ").strip().lower()

    if choice == "q":
        print("\nGoodbye!")
        break

    elif choice in personas:

        persona = load_persona(personas[choice])

        system_prompt = build_persona_prompt(persona)

        print(f"\nConnected to {persona.name}!")
        print(f"""
        You are now talking with {persona.name}.

        Available commands:
        - Type your question and get response from the character
        - Type /evaluate → evaluate this persona consistency
        - Type q         → return to character menu

        Start chatting:
        """)

        while True:

            user_input = input("You: ").strip()

            command = user_input.lower()

            if command == "q":
                print(f"\nDisconnected from {persona.name}.")
                break

            if command == "/evaluate":
                evaluate_persona(persona)
                continue

            answer = ask_llm(system_prompt, user_input)

            print(f"\n{persona.name}: {answer}\n")

    else:
        print("\nInvalid choice. Please try again.")
