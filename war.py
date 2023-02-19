import random as r
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
#assigns comp & player random cards (26 for each cuz only one deck of 52 cards)
dealCards(all_cards,p_c,c_c,f,card_values)
#########
print(p_c)
print(c_c)








