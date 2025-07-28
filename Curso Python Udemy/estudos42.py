for i in range(10):
    if i == 2:
        print('O 2 está sendo pulado!')
        continue
    if i == 8:
        print('O else não vai ser executado!')
        break
    for j in range(1,4):
        print(i,j)
else:
    print('O for foi executado completamente.')