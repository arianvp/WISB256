## A class for polynomials

### Goals

* learn more about Object-oriented programming (inheritance)

### Read

* [Think Python](http://www.greenteapress.com/thinkpython/) ch. 18

### Assignment

Write a superclass to represent real-valued square integrable functions $f:[a,b]\rightarrow \mathbb{R}$ which has the following methods


| method						| description of the method			|
| ----------------------------- | --------------------------------- |
| ```y = f.eval(x)```			| $y = f(x)$						|
| ```g = f.diff(n)```		 	| $g = f^{(n)}$  					| 
| ```g = f.int(n)```  			| $g = f^{(-n)}$ 					|
| ```h = f.add(g)```			| $h = f + g$ 						|
| ```h = f.multiply(g)``` 		| $h = f\cdot g$					|
| ```h = f.divide(g)```    		| $h = f/g$							|
| ```c = f.inner(g)```			| $c = \int_a^bf(x)g(x)\mathrm{d}x$ |
| ```c = f.norm```				| $c = \int_a^bf(x)^2\mathrm{d}x$ 	|

This class is not supposed to be used directly, as the methods cannot be implemented unless we have a specific function in mind. Implement the methods that can be implemented without referring to a particular function and 

Based on this superclass, write a class for polynomials or order $n$
$$
p_n(x) = \sum_{i=0}^ n a_i x ^{i}.
$$

An instance of this class is initialized by giving the coefficients $a_i$. Implement the methods ```eval```, ```diff``` first and adapt your bisection code to take objects of this type as input. 


**Bonus:**
Multiplication of two polynomials with coefficients $a_i$ and $b_i$ yields a polynomial with coefficients

$$
c_k = \sum_ {i=0}^ {n-k} a_i b_{i+k}.
$$

Use this to implement the ```multiply``` method. 

Division of a polynomial by a monomial can be achieved by [Ruffini's rule](http://en.wikipedia.org/wiki/Ruffini%27s_rule). Use this to implement the ```divide``` method. Make sure to add a check that verifies whether the input is a polynomial of order 1 and return an error message otherwise.

Devise an algorithm that finds all the roots of a given polynomial by repeatedly finding a root and dividing it out. For more details see [Horner's method](http://en.wikipedia.org/wiki/Horner%27s_method#Polynomial_root_finding).