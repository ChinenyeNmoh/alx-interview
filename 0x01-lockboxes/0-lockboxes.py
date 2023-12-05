#!/usr/bin/python3
"""Lock boxes"""


def can_unlock_all(boxes):
    """Check if all of boxes can be opened"""
    boxesLength = len(boxes)
    keys = set()
    for index, box in enumerate(boxes, start=1):
        for num in box:
            if num < boxesLength:
                keys.add(num)
                keys.update(boxes[num])
            if len(keys) == boxesLength-1 or
            len(keys) == boxesLength:
                return True
        if index not in keys:
            return False


canUnlockAll = can_unlock_all
