# conftest.py — tells pytest where to find project modules
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))