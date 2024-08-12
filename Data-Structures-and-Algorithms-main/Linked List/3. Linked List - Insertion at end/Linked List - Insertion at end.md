# Insertion at end is fairly straightforward

**See the following steps:**
1.Make a new node with the desired value.
2.Start at the head and move to the last node of the linked list.
3.Insert the new node after the last node.

The only edge case is when there is no value in the linked list. In that case, we set the head of the linked list to the new node.

**Task**
Complete the function insertAtEnd in IDE to insert an element at the end of a linked list. I have also added a new function getLastValue to print the last value of a linked list.

**Input Format**
First line denotes 'n' the number of elements to be inserted in the list.
Second line consists of n space-separated integers denoting the elements to be added in the list.

**Output Format**
The value at the end of the list after each insertion.

**Constraints**
1 ≤ N ≤ 1000

**Sample 1:**
Input      | Output
4          | 2 32 23 53
2 32 23 53 |

**Explanation:**
Initially we have an empty linked list. After each step:

2
2->32
2->32->23
2->32->23->53
