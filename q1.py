"""
----------------------------------------------------


----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-08"
----------------------------------------------------
"""
from priority_queue_linked import PriorityQueue

pq1 = PriorityQueue()
pq1.insert(3)
pq1.insert(2)
pq1.insert(1)
pq1.insert(34)

pq2, pq3 = pq1.split(3)
for i in pq2:
    print(i)
    