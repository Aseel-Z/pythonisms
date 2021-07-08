import pytest
from pythonisms import * 


def test_append_one():
  list = LinkedList()
  list.append(6)
  print(str(list))
  assert str(list) == ' >>6'


def test_str_two():
  list = LinkedList()
  list.append(1)
  list.append(2)
  list.append(3)
  assert str(list) == ' >>1 >>2 >>3'


def test_iter_three():
  list = LinkedList()
  list.append(1)
  list.append(2)
  list.append(3)
  iter_list = []
  for element in list:
    iter_list.append(element)
  assert iter_list == [1,2,3]

def test_decorator():

  assert random(5) < 16 and random(5) > 4




