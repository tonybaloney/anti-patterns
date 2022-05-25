import re

def regex_with_anchors():
    SNAKE_CASE_RE = re.compile(r'^([a-z]+\d*_[a-z\d_]*|_+[a-z\d]+[a-z\d_]*)$')
    tests = ['data_type', 'data_type_', '_dataType', 'dataType', 'data type']
    for x in range(100_000):
        for test_str in tests:
            SNAKE_CASE_RE.match(test_str)

def regex_with_fullmatch():
    SNAKE_CASE_RE = re.compile(r'([a-z]+\d*_[a-z\d_]*|_+[a-z\d]+[a-z\d_]*)')
    tests = ['data_type', 'data_type_', '_dataType', 'dataType', 'data type']
    for x in range(100_000):
        for test_str in tests:
            SNAKE_CASE_RE.fullmatch(test_str)

def regex_with_ignorecase():
    SNAKE_CASE_RE = re.compile(r'([a-z]+\d*_[a-z\d_]*|_+[a-z\d]+[a-z\d_]*)', re.IGNORECASE)
    tests = ['data_type', 'data_type_URL', '_DataType', 'DataTypeURL', 'Data Type URL']
    for x in range(100_000):
        for test_str in tests:
            SNAKE_CASE_RE.fullmatch(test_str)

def regex_with_capitalrange():
    SNAKE_CASE_RE = re.compile(r'([a-zA-Z]+\d*_[a-zA-Z\d_]*|_+[a-zA-Z\d]+[a-zA-Z\d_]*)')
    tests = ['data_type', 'data_type_URL', '_DataType', 'DataTypeURL', 'Data Type URL']
    for x in range(100_000):
        for test_str in tests:
            SNAKE_CASE_RE.fullmatch(test_str)


__benchmarks__ = [
    (regex_with_anchors, regex_with_fullmatch, "Using fullmatch instead of anchors"),
    (regex_with_ignorecase, regex_with_capitalrange, "Using a-zA-Z instead of IGNORECASE"),
]
