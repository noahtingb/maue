#youtube länk: censur

#importa nödvändiga biblotek
import numpy as np
import matplotlib.pyplot as plt
import scipy
#egen klass från andra projekt
class noahti:
    def slf(x,y):#minsta kvadrat anpassning
        x_=x-np.mean(x)
        y_=y-np.mean(y)
        return np.sum(x_*y_)/np.sum(x_**2),np.mean(y)-np.mean(x)*np.sum(x_*y_)/np.sum(x_**2)

def uppgift1():
    def uppgift1a():
        fig, ax = plt.subplots()#figur och axel
        ax.scatter(T,R,marker='o')
        ax.set_xlabel("Temperatur (°C)")
        ax.set_ylabel("Resistans (Ohm)")
        plt.show()
    def uppgift1b():
        print(f"Anpassad funktion är: R = {f(0):.3f} + {k:.4f}*T")#printa anpassad funktion
        fig, ax = plt.subplots()#figur och axel
        x=np.linspace(20,100,1000)#xvärden
        ax.scatter(T,R,marker='o')#data
        ax.plot(x,f(x),color="orange")#anpassad funktion
        ax.set_xlabel("Temperatur (°C)")
        ax.set_ylabel("Resistans (Ohm)")
        plt.show()
    def uppgift1c():
        print("Uppskattad resistans vid 100°C är "+f"{f(100):.1f} Ohm")#uppskattat vid f(100)
    T= np.array([20.5,32.7,51.0,73.2,95.7])#temperatur i celcius
    R= np.array([765,826,873,942,1032])#resistans i Ohm
    uppgift1a()
    k,m=noahti.slf(T,R)#anpassa linjär funktion
    f = lambda t: k*t + m #anpassad funktion
    uppgift1b()
    uppgift1c()
def uppgift2():
    def f(L,a0,a1):
        return a0 * L ** a1
    data=np.array([[3+34.5,13.08],[3+33,12.56],[3+30,12.03],[3+28,11.07],[3+26,10.9],[3+23,10.76],[3+21,10.28],[3+40,13.43]])
    x=data[:,0]#xvärden
    y=data[:,1]/10#yvärden
    [p0,p1],_=scipy.optimize.curve_fit(f, x, y, p0=[2, 0.5])#anpassa funktion #uppgift a
    print(f"a) T={p0:.2f}*L^{p1:.2f}, (Ok enligt dim. analys)")#plotta resultat
    fig, ax = plt.subplots()#figur och axel
    x1=np.linspace(0, np.max(x), 100)#linspace för anpsad funktion
    ax.scatter(x,y,marker='o')
    ax.plot(x1, f(x1,p0,p1), color="orange")#anpassad funktion
    ax.set_xlabel("Längd (cm)")
    ax.set_ylabel("Periodstid (s)")
    plt.show()
    print(f"c) L= {(1/p0)**(1/p1):.2f} cm ty jag har en lätt vikt")#enligt min låga massa

def uppgift3():
    def uppgift3a():
        fig, ax = plt.subplots()#figur och axel
        ax.scatter(S_data,v_data,marker='o')
        ax.set_xlabel("S (mol)")
        ax.set_ylabel("V mg/min")
        plt.show()
    def uppgift3b():
        fig, ax = plt.subplots()#figur och axel
        Sspan=np.linspace(0, np.max(S_data)*1.2, 100)
        ax.scatter(S_data,v_data,marker='o')
        ax.plot(Sspan, v(Sspan,[p0,p1]), color="orange")#anpassad funktion
        ax.set_xlabel("S (mol)")
        ax.set_ylabel("V mg/min")
        plt.show()
    def v(S,a):
        return a[0]*S/(1+a[1]*S)
    def dif(params,xd,yd):
        return yd - v(xd,params)
    S_data=np.array([1.5,2.0,3.0,4.0,8.0])#Sdata
    v_data=np.array([0.21,0.25,0.28,0.33,0.44])#Vdata
    [p0,p1],_=scipy.optimize.leastsq(dif, [1, 1], (S_data, v_data))#anpassa funktion

    uppgift3a()
    uppgift3b()

def uppgift4():
    def uppgift4a():
        fig, ax = plt.subplots()#figur och axel
        ax.plot(ardata,data)#datan
        ax.set_xlabel("år")#xlabel
        ax.set_ylabel("personer (miljader)")#ylabel
        plt.show()#visa
    def uppgift4b():
        print(f"Anpassad funktion är: N(t) = {p0*1e15:.2f}*exp({p1:.4f}*t)*10^(-15)")#printa anpassad funktion
        fig, ax = plt.subplots()#figur och axel
        Tspan=np.linspace(np.min(ardata), 2101, 1000)#linspace
        ax.scatter(ardata,data)#datan
        ax.plot(Tspan, N(Tspan,[p0,p1]), color="orange")#anpassad funktion
        ax.set_xlabel("år")#xlabel
        ax.set_ylabel("personer (miljader)")#ylabel
        plt.show()#visa
    def uppgift4c():
        print(f"År då befolkningen är 15 miljarder: {np.log(15/p0)/p1:.0f}")#anger det år då befolkningen är 15 miljader
    def uppgift4d():
        print(f"Befolkning år 2100: {N(2100,[p0,p1]):.2f} miljarder personer vilket inte är rimligt")#printa befolkningen
    def N(t,a):#funktionen som ska anpassas
        return a[0]*np.exp(a[1]*t)#funktion
    def dif(params,xd,yd):#skillnad
        return yd - N(xd,params)#dif     
    data=np.loadtxt("population.txt")#ladda data
    ar=np.arange(1951,1951+150,1)#år från 1951 till 2100
    ardata=ar[:np.shape(data)[0]]#år med data
    uppgift4a()#kör uppgift 4a
    [p0,p1],_=scipy.optimize.leastsq(dif, [1e-3, 1e-2], (ardata, data))#anpassa funktion
    uppgift4b()#kör uppgift 4b
    uppgift4c()#kör uppgift 4c
    uppgift4d()#ej rimligt ty funktion är mer som a1*exp(r1*t)/(1+a2*exp(r1*t))

def uppgift():
    print()
    print("\nUppgift 1:")
    #uppgift1() #kör uppgift1
    print("\nUppgift 2:")
    #uppgift2() #kör uppgift2
    print("\nUppgift 3:")
    #uppgift3() #kör uppgift3
    print("\nUppgift 4:")
    uppgift4() #kör uppgift4
uppgift() #kör alla markerade uppgifter

#youtube länk: censur
