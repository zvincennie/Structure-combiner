# Structure-combiner
This Python code defines functions to manage a linked structure of nodes, including inserting items in ascending order, calculating the length of the structure, and printing its contents. It then prompts the user to input words and constructs the linked structure accordingly.
#Zachary Vincennie U80303351

"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    
    while probe is not None:
        count += 1
        probe = probe.next
    
    return count

def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    
    new_node = Node(newItem)
    
    if head is None or newItem < head.data:
        # If the list is empty or the new item is smaller than the head, 
        # make the new node the new head.
        new_node.next = head
        return new_node
    else:
        current = head
        while current.next is not None and newItem >= current.next.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

def main():
    """Gets words from the user and inserts them in the
    structure referred to by head."""
    
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)
        
    print('The structure contains', length(head), 'items:')
    printStructure(head)

if __name__ == "__main__":
    main()
