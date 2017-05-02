# Given a list of tasks and the time each one need to spend to finish. Also for each task, given a list of the tasks which have to be done before it start. 
# Input is the name of the task and output how long it will take to finish.

# Design the data structure to held all the information for tasks.
# For examples: A needs 7, B starts after A and needs 5,C starts after A and needs 9, D starts after B and C and needs 4. Then calculate how long D will take.

# Use dictionary to store all the data:
# The key is the name of the task:A,B,C,D...
# The value is a list starting with the time each task needs followed by the tasks need to be done ahead.

task_dict = { "A":[7,None],
              "B":[5,'A'],
              "C":[9,'A'],
              "D":[4,'B','C','E'],
              "E":[5,'B']

        }
#recursively calculate the time all the previous tasks will need
def cal_time(task):
    if task is None:
        return 0
    prev = task_dict[task][1:]
    time = [task_dict[task][0]]
    c = len(time)
    i = 0 
    while i < c:
        t = time.pop(0)
        for tp in prev:
            time.append(t+cal_time(tp))
        i += 1

    return max(time)

print(cal_time('D'))

# Give a list of tuples with [childID,parentID], return the root of the tree
# For example: (2,1),(3,1),(1,None),(5,2),(4,1) then return the pointer to node 1 and be able to visit all the nodes in the tree

class Node():
    def __init__(self,v):
        self.value = v
        self.list_of_children = []

    def add_child(self,node):
        self.list_of_children.append(node)

list_pairs = [(2,1),(3,1),(1,None),(5,2),(4,1),(6,5),(7,5)]

def get_root():
    dnode = {}
    root = None
    for pair in list_pairs:
        for n in pair:
            if n not in dnode:
                node = Node(n)
                dnode[n] = node

        if pair[1] is None:
            root = dnode[pair[0]]
        else:
            dnode[pair[1]].add_child(dnode[pair[0]])

    return root
# in-order vist the tree
def print_tree(root):
    print(root.value,'\n')
    if len(root.list_of_children) > 0:
        for n in root.list_of_children:
            print_tree(n)

r = get_root()
print_tree(r)

