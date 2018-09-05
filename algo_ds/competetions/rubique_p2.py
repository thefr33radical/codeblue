"""
Suraj designed an enhanced version of chess game of size  with top left position as . In this version of game if a piece crosses the border from one side, it enters from the exact opposite side. 

For example :  

if it goes up from  position, it will enter the board from . 
if it goes left from  position , it will enter the board from .

He started with a knight from an initial position. In the first step knight can move to  different positions which get distributed to  knights in these  positions. Now in the second step each of these  knights can move to  different positions, get distributed and so on.

Given an intial position of knight  on the board such that  and , suraj wants to find how many minimum steps required to visit each position on the board. If knight is unable to cover all the positions, print .

Input
: Total number of test cases
In each test case you are given two space integers  and . 
In the next line two space separated integers  and .

Output

Print minimum number of steps such that knights can cover each and every cell on the board.
For each test case, output should be in a different line. 

https://www.hackerearth.com/challenge/competitive/rubique-finhack/algorithm/knights-on-board/

"""
