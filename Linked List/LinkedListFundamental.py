class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return '{}-{}'.format(self.value, self.next.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.value, end='-->')
            current = current.next

    # Thêm phần tử vào đầu Linked List
    def placeOnTop(self, new_value):  # O(1)
        # 1. tạo ra node mới
        new_node = Node(new_value)
        # 2. trỏ node này tới head hiện tại
        new_node.next = self.head
        # 3. set node này là head
        self.head = new_node

    # Thềm phàn tử vào cuối Linked List
    def append(self, new_value):  # O(n)
        # 1. tạo ra node mới
        new_node = Node(new_value)
        # Nếu Linked List rỗng
        if not self.head:
            self.head = new_node

        # Nếu không rỗng
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Thêm phần tử vào sau một phẩn tử bất kỳ
    def insert(self, target_node, new_value):
        if not target_node:
            return

        new_node = Node(new_value)

        new_node.next = target_node.next
        target_node.next = new_node

    def insertByValue(self, target_value, new_value):  # O(n)
        if not target_value:
            return

        target_node = self.head
        while target_node.value != target_value:
            target_node = target_node.next

        new_node = Node(new_value)

        new_node.next = target_node.next
        target_node.next = new_node

    # Xóa một phần tử bất kỳ khỏi Linked List
    def delete(self, target):
        current = self.head
        if current is not None:
            if current.value == target:
                self.head = current.next
                current = None
                return

        while current:
            if current.value == target:
                break
            pre = current
            current = current.next
            
        if not current:
            return

        pre.next = current.next
        current = None


linkedList = LinkedList()
Hanoi = Node('Hanoi')
Danang = Node('Danang')
QuangBinh = Node('QuangBinh')
SaiGon = Node('SaiGon')

linkedList.head = Hanoi
Hanoi.next = QuangBinh
QuangBinh.next = Danang
Danang.next = SaiGon

linkedList.placeOnTop('HaGiang')
linkedList.append('Ca Mau')
linkedList.insertByValue('Ca Mau', 'Nghe An')
linkedList.printList()
