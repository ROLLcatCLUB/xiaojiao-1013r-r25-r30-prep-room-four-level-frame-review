from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_main_shell_fetch_adapter_1013L_R5 as l5_shell_adapter
from . import prep_room_page_copy_package_binding_1013R_R21 as r21_page_binding
from . import prep_room_render_block_component_boundary_1013R_R24 as r24_component_boundary
from . import prep_room_render_blocks_protocol_1013R_R17 as r17_render_blocks
from . import prep_room_render_shell_registry_1013L_R0 as l0_shell_registry


STAGE_ID = "1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP"
MAP_ID = "SHIWEI_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r24_component_boundary.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "four_level_frame_implementation_map_defined": True,
            "history_viewer_used_as_index_only": True,
            "openclaw_runtime_imported": False,
            "openclaw_memory_imported": False,
            "page_dom_modified": False,
            "prototype_copy_created": False,
            "new_disconnected_page_created": False,
            "route_registered": False,
            "endpoint_registered": False,
            "component_implementation_created": False,
            "R36_modified": False,
            "main_shell_modified": False,
            "existing_page_modified": False,
            "runtime_connected": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
        }
    )
    return flags


def history_viewer_intake() -> dict[str, Any]:
    return {
        "source_url": "http://localhost:9876/history-viewer.html",
        "data_files": [
            "http://localhost:9876/data/timeline.json",
            "http://localhost:9876/data/inventory-l2.json",
            "http://localhost:9876/data/audit-log.json",
        ],
        "used_for": "asset_index_and_scan_clues_only",
        "not_used_for": [
            "product_truth",
            "runtime_decision",
            "field_standard",
            "provider_or_memory_binding",
        ],
        "observed_limits": [
            "inventory scan is L2/project-level",
            "scan_meta states code was not deeply read",
            "OpenClaw interpretation may diverge from product intent",
        ],
    }


def existing_asset_decisions() -> list[dict[str, Any]]:
    return [
        {
            "asset_id": "1013L_shell_registry_and_fetch_adapter",
            "decision": "reuse_as_level_1_and_level_2_backbone",
            "files": [
                "backend/xiaobei_ai/prep_room_render_shell_registry_1013L_R0.py",
                "backend/xiaobei_ai/prep_room_main_shell_fetch_adapter_1013L_R5.py",
            ],
            "why": "Already defines persistent shell, RenderStage states, and readonly fetch adapter boundaries.",
            "current_status": "bridge_now_contract_only",
        },
        {
            "asset_id": "1013R_unified_package_render_blocks_component_boundary",
            "decision": "reuse_as_level_4_render_contract",
            "files": [
                "backend/xiaobei_ai/prep_room_unified_viewmodel_1013R_R15.py",
                "backend/xiaobei_ai/prep_room_source_policy_validator_1013R_R16.py",
                "backend/xiaobei_ai/prep_room_render_blocks_protocol_1013R_R17.py",
                "backend/xiaobei_ai/prep_room_unified_package_readonly_export_1013R_R20.py",
                "backend/xiaobei_ai/prep_room_render_block_component_boundary_1013R_R24.py",
            ],
            "why": "These modules already turn the lesson object into render slots, render blocks, source policy, action gates, and future component boundaries.",
            "current_status": "connect_next_without_runtime",
        },
        {
            "asset_id": "1013R_R21_current_page_copy",
            "decision": "keep_as_visible_prototype_surface",
            "files": [
                "backend/xiaobei_ai/prep_room_page_copy_package_binding_1013R_R21.py",
                "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R21_page_copy_binds_unified_package/prep_room_page_copy_binds_unified_package_1013R_R21.html",
            ],
            "why": "User-facing prep-room adjustments must stay inside this existing page copy line unless a rollback copy is explicitly needed.",
            "current_status": "visible_surface_only",
        },
        {
            "asset_id": "1013K_big_unit_and_courseware_assets",
            "decision": "reuse_before_new_unit_or_courseware_fields",
            "files": [
                "backend/xiaobei_ai/prep_room_big_unit_render_viewmodel_1013K_R7.py",
                "backend/xiaobei_ai/prep_room_big_unit_renderer_fetch_adapter_1013K_R13.py",
                "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013K_R29A_courseware_viewmodel_normalization_before_visible_render/",
            ],
            "why": "Existing big-unit and courseware ViewModel chains explain where unit chunks, screen seeds, display preview, and courseware data should come from.",
            "current_status": "reuse_as_level_3_tool_sources",
        },
        {
            "asset_id": "platform_core_render_blocks_0954C",
            "decision": "reference_as_safety_and_type_registry_not_runtime",
            "files": [
                "platform_core/render_blocks/render_block_registry_contract_0954C.md",
                "platform_core/render_blocks/render_block_registry_0954C.js",
            ],
            "why": "It has a useful inactive render block registry and safety model, but its own contract says it is not imported into runtime.",
            "current_status": "reference_only_until_adapter_stage",
        },
        {
            "asset_id": "system_semantic_interaction_runtime",
            "decision": "reference_for_future_intent_command_gate_not_connected_now",
            "files": [
                "backend/xiaobei_ai/system_semantic_interaction_runtime/action_policy.py",
                "backend/xiaobei_ai/system_semantic_interaction_runtime/command_dsl.py",
                "backend/xiaobei_ai/system_semantic_interaction_runtime/side_effect_gate.py",
                "backend/xiaobei_ai/system_semantic_interaction_runtime/orchestrator.py",
            ],
            "why": "Existing command/gate concepts match the four-level route idea, but R25-R29 stay static/fixture and do not connect runtime.",
            "current_status": "future_bridge",
        },
        {
            "asset_id": "frontend_workbench_legacy_assets",
            "decision": "mine_for_patterns_not_new_page_line",
            "files": [
                "frontend/workbench/workbench_intent_router_v1.js",
                "frontend/workbench/workbench_preview_viewmodel_adapter_070G.js",
                "frontend/workbench/workbench_renderer_protocol_v1.js",
                "frontend/workbench/workbench_candidate_decision_v1.js",
            ],
            "why": "Workbench contains prior router, preview, renderer, and candidate-decision vocabulary; current prep-room work should not reopen a disconnected workbench page.",
            "current_status": "pattern_reference",
        },
        {
            "asset_id": "openclaw_history_and_scans",
            "decision": "archive_reference_only",
            "files": [
                "http://localhost:9876/history-viewer.html",
                "http://localhost:9876/data/inventory-l2.json",
                "docs/audit/openclaw_import_allowlist_067D.md",
                "docs/audit/capability_executor_coverage_inventory_067E.md",
            ],
            "why": "OpenClaw scan output is useful for locating old assets, but old policy forbids importing its runtime or memory.",
            "current_status": "do_not_bind_as_runtime",
        },
    ]


