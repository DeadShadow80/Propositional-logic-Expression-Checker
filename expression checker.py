#!/usr/bin/python3
#Operators: (,),!,&,|,→,⇔
#Operators=['!','&','|','→','⇔']
#Example1: ((P→(!Q))&(!((P→(!Q))|(!(P⇔R))))  not valid, add a closing parentheses at the end for it to work
#Example2: (P→(Q&R))   valid
import sys,re

def main(argc,argv):
	try:
		i=input("Enter an expression: ")
	except:
		print("Wrong input")
		return
	if len(i)==0:
		print("No input")
	elif len(i)==1:
		if i.isalpha():
			print("Is a unit")
		else:
			print ("Is not a unit, try a letter")
	elif i[0]!="(":
		print("The proposition is missing a parentheses at the begining")
	else:
		i=parse_nested(i)
		if i!=0:
			if recursion(i)==1:
				print("The proposition is valid.")

#Converts the input list into nested lists based on parentheses
def parse_nested(text, left=r'[(]', right=r'[)]'):
    """ Based on https://stackoverflow.com/a/23185606 (unubtu)
	Who based his answer on https://stackoverflow.com/a/17141899/190597 (falsetru) """
    tokens=list(text)
    stack = [[]]
    for x in tokens:
        if not x: continue
        if re.match(left, x):
            stack[-1].append([])
            stack.append(stack[-1][-1])
            #Keep opening parentheses
			#stack[-1].append(x)
        elif re.match(right, x):
            #Keep closing parentheses
			#stack[-1].append(x)
            stack.pop()
            if not stack:
                print('The proposition is missing an opening parantheses')
                return 0
        else:
            stack[-1].append(x)
    if len(stack) > 1:
        print('The proposition is missing a closing parantheses')
       	return 0
    return stack.pop()[0]

#Checks a basic expression (if it contains a list it considers it valid)
def check_expression(expression):
	Operators=['!','&','|','→','⇔']
	if len(expression)!=2 and len(expression)!=3:
		print(str(expression)+" is not an expression.")
		return 0
	if len(expression)==2:
		if expression[0]=="!":
			if type(expression[1])==list:
				return 1
			elif expression[1].isalpha():
				return 1
		else:
			print(str(expression)+" is not a valid expression. Is missing an operator or an atom/proposition")
			return 0
	else:
		if type(expression[0])==list or expression[0].isalpha():
			if (expression[1] in Operators) and expression[1]!='!':
				if type(expression[2])==list or expression[2].isalpha():
					return 1
				else:
					print(str(expression)+" Error: the last argument of the expression is not an unit or expression")
					return 0
			else:
				print(str(expression)+" Error: the expression is missing an operator")
				return 0
		else:
			print(str(expression)+" Error: the first argument of the expression is not an unit or expression")
			return 0

#Checks if an expression doesnt contain lists (it' minimal)
def minimal(expression):
	for each in expression:
		if type(each)==list:
			return 0
	return 1

#Iterates through the expression and checks from the innerest ones
def recursion(expression):
	if minimal(expression):
		return check_expression(expression)
	else:
		for each in expression:
			if type(each)==list:
				#print("Verifying this smaller proposition: "+str(each))
				if recursion(each)==0:
					return 0
		return check_expression(expression)


if __name__ == '__main__':
	main(len(sys.argv),sys.argv)

# Legacy code, could be useful later

# GOOD to skip () for a linear iteration of the expression
# for i,c in enumerate(expression):
# 	if c in ['(',')']:
# 		sw*=-1
# 		last=')'
# 		pass
# 	if sw==1:
# 		pass	
# 	last=c

# OLD CHECK JUST VALIDITY
# st=0
# en=0
# was_not=0
# cond=0
# if was_not==1:
# 	if i==")":
# 		cond=0
# 	was_not=0
# else:
# 	if i=="(":
# 		st+=1
# 	elif i==")":
# 		en+=1
# 	elif i=="!":
# 		was_not=1