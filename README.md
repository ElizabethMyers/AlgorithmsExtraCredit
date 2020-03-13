# Algorithms Extra Credit
A work by: Elizabeth Myers

## NP Problem: Knapsack Problem

### Description and Application
*Find a real world problem that requires an NP algorithm to find its solution. Describe the problem and the applications of the solution; make a case of its importance.* 
A real world problem that requires an NP algorithm to find its solution is the 0-1 Knapsack Problem. The Knapsack Problem is based off a set of request items _i_ and a knapsack with a weight capacity of _W_. Each request item _i_ has a weight and a value. The goal of the Knapsack Problem is to optimize the value in the knapsack by adding items without exceeding the weight limit of the knapsack itself. A more specific and applicable real-world case of the Knapsack Problem is the 0-1 Knapsack Problem. The "0-1" part of this problem means that each item will either be wholly accepted or rejected, rather than being able to take fractions or pieces of items being added. "0" means that the item was not added to the knapsack, while "1" means that the item was added to the knapsack. As mentioned before, this problem requires an NP algorithm to find its solution. The 0-1 Knapsack Problem can be solved using dynamic programming based on the capacity of the knapsack for a heauristic solution. 

The Knapsack Problem has importance and application to anyone who is traveling or taking a bag with them to another location, particularly when flying. Whether carry-on or checked-bags, airlines have restrictions on how heavy passengers' bags can be. This can often be a problem for travelers, particularly those like myself who do not want to have to pay high fees to check bags and are trying to fit all their essentials in a single carry-on bag. The 0-1 Knapsack Problem is important for travelers, as it allows them to assign a value of importance to their items along with its weight, and the solution of this problem can tell them which items they can bring with them while traveling without going over the weight limit. This solution for the problem will save travelers time and effort, for they would have to personally lay each item they are planning on taking with them out and individually choosing which to take with them while constantly weighing their back to ensure they don't go over the weight limit. The solution would also save travelers money as they will not have to pay for a checked bag because their essentials are all in their carry-on, and they will not be charged for a bag that goes over the weight limit when being weighed before takeoff. 

For our problem, let us look at a specific real-world application of this problem. One of my friends was studying abroad in Ireland, so I decided to plan a 5 day trip to see them and sight-see in Ireland. Because my roundtrip flight was over $800 and I was planning to stay for less than a week, I wanted to only bring a carry-on with me so I could save money and not have to drag two rolling suitecases around Ireland by myself. Because I had a limited amount of space in my suitcase and British Airways has a 23kg (~50lb) carry-on weight limit, I had to pack my carry-on carefully with only the essentials. 


### Solution
*Research for a heuristic(approximate) solution of the problem, describe the solution, and implement the solution with a real world input.*
The heuristic solution for the 0-1 Knapsack Problem that I will explore is the dynamic programming solution. In this solution, there are _n_ items given with each item having two integer array values, _val_[0..n-1] for the value of the item and _wt_[0..n-1] for the weight of the item. There is also an integer _cap_ which is the capacity of the knapsack. This algorithm finds the maximum value subset of the item values so the weights of these items added together is less than or equal to the knapsack capacity weight. Because this is the 0-1 Knapsack Problem, either an item is included in the optimal subset or it is not. 


Therefore, the maximum value that can be obtained from n items is max of following two values.
1) Maximum value obtained by n-1 items and W weight (excluding nth item).
2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).
If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.
It should be noted that the above function computes the same subproblems again and again. See the following recursion tree, K(1, 1) is being evaluated twice. Time complexity of this naive recursive solution is exponential (2^n).
Since suproblems are evaluated again, this problem has Overlapping Subprolems property. So the 0-1 Knapsack problem has both properties (see this and this) of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array K[][] in bottom up manner. Following is Dynamic Programming based implementation.
Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.


First, we create a 2-dimensional array (i.e. a table) of n + 1 rows and w + 1 columns.
A row number i represents the set of all the items from rows 1— i. For instance, the values in row 3 assumes that we only have items 1, 2, and 3.
A column number j represents the weight capacity of our knapsack. Therefore, the values in column 5, for example, assumes that our knapsack can hold 5 weight units.
Putting everything together, an entry in row i, column j represents the maximum value that can be obtained with items 1, 2, 3 … i, in a knapsack that can hold j weight units.
Let’s call our table mat for matrix. Therefore, int[][] mat = new int[n + 1][w + 1].
Step 2:
We can immediately begin filling some entries in our table: the base cases, for which the solution is trivial. For instance, at row 0, when we have no items to pick from, the maximum value that can be stored in any knapsack must be 0. Similarly, at column 0, for a knapsack which can hold 0 weight units, the maximum value that can be stored in it is 0. (We’re assuming that there are no massless, valuable items.)
To calculate the maximum value that we can obtain with item i, we first need to compare the weight of item i with the knapsack’s weight capacity. Obviously, if item i weighs more than what the knapsack can hold, we can’t include it, so it does not make sense to perform the calculation. In that case, the solution to this problem is simply the maximum value that we can obtain without item i (i.e. the value in the row above, at the same column).
Therefore, at row i and column j (which represents the maximum value we can obtain there), we would pick either the maximum value that we can obtain without item i, or the maximum value that we can obtain with item i, whichever is larger.

filter_none

*Indispensable:
-Real world data
-Show runtime screenshots*




- Explain

- Code an approximate algorithm for some np problem

- Provide test data
