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
    already_visited : list = list()
    # actual state (coordinates)
    actual_state = search_problem.getStartState()
    # temporal dictionary
    temp_dic = dict()
    temp_dic["path"]=list()

    # sucessors -> coord[0], card[1], cost[2]
    already_visited.append(actual_state)
    
    # while the actual state is not the goal state
    while not search_problem.isGoalState(actual_state):
        # the actual sucessors will be updated with the actual state
        actual_sucessors = search_problem.getSuccessors(actual_state)
        for i in actual_sucessors:
            if i[0] not in already_visited:
                # if its not visited it will be pushed
                # with all the data of the path
                path_trace = temp_dic["path"].copy()   
                path_trace.append(i[1])
                st.push({"node":i, "path":path_trace})
        # if its empty there is no solution
        if st.isEmpty():
            return None
        
        # do while
        while True and not st.isEmpty():
            # the next state to check
            temp_dic = st.pop()
            # keep the actual state and the path
            actual_state = temp_dic["node"][0]
            # if its in already visited continue
            if actual_state not in already_visited: 
                break
        # append to already visited
        already_visited.append(actual_state)
        path_trace = temp_dic["path"]


    return path_trace


def breadthFirstSearch(search_problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    from game import Directions
    
    # queue of sucessors
    q : Queue = Queue()
    # list of path
    path_trace : list = list()
    # list of already visited
    already_visited : list = list()
    # actual state (coordinates)
    actual_state = search_problem.getStartState()
    # temporal dictionary
    temp_dic = dict()
    temp_dic["path"] = list()
    
    # sucessors -> coord[0], card[1], cost[2]
    already_visited.append(actual_state)
    
    # while the actual state is not the goal state
    while not search_problem.isGoalState(actual_state):
        # the actual sucessors will be updated with the actual state
        actual_sucessors = search_problem.getSuccessors(actual_state)

        for i in actual_sucessors:
            if i[0] not in already_visited:
                # if its not visited it will be pushed
                # with all the data of the path
                path_trace = temp_dic["path"].copy()   
                path_trace.append(i[1])
                q.push({"node":i, "path":path_trace})

        # if its empty there is no solution
        if q.isEmpty():
            return None
        
        # do while
        while True and not q.isEmpty():
            # the next state to check
            temp_dic = q.pop()
            # keep the actual state and the path
            actual_state = temp_dic["node"][0]
            # if its in already visited continue
            if actual_state not in already_visited: 
                break

        # append to already visited
        already_visited.append(actual_state)
        path_trace = temp_dic["path"]

    return path_trace

def uniformCostSearch(search_problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    # queue of sucessors
    pq : PriorityQueue = PriorityQueue()
    # list of path
    path_trace : list = list()
    # list of already visited
    already_visited : list = list()
    # actual state (coordinates)
    actual_state = search_problem.getStartState()
    # temporal dictionary
    temp_dic = dict()
    temp_dic["path"] = list()
    # cost
    cost = 0 

    # sucessors -> coord[0], card[1], cost[2]
    already_visited.append(actual_state)

    # while the actual state is not the goal state
    # import pdb;pdb.set_trace()
    while not search_problem.isGoalState(actual_state):
        # the actual sucessors will be updated with the actual state
        # print ("current node:", actual_state)
        actual_sucessors = search_problem.getSuccessors(actual_state)
        for sucessor in actual_sucessors:
            # if its not visited it will be pushed
            if sucessor[0] not in already_visited:
                # with all the data of the path and cost
                path_trace = temp_dic["path"].copy()   
                path_trace.append(sucessor[1])
                # cost equals cost of actions
                cost = (search_problem.getCostOfActions(path_trace))
                pq.push({"node":sucessor, "path":path_trace}, cost)
        # if its empty there is no solution
        if pq.isEmpty():
            return None

        # do while
        while True and not pq.isEmpty():
            # the next state to check
            temp_dic = pq.pop()
            # keep the actual state and the path
            actual_state = temp_dic["node"][0]
            # if its in already visited continue
            if actual_state not in already_visited: 
                break

        # append it to already visited
        already_visited.append(actual_state)
        path_trace = temp_dic["path"]
            
    return path_trace

def nullHeuristic(state, search_problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(search_problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    # queue of sucessors
    pq : PriorityQueue = PriorityQueue()
    # list of path
    path_trace : list = list()
    # list of already visited
    already_visited : list = list()
    # actual state (coordinates)
    actual_state = search_problem.getStartState()
    # temporal dictionary
    temp_dic = dict()
    temp_dic["path"] = list()
    # cost
    cost = 0 

    # sucessors -> coord[0], card[1], cost[2]
    already_visited.append(actual_state)

    # while the actual state is not the goal state
    # import pdb;pdb.set_trace()
    while not search_problem.isGoalState(actual_state):
        # the actual sucessors will be updated with the actual state
        # print ("current node:", actual_state)
        actual_sucessors = search_problem.getSuccessors(actual_state)
        for sucessor in actual_sucessors:
            # if its not visited it will be pushed
            if sucessor[0] not in already_visited:
                # with all the data of the path and cost
                path_trace = temp_dic["path"].copy()   
                path_trace.append(sucessor[1])
                # cost equals cost of actions + heuristic
                cost = (search_problem.getCostOfActions(path_trace) + 
                        heuristic(sucessor[0], search_problem))
                pq.push({"node":sucessor, "path":path_trace}, cost)
        # if its empty there is no solution
        if pq.isEmpty():
            return None

        # do while
        while True and not pq.isEmpty():
            # the next state to check
            temp_dic = pq.pop()
            # keep the actual state and the path
            actual_state = temp_dic["node"][0]
            # if its in already visited continue
            if actual_state not in already_visited: 
                break

        # append it to already visited
        already_visited.append(actual_state)
        path_trace = temp_dic["path"]
            
    return path_trace
    # from util import PriorityQueue
    # # queue of sucessors
    # pq : PriorityQueue = PriorityQueue()
    # # list of path
    # path_trace : list = list()
    # # list of already visited
    # already_visited : list = list()
    # # list of already visited cost
    # already_visited_cost : list = list()
    # # actual state (coordinates)
    # actual_state = search_problem.getStartState()
    # # temporal dictionary
    # temp_dic = dict()
    # temp_dic["path"] = list()
    # temp_dic["cost"] = int(0)
    # temp_dic["realcost"] = int(0)
    # # cost
    # cost = 0 
    # realcost = 0 
    # # list that will keep solutions
    # solutions = list()
    
    # # sucessors -> coord[0], card[1], cost[2]
    # already_visited.append(actual_state)

    # # while the actual state is not the goal state
    # while 1:
    #     # the actual sucessors will be updated with the actual state
    #     actual_sucessors = search_problem.getSuccessors(actual_state)
    #     for i in actual_sucessors:
    #         # if its already visited but has lest cost, it gets selected
    #         if i[0] not in already_visited or (i[2]
    #                                             < already_visited_cost
    #                                             [already_visited.index(i[0])]):
    #             # it get replaced in case that its already visited
    #             if i[0] in already_visited:
    #                 already_visited_cost[already_visited.index(i[0])] = i[2]
    #             # if its not visited it will be pushed
    #             # with all the data of the path and cost
    #             path_trace = temp_dic["path"].copy()   
    #             path_trace.append(i[1])
    #             realcost = temp_dic['realcost']
    #             realcost += i[2]
    #             cost = temp_dic["cost"]
    #             cost += (heuristic(i[0], search_problem) + realcost)
    #             pq.push({"node":i, "path":path_trace, "cost": cost, "realcost": realcost}, cost)
    #     # the next state to check
    #     temp_dic = pq.pop()
    #     # append it to allready visited
    #     already_visited.append(temp_dic["node"][0])
    #     already_visited_cost.append(temp_dic["node"][2])
    #     # keep the actual state and the path
    #     actual_state = temp_dic["node"][0]
    #     path_trace = temp_dic["path"]

    #     if search_problem.isGoalState(actual_state):
    #         solutions.append(temp_dic)

    #     if pq.isEmpty() and len(solutions) > 0:
    #         break
        
    # cost = int(solutions[0]['cost'])
    
    # for i in solutions:
    #     if int(i['cost']) <= cost:
    #         cost = int(i['cost'])
    #         path_trace = i['path']

    # return path_trace


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