def four_level_implementation_map() -> dict[str, Any]:
    shell_registry = l0_shell_registry.render_stage_registry()
    shell_adapter = l5_shell_adapter.adapter_map()
    render_protocol = r17_render_blocks.build_render_blocks_protocol()
    component_boundary = r24_component_boundary.build_component_boundary_map()

    return {
        "ok": True,
        "stage": STAGE_ID,
        "map_id": MAP_ID,
        "generated_at": _now(),
        "framework_reference": "docs/1013R_product_frame_four_level.md",
        "history_viewer_intake": history_viewer_intake(),
        "consumes": {
            "l0_shell_registry_stage": shell_registry.get("stage"),
            "l5_shell_adapter_stage": shell_adapter.get("stage"),
            "r17_render_blocks_stage": render_protocol.get("stage"),
            "r21_page_binding_stage": r21_page_binding.STAGE_ID,
            "r24_component_boundary_stage": component_boundary.get("stage"),
        },
        "current_visible_surface": {
            "stage": r21_page_binding.STAGE_ID,
            "rule": "all visible prep-room prototype changes target the existing R21 page copy or an explicit rollback copy",
            "new_disconnected_page_allowed": False,
        },
        "levels": [
            {
                "level": 1,
                "level_key": "platform_shell",
                "teacher_name": "平台外壳框架",
                "responsibility": "Keep the Shiwei top global bar and bottom Xiaojiao entry stable across rooms.",
                "existing_sources": [
                    "1013L_R0 shell_shape.top_shell_persistent",
                    "1013L_R0 shell_shape.bottom_agent_bar_persistent",
                    "1013L_R5 main shell ViewModel adapter",
                    "R21 visible top bar and bottom composer DOM",
                ],
                "r26_marker_targets": [
                    "top global bar",
                    "global mode toolbar",
                    "bottom Xiaojiao composer",
                ],
                "must_not_do": [
                    "put room-specific lesson content into level 1",
                    "create another top-level static page for a room feature",
                ],
            },
            {
                "level": 2,
                "level_key": "room_workspace",
                "teacher_name": "各室工作空间框架",
                "responsibility": "Switch the teacher's work context by room while keeping Xiaojiao as one agent with room-specific duties.",
                "existing_sources": [
                    "1013L_R0 render_stage_registry",
                    "1013L_R5 state_fetch_adapters",
                    "R21 body[data-active-view='prepNotebook']",
                ],
                "room_states_now": deepcopy(shell_registry.get("states", [])),
                "planned_rooms": ["备课室", "教室", "研究室", "资料室", "评阅室", "档案室"],
                "r28_registry_seed": "derive room registry from 1013L states instead of inventing a parallel room list",
                "must_not_do": [
                    "turn each room into a separate chat page",
                    "hard-code six rooms into content components",
                ],
            },
            {
                "level": 3,
                "level_key": "tool_frame",
                "teacher_name": "工具框架",
                "responsibility": "Expose room-local tools that change the level-4 content mode and action gate.",
                "existing_sources": [
                    "1013L_R5 active_capability",
                    "1013R_R17 block_groups",
                    "1013R_R24 component_groups",
                    "R21 right rail / section action buttons / view-edit toggles",
                ],
                "tool_candidates": [
                    "备课本",
                    "大单元",
                    "单课",
                    "课件",
                    "大屏",
                    "资料",
                    "评价",
                    "周课表",
                    "查看编辑动作",
                ],
                "r29_registry_seed": "derive tool registry from L5 state_fetch_adapters plus R17 block_groups",
                "must_not_do": [
                    "mix tool controls into lesson prose",
                    "let a tool action bypass teacher confirmation gate",
                ],
            },
            {
                "level": 4,
                "level_key": "content_rendering",
                "teacher_name": "内容框架",
                "responsibility": "Render lesson text, unit chunks, process steps, cards, screen drafts, sources, and candidate edits.",
                "existing_sources": [
                    "1013R_R15 render_slots",
                    "1013R_R17 render_blocks",
                    "1013R_R20 unified package",
                    "1013R_R24 component boundary entries",
                    "1013R_R21 R36 edit bubble reuse and big-unit row binding",
                ],
                "content_blocks_now": deepcopy(render_protocol.get("render_blocks", [])),
                "component_boundary_now": deepcopy(component_boundary.get("component_boundary_entries", [])),
                "r26_marker_targets": [
                    "lesson document sections",
                    "teaching process rows",
                    "big-unit numbered rows",
                    "R36 edit bubble",
                    "right rail screen draft rows",
                ],
                "must_not_do": [
                    "promote AI draft to standard source",
                    "save, export, archive, or assess without preview and teacher confirmation",
                ],
            },
        ],
        "asset_decisions": existing_asset_decisions(),
        "implementation_sequence": [
            {
                "stage": "1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS",
                "purpose": "Add data-level markers inside the current R21 page copy only.",
                "depends_on": ["1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP"],
            },
            {
                "stage": "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE",
                "purpose": "Create static intent-to-level routing fixture, no model/provider/runtime.",
                "depends_on": ["1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP"],
            },
            {
                "stage": "1013R_R28_ROOM_WORKSPACE_REGISTRY",
                "purpose": "Derive room registry from 1013L states and current product rooms.",
                "depends_on": ["1013L_R0_MAIN_RENDER_SHELL_BASELINE_AND_BACKEND_REUSE_REGISTRY"],
            },
            {
                "stage": "1013R_R29_TOOL_FRAME_REGISTRY",
                "purpose": "Derive tool frame registry from L5 active capabilities and R17/R24 render groups.",
                "depends_on": ["1013L_R5_MAIN_SHELL_BACKEND_VIEWMODEL_READONLY_FETCH_ADAPTER", "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0"],
            },
        ],
        "routing_principles": {
            "route_intent_by_framework_level": True,
            "diagnose_issues_by_framework_level": True,
            "assign_features_by_framework_level": True,
            "implement_recursively_by_framework_level": True,
            "recursive_order": ["level_1_platform_shell", "level_2_room_workspace", "level_3_tool_frame", "level_4_content_rendering"],
        },
        "boundary": boundary_flags(),
    }


def build_implementation_sample_bundle() -> dict[str, Any]:
    frame_map = four_level_implementation_map()
    return {
        "stage": STAGE_ID,
        "implementation_map": frame_map,
        "levels": deepcopy(frame_map["levels"]),
        "asset_decisions": deepcopy(frame_map["asset_decisions"]),
        "implementation_sequence": deepcopy(frame_map["implementation_sequence"]),
        "boundary": deepcopy(frame_map["boundary"]),
    }
