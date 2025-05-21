# DSA Python

## CodeAcademy - DSA Python

### Introduction

- Structure data, so algorithms can maintain, utilize, iterate
- Data Structure -- store and retrieve information
  - input -- how its received
  - process -- manipulating -- concurrently etc
  - maintain -- organization, relationships, memory
  - retrieve -- access, find, search
- What Data Structure to choose
  - Intended purpose -- built-in functionality -- search, sort, iterate
  - Control over memory -- static vs dynamic memory allocation
  - Time taken for activity -- runtime
- Algorithms -- instructions
  - Sorting
  - Searching
  - Divide and Conquer
  - Greedy
  - Brute Force


<br/><br/>

- Computer Science -- software, hardware, algorithms, computation
  - Frontend -- art + ability to program
  - Backend
  - FullStack
  - Data Scientist
  - Cybersecurity
  - Entrepreneurship

### Nodes

- fundamental building block
- contains data, links to other nodes -- pointers
- orphaned node -- node that cannot be referenced, lost, no variable pointing to it

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
```


### Linked Lists

- head and tail nodes
- not required to be sequential in memory because they use links
- operations -- add remove find traverse
- unidirectional or bidirectional

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
```



<br/><br/>

- Swap Nodes
```py
import Node
import LinkedList

def swap_nodes(input_list, val1, val2):
    node1_prev = None
    node2_prev = None

    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
        print("Elements are same, no swap needed")
        return

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible")
        return

    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


ll = LinkedList.LinkedList()
for i in range(10):
    ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
```


<br/><br/>

#### Two Pointer Linked List Technique -- runner technique

##### Two pointers moving in parallel

```py
def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]


def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head()
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1

        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current
```

##### Pointers at different speeds

```py
def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node

    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()

    return slow
```

```py
def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node

    while fast:
        fast = fast.get_next_node()
        if count % 2 != 0:
            slow = slow.get_next_node()
        count += 1
    return slow
```



<br/><br/>

- Floydd's Cycle Detection Algorithm | Tortoise and Hare

```py
def has_cycle(linked_list):
    head_node = linked_list.head_node

    if head_node is None or head_node.get_next_node() is None:
        return False

    fast = head_node
    slow = head_node

    while fast is not None and fast.next is not None:
        slow = slow.get_next_node()
        fast = fast.get_next_node().get_next_node()

        if slow == fast:
            return True
    
    return False
```

- Rotate Linked List by K places

```py
def print_list(head: Node):
    current = head
    nodes = []
    while current:
        nodes.append(str(current.value))
        current = current.next
    print(" --> ".join(nodes) if nodes else "Empty List")

def rotate_right(head: Node, k: int) -> Node:
    if not head or not head.next or k == 0:
        return head
    
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head

    tail.next = head


    steps_to_reach_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_reach_new_tail):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

### Doubly Linked Lists

```py
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
```

```py
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head
```

```py
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail
```

```py
  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()
```

```py
  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()
```

```py
  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    return node_to_remove
```

```py
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
```

```py
subway = DoublyLinkedList()

subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

print(subway.stringify_list())

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())

subway.remove_by_value("Times Square")
print(subway.stringify_list())
```

### Queues

- ordered set of data
- enqueue, dequeue, peek 
- First In, First Out -- FIFO
- bounded queue -- limit in the number of persons or queue length
- queue overflow and underflow

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
```

```py
from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
```

```py
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
```

```py
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")
```

```py
  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("No orders waiting!")
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
```

```py
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")

deli_line.enqueue("western omelet with home fries")

print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()

deli_line.dequeue()
```


### Stacks

- ordered set of data
- push, pop, peek
- Last In, First Out -- LIFO

```py
from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")
```

```py
def peek(self):
    if not self.is_empty():
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0
```

```py
pizza_stack = Stack(6)

pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

pizza_stack.push("pizza #7")

print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.pop()
```

```py
def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))
```

