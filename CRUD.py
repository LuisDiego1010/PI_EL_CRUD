estudiantes = {}
loop = True

def Create():
    carne=input("Ingrese el número de carnet del estudiante")
    add_courses=True
    cursos={}
    course=input("Ingrese el nombre del curso")
    cursos[course]=0
    while add_courses==True:
        answer=input("¿Desea agregar mas cursos?\n")
        if answer.lower() =="si" or answer.lower()=="sí" or answer.lower()=="yes":
            course=input("Ingrese el nombre del curso")
            cursos[course]=0
        else:
            print(cursos)
            add_courses=False

while loop:  
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("Por favor ingrese deseada del menú anterior:"))
    match option:
        case 1:
            Create()
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



    