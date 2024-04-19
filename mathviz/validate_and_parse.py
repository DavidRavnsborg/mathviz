import re
import logging
from sympy import sympify, SympifyError


def validate_and_parse(input_expr):
    """Validates that input strings are valid mathematical expressions.

    NOTE: This is just a first step. Any hosted application accepting 3rd-party user input requires
    additional string sanitization to mitigate the potential for injection attacks. This is just a
    starting point.
    NOTE 2: sympify uses "eval" which can potentially be very dangerous, see:
    https://github.com/sympy/sympy/issues/10805
    """

    # Allow only numbers, basic operators, and alphabetic characters for variables
    if not re.match(r"^[\d+\-*/^()aAbBcCdDqQrRsStTuUvVwWxXyYzZ. ]+$", input_expr):
        raise ValueError("Invalid characters in input.")

    try:
        # Try to parse the expression using sympy which can handle symbolic mathematics safely
        expr = sympify(input_expr)  # , strict=True)
    except SympifyError as e:
        logging.error(e)
        raise ValueError("Invalid mathematical expression.")

    return expr
