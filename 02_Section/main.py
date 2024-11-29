myset1 = set([1,3,24,4,5,6])
myset2 = set((1,2,3,4,5,6))
myset = set((10,40,12,30))

mysetA = { 1,2,3}
mysetB = { 3,2,1}
print(myset)

print(myset1)
print(myset2)



operations = {

  "add": lambda x, y: x + y,
  "subtract": lambda x, y: x - y,
  "multiply": lambda x, y: x * y,
  "divide": lambda x, y: x / y if y != 0 else "Division by zero!"
}



print(operations)
result = operations["add"](5, 3)
print(result)


result = operations["divide"](10, 2)
print(result)



result = operations["divide"](10, 0)
print(result)