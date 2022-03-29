import json
import glob
from df_engine.core.keywords import (TRANSITIONS, 
                                     GLOBAL, 
                                     LOCAL, 
                                     MISC, 
                                     PROCESSING, 
                                     RESPONSE
                                    )
from df_engine.core import Context, Actor
from typing import Union, Optional, Tuple
import logging
import sys
import re


logging.basicConfig(
    format="%(asctime)s-%(name)15s:%(lineno)3s:%(funcName)20s():%(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

keywords = [TRANSITIONS, GLOBAL, LOCAL, MISC, PROCESSING, RESPONSE]

def plots_from_json(root_dir: str) -> dict:
    plots = {}
    for json_file in glob.glob(f'{root_dir}/*.json'):
        with open(json_file) as f:
            plot = json.load(f)
            walk(plot)
            plots.update(plot)
    logger.info("Dialog plots were loaded.")
    logger.info(plots.keys())
    return plots


def walk(plot: dict):
    """
        Recursively walk through nested dict to replace strings with commands (if needed)
    """
    for key, value in plot.copy().items():
        try:
            key_ = eval(key)
        except:
            key_ = key
        plot[key_] = plot.pop(key)
        if isinstance(value, str):
            while True:
                try:
                    plot[key_] = eval(value) if re.match('(cnd)|(transitions)|(rsp)|(responses)\.', value) else value
                    break
                except NameError as e:
                    module_name = str(e).split("'")[1]
                    if module_name == 'cnd':
                        import_str = 'import df_engine.conditions as cnd'
                    elif module_name == 'rsp':
                        import_str = 'import df_engine.responses as rsp'
                    else:
                        import_str = f'import {module_name}'
                    exec(import_str)
        elif isinstance(value, dict):
            walk(plot[key_])


def turn_handler(in_request: str, 
                 ctx: Union[Context, str, dict], 
                 actor: Actor, 
                 true_out_response: Optional[str] = None) -> Tuple[str, Context]:
    ctx = Context.cast(ctx)
    ctx.add_request(in_request)
    ctx = actor(ctx)
    out_response = ctx.last_response
    if true_out_response is not None and true_out_response != out_response:
        msg = f"in_request = {in_request} -> true_out_response != out_response: {true_out_response} != {out_response}"
        raise Exception(msg)
    else:
        logger.info(f"in_request = {in_request} -> {out_response}")
    return out_response, ctx


def init_actor(root_dir: str, 
               start_label: Tuple[str, str], 
               fallback_label: Optional[Tuple[str, str]] = None) -> Actor:
    plot = plots_from_json(root_dir)
    actor = Actor(plot, start_label, fallback_label, label_priority=1.0)
    logger.info("Actor initialized.")
    return actor


def run_test(dialog_file: str, actor: Optional[Actor] = None, **kwargs):
    """
    Args:
        dialog_file -- file with rows of the form List[Tuple[str, str]]
        kwargs -- should duplicate `init_actor` arguments if actor is None
    """
    ctx = {}
    if actor is None:
        actor = init_actor(**kwargs)

    with open(dialog_file) as f:
        dialogue = eval(f.read())

    for in_request, true_out_response in dialogue:
        true_out_response = None if len(true_out_response) == 0 else true_out_response
        _, ctx = turn_handler(in_request, ctx, actor, true_out_response)

    logger.info('All tests were passed successfully.')


def run_interactive_mode(actor: Optional[Actor] = None, **kwargs):
    """
        kwargs -- should duplicate `init_actor` arguments if actor is None
    """
    if actor is None:
        actor = init_actor(**kwargs)

    ctx = {}
    logger.info('Type something to start dialog...')

    while True:
        in_request = sys.stdin.readline()
        if not in_request:
            break
        in_request = in_request.rstrip('\n')
        _, ctx = turn_handler(in_request, ctx, actor)


    
