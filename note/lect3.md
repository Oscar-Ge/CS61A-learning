### CS61A lect3

**None Indicates that Nothing is Returned:**
The special value None represents nothing in Python
A function that does not explicitly return a value will return None
Careful: None is not displayed by the interpreter as the value of an expression
example:`print(print(1), print(2))`
1
2
None None

**Miscellaneous Python Features**
interept：python3 -i xx.py
multiple return values
doctests:
write inputs in the 注释！
for example:
`""">>>q, r=divide_exact(5, 3)`
`>>>q`
`201`
`>>>r`
`3`
`"""`
python3 -m doctest -v xx.py
**Compound Statements**
Execution Rule for a sequence of statements:
• Execute the first statement 
• Unless directed otherwise, execute the rest
**Conditional Statements**
Execution Rule for Conditional Statements:
Each clause is considered in order. 
1. Evaluate the header's expression. 
2. If it is a true value, execute the suite & skip the remaining clauses.


Syntax Tips:
1. Always starts with "if" clause. 
2. Zero or more "elif" clauses. 
3. Zero or one "else" clause, always at the end.
**Boolean Contexts**
False values in Python: False, 0, '', None
True values in Python: Others
**While Statements**
Execution Rule for While Statements:
1. Evaluate the header’s expression. 
2. If it is a true value, execute the (whole) suite, then return to step 1.

