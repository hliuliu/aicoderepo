



class ai_node(object):
	'''
	A node used in an AI search problem.
	'''
	def __init__(self,state,parent,action,path_cost):
		self.state = state # the state of the node in the problem being solved, can be any object
		self.parent = parent # parent ai_node in the search tree
		self.action = action # a label for the action taken to get from parent node to this node. must be hashable
		self.path_cost = path_cost # a nonnegative number determining a cost of the path going from the root node of the search tree, to this one



class ai_problem(object):
	'''
	A datatype storing the details of a problem used for AI search
		The standard 4-tuple AI definition is modelled here
	'''
	def __init__(self, initial_state, action_set):
		self.initial_state = initial_state # the initial state of the problem
		self.action_set = set(action_set) # a sequence of action labels. must be hashable
		self.action_list = list(action_set) # in case the order of actions metter

	def result(self, state, action):
		'''
			The result successor function.
			Currently returns the original state assuming actions are all useless
			Should be overriden in a subclass
			Call this superclass method first for best results
		'''
		if action not in self.action_set:
			raise ValueError("The specified action is not in the list")
		return state


