# 067D OPENCLAW Import Allowlist

日期：2026-05-16

## 1. 本次没有做什么

- 未导入 OPENCLAW memory
- 未接入 OPENCLAW workspace runtime
- 未接小教 runtime
- 未接小评 runtime
- 未写飞书
- 未写数据库
- 未写知识库正式目录
- 未启用正式评分
- 未真实导出
- 未接入前端默认流程

067D 只建立只读、dry-run、可审计的候选导入闸门。

## 2. Allowlist

| 路径模式 | 允许动作 | 说明 |
| --- | --- | --- |
| `.openclaw/workspace-xiaobei/AGENTS*` | candidate scan only | 只允许扫描角色边界候选，不导入。 |
| `.openclaw/workspace-xiaobei/SOUL*` | candidate scan only | 只允许扫描小备 SOUL 方法候选，不导入。 |
| `.openclaw/workspace-xiaobei/MEMORY*` | candidate scan only | 只允许扫描记忆方法候选，不导入原始记忆。 |
| `.openclaw/workspace-xiaojiao/AGENTS*` | candidate scan only | 只允许扫描小教角色边界候选，不接 runtime。 |
| `.openclaw/workspace-xiaojiao/SOUL*` | candidate scan only | 只允许扫描小教 SOUL 方法候选。 |
| `.openclaw/workspace-xiaoping/AGENTS*` | candidate scan only | 只允许扫描小评角色边界候选，不接评分。 |
| `.openclaw/workspace-xiaoping/SOUL*` | candidate scan only | 只允许扫描小评 SOUL 方法候选。 |
| `.openclaw/plugins/**` | candidate scan only | 只参考技能组织方式，不复制执行器。 |
| `.openclaw/plugin-skills/**` | candidate scan only | 只参考技能组织方式，不接入默认流程。 |

allowlist 命中后仍必须做 secret scan。只有 `scan_result=clean` 的候选文件才允许进入红线内的摘要评审。

## 3. Denylist

| 路径模式 | 禁止原因 |
| --- | --- |
| `.openclaw/credentials/**` | 凭证区域，永远禁止迁移。 |
| `.openclaw/agents/*/auth-profiles.json` | 可能包含 provider profile 和 token，永远禁止迁移。 |
| `.openclaw/logs/**` | 可能包含运行记录和敏感上下文。 |
| `.openclaw/media/**` | 可能包含学生作品、图片、音视频或个人文件。 |
| `.openclaw/tasks/**` | 可能包含原始任务轨迹。 |
| `.openclaw/sessions/**` | 可能包含原始对话和个人上下文。 |
| `.openclaw/cache/**` | 缓存不作为迁移源。 |
| `.openclaw/tmp/**` | 临时文件不作为迁移源。 |
| `.openclaw/runtime/**` | runtime 轨迹不作为迁移源。 |
| `.openclaw/history/**` | 历史记录可能含敏感上下文。 |
| `.openclaw/backups/**` | 备份可能包含未审查副本。 |
| `*.key` / `*.pem` / `*.p12` / `*.pfx` | 密钥文件。 |
| `*.env` / `*.sqlite` / `*.db` / `*.log` | 配置、数据库或日志。 |
| `*.zip` / `*.7z` / `*.rar` | 压缩包不可审计。 |
| 图片/音频/视频原始文件 | 可能包含学生作品或个人信息。 |
| `.env` / `.env.local` / `.env.production` / `.env.development` | 隐藏环境配置文件，任何候选目录下都禁止。 |
| `.npmrc` / `.pypirc` / `.netrc` | 可能含 registry、PyPI 或网络凭证。 |
| `id_rsa` / `id_dsa` / `id_ecdsa` / `id_ed25519` / `known_hosts` | SSH 密钥或主机信任文件。 |
| `auth-profiles.json` / `auth_profiles.json` | auth profile，任何候选目录下都禁止。 |
| `credentials.json` / `credential.json` | 凭证命名文件，任何候选目录下都禁止。 |
| `secrets.json` / `secret.json` | secret 命名文件，任何候选目录下都禁止。 |
| `tokens.json` / `token.json` | token 命名文件，任何候选目录下都禁止。 |
| `private_key` / `private_key.txt` | 私钥命名文件，任何候选目录下都禁止。 |
| 文件名包含 `credential` / `secret` / `token` / `password` / `api_key` / `private_key` / `auth-profile` | 路径层直接 deny，不依赖内容扫描兜底。 |

## 4. Root 校验

scanner 必须显式传入 root，且只接受以下两种形态：

| 输入 root | 行为 |
| --- | --- |
| root 本身名为 `.openclaw` | 扫描该 root。 |
| root 不叫 `.openclaw`，但存在 `root/.openclaw` 子目录 | 只扫描 `root/.openclaw` 子目录。 |
| root 不叫 `.openclaw`，且不存在 `root/.openclaw` 子目录 | 拒绝，返回 `explicit_root_is_not_openclaw`。 |

普通目录不能被伪装成 OPENCLAW root。

## 5. Dry-run 结果

| 文件 | policy_result | scan_result | action |
| --- | --- | --- | --- |
| fake `.openclaw/workspace-xiaobei/SOUL.md` | allow_candidate | clean | allow_candidate_summary |
| fake `.openclaw/workspace-xiaobei/MEMORY.md` with fake token | allow_candidate | deny | deny |
| fake `.openclaw/agents/xiaobei/auth-profiles.json` | deny | not_scanned | deny |
| fake `.openclaw/plugins/.env` | deny | not_scanned | deny |
| fake plain root without `.openclaw` | rejected | not_scanned | deny |

以上结果来自临时 fake fixture，不读取真实外部 OPENCLAW 目录。

## 6. 下一步建议

067D 通过后进入 067E：capability registry -> executor coverage matrix。

在进入 068A 前，所有 OPENCLAW-derived 内容必须继续满足：

```text
preview-only
candidate
pending_review
teacher review only
```
