"""Legacy plugin from Grapewhistle."""
from util import hook
import random
import re

emotes = ["pets", "hugs"]
reactions = ["Oi!", "Eww, nerd cooties.", "'git offa me!", "Hands off, peasant.",
    "You can stop now.",
    "Oh \x02babby"
]

@hook.regex("ACTION.*(" + "|".join(emotes) + ") (?:the )?(\S+)\x01", re.I)
def react(inp, input=None):
    if inp.groups()[1].lower() == input.conn.nick.lower():
        input.say(random.choice(reactions))
