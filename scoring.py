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
    """Calculate the original score using points and hands.
    Returned values are score containing dict object.
    """
    border_point = 2000

    original_score_base = points * pow(2, hands + 2)

    # bigger than border_point is strong winning hands
    if original_score_base > border_point:
        original_child_score = calc_strong_score(hands)
        original_parent_score = original_child_score * 1.5
    else:
        child_base = 4
        parent_base = child_base * 1.5

        original_child_score = original_score_base * child_base
        original_parent_score = original_score_base * parent_base

    child_score = {
        "drawn": ceil_score(original_child_score / 4), # for child
        "drawn_for_parent": ceil_score(original_child_score / 2), # for parent
        "direct": ceil_score(original_child_score)
    }
    parent_score = {
        "drawn": ceil_score(original_parent_score / 3), # split by 3 children
        "direct": ceil_score(original_parent_score)
    }

    score = {
        "child": child_score,
        "parent": parent_score,
        "points": points,
        "hands": hands
    }

    return score

def calc_strong_score(hands):
    """Calculate strong winning hands score.
    This function return child score, so if you need parent score,
    the score should be 1.5 times.
    """

    # basic point has been calcurated already, so under 5 hands are the same score
    if hands <= 5:
        score = 8000
    elif hands <= 7:
        score = 12000
    elif hands <= 10:
        score = 16000
    elif hands <= 12:
        score = 24000
    elif hands > 12:
        score = 32000

    return score

def ceil_score(original_score):
    """Return round up value. Returned value type is int."""
    return int(math.ceil(original_score / 100.0) * 100)

if __name__ == '__main__':
    WEEK_HANDS = {"points": 40, "hands": 2}
    print(main(WEEK_HANDS))

    STRONG_HANDS = {"points": 30, "hands": 6}
    print(main(STRONG_HANDS))
