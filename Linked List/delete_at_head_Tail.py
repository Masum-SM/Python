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

    def delete_at_head(self):
        
        if self.head == None:
            print("Linked list is empty")
            return
        else:
            delNode = self.head
            self.head = self.head.Next
            del delNode

    def delete_at_tail(self):
        temp = self.head
        if self.head != None:
            while temp.Next.Next != None:
                temp = temp.Next
            delNode = temp.Next
            temp.Next = None;
            del delNode
        else:
            if self.head == None:
                print("linked list is empty")
            else:
                self.delete_at_head()


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
    List.inser_in_tail(50)
    List.insert_at_head(0)
    print("Linked list before deletion at head")
    List.print_linked_list()

    print("Linked list After deletion at head")
    List.delete_at_head()

    print("Linked list After deletion at tail")
    List.delete_at_tail()
    List.print_linked_list()

main()

        