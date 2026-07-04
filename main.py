import logging
from typing import Any, Dict

from openchadpy.tool_base import ToolBase

logger = logging.getLogger(__name__)


class Tool(ToolBase):
    """Minimal example tool that returns the provided greeting unchanged."""

    name = "greeting"
    description = (
        "Echoes back a greeting string provided by the caller. "
        "A minimal reference tool for verifying that tool registration, "
        "schema validation, and the invocation pipeline work end-to-end."
    )
    input_schema = {
        "type": "object",
        "properties": {
            "greeting": {
                "type": "string",
                "description": (
                    "The greeting text to echo back (e.g. 'Hello, world!'). "
                    "Leading and trailing whitespace is stripped, and the "
                    "value must contain at least one non-whitespace character."
                ),
            },
        },
        "required": ["greeting"],
    }
    allowed_callers = ["direct", "code_execution", "mcp_client"]

    async def execute(self, **kwargs) -> Dict[str, Any]:
        greeting: str = kwargs.get("greeting", "").strip()

        if not greeting:
            return {"error": "greeting is required and must not be empty."}

        return {
            "result": greeting,
        }