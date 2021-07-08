#  iterators/generators on a custom collection

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
 
  def __init__(self):
    self.head = None

  def append(self, value):
      """appends node to a linked list  """
      node = Node(value)
      if not self.head:
          self.head=node
      current = self.head
      while current.next:
          current = current.next
      current.next = node 


  def __iter__(self):
    """makes the linked list iterable"""
    current = self.head
    while current:
      yield current.value
      current = current.next


#  dunder methods make your code more readable and elegant
  def __str__(self):
    """returns a sting represring the linked list"""
    result = ""
    current = self.head
    while current:
      result+= f" >>{current.value}"
      current=current.next
    return result


# a decorator that adds behavior to a given function


def debug_code(any_fun):
  def wrapper(*arg, **kwargs):
    x = arg
    y = kwargs
    print(f'inputs are : {x}, {y}')
    output = any_fun(*arg, **kwargs)
    print(f'output is : {output}')
    return output

  return wrapper


@debug_code
def random(n):
  """generates number between a number and its following number that is larger by 10, n and n+10"""
  import random
  randNum = random.randint(0, n+10)
  print(randNum)
  return(randNum)









