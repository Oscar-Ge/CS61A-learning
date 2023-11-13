### CS61A lect4

```
def fib(n): 
 """Compute the nth Fibonacci number, for N >= 1."""
 pred, curr = 0, 1 # 0th and 1st Fibonacci numbers
 k = 1 # curr is the kth Fibonacci number
 while k < n: 
 pred, curr = curr, pred + curr 
 k = k + 1
 return curr
```
**Describing Functions**
A function's domain is the set of all inputs it might possibly take as arguments.
A function's range is the set of output values it might possibly return.
A pure function's behavior is the relationship it creates between input and output
Give each function exactly one job, but make it apply to many related situations!
Don’t repeat yourself (DRY): Implement a process just once, but execute it many times
**Generalizing Over Computational Processes**
Summation Example:
```
def cube(k): return pow(k, 3)
def summation(n, term):
 """Sum the first n terms of a sequence.
 
 >>> summation(5, cube)
 225
 """
 total, k = 0, 1
 while k <= n:
 total, k = total + term(k), k + 1
 return total
 ```
 **Functions as Return Values**
 Functions defined within other function bodies are bound to names in a local frame
 ```
 def make_adder(n):
 """Return a function that takes one argument k and returns k + n.
 >>> add_three = make_adder(3)
 >>> add_three(4)
 7
 """
 def adder(k): 
     return k + n 
 return adder
```
make_adder(3)(4)
oprater operand
**Lambda Expressions**
`square = lambda x: x * x`
an expression: evaluates to a function
unimportant in Python but important in other languages
**Lambda Expressions Versus Def Statements**
Only the def statement gives the function an intrinsic name, which shows up in environment diagrams but doesn't affect execution (unless the function is printed)
**return**
return statements:
A return statement completes the evaluation of a call expression and provides its value:
f(x) for user-defined function f: switch to a new environment; execute f's body
Only one return statement is ever executed while executing the body of a function
`return None`----End the function directly
**control**
difference:
```
if __________: 
 _________ 
else: 
 _________
```
and
`if_(________, ________, ________)`
Execution Rule for Conditional Statements:
Each clause is considered in order.
1. Evaluate the header's expression (if present).
2. If it is a true value (or an else header), execute the suite & skip the remaining clauses.
Evaluation Rule for Call Expressions:
1. Evaluate the operator and then the operand subexpressions
2. Apply the function that is the value of the operator to the arguments that are the values of the operands

**Logical Operators**
To evaluate the expression <left> and <right>:
1. Evaluate the subexpression <left>.
2. If the result is a false value v, then the expression evaluates to v.
3. Otherwise, the expression evaluates to the value of the subexpression <right>.
To evaluate the expression <left> or <right>:
1. Evaluate the subexpression <left>.
2. If the result is a true value v, then the expression evaluates to v.
3. Otherwise, the expression evaluates to the value of the subexpression <right>.

**Conditional Expressions**
A conditional expression has the form
<consequent> if <predicate> else <alternative>
Evaluation rule:
1. Evaluate the <predicate> expression.
2. If it's a true value, the value of the whole expression is the value of the <consequent>.
3. Otherwise, the value of the whole expression is the value of the <alternative>.
```
>>> x = 0
>>> abs(1/x if x != 0 else 0) 
```
