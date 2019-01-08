import itertools
class Gear(object):
    def __init__(self,teeth,pd,od):
        self.teeth=teeth
        self.pd=pd
        self.od=od
    def __repr__(self):
        #return "Gear qualities:""\nTeeth Count: "+str(self.teeth)+"\nOuter Diameter: "+str(self.od)+"\nPitch Diameter: "+str(self.pd)
        return str(self.teeth)
    def getod(self):
        return self.od
t20=Gear(20,1,1.1)
t24=Gear(24,1.2,1.3)
t30=Gear(30,1.5,1.6)
t34=Gear(34,1.8,1.9)

if __name__=="__main__":
    done=False
    while done != True:
        r=int(input("How many gears are you using?"))
        print(t20)
        gearlst=[t20.od,t24.od,t30.od,t34.od]
        final=list(itertools.combinations(gearlst,r))
        print(final)
        geartrain=list(map(sum,final))
        print(geartrain)
        cont=input("would you like to continue(y or n)")
        if cont=="y" or cont=="Y":
            done=False
        else:
            done=True
