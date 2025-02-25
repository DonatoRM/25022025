# definir la función principal del programa
def vida_util_software():
    # mensaje al usuario de bienvenida
    print(f"Bienvenido al asistente de vida util del software")
    # explicamos el propósito del programa
    print("Este programa te ayudará a estimar la vida util del un software basada en varios factores")

    ''' preguntas al usuario para evaluar los factores que influyen en la vida util del software y
    y convierte la respuesta en minúsculas
    '''
    # soporte técnico
    soporte_tecnico=input("¿El software sigue recibiendo soporte técnico? (si/no): ").lower

    # actualizaciones
    actualizaciones=input("¿El software sigue cometiendo errores? (sí/no): ").lower
    # compatibilidad
    compatibilidad=input("¿el software es compatible con los sistemas operativos actuales (sí/no): ").lower

    # demanda
    demanda=input("¿El software sigue siendo demandado por los usuarios? (sí/no): ").lower

    # evaluar las respuestas del usuario
    # iniciamos la variable que almacena el puntaje de vida util
    vida_util=0

    ''' si el software recibe soporte técnico se suma 2 al porcentaje;
    de lo contrario se resta 1
    '''

    if soporte_tecnico=="sí":
        vida_util+=2
    else:
        vida_util-=1

    ''' 
    Si el software recibe compatibilidad, se suma 2 al puntaje,
    de lo contrario se resta 1
    '''

    if compatibilidad=="sí":
        vida_util+=2
    else:
        vida_util-=1
    ''' 
    Si el software recibe actualizaciones, se suma 2 al puntaje,
    de lo contrario se resta 1
    '''

    if compatibilidad=='sí':
        vida_util+=2
    else:
        vida_util-=1

    ''' 
    Si el software recibe demandas, se suma 2 al puntaje,
    de lo contrario se resta 1
    '''

    if demanda=='sí':
        vida_util+=2
    else:
        vida_util-=1

# resultado de la vida util del software
# si el puntaje es 5 o mayor se considera que el software tiene de vida util larga
    if vida_util>=5:
        print("El software tiene una vida util larga. Es probable que siga siendo util por varios años más")
    # si es puntaje es 3 o 4, se considera que tiene una vida util moderada
    elif vida_util>=3:
        print("El software tiene una vida util moderada. Es posible que siga siendo util por algún tiempo más")
    # el puntaje es menor que 3
    else:
        print("El software tiene una vida util corta. Es probable que deje de ser util en un futuro.")
# nombre del módulo en ejecución
if __name__=="__main__":
    vida_util_software()
