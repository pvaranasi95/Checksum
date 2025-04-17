# # i =1
# # while i<=50:
# #     print('$' * i)
# #     i = i+1
# # print("Done")

# secret=9
# count=0
# while count<3:
#     guess=int(input("Guess: "))
#     count+=1
#     if guess==secret:
#         print("You won!")
#         break
# else:
#     print("You lost!")

command=""
while command!=("quit"):
    command=input("> ").lower()
    if command=="start":
        print("Car started")
    elif command== "stop":
        print("car Stopped")
    elif command=="help":
        print("""
              Enter 
              start : To start the car
              stop : To stop the car
              quit : To quit the car""")
    else:
         print("Please enter help to get more details")

