import df_engine.conditions as cnd
from df_engine.core import Actor, Context
import string
import re


def greeting_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    greeding_regexp = re.compile(f'(Start)|(Hi)|(Hello)[{string.punctuation}]*', flags=re.IGNORECASE)
    return greeding_regexp.match(last_request) is not None


def has_question(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    question_pattern = re.compile('.*\?+')
    is_match = question_pattern.match(last_request) is not None
    return is_match


def name_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    name_pattern = re.compile(f'My name is \w+', flag=re.IGNORECASE)
    is_match = name_pattern.match(last_request) is not None
    return is_match


def name_question_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    name_with_question_pattern = re.compile(".* your name ?\?*", flags=re.IGNORECASE)
    is_match = name_with_question_pattern.match(last_request) is not None
    return is_match


def how_are_you_question_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    how_are_you_pattern = re.compile("((How're)|(How are) (you|u))|(What's up) ?\?*", flags=re.IGNORECASE)
    is_match = how_are_you_pattern.match(last_request) is not None
    return is_match


def and_you_question_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    return cnd.regexp('and you.*', flags=re.IGNORECASE)


def bye_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    last_request = ctx.last_request
    bye_pattern = re.compile("(Bye|Goodbye|Stop).*", flags=re.IGNORECASE)
    is_match = bye_pattern.match(last_request)
    return is_match


