cat_list = []
for i in range(15):
    cat_list.append(list(map(str, input().split())))

for i in range(15):    
    for j in range(15):
        if cat_list[i][j] == 'w':
            exit(print('chunbae'))
        elif cat_list[i][j] == 'b':
            exit(print('nabi'))
        elif cat_list[i][j] == 'g':
            exit(print('yeongcheol'))