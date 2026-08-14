import json


class Persona:
    def __init__(self, data):

        self.name = data["name"]

        self.identity = data["description"]

        self.traits = data["traits"]

        self.values = data["values"]

        self.speech_style = data["speaking_style"]

        self.likes = data.get("likes", [])

        self.dislikes = data.get("dislikes", [])

        self.backstory = data.get("backstory", "")


def load_persona(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Persona(data)
