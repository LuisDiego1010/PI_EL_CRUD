#______________________________________________________________________________________________________________________#
# ELEMENTOS DE COMPUTACIÓN-I SEMESTRE AÑO 2022
# PROYECTO I-ALMACENAMIENTO DE DATOS DE UN ESTUDIANTE
#                                            Luis Diego García Rojas
#                                               Carné 2020124283
#______________________________________________________________________________________________________________________#
import shelve
archive = "students_base"
loop = True
characters="{}"

"""
Función para crear un nuevo estudiante o un nuevo curso para un estudiante si este ya ha sido creado anteriormente
Contiene 2 diccionarios que almacenan la información temporal de los cursos que se están agregando además de multiples
variables donde se almacena la información que es ingresada por el estudiante
"""
def Create_student():
    with shelve.open(archive, writeback=True) as students: #Abrir el archivo
        courses={}
        coursetemp={}
        carnet=int(input("Ingrese el número de carnet del/la estudiante: "))
        while len(str(carnet))!=10:#Validar que tenga 10 campos
            carnet=int(input("Debe de ser números enteros y 10 dígitos. Ingrese nuevamente el número de carnet:"))
        if str(carnet) in students:#Validar si el carnet está en el archivo
            option=input("El estudiante ya se encuentra agregado, si desea agregar un curso al estudiante digite la tecla s o oprima cualquier otra para continuar: ")    
            if option.lower() == "s":
                course=input("\nIngrese el código del curso: ") 
                while len(str(course))!=6:#Validar que tenga 6 campos
                    course=input("Debe contener 6 campos, digite nuevamente el curso: ")
                if str(course) in (students[str(carnet)]["Cursos"]):
                    print("Este curso ya se encuentra en la información del estudiante, por lo tanto no fue agregado")
                else:
                    students[str(carnet)]["Cursos"][course]=0
                    print("\nEl curso " +str(course) + " fue creado")
        else:    
            add_courses=True
            course=input("\nIngrese el código del curso: ")
            while len(str(course))!=6:#Validar que tenga 6 campos
                course=input("Debe contener 6 campos, digite nuevamente el curso: ")
            coursetemp[course]=0
            courses["Cursos"]=coursetemp
            students[str(carnet)]=courses
            print("\nEl curso " + str(course) + " fue creado")
            while add_courses==True: #Ciclo para agregar cursos hasta que el usuario desee
                answer=input("\n¿Desea agregar mas cursos? Si lo desea oprima la tecla s o no oprima cualquier otra tecla: ")
                #Validar que el curso no exista
                if answer.lower() =="s":
                    course=input("Ingrese el código del curso: ")
                    while len(str(course))!=6:#Validar que tenga 6 campos
                        course=input("Debe contener 6 campos, digite nuevamente el curso: ")#Validar que tenga 6 campos                    
                    coursetemp[course]=0
                    courses["Cursos"]=coursetemp
                    print("\nEl curso " + str(course) + " fue creado")
                else:
                    students[str(carnet)]=courses
                    add_courses=False
                    break;
            #Solicitar los datos del estudiante al usuario
            name=str(input("Ingrese el nombre del/la estudiante: "))
            courses["Nombre"]=name
            direction=input("Ingrese la dirección del/la estudiante: ")
            courses["Dirección"]=direction
            telephone=int(input("Ingrese el teléfono del/la estudiante: "))
            courses["Teléfono"]=telephone
            email=str(input("Ingrese el correo electrónico del/la estudiante: "))
            courses["Email"]=email
            print("\nEl estudiante fue creado")
            students.close()  #Cerrar el archivo

"""
Esta función realiza distintas acciones de lectura según lo que el usuario desee:    
    1. Lee la información de todos lo estudiantes.
    2. Lee la información de un estudiante en particular escribiendo su carnet.
    3. Los cursos de un estudiante en particular digitando su carnet.
"""

def Read():
    with shelve.open(archive, writeback=True) as students: #Abrir el archivo
        #Menú de opciones en Read
        option_r=int(input("Este es el menú de Read, elija una de las siguientes opciones \n1. Leer la información de todos los estudiantes. \n2. Leer la información de un estudiante en particular. \n3. Cursos de un estudiante en particular \n4. Oprima cualquier otra tecla para continuar\n"))
        
        if option_r==1:
            if len(students)>0: #Verifica si hay datos en el archivo
                print("\nLa información de todos los estudiantes es:")
                for i,j in students.items():
                    print("\nEstudiante = ",i,":")
                    for f,z in j.items():
                        print(f,":",z)
            else:
                print("Aún no se han agregado información estudiantes")
            
        elif option_r==2:
            carnet_r= int(input("Ingrese el carnet del estudiante que desea buscar: "))
            if str(carnet_r) in students:
                for i,j in students.items():
                    if i == str(carnet_r):
                        print("La información del estudiante con carnet",i,"es:\n")
                        for f,z in j.items():
                            print(f,":",z)
            else:
                print("\nEl estudiante no fue encontrado")
        
        elif option_r==3:
            carnet_r= int(input("Ingrese el carnet del estudiante que desea buscar: "))
            if str(carnet_r) in students:
                for i,j in students.items():
                    if i == str(carnet_r):
                        print("Los cursos de",i, "son: ")
                        conversion=str(j["Cursos"])
                        for x in range(len(characters)):
                            conversion = conversion.replace(characters[x],"")
                        print(conversion.replace(",","\n"))
            else:
                print("\nEl estudiante no fue encontrado")
    students.close() #Cerrar el archivo

