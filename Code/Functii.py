def dilatarefun(calp):
  # i si j iau valori de la 1 pt a evita cazurile particulare
  i=0
  j=0
  n=h
  m=w
  p=1 #de cate ori sa se repete dilatarea facuta in partea de test a functiei si nu am mai scos-o ca sa nu
      #ne mai chinuim cu intendarea.
  cal2=asarray(calp) #luam cal2 ca fiind un array
  dilatare=np.zeros((n,m)) #construim o matrice plina cu 0 in care sa ne facem dilatarea
  while p!=0:
    for i in range(n-1):
      for j in range(m-1): #pct central din el structural se face alb daca exista cel putin un pixel alb acoperit de elementul structural
       if cal2[i-1][j]==255 or cal2[i+1][j]==255 or cal2[i][j+1]==255 or cal2[i][j-1]==255:
       #if cal2[i-1][j]==255 or cal2[i-1][j-1]==255 or cal2[i-1][j+1]==255 or cal2[i+1][j]==255 or cal2[i+1][j-1]==255 or cal2[i+1][j+1]==255 or cal2[i][j+1]==255 or cal2[i][j-1]==255:
         dilatare[i][j]=255
       else:
         dilatare[i][j]=0
    p=p-1
    dilatare1=Image.fromarray(dilatare) #construim imaginea dilatata
    cal2=asarray(dilatare1) #o redam ca parametru in cazul in care pasul p al dilatarii este !=1 adica facem dilatarea de mai multe ori
  return(cal2)

def eroziunefun(calp):
  i=0
  j=0
  n=h
  m=w
  p=1 #de cate ori sa se repete dilatarea facuta in partea de test a functiei si nu am mai scos-o ca sa nu
      #ne mai chinuim cu intendarea.
  cal3=asarray(calp) #luam cal3 ca fiind un array
  eroziune=np.zeros((n,m)) #construim o matrice plina cu 0 in care sa ne facem eroziunea
  while p!=0:
    for i in range(n-1):
      for j in range(m-1):
        #daca originea elementului structural se suprapune peste un pixel "obiect"
        if cal3[i][j]==255:
          if cal3[i-1][j]==255 and cal3[i+1][j]==255 and cal3[i][j+1]==255 and cal3[i][j-1]==255:
          #if cal3[i-1][j]==255 and cal3[i-1][j-1]==255 and cal3[i-1][j+1]==255 and cal3[i+1][j]==255 and cal3[i+1][j-1]==255 and cal3[i+1][j+1]==255 and cal3[i][j+1]==255 and cal3[i][j-1]==255:
            eroziune[i][j]=255 #pixelul ramane alb daca toti pixeli care sunt acoperiti de elementul structural sunt albi
          else:
            eroziune[i][j]=0 #daca cel putin unul este negru => pixelul este copiat ca fiind negru
    p=p-1
    eroziune1=Image.fromarray(eroziune) #construim imaginea erodata
    cal3=asarray(eroziune1) #o retrimitem catre urmatorul loop de erodare in caz ca p!=1
  return(cal3)