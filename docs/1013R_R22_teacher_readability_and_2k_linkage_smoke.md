# R22：教师可读性与派生对象可见联动验证

```text
stage_id=1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE
smoke_id=SHIWEI_PREP_ROOM_TEACHER_READABILITY_2K_SMOKE_R0
```

R22 不新增业务功能，只验证 R21 页面副本是否真的像教师工作推进系统，而不是普通聊天框。
R22 必须验证 R21 仍以 R11 原型页为基底，不允许另起脱离原型的新静态页，也不允许在原型外部贴协议工作带。

## 检查点

```text
1. 第一眼知道当前空间是备课室
2. 第一眼知道当前对象是三年级第二单元第1课《色彩的渐变》
3. 第一眼知道小教判断当前在备课
4. 已知材料 / 缺口 / 教师确认动作清楚
5. render_blocks 页面可见
6. 课件 / 大屏 / 学习单 / 评价表都有入口
7. 教学过程与派生对象联动可见
8. 来源提示可见但不压过主任务
9. 输入框不是“请输入你的问题”
10. 2K 截图尺寸为 2560x1440
11. 页面包含 R11 原型基底标记和 R21 内部绑定脚本
12. 页面不包含外置协议工作带
```

## 边界

```text
R36_modified=false
main_shell_modified=false
existing_page_modified=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
```

## 下一步

```text
R23：备课室教师走查脚本
```
