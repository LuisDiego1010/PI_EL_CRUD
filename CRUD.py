students = {34: {'Cursos': {'DFAE': 0, 'dafa': 0}, 'Nombre': 'Diego', 'Dirección': 'fasd', 'Teléfono': 3, 'Email': 'diego'}, 213: {'Cursos': {'CS': 0, 'dafa': 0, 'FSD': 0}, 'Nombre': 'Dani', 'Dirección': 'fsdz', 'Teléfono': 3, 'Email': 'dsa'},29: {'Cursos': {'FDF': 0, 'F3F': 0, 'FRE': 0}, 'Nombre': 'Ana', 'Dirección': 'sa', 'Teléfono': 323, 'Email': 'ana'}}
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
            print("\nEl curso " +str(course) + " fue creado")
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
                print("\nEl curso " + str(course) + " fue creado")
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
        print("\nEl estudiante due creado")

def Read():
    option_r=int(input("Este es el menú de Read, elija una de las siguientes opciones \n1. Leer la información de todos los estudiantes. \n2. Leer la información de un estudiante en particular. \n3. Cursos de un estudiante en particular \n4. Oprima cualquier otra tecla para continuar\n"))
    if option_r==1:
        print("La información de todos los estudiantes es:")
        for i,j in students.items():
            print("\nEstudiante = ",i,":")
            for f,z in j.items():
                print(f,":",z)
    
    if option_r==2:
        carnet_s= int(input("Ingrese el carnet del estudiante que desea buscar: "))
        if carnet_s in students:
            for i,j in students.items():
                if i == carnet_s:
                    print("La información del estudiante con carnet",i,"es:\n")
                    for f,z in j.items():
                        print(f,":",z)
        else:
             print("\nEl estudiante no fue encontrado")
    
    if option_r==3:
        carnet_s= int(input("Ingrese el carnet del estudiante que desea buscar: "))
        if carnet_s in students:
            for i,j in students.items():
                if i == carnet_s:
                    print("Los cursos de",i, "son: ")
                    conversion=str(j["Cursos"])
                    for x in range(len(characters)):
                        conversion = conversion.replace(characters[x],"")
                    print(conversion.replace(",","\n"))
        else:
           print("\nEl estudiante no fue encontrado")

def Update():
    carnet_u= int(input("Ingrese el carnet del estudiante que desea actualizar: "))
    if carnet_u in students:
        option_u=int(input("Este es el menú de Update, elija una de las siguientes opciones: \n1. Actualizar la información del estudiante. \n2. La nota de un curso de un estudiante.\n"))
        if option_u==1:
            option_u_2=int(input("¿Que información desea actualizar?. \n1. Nombre \n2. Dirección \n3. Teléfono \n4. Email\n"))
            if option_u_2==1:
                 for i,j in students.items():
                        if i == carnet_u:
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_name=input("Por favor digite el nuevo nombre: ")
                            j["Nombre"]=new_name
                            print("La información del nombre del estudiante " + str(carnet_u) + " fue actualizada")

            if option_u_2==2:
                 for i,j in students.items():
                        if i == carnet_u:
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_direction=input("Por favor digite la nueva dirección: ")
                            j["Dirección"]=new_direction
                            print("\nLa información de la dirección del estudiante " + str(carnet_u) + " fue actualizada")
            
            if option_u_2==3:
                 for i,j in students.items():
                        if i == carnet_u:
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_number=input("Por favor digite el nuevo número de teléfono: ")
                            j["Teléfono"]=new_number
                            print("\nLa información del teléfono del estudiante " + str(carnet_u) + " fue actualizada")
            
            if option_u_2==4:
                 for i,j in students.items():
                        if i == carnet_u:
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_email=input("Por favor digite el nuevo email: ")
                            j["Email"]=new_email
                            print("\nLa información del email del estudiante " + str(carnet_u) + " fue actualizada")
        
        elif option_u==2:
            course_u= str(input("\nIngrese el curso al que desea cambiarle la nota: "))
            if course_u in (students[carnet_u]["Cursos"]):
                for i,j in students.items():
                    for k,l in j['Cursos'].items():
                        if i==carnet_u and k == course_u:
                            new_calification = int(input("Ingrese la nota que desea colocarle al curso: "))
                            j['Cursos'][k] = new_calification
                            print("\nEl curso" + str(course_u) + "del estudiante " + str(carnet_u) + " fue actualizada")
            else:
                print("\nEl curso " + course_u + " no se encuentra en los cursos de " + str(carnet_u))
    else:
        print("\nEl carnet " + str(carnet_u) + " no se encuentra")


def Delete():
    carnet_d= int(input("Ingrese el carnet del estudiante que desea eliminar o al que desea elminar un curso: "))
    if carnet_d in students:
        option_d=int(input("Este es el menú de Delete, elija una de las siguientes opciones: \n1. Eliminar la información de un estudiante. \n2. Eliminar la información para un curso de un estudiante.\n"))
        if option_d==1:
            del students[carnet_d]
            print("La información del estudiante " + str(carnet_d) + " fue eliminada")
        
        if option_d==2:
            course_d= str(input("\nIngrese el curso que desea eliminar: "))
            if course_d in (students[carnet_d]["Cursos"]):
                del (students[carnet_d]["Cursos"][course_d])
                print("\nEl curso " + str(course_d) + " del estudiante " + str(carnet_d) + " fue eliminado")
            else:
                print("\nEl curso " + course_d + " no se encuentra en los cursos de " + str(carnet_d))



    
    else:
        print("\nEl carnet " + str(carnet_d) + " no se encuentra")

while loop:
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("\nPor favor ingrese la opción deseada del menú anterior: "))
    match option:
        case 1:
            Create_student()
        case 2:
            Read()
        case 3:        
            Update()
        case 4:
           Delete()
        case 5:        
            print("\n¡Gracias por usar el programa!")
            loop=False
            break;    
