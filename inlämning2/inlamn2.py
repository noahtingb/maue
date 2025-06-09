#youtubelänk censur

#biblotek
import numpy as np
import matplotlib.pyplot as plt

def uppgift1():
    def uppgift1a():
        fig, ax = plt.subplots() #make subplots
        ax.tick_params(labelsize=14) #ni ville detta
        ax.plot(x,f(x),color='green',linestyle="--") #plota funk f
        ax.plot(x,g(x),color='red',linestyle="-")# plota funk g
        plt.show() #visa plotten    
    def uppgift1b():
        #kopierat från korsboken delviss
        fig, ax = plt.subplots()#make subplots
        ax.plot(x,f(x),color='green',linestyle="--")#plotta funk f
        ax.plot(x,g(x),color='red',linestyle="-")#plota funk g
        ax.tick_params(labelsize=14)#storleken på etiketterna
        ax.grid('on')#ha grids
        ax.spines['top'].set_visible(False)#ingen linje uppe
        ax.spines['right'].set_visible(False)#ingen linje till höger
        ax.spines['left'].set_position('zero')#linjen vid 0 i x-led
        ax.spines['bottom'].set_position('zero')#linjen vid 0 i y-led
        plt.show()
    f= lambda x: x/(1+x)#funktionen f
    g=lambda x: x**2/(1+x**2)#funktionen g
    x=np.linspace(0,10,1000) #linspace från 0 till 10 med 1000 punkter
    uppgift1a() #kör uppgift1a
    uppgift1b() #kör uppgift1b

def uppgift2():
    fig,ax=plt.subplots() #make subplots
    datax=np.array([1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960])#år
    datay=1000*np.array([3929,5308,7240,9638,12866,17069,23192,31443,38558,50156,62948,75995,91972,105711,122775,131669,150697,179323])#antal invåndare
    N=lambda t: 197273000/(1+np.exp(-0.03134*(t-1913.25)))#funktionen n
    t=np.linspace(1790,1960,1000)#tiden från 1913 till 2013
    ax.plot(t,N(t),color='blue',linestyle='--')#plota funk N(t)
    ax.scatter(datax,datay,color='red')#plota datan
    ax.set_xlabel('År')#xlavel
    ax.set_ylabel("Befolkningsstorlek")#ylabel
    ax.set_title("Befolkningen i USA mellan 1790 och 1960")
    plt.show()#visa ploten
def uppgift3():
    def uppgift3a():
        fig,ax=plt.subplots()#make subplots
        ax.set_xlabel('temperatur år 1981')#xlabel
        ax.set_ylabel('frekvens')#ylabel
        ax.hist(T[0,:], bins=15,edgecolor='black')#Histogram 1
        plt.show()#visa ploten
    def uppgift3b():
        fig,ax=plt.subplots()#make subplots
        ax.set_ylabel('frekvens')#ylabel
        ax.set_xlabel('temperatur år 1985')#xlabel
        ax.hist(T[4,:], bins=15,edgecolor='black')#Histogram 1
        plt.show()#visa ploten
    T=np.loadtxt('T10365.txt')#läs in matrisen
    uppgift3a() #kör uppgift3a
    uppgift3b() #kör uppgift3b
def uppgift4():
    def inputa(text):#hantera error
        try:
            return float(input(text)) #
        except:
            print("error")
            inputa(text)#kalla igen vid fel
    print("a/b:")
    a=inputa("a= ")#input a
    b=inputa("b= ")#input b
    while b==0:
        print("Division med noll ej tillåtet")
        b=inputa("b= ")#input b
    print(f"a/b={a/b:.2f}")#skriv ut res
def uppgift5():
    C=np.loadtxt("CCD.txt")#läs in matrisen
    plt.imshow(C,cmap="gray",vmin=3,vmax=7)#plota bilden

    plt.show()#visa plotten
    for i in range(C.shape[0]):#loppa igenom raderna
        for j in range(C.shape[1]):#lopa igenom kolumnerna
            if C[i,j]==0:#ifall värdet är 0
                C[i,j]=1/8*(C[i-1,j]+C[i+1,j]+C[i-1,j+1]+C[i+1,j+1]+C[i-1,j-1]+C[i+1,j-1]+C[i,j-1]+C[i,j+1])#korrigera
    plt.imshow(C,cmap="gray",vmin=3,vmax=7)#plota bilden
    plt.show()#visa plotten
    #visa ploten
def uppgift6():
    def uppgift6a():
        A=plt.imread("havsorn_PO.jpg")#läs in bild
        fig, ax = plt.subplots()  # skapa en figur och axel
        ax.imshow(A)   # visa bild
        ax.axis('equal')
        ax.axis('off')
        plt.show()#visa plotten
        fig, ax = plt.subplots()  # skapa en figur och axel
        A=A.astype(dtype='float')
        bla  = np.array([1,122,195])# blå färg som vi vill byta ut
        rosa = np.array([255,192,203]) # ny färg, ljus rosa  
        (m,n,o)=A.shape #få storlek
        for m in range(A.shape[0]): #loop igenom raderna
            for n in range(A.shape[1]): #loop igenom kolumnerna
                if np.sqrt(np.sum((A[m,n,:]-bla)**2)/np.sum(A[m,n,:]**2))<0.1:
                    A[m,n]=rosa
        A=A.astype(dtype='int')#till heltal
        ax.imshow(A)   # visa bild
        ax.axis('equal')
        ax.axis('off')
        plt.show()#visa plotten
    def uppgift6b():
        A=plt.imread("havsorn_PO.jpg")#läs in bild
        fig, ax = plt.subplots()  # skapa en figur och axel
        ax.imshow(A)   # visa bild
        ax.axis('equal')
        ax.axis('off')
        plt.show()
        fig, ax = plt.subplots()  # skapa en figur och axel
        A=A.astype(dtype='float')
        bla  = [1,122,195]# blå färg som vi vill byta ut
        rosa = [255,192,203] # ny färg, ljus rosa  
        (m,n,o)=A.shape #få storlek
        for m in range(A.shape[0]): #loop igenom raderna
            for n in range(A.shape[1]): #loop igenom kolumnerna
                if np.sqrt(np.sum((A[m,n,:]-bla)**2)/np.sum(A[m,n,:]**2))>0.1:#kolla om färgen är lågnt ifrån den blåa färgen
                    A[m,n]=rosa
        A=A.astype(dtype='int')#till heltal
        ax.imshow(A)   # visa bild
        ax.axis('equal')
        ax.axis('off')
        plt.show()
    #uppgift6a()
    uppgift6b()
def uppgift():
    #uppgift1() #kör uppgift1
    #uppgift2() #kör uppgift2
    #uppgift3() #kör uppgift3
    #uppgift4() #kör uppgift4
    #uppgift5() #kör uppgift5
    uppgift6() #kör uppgift6
uppgift() #kör alla markerade uppgifter

#länk censur
