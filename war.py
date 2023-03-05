import random as r
import os
from time import sleep
#card format
'''
* * *
*   *
* * *
'''
##########
card_values = [2,3,4,5,6,7,8,9,0,"J","Q","K","a"]
##########
#clubs
cardc_values = {
    "2c":"",
    "3c":"",
    "4c":"",
    "5c":"",
    "6c":"",
    "7c":"",
    "8c":"",
    "9c":"",
    "0c":"",
    "Jc":"",
    "Qc":"",
    "Kc":"",
    "ac":""
}
#hearts
cardh_values = {
    "2h": "",
    "3h": "",
    "4h": "",
    "5h": "",
    "6h": "",
    "7h": "",
    "8h": "",
    "9h": "",
    "0h": "",
    "Jh": "",
    "Qh": "",
    "Kh": "",
    "ah": ""
}
#diamonds
cardd_values = {
    "2d": "",
    "3d": "",
    "4d": "",
    "5d": "",
    "6d": "",
    "7d": "",
    "8d": "",
    "9d": "",
    "0d": "",
    "Jd": "",
    "Qd": "",
    "Kd": "",
    "ad": ""
}
#spades
cards_values = {
    "2s": "",
    "3s": "",
    "4s": "",
    "5s": "",
    "6s": "",
    "7s": "",
    "8s": "",
    "9s": "",
    "0s": "",
    "Js": "",
    "Qs": "",
    "Ks": "",
    "as": ""
}
#creates cards -> the suits (diamonds, spades, clubs, hearts)
def cardCreate(suit, cardDict):
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 0, "J", "Q", "K", "a"]
    card = ''''''
    z = 0
    x = 0
    while z < len(card_values):
        for i in range(3):
            for j in range(3):
                if (i > 0 and i < 2) and (j == 2):
                    card += f"{card_values[z]} {suit}"
                elif (i >= 1 and i <= 2) and (j >= 1 and i < 2):
                    continue
                else:
                    card += f"{suit} "

            if (i != 2):
                card += "\n"
        card_values[z] = card
        card = ''''''
        z += 1

    for keys in cardDict:
        cardDict[keys] = card_values[x]
        x += 1
    return cardDict

##########
#fucntion called to create the suits
cardc_values = cardCreate("*",cardc_values)
cardh_values = cardCreate("@",cardh_values)
cardd_values = cardCreate("^",cardd_values)
cards_values = cardCreate("$",cards_values)
##########
def dealCards(all_c,player,comp,f,c_v):
    for i in all_c:
        l = list(i)
        for j in range(len(c_v) - f):
            rnd = r.choice(l)
            player.append(rnd)
            l.remove(rnd)
        for k in l:
            comp.append(k)
        if f % 2 == 0:
            f += 1
        else:
            f -= 1


##########
#vars
p_c = []
c_c = []
all_cards = [cards_values,cardh_values,cardc_values,cardd_values]
f = 6
##########
def place_Card(v,cards_values,cardh_values,cardc_values,cardd_values):
    if v[1] == 's':
        print(cards_values[v])
    elif v[1] == 'd':
        print(cardd_values[v])
    elif v[1] == 'c':
        print(cardc_values[v])
    elif v[1] == 'h':
        print(cardh_values[v])

##########
def checkCard(v,cards_values,cardh_values,cardc_values,cardd_values):
    list_s = list(cards_values)
    list_h = list(cardh_values)
    list_c = list(cardc_values)
    list_d = list(cardd_values)
    if v[1] == 's':
        return list_s.index(v)
    elif v[1] == 'h':
        return list_h.index(v)
    elif v[1] == 'c':
        return list_c.index(v)
    elif v[1] == 'd':
        return list_d.index(v)
##########
def play_Game(pc,cc,cards_values,cardh_values,cardc_values,cardd_values):
    os.system('cls')
    pc = set(pc)
    pc = list(pc)
    cc = set(cc)
    cc = list(cc)
    print("\n")
    while len(pc) != 52 or len(cc) != 52:
        os.system('cls')
        for i in range(3):
            print(f"Placing card in {i+1}")
            sleep(1)
        for i in range(1):
            value1 = pc[i]
            value2 = cc[i]
            print("\nyou:")
            place_Card(value1,cards_values, cardh_values, cardc_values, cardd_values)
            print("-----")
            print("comp:")
            place_Card(value2, cards_values, cardh_values, cardc_values, cardd_values)
            check1 = checkCard(value1,cards_values,cardh_values,cardc_values,cardd_values)
            check2 = checkCard(value2,cards_values,cardh_values,cardc_values,cardd_values)
            if(check1 > check2):
                print("\nYou have the higher card! You take the comp's card!")
                x = value1
                pc.remove(value1)
                pc.append(x)
                pc.append(value2)
                cc.remove(value2)
            elif(check1 < check2):
                print("\nThe comp has the higher card! The comp takes your card!")
                y = value2
                cc.remove(value2)
                cc.append(y)
                cc.append(value1)
                pc.remove(value1)
            elif(check1 == check2):
                print("No change")
        print("You now have " + str(len(pc)) + " card(s)\n")
        cont = input("Continue?: ")
        if(cont == 'y'):
            pass
        else:
            print("Bye!\n")
            break
    if(len(pc) == 52):
        print("You win!")
    elif(len(cc) == 52):
        print("Comp win!")





##########
def instructions():
    os.system('cls')
    print("Welcome to the long and grueling game of war!\n")
    print("The objective is to obtain all the cards in your hand")
    print("To do so, your card must be higher than the comp's card so you can take it ; if not, the comp will "
          "take your card and will be one step closer to winning")
    print("\nbtw the 0 is a 10 (i put it like that cuz formating stuff) and 'a' is ace")
    print("press 'b' to go back")
    x  = input("")
    if x == 'b':
        os.system('cls')
        return 1
def Start():
    os.system('cls')
    start = input("Do you want to play? (i for instructions): ")
    if start == 'y':
        dealCards(all_cards,p_c,c_c,f,card_values)
        play_Game(p_c,c_c,cards_values,cardh_values,cardc_values,cardd_values)
    elif start == 'i':
        instructions()
        Start()
    else:
        print("im guessing thats a no, bye!")

Start()








