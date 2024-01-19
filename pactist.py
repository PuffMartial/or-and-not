temp = int(input("whats the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temprature is good today")
    print("you may go outside")
elif temp < 0 or temp > 30:
    print("the temprature is bad today")
    print("stay inside")