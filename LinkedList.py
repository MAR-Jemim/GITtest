class SinglyNode:
  def __init__(self, value) -> None:
    self.value = value
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
      display.append(str(cur.value))
      cur = cur.next
    return '->'.join(display) if display else "None"

  def __len__(self) -> int | None:
    count = 0
    cur = self.head
    while cur:
      count += 1
      cur = cur.next
    return count

  def delete(self, instance):
    """Deleting a non-existing node will not raise any error."""
    if not self.head:
      return
    cur = self.head
    if cur.value == instance:
      self.head = cur.next
      return

    while cur.next:
      if cur.next.value == instance:
        cur.next = cur.next.next
        return
      cur = cur.next

  def append(self, value):
    new = SinglyNode(value)
    if not self.head:
      self.head = new
      return
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = new

  def append_left(self, value):
    new = SinglyNode(value)
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
    print(cur.value, end='')
    if cur == self.head:
        print()

  def extend(self, arr: list):
    for i in arr:
      self.append(i)

  def pop(self):
    if not self.head:
      raise IndexError("The linked list is already empty")
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

  def popleft(self):
    if not self.head:
      raise IndexError("The linked list is already empty")
    val = self.head.value
    self.head = self.head.next
    return val



if __name__ == '__main__':
  ll = SinglyLinkedList([2,6,4])
  print(ll)
  ll.delete(7)
  print(ll, len(ll))
  ll.display_reverse()