""" 
Esta función realiza distintas acciones de actualización de datos según lo que el usuario desee:    
    1. Actualiza la información de un estudiante (nombre, dirección, teléfono o email).
    2. La nota de un curso para un estudiante.
"""

def Update():
    with shelve.open(archive, writeback=True) as students: #Abrir el archivo
        carnet_u= int(input("Ingrese el carnet del estudiante que desea actualizar: "))
        if str(carnet_u) in students: #Validar que el estudiante se encuentre en el archivo
            #Menú de opciones en Update
            option_u=int(input("Este es el menú de Update, elija una de las siguientes opciones: \n1. Actualizar la información del estudiante. \n2. La nota de un curso de un estudiante.\n"))
            if option_u==1:
                #Menú para actualizar distintos datos
                option_u_2=int(input("¿Que información desea actualizar?. \n1. Nombre \n2. Dirección \n3. Teléfono \n4. Email\n"))
                if option_u_2==1:
                    for i,j in students.items():
                        if i == str(carnet_u):
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_name=input("Por favor digite el nuevo nombre: ")
                            j["Nombre"]=new_name
                            print("La información del nombre del estudiante " + str(carnet_u) + " fue actualizada")

                elif option_u_2==2:
                    for i,j in students.items():
                        if i == str(carnet_u):
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_direction=input("Por favor digite la nueva dirección: ")
                            j["Dirección"]=new_direction
                            print("\nLa información de la dirección del estudiante " + str(carnet_u) + " fue actualizada")
                
                elif option_u_2==3:
                    for i,j in students.items():
                        if i == str(carnet_u):
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_number=input("Por favor digite el nuevo número de teléfono: ")
                            j["Teléfono"]=new_number
                            print("\nLa información del teléfono del estudiante " + str(carnet_u) + " fue actualizada")
                
                elif option_u_2==4:
                    for i,j in students.items():
                        if i == str(carnet_u):
                            print ("El nombre del carnet buscado es: " + j["Nombre"])
                            new_email=input("Por favor digite el nuevo email: ")
                            j["Email"]=new_email
                            print("\nLa información del email del estudiante " + str(carnet_u) + " fue actualizada")
            
            elif option_u==2:
                course_u= str(input("\nIngrese el curso al que desea cambiarle la nota: "))
                if str(course_u) in (students[str(carnet_u)]["Cursos"]):
                    for i,j in students.items():
                        for k,l in j["Cursos"].items():
                            if i==str(carnet_u) and k == str(course_u):
                                new_calification = int(input("Ingrese la nota que desea colocarle al curso: "))
                                j["Cursos"][k] = new_calification
                                print("\nEl curso" + str(course_u) + "del estudiante " + str(carnet_u) + " fue actualizada")
                else:
                    print("\nEl curso " + course_u + " no se encuentra en los cursos de " + str(carnet_u))
        else:
            print("\nEl carnet " + str(carnet_u) + " no se encuentra")
    students.close() #Cerrar el archivo

"""
Esta función realiza distintas acciones de borrado de datos según lo que el usuario desee
    1. Elimine la información de un curso para un estudiante
    2. Elimina a un estudiante completo.
"""
def Delete():
    with shelve.open(archive, writeback=True) as students: #Abrir el archivo
        carnet_d= int(input("Ingrese el carnet del estudiante que desea eliminar o al que desea eliminar un curso: "))
        if str(carnet_d) in students:#Validar que el usuario se encuentre en el archivo
            option_d=int(input("Este es el menú de Delete, elija una de las siguientes opciones: \n1. Eliminar la información de un estudiante. \n2. Eliminar la información para un curso de un estudiante.\n"))
            if option_d==1:
                del students[str(carnet_d)]
                print("La información del estudiante " + str(carnet_d) + " fue eliminada")
            
            elif option_d==2:
                course_d= str(input("\nIngrese el curso que desea eliminar: "))
                if str(course_d) in (students[str(carnet_d)]["Cursos"]): #Validar que el curso esté asociado al usuario buscado
                    del (students[str(carnet_d)]["Cursos"][course_d])
                    print("\nEl curso " + str(course_d) + " del estudiante " + str(carnet_d) + " fue eliminado")
                else:
                    print("\nEl curso " + course_d + " no se encuentra en los cursos de " + str(carnet_d))
        else:
            print("\nEl carnet " + str(carnet_d) + " no se encuentra")
    students.close() #Cerrar el archivo

"""Ciclo para que corra el menú hasta que se seleccione la opción de salir"""
while loop:
    print("\nMenu: \n1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit ")
    option=int(input("\nPor favor ingrese la opción deseada del menú anterior: "))
    
    if option==1:
        Create_student()
    
    if option==2:
        Read()
    
    if option==3:
        Update()
    
    if option==4:       
        Delete()
    
    if option==5:  
        print("\n¡Gracias por usar el programa!")
        loop=False            
        break;

#Fuentes consultadas para la elaboración del proeyecto

# https://docs.python.org/3/library/shelve.html      
"""Documentación de archivos archuivos en python, usada para conocer de lleno a los archivos shelve y su funcionamiento"""

#https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
"""Usada para buscar alternativas a switch en python"""