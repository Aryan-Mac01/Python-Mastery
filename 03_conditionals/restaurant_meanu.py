item = input("What you want today?")
    # write your code below this line
match item.lower():
    case "pizza":
        print("Price: 30 bucks")
    case "burger":
        print("Price: 30 bucks")
    case "pasta":
        print("Price: 30 bucks")
    case "salad":
        print("Price: 30 bucks")
    case _:
        print("Price: 30 bucks")
   