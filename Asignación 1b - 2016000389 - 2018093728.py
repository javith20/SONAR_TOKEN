#---------------------------Referencias------------------------------------------------------
#https://pyformat.info/#string_pad_align
#https://docs.python.org/3/library/datetime.html

from datetime import date
#R0 ---------------------------------------------------------------------
#mari
def fecha_es_tupla(fecha): #Cambio de nombre
    if(len(fecha) != 3):
        #print('tupla no valida')
        return (bool(0))
    else:
        for i in range(3):
            if (fecha[i]<= 0):
                #print('no todos son enteros positivos')
                return (bool(0))
        if (fecha[1]<=12):
            if (fecha[2]<=32):
                return (bool(1))
        else:
             #print('Mes no valida')
             return (bool(0))

#(15,1,12) = valido     (2000,2,0)=falso

def cal_Dia(fecha):
    formatoMeses = {1:11,2:12,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:9,12:10}
    dia = fecha[2] #Dia del año
    mes = formatoMeses[fecha[1]] #Mes del año, se cuenta desde marzo (Marzo = 1)
    anno = fecha[0]
    if (mes == 12) or (mes == 11): #Se cuentan los ultimos dos meses del año pasado como enero y febrero
        anno -=1 
    PD = anno//100 #Primeros dos digitos del año
    UD = anno%100 #Ultimos dos digitos del año
    
    NumDia = (dia+( (13*mes-1)//5 )+UD+(UD//4)+(PD//4)-2*PD)%7 #Numero correspondiente al día de la semana de esa fecha en particular
    return NumDia

def contador_dia_simple(fecha): 
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    anno = fecha[0]
    dia = fecha[2]
    mes = fecha[1]
    if (mes == 0 and dia == 31):
        fecha = (anno,mes+1,1)
        return fecha
    elif (mes in Dias_31) and (dia == 31):
        if (mes == 12): #Devuelve el año siguiente
            fecha = (anno+1,1,1)
            return fecha
        else:
            fecha = (anno,mes+1,1)
            return fecha
        
    elif (mes in Dias_30) and (dia == 30):
        fecha = (anno,mes+1,1)
        return fecha
            
    elif (bisiesto(anno)) and (mes == 2):
            if (dia == 29):
                fecha = (anno,mes+1,1)
                return fecha
            else:
                fecha = (anno,mes,dia+1)
                return fecha
            
    elif (mes == 2) and (dia == 28):
        fecha = (anno,mes+1,1)#Devuelve el día siguiente en Febrero
        return fecha
    else:
        fecha = (anno,mes,dia+1)
        return fecha

#R1 ---------------------------------------------------------------------
#joshua
def bisiesto(fecha): #Cambio de nombre
    if(fecha >= 1582):
        if(fecha%4 == 0):
            return True
        elif (fecha%100 == 0) and (fecha%400 == 0):
            return True
        else:
            return False

#R2 --------------------     fecha valida G.     ------------------------------
#mari 

def cal_G(dia, mes, anno): #Cambio de nombre
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]

    if(anno==1582):
        if (mes==10 and dia>=15 and dia<=31):
            return (bool(1))
        elif (mes==11 and dia<=30):
            return (bool(1))
        elif (mes==12 and dia<=31):
            return (bool(1))
        else:
            return (bool(0))
        
    elif(mes==2 and dia<=28):
        return (bool(1))
        
    elif (bisiesto(anno)and dia<=29):
        return (bool(1))
        
    elif(mes in Dias_30 and dia<=30):
        #print(dia)
        return (bool(1))
        
    elif(mes in Dias_31 and dia<=31):
        return (bool(1))
        
    else:
        return (bool(0))
    
def fecha_es_valida(fecha):
    if(fecha_es_tupla(fecha)):
        if(fecha[0]>=1582):
            if (cal_G(fecha[2],fecha[1],fecha[0])):
                return (bool(1))
            else:
                return (bool(0))
        else:
            return (bool(0))
    else:
        return (bool(0))
        

#R3 --------------------     dia siguiente       -------------------------------------
#joshua
def dia_siguiente(dia_actual): #Cambio de nombre
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    if (fecha_es_tupla(dia_actual) and fecha_es_valida(dia_actual) and dia_actual[0] > 1582): #Normalización de espacios e identaciones
        esBisiesto = bisiesto(dia_actual[0])
        dia = dia_actual[2]
        mes = dia_actual[1]
        if (mes in Dias_31) and (dia == 31):
            if (mes == 12): #Devuelve el año siguiente
                dia_actual = (dia_actual[0]+1,1,1)
                return dia_actual
            else:
                dia_actual = (dia_actual[0],dia_actual[1]+1,1)
                return dia_actual
        elif (mes in Dias_30) and (dia == 30):
            dia_actual = (dia_actual[0],dia_actual[1]+1,1)
            return dia_actual
    
        elif (esBisiesto) and (mes == 2):
            if (dia == 29):
                dia_actual = (dia_actual[0],dia_actual[1]+1,1)
                return dia_actual
            else:
                dia_actual = (dia_actual[0],dia_actual[1],dia_actual[2]+1)
                return dia_actual
        elif (mes == 2) and (dia == 28):
            dia_actual = (dia_actual[0],dia_actual[1]+1,1)#Devuelve el día siguiente en Febrero
            return dia_actual
        else:
            dia_actual = (dia_actual[0],dia_actual[1],dia_actual[2]+1)
            return dia_actual
    else:
        print("La fecha ingresada no es válida")
            
#R4 --------------------     ordinal             ------------------------------------------
#mari
def ordinal_dia(ordinal): #Cambio de nombre
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    dias = 0
    if(fecha_es_valida(ordinal)):
        for i in range(ordinal[1]):
            if (i ==2):
                if (bisiesto(ordinal[0])):
                    #print("isiesto")
                    dias = dias + 29
                else:
                    dias = dias + 28
            elif (i in Dias_30):
                dias = dias + 30
            elif (i in Dias_31):
                dias = dias + 31
        dias = dias + ordinal[2]
        return (dias)
            
#R5 --------------------     CALENDARIO          ------------------------------------------
#joshua y mari

def Imprimir_3x4(calendario): #Cambio de nombre
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    if calendario <= 1582:
        print("La fecha no es correcta")
    else:
        Meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        Dias = "   D  L  M  M  J  V  S  "
        x = 1
        print("----------------------------------------------------------------------------------------------------")
        print("                                    Calendario      ",calendario)
        while (x < 4):
            #print(' {:^10}{:^10}{:^10}{:^10} '.format("Enero","Febrero","Marzo","Abril"))
            if  x == 1:
                print("----------------------------------------------------------------------------------------------------")
                print(' {:^15}{:^45}{:^5}{:^45} '.format("Enero","Febrero","Marzo","Abril"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,1,1)
                d1= (calendario,1,1)
                d2 = (calendario,2,1)
                d3 = (calendario,3,1)
                d4 = (calendario,4,1)
            elif  x == 2:
                print("                                                                                                    ")
                print(' {:^15}{:^45}{:^5}{:^45} '.format("Mayo","Junio","Julio","Agosto"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,5,1)
                d1= (calendario,5,1)
                d2 = (calendario,6,1)
                d3 = (calendario,7,1)
                d4 = (calendario,8,1)

            else:
                print("                                                                                                    ")
                print(' {:^20}{:^35}{:^5}{:^45} '.format("Septiembre","Octubre","Noviembre","Diciembre"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,9,1)
                d1= (calendario,9,1)
                d2 = (calendario,10,1)
                d3 = (calendario,11,1)
                d4 = (calendario,12,1)

            c = 0
            i=0
            j = 0
            f1=0
            f2=0
            f3=0
            f4=0
            while (i < 24):
                p1 = " "
                p2 = " "
                p3 = " "
                p4 = " "
                p5 = " "
                p6 = " "
                p7 = " "
                if (i == 0 or i == 4 or i == 8 or i == 12 or i == 16 or i == 20):
                    m1 = d1
                    ff = f1
                    if (i > 0):
                        m1 = R3(m1)
                elif (i == 1 or i == 5 or i == 9 or i == 13 or i == 17  or i == 21):
                    m1 = d2
                    ff = f2
                    if (i > 1):
                        m1 = R3(m1)
                elif (i == 2 or i == 6 or i == 10 or i == 14 or i == 18 or i == 22):
                    m1 = d3
                    ff = f3
                    if (i > 2):
                        m1 = R3(m1)
                elif (i == 3 or i == 7 or i == 11 or i == 15 or i == 19 or i == 23):
                    m1 = d4
                    ff = f4
                    if (i > 3):
                        m1 = R3(m1)
                c = cal_Dia(m1)
                if (c == 0 ):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p1 = str(m1[2])
                                
                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p2 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p3 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p4 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p5 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=29 and ff==0):
                                                    if (m1[2]==29):
                                                        ff = 1
                                                    p6 = str(m1[2])

                                                    m1 = R3(m1)
                                                    if (m1[2]<=29 and ff==0):
                                                        if (m1[2]==29):
                                                            ff = 1
                                                        p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p1 = str(m1[2])
                                
                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p2 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p3 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p4 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p5 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=28 and ff==0):
                                                    if (m1[2]==28):
                                                        ff = 1
                                                    p6 = str(m1[2])

                                                    m1 = R3(m1)
                                                    if (m1[2]<=28 and ff==0):
                                                        if (m1[2]==28):
                                                            ff = 1
                                                        p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p1 = str(m1[2])
                            
                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=30 and ff==0):
                                                if (m1[2]==30):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=30 and ff==0):
                                                    if (m1[2]==30):
                                                        ff = 1
                                                    p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p1 = str(m1[2])
                            
                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=31 and ff==0):
                                                if (m1[2]==31):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=31 and ff==0):
                                                    if (m1[2]==31):
                                                        ff = 1
                                                    p7 = str(m1[2])
                elif (c == 1):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=29 and ff==0):
                                                    if (m1[2]==29):
                                                        ff = 1
                                                    p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=28 and ff==0):
                                                    if (m1[2]==28):
                                                        ff = 1
                                                    p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p2 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=30 and ff==0):
                                                if (m1[2]==30):
                                                    ff = 1
                                                p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p2 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=31 and ff==0):
                                                if (m1[2]==31):
                                                    ff = 1
                                                p7 = str(m1[2])

                    
                elif (c == 2):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p3 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p3 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p7 = str(m1[2])
                elif (c == 3):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p4 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p4 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p7 = str(m1[2])
                elif (c == 4):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p5 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p5 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p7 = str(m1[2])
                elif (c == 5):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p6 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p6 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p7 = str(m1[2])
                elif (c == 6):
                    if(m1[1]== 2):
                        if(bisiesto(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p7 = str(m1[2])

                if (j == 0 or j == 4 or j == 8 or j == 12 or i == 16 or i == 20):
                    d1 = m1
                    f1 = ff
##                        print(d1)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 1 or j == 5 or j == 9 or j == 13 or i == 17 or i == 21):
                    d2 = m1
                    f2 = ff
##                        print(d2)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 2 or j == 6 or j == 10 or j == 14 or i == 18 or i == 22):
                    d3 = m1
                    f3 = ff
##                        print(d3)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 3 or j == 7 or j == 11 or j == 15 or i == 19 or i == 23):
                    d4 = m1
                    f4 = ff
##                        print(d4)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7))
                i += 1
                j += 1
            x += 1
        

#-------------------------------    1b           ----------------------------------------------------


#R6 --------------------     dia_semana          ------------------------------------------
#Descripción: Dada una fecha, devuelve un valor númerico que indica el día de la semana al cual corresponde esta fecha
#parametro: Terna que contiene una fecha en el formato (año,mes,dia)
#devuelve: Un número que representa un día de la semana 

def dia_semana(fecha):
    if (fecha_es_tupla(fecha) and fecha_es_valida(fecha) and fecha[0] > 1582 ): #Se agregaron validaciones
        formatoMeses = {1:11,2:12,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:9,12:10} #Valor númerico que toman los meses en este algoritmo
        dia = fecha[2] #Dia del año
        mes = formatoMeses[fecha[1]] #Mes del año, se cuenta desde marzo (Marzo = 1)
        anno = fecha[0]
        if (mes == 12) or (mes == 11): #Se cuentan los ultimos dos meses del año pasado como enero y febrero
            anno -=1 
        PD = anno//100 #Primeros dos digitos del año
        UD = anno%100 #Ultimos dos digitos del año
        
        NumDia = (dia+( (13*mes-1)//5 )+UD+(UD//4)+(PD//4)-2*PD)%7 #Numero correspondiente al día de la semana de esa fecha en particular
        return NumDia
    else:
        print("Fecha no valida")

#R7 --------------------     fecha_futura          ------------------------------------------
#tupla y umero, devolver ua tupla??


def fecha_futura(fecha,num):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    
    if(fecha_es_valida(fecha)):
        if (num < 0):
            print("La numero es negativo")
        elif(num == 0):
            return fecha
        else:
            while num>0:
                dias_mas=0
                if(fecha[1] in Dias_31):
                    dias_mas = 31 -  fecha[2]
                    if (num >= dias_mas):
                        fecha = (fecha[0],fecha[1],fecha[2]+dias_mas)
                        num = num - dias_mas
                    else:
                        fecha = (fecha[0],fecha[1],fecha[2]+num)
                        num = 0

                    if (fecha[2]==31):
                        if(num >0):
                            if (fecha[1]==12):
                                fecha = (fecha[0]+1,1,1)
                            else:
                                fecha = (fecha[0],fecha[1]+1,1)
                            num = num - 1
                            
                elif(fecha[1] in Dias_31):
                    dias_mas = 30 -  fecha[2]
                    if (num >= dias_mas ):
                        fecha = (fecha[0],fecha[1],fecha[2]+dias_mas)
                        num = num - dias_mas
                    else:
                        fecha = (fecha[0],fecha[1],fecha[2]+num)
                        num = 0

                    if (fecha[2]==30):
                        if(num >0):
                            fecha = (fecha[0],fecha[1]+1,1)
                            num = num - 1
                else:
                    if (bisiesto(fecha[0])):
                        dias_mas = 29 -  fecha[2]
                        if (num >= dias_mas ):
                            fecha = (fecha[0],fecha[1],fecha[2]+dias_mas)
                            num = num - dias_mas
                        else:
                            fecha = (fecha[0],fecha[1],fecha[2]+num)
                            num = 0

                        if (fecha[2]==29):
                            if(num >0):
                                fecha = (fecha[0],fecha[1]+1,1)
                                num = num - 1
                    else:
                        dias_mas = 28 -  fecha[2]
                        if (num >= dias_mas ):
                            fecha = (fecha[0],fecha[1],fecha[2]+dias_mas)
                            num = num - dias_mas
                        else:
                            fecha = (fecha[0],fecha[1],fecha[2]+num)
                            num = 0

                        if (fecha[2]==28):
                            if(num >0):
                                fecha = (fecha[0],fecha[1]+1,1)
                                num = num - 1
            return fecha
    else:
        print("La fecha no es valida")
    
#R8 --------------------     dias_entre          ------------------------------------------
#Descripción: Calcula el número de días que hay entre 2 fechas
#Entradas: Dos ternas que contienen cada una, una fecha
#Salidas: El número de días existentes entre las 2 fechas
def dias_entre(fecha1,fecha2):
    if (fecha_es_tupla(fecha1) and fecha_es_tupla(fecha2) and fecha_es_valida(fecha1) and fecha_es_valida(fecha2) and fecha1[0] > 1582 and fecha2[0] > 1582): #Validación con R0 y R2
        if (fecha1 == fecha2):
            return 0
        elif (fecha1[0] == fecha2[0]):
            if (fecha1[1] == fecha2[1]):
                if (fecha1[2] > fecha2[2]):
                    return fecha1[2] - fecha2[2]
                else:
                    return fecha2[2] - fecha1[2]
            else:
                if (fecha1[1] > fecha2[1]):
                    return ordinal_dia(fecha1) - ordinal_dia(fecha2)
                else:
                    return ordinal_dia(fecha2) - ordinal_dia(fecha1)   
        else:
            dias = 0
            if (fecha1[0] > fecha2[0]):
                while (fecha1 > fecha2):
                    fecha2 = dia_siguiente(fecha2)
                    dias += 1
                return dias
            else:
                while (fecha2 > fecha1):
                    fecha1 = dia_siguiente(fecha1)
                    dias += 1
                return dias
    else:
        print("La fecha no es válida")

#R9 --------------------     edad_al          ------------------------------------------
#lista que tiene 2 tuplas
#return (años que tiene, meses,dias)
#validar con R0
def edad_al(fecha_na,fecha_actual):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    tiempo=(0,1,0)
    
    if(fecha_es_valida(fecha_na)):
        if (fecha_es_valida(fecha_actual)):
            if (fecha_na[0]==fecha_actual[0] and fecha_na[1]>=fecha_actual[1] and fecha_na[2]>fecha_actual[2]):
                print("La fecha de nacimiento es mas reciente que la fecha actual dada")
            else:
                while(fecha_na != fecha_actual):
                    esBisiesto = bisiesto(fecha_na[0])
                    anno = fecha_na[0]
                    mes = fecha_na[1]
                    dia = fecha_na[2]
                    if (mes in Dias_31) and (dia == 31):
                        if (mes == 12): #Devuelve el año siguiente
                            fecha_na = (anno+1,1,1)
                            tiempo = contador_dia_simple(tiempo)
                        else:
                            fecha_na = (anno,mes+1,1)
                            tiempo = contador_dia_simple(tiempo)
                    elif (mes in Dias_30) and (dia == 30):
                        fecha_na = (anno,mes+1,1)
                        tiempo = contador_dia_simple(tiempo)
                    elif (mes == 2) and (esBisiesto==bool(1)) and (dia == 29):
                        if (dia == 29):
                            fecha_na = (anno,mes+1,1)               # Devuelve el día siguiente en Febrero bisiesto
                            tiempo = contador_dia_simple(tiempo)
                        if (dia == 28):
                            fecha_na = (anno,mes,dia + 1)           # Devuelve el día 29 Febrero
                            tiempo = contador_dia_simple(tiempo)
                    elif (mes == 2) and (esBisiesto==bool(0)) and (dia == 28):
                        fecha_na = (anno,mes+1,1)#Devuelve el día siguiente en Febrero
                        tiempo = contador_dia_simple(tiempo)
                    else:
                        fecha_na = (anno,mes,dia+1)
                        tiempo = contador_dia_simple(tiempo)
                tiempo = (tiempo[0],tiempo[1]-1,tiempo[2])
                return tiempo
        else:
            print("La fecha actual dada no es válida")
    else:
        print("La fecha nacimiento dada no es válida")  
        
    
#R10 --------------------     fecha_hoy          ------------------------------------------
#Descripción: Llamar a esta función devuelve la fecha de hoy, obtenida a partir de la función today(), pero con el formato (año,mes,dia)
#Entradas: Ningunas
#Salidas: Una terna con la fecha de hoy, en formato (año,mes,dia)
def fecha_hoy():
    fecha_sin_formatear = str(date.today()) # Obtiene la fecha de hoy
    anno = int(fecha_sin_formatear[0:4])
    mes = int(fecha_sin_formatear[5:7])
    dia = int(fecha_sin_formatear[8:10])
    fecha_formateada = (anno,mes,dia)
    if (fecha_es_tupla(fecha_formateada) and fecha_es_valida(fecha_formateada) and fecha_formateada[0] > 1582 ):
        return fecha_formateada
    else:
        print("La fecha no es correcta")

#R11 --------------------     edad_hoy          ------------------------------------------
def edad_hoy(fecha_na):
    tiempo=(0,0,0)
    
    if(fecha_es_valida(fecha_na)):
        fecha_actual = fecha_hoy()
        tiempo = edad_al(fecha_na,fecha_actual)
        return tiempo 
    else:
        print("La fecha nacimiento dada no es válida")

#---------------------------Pruebas-------------------------------------
#R6
##dia_semana((2022,4,7))
##dia_semana((2022,4,8))
##dia_semana((1223,4,7))
##dia_semana((123144,24,4))
#R7
##fecha_futura((2022,2,7),2)
##fecha_futura((2022,2,28),2)
##fecha_futura((2022,2,28),0)
##fecha_futura((2022,2,29),0)
##fecha_futura((2022,2,29),1)
##fecha_futura((2016,2,29),1)
##fecha_futura((2016,13,2),1)
##fecha_futura((1333,13,2),1)
##fecha_futura((1993,12,31),1)
##fecha_futura((1993,12,31),20)
##fecha_futura((1993,12,31),365)
##fecha_futura((1993,12,31),-365)
#R8
##dias_entre((2022,4,7),(2022,4,6))
##dias_entre((2022,4,6),(2022,4,7))
##dias_entre((2022,4,7),(2022,4,7))
##dias_entre((2022,5,7),(2022,4,6))
##dias_entre((2022,4,7),(2022,5,6))
##dias_entre((2023,4,7),(2022,4,6))
##dias_entre((2022,4,7),(2023,4,6))
##dias_entre((2022,4,7),(2022,4,6))
##dias_entre((1333,4,7),(2022,4,6))
##dias_entre((1583,4,7),(2022,4,6))
##dias_entre((2022,4,7),(2022,53,6))
##dias_entre((2022,64,7),(2022,4,6))
##dias_entre((2022,4,7),(2022,4,51))
##dias_entre((2022,4,91),(2022,4,6))
#R9

#R10
#fecha_hoy()
