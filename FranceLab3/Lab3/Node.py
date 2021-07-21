#Node.py
#Kordel France
########################################################################################################################
#This file contains the specification class for a node of a linked list.
########################################################################################################################

class Node:
    def __init__(self, coef, xdeg, ydeg, zdeg):
        """
        The Node class is used to hold polynomial data as part of a linked list ADT.
        :param coef: The coefficient of the polynomial.
        ;param xdeg: The degree of the x-term.
        ;param ydeg: The degree of the y-term.
        ;param zdeg: The degree of the z-term.
        ;param nodeType: Optional parameter to set node type as coef, xdeg, ydeg, zdeg, etc.
        ;param next: The next node the linker points to.
        """
        self.coef = coef
        self.xdeg = xdeg
        self.ydeg = ydeg
        self.zdeg = zdeg
        self.nodeType = None
        self.next = None

    def getNodeXDegree(self):
        """
        Gets the degree (exponent) of the x-component of the polynomial.
        :returns: The degree of the x-term as an int.
        """
        return self.xdeg

    def getNodeYDegree(self):
        """
        Gets the degree (exponent) of the y-component of the polynomial.
        :returns: The degree of the y-term as an int.
        """
        return self.ydeg

    def getNodeZDegree(self):
        """
        Gets the degree (exponent) of the z-component of the polynomial.
        :returns: The degree of the z-term as an int.
        """
        return self.zdeg

    def getNodeCoefficient(self):
        """
        Gets the coefficient of the polynomial.
        :returns: The coefficient integer of the polynomial.
        """
        return self.coef

    def getNodeType(self):
        """
        Gets the type of parameter this node represents in the polynomial.
        :returns: The node type as a string.
        """
        return self.nodeType

    def getNextNode(self):
        """
        Gets the node that the pointer points to in the circular singly linked list.
        :returns: The node of type Node.
        """
        return self.next

    def setNodeXDegree(self, new_deg):
        """
        Sets the degree (exponent) of the x-component of the polynomial.
        ;param new_deg: The new degree to set the x-component as.
        """
        self.xdeg = new_deg

    def setNodeYDegree(self, new_deg):
        """
        Sets the degree (exponent) of the y-component of the polynomial.
        ;param new_deg: The new degree to set the y-component as.
        """
        self.ydeg = new_deg

    def setNodeZDegree(self, new_deg):
        """
        Sets the degree (exponent) of the z-component of the polynomial.
        ;param new_deg: The new degree to set the z-component as.
        """
        self.zdeg = new_deg

    def setNodeCoefficient(self, new_coef):
        """
        Sets the coefficient of the polynomial.
        ;param new_coef: The new coefficient to set the x-component as as an int.
        """
        self.coef = new_coef

    def setNodeType(self, new_type):
        """
        Sets the type of parameter this node represents in the polynomial.
        ;param new_type: The type of term this node represents in the polynomial as a string.
        """
        self.nodeType = new_type

    def setNextNode(self, new_next_node):
        """
        Sets the node that the pointer references in the linked list.
        ;param new_next_node: The node that the pointer points to as type Node.
        """
        self.next = new_next_node

    def printNode(self):
        """
        Prints the contents of the node to the console including the contents of the node it points to
        """
        print(f'node coefficient: {self.coef}')
        print(f'node xdegree: {self.xdeg}')
        print(f'node ydegree: {self.ydeg}')
        print(f'node zdegree: {self.zdeg}')
        if self.next != None:
            print(f'\tnext node pointer')
            print(f'\tnext node coefficient: {self.next.coef}')
            print(f'\tnext node xdegree: {self.next.xdeg}')
            print(f'\tnext node ydegree: {self.next.ydeg}')
            print(f'\tnext node zdegree: {self.next.zdeg}')
