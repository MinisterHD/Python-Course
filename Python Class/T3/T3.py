#Rock Paper Scissors : Player VS Pc

ComputerMove="Scissors"
PlayerPoints=0
PCPoints=0
z=int(input("How Many Rounds You Want to Play ? "))
for i in range(z):
    PlayerMove=input("Make your Move : ")
    while (PlayerMove!="Rock") and (PlayerMove!="Paper") and  (PlayerMove!="Scissors") :
        PlayerMove=input("Make your Move again: ")
    if PlayerMove==ComputerMove :
        print("Draw")
    elif (PlayerMove=="Paper") and (ComputerMove=="Rock"):
        print("Player Wins")
        PlayerPoints=PlayerPoints+1
    elif (PlayerMove=="Scissors") or (ComputerMove=="Rock" ):
        print("Pc Wins")
        PCPoints=PCPoints+1
    elif (PlayerMove=="Paper") and (ComputerMove=="Scissors"):
        print("Pc Wins Wins")
        PCPoints=PCPoints+1
    elif (PlayerMove=="Rock") or (ComputerMove=="Scissors" ):
        print("Player Wins")
        PlayerPoints=PlayerPoints+1
    elif (PlayerMove=="Scissors") and (ComputerMove=="Paper"):
        print("Player Wins")
        PlayerPoints=PlayerPoints+1
    elif (PlayerMove=="Rock") or (ComputerMove=="Paper" ):
        print("Pc Wins")
        PCPoints=PCPoints+1
if PlayerPoints>PCPoints:
    print(f"Player Wins the Game {PlayerPoints} vs {PCPoints}")
elif PlayerPoints==PCPoints:
    print(f"The Game is a Draw {PlayerPoints} vs {PCPoints}")
else :
    print(f"PC Wins the Game {PCPoints} vs {PlayerPoints}")