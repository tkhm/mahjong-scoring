# mahjong-scoring
Calculate the score using points and hands.

This is intended to use on OpenWhisk or similar FaaS.

You can invoke the function with these parameter.

```json
{
    "hands": 2,
    "points": 30
}
```

And you can get the score like the following:

```json
{
    "hands": 2,
    "points": 30,
    "child": {
        "direct": 2000,
        "drawn": 500,
        "drawn_for_parent": 1000
    },
    "parent": {
        "direct": 2900,
        "drawn": 1000
    }
}
```

Currently, OpenWhisk is not supported by Delivery Pipeline auto deploy. Alternatively, you can push your code with the following code after setup OpenWhisk CLI:

`bash tools/deploy.sh scoring.py`
