name=input("enter your name:")
print("hello {}".format(name))
qualification=input("enter your qualification:")
if qualification in ("mba", "mca", "btech"):
    year =eval(input("enter your passedout year:"))
    if year in (2018,2019,2020,2021):
        percentage=int(input("enter your percentage:"))
        if percentage >= 0 and percentage <= 50:
            print("you can attend interview in next month")
        elif prrcentage >= 50 and percentage <= 80:
            print("you can attend interview in next month")
        elif percentage >= 80 and percentage <= 90:
            print("you can attend interview in next day")
        else:
            print("you are not eligible")


    elif year <2018:
        print("your passed out year is {}".format(year))
        print("you are not eligible")
    elif year >2022:
        print("your passed out year is {}".format(year))
        print("you are not eligible")
else:
    print("you are not having the qualification")
    print("this is only for the mba.mca,btech students only")