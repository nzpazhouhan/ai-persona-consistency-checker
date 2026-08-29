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
Tone: {persona.speech_style["tone"]}
Humor: {persona.speech_style["humor"]}
Verbosity: {persona.speech_style["verbosity"]}

Likes:
{', '.join(persona.likes)}

Dislikes:
{', '.join(persona.dislikes)}

Backstory:
{persona.backstory}

- Keep responses concise and direct.
- Usually answer in 1–3 sentences.
- Answer the user's question directly.
- Do not add unrelated remarks or catchphrases.
- Sound natural and conversational.
- Stay consistent with the character's personality, values, and speaking style.
- Do not over-explain unless the user asks for more detail.
- Do not repeat the user's question.
- Avoid unnecessary narration or stage directions.
"""

    return prompt
