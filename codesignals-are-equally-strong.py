"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    my_arms = [yourLeft, yourRight]
    friends_arm = [friendsLeft, friendsRight]

    x = sorted(my_arms)
    y = sorted(friends_arm)

    return True if x == y else False


"""
True
yourLeft: 10
yourRight: 15
friendsLeft: 15
friendsRight: 10

False
yourLeft: 10
yourRight: 15
friendsLeft: 5
friendsRight: 20
"""

print(solution(10, 15, 15, 10))
print(solution(10, 15, 5, 20))
