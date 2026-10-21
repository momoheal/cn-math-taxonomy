# -*- coding: utf-8 -*-
"""构建辅导卡与题目的轻量辅助函数。"""


def qn(diff, prompt, answer, explanation, verify=None):
    """数值题；answer 必须可被 validate 解析为数。"""
    d = {
        "difficulty": diff,
        "type": "numeric",
        "prompt": prompt,
        "answer": str(answer),
        "explanation": explanation,
    }
    if verify:
        d["verify"] = verify
    return d


def qc(diff, prompt, choices, answer, explanation):
    """选择题；choices 为 [(key, text), ...]，answer 为正确选项 key。"""
    return {
        "difficulty": diff,
        "type": "choice",
        "prompt": prompt,
        "choices": [(k, str(v)) for k, v in choices],
        "answer": answer,
        "explanation": explanation,
    }


def qs(diff, prompt, answer, explanation):
    """短答题；answer 可含单位、时间等非纯数字文本。"""
    return {
        "difficulty": diff,
        "type": "short",
        "prompt": prompt,
        "answer": str(answer),
        "explanation": explanation,
    }


def topic(kp, ex_problem, ex_steps, ex_answer, mistakes, tip, questions):
    """组装一条辅导内容。"""
    assert len(kp) == 3, kp
    assert len(mistakes) == 2, mistakes
    assert len(questions) == 4, questions
    return {
        "kp": kp,
        "ex": {
            "problem": ex_problem,
            "steps": ex_steps,
            "answer": str(ex_answer),
        },
        "mis": mistakes,
        "tip": tip,
        "q": questions,
    }
