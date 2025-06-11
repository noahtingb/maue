#youtube länk: censur

#%% bibliotek
#importa nödvändiga biblotek
import numpy as np
import matplotlib.pyplot as plt
import scipy

    
#%% mycode
#egen klass från andra projekt tom

#%% uppgift 1
def uppgift1():
    def derivate(x,y):
        prim=np.zeros(x.shape[0])#vektor
        prim[0]=(y[1]-y[0])/(x[1]-x[0])#first
        prim[x.shape[0]-1]=(y[x.shape[0]-1]-y[x.shape[0]-2])/(x[x.shape[0]-1]-x[x.shape[0]-2])#last
        for i in range(x.shape[0]-2):#alla andra
            prim[i+1]=(y[i+2]-y[i])/(x[i+2]-x[i])
        return prim
    def f(x):
        return x**2
    xs=np.linspace(-2, 2, 2000)  # 2000 punkter i intervallet [-2, 2]
    y=f(xs)#funktionen
    y_d1=derivate(xs,y)#första derivatan
    fig,ax=plt.subplots()#figur och axel
    ax.spines['top'].set_visible(False)#ingen linje uppe
    ax.spines['right'].set_visible(False)#ingen linje till höger
    ax.spines['left'].set_position('zero')#linjen vid 0 i x-led
    ax.spines['bottom'].set_position('zero')#linjen vid 0 i y-led
    ax.plot(xs,y,label="f(x)")#funktionen
    ax.plot(xs,y_d1,color='orange',label="f'(x)")#derivatan
    ax.grid("on")
    ax.legend()
    plt.show()
#%% uppgift 2
def uppgift2():
    def uppgift2a(Lmax=68.5, r=0.1, L0=18):
        t=np.linspace(0,40,1000) # 1000 punkter för x från 0 till 40
        L=np.zeros(t.shape[0]) # Skapa en tom vektor för L
        L[0]=L0#initialvärde för L
        for i in range(t.shape[0]-1):#loppa igenom dem
            L[i+1]=r*(Lmax-L[i])*(t[i+1]-t[i])+L[i]#differentialekvationen
        fig,ax=plt.subplots()#figur och axel
        ax.plot(t,L,label="L(t)")#funktionen
        ax.set_xlabel("t i år")#xlabel
        ax.set_ylabel("L i cm")#ylabel
        plt.show()   
    def uppgift2b():
        def diffekv(x,params):
            y=np.zeros(x.shape[0])#skapa en tom vektor för y
            y[0]=params[0]#första värdet
            for i in range(x.shape[0]-1):#loppa igenom dem
                y[i+1]=params[2]*(params[1]-y[i])*(x[i+1]-x[i])+y[i]#differentialekvationen
            return y#returna vektorn
        def dif(params,xd,yd):
            return yd - diffekv(xd,params)
        
        t=np.array([3,5,7,9,11,13,15,17,19,21])#xdata
        L=np.array([25.5,29.1,35.5,41.8,45.5,50.0,53.6,56.4,56.5, 58.2])#ydata
        [L3,Lmax,r],_=scipy.optimize.leastsq(dif, [24, 70,0.07], (t, L))#anpassa funktion
        L0=diffekv(3-np.linspace(0,3,1000),[L3,Lmax,r])[1000-1]#beräkna L(0) bakåt
        print(f"Anpassad funktion är: L0(3)={L0:.2f}, dL(t)/dt = {r:.4f}*({Lmax:.2f} - L(t))")
        tlin=np.linspace(0,40,10000) # 10000 punkter för x från 0 till 40
        fig,ax=plt.subplots()#figur och axel
        ax.scatter(t,L)#datan
        ax.plot(tlin,diffekv(tlin,[L0,Lmax,r]),color="orange")
        ax.set_xlabel("tid i år")#xlabel
        ax.set_ylabel("längd i cm")#ylabel
        plt.show()   
        return [L0,Lmax,r] #returna värdena
    def uppgift2c():
        def diffekv(x):
            y=np.zeros(x.shape[0])#skapa en tom vektor för y
            y[0]=paramsout[0]#första värdet
            for i in range(x.shape[0]-1):#loppa igenom dem
                y[i+1]=paramsout[2]*(paramsout[1]-y[i])*(x[i+1]-x[i])+y[i]#differentialekvationen
            return y#returna vektorn
        def derivate(x,y):#derivatan
            prim=np.zeros(x.shape[0])#vektor
            prim[0]=(y[1]-y[0])/(x[1]-x[0])#first
            prim[x.shape[0]-1]=(y[x.shape[0]-1]-y[x.shape[0]-2])/(x[x.shape[0]-1]-x[x.shape[0]-2])#last
            for i in range(x.shape[0]-2):#alla andra
                prim[i+1]=(y[i+2]-y[i])/(x[i+2]-x[i])
            return prim
        def M(L):
            return 0.00000892 * L**3#funktionen för M
        t=np.linspace(0,40,1000)
        massa=M(diffekv(t))#beräkna massan
        massprim=derivate(t,massa)#derivatan av massan
        fig,ax=plt.subplots(1,2,figsize=(12,5))#figur och axel
        ax[0].plot(t,massa,label="M(t)")#massan
        ax[1].plot(t,massprim,label="dM/dt")#tidsderivatan av massa
        ax[0].set_xlabel("tid i år")#xlabel
        ax[1].set_xlabel("tid i år")#xlabel
        ax[0].set_ylabel("massa i kg")#ylabel
        ax[1].set_ylabel("dm/dt i kg/år")#ylabel
        plt.show() 
        print(f"Ökningen av massa är som störst vid {t[np.argmax(massprim)]:.2f} år")#printa tiden då derivatan är störst 12.3 år
    uppgift2a()
    paramsout=uppgift2b()
    uppgift2c()

