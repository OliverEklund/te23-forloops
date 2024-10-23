inventory = ["vattenflaska", "Pizzalåda", "scud missil", "poker chip"]
print("Välkommen till the Inventory, där du sparar vad du vill")
run = True
while run:
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till sak\n[3] Ta bort sak\n[4] Rensa\n[5] Avsluta\n Vad blir det?: ")

    if choice == "1":
        print("Inventoriet innehåller")
        for item in inventory:
            print(item)
        
    elif choice == "2":
        item = input("Lägg till en ny sak: ")
        inventory.append(item)
    
    elif choice == "3":
        item_remove = input("Remove Item: ")
        inventory.remove(item_remove)
    
    elif choice == "4":
        inventory = [""]

    elif choice == "5":
        run = False