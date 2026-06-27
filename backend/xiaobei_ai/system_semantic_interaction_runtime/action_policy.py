from __future__ import annotations

from typing import Any


FORMAL_ACTION_MARKERS = ["导出", "提交", "发布", "覆盖", "写入", "记住", "保存到", "正式"]
MODIFY_MARKERS = ["改", "调整", "修改", "换成", "轻一点", "重一点", "删掉", "补充"]
GENERATE_MARKERS = ["生成", "做一份", "写一份", "直接做", "开始做"]


def detect_operation(message: str, state: dict[str, Any]) -> str:
    text = message.strip()
    risk_text = text.replace("提交用", "").replace("学校提交用", "")
    if any(marker in risk_text for marker in FORMAL_ACTION_MARKERS):
        return "formal_action"
    if state.get("candidate_exists") and any(marker in text for marker in MODIFY_MARKERS):
        return "modify"
    if any(marker in text for marker in GENERATE_MARKERS):
        return "create"
    return "clarify_or_continue"


def decide_action_mode(
    *,
    operation: str,
    artifact: str | None,
    sufficiency: dict[str, Any],
    risk: dict[str, Any],
) -> dict[str, Any]:
    if risk.get("requires_confirmation"):
        return {
            "mode": "ASK_CONFIRMATION",
            "teacher_reply_required": True,
            "model_candidate_required": False,
            "renderer_sync_required": False,
            "confirmation_required": True,
        }
    if risk.get("blocked"):
        return {
            "mode": "BLOCK_ACTION",
            "teacher_reply_required": True,
            "model_candidate_required": False,
            "renderer_sync_required": False,
            "confirmation_required": False,
        }
    if operation == "modify":
        return {
            "mode": "MODIFY_CANDIDATE",
            "teacher_reply_required": False,
            "model_candidate_required": True,
            "renderer_sync_required": True,
            "confirmation_required": False,
        }
    if not artifact:
        return {
            "mode": "CLARIFY_ARTIFACT",
            "teacher_reply_required": True,
            "model_candidate_required": False,
            "renderer_sync_required": False,
            "confirmation_required": False,
        }
    if sufficiency.get("can_produce_useful_result"):
        return {
            "mode": "GENERATE_CANDIDATE",
            "teacher_reply_required": False,
            "model_candidate_required": True,
            "renderer_sync_required": True,
            "confirmation_required": False,
        }
    return {
        "mode": "CLARIFY_KEY_SLOT",
        "teacher_reply_required": True,
        "model_candidate_required": False,
        "renderer_sync_required": False,
        "confirmation_required": False,
    }
