# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).

Name student 1: Sergio Hidalgo Gamborino
Name student 2: Alexis Canales Molina
IA lab group and pair: 1331 - 11

"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(search_problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(search_problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    from util import Stack
    
    # stack of sucessors
    st : Stack = Stack()
    # list of path
    path_trace : list = list()
    # list of already visited
    allready_visited : list = list()
    # actual state (coordinates)
    actual_state = search_problem.getStartState()
    # temporal dictionary
    temp_dic = dict()
    temp_dic["path"]=list()
    temp_dic["cost"]=int()
    # cost of path
    cost = 0
    # list of posible responses
    responses = list()
    
    # sucessors -> coord[0], card[1], cost[2]
    allready_visited.append(actual_state)
    st.push(0)
    # while 1
    while 1:
        # the actual sucessors will be updated with the actual state
        actual_sucessors = search_problem.getSuccessors(actual_state)
        for i in actual_sucessors:
            if i[0] not in allready_visited:
                # if its not visited it will be pushed
                # with all the data of the path and its cost
                path_trace = temp_dic["path"].copy()   
                path_trace.append(i[1])
                cost = temp_dic["cost"]
                cost+=i[2]
                st.push({"node":i, "path":path_trace, "cost":cost})


        # the next state to check
        temp_dic = st.pop()
        # if it equals to 0 its the end of the stack
        if temp_dic == 0:
            break
        # append it to allready visited
        allready_visited.append(temp_dic["node"][0])
        # keep the actual state and the path
        actual_state = temp_dic["node"][0]
        path_trace = temp_dic["path"]

        # if its a goal state its appended to the responses
        if search_problem.isGoalState(actual_state):
            responses.append(temp_dic)

    # the cost will be equal to the first path cost
    cost = responses[0]['cost']
    for i in responses:
        # if the cost of the i response is minus or equal
        if i['cost'] <= cost:
            cost = i['cost']
            # it will become the new path
            path_trace = i['path']

    return path_trace


def breadthFirstSearch(search_problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(search_problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, search_problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(search_problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
