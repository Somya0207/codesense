# core/complexity.py — scores how complex each function is

import ast
from core.models import Issue, FunctionReport

BRANCH_NODES = (ast.If, ast.For, ast.While, ast.ExceptHandler)

def score_function(node) -> FunctionReport:
    complexity = 1
    for child in ast.walk(node):
        if isinstance(child, BRANCH_NODES):
            complexity += 1

    issues = []
    if complexity > 10:
        issues.append(Issue(
            kind="complexity",
            message=f"Too complex (score {complexity}) — split this function",
            line=node.lineno
        ))
    elif complexity > 7:
        issues.append(Issue(
            kind="complexity",
            message=f"Getting complex (score {complexity}) — consider refactoring",
            line=node.lineno
        ))

    return FunctionReport(
        name=node.name,
        line=node.lineno,
        complexity=complexity,
        issues=issues
    )