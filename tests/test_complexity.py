# tests/test_complexity.py — tests for the complexity scorer

import ast
from core.complexity import score_function

def get_node(code: str):
    tree = ast.parse(code)
    return next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef))

def test_simple_scores_one():
    code = "def greet(name): return name"
    report = score_function(get_node(code))
    assert report.complexity == 1

def test_one_if_scores_two():
    code = "def check(x):\n    if x > 0:\n        return x"
    report = score_function(get_node(code))
    assert report.complexity == 2

def test_high_complexity_creates_issue():
    code = """
def messy(x):
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
    if x: pass
"""
    report = score_function(get_node(code))
    assert report.complexity > 10
    assert len(report.issues) > 0