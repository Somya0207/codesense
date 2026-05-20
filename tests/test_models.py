# tests/test_models.py — tests for Issue and FunctionReport

from core.models import Issue, FunctionReport

def test_issue_stores_data():
    i = Issue(kind="complexity", message="too complex", line=5)
    assert i.kind == "complexity"
    assert i.message == "too complex"
    assert i.line == 5

def test_health_label_good():
    r = FunctionReport(name="greet", line=1, complexity=3)
    assert r.health_label() == "good"

def test_health_label_warning():
    r = FunctionReport(name="greet", line=1, complexity=9)
    assert r.health_label() == "warning"

def test_health_label_critical():
    r = FunctionReport(name="greet", line=1, complexity=15)
    assert r.health_label() == "critical"

def test_function_report_empty_issues():
    r = FunctionReport(name="greet", line=1, complexity=1)
    assert r.issues == []