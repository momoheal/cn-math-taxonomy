# -*- coding: utf-8 -*-
"""Helper utilities for building Shanghai Elementary Math (沪教版五四学制 1-5年级) dataset."""


def ext_node(num, name, domain, description):
    return {
        "id": f"cnm_ext_{num:03d}",
        "name": name,
        "domain": domain,
        "grade": "学前",
        "description": description,
        "external": True,
        "standards": []
    }


def std_ref(sid, confidence="exact", note=None):
    d = {"id": sid, "confidence": confidence}
    if note:
        d["note"] = note
    return d


def make_topic(
    tid, name, domain, grade, semester, chapter, ttype,
    description, mastery_criteria, dq_q, dq_a,
    standards, key_points, example_prob, example_steps, example_ans,
    mistakes, coaching_tip, prereqs, questions
):
    """
    Returns (topic_dict, dep_list, question_list)
    prereqs: list of tuples (prereq_id, strength, reason)
    questions: list of 4 question dicts (q1, q2, q3, q4)
      q1 prompt must start with dq_q.
    """
    topic = {
        "id": tid,
        "name": name,
        "domain": domain,
        "grade": grade,
        "semester": semester,
        "chapter": chapter,
        "type": ttype,
        "description": description,
        "mastery_criteria": mastery_criteria,
        "diagnostic_question": {
            "question": dq_q,
            "answer": str(dq_a)
        },
        "external": False,
        "standards": standards,
        "tutoring": {
            "key_points": key_points,
            "worked_example": {
                "problem": example_prob,
                "steps": example_steps,
                "answer": str(example_ans)
            },
            "common_mistakes": mistakes,
            "coaching_tip": coaching_tip
        }
    }
    deps = []
    for pid, strength, reason in prereqs:
        deps.append({
            "topicId": tid,
            "prerequisiteId": pid,
            "strength": strength,
            "reason": reason
        })
    qs = []
    for idx, q in enumerate(questions, 1):
        qd = {
            "id": f"{tid}_q{idx}",
            "topicId": tid,
            "difficulty": q["difficulty"],
            "type": q["type"],
            "prompt": q["prompt"],
            "answer": str(q["answer"]),
            "explanation": q["explanation"]
        }
        if "choices" in q:
            qd["choices"] = [{"key": k, "text": str(v)} for k, v in q["choices"]]
        if "verify" in q and q["verify"]:
            qd["verify"] = q["verify"]
        if "unordered" in q and q["unordered"]:
            qd["unordered"] = True
        if "accept" in q and q["accept"]:
            qd["accept"] = [str(x) for x in q["accept"]]
        qs.append(qd)
    return topic, deps, qs


def q_num(diff, prompt, answer, explanation, verify=None, unordered=False, accept=None):
    d = {
        "difficulty": diff,
        "type": "numeric",
        "prompt": prompt,
        "answer": str(answer),
        "explanation": explanation,
    }
    if verify:
        d["verify"] = verify
    if unordered:
        d["unordered"] = True
    if accept:
        d["accept"] = accept
    return d


def q_choice(diff, prompt, choices, answer, explanation, verify=None):
    """choices: list of ('A', 'text'), ..."""
    d = {
        "difficulty": diff,
        "type": "choice",
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }
    if verify:
        d["verify"] = verify
    return d
