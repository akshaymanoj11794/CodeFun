# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   50 + 2 * 100 = 250
#  1 1 1 3 1   1000 + 100 = 1100
#  2 4 4 5 4   400 + 50 = 450
# In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.


def score(dice):
    sumscore=0
    dice_dict={1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0}
    print(dice)
    print(dice_dict)
    for index,value in enumerate(dice):
        dice_dict[value]+=1
        extra=1
        if(dice_dict[value]==3):
            if(value==1):
                extra=10
            sumscore+=(value*100*extra)
            dice_dict[value]=0
    sumscore+=dice_dict[1]*100
    sumscore+=dice_dict[5]*50
    print(sumscore)
    return sumscore