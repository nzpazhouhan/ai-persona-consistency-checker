import json


class Persona:
    def __init__(self, data):

        # Identity
        self.name = data["identity"]["name"]
        self.identity = data["identity"]["description"]
        self.background = data["identity"].get("background", "")

        # Personality
        personality = data.get("personality", {})

        self.traits = personality.get("traits", [])

        self.emotional_patterns = personality.get(
            "emotional_patterns", {}
        )

        self.cognitive_style = personality.get(
            "cognitive_style", {}
        )

        self.social_style = personality.get(
            "social_style", {}
        )

        self.behavioral_patterns = personality.get(
            "behavioral_patterns", []
        )

        # Values
        values = data.get("values", {})

        self.values = values.get("core_values", [])

        self.moral_principles = values.get(
            "moral_principles", []
        )

        self.beliefs = values.get(
            "beliefs", []
        )

        self.boundaries = values.get(
            "boundaries", []
        )

        # Motivations
        motivations = data.get("motivations", {})

        self.goals = motivations.get("goals", [])
        self.drives = motivations.get("drives", [])
        self.ambitions = motivations.get("ambitions", [])

        # Preferences
        preferences = data.get("preferences", {})

        self.likes = preferences.get("likes", [])
        self.dislikes = preferences.get("dislikes", [])
        self.interests = preferences.get("interests", [])
        self.hobbies = preferences.get("hobbies", [])

        # Relationships
        self.relationships = data.get("relationships", {})

        # Decision making
        self.decision_making = data.get(
            "decision_making", {}
        )

        # Communication
        self.speech_style = data.get(
            "communication", {}
        )

        # Knowledge
        self.knowledge = data.get(
            "knowledge", {}
        )

        # Narrative
        narrative = data.get("narrative", {})

        self.backstory = narrative.get(
            "backstory", ""
        )

        self.important_events = narrative.get(
            "important_events", []
        )


def load_persona(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Persona(data)
