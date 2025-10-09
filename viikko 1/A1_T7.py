
print("Calculate fuel consumtion.")         # Otsikon tulostus

Feed = input("Enter travel distance(kilometers): ")     # Kysytään matkustettu matka ja tallennetaa feed:iin

Distance =  int(float(Feed))                           # tallennetaan se Distance alle kokonaislukuna

Feed = input("Enter fuel usage(liters): ")          # Kysytään käytetyn molttoaineen määrä

FuelUsage = int(float(Feed))                              # Tallennetaan se FuelUsage alle kokonaislukuna

Consumption = int((FuelUsage / Distance) * 100)         # Lasketaan kulutus per 100 km

print(f"Fuel consumption is {Consumption} l per 100 km")        # Tulostetaan kulutus

