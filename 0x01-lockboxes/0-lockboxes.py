#!/usr/bin/python3
""" You have n number of locked boxes in front of you. Each box is numbered sequentially"""


def canUnlockAll(boxes):
    """ boxes, key
    """
    keys = {0}
    for box in range(0, len(boxes)):
        if box in keys:
            keys.update(boxes[box])
            for key in boxes[box]:
                if key < len(boxes):
                    keys.update(boxes[key])
        else:
            return False
    return True
