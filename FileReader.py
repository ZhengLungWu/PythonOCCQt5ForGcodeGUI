##from array import *
class Gtype():
    G00=0
    G01=1
    G02=2
    G03=3
    G15=15
    G16=16
    G17=17
    G18=18
    G19=19
    G54=54
    G55=55
    G56=56
    G57=57
    G58=58
    G59=59
    G90=90
    G91=91
    Undef=-1
class Planetype():
    G17='xy'
    G18='zx'
    G19='yz'
    Undef=-1
class OffsetWCS():
    Sys54=0
    Sys55=1
    Sys56=2
    Sys57=3
    Sys58=4
    Sys59=5
    Undef=-1
class OWCSData():
    NR=OffsetWCS()
    index=-1
    def __init__(self,NR,index):
        self.NR=NR
        self.index=index
    
    

class CWj():
    CW=0
    CCW=1
    Undef=-1

class ARCCMD_R:
    PlaneType=Planetype()
    #GType=Gtype.Undef
    CWm=CWj()
    ##G02on=True
    index=-1
    XP=0.0
    YP=0.0
    ZP=0.0
    ##I=0.0
    ##J=0.0
    ##K=0.0
    R=0.0

    def __init__(self,PlaneType,CWm,index,R):
        ##self.GType=GType
        self.CWm=CWm
        self.PlaneType=PlaneType
        self.index=index
        self.R=R      
  
class ARCCMD_IJK:
    PlaneType=Planetype()
    ##GType=Gtype.Undef
    CWm=CWj()
    ##G02on=True
    index=-1
    I=0.0
    J=0.0
    K=0.0
    ##R=0.0

    def __init__(self,PlaneType,CWm,index,I,J,K):
        ##self.GType=GType
        self.CWm=CWm
        self.PlaneType=PlaneType
        self.index=index
        self.I=I
        self.J=J
        self.K=K
          



