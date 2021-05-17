# ----------------Recursion------------
import sys
def rec(n):
   if n==1:
     print("Lavanya")
   else:
     print("Lavanya")
     rec(n-1)
rec(3)
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())