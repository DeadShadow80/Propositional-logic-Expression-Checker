# Propositional-logic-Expression-Checker

Run the script using python3.
Enter an logical expression with no spaces, letters from the alphabet as atoms, ( and ) as parantheses around an expression, and the following symbols as operators: !,&,|,→,⇔

The script transforms the expression into nested lists, and checks recursively each expression from the inside out.

Examples to try the program with:
# Example1: ((P→(!Q))&(!((P→(!Q))|(!(P⇔R))))
Not valid, it's missing a closing parentheses
# Example2: (P→(Q&R))
Valid
