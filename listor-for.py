Item_equipped = "inget"
inventory = ["vattenflaska", "Pizzalåda", "scud missil", "poker chip"]
print("Välkommen till the Inventory, där du sparar vad du vill")
run = True
while run:
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till sak\n[3] Ta bort sak\n[4] Rensa\n[5] Välja en sak\n[6] Avsluta\n Vad blir det?: ")

    if choice == "1":
        print("Inventoriet innehåller")
        for item in inventory:
            print(item)
            print(f"Vapen i handen: {Item_equipped}")
        
    elif choice == "2":
        item = input("Lägg till en ny sak: ")
        inventory.append(item)
    
    elif choice == "3":
        item_remove = input("Välj föremål att ta bort: ")
        inventory.remove(item_remove)
    
    elif choice == "4":
        inventory = [""]

    elif choice == "5":
        print("Inventoriet innehåller")
        for item in inventory:
            print(item)
        print(f"Vapen i handen: {Item_equipped}")
        print("Vilket vill du välja?")
        Item_equipped = input("V")
    
    elif choice == "6":
        run = False