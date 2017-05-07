#coding: UTF-8

"""
main() will be invoked when you run this action.
"""

import math

def main(score_base):
    """Calculate and return score.
    @param OpenWhisk actions accept a single parameter, which must be a JSON object.
    @return The output of this action, which must be a JSON object.
    """
    points = score_base.get("points")
    hands = score_base.get("hands")

    return calc_score(points, hands)

def calc_score(points, hands):
    """Calculate the oritinal score using points and hands.
    Returned values are score containing dict object.
    """
    parent_base = 6
    child_base = 4

    original_parent_score = points * parent_base * pow(2, hands + 2)
    original_child_score = points * child_base * pow(2, hands + 2)

    parent_direct_score = ceil_score(original_parent_score)
    child_direct_score = ceil_score(original_child_score)

    parent_drown_score = ceil_score(original_parent_score / 3) # split by 3 ppl
    child_drown_score = ceil_score(original_parent_score / 4)
    child_drown_score_for_parent = ceil_score(original_parent_score / 2)

    parent_score = {
        "drawn": parent_drown_score,
        "direct": parent_direct_score
    }
    child_score = {
        "drawn": child_drown_score,
        "drawn_for_parent": child_drown_score_for_parent,
        "direct": child_direct_score
    }

    score = {
        "parent": parent_score,
        "child": child_score,
        "points": points,
        "hands": hands
    }

    return score

def ceil_score(original_score):
    """Return round up value. Returned value type is int."""
    return int(math.ceil(original_score / 100.0) * 100)

if __name__ == '__main__':
    DUMMY_VALUE = {"points": 30, "hands": 4}
    print(main(DUMMY_VALUE))
