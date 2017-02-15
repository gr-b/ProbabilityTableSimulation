#File: sample.py
#Authors: Griffin Bishop, David Deisde, Gianluca Tarquinio, Godot

import sys, random, math


def main():
    arguments = sys.argv
    

if __name__ == '__main__':
    main()

    
class Node(object):
    """
    Node object, has reference to its parent
    """
    def __init__(self, parent=None):
        self.parent = parent
