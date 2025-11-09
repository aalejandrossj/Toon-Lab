from __future__ import annotations

import json

from toon_format import encode, decode

import os

from graph.agent import build_default_chain
from graph.state import GraphState

agent = build_default_chain()


async def process_json_node(state: GraphState) -> GraphState:
    """Analyse the original JSON payload with the default LangChain runnable."""
    pretty = json.dumps(state["input_json"], indent=2, ensure_ascii=False)
    message = pretty
    notes = await agent.ainvoke({"message": message})

    # Save result to json_result.md
    with open("json_result.md", "w", encoding="utf-8") as f:
        f.write(notes)

    print("result saved to json_result.md")

    return {**state, "json_agent_notes": notes}


def convert_json_to_toon(state: GraphState) -> GraphState:
    """Convert the JSON data to TOON and keep a decoded copy in the state."""
    input_json = state["input_json"]
    toon_payload = encode(input_json)

    print("\n")
    print("original_json")
    print(input_json)
    
    print("\n")
    print("toon_payload")
    print(toon_payload)
    print("\n")
    restored = decode(toon_payload)
    return {**state, "toon_payload": toon_payload, "toon_decoded": restored}


async def process_toon_node(state: GraphState) -> GraphState:
    """Run the same agent but feeding the TOON representation instead of JSON."""
    toon_payload: str = state["toon_payload"]
    message = toon_payload
    notes = await agent.ainvoke({"message": message})

    # Save result to toon_result.md
    with open("toon_result.md", "w", encoding="utf-8") as f:
        f.write(notes)

    print("result saved to toon_result.md")

    return {**state, "toon_agent_notes": notes}
