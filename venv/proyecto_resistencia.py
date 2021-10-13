#parametrizacion curva caracteristica del motor
def factor(x):
    y = -221.71*(x**2)+(398.62*x)-176.9
    return y

#datos iniciales conocidos del motor y el diseño
torque_n= 1436.48
#este factor de seguridad hace referencia a la seccion de diametro d3 del eje
FS=3.8
pi=3.14159265
G=11500000
relacion_engranajes = 44/8
relacion_d2_d1 = 1.1
relacion_d3_d2 = 1.2
relacion_r1_d2 = 0.19
relacion_r2_d1 = 0.03
print("bienvenido ingrese la velocidad asincronica \nen la que va a utilizar el motor Siemens NEMA B FRAME 324T")
opc = int(input("1=porcentaje/100 entre 0.9 y 1\n2=rpm entre 1620 y 1800\n"))
f = 0
flag = True
if opc == 1:
    while flag:
        f = float(input("porcentaje/100 = "))
        if f>1 or f<0.9:
            print("valor fuera de los limites vuelva a intentar")
        else:
            flag = False
elif opc == 2:
    while flag:
        f = float(input("rpm = "))
        if f>1800 or f<1620:
            print("valor fuera de los limites vuelva a intentar")
        else:
            flag=False
            #convertimos las rpm a porcentaje
            f = f/1800
#multiplicador para encontrar el torque de entrada
torque_in = torque_n*factor(f)
torque_out = torque_in*relacion_engranajes
# sabemos que tau_max = S_u/FS S_u=322 ksi = 322000psi
tau_max=322000/FS
#aqui despejamos el diametro de la ecuacion tau_max = T *c/J=> d^3 =16*T/(pi*tau_max)
d3_1= (16*torque_out/(pi*tau_max))**(1/3)
#por medio del angulo de torsion por unidad de longituda tnemos la siguiente formula
#phi/L = 2.5°/in = 0.0436 rad/in
phi_l=0.0436
# phi/L = T/(J*G) => c^4=2T/(pi*G*(phi/L))=>d^4=32T/(pi*G*(phi/L))
d3_2 = (32*torque_out/(pi*G*phi_l))**(1/4)
d3=0
#aqui obtenemos el d3 minimo necesario
if d3_1>d3_2:
    d3=d3_1
else:
    d3=d3_2
#ahora con las relaciones geometricas definimos las demas caracteristicas teniendo en cuenta que r1 es el radio en los engranajes y r2 es el radio en los rodamientos
d2=0
d1=0
r1=0
r2=0
d2=d3/relacion_d3_d2
d1=d2/relacion_d2_d1
r1=relacion_r1_d2*d2
r2=relacion_r2_d1*d1
#continuamos buscando el esfuerzo maximo a trevez de las formulas de concentracion de estress
#primero en la seccion 3,2
h=(d3-d2)/2
c1=0.905+(0.783*((h/r1)**(1/2)))-(0.075*h/r1)
c2=-0.437-(1.969*((h/r1)**(1/2)))+(0.553*h/r1)
c3=1.557+(1.073*((h/r1)**(1/2)))-(0.578*h/r1)
c4=-1.061+(0.171*((h/r1)**(1/2)))+(0.086*h/r1)
#multiplicador para la concentracion de esfuerzos
K = c1+(c2*2*h/d3)+c3*((2*h/d3)**2)+c4*((2*h/d3)**3)
tau_nom=16*torque_out/(pi*(d2**3))
tau_maximo32=K*tau_nom
#calculamos los esfuerzos y angulos ya que no sabemos que diametro se escogio
tau_max=16*torque_out/(pi*(d3**3))
phi_l=32*torque_out/(pi*G*(d3**4))
print("d3 =",round(d3,3),"in\nd2 =",round(d2,3),"in\nd1 =",round(d1,3),"in\nestres maximo en la seccion 3 =",round(tau_max/1000,2),"ksi\nestres maximo en las secciones 2 =",round(tau_maximo32/1000,2),"ksi")
print("angulo de rotacion por unidad de longitud =",round(phi_l*360/(2*pi),4),"°/in")
print("radio engranajes =",round(r1,4),"in\nradio rodamiento =",round(r2,4),"in")
#estres maximo en las secciones 1 =",tau_maximo21/1000,"ksi\n
#,phi_l,"rad/in = "