# Import the necessary libraries
import cv2
from Functii import dilatarefun
from Functii import eroziunefun
import numpy as np
from PIL import Image
from numpy import asarray
import matplotlib.pyplot as afisare
from google.colab import drive
drive.mount("/content/gdrive", force_remount=True)

#citim imaginea in gray scale
img2 = cv2.imread('/content/gdrive/MyDrive/Proiect_PNI/cal.PNG', 0)
#facem img2 sa fie imagine binara salvata in variabila cal
ret,cal = cv2.threshold(img2, 127, 255, 0)
#generam o matrice goala(plina cu 0) in care ne vom construi scheletul
skel = np.zeros(cal.shape, np.uint8)
#size = np.size(cal) era folosita in alta abordare in functia while
#se genereaza elementul de structura
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) #posibil sa fie cam degeaba avand in vedere ca am lucrat in codul din matrici direct cu elementul +
afisare.figure()
afisare.imshow(element)
#afisare de test pentru dilatare
afisare.figure()
afisare.imshow(cal, cmap='gray')
afisare.suptitle('Imaginea initiala pentru test dilatare')   
#functia de dilatare 
h, w= cal.shape #preluam dimensiunea imaginii
#apel de test pentru dilatare 
dilatare=dilatarefun(cal)
afisare.figure()
#afisare de test pt eroziune
afisare.imshow(dilatare, cmap='gray')
afisare.suptitle('Test functie de dilatare')
afisare.figure()
afisare.imshow(cal, cmap='gray')
afisare.suptitle('Imaginea initiala pentru test eroziune')  
#apel de test pentru eroziune 
eroziunea=eroziunefun(cal) 
afisare.figure()
#afisare de test pt eroziune
afisare.imshow(eroziunea, cmap='gray')
afisare.suptitle('Test functie de eroziune') 
er=asarray(eroziunea)   
print(er.shape) 
print(h,w) 
while True:
    #efectuez operatia de deschidere
    #deschiderea consta intr-o eroziune urmata de o dilatare
    open1=eroziunefun(cal)
    open2=dilatarefun(open1)
    #scadem mereu din imaginea cal imaginea dupa deschidere
    #open3=asarray(open2)
    temp=cal-open2 #temp preia diferenta dintre cal si deschidere
    erodare=eroziunefun(cal) #se efectueaza o noua eroziune care ulterior va lua locul imaginii cal
    temp=temp.astype(np.uint8)
    skel = skel | temp #se construieste treptat scheletul prin sau logic
    cal = erodare.copy() #cal devine cal erodat
    if cv2.countNonZero(cal)==0:
        break
  #executia blocului dureaza aprox 20 de min
ret,skel2 = cv2.threshold(skel, 160, 255, 0)
afisare.figure()
afisare.imshow(skel2,cmap='gray')