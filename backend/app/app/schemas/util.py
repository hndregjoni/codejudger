from app.core.config import settings

from typing import Set

def _validate_test_cases(cls, cases):
    if cases is None or  not (0 < len(cases) <= settings.MAX_CASES):
        raise ValueError("You must provide test cases")
    
    test_set: Set[str] = {}
    # Check for duplicates
    for case in cases:
        if case.a in test_set:
            raise ValueError(f"Test case duplicate: {case.a}")
    
    return cases