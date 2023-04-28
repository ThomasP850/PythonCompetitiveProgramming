# **Batman vs. Croc**

Killer Croc made off from the Gotham Bank with a sack of gold bars and hid them in the connected
network of sewers below the city. Batman has a map of the sewers and knows the travel time along each
stretch of sewer pipe, so is going to try to retrieve the gold bars. However, Killer Croc, expecting that
Batman would try to play hero again, placed bombs at some of the intersections of the tunnels. Batman
was able to do a satellite scan of the sewer system and discovered exactly where the gold is hidden, where
each bomb is located and at what point it will explode.

Once a bomb explodes, that intersection is
destroyed and is henceforth impassable. It goes without saying that Batman does NOT want to be at an
intersection when a bomb explodes. But because of his finely honed athletic abilities, he will escape
unscathed if he misses the explosion by even a second.

Batman wants to get to the gold in the least
amount of time possible.Your job is to find that minimal time.
<br>
<br>
<br>
![Image of a weighted bidirectional graph with bombs placed on some of the nodes](../../images/Screenshot%202023-04-28%20155157.png)
<br>
<br>
<br>
For example, in the following situation, Batman (starting at the intersection marked J) can get to the gold
(marked Q) in a minimum of 13 seconds. The integers on each sewer line indicate travel time and the
integers at some nodes (surrounded by parentheses) indicate the time a bomb goes off at that node.
Batman starts running at time 0 and all timing on the bombs is relative to time 0.


## **Details of the input**
 - The first line of input contains a single integer, *c*, which is the number of test cases to be processed.
 - For each case, its first line of input contains *a* single integer, *n* (*n* <= 40).
 - There are *n+1* nodes in the input set
numbered *0,1,…,n*.
 - Batman (*J*) is located at node 0 and the gold (*Q*) is located at node *n*.
 - The next line has two integers, *p* and *b* (0 <= *b* <= 10), indicating the number of sewer pipes and bombs, respectively.
 - The next *p* lines each contain three integers, *n1*, *n2*, and *t*, indicating that there is a pipe from node *n1* to node *n2* that takes time *t* to travel.
 - The next *b* lines will contain two integers, *N* and *T*, indicating there is a bomb at node *N* that is set to go off at time *T*. There will be at most one bomb at any intersection.

## **Details of the output**
 - For each input set, output a line of the form  
 &emsp;*Batman can reach the gold in time t.*  
 where *t* is the minimal time required, if Batman can reach the gold at all.
 - If Batman cannot reach the gold, output  
 &emsp; *Batman cannot reach the gold.*

#### **Sample input**
```
1  
12  
20 4  
0 1 4  
0 2 2  
3 0 5  
2 4 1  
2 5 3  
5 4 2  
1 4 1  
1 6 6  
4 6 5  
4 7 4  
7 8 3  
9 5 1  
3 9 5  
6 8 1  
9 10 1  
10 8 1  
8 11 2  
11 12 1  
8 12 4  
6 12 1  
5 4  
4 4  
10 10  
6 8
```
#### **Sample output**
```
Batman can reach the gold in time 13.
```