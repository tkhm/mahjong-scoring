#coding: UTF-8

"""
main() will be invoked when you Run This Action
"""

import math

def main(score_base):
    """
    @param OpenWhisk actions accept a single parameter, which must be a JSON object.
    @return The output of this action, which must be a JSON object.
    """
    # points, hands
    points = score_base.get("points")
    hands = score_base.get("hands")

    original_score = points * 4 * pow(2, hands + 2)
    direct_score = ceil_score(original_score)
    parent_score = ceil_score(original_score / 2)
    children_score = ceil_score(original_score / 4)

    return {"score": direct_score, "parent": parent_score, "children": children_score}

def ceil_score(original_score):
    """
    Return round up value
    """
    return math.ceil(original_score / 100.0) * 100

if __name__ == '__main__':
    dummy = {"points": 30, "hands": 4} # pylint: disable=invalid-name
    print(main(dummy))
