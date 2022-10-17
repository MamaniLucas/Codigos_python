class Node:
    def __init__(self, data):
        self.item = data 
        self.ref=None


class LinkedLsit:

    def __init__(self):
        self.start_node = None
    def make_new_list(self):
        nums= int(input("Cuantos nodos deseqas crear: "))
        if nums==0:
            return
        for i in range(nums):
            value = int(input("Ingrese el valor del node: "))
            self.insert_at_end(value)
    def get_count(self):
        if self.start_node is None:
             return 0;
        n=self.start_node
        count=0;
        while n is not None:
            count = count + 1
            n=n.ref
        return count
    def traverse_list(self):
        if self.start_node is None:
            print("No tiene elementos")
            return
        else:
            n=self.start_node
            while n is not None:
                print(n.item, " ")
                n=n.ref
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node=new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node

    def insert_after_item(self, x, data):
        n=self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n=n.ref
        if n is None:
            print("item no encontrada")
        else:
            new_node= Node(data)
            new_node.ref=n.ref
            n.ref = new_node
 
    def insert_before_item(self, x, data):
        if self.start_node is None:     
           print("No tiene elementos")
           return
        if x== self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item ==x:
                break
            n =n.ref
            if n.ref is None:
                print("Item no pertenece a lista")
            else:
                new_node = Node(data)
                new_node.ref=n.ref
                n.ref = new_node

   

new_linked_list=LinkedLsit()
print("Mi_lista de elementos")
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(41)
new_linked_list.insert_at_end(42)
new_linked_list.insert_at_end(43)
new_linked_list.insert_at_end(44)
new_linked_list.insert_at_end(45)
new_linked_list.insert_at_end(50)
new_linked_list.insert_at_end(51)
new_linked_list.insert_at_end(52)
new_linked_list.insert_at_end(53)
new_linked_list.insert_at_end(54)

new_linked_list.traverse_list()


