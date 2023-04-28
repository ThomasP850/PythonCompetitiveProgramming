# **Alien Chess**
You’ve been taken hostage by aliens. However, they’re relatively fair aliens. They have given you a
chance to win your freedom by winning what they believe to be how the Earthlings play Chess.
However, their version of Chess has a few key differences:

1. Every move must start with your Super Pawn taking a piece.
2. A Super Pawn behaves like the piece it just took. At the start of the game it acts as a pawn.
3. You may perform a combo by, after taking a piece with your Super Pawn, taking another piece
with your Super Pawn.
4. You win by capturing the Enemy’s Super Pawn.
5. The only piece on the board that belongs to you is your Super Pawn. The remaining pieces
belong to your Enemy and include the Enemy’s Super Pawn, regular pawns, rooks, bishops, and
knights.
6. There can be any number of rooks, pawns, and knights, but only one Super Pawn and one Enemy Super Pawn.

A pawn can only capture a piece by moving one
space diagonally forward. Thus the pawn P can
only take pieces in the spots marked with an X.
Forward is always oriented in this direction for
you.  
\- - - - - - - -  
\- - - X - X - -  
\- - - - P - - -  
\- - - - - - - -  

A rook can capture any piece located directly above, below, or to either side of it as long as no other
piece is between the rook and that piece.

A bishop can capture any piece on the diagonals from itself as long as no other piece is between the
bishop and that piece.

A knight can capture pieces in any of the 8 squares located by
moving two squares horizontally and one square vertically, or two
squares vertically and one square horizontally. So a knight, marked
by K, can capture any piece in the spots marked with an X.
NOTE: A knight ‘jumps’ over any other piece between itself and its
target. In other words, it cannot be blocked.

\- - - - - - - -   
\- - - - - - - -  
\- - X - X - - -  
\- X - - - X - -  
\- - - K - - - -  
\- X - - - X - -  
\- - X - X - - -  
\- - - - - - - -  

You are currently on the last possible move before the aliens get bored of the game and revoke their
offer to free you. You are to determine whether or not your next move will free you.

## **Details of the Input**

The first line is a single integer, *n*, denoting the number of games to be played. For each game, the board
is described by 8 lines of 8 characters each. The only possible characters are:

- ‘-‘ an empty position  
- ‘S’ your Super Pawn, which is also your starting position  
- ‘E’ your enemy’s Super Pawn, which is your ending position  
- ‘P’ a Pawn  
- ‘R’ a Rook  
- ‘B’ a Bishop  
- ‘K’ a Knight

There will be one ‘S’ and one ‘E’ on each board. There will be one blank line separating one board
description from the next.

## **Details of the Output**
- There should be one line of output for each of the *n* boards.
- Each output line should begin with “Case i:” where i is the corresponding case number.
- That should be followed by a single space, then either “Yes”
if you can win, or “No” if you cannot win on our next turn.

#### **Sample Input**
```
3
-------E
------P-
-----P--
----P---
---P----
--P-----
-P------
S-------
----E---
--R---R-
--------
--------
--------
--R---R-
-P------
S-------
----R--E
--------
---K----
--------
--------
------B-
-----S--
--------
```
#### **Sample Output**
```
Case 1: Yes
Case 2: No
Case 3: Yes
```