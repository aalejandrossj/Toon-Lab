from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from graph.nodes import convert_json_to_toon, process_json_node, process_toon_node
from graph.state import GraphState


def build_graph():
    """Create a three-node LangGraph workflow with START and END wiring."""
    workflow = StateGraph(GraphState)

    workflow.add_node("json_agent", process_json_node)
    workflow.add_node("to_toon", convert_json_to_toon)
    workflow.add_node("toon_agent", process_toon_node)

    workflow.add_edge(START, "json_agent")
    workflow.add_edge("json_agent", "to_toon")
    workflow.add_edge("to_toon", "toon_agent")
    workflow.add_edge("toon_agent", END)

    return workflow.compile()


__all__ = ["build_graph"]