#%% Uppgift 3
def uppgift3():
    def uppgift3a():
        def diffekv(x):
            M=np.zeros(x.shape[0])#skapa en tom vektor för y
            M1=np.zeros(x.shape[0])#skapa en tom vektor för y
            M[0]=0.6#första värdet
            M1[0]=0.4#första värdet
            for i in range(x.shape[0]-1):#loppa igenom dem
                M[i+1]=(-0.25*M[i]+0.02*M1[i])*(x[i+1]-x[i])+M[i]#differentialekvationen1
                M1[i+1]=(0.25*M[i]+(-0.02-0.05)*M1[i])*(x[i+1]-x[i])+M1[i]#differentialekvationen1
            return M,M1#returna vektorn
        
        t=np.linspace(0,20,1000)
        M_t,M1_t=diffekv(t)#beräkna massan
        fig,ax=plt.subplots()#figur och axel
        ax.plot(t,M_t,label="plantor")#massan
        ax.plot(t,M1_t,label="jord",linestyle="--")#skillnaden av massa
        ax.set_xlabel("tid i månader")#xlabel
        ax.set_ylabel("M")#ylabel
        ax.legend()
        plt.show() 
        return t, M_t, M1_t# returna tiden och massorna
    def uppgift3b():
        print(f"Giftnivån i jorden är som störst vid {t[np.argmax(M1_t)]:.2f} månader")#printa tiden då M1 är störst 
    t, M_t, M1_t=uppgift3a()
    uppgift3b()

