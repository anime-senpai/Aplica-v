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


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	"""
	"*** YOUR CODE HERE ***"

	frontera = util.Stack()
	estadoInicial= problem.getStartState()
	frontera.push((estadoInicial, [],0))
	visitados=[]
	visitados.append(estadoInicial)

	while not(frontera.isEmpty()):
		(estado, camino, costo) =frontera.pop()
		if(problem.isGoalState(estado)):
			break

		sucesores=problem.getSuccessors(estado)
		for sucesor in sucesores:
			if sucesor[0] not in visitados:
				frontera.push((sucesor[0], camino + [sucesor[1]], costo + sucesor[2]))
				visitados.append(sucesor[0])
	return camino

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	from game import Directions

	frontera=util.Queue()
	estadoInicial= problem.getStartState()
	frontera.push((estadoInicial, [],0))
	visitados=[]
	visitados.append(estadoInicial)

	while not(frontera.isEmpty()):
		(estado, camino, costo) =frontera.pop()
		if(problem.isGoalState(estado)):
			break

		sucesores=problem.getSuccessors(estado)
		for sucesor in sucesores:
			if sucesor[0] not in visitados:
				frontera.push((sucesor[0], camino + [sucesor[1]], costo + sucesor[2]))
				visitados.append(sucesor[0])
	return camino

'''def recursiveDLS(nodo, problem, limitee):
	(estado, camino, costo) = nodo
	#print estado[0] , estado[1] , limitee
	if problem.isGoalState(estado):
		return camino
	elif limitee == 0:
		return [0]
	else:
		interrumpio = False
		sucesores=problem.getSuccessors(estado)
		for sucesor in sucesores:
			hijo = (sucesor[0], camino + [sucesor[1]], costo + sucesor[2])
			resultado = recursiveDLS(hijo, problem, limitee-1)
			if resultado == [0]:
				interrumpio = True
			elif(resultado != [-1]):
				return resultado
		if interrumpio:
			return [0]
		else:
			return [-1]

def depthLimiteedSearch(problem, limitee):
	return recursiveDLS((problem.getStartState(),[],0), problem, limitee);


def iterativeDeepeningSearch(problem):
	"""This function is for the first of the grad students questions"""
	"*** MY CODE HERE ***"

	limitee = 1
	while True:
		print limitee
		resultado = depthLimiteedSearch(problem, limitee)
		#print resultado
		if resultado != [0]:
			return resultado
		limitee +=1'''

def iterativeDeepeningSearch(problem):
	"*** MY CODE HERE ***"
	from game import Directions

	frontera = util.Stack()
	limite = 1;

	while True:
		visitados = []
		estadoInicial = problem.getStartState()
		frontera.push((estadoInicial,[],0))
		(estado, camino, costo) = frontera.pop()
		visitados.append(estado)
		while not problem.isGoalState(estado):
			successors = problem.getSuccessors(estado)
			for sucesor in successors:
				if (not sucesor[0] in visitados) and (costo + sucesor[2] <= limite):
					frontera.push((sucesor[0],camino + [sucesor[1]],costo + sucesor[2]))
					visitados.append(sucesor[0])

			if frontera.isEmpty():
				break

			(estado,camino,costo) = frontera.pop()

		if problem.isGoalState(estado):
			return camino

		limite += 1

def inFrontera(e,lista):
	for i in range(len(lista)):
		(estado, camino, costo)= lista[i]
		if e[0]==estado[0] and e[1]==estado[1] :
			return True
	return False

def BidirectionalSearch(problem):
	from game import Directions

	fronteraIni=util.Queue()
	estadoInicial= problem.getStartState()
	fronteraIni.push((estadoInicial, [],0))
	visitadosIni=[]
	visitadosIni.append(estadoInicial)

	fronteraObj=util.Queue()
	estadoObjetivo= (problem.startingPosition,[True,True,True,True,True])
	fronteraObj.push((estadoObjetivo, [],0))
	visitadosObj=[]
	visitadosObj.append(estadoObjetivo)

	while not(fronteraIni.isEmpty()) and not(fronteraObj.isEmpty()):
		(estado, camino, costo) =fronteraIni.pop()
		if(problem.isGoalState(estado) and inFrontera(estado,fronteraObj.list)):
			break

		sucesores=problem.getSuccessors(estado)
		for sucesor in sucesores:
			if sucesor[0] not in visitadosIni and sucesor not in fronteraIni.list:
				fronteraIni.push((sucesor[0], camino + [sucesor[1]], costo + sucesor[2]))
				visitadosIni.append(sucesor[0])

		(estado, camino, costo) =fronteraObj.pop()
		if(estado[0]== problem.startingPosition and estado[1]==[False,False,False,False,False]) and inFrontera(estado,fronteraIni.list):
			break

		sucesores=problem.getSuccessors2(estado)
		for sucesor in sucesores:
			if sucesor[0] not in visitadosObj and sucesor not in fronteraObj.list:
				fronteraObj.push((sucesor[0], camino + [sucesor[1]], costo + sucesor[2]))
				visitadosObj.append(sucesor[0])

	return camino

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"


	util.raiseNotDefined()

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"

	frontera=util.PriorityQueue()
	estadoInicial= problem.getStartState()
	visitados=[]
	nodo = []
	nodo.append(estadoInicial)
	nodo.append(0)
	nodo.append(heuristic(estadoInicial,problem))
	nodo.append([])

	frontera.push(nodo, nodo[1]+nodo[2])

	while not(frontera.isEmpty()):

		nodo = frontera.pop()
		estado = nodo[0]
		costo = nodo[1]
		v = nodo[2]
		camino = nodo[3]

		if(problem.isGoalState(estado)):
			break

		sucesores=problem.getSuccessors(estado)
		for sucesor in sucesores:
			if sucesor[0] not in visitados:
				nodoSuc = []
				nodoSuc.append(sucesor[0])
				nodoSuc.append(costo + sucesor[2])
				nodoSuc.append(heuristic(nodoSuc[0], problem))
				nodoSuc.append(camino + [sucesor[1]])

				frontera.push(nodoSuc, nodoSuc[1]+nodo[2])
				#frontera.push((sucesor[0], camino + [sucesor[1]], costo + sucesor[2]))
				visitados.append(sucesor[0])
	return camino

	#util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
it = iterativeDeepeningSearch
