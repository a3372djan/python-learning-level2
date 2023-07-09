flag=False
my_players=["d-bee","alok.orion","k","chrono"]
u = input("search: ")
for i in range(0,4):
    if my_players[i]==u :
        flag=True

if flag==True:
    print("found")
else:
    print("not found")






