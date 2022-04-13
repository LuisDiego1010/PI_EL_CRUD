loop = True
while loop:  
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("Por favor ingrese deseada del menú anterior:"))
    match option:
        case 1:
            print("\n Create")
        case 2:
           print("\n Read")
        case 3:        
            print("\n Update")
        case 4:
           print("\n Delete")
        case 5:        
            print("\n Gracias por usar el programa")
            loop=False
            break;