```py
# Towers of Hanoi

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while(num_disks <3):
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
  left_stack.push(i)

num_optimal_moves = (2 ** num_disks) - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while(True):
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]

      print(f"Enter {letter} for {name}")

    user_input = input("")

    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

num_user_moves = 0
while(right_stack.get_size() != num_disks):
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
```

### HashMaps

- hashing functions or hash functions -- return array index or numeric value
  - aka compression functions 
- hash value|hash code|hash mod array_size
- hashing is not reversible process
- hash bucket -- storage location at the index given by hash
- hash collision -- same hash value for different hash keys
  - separate chaining -- say array of linked lists -- frequent collisions make this a poor choice for faster lookups as lookup is now dependent on linked lists
    - we can also have another data structure instead of linked lists (tree/hashmap?)
    - saving keys: we need to save keys to be able to distinguish which key the values belong to
  - open addressing
    - linear probing method -- continue to find until you find an empty slot -- we add fixed number of steps for finding next slot
    - quadratic probing method -- we add 1, 4, 9, ... -- increasingly large numbers
- clustering -- is what happens when a single hash collision causes additional hash collisions
- `str.encode()` -- converts string to corresponding bytes -- list like object

```py
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size
```

```py
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return
```

```py
def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      number_collisions += 1

    return
```

```py
hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
```

```py
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
  
  def hash(self, key):
    key_bytes = key.encode()
    hash = sum(key_bytes)
    return hash

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)

    payload = Node([key, value])

    list_at_array = self.array[array_index]

    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)

    list_at_index = self.array[array_index]

    for item in list_at_index:
      if key == item[0]:
        return item[1]
    return None


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve("daisy"))
```

### Recursion

- strategy for solving problems by defining the problem interms of itself
- base case, recursive step
- call stacks and execution contexts

```py
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)
```

```py
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n - 1)

print(sum_to_one(7))
```

```py
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(12))
```

```py
def power_set(set):
  power_set_size = 2**len(set)
  result = []

  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result


def power_set(my_list):
  if len(my_list) == 0:
    return [[]]
  power_set_without_first = power_set(my_list[1:])
  with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
  return with_first + power_set_without_first
```

```py
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
```

```py
def fibonacci(n):
  if n == 1:
    return n
  if n == 0:
    return n
  
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(5)
fibonacci_runtime = "2^N"
```

```py
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"

  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  
  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))
  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1 : ])

  return tree_node
  
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

runtime = "N*logN"
```

```py
def sum_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        return last_digit + sum_digits(n//10)

sum_digits(539)
```


<br/><br/>

```py
def factorial(n):  
  if n < 0:
    return ValueError("Inputs 0 or greater only")
  result = 1
  while n != 0:
    result *= n
    n -= 1
  return result

def factorial(n):  
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)
```


```py
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")

  fibs = [0, 1]
  
  if n <= len(fibs) - 1:
    return fibs[n]

  while n > len(fibs) - 1:
    fibs.append(fibs[-1] + fibs[-2])
    
  return fibs[-1]
```

```py
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit
```

```py
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

def find_min(my_list, min = None):
  if not my_list:
    return min

  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)
```

```py
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 


def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True

def is_palindrome(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])
```

```py
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

def multiplication(num_1, num_2):
  if num_1 == 0 or num_2 == 0:
    return 0
  
  return num_2 + multiplication(num_1 - 1, num_2)
```


```py
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result

two_level_tree = {
"data": 6, 
"left_child":
  {"data": 2}
}

four_level_tree = {
"data": 54,
"right_child":
  {"data": 93,
   "left_child":
     {"data": 63,
      "left_child":
        {"data": 59}
      }
   }
}


depth(two_level_tree) # 2
depth(four_level_tree) # 4



def depth(tree):
  if not tree:
    return 0

  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1
```


<br/><br/>


```py
def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return []
      
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)

  return result

def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    return head

def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"

  return result
```


### Asymptotic Notation

