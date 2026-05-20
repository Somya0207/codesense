# tests/test_scanner.py — tests for the full file scanner

from cli.scanner import scan_file

def test_scan_finds_functions():
    reports = scan_file("test_sample.py")
    assert len(reports) == 3

def test_scan_function_names():
    reports = scan_file("test_sample.py")
    names = [r.name for r in reports]
    assert "simple" in names
    assert "medium" in names
    assert "complex_func" in names

def test_simple_is_good():
    reports = scan_file("test_sample.py")
    simple = next(r for r in reports if r.name == "simple")
    assert simple.health_label() == "good"

def test_empty_file_returns_empty_list():
    reports = scan_file("config.py")
    assert reports == []