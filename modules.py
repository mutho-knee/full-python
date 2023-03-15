import math
import statistics
from mymodule import x,y
import mymodule


mymodule.shule("eMobilis Mobile Technology")

print("Addition", mymodule.x + mymodule.y)
print("Subtraction", mymodule.x - mymodule.y)
print("Multiplication", mymodule.x * mymodule.y)
print("Division", mymodule.x / mymodule.y)
print(x+y)

# This are inbuild modules
print(math.sqrt(25))
dataset = [6, 2, 1, 4, 78, 4, 7, 4, 1, 87]
x = statistics.mean(dataset)
print("Mean is ", x)
y=statistics.median(dataset)
print("The median is",y)
v=statistics.mode(dataset)
print("The mode is",v)
v=statistics.fmean(dataset)
print("The fmean is",v)
