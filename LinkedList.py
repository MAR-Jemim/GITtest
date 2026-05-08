class SinglyNode:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self, arr:list = None):
    self.head = None
    if not arr:
      return
    self.extend(arr)

  def __str__(self):
    cur = self.head
    display = []
    while cur:
      display.append(str(cur.data))
      cur = cur.next
    return '->'.join(display)

  def append(self, data):
    new = SinglyNode(data)
    if not self.head:
      self.head = new
      return
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = new

  def append_left(self, data):
    new = SinglyNode(data)
    if not self.head:
      self.head = new
      return
    new.next = self.head
    self.head = new

  def display_reverse(self, cur:SinglyNode=None):
    if not self.head:
        print(None)
        return
    if cur is None:
        cur = self.head
    if cur.next:
        self.display_reverse(cur.next)
        print('<-', end='')
    print(cur.data, end='')
    if cur == self.head:
        print()

  def extend(self, arr: list):
    for i in arr:
      self.append(i)

  # pop function has used node.value instead of node.data
  # need to fix it.
  def pop(self):
    if not self.head:
      raise ValueError("The linked list is already empty")
    elif not self.head.next:
      val = self.head.value
      self.head = None
      return val
    cur = self.head
    while cur.next and cur.next.next:
      cur = cur.next
    val = cur.next.value
    cur.next = None
    return val




if __name__ == '__main__':
  ll = SinglyLinkedList([1,2,3,4,5])
  print(ll.pop())
  print(ll.pop())
  print(ll.pop())
  ll.display_reverse()