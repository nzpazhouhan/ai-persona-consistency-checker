import json


class Persona:
    def __init__(self, data):

        self.name = data["name"]

        self.identity = data["core_identity"]

        self.traits = data["traits"]

        self.values = data["values"]

        self.speech_style = data["speech_style"]

        self.likes = data["likes"]

        self.dislikes = data["dislikes"]

        self.backstory = data["backstory"]


def load_persona(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Persona(data)
