import json
import os
import random

FIRST_NAMES = os.path.join(os.path.dirname(__file__), "first_names.json")
LAST_NAMES = os.path.join(os.path.dirname(__file__), "last_names.json")


def pick_name(filepath, nationality):
    with open(filepath, "r", encoding="UTF-8") as f:
        names = json.load(f)
    return random.choice(names[nationality])


def first(nationality):
    return pick_name(FIRST_NAMES, nationality)


def last(nationality):
    return pick_name(LAST_NAMES, nationality)


def full(nationality):
    return f"{first(nationality)} {last(nationality)}"
