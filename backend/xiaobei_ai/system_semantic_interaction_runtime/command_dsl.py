from __future__ import annotations

COMMAND_TYPES = [
    "START_FLOW",
    "SET_SLOT",
    "UPDATE_SLOT",
    "DISAMBIGUATE_FLOW",
    "CLARIFY_INTENT",
    "CLARIFY_ARTIFACT",
    "CLARIFY_USE_CASE",
    "CLARIFY_KEY_SLOT",
    "GENERATE_CANDIDATE",
    "MODIFY_CANDIDATE",
    "SYNC_RENDERER",
    "ASK_CONFIRMATION",
    "BLOCK_ACTION",
    "EXPLAIN_LIMITATION",
    "NOOP",
]

COMMAND_TYPE_SET = set(COMMAND_TYPES)


def make_command(command_type: str, **payload: object) -> dict:
    if command_type not in COMMAND_TYPE_SET:
        raise ValueError(f"unknown semantic command: {command_type}")
    command = {"type": command_type}
    command.update(payload)
    return command


def validate_commands(commands: list[dict]) -> None:
    for command in commands:
        command_type = command.get("type")
        if command_type not in COMMAND_TYPE_SET:
            raise ValueError(f"invalid semantic command: {command_type}")
