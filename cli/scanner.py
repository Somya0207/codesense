import ast
from core.complexity import score_function

def scan_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        source = f.read()
    tree = ast.parse(source)
    reports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            report = score_function(node)
            reports.append(report)
    return reports