# 沪教版小学数学（1-5年级·五四学制）知识图谱与同步辅导 · 辅导版

用「知识点节点 + 先修边」有向无环图（DAG）描述沪教版小学数学（一年级上至五年级下，共 10 册）的知识结构，严格对齐课本目录，并在每个知识点上附加**课本同步精讲四件套**与**配套题库**，配合自适应诊断工具实现“学—练—测—补”闭环。数据格式与设计思路参考 [Marble os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) 与本仓库原初中版 [momoheal/cn-math-taxonomy](https://github.com/momoheal/cn-math-taxonomy) 的 `topics + dependencies + standards + questions + diagnose` 体系。

> **状态声明：AI 生成的初稿，未经任何一线教师审核。** 知识点的拆分粒度、掌握标准、诊断题答案、辅导讲解，尤其是**先修关系（hard/soft 强度与是否存在）与辅导建议，都需要沪教版小学数学教师审核后才能用于教学。** 题库答案虽经机器核验，但非权威。

## 1. 数据来源与对齐依据

### 1.1 课本目录（严格遵守）

| 册次 | 课本版本 | 采用目录 | 章节结构 | 核实情况 |
|---|---|---|---|---|
| **一年级上** | **2024 审定版**（上海教育出版社，李大潜主编，教育部2024年8月教学用书目录） | 第一单元 我是小学生 … 第六单元 20以内加减法（一），第七单元 复习 | 7 单元（入学适应 / 认识图形 / 10以内数 / 10以内加减法 / 20以内数 / 20以内加减法一 / 复习） | 已核对多源公开目录（dzkbw.com、haoduoyun.cc、21cnjy.com）并与教育部用书目录交叉验证 |
| **一年级下** | **2024 审定版** | 第一单元 复习与提高 … 第六单元 整理与提高 | 6 单元（20以内复习 / 100以内数 / 时间一 / 100以内加减 / 几何小实践 / 整理） | 同上 |
| **二年级上** | 现行试用本（上海教育出版社 / 少年儿童出版社，九年义务教育课本） | 第一单元 复习与提高 … 第六单元 整理与提高 | 6 单元（含乘除一/二、统计、几何小实践） | 已核对dzkbw/haoduoyun公开目录，与“试用本”封面目录一致 |
| **二年级下** | 现行试用本 | 第一单元 复习与提高 … 第七单元 整理与提高 | 7 单元（千以内数 / 时间二 / 三位数加减 / 质量 / 几何 / 整理） | 同上 |
| **三年级上** | 现行试用本 | 第一单元 复习与提高 … 第六单元 整理与提高 | 6 单元（一位数乘/除、时间三、几何小实践等） | 同上 |
| **三年级下** | 现行试用本 | 第一单元 复习与提高 … 第七单元 整理与提高 | 7 单元（两位数乘除、统计、分数一、计算器、几何等） | 同上 |
| **四年级上** | 现行试用本 | 第一单元 复习与提高 … 第六单元 整理与提高 | 6 单元（数与量、分数二、整数四则运算、几何等） | 同上 |
| **四年级下** | 现行试用本 | 第一单元 复习与提高 … 第五单元 整理与提高 | 5 单元（小数加减、统计、垂直平行等） | 同上 |
| **五年级上** | 现行试用本 | 第一单元 复习与提高 … 第六单元 整理与提高 | 6 单元（小数乘除、统计、简易方程一、几何小实践等） | 同上 |
| **五年级下** | 现行试用本 | 第一单元 复习与提高 … 第五单元 可能性 | 6 单元（含正负数、简易方程二、长方体正方体体积表面积、可能性等） | 同上 |

**过渡说明（hybrid_2024）**：教育部 2024 年审定版小学数学（五四学制）目前仅公布至一年级上下册（2024 秋、2025 春启用），二至五年级 2024 版尚未出版。本项目按“一年级上/下用 2024 新版，其余册次沿用现行试用本并标注”的混合策略处理，与当前上海学校实际用书一致。待二至五年级新版发布后，将逐册更新并在 `CHANGELOG.md` 中记录。

所有知识点的 `chapter` 字段均按上述目录的“册 + 单元 + 小节”书写，例如 `一年级上 第三单元 10以内的数 3.1 1-5的认识`，确保可追溯到课本原文。

### 1.2 课程标准

- **依据**：教育部《义务教育数学课程标准（2022年版）》第一学段（1-2年级）、第二学段（3-4年级）、第三学段（5-6年级）【内容要求】。
- **条目**：`data/cn-curriculum-standards.json` 共 **64 条**（数与代数 29、图形与几何 20、统计与概率 7、综合与实践 8），id 形如 `cms-2022:1.NA.01`（学段.领域.序号），按课标原顺序连续编号。内容为课标原文归纳分条，已标注主题、子主题、条款号与印刷页码。
- **映射**：每个正式知识点通过 `standards` 字段挂接 1-3 条课标（共 181 条映射），`confidence` 均为 `exact`（本项目按课标分条已尽量精确，inferred 暂未使用）。学前外部节点的 `standards` 为空。
- **说明**：上海五四学制的五年级（相当于六三学制的六年级上学期部分内容）在课标中对应第三学段的部分要求，已纳入；初中第四学段未包含。

### 1.3 习题

- **课本习题**：诊断题与辅导例题的设计严格对齐课本例题与练习的题型与难度，习题文本自行命制，不直接复制课本原题（避免版权问题），但题型、知识点与解题思路与课本一致。
- **外部题库**：题库中数值计算、应用题、几何测量等题目可自行选取市面常见教辅题型改编，确保答案可机器核验。

## 2. 文件结构

```
data/topics.json              知识点节点（JSON 数组，含辅导四件套）
data/dependencies.json        先修边（JSON 数组）
data/cn-curriculum-standards.json  课标条目（64 条）
data/questions.json           题库：每个正式知识点 4 题（共 628 题）
data/verification_report.json 题库答案核验报告（机器核验）
docs/standards-mapping.md     课标对齐说明
docs/questions.md             题库说明与核验方法
diagnose/                     诊断小工具（纯静态）
  index.html  engine.js  app.js  style.css
index.html                    知识图谱浏览页（单文件，无外部依赖）
scripts/validate.py           校验脚本（仅标准库）
scripts/verify_questions.py   题库答案自动核验（受限表达式求值）
_builder/                     数据构建脚本（_builder/build.py + common.py）
tests/test_engine.js          诊断引擎测试（Node，无依赖）
screenshots/                  诊断小工具截图（旧版占位）
```

### topics.json 字段

正式知识点（`external: false`）：

| 字段 | 说明 |
|---|---|
| `id` | 稳定 id，`cnm_001` … `cnm_157` |
| `name` | 中文名称（与课本小节名一致或高度概括） |
| `domain` | 数与代数 / 图形与几何 / 统计与概率 / 综合与实践 |
| `grade` | 1 / 2 / 3 / 4 / 5（五四学制年级） |
| `semester` | "上" 或 "下" |
| `chapter` | 课本章节，如 `一年级上 第三单元 10以内的数 3.1 1-5的认识` |
| `type` | conceptual / procedural / reasoning / application / modeling |
| `description` | 通俗说明（1-2句） |
| `mastery_criteria` | 2-3 条掌握标准 |
| `diagnostic_question` | `{ "question": "...", "answer": "..." }` |
| `external` | `false` |
| `standards` | 课标映射数组 `[{ id, confidence, note? }]` |
| `tutoring` | **辅导四件套**：`{ key_points(3条), worked_example{problem, steps(2-3), answer}, common_mistakes(2条), coaching_tip(1条) }` |

学前外部节点（`external: true`）：`id: cnm_ext_001` … `cnm_ext_012`，`grade: "学前"`，仅有 `name/domain/description/external/standards`。

### dependencies.json 字段

```json
{"topicId": "A", "prerequisiteId": "B", "strength": "hard", "reason": "一句中文理由"}
```

含义：**A 依赖 B**（学 A 之前需要 B）。hard 会 B 基本无法学 A，soft 会 B 有帮助但非硬门槛。

### 题库（questions.json）

每个正式知识点 **4 题**（basic 2 题、standard 1 题、advanced 1 题，含 basic 与 standard）：

| 字段 | 说明 |
|---|---|
| `id` | `<topicId>_qN`，如 `cnm_050_q1` |
| `topicId` | 知识点 id |
| `difficulty` | basic / standard / advanced |
| `type` | numeric / choice / short（short 用于含单位、时间等非纯数字答案） |
| `prompt` | 中文题干（纯文字，不依赖图形） |
| `answer` | 字符串（numeric 为可解析数字，choice 为选项字母） |
| `choices` | choice 题的 3-4 个选项 `{key, text}` |
| `explanation` | 中文解析 |
| `verify` | 可选，Python 表达式用于机器核验 |
| `accept` | 可选，等价答案列表 |

`topics.json` 中原有的 `diagnostic_question` 保留为第 1 题的原型（`_q1` 题干以其开头）。

## 3. 当前统计（`python3 scripts/validate.py` 实际输出）

- 知识点总数 **169**：正式 **157**，学前外部 **12**
- 按领域（正式）：数与代数 103，图形与几何 33，综合与实践 15，统计与概率 6
- 按册次（正式）：一年级上 18，一年级下 16，二年级上 18，二年级下 18，三年级上 16，三年级下 16，四年级上 14，四年级下 10，五年级上 17，五年级下 14
- 按类型（正式）：procedural 72，conceptual 54，application 20，reasoning 10，modeling 1
- 先修边 **188** 条：hard 165，soft 23；正式知识点平均先修 1.20
- 课标对齐：64 条中 61 条被引用；正式知识点 100% 有映射（181 条映射，均为 exact）
- 题库：628 题（numeric 382，choice 185，short 61；basic 314，standard 157，advanced 157；每点 4 题）
- 机器核验：auto_verified 382，mismatch 0，unverifiable 246（choice+short 主要靠第二遍复核或人工审核）

## 4. 辅导设计（新增）

每个正式知识点在浏览页均可展开**同步辅导卡**：

1. **要点精讲（key_points 3条）**：用家长/学生易懂的语言提炼课本定义、操作步骤与联系生活的应用。
2. **例题精讲（worked_example）**：1 道与课本例题同类的小例题，含 2-3 步解法与答案，家长可照着讲。
3. **常见错误（common_mistakes 2条）**：列出该知识点学生易错点（如进位漏加、单位混淆）。
4. **辅导建议（coaching_tip 1条）**：给家长的具体话术或活动建议（如“先摆小棒再列式，多问一句怎么想的”）。

浏览页 `index.html` 中点击知识点即可查看；诊断工具结果页中每个薄弱根因也提供“查看辅导要点”跳转链接。所有辅导内容由 AI 基于课本生成，**需教师审核**，仅供家庭辅导参考。

## 5. 诊断小工具

`diagnose/` 为纯静态、可离线的诊断页面：选目标知识点或整章，按先修关系自适应出题（每点最多 2 题：第一题对→掌握并跳过祖先；错→第二题，同级或更易；第二题对→不稳不回溯，错→薄弱并回溯 hard 优先），给出根因、不稳点、拓扑学习路径、课标条目与路径图。

```bash
python3 -m http.server 8000
# 访问 http://localhost:8000/diagnose/  （演示：?target=cnm_050&demo=1）
node tests/test_engine.js
```

算法、判题、URL 参数见 [diagnose/README.md](diagnose/README.md)。

## 6. 运行校验

```bash
python3 scripts/validate.py
python3 scripts/verify_questions.py
```

`validate.py` 检查 JSON 合法、id 唯一、必填字段、取值合法、边存在且无环、非外部点有先修、题库格式与覆盖等；打印统计。`verify_questions.py` 对带 `verify` 的 numeric/choice 题做受限表达式求值核验，输出 `data/verification_report.json`。当前 `VALIDATION PASSED` 且 `VERIFICATION PASSED`（mismatch 0）。

## 7. 已知局限

- **审核缺位**：先修图、辅导四件套、题库答案均未经教师审核，不能直接用于教学决策。
- **目录过渡**：二至五年级为“试用本”目录，新版发布后需更新；一年级为2024新版已核对但仍建议以课本实物为准。
- **题库规模**：每点 4 题、诊断每点最多 2 题，选择题有猜对概率，结果仅为线索。
- **图形题**：题干纯文字，无配图；作图与证明题未覆盖。
- **辅导深度**：例题与建议为通用模板化生成，未针对上海教研细节（如“沪教版巧算策略”）逐条优化，需一线教师补充。

## 8. 许可证

本项目采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hans) 授权，详见 [LICENSE](LICENSE)。商用需联系作者。

---

*本项目为 fork 自初中版后的小学辅导版，保持相同的技术底座与校验体系，仅内容域替换为沪教版小学数学并新增辅导卡；适合作为家校共育的轻量辅导工具原型。*
