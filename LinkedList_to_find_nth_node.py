count = 0
data = 0
class Node(object):
	def __init__(self, d):
		self.data = d
		self.next = None
def getNode(data):
	newNode = Node(0)
	newNode.data = data
	newNode.next = None
	return newNode
def findNthFromLast(head, n, nth_last) :
	global count
	global data
	if (head == None):
		return
	findNthFromLast(head.next, n, nth_last)
	count = count + 1
	if (count == n) :	
		data = head.data
def findNthFromLastUtil(head, n) :
	global count
	global data
	nth_last = Node(0)
	count = 0
	findNthFromLast(head, n, nth_last)
	if (nth_last != None) :
		print("Nth node from last is: " , data)
	else:
		print("Node does not exists")

""" linked list: 4.2.1.5.3"""
head = getNode(4)
head.next = getNode(2)
head.next.next = getNode(1)
head.next.next.next = getNode(5)
head.next.next.next.next = getNode(3)
n = 2
findNthFromLastUtil(head, n)
