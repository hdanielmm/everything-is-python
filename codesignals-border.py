def solution(picture):
    new_picture = []
    size = len(picture[0]) + 2
    stars = [size*"*"]
    for p in picture:
        p = "*" + p + "*"
        new_picture.append(p)
    return stars + new_picture + stars


print(solution(["abc", "ded"]))
print(solution(["a"]))
