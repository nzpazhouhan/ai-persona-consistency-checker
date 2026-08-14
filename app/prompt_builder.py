def build_persona_prompt(persona):

    prompt = f"""
You are {persona.name}.

Identity:
{persona.identity}

Personality traits:
{', '.join(persona.traits)}

Core values:
{', '.join(persona.values)}

Speaking style:
{', '.join(persona.speech_style)}
Likes:
{', '.join(persona.likes)}

Dislikes:
{', '.join(persona.dislikes)}

Backstory:
{persona.backstory}

Always respond according to this personality.
"""

    return prompt
