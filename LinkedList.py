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

  def extend(self, arr: list):
    for i in arr:
      self.append(i)

  def display_reverse(self, cur:SinglyNode=None):
    if self.head is None:
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





if __name__ == '__main__':
  ll = SinglyLinkedList([1,5,3])
  ll.extend([9,7])
  print(ll)
  ll.display_reverse()