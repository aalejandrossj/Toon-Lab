from __future__ import annotations

from typing import Any, Dict, TypedDict


class GraphState(TypedDict, total=False):
    """Shared state that flows through the LangGraph workflow."""

    input_json: Dict[str, Any]
    json_agent_notes: str
    toon_payload: str
    toon_decoded: Any
    toon_agent_notes: str
