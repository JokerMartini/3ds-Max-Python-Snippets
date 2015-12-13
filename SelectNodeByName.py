'''
    This file demonstrates multiple ways for collecting scene nodes by name
'''
import MaxPlus

names = ["Teapot001", "Box001", "Sphere001", "Ball"]
nodes = MaxPlus.INodeTab()

for n in names:
	node = MaxPlus.INode.GetINodeByName(n)
	if node:
		nodes.Append(node)

MaxPlus.SelectionManager.ClearNodeSelection()
MaxPlus.SelectionManager.SelectNodes(nodes)
