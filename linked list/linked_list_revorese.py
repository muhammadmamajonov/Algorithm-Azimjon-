from nodes import head

# print(head.value)
def revorse(head):
    curr = head.next
    next_ = curr.next
    curr.next = None
    

    while curr:
        print(curr.value, curr.next)
        curr.next = next_
        print(curr.next, head.next)
        next_ = head.next
        print(next_.value)
        head = next_
        print(head.value)
        curr = head
        print(curr.value)



prev = None
cur = head

while cur is not None:
    next_ = cur.next
    cur.next = prev
    prev = cur
    cur = next_


c = prev
while c:
    print(c.value, c.next)
    c = c.next

