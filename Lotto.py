import random

def lottoziehung():

    verfuegbare_zahlen = list(range(1, 46))
    gezogene_zahlen = []
    # Führe 6 Ziehungen durch
    for _ in range(6):
        # Ziehe Zufallszahl 
        gezogene_zahl = random.choice(verfuegbare_zahlen)
        
        gezogene_zahlen.append(gezogene_zahl)
        verfuegbare_zahlen.remove(gezogene_zahl)

    print("Ziehungen von LottoEgger am Donnerstag:", gezogene_zahlen)

lottoziehung()