# Standup Randomizer

Python script that can generate a randomized list order, with groupings. Quickly
mix up your standup meetings with some randomization.

Usage:
```
standup.py [--popcorn] [GroupA:]MemberA,MemberB,MemberC [[GroupB:]Member1,Member2,Member3]
```

Usage Notes:
* Groupings are space-delimited. At least one must be provided.
* Groupings contain members which are comma-delimited.
* Groupings can be titled by providing a colon-separated name before member list.
* `--popcorn` reveals one name at a time, showing progress (e.g., `(1/6)`), and
  waits for Enter before showing the next.

Examples:
```
> ./standup.py Colin,JT,Michael,Tim
* Tim
* JT
* Michael
* Colin

> ./standup.py Blue:Colin,JT,Michael,Tim Green:Arthur,Leslie,Max
Blue
----
* JT
* Tim
* Colin
* Michael

Green
-----
* Leslie
* Arthur
* Max
```
