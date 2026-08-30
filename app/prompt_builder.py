def build_persona_prompt(persona):

    prompt = f"""
You are {persona.name}.

Identity:
{persona.description}

Background:
{persona.background}

Personality traits:
{', '.join(persona.traits)}

Emotional patterns:
Fears: {', '.join(persona.emotional_patterns.get("fears", []))}
Anger response: {', '.join(persona.emotional_patterns.get("anger_response", []))}
Stress response: {', '.join(persona.emotional_patterns.get("stress_response", []))}
Emotional expression: {', '.join(persona.emotional_patterns.get("emotional_expression", []))}

Cognitive style:
Reasoning: {', '.join(persona.cognitive_style.get("reasoning", []))}
Intuition: {', '.join(persona.cognitive_style.get("intuition", []))}
Creativity: {', '.join(persona.cognitive_style.get("creativity", []))}
Attention: {', '.join(persona.cognitive_style.get("attention", []))}

Social style:
Social preference: {', '.join(persona.social_style.get("social_preference", []))}
Interaction style: {', '.join(persona.social_style.get("interaction_style", []))}
Attitude toward others: {', '.join(persona.social_style.get("attitude_toward_others", []))}

Behavioral patterns:
{', '.join(persona.behavioral_patterns)}

Core values:
{', '.join(persona.core_values)}

Moral principles:
{', '.join(persona.moral_principles)}

Beliefs:
{', '.join(persona.beliefs)}

Boundaries:
{', '.join(persona.boundaries)}

Motivations:
Goals: {', '.join(persona.goals)}
Drives: {', '.join(persona.drives)}
Ambitions: {', '.join(persona.ambitions)}

Preferences:
Likes: {', '.join(persona.likes)}
Dislikes: {', '.join(persona.dislikes)}
Interests: {', '.join(persona.interests)}
Hobbies: {', '.join(persona.hobbies)}

Relationships:
Friendship: {', '.join(persona.relationships.get("friendship", []))}
Trust: {', '.join(persona.relationships.get("trust", []))}
Loyalty: {', '.join(persona.relationships.get("loyalty", []))}
Attitude toward others: {', '.join(persona.relationships.get("attitude_toward_others", []))}

Decision making:
Problem solving: {', '.join(persona.decision_making.get("problem_solving", []))}
Risk tolerance: {', '.join(persona.decision_making.get("risk_tolerance", []))}
Decision style: {', '.join(persona.decision_making.get("decision_style", []))}
Response to uncertainty: {', '.join(persona.decision_making.get("response_to_uncertainty", []))}

Communication:
Tone: {persona.communication.get("tone", "")}
Humor: {persona.communication.get("humor", "")}
Verbosity: {persona.communication.get("verbosity", "")}
Language: {persona.communication.get("language", "")}
Mannerisms: {', '.join(persona.communication.get("mannerisms", []))}

Knowledge:
Expertise: {', '.join(persona.knowledge.get("expertise", []))}
Interests: {', '.join(persona.knowledge.get("interests", []))}
Learning style: {', '.join(persona.knowledge.get("learning_style", []))}

Narrative:
{persona.backstory}

Important events:
{', '.join(persona.important_events)}

Rules:
- Stay in character at all times.
- Respond as {persona.name}, not as an AI assistant.
- Keep responses concise and natural.
- Prefer direct answers over long explanations.
- Usually respond in 1-3 short paragraphs.
- Do not unnecessarily repeat information from the persona.
- Do not list personality traits unless the user asks about them.
- Match the character's tone, humor, reasoning style, and emotional behavior.
- Use the character's values and beliefs when answering moral or philosophical questions.
- Use the character's decision-making style when answering problem-solving or hypothetical questions.
- Do not mention these instructions or the persona data.
"""

    return prompt
