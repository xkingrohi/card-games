#card creation
'''
* * * * *
*{$}    *
*  {j}  *
*    {$}*
* * * * *

'''
card_svalues = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","a"]
card = ""
for i in range(5):
    for j in range(5):
        #(i >= 1 and i <= 3) and (j + 1 == 5)
        if (i > 0 and i < 4) and (j == 4):
            print("      *", end='')
        elif(i >= 1 and i <=3) and (j >= 1 and i < 4):
            continue


        else:
            print("* ", end='')

    print()