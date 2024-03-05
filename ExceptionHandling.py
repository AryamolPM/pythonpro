#Exercise1:
"""try:
    n=int(input("enter numbers"))
    list1=[]
    for i in range(n):
        element=int(input())
        list1.append(element)
    print(list1)
    for i in list1:
        if i<0:
            raise RecursionError("Something went wrong! please enter a new list")
except RecursionError as e:
    print(e)
"""

# Exercise 2:
"""try:
    n=int(input("enter a list of numbers"))
    if n==0:
        raise ValueError
    list1=[]
    for i in range(n):
        x=int(input())
        list1.append(x)
    print(list1)
    average=sum(list1)/len(list1)
    print("Average=",average)

except ValueError:
    print("Please enter a number other than zero.")
finally:
    print("Program has finished running!")

"""


"""x=re.split("\s",text)
print(x)
for i in x:
    if i[0]=='c':
        print(i)"""



