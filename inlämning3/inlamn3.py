#youtubelänk censur

#biblotek
import numpy as np
import matplotlib.pyplot as plt

def uppgift1():
    def uppgift1a():
        
        print(f"Typ      Män \t Kvinnor\
              \nHögsta:  {np.max(men_length):.1f} \t {np.max(women_length):.1f}\
              \nLägsta:  {np.min(men_length):.1f} \t {np.min(women_length):.1f}\
              \nMedel:   {np.mean(men_length):.1f} \t {np.mean(women_length):.1f}\
              \nMedian:  {np.median(men_length):.1f} \t {np.median(women_length):.1f}\
              \nStd:     {np.std(men_length):.1f} \t {np.std(women_length):.1f}")#printa alla värden i en tabell
    def uppgift1b():
        fig,ax=plt.subplots(1,2,figsize=(12,4))#skapa en figur och axel
        ax[0].hist(men_length,bins=20,edgecolor="black")
        ax[1].hist(women_length,bins=20,edgecolor="black")
        ax[1].set_title("Medellängd kvinnor i cm")#titel
        ax[0].set_xlabel("Medellängd män i cm")#titel
        ax[1].set_xlabel("längd i cm")#titel
        ax[0].set_xlabel("längd i cm")#titel
        ax[1].set_ylabel("Frekvens")#titel
        ax[0].set_ylabel("Frekvens")#titel
        plt.show()
    men_length=np.loadtxt('men_length.txt')#mäns längd
    women_length=np.loadtxt('women_length.txt')#kvinnors längd
    uppgift1a()
    uppgift1b()
def uppgift2():
    def uppgift2a():
        fig,ax=plt.subplots()#skapa en figur och axel
        ax.stairs(datay,datax,fill=True)#plota historgammet
        ax.set_xlabel("ålder")#xlabel
        ax.set_ylabel("frekvens")#ylabel
        plt.show()
    def uppgift2b():
        mean_age=np.sum((datax[1:]-2.5)*datay)/np.sum(datay)#beräkna medelålder
        over70=np.sum(datay[14:])#antal över 70 år
        print(f"Medelålder: {mean_age:.1f} år")#printa medelåldern
        print(f"Över 70 år: {over70} personer")#printa antal personer över 70 år
    datax=np.arange(-0.5,109.5,5)#xdatan
    datay=np.array([286361,316609,324475,315801,311004,332023,399933,367985,335631,328040,334373,345526,\
                    295365,269801,250856,241515,151369,73559,26561,5256,476])#datany
    uppgift2a()
    uppgift2b()

def uppgift3():
    def uppgift3a():        
        fity=np.array([np.mean(y[max(i-k,0):min(leny,i+k+1)]) for i in range(leny)])#medelvärdesavbildningen
        plt.plot(y,color='blue')#plota signalen
        plt.plot(fity,color='red')#plota fited signalen
        plt.show()#visa
    def uppgift3b():        
        fity=np.array([np.median(y[max(i-k,0):min(leny,i+k+1)]) for i in range(leny)])#medianvärdesavbildningen
        plt.plot(y,color='blue')#plota signalen
        plt.plot(fity,color='red')#plota fited signal
        plt.show()#visa
    y=np.loadtxt('signal.txt')#läs in signalen
    k=5#fönsterstorleken
    leny=y.shape[0]#sizen på y
    uppgift3a()
    uppgift3b()

def uppgift4():
    def uppgift4a():
        fig,ax=plt.subplots()#skapa en figur och axel
        ax.hist(Wtot,bins=20,edgecolor="black")#plota signalen
        ax.set_xlabel("Rörelseenergi i J")#xlabel fel enhet använder ni
        ax.set_ylabel("Frekvens")#ylabel
        plt.show()#visa
    def uppgift4b():
        print(f"Medelvärde av energin: {np.mean(Wtot):.0f} J")#printa medelvärde 
    m = lambda: 5000+100*np.random.standard_normal()#massan
    v = lambda: 400+70*np.random.standard_normal()#farten
    W = lambda m,v: 0.5*m*v**2#rörelseenrgin
    N = int(1e5)#antal simuleringar
    Wtot=np.array([W(m(),v()) for i in range(N)])#energi
    uppgift4a()
    uppgift4b()
def uppgift5():

    punkter=np.array([[-2,-1],[2,4]])#datapunkter
    k=(punkter[0,1]-punkter[1,1])/(punkter[0,0]-punkter[1,0])#lutning
    m=punkter[0,1]-punkter[0,0]*k#konstanten
    print(f"y={k:.2f}*x+{m:.1f}")#printa ekvationen
    #y=1.25*x+1.5
    x=np.linspace(-3,3,100)#xdata
    y=k*x+m#ydata
    fig,ax=plt.subplots()#skapa en figur och axel
    ax.plot(x,y,color='blue')#plota linjen
    ax.scatter(punkter[:,0],punkter[:,1],color="red")#plota linjen
    plt.show()#visa plotten
def uppgift6():
    from scipy.optimize import curve_fit as fit
    def uppgift6a():
        fig,ax=plt.subplots()#figur och axel
        t=np.linspace(1954,1980,100)#tid för plot
        ax.plot(t,expfunk(t,0.1),label=f'r={0.1}')#r=0.1 plot
        ax.plot(t,expfunk(t,0.3),label=f'r={0.3}')#r=0.3 plot
        ax.plot(t,expfunk(t,rfit),label=f'r={rfit:.2f} (fitted)')#fitted plot mha curve_fit
        ax.scatter(xdata,ydata,color='black',label='Data')#datapunkter
        ax.legend()
        ax.set_xlabel("År")
        ax.set_ylabel("Häckande par")
        plt.show()#visa
    def uppgift6b():
        utdödår=-np.log(1/45)/rfit+1954#ekvation för att hitta året då arten är utdöd
        print(f"Arten är utdöd år {utdödår:.0f}")
        fig,ax=plt.subplots()#figur och axel
        t=np.linspace(1954,1980,100)#tid för plot
        ax.plot(t,expfunk(t,rfit),label=f'r={rfit:.2f} (fitted)',color="orange")#fitted plot mha curve_fit
        ax.scatter(xdata,ydata,color='blue',label='Data')#datapunkter
        ax.legend()
        ax.set_xlabel("År")
        ax.set_ylabel("Häckande par")
        plt.show()#visa
    def expfunk(t,r): 
        return 45*np.exp(-r*(t-1954))#funktionen
    xdata=np.array([1954, 1956, 1958, 1960, 1962, 1964, 1966, 1968, 1970])#år
    ydata=np.array([45, 33, 26, 16, 10, 8, 6, 6, 5])#äckande par
    [rfit],_=fit(expfunk,xdata,ydata, p0=[0.1])#fitting
    uppgift6a()
    uppgift6b()

def uppgift():
    print()
    print("\nUppgift 1:")
    uppgift1() #kör uppgift1
    print("\nUppgift 2:")
    uppgift2() #kör uppgift2
    print("\nUppgift 3:")
    uppgift3() #kör uppgift3
    print("\nUppgift 4:")
    uppgift4() #kör uppgift4
    print("\nUppgift 5:")
    uppgift5() #kör uppgift5
    print("\nUppgift 6:")
    uppgift6() #kör uppgift6
uppgift() #kör alla markerade uppgifter

#länk censur
