#File: sample.py
#Authors: Griffin Bishop, David Deisadze, Gianluca Tarquinio, Ian Vossoughi

import sys, random, math

total_samples = 0
numIterations = 0

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
day = {'dependent_on': [], 'weekend':0.2,'weekday':1}

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


graph = {'humidity': humidity, 'temperature': temperature, 'day': day,
         'snow': snow, 'icy': icy, 'cloudy': cloudy, 'exams': exams,
         'stress': stress}

# dictionary dictionary -> string
# node: the node we are assigning
# new_graph: the already assigned values for nodes we are depending on
# Look up the values that the node depends on in the given graph
#new_graph = {'humidity': 'low', 'temperature': 'cold', 'day': 'weekend', 'snow': 'true', 'exams': 'true'}
def assign_depending(node, new_graph, node_name):
    depending_on = node['dependent_on']
    # Accessors must be in the correct order in the depending on list
    accessors = [new_graph[key] for key in depending_on]

    probability = node
    prevProb = None
    for accessor in accessors:
        prevProb = probability
        
        probability = probability[accessor]

    # Now we should have a number in probability
    dice = random.random()
    if dice < probability:
        if node_name == 'stress':
            return 'high'
        return 'true' # this won't work for stress, add an if statement
    else:
        if node_name == 'stress':
            return 'low'
        return 'false'

# dictionary -> string
# Given a cumulative probability node, return
# an assignment.
def assign_nondependent(node):
    node = {k:v for k,v in node.items() if not k == 'dependent_on'}
    dice = random.random()
    for key in node.keys():
        probability = node[key]
        #print(dice, probability, key)
        if dice < probability:
            return key
    
# global dictionary -> dictionary of assigned values
# Requires that all nondependent values be placed at the front
# of the dictionary.
def assign_values():
    new_graph = {}
    for key in graph.keys():
        item = graph[key]
        if len(item['dependent_on']) == 0:
            new_graph[key] = assign_nondependent(item)
        else:
            new_graph[key] = assign_depending(item, new_graph, key)
            
    return new_graph

def perform_iteration(test_node, given_list):
    global total_samples, numIterations
    total_samples += 1
    world = assign_values()
    for key, value in given_list:
        if not world[key] == value:
            #print('world not work, moving on')
            
            #print(total_samples, numIterations)
            if total_samples >= numIterations:
                return -1 # failure
            return perform_iteration(test_node, given_list)
    return world[test_node[0]]

def perform_iteration2(test_node, given_list):
    world = assign_values()
    valid_sample = True
    for key, value in given_list:
        if not world[key] == value:
            valid_sample = False
    if valid_sample:
        return world[test_node[0]]
    else:
        return -1
                

def perform_iterations2(test_node, num_iterations, given_list):
    global total_samples
    total_samples = 0
    event_occurred = 0
    non_rejected = 0
    while total_samples < num_iterations:
        result = perform_iteration2(test_node, given_list)
        total_samples += 1
        if result == test_node[1]:
            event_occurred += 1
            non_rejected += 1
        elif result == -1:
            pass
        else:
            non_rejected += 1
    if non_rejected > 0:
        return (event_occurred / non_rejected, total_samples, non_rejected)
    else:
        return (0, total_samples, 0)
                
                

# test_node: of the form (stringA, stringB) where stringA is the
# name of the node we are concerned with, and stringB is the value
# num_iterations: how many successful trials do we want
# given_list: a list of tuples of the form above, where each tuple is a
# condition on the world for it to be counted as a successfull trial.
# Returns the number of trials in which the test_node condition was true
def perform_iterations(test_node, num_iterations, given_list):
    global total_samples
    total_samples = 0
    event_occurred = 0
    i = 0
    while i < num_iterations and total_samples < num_iterations:
    #for i in range(num_iterations):
        i += 1
        result = perform_iteration(test_node, given_list)
        if test_node[1] == result:
            event_occurred += 1
        elif result == -1:
            i += -1
    #while successful_iterations < num_iterations:
    #    result = perform_iteration(test_node, given_list)
    #    if result != None:
    #        successful_iterations += 1
    #        if result == test_node[1]:
    #            test_event_occured += 1
    return event_occurred / num_iterations
                









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
    print(die_rolled)

    # get all indices after the first
    for key in sorted(base_node, key=base_node.get):
        if key != 'dependent_on':
            val = base_node[key]

            if die_rolled - val < 0:
                return (key, base_node[key])


def main():
    global total_samples, numIterations
    arguments = sys.argv
    #print baseNodeGetProbability(humidity)
    #print baseNodeGetProbability(temperature)

    if len(arguments) < 3:
        print("Too few arguments. Try: ./sample.py [nodename]=[value] [numIterations] ...")
    nodeLower = arguments[1].lower()
    test_node = nodeLower.split('=')
    numIterations = int(arguments[2])
    #condition_list = [(k, v) for k, v in argument.split('=') for argument in arguments[2:]]
    #print(test_node, numIterations)
    condition_list = []
    for argument in arguments[3:]:
        argLower = str(argument.lower())
        print(argLower)
        k, v = argLower.split('=')
        condition_list += [(k,v)]
    #print(condition_list)

    result = perform_iterations2(test_node, numIterations, condition_list)
    p = result[0]
    total_samples = result[1]
    numIterations = result[2]
    sd = (p * (1-p))**(1/2) # Using formula given on canvas
    error = 2*sd/(total_samples**(1/2))
    print("Prob: {0:.05f}".format(p) + " | Samples: {}".format(total_samples) +
          " | Non-rejected: {}".format(numIterations))
    print("SD: {0:.05f}".format(sd)  + " | Range: {0:.05f}".format(2*error)
    + " | 95% interval: ({0:.05f},{1:.05f})".format(p-error,p+error))

    

if __name__ == '__main__':
    main()

