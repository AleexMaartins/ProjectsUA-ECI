#Autor : Alexandre Martins,103552
#discussed with: Marco Almeida, Bruno Gomes, Tomas Rodrigues
from tree_search import *
from cidades import *
from blocksworld import *



def func_branching(connections,coordinates):
    cidades = MyCities(connections,coordinates)
    done = set()
    nos = 0

    for(cityA,cityB,cost) in connections:
        if cityA not in done:
            nos += len(cidades.actions(cityA))
        if cityB not in done:
            nos += len(cidades.actions(cityB))
        done.add(cityA)
        done.add(cityB)
    return nos / len((done)) -1

class MyCities(Cidades):
    def __init__(self,connections,coordinates):
        super().__init__(connections,coordinates)
        # ADD CODE HERE IF NEEDED

class MySTRIPS(STRIPS):
    def __init__(self,optimize=False):
        super().__init__(optimize)

    def simulate_plan(self, state, plan):
        for act in plan:
            state = self.result(state, act)         
            return state


 
class MyNode(SearchNode):
    def __init__(self,state,parent,cost=0,heuristic=0,depth=0):
        super().__init__(state,parent)
        self.cost = cost
        self.heuristic = heuristic
        self.depth = depth
        #ADD HERE ANY CODE YOU NEED

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
      #  super().__init__(problem,strategy)
        self.optimize = optimize
        self.keep = keep
        self.problem = problem
        self.strategy = strategy
        self.solution = None
        self.non_terminals = 0
        problem_initial = problem.initial if optimize < 2 else problem[-2]

        if optimize == 0:
            root = MyNode(problem_initial, None)
            self.all_nodes = [root]
            self.open_nodes = [0]

        if optimize >= 1:
            root = (problem_initial, None, 0, 0, 0)
            self.all_nodes = [root]
            self.open_nodes = [0]

        #ADD HERE ANY CODE YOU NEED
    

    

    def astar_add_to_open(self,lnewnodes):
        if self.optimize == 0:
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda x: self.all_nodes[x].heuristic + self.all_nodes[x].cost) 
        else: 
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda x: self.all_nodes[x][2] + self.all_nodes[x][2]) #resultado está errado porque nao fiz o 5
        
        

    
    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        #IMPLEMENT HERE
        pass
   

    def get_path(self, node):
        this_parent = node.parent if isinstance(node, MyNode) else node[1]
        this_state = node.state if isinstance(node, MyNode) else node[0]
        if this_parent == None:
            return [this_state]
        path = self.get_path(self.all_nodes[this_parent])
        path += [this_state]
        return(path)

    # procurar a solucao
    def search2(self):
        #self.non_terminals = 0
        while self.open_nodes != []:
            nodeID = self.open_nodes.pop(0)
            node = self.all_nodes[nodeID]
            if self.optimize==0:
                if self.problem.goal_test(node.state):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path(node)
            if self.optimize==1:
                if self.problem.goal_test(node[0]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path(node)
            if self.optimize>=2:
                if self.problem[0][4](node[0],self.problem[2]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path(node)        

            lnewnodes = []
            self.non_terminals += 1
            este_state = node.state if self.optimize == 0 else node[0]
            este_actions = self.problem.domain.actions(este_state) if self.optimize <2 else self.problem[0][0](este_state)
            
            for a in este_actions:
                este_result = self.problem.domain.result(este_state,a) if self.optimize <2 else self.problem[0][1](este_state,a)
                newstate = este_result
                if newstate not in self.get_path(node):
                    if self.optimize == 0:
                        newnode = MyNode(newstate,nodeID, node.cost + self.problem.domain.cost(node.state, a), self.problem.domain.heuristic(newstate, self.problem.goal), node.depth + 1)
                    if self.optimize ==1: #state,parent,cost=0,heuristic=0,depth=0
                        newnode = (newstate,nodeID, node[2] + self.problem.domain.cost(node[0], a), self.problem.domain.heuristic(newstate, self.problem.goal), node[4] + 1) 
                    if self.optimize >=2: #state,parent,cost=0,heuristic=0,depth=0
                        newnode = (newstate,nodeID, node[2] + self.problem[0][2](node[0], a), self.problem[0][3](newstate, self.problem[2]), node[4] + 1) 
                    
                    lnewnodes.append(len(self.all_nodes))
                    self.all_nodes.append(newnode)
            self.add_to_open(lnewnodes)
        return None

# If needed, auxiliary functions can be added




