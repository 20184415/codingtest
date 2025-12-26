sound = input()
str_="quack"
lst_duck=[]
index = 0
for char in sound:
    found = False
    if char not in str_:
        print(-1)
        exit()

    cur_index = str_.index(char)
    for i in range(lst_duck):
        if lst_duck[i] == cur_index:
            if lst_duck[i]==4:
                lst_duck[i]=0
            else:
                lst_duck[i]+=1

            found = True
            break
    if not found:
        if cur_index==0:
            lst_duck.append(1)
        else:
            print(-1)
            exit()