class Reader:
    G00Line=[]
    G01Line=[]
    ##G01Line=array('i')
    G02Line=[]
    G03Line=[]
    G54Line=[]
    G55Line=[]
    G56Line=[]
    G57Line=[]
    G58Line=[]
    G59Line=[]
    GType=Gtype.Undef
    PlaneType=Planetype()
    ABSMode=True
    WPCSetting=False
    ABSPOS=[]
    INCREC=[]
    G02REC=[]
    G03REC=[]
    OffsetWPCSdata=[]

    def ExamNum(self,char):
        for i in range(10):
            if char==str(i):
                return True
        if char=='E' or char=='e':
            return True
        elif char=='-':
            return True
        elif char=='.':
            return True
        else:
            return False
        
    
        
            

    
    def __init__(self,filePath):
        self.filePath=filePath
        self.Transcript()
    def Transcript(self):
        fileExist=bool(self.filePath)
        if fileExist==True:
            File=open(self.filePath,'r')
            alltext=File.readlines()
            ##AbsPos=array(array('d'))
            for i in range(len(alltext)):
                G02on=False
                G03on=False
                indexofX=-1
                indexofY=-1
                indexofZ=-1
                indexofI=-1
                indexofJ=-1
                indexofK=-1
                indexofT=-1
                indexofXP=-1
                indexofYP=-1
                indexofZP=-1
                indexofR=-1
                indexofA=-1
                indexofB=-1
                indexofC=-1
                for j in range(len(alltext[i])):
                               if alltext[i][j]=='X'or alltext[i][j]=='x':
                                   indexofX=j
                                   if alltext[i][j+1]=='P' or alltext[i][j+1]=='p':
                                       indexofXP=j+1
                                
                               if alltext[i][j]=='Y'or alltext[i][j]=='y':
                                   indexofY=j
                                   if alltext[i][j+1]=='P' or alltext[i][j+1]=='p':
                                       indexofYP=j+1
                               if alltext[i][j]=='Z'or alltext[i][j]=='z':
                                   indexofZ=j
                                   if alltext[i][j+1]=='P' or alltext[i][j+1]=='p':
                                       indexofZP=j+1
                               if alltext[i][j]=='R'or alltext[i][j]=='r':
                                   indexofR=j
                               if alltext[i][j]=='I'or alltext[i][j]=='i':
                                   indexofI=j
                               if alltext[i][j]=='J'or alltext[i][j]=='j':
                                   indexofJ=j
                               if alltext[i][j]=='K'or alltext[i][j]=='k':
                                   indexofK=j
                               if alltext[i][j]=='A'or alltext[i][j]=='a':
                                   indexofA=j
                               if alltext[i][j]=='B'or alltext[i][j]=='b':
                                   indexofB=j
                               if alltext[i][j]=='C'or alltext[i][j]=='c':
                                   indexofC=j
                               if alltext[i][j]=='T'or alltext[i][j]=='t':
                                   indexofT=j

                               if alltext[i][j]=='G' or alltext[i][j]=='g':
                                   if alltext[i][j+1]=='0':
                                       if alltext[i][j+2]=='0':
                                           self.G00Line.append(i)
                                           G03on=False
                                           G02on=False
                                       elif alltext[i][j+2]=='1':
                                           self.G01Line.append(i)
                                           G03on=False
                                           G02on=False
                                       elif alltext[i][j+2]=='2':
                                           self.G02Line.append(i)
                                           G02on=True
                                           G03on=False
                                       elif alltext[i][j+2]=='3':
                                           self.G03Line.append(i)
                                           G03on=True
                                           G02on=False
                                       elif alltext[i][j+2]==' ':
                                           self.G00Line.append(i)
                                           G03on=False
                                           G02on=False
                                   elif alltext[i][j+1]=='1':
                                       if alltext[i][j+2]=='7':
                                           ##GType=Gtype.G17
                                           self.PlaneType=Planetype.G17
                                           
                                       elif alltext[i][j+2]=='8':
                                           ##GType=Gtype.G18
                                           self.PlaneType=Planetype.G18
                                       elif alltext[i][j+2]=='9':
                                           ##GType=Gtype.G19
                                           self.PlaneType=Planetype.G19
                                       elif alltext[i][j+2]==' ':
                                           self.G01Line.append(i)
                                   elif alltext[i][j+1]=='2':
                                       if alltext[i][j+2]==' ':
                                           G02on=True
                                           G03on=False
                                           self.G02Line.append(i)
                                   elif alltext[i][j+1]=='3':
                                       if alltext[i][j+2]==' ':
                                           G03on=True
                                           G02on=False
                                           self.G03Line.append(i)
                                   elif alltext[i][j+1]=='5':
                                       if alltext[i][j+2]=='4':
                                           self.WPCSetting=True
                                          ## GType=Gtype.G54
                                           data=OWCSData(OffsetWCS.Sys54,i)
                                           self.OffsetWPCSdata.append(data)
                                           
                                       elif alltext[i][j+2]=='5':
                                           self.WPCSetting=True
                                           ##GType=Gtype.G55
                                           data=OWCSData(OffsetWCS.Sys55,i)
                                           self.OffsetWPCSdata.append(data)
                                       elif alltext[i][j+2]=='6':
                                           self.WPCSetting=True
                                           ##GType=Gtype.G56
                                           data=OWCSData(OffsetWCS.Sys56,i)
                                           self.OffsetWPCSdata.append(data)
                                       elif alltext[i][j+2]=='7':
                                           self.WPCSetting=True
                                           ##GType=Gtype.G57
                                           data=OWCSData(OffsetWCS.Sys57,i)
                                           self.OffsetWPCSdata.append(data)
                                       elif alltext[i][j+2]=='8':
                                           self.WPCSetting=True
                                           ##GType=Gtype.G58
                                           data=OWCSData(OffsetWCS.Sys58,i)
                                           self.OffsetWPCSdata.append(data)
                                       elif alltext[i][j+2]=='9':
                                           self.WPCSetting=True
                                           ##GType=Gtype.G59
                                           data=OWCSData(OffsetWCS.Sys59,i)
                                           self.OffsetWPCSdata.append(data)
                                   elif alltext[i][j+1]=='9':
                                       if alltext[i][j+2]=='0':
                                           GType=Gtype.G90
                                           ABSmode=True
                                       elif alltext[i][j+2]=='1':
                                           GType=Gtype.G91
                                           ABSmode=False
                                       elif alltext[i][j+2]=='2':
                                           GType=Gtype.G92
                                           ##WPCSetting=True
                                
                SpaceXrec=-1
                SpaceYrec=-1
                SpaceZrec=-1
                ValX=0.0
                ValY=0.0
                ValZ=0.0
                if indexofX!=-1:
                    totalXnum=0
                    breakXnum=-1
                    for j in range(indexofX+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceXrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalXnum+=1
                        else:
                            breakXnum=j
                            break
                    destX=''
                    for k in range(totalXnum):
                        ##destX.append(alltext[i][indexofX+1+k]) ##deal as list
                        destX=destX+alltext[i][indexofX+1+k]  ##deal as string
                    ##print(destX)
                    ValX=float(destX)
                    ##print(ValX)
                if indexofY!=-1:
                    totalYnum=0
                    breakYnum=-1
                    for j in range(indexofY+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceYrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalYnum+=1
                        else:
                            breakYnum=j
                            break
                    destY=''
                    for k in range(totalYnum):

                        destY=destY+alltext[i][indexofY+1+k]  ##deal as string
                    
                    ValY=float(destY)
                if indexofZ!=-1:
                    totalZnum=0
                    breakZnum=-1
                    for j in range(indexofZ+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceZrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalZnum+=1
                        else:
                            breakZnum=j
                            break
                    destZ=''
                    for k in range(totalZnum):

                        destZ=destZ+alltext[i][indexofZ+1+k]  ##deal as string
                    
                    ValZ=float(destZ)       

                SpaceIrec=-1
                SpaceJrec=-1
                SpaceKrec=-1
                ValI=0.0
                ValJ=0.0
                ValK=0.0
                if indexofI!=-1:
                    totalInum=0
                    breakInum=-1
                    for j in range(indexofI+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceIrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalInum+=1
                        else:
                            breakInum=j
                            break
                    destI=''
                    for k in range(totalInum):

                        destI=destI+alltext[i][indexofI+1+k]  ##deal as string
                    
                    ValI=float(destI)
                    
                if indexofJ!=-1:
                    totalJnum=0
                    breakJnum=-1
                    for j in range(indexofJ+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceJrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalJnum+=1
                        else:
                            breakJnum=j
                            break
                    destJ=''
                    for k in range(totalJnum):

                        destJ=destJ+alltext[i][indexofJ+1+k]  ##deal as string
                    
                    ValJ=float(destJ)
                    
                if indexofK!=-1:
                    totalKnum=0
                    breakKnum=-1
                    for j in range(indexofK+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceKrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalKnum+=1
                        else:
                            breakKnum=j
                            break
                    destK=''
                    for k in range(totalKnum):

                        destK=destK+alltext[i][indexofK+1+k]  ##deal as string
                    
                    ValK=float(destK)
                if indexofI!=-1 and indexofJ!=-1 and indexofK==-1:
                    self.PlaneType=Planetype.G17
                elif indexofK!=-1 and indexofJ!=-1 and indexofI==-1:
                    self.PlaneType=Planetype.G19
                elif indexofK!=-1 and indexofI!=-1 and indexofJ==-1:
                    self.PlaneType=Planetype.G18    
                    

                SpaceRrec=-1
                ValR=0.0
                if indexofR!=-1:
                    totalRnum=0
                    breakRnum=-1
                    for j in range(indexofR+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceRrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalRnum+=1
                        else:
                            breakRnum=j
                            break
                    destR=''
                    for k in range(totalRnum):

                        destR=destR+alltext[i][indexofR+1+k]  ##deal as string
                    
                    ValR=float(destR)

                SpaceTrec=-1
                NrT=-1
                if indexofT!=-1:
                    totalTnum=0
                    breakTnum=-1
                    for j in range(indexofT+1,len(alltext[i])):
                        if alltext[i][j]==' ':
                            SpaceTrec=j
                        if self.ExamNum(alltext[i][j])==True:
                            totalTnum+=1
                        else:
                            breakTnum=j
                            break
                    destT=''
                    for k in range(totalTnum):

                        destT=destT+alltext[i][indexofT+1+k]  ##deal as string
                    
                    NrT=int(destT)

                if self.ABSMode==True:
                    coors=[ValX,ValY,ValZ]
                    checks=[indexofX,indexofY,indexofZ]
                    if i==0:
                        for k in range(3):
                            if checks[k]==-1:
                                coors[k]=0.0
                        self.ABSPOS.append(coors)
                        self.INCREC.append(coors)
                        ##print(self.ABSPOS)
                    elif i>0:
                        incs=[0.0,0.0,0.0]
                        for k in range(3):
                            if checks[k]==-1:
                                coors[k]=self.ABSPOS[i-1][k]
                        self.ABSPOS.append(coors)
                        for q in range(3):
                            incs[q]=coors[q]-self.ABSPOS[i-1][q]
                        self.INCREC.append(incs)
                else:##ABSMode==False
                    coors=[ValX,ValY,ValZ]
                    checks=[indexofX,indexofY,indexofZ]
                    if i==0:
                        for k in range(3):
                            if checks[k]==-1:
                                coors[k]=0.0
                        self.ABSPOS.append(coors)
                        self.INCREC.append(coors)
                    elif i>0:
                        TEMP=[0.0,0.0,0.0]
                        for k in range(3):
                            if checks[k]==-1:
                                coors[k]=0.0
                            TEMP[k]=self.ABSPOS[i-1][k]+coors[k]
                        self.ABSPOS.append(TEMP)
                        self.INCREC.append(coors)

                if G02on==True:
                    cw=CWj()
                   
                    if indexofR==-1:
                        G02CMD=ARCCMD_IJK(self.PlaneType,cw.CW,i,ValI,ValJ,ValK)
                    else:
                        G02CMD=ARCCMD_R(self.PlaneType,cw.CW,i,ValR)
                    self.G02REC.append(G02CMD)
                elif G03on==True:
                    cw=CWj()
                   
                    if indexofR==-1:
                        G03CMD=ARCCMD_IJK(self.PlaneType,cw.CCW,i,ValI,ValJ,ValK)
                    else:
       
                        G03CMD=ARCCMD_R(self.PlaneType,cw.CCW,i,ValR)
                    self.G03REC.append(G03CMD)
                            

     

        

if __name__=='__main__':
    a=r"C:\Users\dell\Desktop\NC SAMPLE.txt"

    d=Reader(a)
    print(d.ABSPOS)
    print(d.INCREC)
    print(d.G02Line)
    print(d.G02REC[0].PlaneType)
