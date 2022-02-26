class Packet(object):

def MM1(lamda, mu):
   
   print ("ejercicio", "1:")
   print ("en promedio una doctora pasa en promedio 20 minutos con sus pasientes. si el timpo estimado de llegada de cada cliente es de 30minutos")
   print ("determinar los puntos de la A a la F")
   print ("a:", "numero promedio de pacientes en el sistema")
   print ("b:", "tiempo total que consume un paciente en el consultorio")
   print ("c:", "factor de uso en el sistem")
   print ("d:", "numero promedio de pacientes haciendo fila " )
   print ("e:", "probabilidad de que el consultorio este vacio")
   print ("f:", "probabilidad que se encuentren 2 pacieentes en el sistema")
   
   lamda =int(input("introdusca el promedio de pacientes por hora: "))
   mu=int(input("introdusca el promedio de pacientes atendidos por hora: "))
   
   Ls = lamda /(mu-lamda)
   
   Ws = 1 /(mu-lamda)
   
   p = (mu-lamda) * 100
   
   Lq = (lamda * lamda) / mu * (mu - lamda)
   
   po = (1 - 0.66)*100
   p2 = (Ls / 100)
   
    

   print ("a:", "numero promedio de pacientes en el sistema {Ls}")
   print ("b:", "tiempo total que consume un paciente en el consultorio {WS}")
   print ("c:", "factor de uso en el sistem {P}")
   print ("d:", "numero promedio de pacientes haciendo fila {Lq}" )
   print ("e:", "probabilidad de que el consultorio este vacio {Po}")
   print ("f:", "probabilidad que se encuentren 2 pacieentes en el sistema {P2}")
   
   
   