'''
    This file demonstrates multiple ways for collecting the names of selected node
'''
import MaxPlus

'''
    Collects selected node names and loop through each node appending it's name to a list
'''
nodes = MaxPlus.SelectionManager.GetNodes()
node_names = []

for n in nodes:
	node_name = n.GetName()
	node_names.append( node_name )	
print node_names

'''
    Collects each selected node's name into a list
'''
nodes = MaxPlus.SelectionManager.GetNodes()
node_names = [n.GetName() for n in nodes]
print node_names
