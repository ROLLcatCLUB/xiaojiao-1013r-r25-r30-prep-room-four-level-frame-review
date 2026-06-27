from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from html import escape
from typing import Any

from . import prep_room_render_blocks_protocol_1013R_R17 as r17_blocks


STAGE_ID = "1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE"
ADAPTER_ID = "SHIWEI_LIGHT_RENDER_ADAPTER_SAMPLE_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r17_blocks.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "light_render_adapter_readonly": True,
            "light_render_adapter_defined": True,
            "route_registered": False,
            "existing_page_modified": False,
            "runtime_write_allowed": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
            "R36_modified": False,
            "main_shell_modified": False,
        }
    )
    return flags


def _block_summary(block: dict[str, Any]) -> str:
    state = block.get("render_state", "unknown")
    gate = block.get("gate_type", "unknown")
    actions = block.get("available_actions", [])
    if actions:
        action_text = " / ".join(str(item.get("label")) for item in actions[:2])
    else:
        action_text = "暂无可执行动作"
    return f"{state} · {gate} · {action_text}"


def render_block_html(block: dict[str, Any]) -> str:
    badges = "".join(f"<span>{escape(str(item))}</span>" for item in block.get("source_badges", []))
    return (
        f'<section class="r18-block" data-slot="{escape(str(block.get("slot_id")))}" '
        f'data-gate="{escape(str(block.get("gate_type")))}">'
        f'<div class="r18-block-head">'
        f'<strong>{escape(str(block.get("title") or block.get("slot_id")))}</strong>'
        f'<em>{escape(str(block.get("block_type")))}</em>'
        f"</div>"
        f'<p>{escape(_block_summary(block))}</p>'
        f'<div class="r18-badges">{badges}</div>'
        f"</section>"
    )


def render_sample_html(protocol: dict[str, Any] | None = None) -> str:
    if protocol is None:
        protocol = r17_blocks.build_render_blocks_protocol()
    blocks = protocol.get("render_blocks", [])
    body = "\n".join(render_block_html(block) for block in blocks)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>R18 备课室轻量渲染适配样板</title>
  <style>
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f7f3; color: #263f38; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 28px; }}
    h1 {{ font-size: 24px; margin: 0 0 8px; }}
    .r18-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }}
    .r18-block {{ min-height: 118px; border: 1px solid #d8e4dd; background: #fffdf7; border-radius: 8px; padding: 14px; box-sizing: border-box; }}
    .r18-block-head {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
    .r18-block-head strong {{ font-size: 15px; }}
    .r18-block-head em {{ font-style: normal; color: #5a756b; font-size: 12px; }}
    .r18-block p {{ color: #425e54; font-size: 13px; line-height: 1.5; }}
    .r18-badges {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .r18-badges span {{ border: 1px solid #d3e6dd; border-radius: 999px; padding: 3px 7px; font-size: 12px; color: #2d6f61; }}
  </style>
</head>
<body>
  <main>
    <h1>备课室轻量渲染适配样板</h1>
    <p>当前对象：2-1《色彩的渐变》。本页只渲染 R17 render_blocks，不写入、不调用模型、不 formal apply。</p>
    <div class="r18-grid">
{body}
    </div>
  </main>
</body>
</html>
"""


def build_render_adapter_sample() -> dict[str, Any]:
    protocol = r17_blocks.build_render_blocks_protocol()
    blocks = deepcopy(protocol.get("render_blocks", []))
    return {
        "ok": True,
        "stage": STAGE_ID,
        "adapter_id": ADAPTER_ID,
        "generated_at": _now(),
        "consumes": {
            "render_blocks_protocol_stage": protocol.get("stage"),
            "protocol_id": protocol.get("protocol_id"),
            "block_count": len(blocks),
        },
        "render_plan": {
            "layout": "three_column_block_grid",
            "block_count": len(blocks),
            "required_block_fields": ["block_id", "slot_id", "block_type", "title", "render_state", "gate_type"],
            "html_output": "static_sample_only",
        },
        "html": render_sample_html(protocol),
        "next_stage_recommendation": {
            "stage": "1013R_R19_DERIVATIVE_OBJECT_STATIC_LINKAGE_SAMPLE",
            "why": "轻量适配器已经能渲染 blocks；下一步把大屏、课件、学习单、评价表和教学过程建立静态联动。",
        },
        "boundary": boundary_flags(),
    }


def build_adapter_sample_bundle() -> dict[str, Any]:
    sample = build_render_adapter_sample()
    return {
        "stage": STAGE_ID,
        "light_render_adapter_sample": sample,
        "html": sample["html"],
        "boundary": deepcopy(sample["boundary"]),
    }
