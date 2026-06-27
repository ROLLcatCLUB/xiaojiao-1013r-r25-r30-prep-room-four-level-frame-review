from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package"
DOC_PATH = ROOT / "docs" / "1013R_R21_page_copy_binds_unified_package.md"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def fail(errors: list[str], code: str) -> None:
    errors.append(code)


def validate() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    from backend.xiaobei_ai import prep_room_page_copy_package_binding_1013R_R21 as module

    errors: list[str] = []
    bundle = module.build_binding_sample_bundle()
    binding = bundle.get("page_copy_binding", {})
    html = bundle.get("html", "")
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if binding.get("binding_id") != "SHIWEI_PREP_ROOM_PAGE_COPY_PACKAGE_BINDING_R0":
        fail(errors, "binding_id_mismatch")
    if binding.get("consumes", {}).get("r20_stage") != "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0":
        fail(errors, "r20_package_not_consumed")
    if binding.get("consumes", {}).get("source_prototype_stage") != "1013R_R11_prep_room_fetch_r10_viewmodel_static_binding":
        fail(errors, "r11_prototype_base_not_consumed")
    if binding.get("consumes", {}).get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")

    required_tokens = [
        "data-r20-package-bound=\"true\"",
        "data-1013j-prep-start=\"true\"",
        "topbar",
        "script-1013R-R21-internal-prototype-binding",
        "data-1013r-r21-internal-bound",
        "model.views.prepNotebook.current_lesson",
        "chatInput",
        "statusMain",
        "nb-state-bar",
        "nb-doc-section-head",
        "nb-flow-step",
        "nb-drawer",
        "2-1《色彩的渐变》",
        "小教任务状态",
        "已知材料",
        "还缺",
        "教师确认动作",
        "资料来源轻校验",
        "课件",
        "大屏",
        "学习单",
        "评价表",
        "readable_details",
        "restoreProcessStepDetails",
        "bindEditFullTextCapture",
        "data-r21-process-restored",
        "data-r21-full-text",
        "data-r21-current-before",
        "ensureBigUnitEditActions",
        "enhanceBigUnitParagraphRows",
        "openBigUnitSingleLessonBubble",
        "rememberBigUnitRowIntent",
        "bindBigUnitRowIntentCapture",
        "activeBigUnitItemForEdit",
        "renderBigUnitEditModal",
        "polishBigUnitEditModal",
        "data-r21-big-unit-lines",
        "data-r21-big-unit-row",
        "data-r21-big-unit-numbered-rows",
        "r21-big-unit-line",
        "data-r21-big-unit-editable-section",
        "data-r21-big-unit-edit-actions",
        "data-r21-big-unit-edit-card-grammar",
        "data-r21-big-unit-before",
        "data-r21-big-unit-after",
        "data-r21-big-unit-advice",
        "data-r21-big-unit-actions",
        "r6p-modal-impact-help",
        "--r21-bottom-composer-space: 146px",
        "--r21-binder-cover-inset: 14px",
        "--r21-binder-gutter-width: 24px",
        "--r21-prep-scene-height",
        "--r21-prep-column-height",
        "scrollbar-gutter: auto",
        "scrollbar-color: rgba(42, 88, 73, .58) transparent",
        "::-webkit-scrollbar-button",
        "*::-webkit-scrollbar-button:vertical:start:decrement",
        "*::-webkit-scrollbar-button:vertical:end:increment",
        "::-webkit-scrollbar-track-piece",
        "width: 6px !important",
        "height: 6px !important",
        "展现差异",
        "留下证据",
        "选证据",
        "告诉小教你要推进哪一步",
    ]
    for token in required_tokens:
        if token not in html:
            fail(errors, f"html_token_missing:{token}")
    if "穿穿编编" in html:
        fail(errors, "deprecated_chuanchuanbianbian_present")
    if "请输入你的问题" in html:
        fail(errors, "chatbox_placeholder_present")
    if "r21-prototype-protocol-band" in html:
        fail(errors, "external_protocol_band_present")
    if "R21 原型副本 / 读取 R20" in html:
        fail(errors, "external_protocol_band_copy_present")
    if html.count("data-r21-process-restored-count") < 1:
        fail(errors, "process_detail_restore_hook_missing")
    if not all(token in html for token in ["r21_intro", "r21_sense", "r21_explore", "r21_make", "r21_share"]):
        fail(errors, "process_step_ids_not_preserved")
    if not all(token in html for token in ["展现差异", "指认方向", "收住发现", "学生试色", "保留调整", "同伴反馈"]):
        fail(errors, "process_step_detail_copy_not_expanded")
    if not all(token in html for token in ["data-r21-full-text", "__PREP_ROOM_R21_LAST_EDIT_FULL_TEXT__", "capturedBeforeText"]):
        fail(errors, "edit_bubble_before_full_text_restore_missing")
    if not all(
        token in html
        for token in [
            "ensureBigUnitEditActions",
            "enhanceBigUnitParagraphRows",
            "openBigUnitSingleLessonBubble",
            "rememberBigUnitRowIntent",
            "bindBigUnitRowIntentCapture",
            "activeBigUnitItemForEdit",
            "renderBigUnitEditModal",
            "polishBigUnitEditModal",
            "data-r21-big-unit-lines",
            "data-r21-big-unit-row",
            "data-r21-big-unit-numbered-rows",
            "r21-big-unit-line",
            "data-r21-big-unit-before",
            "data-r21-big-unit-after",
            "data-r21-big-unit-advice",
            "data-r21-big-unit-actions",
            "r6p-modal-impact-help",
            "采纳",
            "重改",
            "取消",
        ]
    ):
        fail(errors, "big_unit_edit_card_grammar_missing")
    if not all(
        token in html
        for token in [
            "--r21-bottom-composer-space: 146px",
            "--r21-binder-cover-inset: 14px",
            "--r21-binder-gutter-width: 24px",
            "--r21-prep-scene-height",
            "--r21-prep-column-height",
            "var(--r21-binder-cover-inset) * 2",
            "var(--r21-binder-gutter-width)",
            "border-right: 0 !important",
            "border-left: 0 !important",
            "height: var(--r21-prep-column-height) !important",
            "scrollbar-gutter: auto",
            "scrollbar-color: rgba(42, 88, 73, .58) transparent",
            "::-webkit-scrollbar-button",
            "*::-webkit-scrollbar-button:vertical:start:decrement",
            "*::-webkit-scrollbar-button:vertical:end:increment",
            "::-webkit-scrollbar-track-piece",
            "width: 6px !important",
            "height: 6px !important",
            "min-height: 0 !important",
            "background: transparent !important",
        ]
    ):
        fail(errors, "prep_notebook_bottom_alignment_patch_missing")
    if len(html.encode("utf-8")) < 900000:
        fail(errors, "prototype_html_too_small_probably_new_static_page")
    internal_targets = set(binding.get("internal_binding_targets", []))
    for target in [
        "model.views.prepNotebook.current_lesson",
        "model.views.prepNotebook.current_lesson.right_panels",
        "model.views.prepNotebook.current_lesson.reasoning_trace",
        "chatInput.placeholder",
        "statusMain",
        ".nb-flow-step",
        ".nb-drawer",
    ]:
        if target not in internal_targets:
            fail(errors, f"internal_binding_target_missing:{target}")

    blocked_true_flags = [
        "route_registered",
        "endpoint_registered",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
        "existing_page_modified",
        "new_blank_static_page_created",
        "source_prototype_modified",
        "external_protocol_band_created",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("page_copy_created"):
        fail(errors, "page_copy_created_not_marked")
    if not boundary.get("page_binds_unified_package"):
        fail(errors, "page_binds_unified_package_not_marked")
    if not boundary.get("prototype_copy_created"):
        fail(errors, "prototype_copy_created_not_marked")
    if not boundary.get("internal_prototype_binding"):
        fail(errors, "internal_prototype_binding_not_marked")

    for token in [
        "R36_modified=false",
        "route_registered=false",
        "endpoint_registered=false",
        "formal_apply_performed=false",
        "new_blank_static_page_created=false",
        "source_prototype_modified=false",
        "external_protocol_band_created=false",
        "internal_prototype_binding=true",
    ]:
        if token not in doc:
            fail(errors, f"r21_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_page_copy_package_binding_1013R_R21",
        "binding_id": binding.get("binding_id"),
        "consumes": binding.get("consumes"),
        "html_length": len(html),
        "external_protocol_band_present": "r21-prototype-protocol-band" in html,
        "internal_binding_targets": binding.get("internal_binding_targets"),
        "prototype_base_stage": binding.get("consumes", {}).get("source_prototype_stage"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "r20_package_consumed": binding.get("consumes", {}).get("r20_stage")
            == "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0",
            "r11_prototype_base_consumed": binding.get("consumes", {}).get("source_prototype_stage")
            == "1013R_R11_prep_room_fetch_r10_viewmodel_static_binding",
            "not_new_blank_static_page": len(html.encode("utf-8")) >= 900000 and boundary.get("new_blank_static_page_created") is False,
            "no_external_protocol_band": "r21-prototype-protocol-band" not in html
            and boundary.get("external_protocol_band_created") is False,
            "internal_prototype_binding": boundary.get("internal_prototype_binding") is True,
            "teacher_visible_sections_present": not any(code.startswith("html_token_missing") for code in errors),
            "render_blocks_visible": "packageData.render_blocks" in html or '"render_blocks"' in html,
            "derivative_linkage_visible": "derivative_linkage" in html and ".nb-flow-step" in html,
            "process_steps_expanded": not any(code.startswith("process_") for code in errors),
            "big_unit_edit_card_grammar": "big_unit_edit_card_grammar_missing" not in errors,
            "prep_notebook_bottom_alignment": "prep_notebook_bottom_alignment_patch_missing" not in errors,
            "readonly_boundaries_intact": not any(code.startswith("readonly_boundary_broken") for code in errors),
            "R36_modified": False,
            "provider_called": False,
            "model_called": False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_page_copy_package_binding_1013R_R21 as module

    bundle = module.build_binding_sample_bundle()
    write_json(STAGE_DIR / "1013R_R21_result.json", result)
    write_json(STAGE_DIR / "page_copy_binding_1013R_R21.json", bundle["page_copy_binding"])
    write_json(STAGE_DIR / "page_copy_binding_evidence_1013R_R21.json", evidence)
    write_text(STAGE_DIR / "prep_room_page_copy_binds_unified_package_1013R_R21.html", bundle["html"])
    report = f"""# 1013R_R21 page copy binds unified package

```text
stage_id={STAGE_ID}
binding_id=SHIWEI_PREP_ROOM_PAGE_COPY_PACKAGE_BINDING_R0
current_object=三年级第二单元第1课《色彩的渐变》
R36_modified=false
main_shell_modified=false
existing_page_modified=false
new_blank_static_page_created=false
source_prototype_modified=false
external_protocol_band_created=false
internal_prototype_binding=true
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE
```
"""
    write_text(STAGE_DIR / "1013R_R21_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R21 page copy binds unified package")


if __name__ == "__main__":
    main()
