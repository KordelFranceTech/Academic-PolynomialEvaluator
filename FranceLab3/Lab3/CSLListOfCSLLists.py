#CSLListOfCSLlists.py
#Kordel France
########################################################################################################################
#This file contains the specification class for a circular singly linked list (C S L List) of CSL Lists.
########################################################################################################################

from Lab3.Node import Node
from Lab3.CSLList import CSLList


class CSLListOfCSLLists:
    """
    The CSLListOfCSLLists class is a circular singly linked list ADT of circularly linked list (CSLList) objects.
    It is used to hold whole polynomial sequences (ie CSLLists) so that polynomial expressions can be evaluated in
        sequential form.
    :param coef: The coefficient of the polynomial CSLList head.
    ;param xdeg: The degree of the x-term of the polynomial CSLList head.
    ;param ydeg: The degree of the y-term of the polynomial CSLList head.
    ;param zdeg: The degree of the z-term of the polynomial CSLList head.
    """
    def __init__(self, cslList=None):
        if cslList is None:
            self.head = None
        else:
            self.head = CSLList(coef, xdeg, ydeg, zdeg)
        self.tail = self.head


    def appendToList(self, csllist):
        """
        Appends a new polynomial term to the current CSLList.
        :param coef: The coefficient of the polynomial to append.
        :param xdeg: The x-degree of the polynomial to append.
        :param ydeg: The y-degree of the polynomial to append.
        :param zdeg: The z-degree of the polynomial to append.
        """
        if coef != 0.0:
            csllistHead = CSLListOfCSLLists(csllist)
            if self.head is None:
                self.head = csllistHead
            else:
                self.tail.next = csllistHead
            self.tail = csllistHead

    def printFullList(self):
        """
        Prints the contents of the entire CSSLListOfCSLLsits as readable polynomials.
        """
        curCslList = self.head
        while curCslList is not None:
            if curCslList.next is not None:
                print(f'{curCslList.cslList.printFullList()}\n')
            curCslList = curCslList.next


    def returnFullList(self):
        """
        Returns a string of the entire CSSLListOfCSLLists as readable polynomials.
        returns fullList: string of all CSLListOfCSLLists contents
        """
        curCslList = self.head
        fullList = ''
        while curCslList is not None:
            if curCslList.next is not None:
                print(f'{curCslList.cslList.printFullList()}\n')
            curCslList = curCslList.next
        return fullList

