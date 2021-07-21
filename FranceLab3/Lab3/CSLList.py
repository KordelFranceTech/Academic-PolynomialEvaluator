#CSLList.py
#Kordel France
########################################################################################################################
#This file contains the specification class for a circular singly linked list (C S L List).
########################################################################################################################

from Lab3.Node import Node


class CSLList:
    """
    The CSLList class is a circular singly linked list ADT used to represent a multi-term.
    :param coef: The coefficient of the polynomial.
    ;param xdeg: The degree of the x-term.
    ;param ydeg: The degree of the y-term.
    ;param zdeg: The degree of the z-term.
    """
    def __init__(self, coef=None, xdeg=None, ydeg=None, zdeg=None):
        if xdeg is None:
            self.head = None
        else:
            self.head = Node(coef, xdeg, ydeg, zdeg)
        self.tail = self.head


    def getNode(self, degree):
        """
        Searches for and returns a particular node in the CSLList if found with the specified maximum degree.
        :param degree: The maximum degree of the desired polynomial node.
        ;return coef: The coefficient of the searched node.
        """
        try:
            curNode = self.head
            while curNode is not None and curNode.deg >= degree:
                curNode = curNode.next

            if curNode is None or curNode.deg != degree:
                return 0.0
            else:
                return curNode.coef
        except:
            print('***Error: the degree of this polynomial is negative')


    def appendToList(self, coef, xdeg, ydeg, zdeg):
        """
        Appends a new polynomial term to the current CSLList.
        :param coef: The coefficient of the polynomial to append.
        :param xdeg: The x-degree of the polynomial to append.
        :param ydeg: The y-degree of the polynomial to append.
        :param zdeg: The z-degree of the polynomial to append.
        """
        if coef != 0.0:
            node = Node(coef, xdeg, ydeg, zdeg)
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node

    def printFullList(self):
        """
        Prints the contents of the entire CSSLList as a readable polynomial.
        """
        curNode = self.head
        while curNode is not None:
            if curNode.next is not None:
                print(f'{curNode.coef} x^{curNode.xdeg} y^{curNode.ydeg} z^{curNode.zdeg} + ', end='')
            else:
                print(f'{curNode.coef} x^{curNode.xdeg} y^{curNode.ydeg} z^{curNode.zdeg}\n')
            curNode = curNode.next


    def returnFullList(self):
        """
        Prints the contents of the entire CSSLList as a readable polynomial.
        """
        curNode = self.head
        fullList = ''
        while curNode is not None:
            if curNode.next is not None:
                fullList += f'{curNode.coef} x^{curNode.xdeg} y^{curNode.ydeg} z^{curNode.zdeg} + '
            else:
                fullList += f'{curNode.coef} x^{curNode.xdeg} y^{curNode.ydeg} z^{curNode.zdeg}'
            curNode = curNode.next
        return fullList


    def __add__(self, opList):
        """
        Overwrites the add function so that a distinctive order of operations can be performed specific
            to our polynomial circular singly linked list.
        ;param opList: the CSLList to add to this CSLList.
        ;returns resultList: a CSLList that is the product of both added CSLLists.
        """
        try:
            resultList = CSLList()
            n0 = self.head
            n1 = opList.head

            while (n0 is not None) and (n1 is not None):
                global shiftN0
                global shiftN1
                shiftN0 = False
                shiftN1 = False

                if (n0.xdeg == n1.xdeg) and (n0.ydeg == n1.ydeg) and (n0.zdeg == n1.zdeg):
                    xdeg = n0.xdeg
                    ydeg = n0.ydeg
                    zdeg = n0.zdeg
                    coef = n0.coef + n1.coef
                    shiftN0 = True
                    shiftN1 = True
                else:
                    xdeg = n1.xdeg
                    ydeg = n1.ydeg
                    zdeg = n1.zdeg
                    coef = n1.coef
                    shiftN1 = True

                if shiftN0 == True:
                    n0 = n0.next
                if shiftN1 == True:
                    n1 = n1.next

                resultList.appendToList(coef, xdeg, ydeg, zdeg)

            while n0 is not None:
                resultList.appendToList(n0.coef, n0.xdeg, n0.ydeg, n0.zdeg)
                n0 = n0.next

            while n1 is not None:
                resultList.appendToList(n1.coef, n1.xdeg, n1.ydeg, n1.zdeg)
                n1 = n1.next

            return resultList
        except:
            print('***Error: the degree of this polynomial is negative')

    def __sub__(self, opList):
        """
        Overwrites the subtract function so that a distinctive order of operations can be performed specific
            to our polynomial circular singly linked list.
        ;param opList: the CSLList to subtract from this CSLList.
        ;returns resultList: a CSLList that is the product of both subtracted CSLLists.
        """
        try:
            resultList = CSLList()
            n0 = self.head
            n1 = opList.head

            while (n0 is not None) and (n1 is not None):
                global shiftN0
                global shiftN1
                shiftN0 = False
                shiftN1 = False

                if (n0.xdeg == n1.xdeg) and (n0.ydeg == n1.ydeg) and (n0.zdeg == n1.zdeg):
                    xdeg = n0.xdeg
                    ydeg = n0.ydeg
                    zdeg = n0.zdeg
                    coef = n0.coef - n1.coef
                    shiftN0 = True
                    shiftN1 = True
                else:
                    xdeg = n1.xdeg
                    ydeg = n1.ydeg
                    zdeg = n1.zdeg
                    coef = n1.coef
                    shiftN1 = True

                if shiftN0 == True:
                    n0 = n0.next
                if shiftN1 == True:
                    n1 = n1.next

                resultList.appendToList(coef, xdeg, ydeg, zdeg)

            while n0 is not None:
                resultList.appendToList(n0.coef, n0.xdeg, n0.ydeg, n0.zdeg)
                n0 = n0.next

            while n1 is not None:
                resultList.appendToList(n1.coef, n1.xdeg, n1.ydeg, n1.zdeg)
                n1 = n1.next

            return resultList
        except:
            print('***Error: the degree of this polynomial is negative')

    def __mul__(self, opList):
        """
        Overwrites the multiply function so that a distinct order of operations can be performed specific
            to our polynomial circular singly linked list.
        This is different than the getProductOfTerms function in that this multiplies the terms together and
            then calls getProductOfTerms to distribute the multiplication to all terms in the CSLList.
        ;param opList: the CSLList to multiply this CSLList by.
        ;returns resultList: a CSLList that is the product of both multiplied CSLLists.
        """
        try:
            n = self.head
            resultList = opList.getProductOfTerms(n)
            n = n.next
            while n is not None:
                resultList += opList.getProductOfTerms(n)
                n = n.next
            return resultList
        except:
            print('***Error: the degree of this polynomial is negative')

    def __truediv__(self, opList):
        """
        Overwrites the divide function so that a distinct order of operations can be performed specific
            to our polynomial circular singly linked list.
        This is different than the getQuotientOfTerms function in that this divides the terms together and
            then calls getQuotientOfTerms to distribute the multiplication to all terms in the CSLList.
        ;param opList: the CSLList to multiply this CSLList by.
        ;returns resultList: a CSLList that is the quotient of both divided CSLLists.
        """
        try:
            n = self.head
            resultList = opList.getQuotientOfTerms(n)
            n = n.next
            while n is not None:
                resultList -= opList.getQuotientOfTerms(n)
                n = n.next
            return resultList
        except:
            print('***Error: the degree of this polynomial is negative')


    def getProductOfTerms(self, termNode):
        """
        Performs the distributed multiplication product of terms between two polynomials.
        :param termNode: The CSLList to multiply the current CSLList by.
        ;return resultList: The CSLList containing the product of the two polynomials.
        """
        resultList = CSLList()
        curNode = self.head
        while curNode is not None:
            resultDegx = curNode.xdeg + termNode.xdeg
            resultDegy = curNode.ydeg + termNode.ydeg
            resultDegz = curNode.zdeg + termNode.zdeg
            resultCoef = curNode.coef * termNode.coef
            resultList.appendToList(resultCoef, resultDegx, resultDegy, resultDegz)
            curNode = curNode.next
        return resultList


    def getQuotientOfTerms(self, termNode):
        """
        Performs the distributed division of terms between two polynomials.
        :param termNode: The CSLList to divide the current CSLList by.
        ;return resultList: The CSLList containing the quotient of the two polynomials.
        """
        resultList = CSLList()
        curNode = self.head
        while curNode is not None:
            resultDegx = curNode.xdeg - termNode.xdeg
            resultDegy = curNode.ydeg - termNode.ydeg
            resultDegz = curNode.zdeg - termNode.zdeg
            resultCoef = curNode.coef / termNode.coef
            resultList.appendToList(resultCoef, resultDegx, resultDegy, resultDegz)
            curNode = curNode.next
        return resultList


    def evaluateList(self, xVal, yVal, zVal):
        """
        Overwrites the add function so that a distinctive order of operations can be performed specific
            to our polynomial circular singly linked list.
        ;param xVal: the integer or floating-point value for the x parameter.
        ;param yVal: the integer or floating-point value for the y parameter.
        ;param zVal: the integer or floating-point value for the z parameter.
        ;returns result: a single integer or floating point value of the evaluated function.
        """
        result = 0.0
        # if self.deg >= 0:
        try:
            curNode = self.head
            while curNode is not None:
                xResult = pow(xVal, curNode.xdeg)
                yResult = pow(yVal, curNode.ydeg)
                zResult = pow(zVal, curNode.zdeg)
                result += curNode.coef * xResult * yResult * zResult
                curNode = curNode.next
            return result
        except:
            print('***Error: the degree of this polynomial is negative')
