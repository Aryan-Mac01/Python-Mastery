#Syntax: ( expression for item in items if condition ) doen't create am entire list but makes a stream instead

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = sum( sale for sale in daily_sales if sale>5 )