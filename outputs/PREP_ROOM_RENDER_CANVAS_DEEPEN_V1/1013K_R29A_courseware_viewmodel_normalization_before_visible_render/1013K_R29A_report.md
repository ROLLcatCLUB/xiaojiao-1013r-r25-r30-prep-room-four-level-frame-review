# 1013K_R29A Courseware ViewModel Normalization Before Visible Render

## Status

`PASS_1013K_R29A_COURSEWARE_VIEWMODEL_NORMALIZATION_BEFORE_VISIBLE_RENDER`

## Why This Stage Exists

R29 found that the hidden courseware viewmodel could be parsed and had 8 screens, but did not provide full render fields for every screen.

R29A fixes that by deriving a normalized render viewmodel from R25 screen seeds.

## What Was Added

R29A creates:

```text
normalized_courseware_render_viewmodel_1013K_R29A.json
```

and injects the same normalized data into the existing `1013J_R1M` courseware page as hidden JSON:

```text
<script id="1013k-courseware-normalized-render-viewmodel" type="application/json">
```

Every screen now has:

```text
title
teaching_intent
display_body
teacher_note
source_chunk_ref
```

## Boundary

This is still not visible rendering.

R29A does not change the teacher-visible UI, does not create a new page, does not connect runtime/provider/model/database/memory/Feishu/upload/search/whiteboard/PPT export, and does not perform formal apply.

## Next Stage

`1013K_R30_EXISTING_PAGE_VIEWMODEL_VISIBLE_RENDER_STATIC_APPLY`

R30 may render the normalized hidden viewmodel into the existing courseware page, with rollback backup and screenshot smoke.
