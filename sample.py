#File: sample.py
#Authors: Griffin Bishop, David Deisadze, Gianluca Tarquinio, Godot

import sys, random, math

# CPTs -- For nodes which don't depend on others,
# the values have been shifted(made cumulative) so we can just check if
# the generated random is lower than the value in the table.
humidity = {'dependent_on': [],
            'low':0.2, 'medium':0.7, 'high':1}
temperature = {'dependent_on': [],
               'warm':0.1, 'mild':0.5, 'cold':1}

#not cumulative
icy = {'dependent_on': ['humidity','temperature'],
       'low':
           {'warm': 0.001, 'mild': 0.01, 'cold': 0.05},
       'medium':
           {'warm': 0.001, 'mild': 0.03, 'cold': 0.02},
       'high':
           {'warm': 0.005, 'mild': 0.01, 'cold': 0.35}}

snow = {'dependent_on': ['humidity','temperature'],
        'low':
           {'warm': 0.0001, 'mild': 0.001, 'cold': 0.1},
       'medium':
           {'warm': 0.0001, 'mild': 0.0001, 'cold': 0.25},
       'high':
           {'warm': 0.0001, 'mild': 0.001, 'cold': 0.4}}

#cumulative
day = {'weekend':0.2,'weekday':1}

#not cumulative:
cloudy = {'dependent_on': ['snow'],
          'false':0.3, 'true':0.9}

exams = {'dependent_on': ['snow','day'],
        'false':
             {'weekend': 0.001, 'weekday':0.1},
         'true':
             {'weekend': 0.0001, 'weekday': 0.3}}

stress = {'dependent_on': ['snow','exams'],
          'false':
              {'false': 0.01, 'true': 0.2},
          'true':
              {'false': 0.1, 'true': 0.5}}

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


def main():
    arguments = sys.argv
    print baseNodeGetProbability(humidity)
    print baseNodeGetProbability(temperature)


if __name__ == '__main__':
    main()

