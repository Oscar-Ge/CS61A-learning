### CS61A lect2
Anatomy of a Call Expression：operator, operand
add ( 2 , 3 )
Operator Operand Operand
Operators and operands are also expressions


**Evaluation procedure for call expressions:**
1. Evaluate the operator and then the operand subexpressions
2. Apply the function that is the value of the operator 


to the arguments that are the values of the operands

**Execution rule for assignment statements:**
1. Evaluate all expressions to the right of = from left to right.
2. Bind all names to the left of = to those resulting values in the current frame.

**Execution procedure for def statements:**
1. Create a function with signature `<name>(<formal parameters>)`
2. Set the body of that function to be everything indented after the first line
3. 3. Bind `<name>` to that function in the current frame

**Procedure for calling/applying user-defined functions (version 1):**
1. Add a local frame, forming a new environment
2. Bind the function's formal parameters to its arguments in that frame
3. Execute the body of the function in that new environment

**Most important two things I’ll say all day:**
1. An environment is a sequence of frames.
2. A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.



Exercise:

What is the value of the final expression in this sequence? 

`f = min `

 `f = max `

 `g, h = min, max `

`max = g `

`max(f(2, g(h(1, 5), 3)), 4)`

