points = []
prices =[]
y = float(input("Y-Intercept: "))
xprice = float(input("X-Axis Price: "))
yprice = float(input("Y-Axis Price: "))

while y >= 0:
    for x in range(0,13):
        if (1.5*x + y) > 20 or (5*x + 20*y) > 200: #edit constraints here
            break
        tempvar = (xprice*x)+(yprice*y) #sell price of point totalled
        points.append({'x':x, 'y':y, 'price':tempvar}) #store values
    y = y-1

print(f"{len(points)} points found.") 

for i in range(len(points)):
    prices.append(points[i]['price'])
prices.sort(reverse=True)
bestprice = int(prices[0])


for element in points:
    if element['price']== bestprice:
        bestpoint = "("+str(element['x'])+","+str(element['y'])+")"

print(f"{bestpoint} is the best point/profit.")
