
def display_game(game_list):
    print("here is a current list")
    print(game_list)



def positon_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=(input("enter a value (0,1,2):"))

    if choice not in ['0','1','2']:
           print("soryy not in choice")
    return int(choice)
game_list=['0','1','2']
display_game(game_list)
a=positon_choice()
print(a)