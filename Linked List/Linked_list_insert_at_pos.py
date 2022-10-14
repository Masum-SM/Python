from email import header
from turtle import position


class Node:
    def __init__(self,value):
        self.value = value
        self.Next = None

class Linked_List:
    def __init__(self):
        self.head = None


    def insert_at_head(self,value):
        newNode = Node(value)
        newNode.Next = self.head
        self.head = newNode

    def inser_in_tail(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.Next != None:
                temp = temp.Next
            temp.Next = newNode


    def insert_at_position(self,pos,value):
        newNode = Node(value)
        if pos == 0:
            self.insert_at_head(value)
        else:   
            temp = self.head
            for i in range(pos-1):
                temp = temp.Next
                if temp == None:
                    print("Out of bound")
                    return
            newNode.Next = temp.Next
            temp.Next = newNode
    

    
    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.Next

def main():
    List = Linked_List()
    List.inser_in_tail(10)
    List.inser_in_tail(20)
    List.inser_in_tail(30)
    List.inser_in_tail(40)
    List.insert_at_head(0)
    List.insert_at_head(-2)
    List.insert_at_position(0,100)
    List.print_linked_list()

main()

        