#TODO Uppgift 1,2,3,4 done

class myfunc:#kod från min leetcode eller github eller någonstans där jag är uppehovsrättsinnehavare för koden
    def inplacefunsort(self,nums):#från leetcode "sort an array" (fun version) gissa vilken ovanlig sorteringsmetod jag använder tips worst case: nlog(n) och in-place
        for index in range(len(nums)):    
            while index>0 and nums[index]>nums[(index-1)//2]:
                nums[(index-1)//2],nums[index]=nums[index],nums[(index-1)//2]
                index=(index-1)//2
            #print(nums)

        i=len(nums)-1
        #print(nums)
        while i>0:
            nums[0],nums[i]=nums[i],nums[0]
            index=0
            while True:
                if index*2+2<i:
                    if nums[(index*2+1)]>nums[(index*2+2)]:
                        indexcomp=(index*2+1)
                    else:
                        indexcomp=(index*2+2)
                    if nums[index]<nums[indexcomp]:
                        nums[index],nums[indexcomp]=nums[indexcomp],nums[index]
                        index=indexcomp
                    else:
                        break
                elif index*2+2==i:
                    indexcomp=index*2+1
                    if nums[index]<nums[indexcomp]:
                        nums[index],nums[indexcomp]=nums[indexcomp],nums[index]
                        index=indexcomp
                    else:
                        break
                else:
                    break
            i+=-1
        return nums
    


def uppgift1():
    def uppgift1a():#okej
        s = 0                  # Sätt summa till noll
        for i in range(1,101): # Loopa från 1 till 100, måste skriva 101 inte 100
            s = s + i          # Addera term till summan 
        print('Summan är ',s)  # Skriv ut resultatet
    def uppgift1b():
        s=0
        for i in range(1,11):
            s+=1
        print('Summan är ',s)  # Skriv ut resultatet
    uppgift1a()
    uppgift1b()

def uppgift2():
    def uppgift2a():return 9**(1/2); #ja eftersom 9**1/2 tar ju 9**1 först ty proriteringsregler
    def uppgift2b():return 1.51*10**-8*6.18*10**9;#behövs ej kommenteras 
    uppgift2a()
    uppgift2b()

def uppgift3():
    def uppgift3a(k,m):
        f = lambda x : k*x + m #definerade funktionen
        return f
    def uppgift3b():
        v=uppgift3a(2,3)(1)#ta värdena bara
        print(v)
    uppgift3b()

def uppgift4():
    def uppgift4a(x):return len(x);#längden på listan
    def uppgift4b(x): print(x[0],x[1],x[-1]);#first, second last
    def uppgift4c(x):#rolig lösning
        noahtingb=myfunc()
        noahtingb.inplacefunsort(x)
        print(x)
    u=[10,20,3,4,-52]
    n=uppgift4a(u)
    uppgift4b(u)
    uppgift4c(u)

def uppgift5():
    def uppgift5a(): #behövs ej kommenteras
        print("svar för uppgift 5a är 15820.0")
        return 15820
        pass
        Ugamla = float(input('U-värde för gamla fönster '))
        Unya = float(input('U-värde för nya fönster '))
        area = float(input('Fönsterarea '))
        gradtimmar = float(input('Gradtimmar för orten '))
        elpris = float(input('Elpris '))
        energibesparing = (Ugamla - Unya)*area*gradtimmar
        kostnadsbesparing = energibesparing*elpris
        kostnadsbesparing
    def uppgift5b():
        var={"fast avgift":0,"antal enheter":0,"pris per enhet":0}
        fragor=["fast avgift","antal enheter","pris per enhet"]
        for fraga in fragor:  
            try:              
                var[fraga]=float(input(f"{fraga}? "))
            except TypeError:
                print("Felaktig inmatning, var god försök igen från början med tal")
                uppgift5b()     
        netto= var.get("fast avgift")+var.get("antal enheter")*var.get("pris per enhet")
        brutto=netto*1.25
        print(f"kostnaden utan moms är {netto:.0f} kr \\ - || -  med moms är {brutto:.0f} kr")
    uppgift5a()
    uppgift5b()

def uppgift6():
    import numpy as np
    x,y=np.array([1,2,3]),np.array([4,5,6]) #a
    s=x+5 #b
    t=x*8 #c
    u=x+y#d
    print(u)#d
    v=np.sqrt(x)#e
    print(v)#e
    del np
def uppgift7():
    def uppgift7a():
        import numpy as np
        # Läs in temperaturvärden från filen T10365.txt.
        # Lagra i 10 x 365 matrisen T
        T = np.loadtxt('T10365.txt')
        # max, min, medelvärde för 1981-90, avrunda till en decimal
        print() # ger en tom rad
        print('Maximal temperatur under 10 år', np.round( np.max(T),1 ) )
        print('Minimal temperatur under 10 år', np.round( np.min(T),1 ) )
        print('Medeltemperatur under 10 år ', np.round( np.mean(T),1 ) )
    def uppgift7b():
        import numpy as np
        T = np.loadtxt('T10365.txt')
        #print(T.shape)
        print(f"Maximal temperatur under 10 år kollon {np.argmax(T)%T.shape[1]} rad {np.argmax(T)//T.shape[1]}")#behövs ej förklaras mer än T.shape för att få kollon and row
        print(f"Mean feb {np.mean(T[:,32:60]):.2f}")##behövs ej förklaras index 60 för +1
        print(f"Mean 1985 {np.mean(T[4,:]):.2f}")##behövs ej förklaras indexet 4 motsvarar 1985
    uppgift7b()
def inlämning1():
    print("\n\n")
    #uppgift1()
    #uppgift2()
    #uppgift3()
    #uppgift4()
    #uppgift5()
    #uppgift6()
    uppgift7()

inlämning1()
"""
(c) Använd ett skärminspelningsprogram och spela in en kort video, där du förklarar, rad
för rad, vad de olika kommandona gör i programmet i uppgift 
(b) ovan. Visa också hur du
kör programmet. Videon laddas upp på YouTube och du klipper bara in länken i överst i
din py-fil. Tips: om du skriver kommentarer till varje rad så är det lättare att förklara när
du spelar in videon."""
