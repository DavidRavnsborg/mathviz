import re
import logging
from sympy import sympify, SympifyError


def validate_and_parse(input_expr):
    """Validates that input strings are valid mathematical expressions.

    NOTE: This is sufficient for personal use, but is only a starting point for hosted applications
    that accept 3rd-party input. Any such application requires additional string sanitization to
    mitigate the potential for injection attacks.
    NOTE 2: sympify uses "eval" which can potentially be especially dangerous if accepting 3rd party
    input, see: https://github.com/sympy/sympy/issues/10805
    """

    # Allow only numbers, basic operators, and alphabetic characters for variables
    # if not re.match(r"^[\d+\-*/^()aAbBcCdDqQrRsStTuUvVwWxXyYzZ. ]+$", input_expr):
    if not re.match(r"^[\d+\-*/^()a-zA-Z. ]+$", input_expr):
        raise ValueError("Invalid characters in input.")

    try:
        # Try to parse the expression using sympy which can handle symbolic mathematics safely
        expr = sympify(input_expr)  # , strict=True)
    except SympifyError as e:
        logging.error(e)
        raise ValueError("Invalid mathematical expression.")

    return expr
