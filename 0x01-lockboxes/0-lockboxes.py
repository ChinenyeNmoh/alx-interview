#!/usr/bin/python3
"""Lock boxes"""


def can_unlock_all(boxes):
    """Check if all of boxes can be opened"""
    total_boxes = len(boxes)
    uniquekeys = set()
    for index, box in enumerate(boxes, start=1):
        for key in box:
            if key < total_boxes:
                uniquekeys.add(key)
                uniquekeys.update(boxes[key])
            if len(uniquekeys) in {total_boxes - 1, total_boxes}:
                return True
    if index not in uniquekeys:
        return False


canUnlockAll = can_unlock_all
