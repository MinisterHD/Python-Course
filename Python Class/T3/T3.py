#Rock Paper Scissors : Player VS Pc

ComputerMove="Rock"
PlayerPoints=0
PCPoints=0
z=int(input("How Many Rounds You Want to Play ? "))
for i in range(z):
    PlayerMove=input("Make your Move : ")
#    while PlayerMove not in ["Rock","rock","Paper","paper","Scissors","scissors"]:
#        print("Invalid Value")
#        PlayerMove=input("Make your Move Again : ")
    if (PlayerMove=="Rock") or (PlayerMove=="rock") :
        print("Draw")
    elif PlayerMove=="Paper" or (PlayerMove=="paper"):
        print("Player Wins")
        PlayerPoints=PlayerPoints+1
    elif (PlayerMove=="Scissors") or (PlayerMove=="scissors" ):
        print("Pc Wins")
        PCPoints=PCPoints+1
    else:
        print("Invalid Value")
if PlayerPoints>PCPoints:
    print(f"Player Wins the Game {PlayerPoints} vs {PCPoints}")
elif PlayerPoints==PCPoints:
    print(f"The Game is a Draw {PlayerPoints} vs {PCPoints}")
else :
    print(f"PC Wins the Game {PCPoints} vs {PlayerPoints}")