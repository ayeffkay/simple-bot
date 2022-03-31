from df_engine.core import Context, Actor
from df_engine.core.types import NodeLabel3Type


def high_priority_node(flow_label: str, label: str) -> NodeLabel3Type:
    def inner_transition(ctx: Context, actor: Actor, *args, **kwargs):
        return (flow_label, label, 5.0)
    return inner_transition
    

def priority_node(ctx: Context, actor: Actor, *args, **kwargs) -> NodeLabel3Type:
    return ('global_flow', 'node_goodbye', 2.0)