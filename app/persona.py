import json


class Persona:
    def __init__(self, data):

        identity = data.get("identity", {})

        self.name = identity.get("name", "")
        self.description = identity.get("description", "")
        self.background = identity.get("background", "")

        personality = data.get("personality", {})

        self.traits = personality.get("traits", [])
        self.emotional_patterns = personality.get("emotional_patterns", {})
        self.cognitive_style = personality.get("cognitive_style", {})
        self.social_style = personality.get("social_style", {})
        self.behavioral_patterns = personality.get("behavioral_patterns", [])

        values = data.get("values", {})

        self.core_values = values.get("core_values", [])
        self.moral_principles = values.get("moral_principles", [])
        self.beliefs = values.get("beliefs", [])
        self.boundaries = values.get("boundaries", [])

        motivations = data.get("motivations", {})

        self.goals = motivations.get("goals", [])
        self.drives = motivations.get("drives", [])
        self.ambitions = motivations.get("ambitions", [])

        preferences = data.get("preferences", {})

        self.likes = preferences.get("likes", [])
        self.dislikes = preferences.get("dislikes", [])
        self.interests = preferences.get("interests", [])
        self.hobbies = preferences.get("hobbies", [])

        self.relationships = data.get("relationships", {})

        self.decision_making = data.get("decision_making", {})

        self.communication = data.get("communication", {})

        self.knowledge = data.get("knowledge", {})

        narrative = data.get("narrative", {})

        self.backstory = narrative.get("backstory", "")
        self.important_events = narrative.get("important_events", [])


def load_persona(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Persona(data)
