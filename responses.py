from os import stat
import transitions
from df_engine.core import Actor, Context
from typing import Any
import re


def choose_greeting_response(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request

    name_pattern = re.compile("(I'm)|(My name is) (?P<name>\w+)", flags=re.IGNORECASE)
    is_match = name_pattern.match(request)
    if is_match:
        name = is_match.groupdict()['name']
        response = f'Nice to meet you {name}! My name is TestBot. What do you want to talk about?'
        return response

    if transitions.name_question_condition(ctx, actor):
        response = f'My name is TestBot! How\'re u?'
        return response

    state_pattern1 = re.compile("i'm (fine|great)")
    if state_pattern1.match(request):
        response = 'Glad to hear it!'
        return response

    state_pattern2 = re.compile("i'm (bad|upset)")
    if state_pattern2.match(request):
        response = "I feel sorry for you. How can I help?"
        return response

    return "I don't know, what to answer."

def extract_hobbie(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request

    hobbie_pattern = re.compile("I (like|enjoy|love|hate) (?P<hobbie>[\w ]+)", flags=re.IGNORECASE)
    is_match = hobbie_pattern.match(request)
    
    if is_match:
        hobbie = is_match.groupdict()['hobbie']
        response = f"I'm glad to hear it. I like {hobbie} too."
    else:
        response = "Maybe it's interesting, but I don't know. Can you tell more about this?"
    return response
    

    

    