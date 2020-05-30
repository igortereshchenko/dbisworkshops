from datetime import datetime
import re


def book_check(b_id, a_name, a_lname):
    if not isinstance(b_id, int):
        return False
    elif not a_name.isalpha():
        return False
    elif not a_lname.isalpha():
        return False
    else:
        return True


def user_check(name, last_name, email, registration, amount):
    date_check = date_format_check(registration)
    if not name.isalpha() or not last_name.isalpha():
        return False
    elif not date_check:
        return False
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    elif not isinstance(amount, int):
        return False
    else:
        return True


def date_format_check(registration):
    try:
        tmp = datetime.strptime(registration, '%Y-%m-%d')
        return True
    except ValueError:
        return False


