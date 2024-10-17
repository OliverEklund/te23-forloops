inventory = ["vattenflaska", "Pizzalåda", "scud missil", "poker chip"]
print("Välkommen till the Inventory, där du sparar vad du vill")
run = True
while run:
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till sak\n[3] Avsluta\n Vad blir det?: ")

    if choice == "1":
        print("skriv ut")
        for item in inventory:
            print(item)
    elif choice == "2":
        item = input("Lägg till en ny sak: ")
        inventory.append(item)
    elif choice == "3":
        run = False