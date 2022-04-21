students = {34: {'Cursos': {'DFAE': 0, 'dafa': 0}, 'Nombre': 'Diego', 'Dirección': 'fasd', 'Teléfono': 3, 'Email': 'dsa'}, 213: {'Cursos': {'CS': 0, 'DF': 0, 'FSD': 0}, 'Nombre': 'Dani', 'Dirección': 'fsdz', 'Teléfono': 3, 'Email': 'dsa'},29: {'Cursos': {'FDF': 0, 'F3F': 0, 'FRE': 0}, 'Nombre': 'Ana', 'Dirección': 'sa', 'Teléfono': 323, 'Email': 'ana'}}
loop = True
characters="{}"
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

def Read():
    option_r=int(input("Este es el menú de Read estas son las opciones \n1. Leer la información de todos los estudiantes. \n2. Leer la información de un estudiante en particular. \n3. Cursos de un estudiante en particular \n4. Oprima cualquier otra tecla para continuar\n"))
    if option_r==1:
        print("La información de todos los estudiantes es:")
        for i,j in students.items():
            print("\nEstudiante = ",i,":")
            for f,z in j.items():
                print(f,":",z)
    
    if option_r==2:
        carnet_s= int(input("Ingrese el carnet del estudiante que desea buscar: "))
        for i,j in students.items():
            if i == carnet_s:
                print("La información del estudiante con carnet",i,"es:\n")
                for f,z in j.items():
                    print(f,":",z)
    
    if option_r==3:
        carnet_s= int(input("Ingrese el carnet del estudiante que desea buscar: "))
        for i,j in students.items():
            if i == carnet_s:
                print("Los cursos de",i, "son: ")
                conversion=str(j["Cursos"])
                for x in range(len(characters)):
                    conversion = conversion.replace(characters[x],"")
                print(conversion.join(","))





while loop:  
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("\nPor favor ingrese la opción deseada del menú anterior: "))
    match option:
        case 1:
            Create_student()
        case 2:
            Read()
        case 3:        
            print("\n Update")
        case 4:
           print("\n Delete")
        case 5:        
            print("\n¡Gracias por usar el programa!")
            loop=False
            break;    
