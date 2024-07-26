input=list()
with open("input/02.txt", "r") as f:
    for lines in f:
        input.append(lines.rstrip())
def part1():
    m={
        'blue':14,
        'red':12,
        'green':13
    }
    v=0
    game_ids=list()
    for lines in input:
        game=lines.split(":")[0].split(" ")[1]
        draws=lines.split(":")[1].split(";")
        # print(draws)
        f=0
        for i in draws:
            draw=i.split(",")
            for j in draw:
                col=j.split(" ")[2]
                n=j.split(" ")[1]
                # print(n,col)
                # exit()
                if m[col]<int(n):
                    f=1
            if f==1:
                break
        if f==0:
            v+=int(game)
        
    return v


def part2():
    # m={
    #     'blue':14,
    #     'red':12,
    #     'green':13
    # }
    v=0
    game_ids=list()
    for lines in input:
        game=lines.split(":")[0].split(" ")[1]
        # draws=lines.split(":")[1].split(";")
        draws=lines.split(":")[1].replace(";",',')
        # print(draws)
        # f=0
        m={
            "blue":0,
            'red':0,
            'green':0,
        }
        f=1
        draw=draws.split(',')
        # print(draw)
        for j in draw:
                # print(j)
            col=j.split(" ")[2]
            n=j.split(" ")[1]
            # print(n,col)
            # exit()
                # if m[col]<int(n):
                #     f=1
            if int(n)>m[col]:
                m[col]=int(n)
        for i in m.keys():
            # print(m[i])
            f*=m[i]
        v+=f
# v+=int(game)
        
    return v



print(part1())
print(part2())