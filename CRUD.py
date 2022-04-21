students = {}
loop = True
def Create_student():
    courses={}
    course2={}
    carnet=int(input("Ingrese el número de carnet del/la estudiante: ")) #Validar que sean números y que tenga solo 10 dígitos
    if carnet in students:
        option=input("El estudiante ya se encuentra agregado, si desea agregar un curso al estudiante digite la tecla s o oprima cualquier otra para continuar")    
        if option == "s":
            course=input("\nIngrese el código del curso: ") #Validar que tenga 6 campos
            course2[course]=0
    else:    
        add_courses=True
        course=input("\nIngrese el código del curso: ") #Validar que tenga 6 campos
        course2[course]=0
        while add_courses==True:
            answer=input("\n¿Desea agregar mas cursos? ")
            #Validar que el curso no exista
            if answer.lower() =="si" or answer.lower()=="sí" or answer.lower()=="yes":
                course=input("Ingrese el código del curso o oprima cualquier tecla para continuar...: ")
                course2[course]=0
                courses["Cursos"]=course2
            else:
                students[carnet]=courses
                add_courses=False
                break;
        name=str(input("Ingrese el nombre del/la estudiante: "))
        courses["Nombre"]=name
        direction=input("Ingrese la dirección del/la estudiante: ")
        courses["Dirección"]=direction
        telephone=int(input("Ingrese el teléfono del/la estudiante: "))
        courses["Teléfono"]=telephone
        email=str(input("Ingrese el correo electrónico del/la estudiante: "))
        courses["Email"]=email
        print(students)


while loop:  
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("\nPor favor ingrese la opción deseada del menú anterior: "))
    match option:
        case 1:
            Create_student()
        case 2:
           print("\n Read")
        case 3:        
            print("\n Update")
        case 4:
           print("\n Delete")
        case 5:        
            print("\n¡Gracias por usar el programa!")
            loop=False
            break;    
