#coding: UTF-8

"""
main() will be invoked when you Run This Action
"""

def main(score_base):
    """
    @param OpenWhisk actions accept a single parameter, which must be a JSON object.
    @return The output of this action, which must be a JSON object.
    """
    # points, hands
    return {"points": score_base.get("points"), "hands": score_base.get("hands")}

if __name__ == '__main__':
    dummy = {"points": 100, "hands": 10} # pylint: disable=invalid-name
    print(main(dummy))
