# 题库说明（data/questions.json）

每个正式知识点（157 个）配套 4 题，共 628 题，供诊断工具“每点最多 2 题”出题策略使用。题目由 AI 基于课本生成，**未经教师审核**，正确性主要靠机器核验。

## 1. 格式

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | `<topicId>_qN`，如 `cnm_052_q1`；`_q1` 题干与 `topics.json` 的 `diagnostic_question` 一致 |
| `topicId` | 是 | 知识点 id（正式点） |
| `difficulty` | 是 | `basic` 基础（课本例题水平一步计算）、`standard` 标准（2步）、`advanced` 提高（多步或易错） |
| `type` | 是 | `numeric` 数值题（答案可解析为数）、`choice` 选择题、`short` 短答（带单位/时间的非纯数字答案） |
| `prompt` | 是 | 中文题干，纯文字（几何条件用文字描述，不依赖配图） |
| `answer` | 是 | 字符串：numeric 为数字（整数/小数/分数）、choice 为选项字母、short 为短答案（如“10角”“9:05”） |
| `choices` | choice 必填 | 3-4 个选项 `[{key, text}]`，key 依次 A、B、C、D |
| `explanation` | 是 | 1-2 句中文解析 |
| `verify` | 否 | Python 表达式，用于机器核验（见下） |
| `accept` | 否 | 等价答案列表 |
| `unordered` | 否 | 多答案顺序无关时为 true（本版暂未使用） |

## 2. 统计

- 总数 **628 题**，覆盖 157 个正式点，每点 4 题。
- 按 type：numeric 425，choice 197，short 6；numeric+choice 占 99.0%（≥60% 达标）。
- 按 difficulty：basic 314，standard 157，advanced 157；每点含 basic 与 standard。
- choice 正确选项分布大致均匀（A/B/C/D 各 40-50 题）。

## 3. 核验方法

### 3.1 自动核验（`python3 scripts/verify_questions.py`）

numeric 与 choice 题可带 `verify` 表达式，脚本在受限环境（AST 白名单，仅允许四则、比较、少数函数如 `round`）中求值，再与 `answer` 比较：

- numeric：结果与 `answer` 按数值比较（分数精确，浮点容差 1e-9）。多答案支持 `unordered`。
- choice：结果与正确选项文字按数值或字符串比较，并检查无双解。

当前结果（`data/verification_report.json`）：

| 项 | 数量 |
|---|---|
| auto_verified | 425 |
| mismatch | 0 |
| unverifiable | 203（choice 197 + short 6） |

`mismatch 0` 表示有 `verify` 的题目均通过；`unverifiable` 为无 `verify` 的题目（主要为干扰项为文字的选择题与带单位/时间的 short 题），依赖人工审核或后续第二遍独立复核。

### 3.2 格式校验（`python3 scripts/validate.py`）

检查题 id 唯一、topicId 存在且非外部、`difficulty/type` 合法、choice 选项格式、`numeric` 答案可解析、每点 ≥3 题且含 basic+standard、`q1` 与诊断题一致等。

## 4. 局限

- **无教师审核**：干扰项、难度标注均为 AI 主观，未用学生数据校准。
- **题量小**：每点仅 4 题，重测会有重复；诊断每点最多 2 题，选择题有猜对概率。
- **无配图题**：几何题用文字描述数量关系，无作图与证明题。
- **verify 同源风险**：`verify` 与答案同为 AI 生成，若算法同错则无法暴露；已通过统计与多样化题型尽量降低。
- **short 题**：带单位（“10角”）、时间（“9:05”）、角度（“90°”）等答案为 short 类型，判题时需人工或诊断工具的文本规范化逻辑辅助，不在自动核验范围内。
