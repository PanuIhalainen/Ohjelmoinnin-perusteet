# Tee Python-ohjelma, joka voi ottaa käyttäjän syötteitä ja muuntaa ne kokonaisluvuiksi.

# 1.Tulosta " Calculate the area of a wall."
print("Calculate the area of a wall.")
# 2.Kehota käyttäjää
#" Enter the width in meters: "
Feed = input("Enter the width in meters: ")     #Tallennetaan feed
# 3.Tallenna syötearvo Feedmuuttujaan.
# 4.Muunna Feedmuuttuja kokonaisluvuksi ja tallenna se Widthmuuttujaan
Feed = Feed.replace(",", ".")     # korvaa pilkun pisteeksi      
Feed_float = float(Feed)           # muutetaan liukuluvuksi
Widht = int(round(Feed_float))     # pyöristetään ja muutetaan kokonaisluvuksi

# 5.Kehota käyttäjää
#" Enter the height in meters: "
Feed = input("Enter the height in meters: ")
# 6.tallenna syötearvo Feedmuuttujaan.
# 7.Muunna Feedmuuttuja kokonaisluvuksi ja tallenna se Heightmuuttujaan
Feed = Feed.replace(",", ".")
Feed_float = float(Feed)
Height = int(round(Feed_float))
# 8.Tulosta " Width is {Width} m and height is {Height} m."
print(f"Widht is {Widht} m and height is {Height} m.")      # f kertoo että merkkijonossa voi olla muuttujia tai laskutoimituksia
# 9.Kerro Widthja Height, ja tallenna tulos sitten Areamuuttujaan
Area = Widht * Height               # tehdään area muuttuja kertolaskulla
# 10. Näytä tulokset käyttäjälle: “ The wall will be {Area} square meters.”
print(f"The wall will be {Area} square meters.")




