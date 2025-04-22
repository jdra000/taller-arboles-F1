# Laura Natalia Ballesteros Gualdrón 2221650
# Juan David Rey Ardila 2210080
class node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.sons = []
        self.level = 1

nodeList = []
weight = 1
tempOrder = 0
order = 1

data = input("enter root node data ")
nodeRoot = node(data)
nodeList.append(nodeRoot)

while True:
    try:
        root = nodeList.pop(0)
    except IndexError:
        break
    
    while True:
        data = input(f"enter data for son {root.data} level {root.level+1} or q to move to next node ")
        if data == "q":
            if tempOrder > order :
                order = tempOrder
            tempOrder = 0
            break
        else:
            nodeIns = node(data)
            nodeIns.parent = root
            nodeIns.level = root.level + 1

            nodeList.append(nodeIns)
            weight += 1
            tempOrder += 1

print(f"Tree with {root.level} levels")
print(f"Tree with a weight of {weight}")
print(f"Tree with order {order}")






