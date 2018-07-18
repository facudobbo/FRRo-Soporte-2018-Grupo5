
camino=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

l=[[False,False,False,False],
   [True,True,True,False],
   [True,True,True,False],
   [False,True,True,False]]



def laberinto(lab, x,y,a,b):
    c = x
    d = y
    fin=False
    camino[x][y]=1

    if ((x+1)<=3) and (camino[x + 1][y] == 0) and (lab[x + 1][y] == False) :
        c=x+1

    elif ((x-1)>=0) and (camino[x-1][y] == 0) and (lab[x-1][y] == False):
        c=x-1
    elif ((y+1)<=3)and (camino[x][y+1] != 1) and (lab[x][y+1] == False):
        d=y+1

    elif ((y-1)>=0) and (camino[x][y-1] == 0) and (lab[x][y-1] == False):
        d = y-1

    else:
        print('Camino sin salida')
        fin=True

    for i in (camino):
        print(i)
    print('\n')

    if (x==a) and (y==b):
        print('SALIO')
    elif fin is not True:
      laberinto(lab,c,d,a,b)



laberinto(l,0,0,3,3)
