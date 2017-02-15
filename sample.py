#File: sample.py
#Authors: Griffin Bishop, David Deisde, Gianluca Tarquinio, Godot

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


def main():
    arguments = sys.argv
    

if __name__ == '__main__':
    main()

    
class Node(object):
    """
    Node object, has reference to its parent
    """
    def __init__(self, parent):
        self.parent = {}