#%% Uppgift 4
def uppgift4():
    def diffekv(x,a=1,b=0.03,c=0.5,d=0.013,N0_0=90,N1_0=40):
            N0=np.zeros(x.shape[0])#skapa en tom vektor för y
            N1=np.zeros(x.shape[0])#skapa en tom vektor för y
            N0[0]=N0_0#första värdet
            N1[0]=N1_0#första värdet
            for i in range(x.shape[0]-1):#loppa igenom dem
                N0[i+1]=(a*N0[i]-b*N0[i]*N1[i])*(x[i+1]-x[i])+N0[i]#differentialekvationen1
                N1[i+1]=(-c*N1[i]+d*N0[i]*N1[i])*(x[i+1]-x[i])+N1[i]#differentialekvationen1
            return N0,N1#returna vektorn
    def uppgift4a():
        fig,ax=plt.subplots()#figur och axel
        ax.plot(t,N0_t,label="kaniner")#antal
        ax.plot(t,N1_t,label="vargar",linestyle="--")#skillnaden av antal
        ax.set_xlabel("tid i månader")#xlabel
        ax.set_ylabel("antal")#ylabel
        ax.legend()
        plt.show() 
    def uppgift4b():
        fig,ax=plt.subplots()#figur och axel
        ax.plot(N0_t,N1_t,label="orginal")#antal
        ax.plot(N0_t2,N1_t2,label="N0(0)=90 N1(0)=90")#antal
        ax.plot(N0_t3,N1_t3,label="N0(0)=40 N1(0)=90")#antal
        ax.set_xlabel("kaniner")#xlabel
        ax.set_ylabel("varjar")#ylabel
        ax.legend()
        plt.show()
    def uppgift4c(): 
        def dif(x=t,params=[1,0.03,0.5,0.013]):#donttrythis
            dN1,dN2=diffekv(x,a=params[0], b=params[1], c=params[2], d=params[3])
            freq=scipy.fft.fftfreq(x.shape[0],d=x[1]-x[0])#frequencies
            plt.plot(freq,scipy.fft.fft(dN1))
            plt.plot(freq,scipy.fft.fft(dN2))
            plt.show()
            fN1=np.argmax(np.abs(scipy.fft.fft(dN1))[1:])+1
            fN2=np.argmax(np.abs(scipy.fft.fft(dN2))[1:])+1
            print(np.pi*2/freq[fN1],np.pi*2/freq[fN2])
        if False:
            for i in range(4):
                fig,ax=plt.subplots()#figur och axel
                t1=np.linspace(0,30,10000)
                aN0_t,aN1_t=diffekv(t1)#diffekvation
                params=[1,0.03,0.5,0.013]
                params[i]=3*params[i]
                dN0_n,dN1_n=diffekv(t1,a=params[0], b=params[1], c=params[2], d=params[3])#nydif
                params[i]=0.3*params[i]
                dN0_n1,dN1_n1=diffekv(t1,a=params[0], b=params[1], c=params[2], d=params[3])#nydif
                ax.plot(t1,aN0_t,label=f'kaniner gamla {["a","b","c","d"][i]}')#antal
                ax.plot(t1,aN1_t,label=f'vargar gamla {["a","b","c","d"][i]}',linestyle="--")#skillnaden av antal
                ax.plot(t1,dN0_n,label=f'kaniner nya ök {["a","b","c","d"][i]}')#antal
                ax.plot(t1,dN1_n,label=f'vargar nya ök {["a","b","c","d"][i]}',linestyle="--")#skillnaden av antal     
                ax.plot(t1,dN0_n1,label=f'kaniner nya min {["a","b","c","d"][i]}')#antal
                ax.plot(t1,dN1_n1,label=f'vargar nya min {["a","b","c","d"][i]}',linestyle="--")#skillnaden av antal        
                ax.set_xlabel("tid i månader")#xlabel
                ax.set_ylabel("antal")#ylabel
                ax.legend(loc="upper right")
                plt.show() 
            #ökat a minskar periodstid
            #ökat b ökar periodtid
            #ökat c minskar periodstid
            #ökat d ökar periodstid
        print("\tÖkat a minskar periodstid\
                \n\tÖkat b ökar periodtid\
                \n\tÖkat c minskar periodstid\
                \n\tÖkat d ökar periodstid")
    t=np.linspace(0,100,10000)
    N0_t,N1_t=diffekv(t)#diffekvation
    N0_t2,N1_t2=diffekv(t,N0_0=90,N1_0=90)#diffekvation ny
    N0_t3,N1_t3=diffekv(t,N0_0=40,N1_0=90)#diffekvation ny

    uppgift4a()
    uppgift4b()
    uppgift4c()
#%% datorlaboration
def datorlaboration():
    print()
    print("\nUppgift 1")
    uppgift1()
    print("\nUppgift 2")
    uppgift2()
    print("\nUppgift 3")
    uppgift3()
    print("\nUppgift 4")
    uppgift4()
datorlaboration()
#youtube länk: censur