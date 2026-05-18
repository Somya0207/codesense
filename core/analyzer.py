# core/analyzer.py — reads a Python file and finds functions

import ast
from core.models import FunctionReport

class FileAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.reports = []

    def analyze(self, file_path: str) -> list:
        with open(file_path, "r") as f:
            source = f.read()
        tree = ast.parse(source)
        self.visit(tree)
        return self.reports

    def visit_FunctionDef(self, node):
        report = FunctionReport(
            name=node.name,
            line=node.lineno,
            complexity=1
        )
        self.reports.append(report)
        self.generic_visit(node)