# -*- coding: utf-8 -*-
"""把 content/ 下的辅导内容合并进 topics.json 与 questions.json。

用法：python3 _builder/apply_content.py
"""
import importlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TOPICS = os.path.join(ROOT, "data", "topics.json")
QUESTIONS = os.path.join(ROOT, "data", "questions.json")

MODULES = [m for m in ("g1", "g2", "g3", "g4", "g5")
           if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", m + ".py"))]


def load():
    with open(TOPICS, encoding="utf-8") as f:
        topics = json.load(f)
    with open(QUESTIONS, encoding="utf-8") as f:
        questions = json.load(f)
    return topics, questions


def choice_text(q, key):
    for c in q.get("choices", []):
        if c["key"] == key:
            return c["text"]
    return key


def to_question(tid, idx, src):
    q = {
        "id": "%s_q%d" % (tid, idx),
        "topicId": tid,
        "difficulty": src["difficulty"],
        "type": src["type"],
        "prompt": src["prompt"],
        "answer": str(src["answer"]),
        "explanation": src["explanation"],
    }
    if src["type"] == "choice":
        q["choices"] = [{"key": k, "text": str(v)} for k, v in src["choices"]]
    if src.get("verify"):
        q["verify"] = src["verify"]
    if src.get("unordered"):
        q["unordered"] = True
    if src.get("accept"):
        q["accept"] = [str(x) for x in src["accept"]]
    return q


def main():
    topics, questions = load()
    by_id = {t["id"]: t for t in topics}
    pack = {}
    for name in MODULES:
        mod = importlib.import_module("content." + name)
        pack.update(mod.PACK)

    new_questions = []
    covered = 0
    for tid, lesson in pack.items():
        t = by_id.get(tid)
        if t is None or t.get("external"):
            print("跳过未知或外部知识点：", tid)
            continue
        covered += 1
        t["mastery_criteria"] = list(lesson["kp"])
        t["tutoring"] = {
            "key_points": list(lesson["kp"]),
            "worked_example": {
                "problem": lesson["ex"]["problem"],
                "steps": list(lesson["ex"]["steps"]),
                "answer": str(lesson["ex"]["answer"]),
            },
            "common_mistakes": list(lesson["mis"]),
            "coaching_tip": lesson["tip"],
        }
        qs = [to_question(tid, i + 1, q) for i, q in enumerate(lesson["q"])]
        q1 = qs[0]
        t["diagnostic_question"] = {
            "question": q1["prompt"],
            "answer": choice_text(q1, q1["answer"]) if q1["type"] == "choice" else q1["answer"],
        }
        new_questions.extend(qs)

    # 保留未被覆盖知识点的旧题（后续补齐后应为 0）
    covered_ids = {q["topicId"] for q in new_questions}
    kept = [q for q in questions if q["topicId"] not in covered_ids]
    merged = new_questions + kept
    merged.sort(key=lambda q: (q["topicId"], q["id"]))

    with open(TOPICS, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(QUESTIONS, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        f.write("\n")

    formal = [t for t in topics if not t.get("external")]
    print("模块：%s" % ", ".join(MODULES))
    print("覆盖正式知识点：%d / %d" % (covered, len(formal)))
    print("题库：新写 %d 题，保留旧题 %d 题，共 %d 题" % (len(new_questions), len(kept), len(merged)))
    missing = [t["id"] + " " + t["name"] for t in formal if t["id"] not in pack]
    if missing:
        print("未覆盖（仍为旧模板内容）：%d 个" % len(missing))
        for m in missing[:12]:
            print("  -", m)
        if len(missing) > 12:
            print("  ...")


if __name__ == "__main__":
    main()
