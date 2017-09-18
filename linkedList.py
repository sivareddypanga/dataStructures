class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.numberofnodes = 0
        self.head = None

    def addStart(self, data):
        nodeObj = Node(data)
        nodeObj.next = self.head
        self.head = nodeObj
        self.numberofnodes += 1

    def addLast(self, data):
        if self.head == None:
            self.add(data)
            return
        else:
            node_obj = Node(data)
            temp = self.head
            while(temp):
                temp = temp.next
            temp.next = node_obj
            self.numberofnodes += 1

    def addAtPos(self, position, data):
        if position <= 1:
            self.addStart(data)
            return
        if position > self.numberofnodes:
            self.addLast(data)
            return

        temp = self.head
        prevTemp = self.head
        nodeObj = Node(data)
        for i in range(position-1):
            prevTemp = temp
            temp = temp.next

        prevTemp.next = nodeObj
        nodeObj.next = temp
        self.numberofnodes += 1
        del temp, prevTemp

    def remStart(self):
        if self.head is None:
            print ("can't remove from an empty List")
            return
        else:
            temp = self.head.next
            self.head = temp
            del temp
            self.numberofnodes -= 1

    def remLast(self):
        if self.head is None:
            print "Can't remove from an empty list"
            return
        if self.head.next is None:
            self.head = None
            self.numberofnodes -= 1
            return
        temp = self.head
        prevTemp = self.head
        while temp.next!= None:
            prevTemp = temp
            temp = temp.next

        prevTemp.next = None
        del prevTemp, temp
        self.numberofnodes -= 1

    def  printList(self):
        if self.head is None:
            print "Can't Print, List is empty"
            return
        temp = self.head
        while(temp):
            print (temp)
            temp = temp.next

    def ReversePrint(self):
        if self.head is None:
            return
        else:
            self.ReversePrint(self.head.next)
            print self.head.data
