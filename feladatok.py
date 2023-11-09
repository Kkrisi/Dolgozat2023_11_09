# Kadar Kristof


import math
import random

#[30,1000) --> 30 benne van, 1000 nincs benne
#math.floor(random.random()*(1001-30)+30)



#[-10,20)
#math.floor(random.random()*(21-(-10))+(-10))




# 1.Feladat
# Kérj be 1 páros számot a felhasználótól. (1 pont) Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!
def ParosBekeres():
	szam = int(input("Kérek egy páros számot! "))
	while not szam % 2 == 0:
		if szam % 2 == 0:
			print(szam)
		else:
			szam = int(input("Ez nem páros! PÁROS számot kérek!"))











#2. Feladat
#Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”
def Tizenharom():
	i = 0
	szamlalo = 0
	while i != 13:
		szam = math.floor(random.random()*(151-10)+10)
		print(szam)
		if szam % 3 == 0:
			szamlalo += 1
		i += 1
	print(f"A számok között {szamlalo} db 3-mal osztható van!")




#3. Feladat
#Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot.  Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!” Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor!  pl:  feladat3(„Ez az én dumám”,4) a 4. karakter „z”, nagybetűvé alakítva: Z -  ezt írjuk ki 3-szor A kiírás formátuma: A szöveg 4. karaktere z -  ZZZ
def NKarakter(text,n):
	if len(text) < n:
		print("Nincs N. karakter!")
	else:
		print(f"A {n}. karakter a '{text[n]}'")
		i = 0
		while i != 3:
			print(text[n].upper(),end="")
			i += 1





# 4. Feladat
# Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja. Hány nevet adott meg a felhasználó?  A kiírás formája: „A felhasználó 12 nevet adott meg.”
def Nevek():
	szamlalo = 0
	i = 0
	while i != '@':
		nev = str(input("Kérek egy nevet: "))
		if nev == '@':
			i = '@'
		szamlalo += 1
	print(f"A felhasználó {szamlalo-1} nevet adott meg.")










# 5. Feladat
# Szimuláljuk a kő-papír-olló játékot.  Írj eljárást, amiben: A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban.  Ezután a gép generál egy egész számot [1,3] között.  1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban Ezután írd ki, hogy ki nyert! Ha a két szó ugyanaz, írja ki, hogy Döntetlen.  Egyéb esetben azt írja ki, aki győzött! 
# ++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!
def KoPapirOllo():

	lista = ["semmi","kő","papír","olló"]

	i = 0
	while i != 'siker':
		felhasznalo_tippje = str(input("Kő - 1\nPapír - 2\nOlló - 3\n\nVálassz: "))
		if int(felhasznalo_tippje)<4 and int(felhasznalo_tippje)>0:
			i = 'siker'
			print(f"A felhasználó tippje {lista[int(felhasznalo_tippje)]}")
		else:
			print("Kérlek a Kő - Papír - Olló közül válassz!")


	gep_tippje = math.floor(random.random()*(2-3)+3)
	print(f"A gép tippje {lista[gep_tippje]}")


	if int(felhasznalo_tippje) == gep_tippje:
		print("Döntetlen!")
	elif int(felhasznalo_tippje) > gep_tippje:
		print("A felhasználó nyert, ügyes!")
	else:
		print("A gép nyert, sajnos!")











