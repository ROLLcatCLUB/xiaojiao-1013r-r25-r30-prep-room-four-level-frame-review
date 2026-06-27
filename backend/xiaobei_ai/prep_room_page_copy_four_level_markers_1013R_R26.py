from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_four_level_frame_implementation_map_1013R_R25 as r25_frame_map
from . import prep_room_page_copy_package_binding_1013R_R21 as r21_page_binding


STAGE_ID = "1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS"
MARKER_ID = "SHIWEI_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r25_frame_map.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "page_copy_four_level_markers_defined": True,
            "runtime_dom_data_markers_added": True,
            "visible_layout_modified": False,
            "new_disconnected_page_created": False,
            "route_registered": False,
            "endpoint_registered": False,
            "component_implementation_created": False,
            "R36_modified": False,
            "main_shell_modified": False,
            "source_prototype_modified": False,
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


def marker_targets() -> list[dict[str, Any]]:
    return [
        {
            "level": 1,
            "level_key": "platform_shell",
            "selector_groups": [
                ".topbar",
                ".xiaobei-chat-entry",
                "#chatInput",
                "#statusMain",
            ],
            "role": "global_top_bar_and_bottom_xiaojiao_entry",
        },
        {
            "level": 2,
            "level_key": "room_workspace",
            "selector_groups": [
                ".canvas-stage",
                ".render-layer",
                "body[data-active-view='prepNotebook'] .nb-scene:not(.courseware-expanded-scene)",
                "body[data-active-view='prepNotebook'] .nb-binder",
            ],
            "role": "prep_room_workspace_and_dynamic_render_stage",
        },
        {
            "level": 3,
            "level_key": "tool_frame",
            "selector_groups": [
                ".nb-panel",
                ".nb-right-rail",
                ".nb-drawer",
                ".nb-state-bar",
                ".nb-doc-section-head .node-action",
                ".r21-big-unit-section-actions",
                ".courseware-r1e-toolbar",
            ],
            "role": "prep_room_tools_and_action_frames",
        },
        {
            "level": 4,
            "level_key": "content_rendering",
            "selector_groups": [
                ".nb-workspace",
                ".nb-doc-section",
                ".nb-flow-step",
                ".nb-step-detail-item",
                ".r21-big-unit-line",
                ".r36-edit-bubble",
                ".r6p-modal",
                ".courseware-screen-mini",
                ".courseware-screen-card",
                ".courseware-screen-row",
            ],
            "role": "lesson_content_candidate_cards_and_derivative_content",
        },
    ]


def build_marker_contract() -> dict[str, Any]:
    r25_bundle = r25_frame_map.build_implementation_sample_bundle()
    r21_bundle = r21_page_binding.build_binding_sample_bundle()
    html = r21_bundle.get("html", "")
    return {
        "ok": True,
        "stage": STAGE_ID,
        "marker_id": MARKER_ID,
        "generated_at": _now(),
        "consumes": {
            "r25_stage": r25_bundle.get("stage"),
            "r21_stage": r21_bundle.get("stage"),
            "current_surface": "R21 page copy",
        },
        "marker_data_attributes": [
            "data-shiwei-four-level-frame",
            "data-shiwei-four-level-stage",
            "data-shiwei-frame-route-rule",
            "data-shiwei-current-room",
            "data-shiwei-frame-level",
            "data-shiwei-frame-key",
            "data-shiwei-frame-role",
            "data-shiwei-frame-stage",
        ],
        "marker_targets": marker_targets(),
        "html_checks": {
            "has_marker_stage_id": STAGE_ID in html,
            "has_marker_function": "function markFourLevelFrames()" in html,
            "has_marker_state": "__SHIWEI_FOUR_LEVEL_FRAME_MARKERS__" in html,
            "has_level_attribute": "data-shiwei-frame-level" in html,
            "has_room_marker": "data-shiwei-current-room" in html,
        },
        "implementation_rule": {
            "visible_surface_remains_r21_page_copy": True,
            "no_new_html_page_written_by_r26": True,
            "markers_are_runtime_data_attributes": True,
            "markers_do_not_change_layout": True,
        },
        "next_stage_recommendation": {
            "stage": "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE",
            "why": "R21 can now expose four-level frame markers; next define a static Xiaojiao intent-to-frame router fixture without connecting a model.",
        },
        "boundary": boundary_flags(),
    }


def build_marker_sample_bundle() -> dict[str, Any]:
    contract = build_marker_contract()
    return {
        "stage": STAGE_ID,
        "marker_contract": contract,
        "marker_targets": deepcopy(contract["marker_targets"]),
        "boundary": deepcopy(contract["boundary"]),
    }
