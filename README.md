# Check if 2 complete triangles can be found given Triangulation of a polynomial
![picture](img/picture.png)



## The simple solution is 
	1) convert the input from text to dictionary
	2) Make a list of all points, and the number of adjacent points
	3) Sort them in decreasing order w.r.t number of points
	4) For each point that has not been assigned colour (points inside the polygon), 
		i) calculate the number of points adjacent to this point, that do not have a colour
		ii) If this number is 2, then one can guarantee that we can find two complete triangle
		ii) This is a sufficient condition.
		


This solution will only work, when number of points inside polynomial >=3.
We can prove that by construction that if  you find two uncoloured point adjacent to another uncoloured point (that is there is an edge between them), there exists a way to colour the points inside the polygon such that two complete triangles can be found.

## Resources:
https://www.geeksforgeeks.org
https://docs.scipy.org
https://docs.python-guide.org/writing/tests/
https://docs.python.org/3/library/unittest.html
https://www.cs.ucsb.edu/~suri/cs235/Triangulation.pdf


To code it took me 1 hour approximately;
To write all comments: another 30 minutes
It took me 1 hours to understand the problem, and 1 hour to theoretically come up with a refined solution. 
It took me a while to convert the graph to input


If I had to start over again, I might want to solve a general case; optimize the code in few places, and try to print the solution. That is assigning colours to the points


### CODE
This code is written on python 2.7.14 |Anaconda custom (64-bit)| (default, Oct 27 2017, 11:24:26) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]

This code uses numpy library : numpy V 1.12.1

To Run the code
run from the terminal

python Check.py "path to Input"

A sample input is given in input.txt for the figure above.


To run test cases:
	uncomment line 167 unittest.main()
	and comment line 168 main()
	and make sure to change the path in line 37 and 44 in the class Test.
