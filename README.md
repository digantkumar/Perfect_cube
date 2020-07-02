Write definitions for each of the following Python functions, and for each function, includea clear and concise comment to describe its purpose.  
Store all the function definitions in a single file
1.peaks(numlist) Return the list of elements in the numeric list numlist which exceed all previous elements.
peaks([3, 2, 5, 5, 7, 6, 1, 8, 4]) ==> [3, 5, 7, 8]
peaks([1, 2, 3, 4, 5, 6, 7, 8, 9]) ==> [1, 2, 3, 4, 5, 6, 7, 8, 9]
peaks([9, 8, 7, 6, 5, 4, 3, 2, 1]) ==> [9]
peaks( 5, 5, 5, 5, 5, 5, 5, 5, 5]) ==> [5]
peaks([3]) ==> [3]
peaks([]) ==> []
2.iscube(n) Return True if the integerna perfect cube and False otherwise?  
(Recall that a is aperfect cube if there is some integer b such that b^3=a. Do not use Python’s root-finding capabilities .is_cube(0) ==> True 
is_cube(1) ==> True is_cube(2) ==> False is_cube(8) ==> True is_cube(-8) ==> True3. 
firstcubeabove(n) Return the smallest cube which exceeds the non-negative integern.  Do not use Python’s exponentiation or root-finding capabilities.
first_cube_above(7) ==> 8 first_cube_above(8) ==> 27
