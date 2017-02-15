#File: sample.py
#Authors: Griffin Bishop, David Deisde, Gianluca Tarquinio, Godot

class Node(object):
    """
    Node object, has reference to its parent
    """
    def __init__(self, parent=None):
        self.parent = None
