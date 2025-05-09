meme_sozluk= {"LOL":"Komik bir şeye verilen cevap.",
              "CRINGE":"Garip ya da utandırıcı bir şey.",
              "ROFL":"Bir şakaya karşılık cevap.",
              "SHEESH":"Onaylamamak.",
              "CREEPY":"Korkunç.",
              "AGGRO":"Agresifleşmek/sinirlenmek"}
while True:  
    kelime=input("Bilmediğiniz kelimeyi giriniz:").upper()

    if kelime in meme_sozluk:
        print(kelime,"=",meme_sozluk[kelime])
    else:
        print("Maalesef, bu kelime sözlüğümüzde bulunmuyor:(")
#thank you for looking my code :D
