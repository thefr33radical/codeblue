"""Maximum number of teams that can be formed with given persons
geeksforgeeks
Solution:
  1. until(given M,N >= team1(I,II) or given M,N >= team2(I,II))
      1a.if max(M,N)==M:
            M-=team1(I)
            N-team1(II)
         else:
          M-=team2(I)
          N-team2(II)
     count+=1
"""

"""
https://www.hackerrank.com/challenges/team-formation/problem
hackerrank
Solution:

"""

"""
Given a list of n objects, write a function that outputs  the minimum set of numbers that sum to at least K. FOLLOW UP: can you beat O(n ln n)?
FB interview
Solution :
Construct Heap, pop out until sum(pop(num))+present_sum >=K
"""

"""
Maximize the total profit of all the persons
Geeksfor geeks

Solution:
total= max(Preorder Traversal(left),preorder_traversal(right))+root
"""

"""Maximum possible time that can be formed from four digits
Solution :


"""

