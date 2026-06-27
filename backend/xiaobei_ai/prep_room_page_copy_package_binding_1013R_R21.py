from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json

from . import prep_room_unified_package_readonly_export_1013R_R20 as r20_package


STAGE_ID = "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE"
BINDING_ID = "SHIWEI_PREP_ROOM_PAGE_COPY_PACKAGE_BINDING_R0"
ROOT = Path(__file__).resolve().parents[2]
PROTOTYPE_BASE_STAGE = "1013R_R11_prep_room_fetch_r10_viewmodel_static_binding"
PROTOTYPE_BASE_PATH = (
    ROOT
    / "outputs"
    / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
    / PROTOTYPE_BASE_STAGE
    / "prep_room_render_canvas_deepen_v1_1013R_R11_prep_room_fetch_r10_viewmodel_static_binding.html"
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r20_package.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "prototype_copy_created": True,
            "page_copy_created": True,
            "page_binds_unified_package": True,
            "internal_prototype_binding": True,
            "external_protocol_band_created": False,
            "new_blank_static_page_created": False,
            "source_prototype_modified": False,
            "route_registered": False,
            "endpoint_registered": False,
            "R36_modified": False,
            "main_shell_modified": False,
            "existing_page_modified": False,
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


def _read_prototype_base() -> str:
    return PROTOTYPE_BASE_PATH.read_text(encoding="utf-8", errors="ignore")


def _compact_package(package: dict[str, Any]) -> dict[str, Any]:
    lesson = package.get("lesson_viewmodel", {}).get("current_lesson", {})
    return {
        "stage": STAGE_ID,
        "package_id": package.get("package_id"),
        "current_object": deepcopy(package.get("current_object", {})),
        "task_state": deepcopy(package.get("task_state", {})),
        "teacher_action_gate": deepcopy(package.get("teacher_action_gate", {})),
        "source_policy_checks": deepcopy(package.get("source_policy_result", {}).get("checks", [])),
        "render_blocks": deepcopy(package.get("render_blocks", [])),
        "derivative_linkage": deepcopy(package.get("derivative_linkage", {})),
        "lesson": {
            "sections": deepcopy(lesson.get("sections", [])),
            "process_steps": deepcopy(lesson.get("process_steps", [])),
            "flow": deepcopy(lesson.get("flow", [])),
            "badges": deepcopy(lesson.get("badges", [])),
            "big_screen_short_text": deepcopy(lesson.get("big_screen_short_text", [])),
        },
        "courseware_screens": deepcopy(package.get("lesson_viewmodel", {}).get("courseware_screens", [])),
    }


def _internal_binding_style() -> str:
    return """
  <style id="style-1013R-R21-internal-prototype-binding">
    [data-1013r-r21-internal-bound="true"] .r21-inline-chip {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      border: 1px solid rgba(66, 108, 95, .2);
      border-radius: 999px;
      padding: 3px 7px;
      color: #426c5f;
      background: rgba(247, 251, 248, .92);
      font-size: 11px;
      font-weight: 700;
      white-space: nowrap;
    }
    [data-1013r-r21-internal-bound="true"] .r21-inline-chip.is-quiet {
      display: none;
    }
    [data-1013r-r21-internal-bound="true"] .r21-inline-chip.warn {
      color: #8a5653;
      border-color: rgba(138, 86, 83, .24);
      background: rgba(251, 244, 242, .92);
    }
    [data-1013r-r21-internal-bound="true"] .r21-inline-note {
      margin-top: 6px;
      color: #5c6f68;
      font-size: 12px;
      line-height: 1.45;
    }
    [data-1013r-r21-internal-bound="true"] .r21-derived-mini {
      display: grid;
      gap: 5px;
      margin-top: 8px;
    }
    [data-1013r-r21-internal-bound="true"] .r21-derived-mini span {
      border-left: 3px solid rgba(66, 108, 95, .35);
      padding-left: 7px;
      color: #20342f;
      font-size: 12px;
      line-height: 1.45;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble {
      width: min(462px, calc(100vw - 30px)) !important;
      max-width: calc(100vw - 30px) !important;
      overflow: visible;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel {
      box-sizing: border-box;
      width: 100%;
      max-width: 100%;
      border-radius: 10px;
      overflow-x: hidden;
      overflow-y: visible;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto auto auto;
      gap: 8px;
      align-items: center;
      overflow: visible;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title > div:first-child {
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      font-size: 14px;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-edit-title-action {
      color: #5f4a2b;
      font-weight: 800;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-edit-title-target {
      color: #20342f;
      font-weight: 800;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title > span,
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title .r21-edit-state-pill {
      writing-mode: horizontal-tb !important;
      white-space: nowrap;
      border-radius: 999px;
      padding: 3px 8px;
      background: #f7fbf8;
      color: #426c5f;
      border: 1px solid rgba(66, 108, 95, .2);
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title .r21-edit-state-pill {
      justify-self: end;
      font-size: 12px;
      font-weight: 700;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-impact-help {
      position: relative;
      display: inline-grid;
      place-items: center;
      width: 22px;
      height: 22px;
      border-radius: 999px;
      border: 1px solid rgba(217, 119, 6, .28);
      background: #fff7ed;
      color: #b45309;
      font-size: 13px;
      font-weight: 800;
      cursor: help;
      justify-self: end;
      z-index: 4;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-impact-help-popover {
      position: absolute;
      top: 28px;
      right: 0;
      display: none;
      width: min(300px, calc(100vw - 56px));
      max-height: 176px;
      overflow: auto;
      padding: 10px 12px;
      border: 1px solid rgba(217, 119, 6, .24);
      border-radius: 10px;
      background: #fffaf2;
      box-shadow: 0 14px 30px rgba(64, 49, 23, .16);
      color: #5f4a2b;
      font-size: 12px;
      line-height: 1.55;
      text-align: left;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: break-word;
      z-index: 30;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-impact-help:hover .r21-impact-help-popover,
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-impact-help:focus .r21-impact-help-popover,
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .r21-impact-help:focus-within .r21-impact-help-popover {
      display: block;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title > button,
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-panel-title .nb-soft-button {
      width: auto;
      min-width: 44px;
      justify-self: end;
      padding: 3px 8px;
      border-radius: 999px;
      line-height: 1.2;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-surface {
      grid-template-columns: 1fr;
      min-width: 0;
      overflow-x: hidden;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-before-after {
      grid-template-columns: 1fr;
      min-width: 0;
      overflow-x: hidden;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-surface-block {
      max-height: 136px;
      min-width: 0;
      overflow-y: auto;
      overflow-x: hidden;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-surface-block strong {
      color: #426c5f;
      font-size: 12px;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-surface-block strong.r21-coffee-label {
      color: #5f4a2b;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-surface-block.r21-edit-after {
      border-color: rgba(95, 74, 43, .42);
      background: #fffaf2;
      color: #5f4a2b;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-tools {
      justify-content: flex-end;
      flex-wrap: wrap;
      gap: 6px;
      border-top: 1px solid rgba(66, 108, 95, .12);
      padding-top: 8px;
      overflow-x: hidden;
    }
    [data-1013r-r21-internal-bound="true"] .r36-edit-bubble .nb-edit-tools .nb-soft-button {
      flex: 0 0 auto;
      max-width: 132px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal {
      width: min(620px, calc(100vw - 48px)) !important;
      max-height: min(700px, calc(100vh - 80px)) !important;
      overflow: visible;
      border-radius: 12px;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-head {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto auto;
      align-items: center;
      gap: 8px;
      overflow: visible;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-head > div:first-child {
      min-width: 0;
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto auto;
      align-items: center;
      gap: 8px;
      overflow: visible;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-title {
      grid-column: 1 / 2;
      grid-row: 1;
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      color: #20342f;
      font-size: 14px;
      font-weight: 850;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-status {
      grid-column: 3 / 4;
      grid-row: 1;
      justify-self: end;
      writing-mode: horizontal-tb !important;
      white-space: nowrap;
      border-radius: 999px;
      padding: 3px 8px;
      background: #f7fbf8;
      color: #426c5f;
      border: 1px solid rgba(66, 108, 95, .2);
      font-size: 12px;
      font-weight: 700;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-status::before {
      display: none;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-impact-help {
      position: relative;
      display: inline-grid;
      place-items: center;
      width: 22px;
      height: 22px;
      border-radius: 999px;
      border: 1px solid rgba(217, 119, 6, .28);
      background: #fff7ed;
      color: #b45309;
      font-size: 13px;
      font-weight: 800;
      cursor: help;
      justify-self: end;
      z-index: 5;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-impact-popover {
      position: absolute;
      top: 28px;
      right: 0;
      display: none;
      width: min(320px, calc(100vw - 56px));
      max-height: 190px;
      overflow: auto;
      padding: 10px 12px;
      border: 1px solid rgba(217, 119, 6, .24);
      border-radius: 10px;
      background: #fffaf2;
      box-shadow: 0 14px 30px rgba(64, 49, 23, .16);
      color: #5f4a2b;
      font-size: 12px;
      line-height: 1.55;
      text-align: left;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-impact-help:hover .r6p-modal-impact-popover,
    [data-1013r-r21-internal-bound="true"] .r6p-modal-impact-help:focus .r6p-modal-impact-popover,
    [data-1013r-r21-internal-bound="true"] .r6p-modal-impact-help:focus-within .r6p-modal-impact-popover {
      display: block;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-body {
      gap: 9px;
      min-width: 0;
      overflow-x: hidden;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card {
      max-height: 150px;
      min-width: 0;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 10px 11px;
      border: 1px solid rgba(197, 207, 194, .42);
      border-radius: 8px;
      background: rgba(255, 255, 255, .72);
      color: #20342f;
      font-size: 13px;
      line-height: 1.58;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card strong {
      display: block;
      margin-bottom: 5px;
      color: #5f4a2b;
      font-size: 12px;
      font-weight: 800;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card.r21-edit-after {
      border-color: rgba(95, 74, 43, .42);
      background: #fffaf2;
      color: #5f4a2b;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card.r21-xiaojiao-advice {
      max-height: 170px;
      background: rgba(255, 250, 242, .76);
      border-color: rgba(217, 119, 6, .18);
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card .r21-advice-muted {
      margin-top: 7px;
      color: #5f4a2b;
      font-size: 12px;
      line-height: 1.5;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-card details {
      margin-top: 7px;
      color: #5f4a2b;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-actions {
      justify-content: flex-end;
      flex-wrap: wrap;
      gap: 6px;
      border-top: 1px solid rgba(66, 108, 95, .12);
      padding-top: 8px;
      overflow-x: hidden;
    }
    [data-1013r-r21-internal-bound="true"] .r6p-modal-actions .node-action {
      flex: 0 0 auto;
      max-width: 132px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      border-radius: 999px;
    }
    [data-1013r-r21-internal-bound="true"] [data-r21-big-unit-lines="true"] {
      display: grid;
      gap: 6px;
      margin: 4px 0 2px;
      padding: 0;
      list-style: none;
      counter-reset: big-unit-line;
    }
    [data-1013r-r21-internal-bound="true"] [data-r21-big-unit-lines="true"] .r21-big-unit-line {
      display: block;
      padding-left: 34px;
      color: #2f3936;
      line-height: 1.72;
    }
    [data-1013r-r21-internal-bound="true"] [data-r21-big-unit-lines="true"] .r21-big-unit-line::before {
      counter-increment: big-unit-line;
      content: counter(big-unit-line) ".";
      position: absolute;
      left: 11px;
      top: 7px;
      color: #d18a2b;
      font-weight: 850;
      font-size: 13px;
    }
    [data-1013r-r21-internal-bound="true"] [data-r21-big-unit-lines="true"] .r21-big-unit-line:hover {
      background: rgba(244, 248, 245, 0.95);
      box-shadow: inset 3px 0 0 rgba(55, 126, 103, 0.36);
    }
    [data-1013r-r21-internal-bound="true"] [data-r21-big-unit-lines="true"] .r21-big-unit-line.selected {
      background: rgba(255, 248, 237, 0.98);
      box-shadow: inset 3px 0 0 var(--amber, #d18a2b);
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] {
      --r21-bottom-composer-space: 146px;
      --r21-binder-cover-inset: 14px;
      --r21-binder-gutter-width: 24px;
      --r21-prep-scene-height: calc(100vh - 148px - var(--r21-bottom-composer-space));
      --r21-prep-column-height: calc(var(--r21-prep-scene-height) - (var(--r21-binder-cover-inset) * 2));
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) {
      height: var(--r21-prep-scene-height) !important;
      max-height: var(--r21-prep-scene-height) !important;
      min-height: 0 !important;
      overflow: hidden !important;
      box-sizing: border-box;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) > .nb-binder {
      height: 100% !important;
      max-height: 100% !important;
      min-height: 0 !important;
      grid-template-columns: minmax(260px, 0.32fr) var(--r21-binder-gutter-width) minmax(520px, 1fr) !important;
      padding: var(--r21-binder-cover-inset) !important;
      overflow: hidden !important;
      align-items: stretch !important;
      box-sizing: border-box;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail {
      max-height: var(--r21-prep-column-height) !important;
      min-height: 0 !important;
      overflow-y: auto !important;
      overscroll-behavior: contain;
      scrollbar-gutter: auto;
      scrollbar-width: thin;
      scrollbar-color: rgba(42, 88, 73, .58) transparent;
      box-sizing: border-box;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel::-webkit-scrollbar,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace::-webkit-scrollbar,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer::-webkit-scrollbar,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail::-webkit-scrollbar {
      width: 6px !important;
      height: 6px !important;
      background: transparent !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail::-webkit-scrollbar-button {
      display: none !important;
      width: 0 !important;
      height: 0 !important;
      background: transparent !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel::-webkit-scrollbar-track,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace::-webkit-scrollbar-track,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer::-webkit-scrollbar-track,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail::-webkit-scrollbar-track,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel::-webkit-scrollbar-track-piece,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace::-webkit-scrollbar-track-piece,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer::-webkit-scrollbar-track-piece,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail::-webkit-scrollbar-track-piece {
      background: transparent !important;
      border: 0 !important;
      box-shadow: none !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel::-webkit-scrollbar-thumb,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace::-webkit-scrollbar-thumb,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-drawer::-webkit-scrollbar-thumb,
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-right-rail::-webkit-scrollbar-thumb {
      min-height: 54px;
      border: 0 !important;
      border-radius: 999px;
      background: rgba(42, 88, 73, .58) !important;
      box-shadow: none !important;
    }
    html[data-1013r-r21-internal-bound="true"]::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] body::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .canvas-stage::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .render-layer::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-scene::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-binder::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-panel::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-workspace::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-drawer::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] .nb-right-rail::-webkit-scrollbar-button,
    html[data-1013r-r21-internal-bound="true"] *::-webkit-scrollbar-button:vertical:start:decrement,
    html[data-1013r-r21-internal-bound="true"] *::-webkit-scrollbar-button:vertical:end:increment {
      display: none !important;
      width: 0 !important;
      height: 0 !important;
      min-width: 0 !important;
      min-height: 0 !important;
      background: transparent !important;
      border: 0 !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel {
      height: var(--r21-prep-column-height) !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace {
      height: var(--r21-prep-column-height) !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-gutter {
      min-height: 0 !important;
      height: var(--r21-prep-column-height) !important;
      align-self: stretch;
      border-top: 0 !important;
      border-bottom: 0 !important;
      background:
        linear-gradient(90deg,
          #214f42 0%,
          #5f8575 32%,
          #86aa9a 49%,
          #5a7e70 66%,
          #214d40 100%) !important;
      box-shadow:
        inset 5px 0 10px rgba(10, 42, 33, .28),
        inset -5px 0 10px rgba(10, 42, 33, .24) !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-gutter::before {
      inset: 0 !important;
      background:
        linear-gradient(90deg,
          rgba(12, 45, 35, .20),
          rgba(255, 255, 255, .08) 48%,
          rgba(12, 45, 35, .18)) !important;
      opacity: .42 !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-panel {
      border-right: 0 !important;
      box-shadow: -8px 12px 26px rgba(23, 30, 25, .14) !important;
    }
    html[data-1013r-r21-internal-bound="true"][data-1013l-r36-independent-scroll="true"] body[data-active-view="prepNotebook"] .nb-scene:not(.courseware-expanded-scene) .nb-workspace {
      border-left: 0 !important;
      box-shadow: 8px 12px 26px rgba(23, 30, 25, .14) !important;
    }
  </style>
"""


def _internal_binding_script(package: dict[str, Any]) -> str:
    payload = json.dumps(_compact_package(package), ensure_ascii=False)
    return f"""
  <script id="data-1013R-R21-unified-package" type="application/json">{payload}</script>
  <script id="script-1013R-R21-internal-prototype-binding">
    (() => {{
      const STAGE_ID = "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE";
      const FRAME_STAGE_ID = "1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS";
      const INTERNAL_TARGETS = [
        "model.views.prepNotebook.current_lesson",
        "model.views.prepNotebook.current_lesson.right_panels",
        "model.views.prepNotebook.current_lesson.reasoning_trace",
        "data-shiwei-frame-level",
        "data-shiwei-frame-key",
        "chatInput.placeholder",
        "statusMain",
        ".nb-state-bar",
        ".nb-doc-section-head",
        ".nb-flow-step",
        ".nb-drawer"
      ];
      const dataNode = document.getElementById("data-1013R-R21-unified-package");
      const packageData = JSON.parse(dataNode?.textContent || "{{}}");

      function esc(value) {{
        return String(value ?? "").replace(/[&<>"']/g, (ch) => ({{ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }}[ch]));
      }}

      function cleanTeacherText(value) {{
        return String(value ?? "")
          .replace(/\\s*lesson_body\\s*/g, " ")
          .replace(/\\s*进入编辑\\s*/g, " ")
          .replace(/\\s*编辑本段\\s*/g, " ")
          .replace(/\\s*收起编辑\\s*/g, " ")
          .replace(/\\s+/g, " ")
          .trim();
      }}

      function splitLessonTitle(rawTitle) {{
        const title = String(rawTitle || "2-1《色彩的渐变》").trim();
        const match = title.match(/^([0-9]+-[0-9]+)\\s*《(.+)》$/);
        if (!match) return {{ code: "2-1", title }};
        return {{ code: match[1], title: match[2] }};
      }}

      function teacherTitle(rawTitle, fallback) {{
        return String(rawTitle || fallback || "")
          .replace(/^\\s*[一二三四五六七八九十]+[、.．]\\s*/, "")
          .replace(/^\\s*\\d+[、.．]\\s*/, "")
          .trim();
      }}

      function normalizeSections(sections) {{
        return (Array.isArray(sections) ? sections : []).map((section, index) => ({{
          id: section.id || `r21_section_${{index + 1}}`,
          title: teacherTitle(section.title, `备课要点 ${{index + 1}}`),
          status: index === 0 ? "已定位" : "待确认",
          sources: index === 0 ? ["教材依据"] : [],
          body: Array.isArray(section.items) ? section.items : [],
        }}));
      }}

      function processDetailMap() {{
        return {{
          r21_intro: {{
            hover: "先让学生从真实图像和教材页里看见渐变，再收束到“慢慢变化”的核心判断。",
            role: "导入观察",
            design: "从自然图片和教材页入手，避免直接讲术语。",
            transition: "从看见颜色变化，转入同一种颜色如何一步步变浅、变深或变灰。",
            student: "学生先找变化位置，再用自己的话描述颜色从哪里到哪里。",
            risk: "学生可能只说漂亮或颜色多，需要追问变化方向。",
            details: [
              ["展现差异", "出示天空、花瓣、夕阳或教材页中的渐变图，请学生先找哪里从深到浅、从鲜到灰慢慢变化。"],
              ["指认方向", "让学生用手指沿色带走一遍，说出颜色是往亮、往暗、往淡还是往灰变化。"],
              ["收住发现", "教师只收一句：渐变不是几种颜色并排放，而是一步一步慢慢变。"],
            ],
          }},
          r21_sense: {{
            hover: "把明度、纯度先变成可比较的色卡排序，再让学生用语言说出判断依据。",
            role: "概念建立",
            design: "同一颜色加入白色、黑色或灰色，先观察再命名。",
            transition: "从观察差异转入亲手试色，验证每一步只改变一点。",
            student: "学生通过排序、比较、解释，建立浅深、鲜灰和层次变化的感觉。",
            risk: "学生容易把明度和纯度混说，先允许口语表达，再由教师归纳。",
            details: [
              ["建立比较", "同一种颜色分别加入白色、黑色或灰色，先不急着讲定义，只让学生看哪一格更亮、哪一格更灰。"],
              ["排序判断", "给学生 3 到 5 张色卡，让他们按从浅到深或从鲜到灰排成一排。"],
              ["说出依据", "追问：你为什么把这一格放在这里？让学生说到亮一点、暗一点、灰一点。"],
            ],
          }},
          r21_explore: {{
            hover: "示范少量多次加色，保留试色纸作为过程证据，避免学生一次性把颜色调脏。",
            role: "方法示范",
            design: "教师示范每一步只改变一点，学生马上用试色纸跟做。",
            transition: "从小色阶练习转入正式画面，把试出的色阶迁移到对象层次。",
            student: "学生完成 3 到 5 格渐变色阶，边试边比较相邻两格是否跳得太大。",
            risk: "一次加色过多会导致颜色变脏，需要用中间补格的办法修正。",
            details: [
              ["示范方法", "教师从一个原色开始，每次只加一点白色、水或相邻颜色，边调边放到下一格。"],
              ["学生试色", "学生在试色纸上完成 3 到 5 格小色阶，每一步只改变一点，不追求一次调准。"],
              ["及时修正", "如果两格跳得太大，教师提醒回到中间再补一格，让渐变变得更连续。"],
              ["留下证据", "试色纸不扔掉，作为作品旁边的过程证据，用来说明自己怎么调出来。"],
            ],
          }},
          r21_make: {{
            hover: "把渐变方法迁移到动物、植物、建筑或校园空间，形成有层次的画面。",
            role: "创作迁移",
            design: "先选对象，再把试色结果迁移到画面中的光影、远近或情绪变化。",
            transition: "从制作过程转入作品说明，让学生用证据解释自己的渐变方向。",
            student: "学生选择一个对象，把渐变规律转化为画面层次，而不是只涂满颜色。",
            risk: "学生可能把色块并排涂，教师要提醒相邻区域保持连续变化。",
            details: [
              ["选择对象", "提示学生可选择动物、植物、建筑或校园空间，先确定渐变从哪里开始、到哪里结束。"],
              ["迁移色阶", "把试色纸上最合适的一组色阶迁移到正式画面，先铺大关系，再补细节。"],
              ["控制层次", "提醒学生每一层只比前一层亮一点、暗一点或灰一点，避免突然跳色。"],
              ["保留调整", "作品旁边保留一处试色证据，便于后面说清自己怎样调整颜色。"],
            ],
          }},
          r21_share: {{
            hover: "分享不是只说好看，而是用试色纸、画面层次和同伴反馈说明渐变是否成立。",
            role: "评价表达",
            design: "用证据说清楚渐变方向、调色方法和画面效果。",
            transition: "收束到本课核心：颜色可以通过一步一步的变化形成节奏和层次。",
            student: "学生能指着作品和试色纸说明自己的颜色变化过程。",
            risk: "评价容易停在喜欢/不喜欢，要用评价维度把话拉回证据。",
            details: [
              ["选证据", "请学生把作品和试色纸放在一起，指出最能说明渐变的一段颜色。"],
              ["说出理由", "用一句话说明：我的颜色从哪里变到哪里，中间每一步改变了什么。"],
              ["同伴反馈", "同伴只反馈一件事：哪一处变化最连续，哪一处还可以再补一格。"],
              ["收束下课", "教师归纳：渐变让颜色从一个状态慢慢走到另一个状态，也让画面更有层次。"],
            ],
          }},
        }};
      }}

      function normalizeProcessSteps(steps, links) {{
        const linkMap = new Map((Array.isArray(links) ? links : []).map((item) => [String(item.process_step_id || ""), item]));
        const times = ["4分钟", "8分钟", "10分钟", "13分钟", "5分钟"];
        const detailMap = processDetailMap();
        return (Array.isArray(steps) ? steps : []).map((step, index) => {{
          const link = linkMap.get(String(step.id || "")) || links[index] || {{}};
          const stepId = `r21_${{step.id || index + 1}}`;
          const detail = detailMap[stepId] || {{}};
          return {{
            id: stepId,
            name: step.title || `教学步骤 ${{index + 1}}`,
            time: times[index] || "",
            summary: [step.teacher_action, step.student_action].filter(Boolean).join(" "),
            readable_hover: detail.hover || "",
            readable_details: detail.details || [],
            tags: [
              link.courseware_screen?.title,
              link.classroom_display?.student_visible_prompt,
              link.worksheet?.render_state,
              link.assessment_rubric?.render_state,
            ].filter(Boolean).slice(0, 3),
            intent: {{
              role: detail.role || "",
              design: detail.design || "",
              transition: detail.transition || "",
              student: detail.student || "",
              teacher: step.teacher_action || "",
              activity: step.student_action || "",
              screen: link.classroom_display?.student_visible_prompt || step.screen_seed || "",
              material: link.worksheet?.capture_prompt || "",
              evidence: link.assessment_rubric?.evidence || step.evidence || "",
              risk: detail.risk || "",
            }},
          }};
        }});
      }}

      function normalizeCoursewareScreens(screens) {{
        return (Array.isArray(screens) ? screens : []).map((screen, index) => ({{
          id: `r21_courseware_${{screen.screen_no || index + 1}}`,
          index: String(screen.screen_no || index + 1).padStart(2, "0"),
          title: screen.title || `屏幕 ${{index + 1}}`,
          screen_title: screen.title || `屏幕 ${{index + 1}}`,
          lesson_link: screen.role || "课堂推进",
          classroom_text: screen.role || "课堂推进",
          placeholder: screen.status || "待确认",
          status: screen.status || "待确认",
          purpose: screen.role || "课堂推进",
          materials: [screen.status || "待确认"],
          suggestion: "来自当前备课预览；教师确认前不导出、不写入。",
          tools: ["精修", "补素材", "确认"],
        }}));
      }}

      function buildRightPanels(pkg) {{
        const known = pkg.task_state?.known_materials || [];
        const missing = pkg.task_state?.missing_materials || [];
        const actions = pkg.teacher_action_gate?.action_matrix || [];
        const checks = pkg.source_policy_checks || [];
        return {{
          view: [
            {{ title: "小教已知道", tag: "已知", items: known.map((item) => item.label || item.id).slice(0, 5) }},
            {{ title: "小教还需要", tag: "缺口", items: missing.map((item) => item.label || item.id).slice(0, 5) }},
            {{ title: "教师确认动作", tag: "门控", items: actions.map((action) => `${{action.label || action.action_id}} · ${{action.gate_type}}`).slice(0, 6) }},
            {{ title: "资料来源轻校验", tag: "依据", items: checks.map((check) => check.label || check.check_id).slice(0, 5) }},
          ],
          edit: [
            {{ title: "预览后确认", tag: "不写入", items: ["继续精修备课正文", "生成课件脚本预览", "生成大屏呈现预览", "评价表需补评价维度"] }},
          ],
        }};
      }}

      function buildReasoningTrace(pkg) {{
        const title = pkg.current_object?.title || "2-1《色彩的渐变》";
        return {{
          status: "current",
          active_index: 1,
          teacher_input: "小教正在把本课材料整理到备课页内部字段。",
          result: `${{title}} 已进入原型内预览态，保存、导出、评价写入仍需教师确认。`,
          stages: [
            {{ title: "STEP 1 场景定位", desc: "当前空间为备课室，当前对象保持三年级第二单元第1课《色彩的渐变》。" }},
            {{ title: "STEP 2 材料与缺口", desc: "已知材料和缺口写入原页面右侧状态卡。" }},
            {{ title: "STEP 3 派生联动", desc: "教学过程与课件、大屏、学习单、评价表建立内部联动。" }},
            {{ title: "STEP 4 教师确认", desc: "保存、导出、正式评价、归档全部停在确认门或阻断态。" }},
          ],
        }};
      }}

      function markFrameElement(element, level, key, role) {{
        if (!element) return 0;
        element.setAttribute("data-shiwei-frame-level", String(level));
        element.setAttribute("data-shiwei-frame-key", key);
        element.setAttribute("data-shiwei-frame-role", role);
        element.setAttribute("data-shiwei-frame-stage", FRAME_STAGE_ID);
        return 1;
      }}

      function markFrameElements(selector, level, key, role) {{
        return Array.from(document.querySelectorAll(selector)).reduce((count, element) => {{
          return count + markFrameElement(element, level, key, role);
        }}, 0);
      }}

      function markFourLevelFrames() {{
        const counts = {{
          level_1: 0,
          level_2: 0,
          level_3: 0,
          level_4: 0,
        }};
        document.documentElement.setAttribute("data-shiwei-four-level-frame", "true");
        document.documentElement.setAttribute("data-shiwei-four-level-stage", FRAME_STAGE_ID);
        document.documentElement.setAttribute("data-shiwei-frame-route-rule", "level_1_to_level_4_recursive");
        document.body?.setAttribute("data-shiwei-current-room", "prep_room");
        document.body?.setAttribute("data-shiwei-current-room-label", "备课室");
        counts.level_1 += markFrameElement(document.body, 1, "platform_shell", "shiwei_global_shell_root");
        counts.level_1 += markFrameElements(".topbar", 1, "platform_top_shell", "global_top_bar");
        counts.level_1 += markFrameElements(".xiaobei-chat-entry", 1, "platform_bottom_xiaojiao_entry", "bottom_xiaojiao_input_status");
        counts.level_1 += markFrameElements("#chatInput, #statusMain", 1, "platform_bottom_xiaojiao_entry", "bottom_xiaojiao_input_status");

        counts.level_2 += markFrameElements(".canvas-stage, .render-layer", 2, "room_stage_container", "dynamic_room_render_stage");
        counts.level_2 += markFrameElements("body[data-active-view='prepNotebook'] .nb-scene:not(.courseware-expanded-scene)", 2, "prep_room_workspace", "备课室");
        counts.level_2 += markFrameElements("body[data-active-view='prepNotebook'] .nb-binder", 2, "prep_room_binder", "备课室活页夹结构");

        counts.level_3 += markFrameElements(".nb-panel", 3, "prep_room_directory_tool", "备课本目录工具");
        counts.level_3 += markFrameElements(".nb-right-rail, .nb-drawer", 3, "prep_room_side_tool_frame", "资源依据大屏工具");
        counts.level_3 += markFrameElements(".nb-state-bar", 3, "prep_room_task_status_tool", "小教状态工具");
        counts.level_3 += markFrameElements(".nb-doc-section-head .node-action, .r21-big-unit-section-actions, .courseware-r1e-toolbar", 3, "prep_room_content_action_tool", "查看编辑确认工具");

        counts.level_4 += markFrameElements(".nb-workspace", 4, "prep_room_content_workspace", "备课内容承载区");
        counts.level_4 += markFrameElements(".nb-doc-section", 4, "lesson_document_section", "备课正文章节");
        counts.level_4 += markFrameElements(".nb-flow-step", 4, "teaching_process_step", "教学过程环节");
        counts.level_4 += markFrameElements(".nb-step-detail-item, .r21-big-unit-line", 4, "content_editable_paragraph", "可查看修改段落");
        counts.level_4 += markFrameElements(".r36-edit-bubble, .r6p-modal", 4, "candidate_edit_card", "修改前修改后小教建议");
        counts.level_4 += markFrameElements(".courseware-screen-mini, .courseware-screen-card, .courseware-screen-row", 4, "classroom_display_or_courseware_content", "大屏课件草稿内容");

        window.__SHIWEI_FOUR_LEVEL_FRAME_MARKERS__ = {{
          stage: FRAME_STAGE_ID,
          current_room: "prep_room",
          counts,
          recursive_order: ["platform_shell", "room_workspace", "tool_frame", "content_rendering"],
        }};
        return counts;
      }}

      function applyModelBinding() {{
        if (typeof model === "undefined" || !model?.views) return false;
        const prepView = model.views.find((view) => view && view.id === "prepNotebook");
        if (!prepView) return false;
        const current = packageData.current_object || {{}};
        const split = splitLessonTitle(current.title);
        const existingLesson = prepView.current_lesson || {{}};
        const links = packageData.derivative_linkage?.process_derivative_links || [];
        prepView.prep_start_surface = false;
        prepView.active_big_unit_id = "";
        prepView.courseware_workspace_expanded = false;
        prepView.active_node = "nb-lesson-u2_l1";
        prepView.current_lesson = {{
          ...existingLesson,
          id: "g3_u2_l1_color_gradient",
          code: split.code,
          title: split.title,
          unit: current.unit || "第二单元 多彩的世界",
          status: "预览中",
          textbook_page: current.textbook_position || "教材第6-7页",
          flow: packageData.lesson?.flow || existingLesson.flow,
          badges: [
            "备课预览",
            `${{(packageData.task_state?.known_materials || []).length}}项已知材料`,
            `${{(packageData.task_state?.missing_materials || []).length}}项缺口`,
            "教师确认前不生效",
          ],
          sections: normalizeSections(packageData.lesson?.sections),
          process_steps: normalizeProcessSteps(packageData.lesson?.process_steps, links),
          status_cards: [
            ["已知材料", String((packageData.task_state?.known_materials || []).length), "green"],
            ["缺口", String((packageData.task_state?.missing_materials || []).length), "amber"],
            ["派生对象", "4", "blue"],
          ],
          right_panels: buildRightPanels(packageData),
          reasoning_trace: buildReasoningTrace(packageData),
          big_screen_short_text: packageData.lesson?.big_screen_short_text || existingLesson.big_screen_short_text,
        }};
        const mappedScreens = normalizeCoursewareScreens(packageData.courseware_screens);
        window.coursewareScreens1013JR1 = mappedScreens;
        window.coursewareScreens1013JR1F = mappedScreens;
        try {{
          if (typeof coursewareScreens1013JR1 !== "undefined") coursewareScreens1013JR1 = mappedScreens;
          if (typeof coursewareScreens1013JR1F !== "undefined") coursewareScreens1013JR1F = mappedScreens;
        }} catch (error) {{
          window.__PREP_ROOM_R21_COURSEWARE_ASSIGN_ERROR__ = String(error?.message || error);
        }}
        model.active_view = "prepNotebook";
        model.negotiation = model.negotiation || {{}};
        model.negotiation.prompt = "告诉小教你要推进哪一步";
        model.negotiation.understanding = [
          "当前空间：备课室",
          "当前对象：2-1《色彩的渐变》",
          "小教判断：正在备课，先预览后确认",
        ];
        model.negotiation.notes = model.negotiation.notes || {{}};
        model.negotiation.notes.prepNotebook = "本课材料已进入备课页，只作为预览等待老师确认。";
        model.safety = model.safety || {{}};
        model.safety.api_connected = true;
        if (typeof renderNegotiationPanel === "function") renderNegotiationPanel();
        if (typeof renderPrepRoomCanvas === "function") renderPrepRoomCanvas({{ animate: false }});
        return true;
      }}

      function decorateInternalDom() {{
        document.documentElement.setAttribute("data-1013r-r21-internal-bound", "true");
        document.documentElement.setAttribute("data-1013r-r21-stage", STAGE_ID);
        document.body?.setAttribute("data-r20-package-bound", "true");
        const chatInput = document.getElementById("chatInput");
        if (chatInput) chatInput.setAttribute("placeholder", "告诉小教你要推进哪一步");
        const statusMain = document.getElementById("statusMain");
        if (statusMain) statusMain.textContent = "本课材料已进入备课页 · 确认前不写入";
        const stateMain = document.querySelector(".nb-state-bar .nb-state-main");
        if (stateMain && !stateMain.querySelector("[data-r21-inline-state]")) {{
          stateMain.insertAdjacentHTML("beforeend", '<span class="r21-inline-chip is-quiet" data-r21-inline-state="true">协议已接入</span><span class="r21-inline-chip warn">确认前不生效</span>');
        }}
        const firstDocHead = document.querySelector(".nb-doc-section-head");
        if (firstDocHead && !firstDocHead.querySelector("[data-r21-field-anchor='lesson_body']")) {{
          firstDocHead.insertAdjacentHTML("beforeend", '<span class="r21-inline-chip is-quiet" data-r21-field-anchor="lesson_body">lesson_body</span>');
        }}
        const drawer = document.querySelector(".nb-drawer, .nb-right-rail");
        if (drawer && !drawer.querySelector("[data-r21-field-anchor='action_gate']")) {{
          drawer.insertAdjacentHTML("beforeend", '<div class="r21-inline-note" data-r21-field-anchor="action_gate">确认门已进入右侧状态卡：保存、导出、评价写入仍为阻断或待确认。</div>');
        }}
        const flowSteps = Array.from(document.querySelectorAll(".nb-flow-step")).slice(0, 5);
        const links = packageData.derivative_linkage?.process_derivative_links || [];
        flowSteps.forEach((step, index) => {{
          if (step.querySelector("[data-r21-field-anchor='derivative_linkage']")) return;
          const link = links[index] || {{}};
          step.insertAdjacentHTML("beforeend", `<div class="r21-derived-mini" data-r21-field-anchor="derivative_linkage"><span>课件：${{esc(link.courseware_screen?.title || "预览")}}</span><span>大屏：${{esc(link.classroom_display?.student_visible_prompt || "预览")}}</span><span>评价：${{esc(link.assessment_rubric?.render_state || "待确认")}}</span></div>`);
        }});
        window.__PREP_ROOM_R21_INTERNAL_BOUND__ = true;
        window.__PREP_ROOM_R21_UNIFIED_PACKAGE__ = packageData;
        markFourLevelFrames();
      }}

      function restoreProcessStepDetails() {{
        const details = processDetailMap();
        Object.entries(details).forEach(([stepId, detail]) => {{
          const article = document.getElementById(`nb-step-${{stepId}}`);
          const list = article?.querySelector(".nb-step-detail-list");
          const rows = Array.isArray(detail.details) ? detail.details : [];
          if (!list || !rows.length) return;
          const expectedCount = String(rows.length);
          const currentCount = list.querySelectorAll(".nb-step-detail-item").length;
          if (list.getAttribute("data-r21-process-restored-count") === expectedCount && currentCount === rows.length) return;
          list.innerHTML = rows.map((row, index) => {{
            const title = Array.isArray(row) ? row[0] : `推进 ${{index + 1}}`;
            const text = Array.isArray(row) ? row[1] : String(row || "");
            const paragraphId = `p-${{stepId}}-${{index + 1}}`;
            const fullText = `${{title}}：${{text}}`;
            return `<li class="nb-anchor-paragraph nb-step-detail-item" data-edit-target="process:${{esc(stepId)}}:${{esc(paragraphId)}}" data-r21-full-text="${{esc(fullText)}}" data-hover-note="${{esc(detail.hover || "")}}"><span class="nb-micro-title">${{esc(title)}}</span><span class="nb-micro-text">${{esc(text)}}</span></li>`;
          }}).join("");
          list.setAttribute("data-r21-process-restored", "true");
          list.setAttribute("data-r21-process-restored-count", expectedCount);
        }});
        window.__PREP_ROOM_R21_PROCESS_DETAIL_RESTORED__ = true;
      }}

      function bindEditFullTextCapture() {{
        if (window.__PREP_ROOM_R21_EDIT_FULL_TEXT_CAPTURE_BOUND__) return;
        window.__PREP_ROOM_R21_EDIT_FULL_TEXT_CAPTURE_BOUND__ = true;
        document.addEventListener("click", (event) => {{
          const anchor = event.target?.closest?.("[data-edit-target], .nb-anchor-paragraph, .nb-step-detail-item");
          if (!anchor) return;
          const microTitle = cleanTeacherText(anchor.querySelector?.(".nb-micro-title")?.textContent || "");
          const microText = cleanTeacherText(anchor.querySelector?.(".nb-micro-text")?.textContent || "");
          const fullText = cleanTeacherText(anchor.getAttribute?.("data-r21-full-text") || (microTitle && microText ? `${{microTitle}}：${{microText}}` : anchor.textContent || ""));
          if (fullText) window.__PREP_ROOM_R21_LAST_EDIT_FULL_TEXT__ = fullText;
        }}, true);
      }}

      function rememberBigUnitRowIntent(row) {{
        if (!row) return null;
        const sectionId = row.getAttribute("data-r21-big-unit-section") || "";
        const item = bigUnitItemForSection(sectionId);
        const lineText = cleanTeacherText(row.getAttribute("data-r21-full-text") || row.textContent || "");
        if (lineText) window.__PREP_ROOM_R21_LAST_EDIT_FULL_TEXT__ = lineText;
        window.__PREP_ROOM_R21_BIG_UNIT_ACTIVE_ITEM__ = {{
          sectionId,
          item,
          lineText,
          at: Date.now(),
        }};
        return window.__PREP_ROOM_R21_BIG_UNIT_ACTIVE_ITEM__;
      }}

      function bindBigUnitRowIntentCapture() {{
        if (window.__PREP_ROOM_R21_BIG_UNIT_ROW_INTENT_BOUND__) return;
        window.__PREP_ROOM_R21_BIG_UNIT_ROW_INTENT_BOUND__ = true;
        ["pointerdown", "mousedown"].forEach((type) => {{
          document.addEventListener(type, (event) => {{
            const row = event.target?.closest?.("[data-r21-big-unit-row='true']");
            if (row) rememberBigUnitRowIntent(row);
          }}, true);
        }});
      }}

      function activeBigUnitItemForEdit() {{
        const active = window.__PREP_ROOM_R21_BIG_UNIT_ACTIVE_ITEM__;
        if (!active || !active.item) return null;
        if (Date.now() - Number(active.at || 0) > 8000) return null;
        return active;
      }}

      function cleanTechnicalBadges() {{
        document.querySelectorAll(".quiet-tag, .state-tag, .r6o-r1-status-pill").forEach((tag) => {{
          const text = (tag.textContent || "").trim();
          if (/^R20|^R21|统一协议|原型内绑定|原型绑定/.test(text)) tag.remove();
        }});
      }}

      function polishEditBubble() {{
        document.querySelectorAll(".r36-edit-bubble .nb-edit-panel:not([data-r21-edit-polished='true'])").forEach((panel) => {{
          panel.setAttribute("data-r21-edit-polished", "true");
          const activeBigUnit = activeBigUnitItemForEdit();
          const bigUnitItem = activeBigUnit?.item || null;
          const capturedBeforeText = cleanTeacherText(activeBigUnit?.lineText || window.__PREP_ROOM_R21_LAST_EDIT_FULL_TEXT__ || "");
          const title = panel.querySelector(".nb-edit-panel-title > div:first-child");
          if (title) {{
            const targetText = cleanTeacherText(title.textContent.replace(/^正在修改\\s*·\\s*/, ""));
            title.innerHTML = `<span class="r21-edit-title-target">${{esc(targetText)}}</span>`;
            title.setAttribute("title", targetText);
          }}
          const status = panel.querySelector(".nb-edit-panel-title > span");
          if (status) {{
            status.textContent = "待确认";
            status.classList.add("r21-edit-state-pill");
          }}
          const labels = Array.from(panel.querySelectorAll(".nb-edit-surface-block strong"));
          labels.forEach((label) => {{
            const text = label.textContent.trim();
            if (text === "小教建议" || text === "模型生成") label.textContent = "小教建议";
            if (text === "当前段落") {{
              label.textContent = "修改前";
              label.classList.add("r21-coffee-label");
              label.closest(".nb-edit-surface-block")?.setAttribute("data-r21-current-before", "true");
            }}
            if (text === "修改后") {{
              label.textContent = "修改后";
              label.classList.add("r21-coffee-label");
            }}
            if (text === "会影响什么") label.textContent = "影响范围";
          }});
          const beforeBlocks = Array.from(panel.querySelectorAll(".nb-edit-surface-block")).filter((block) => block.querySelector("strong")?.textContent.trim() === "修改前");
          const currentBefore = beforeBlocks.find((block) => block.getAttribute("data-r21-current-before") === "true") || beforeBlocks[0];
          if (currentBefore && capturedBeforeText) {{
            const currentText = cleanTeacherText((currentBefore.textContent || "").replace(/^修改前\\s*/, ""));
            if (capturedBeforeText.length > currentText.length) {{
              currentBefore.innerHTML = `<strong class="r21-coffee-label">修改前</strong>${{esc(capturedBeforeText)}}`;
            }}
          }}
          beforeBlocks.forEach((block) => {{
            if (block !== currentBefore) block.remove();
          }});
          const impactBlock = Array.from(panel.querySelectorAll(".nb-edit-surface-block")).find((block) => block.querySelector("strong")?.textContent.trim() === "影响范围");
          const impactText = bigUnitItem
            ? (Array.isArray(bigUnitItem.impact) ? bigUnitItem.impact : []).map((item) => cleanTeacherText(item)).filter(Boolean).join("；")
            : cleanTeacherText((impactBlock?.textContent || "").replace(/^影响范围\\s*/, "")) || "影响本章节阅读、教学过程承接和右侧大屏草稿对应关系。";
          if (impactBlock) impactBlock.remove();
          if (status && !status.parentElement?.querySelector(".r21-impact-help")) {{
            status.insertAdjacentHTML("beforebegin", `<span class="r21-impact-help" tabindex="0" aria-label="查看影响范围">?<span class="r21-impact-help-popover"><strong>影响范围</strong><br>${{esc(impactText)}}</span></span>`);
          }}
          const currentBlock = Array.from(panel.querySelectorAll(".nb-edit-surface-block")).find((block) => ["当前段落", "修改前"].includes(block.querySelector("strong")?.textContent.trim()));
          if (currentBlock) {{
            Array.from(currentBlock.childNodes).forEach((node) => {{
              if (node.nodeType === Node.TEXT_NODE) node.textContent = cleanTeacherText(node.textContent);
              if (node.nodeType === Node.ELEMENT_NODE && node.tagName !== "STRONG") node.textContent = cleanTeacherText(node.textContent);
            }});
          }}
          Array.from(panel.querySelectorAll(".nb-edit-surface-block strong")).forEach((label) => {{
            const labelText = label.textContent.trim();
            const block = label.closest(".nb-edit-surface-block");
            if (labelText === "修改前") {{
              block?.classList.add("r21-edit-before");
              label.classList.add("r21-coffee-label");
            }}
            if (labelText === "修改后") {{
              block?.classList.add("r21-edit-after");
              label.classList.add("r21-coffee-label");
              if (bigUnitItem?.after) block.innerHTML = `<strong class="r21-coffee-label">修改后</strong>${{esc(bigUnitItem.after)}}`;
            }}
          }});
          const surface = panel.querySelector(".nb-edit-surface");
          const adviceBlock = Array.from(panel.querySelectorAll(".nb-edit-surface-block")).find((block) => block.querySelector("strong")?.textContent.trim() === "小教建议");
          if (adviceBlock && bigUnitItem?.suggestion) {{
            adviceBlock.innerHTML = `<strong>小教建议</strong>${{esc(bigUnitItem.suggestion)}}`;
          }}
          if (surface && adviceBlock) surface.appendChild(adviceBlock);
          const primary = panel.querySelector(".nb-edit-tools .primary");
          if (primary) primary.textContent = "采纳";
          Array.from(panel.querySelectorAll(".nb-edit-tools .nb-soft-button")).forEach((button) => {{
            const text = button.textContent.trim();
            if (text === "继续精修") button.textContent = "重改";
            if (text === "暂不处理") button.textContent = "取消";
          }});
        }});
      }}

      function directChildBlocks(node) {{
        return Array.from(node?.children || []).filter((child) => child.classList?.contains("r6p-modal-block"));
      }}

      function firstStrongText(node) {{
        return cleanTeacherText(node?.querySelector?.("strong")?.textContent || "");
      }}

      function blockByLabel(blocks, pattern) {{
        return blocks.find((block) => pattern.test(firstStrongText(block)));
      }}

      function firstParagraphText(block, excludeClass) {{
        return cleanTeacherText(Array.from(block?.querySelectorAll?.("p") || [])
          .find((paragraph) => !excludeClass || !paragraph.classList.contains(excludeClass))?.textContent || "");
      }}

      function bigUnitEditData() {{
        if (window.__PREP_ROOM_R21_BIG_UNIT_EDIT_DATA__) return window.__PREP_ROOM_R21_BIG_UNIT_EDIT_DATA__;
        const node = document.getElementById("r6p-section-edit-data");
        try {{
          const data = JSON.parse(node?.textContent || "[]");
          window.__PREP_ROOM_R21_BIG_UNIT_EDIT_DATA__ = Array.isArray(data) ? data : [];
          return window.__PREP_ROOM_R21_BIG_UNIT_EDIT_DATA__;
        }} catch (error) {{
          window.__PREP_ROOM_R21_BIG_UNIT_EDIT_DATA_ERROR__ = String(error?.message || error);
          return [];
        }}
      }}

      function bigUnitSectionIdForChunk(chunkId, title) {{
        const map = {{
          render_chunk_curriculum_basis_1013K_R3: "curriculum_basis",
          render_chunk_core_literacy_goals_1013K_R3: "core_literacy",
          render_chunk_student_starting_point_1013K_R3: "student_start",
          render_chunk_unit_questions_1013K_R3: "unit_questions",
          render_chunk_knowledge_and_skills_1013K_R3: "knowledge_skills",
          render_chunk_performance_task_1013K_R3: "performance_task",
          render_chunk_learning_progression_1013K_R3: "learning_progression",
          render_chunk_lesson_task_chain_1013K_R3: "lesson_chain",
          render_chunk_assessment_evidence_1013K_R3: "assessment_evidence",
          render_chunk_materials_and_scaffolds_1013K_R3: "materials_scaffolds",
        }};
        if (map[chunkId]) return map[chunkId];
        const data = bigUnitEditData();
        const titleText = cleanTeacherText(title || "");
        return data.find((item) => titleText && titleText.includes(item.title))?.id || "";
      }}

      function splitBigUnitParagraphLines(text) {{
        const normalized = cleanTeacherText(String(text || "").replace(/\\s*\\n+\\s*/g, "。"));
        if (!normalized) return [];
        const sentenceParts = (normalized.match(/[^。；;！!？?]+[。；;！!？?]?/g) || [normalized])
          .map((item) => cleanTeacherText(item))
          .filter(Boolean);
        if (sentenceParts.length > 1) return sentenceParts.slice(0, 6);
        const commaParts = normalized.split(/(?<=，|、)/u).map((item) => cleanTeacherText(item)).filter(Boolean);
        if (commaParts.length > 1 && normalized.length > 42) {{
          const rows = [];
          let current = "";
          commaParts.forEach((part) => {{
            if ((current + part).length > 34 && current) {{
              rows.push(current);
              current = part;
            }} else {{
              current += part;
            }}
          }});
          if (current) rows.push(current);
          return rows.slice(0, 6);
        }}
        return [normalized];
      }}

      function bigUnitItemForSection(sectionId) {{
        const data = bigUnitEditData();
        return data.find((entry) => entry.id === sectionId) || data.find((entry) => entry.id !== "unit_info") || data[0] || null;
      }}

      function enhanceBigUnitParagraphRows() {{
        const scene = document.querySelector("[data-r6p-section-edit-surface]");
        const data = bigUnitEditData();
        if (!scene || !data.length) return;
        const sections = Array.from(scene.querySelectorAll(".nb-doc[data-r6o-field-render-doc='true'] .nb-doc-section, .nb-doc[data-1013l-r13-doc='true'] .nb-doc-section"));
        let rowCount = 0;
        sections.forEach((section) => {{
          const head = section.querySelector(".nb-doc-section-head");
          if (!head) return;
          const sectionTitle = head.querySelector(".nb-doc-title")?.textContent || section.textContent || "";
          const sectionId = section.getAttribute("data-r21-big-unit-editable-section") || bigUnitSectionIdForChunk(section.getAttribute("data-chunk-id") || "", sectionTitle);
          const item = bigUnitItemForSection(sectionId);
          if (!sectionId || !item) return;
          section.setAttribute("data-r21-big-unit-editable-section", sectionId);
          const existing = section.querySelector("[data-r21-big-unit-lines='true']");
          if (existing) {{
            rowCount += existing.querySelectorAll("[data-r21-big-unit-row='true']").length;
            return;
          }}
          const sourceParagraphs = Array.from(section.children).filter((child) => child.tagName === "P" && !child.querySelector(".quiet-tag"));
          const sourceText = sourceParagraphs.map((paragraph) => cleanTeacherText(paragraph.textContent || "")).filter(Boolean).join(" ");
          const lines = splitBigUnitParagraphLines(sourceText || item.current || item.before || item.after || "");
          if (!lines.length) return;
          sourceParagraphs.forEach((paragraph) => paragraph.remove());
          const list = document.createElement("ol");
          list.className = "r21-big-unit-lines";
          list.setAttribute("data-r21-big-unit-lines", "true");
          lines.forEach((line, index) => {{
            const row = document.createElement("li");
            const paragraphId = `${{sectionId}}-${{index + 1}}`;
            row.className = "nb-anchor-paragraph r21-big-unit-line";
            row.setAttribute("data-r21-big-unit-row", "true");
            row.setAttribute("data-r21-big-unit-section", sectionId);
            row.setAttribute("data-edit-target", `section:${{sectionId}}:${{paragraphId}}`);
            row.setAttribute("data-r21-full-text", line);
            row.setAttribute("data-hover-note", item.suggestion || item.view_note || "小教会围绕这一行给出候选修改，教师确认前不写入正式备课本。");
            row.textContent = line;
            list.appendChild(row);
            rowCount += 1;
          }});
          head.insertAdjacentElement("afterend", list);
        }});
        if (rowCount) document.documentElement.setAttribute("data-r21-big-unit-numbered-rows", String(rowCount));
      }}

      function openBigUnitSingleLessonBubble(sectionId) {{
        const row = document.querySelector(`[data-r21-big-unit-row='true'][data-r21-big-unit-section="${{CSS.escape(sectionId || "")}}"]`);
        if (!row) return false;
        rememberBigUnitRowIntent(row);
        row.dispatchEvent(new MouseEvent("click", {{ bubbles: true, cancelable: true, view: window }}));
        return true;
      }}

      function ensureBigUnitEditActions() {{
        const scene = document.querySelector("[data-r6p-section-edit-surface]");
        const data = bigUnitEditData();
        if (!scene || !data.length) return;
        const byId = new Map(data.map((item) => [item.id, item]));
        const sections = Array.from(scene.querySelectorAll(".nb-doc[data-r6o-field-render-doc='true'] .nb-doc-section, .nb-doc[data-1013l-r13-doc='true'] .nb-doc-section"));
        let count = 0;
        sections.forEach((section) => {{
          const head = section.querySelector(".nb-doc-section-head");
          if (!head || head.querySelector(".r21-big-unit-section-actions")) return;
          const sectionTitle = head.querySelector(".nb-doc-title")?.textContent || section.textContent || "";
          const sectionId = bigUnitSectionIdForChunk(section.getAttribute("data-chunk-id") || "", sectionTitle);
          if (!sectionId || !byId.has(sectionId)) return;
          section.setAttribute("data-r21-big-unit-editable-section", sectionId);
          const actions = document.createElement("span");
          actions.className = "r6p-section-actions r21-big-unit-section-actions";
          actions.innerHTML = `<button class="node-action secondary" type="button" data-r21-big-unit-view="${{esc(sectionId)}}">查看</button><button class="node-action secondary" type="button" data-r21-big-unit-edit="${{esc(sectionId)}}">编辑</button>`;
          const old = head.querySelector('button[data-pending]');
          if (old) old.remove();
          head.appendChild(actions);
          count += 1;
        }});
        if (count) document.documentElement.setAttribute("data-r21-big-unit-edit-actions", String(sections.length));
      }}

      function renderBigUnitEditModal(sectionId, mode) {{
        const data = bigUnitEditData();
        const item = data.find((entry) => entry.id === sectionId) || data.find((entry) => entry.id !== "unit_info") || data[0];
        const backdrop = document.querySelector(".r6p-modal-backdrop");
        const title = backdrop?.querySelector(".r6p-modal-title");
        const body = backdrop?.querySelector(".r6p-modal-body");
        if (!item || !backdrop || !title || !body) return;
        const impact = (Array.isArray(item.impact) ? item.impact : []).map((text) => `<li>${{esc(text)}}</li>`).join("");
        title.textContent = (mode === "view" ? "查看 · " : "正在修改 · ") + (item.title || "当前章节");
        if (mode === "view") {{
          body.innerHTML = `<div class="r6p-modal-block"><strong>章节说明</strong><p>${{esc(item.view_note || item.current || "")}}</p></div><div class="r6p-modal-block"><strong>可能影响</strong><ul>${{impact}}</ul></div><details class="r6p-modal-block"><summary>来源依据</summary><p>依据当前大单元阅读面和候选字段归档，只作为静态预览参考。</p></details>`;
        }} else {{
          body.innerHTML = `<div class="r6p-modal-block"><strong>当前内容</strong><p>${{esc(item.current || item.before || "")}}</p></div><div class="r6p-modal-block"><strong>小教建议</strong><p>${{esc(item.suggestion || "先围绕这一段形成候选改写，教师确认前不写入正式备课本。")}}</p><p class="r6s-teacher-intent">老师意图：${{esc(item.teacher_intent || "调整这一段")}}</p></div><div class="r6p-modal-block"><strong>修改前 / 修改后</strong><div class="r6p-modal-compare"><div class="r6p-modal-compare-box"><strong>修改前</strong><p>${{esc(item.before || item.current || "")}}</p></div><div class="r6p-modal-compare-box r6s-candidate-box"><strong>修改后 · 候选预览</strong><p>${{esc(item.after || "")}}</p></div></div></div><div class="r6p-modal-block"><strong>为什么这样改</strong><p>${{esc(item.why_this_change || "让这一段更适合教师阅读和后续单课继承。")}}</p></div><div class="r6p-modal-block"><strong>影响与操作</strong><ul>${{impact}}</ul><p class="r6s-risk-note">${{esc(item.risk_note || "仅进入本段预览，教师确认前不生效。")}}</p><div class="r6p-modal-actions"><button class="node-action primary" type="button" data-preview-only="true">采纳到本段预览</button><button class="node-action secondary" type="button" data-preview-only="true">继续精修</button><button class="node-action secondary" type="button" data-preview-only="true">暂不处理</button></div></div><details class="r6p-modal-block"><summary>来源依据</summary><p>候选来自 R6R 静态候选包，依据当前大单元阅读面、教师可见字段模型和后端候选映射归档，只作为静态预览参考。</p></details>`;
        }}
        backdrop.classList.add("is-open");
        backdrop.setAttribute("aria-hidden", "false");
        window.setTimeout(polishBigUnitEditModal, 0);
      }}

      function bindBigUnitEditActions() {{
        if (window.__PREP_ROOM_R21_BIG_UNIT_ACTIONS_BOUND__) return;
        window.__PREP_ROOM_R21_BIG_UNIT_ACTIONS_BOUND__ = true;
        document.addEventListener("click", (event) => {{
          const view = event.target?.closest?.("[data-r21-big-unit-view]");
          const edit = event.target?.closest?.("[data-r21-big-unit-edit]");
          if (view) {{
            event.preventDefault();
            event.stopImmediatePropagation();
            const sectionId = view.getAttribute("data-r21-big-unit-view");
            if (!openBigUnitSingleLessonBubble(sectionId)) renderBigUnitEditModal(sectionId, "view");
          }}
          if (edit) {{
            event.preventDefault();
            event.stopImmediatePropagation();
            const sectionId = edit.getAttribute("data-r21-big-unit-edit");
            if (!openBigUnitSingleLessonBubble(sectionId)) renderBigUnitEditModal(sectionId, "edit");
          }}
        }}, true);
      }}

      function polishBigUnitEditModal() {{
        document.querySelectorAll(".r6p-modal-backdrop.is-open .r6p-modal").forEach((modal) => {{
          const body = modal.querySelector(".r6p-modal-body");
          if (!body) return;
          const rawBodyText = cleanTeacherText(body.textContent || "");
          if (!/当前内容|修改前|修改后|小教建议/.test(rawBodyText)) return;
          const title = modal.querySelector(".r6p-modal-title");
          const titleText = cleanTeacherText((title?.textContent || "当前章节").replace(/^正在修改\\s*·\\s*/, "").replace(/^查看\\s*·\\s*/, ""));
          const polishKey = `${{titleText}}|${{rawBodyText.length}}|${{rawBodyText.slice(0, 80)}}`;
          if (body.getAttribute("data-r21-big-unit-polished-key") === polishKey) return;

          const blocks = directChildBlocks(body);
          const currentBlock = blockByLabel(blocks, /^当前内容$/);
          const suggestionBlock = blockByLabel(blocks, /^小教建议$/);
          const compareBlock = blockByLabel(blocks, /修改前\\s*\\/\\s*修改后|修改前/);
          const whyBlock = blockByLabel(blocks, /^为什么这样改$/);
          const impactBlock = blockByLabel(blocks, /^影响与操作$/);
          const boxes = Array.from(compareBlock?.querySelectorAll?.(".r6p-modal-compare-box") || []);

          const currentText = firstParagraphText(currentBlock);
          const beforeText = cleanTeacherText(boxes[0]?.querySelector("p")?.textContent || currentText);
          const afterText = cleanTeacherText(boxes[1]?.querySelector("p")?.textContent || "");
          const suggestionText = firstParagraphText(suggestionBlock, "r6s-teacher-intent") || "小教建议先作为章节候选预览，教师确认前不写入正式备课本。";
          const teacherIntent = cleanTeacherText(suggestionBlock?.querySelector(".r6s-teacher-intent")?.textContent || "").replace(/^老师意图[:：]?\\s*/, "");
          const whyText = firstParagraphText(whyBlock);
          const impactItems = Array.from(impactBlock?.querySelectorAll?.("li") || []).map((item) => cleanTeacherText(item.textContent)).filter(Boolean);
          const riskText = cleanTeacherText(impactBlock?.querySelector(".r6s-risk-note")?.textContent || "");
          const sourceText = cleanTeacherText(body.querySelector("details")?.textContent || "").replace(/^来源依据\\s*/, "");
          if (!beforeText || !afterText) return;

          if (title) {{
            title.textContent = titleText;
            title.setAttribute("title", titleText);
          }}
          const status = modal.querySelector(".r6p-modal-status");
          if (status) {{
            status.textContent = "待确认";
            if (!status.parentElement?.querySelector(".r6p-modal-impact-help")) {{
              const impactText = [...impactItems, riskText].filter(Boolean).join("<br>") || "影响本章节阅读、后续单课继承和评价证据关系。";
              status.insertAdjacentHTML("beforebegin", `<span class="r6p-modal-impact-help" tabindex="0" aria-label="查看影响范围">?<span class="r6p-modal-impact-popover"><strong>影响范围</strong><br>${{esc(impactText)}}</span></span>`);
            }}
          }}

          body.innerHTML = `
            <div class="r6p-modal-card r21-edit-before" data-r21-big-unit-before="true"><strong>修改前</strong>${{esc(beforeText)}}</div>
            <div class="r6p-modal-card r21-edit-after" data-r21-big-unit-after="true"><strong>修改后</strong>${{esc(afterText)}}</div>
            <div class="r6p-modal-card r21-xiaojiao-advice" data-r21-big-unit-advice="true">
              <strong>小教建议</strong>${{esc(suggestionText)}}
              ${{teacherIntent ? `<div class="r21-advice-muted">教师意图：${{esc(teacherIntent)}}</div>` : ""}}
              ${{whyText ? `<div class="r21-advice-muted">为什么这样改：${{esc(whyText)}}</div>` : ""}}
              ${{riskText ? `<div class="r21-advice-muted">提醒：${{esc(riskText)}}</div>` : ""}}
              ${{sourceText ? `<details><summary>来源依据</summary><p>${{esc(sourceText)}}</p></details>` : ""}}
            </div>
            <div class="r6p-modal-actions" data-r21-big-unit-actions="true">
              <button class="node-action primary" type="button" data-preview-only="true" data-r21-big-unit-action="accept">采纳</button>
              <button class="node-action secondary" type="button" data-preview-only="true" data-r21-big-unit-action="revise">重改</button>
              <button class="node-action secondary" type="button" data-preview-only="true" data-r21-big-unit-action="cancel">取消</button>
            </div>
          `;
          body.setAttribute("data-r21-big-unit-polished-key", polishKey);
          modal.setAttribute("data-r21-big-unit-modal-polished", "true");
          document.documentElement.setAttribute("data-r21-big-unit-edit-card-grammar", "true");
        }});
      }}

      function apply() {{
        applyModelBinding();
        decorateInternalDom();
        markFourLevelFrames();
        restoreProcessStepDetails();
        bindEditFullTextCapture();
        bindBigUnitEditActions();
        bindBigUnitRowIntentCapture();
        ensureBigUnitEditActions();
        enhanceBigUnitParagraphRows();
        cleanTechnicalBadges();
        polishEditBubble();
        polishBigUnitEditModal();
        window.setTimeout(decorateInternalDom, 80);
        window.setTimeout(markFourLevelFrames, 82);
        window.setTimeout(restoreProcessStepDetails, 85);
        window.setTimeout(ensureBigUnitEditActions, 88);
        window.setTimeout(enhanceBigUnitParagraphRows, 89);
        window.setTimeout(cleanTechnicalBadges, 90);
        window.setTimeout(polishEditBubble, 90);
        window.setTimeout(polishBigUnitEditModal, 95);
        window.setTimeout(decorateInternalDom, 260);
        window.setTimeout(markFourLevelFrames, 262);
        window.setTimeout(restoreProcessStepDetails, 265);
        window.setTimeout(ensureBigUnitEditActions, 268);
        window.setTimeout(enhanceBigUnitParagraphRows, 269);
        window.setTimeout(cleanTechnicalBadges, 270);
        window.setTimeout(polishEditBubble, 270);
        window.setTimeout(polishBigUnitEditModal, 275);
        document.addEventListener("click", () => {{
          window.setTimeout(ensureBigUnitEditActions, 0);
          window.setTimeout(enhanceBigUnitParagraphRows, 0);
          window.setTimeout(polishBigUnitEditModal, 0);
          window.setTimeout(ensureBigUnitEditActions, 80);
          window.setTimeout(enhanceBigUnitParagraphRows, 80);
          window.setTimeout(polishBigUnitEditModal, 80);
        }}, true);
        const observer = new MutationObserver(() => {{
          restoreProcessStepDetails();
          ensureBigUnitEditActions();
          enhanceBigUnitParagraphRows();
          cleanTechnicalBadges();
          polishEditBubble();
          polishBigUnitEditModal();
          markFourLevelFrames();
        }});
        observer.observe(document.body, {{ childList: true, subtree: true, attributes: true, attributeFilter: ["class"] }});
      }}

      if (document.readyState === "loading") {{
        document.addEventListener("DOMContentLoaded", apply);
      }} else {{
        apply();
      }}
    }})();
  </script>
"""


def build_page_copy_html(package: dict[str, Any] | None = None) -> str:
    if package is None:
        package = r20_package.build_unified_package()
    html = _read_prototype_base()
    injection = _internal_binding_style() + _internal_binding_script(package)
    if "script-1013R-R21-internal-prototype-binding" in html:
        return html
    if "</body>" not in html:
        raise ValueError("prototype_body_end_not_found")
    html = html.replace("<body ", '<body data-stage="1013R_R21" data-r20-package-bound="true" ', 1)
    return html.replace("</body>", injection + "\n</body>", 1)


def build_page_copy_binding() -> dict[str, Any]:
    package = r20_package.build_unified_package()
    html = build_page_copy_html(package)
    return {
        "ok": True,
        "stage": STAGE_ID,
        "binding_id": BINDING_ID,
        "generated_at": _now(),
        "consumes": {
            "r20_stage": package.get("stage"),
            "r20_package_id": package.get("package_id"),
            "source_prototype_stage": PROTOTYPE_BASE_STAGE,
            "source_prototype_path": str(PROTOTYPE_BASE_PATH),
            "current_object": deepcopy(package.get("current_object", {})),
        },
        "internal_binding_targets": [
            "model.views.prepNotebook.current_lesson",
            "model.views.prepNotebook.current_lesson.right_panels",
            "model.views.prepNotebook.current_lesson.reasoning_trace",
            "coursewareScreens1013JR1",
            "data-shiwei-four-level-frame",
            "data-shiwei-frame-level",
            "data-shiwei-frame-key",
            "chatInput.placeholder",
            "statusMain",
            ".nb-state-bar",
            ".nb-doc-section-head",
            ".nb-flow-step",
            ".nb-drawer",
        ],
        "visible_requirements": {
            "current_object_visible": True,
            "xiaojiao_task_state_visible": True,
            "known_and_missing_materials_visible": True,
            "teacher_action_gate_visible": True,
            "source_policy_visible": True,
            "render_blocks_mapped_to_existing_fields": True,
            "derivative_linkage_embedded_in_process_steps": True,
            "not_chatbox_centered": True,
            "prototype_base_preserved": True,
            "no_external_protocol_band": True,
        },
        "html": html,
        "next_stage_recommendation": {
            "stage": "1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE",
            "why": "页面原型副本已在内部字段读取 R20 包；下一步从教师可读性、派生对象可见联动和 2K 截图角度做 smoke。",
        },
        "boundary": boundary_flags(),
    }


def build_binding_sample_bundle() -> dict[str, Any]:
    binding = build_page_copy_binding()
    return {
        "stage": STAGE_ID,
        "page_copy_binding": {key: value for key, value in binding.items() if key != "html"},
        "html": binding["html"],
        "boundary": deepcopy(binding["boundary"]),
    }
