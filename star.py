#python3 code to print pyramid pattern using recursion
def pypart(n):
	if n==0:
		return
	else:
		pypart(n-1)
		print("* "*n)

# Driver Code
n = int(input())
pypart(n)

