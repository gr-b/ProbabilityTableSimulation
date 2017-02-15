#File: sample.py
#Authors: Griffin Bishop, David Deisadze, Gianluca Tarquinio, Godot
import random


class Node(object):
    """
    Node object, has reference to its parent
    """
    def __init__(self, parent=None):
        self.parent = parent

# gets random number [0, 1]
def rollDice():
    return random.random()

# uses random probability to get the key for genrerated probability
# if not in range, returns None
# returns tuple (key, val)
def baseNodeGetProbability(base_node):
    die_rolled = rollDice()
    print die_rolled

    # get all indices after the first
    for key in sorted(base_node, key=base_node.get):
        if key != 'dependent_on':
            val = base_node[key]

            if die_rolled - val < 0:
                return (key, base_node[key])

# print baseNodeGetProbability(humidity)