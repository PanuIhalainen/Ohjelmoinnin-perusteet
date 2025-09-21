
print("Calculate the area of a wall")
Feed = input("Enter the widht in meters: ")    
Feed = Feed.replace(",", ".")        
Feed_float = float(Feed)          
Widht = int(round(Feed_float))   

Feed = input("Enter the heigt in meters: ")
Feed = Feed.replace(",", ".")
Feed_float = float(Feed)
Height = int(round(Feed_float))
print(f"Widht is {Widht} m and height is {Height} m.")      
Area = Widht * Height               
print(f"The wall will be {Area} square meters.")

