import math


from FileReader import *


class G00EXE():
   
    def __init__(self):
        super().__init__()
    
    
    def __new__(cls,StartCoor,endCoor):
        
       
        return[StartCoor,[endCoor[0],StartCoor[1],StartCoor[2]],[endCoor[0],endCoor[1],StartCoor[2]],endCoor]
    
class G01EXE():
    def __new__(cls,startCoor,endCoor):
        return[startCoor,endCoor]

class G02EXE():
    center=[]
    radius=0.0
    startAngle=0.0
    endAngle=0.0
    def __new__(cls,coor1,coor2,ARCCMD):
        if type(ARCCMD) == ARCCMD_R:
            
            print('R')
            pty= ARCCMD.PlaneType
            print(pty)
            i=ARCCMD.index
            startCoor=[]
            endCoor=[]
            R=ARCCMD.R
            print(R)
      
            if pty==Planetype.G17:
                  
                startCoor=[coor1[0],coor1[1]]
                endCoor=[coor2[0],coor2[1]]
            elif pty==Planetype.G18:
                startCoor=[coor1[2],coor1[0]]
                endCoor=[coor2[2],coor2[0]]
            else: ##g19
                startCoor=[coor1[1],coor1[2]]
                endCoor=[coor2[1],coor2[2]]

            vec1=[endCoor[0]-startCoor[0],endCoor[1]-startCoor[1]]
            len1=math.sqrt(vec1[0]*vec1[0]+vec1[1]*vec1[1])
            A=0.0

            a=math.acos(vec1[0]/len1)
            b=math.asin(vec1[1]/len1)
            if a>=0 and b>=0:
                A=a
            elif a>=0 and b<=0:
                A=2*math.pi-a
            elif a<0 and b>0:
                A=math.pi-a
            elif a<0 and b<0:
                A=math.pi+a
            r=0.0
            if R>=0:
                r=R
            else:
                r=-R
                
            B=math.acos((len1/2)/r)
            #print(A,B)

            c1=[r*math.cos(A+B)+startCoor[0],r*math.sin(A+B)+startCoor[1]]
            c2=[r*math.cos(A-B)+startCoor[0],r*math.sin(A-B)+startCoor[1]]
            #print(c1)
            #print(c2)

            startInc1=[startCoor[0]-c1[0],startCoor[1]-c1[1]]
            startInc2=[startCoor[0]-c2[0],startCoor[1]-c2[1]]

            endInc1=[endCoor[0]-c1[0],endCoor[1]-c1[1]]
            endInc2=[endCoor[0]-c2[0],endCoor[1]-c2[1]]

            startAng1=0.0
            #print(r)
            #print(startInc1[0])

            a=math.acos(startInc1[0]/r)
            b=math.asin(startInc1[1]/r)
            if a>=0 and b>=0:
                startAng1=a
            elif a>=0 and b<=0:
                startAng1=2*math.pi-a
            elif a<0 and b>0:
                startAng1=math.pi+a
            elif a<0 and b<0:
                startAng1=math.pi-a

            startAng2=0.0    

            a=math.acos(startInc2[0]/r)
            b=math.asin(startInc2[1]/r)
            if a>=0 and b>=0:
                startAng2=a
            elif a>=0 and b<=0:
                startAng2=2*math.pi-a
            elif a<0 and b>0:
                startAng2=math.pi+a
            elif a<0 and b<0:
                startAng2=math.pi-a    

            endAng1=0.0
            print(endInc1[0])

            a=math.acos(endInc1[0]/r)
            b=math.asin(endInc1[1]/r)
            if a>=0 and b>=0:
                endAng1=a
            elif a>=0 and b<=0:
                endAng1=2*math.pi-a
            elif a<0 and b>0:
                endAng1=math.pi+a
            elif a<0 and b<0:
                endAng1=math.pi-a

            endAng2=0.0    

            a=math.acos(endInc2[0]/r)
            b=math.asin(endInc2[1]/r)
            if a>=0 and b>=0:
                endAng2=a
            elif a>=0 and b<=0:
                endAng2=-a
            elif a<0 and b>0:
                endAng2=math.pi+a
            elif a<0 and b<0:
                endAng2=math.pi-a

            if R>0:
                if endAng1-startAng1>0 and endAng1-startAng1<math.pi: 
                        cls.endAngle=endAng2
                        cls.startAngle=startAng2
                        cls.center=c2
                elif endAng1-startAng1>math.pi and endAng1-startAng1<2*math.pi: 
                        cls.endAngle=endAng1
                        cls.startAng=startAng1
                        cls.center=c1
                elif endAng1-startAng1<0 and endAng1-startAng1>-math.pi:
                        cls.endAngle=endAng1
                        cls.startAng=startAng1
                        cls.center=c1
                elif endAng1-startAng1>-2*math.pi and endAng1-startAng1<-math.pi:
                        cls.endAngle=endAng2
                        cls.startAngle=startAng2
                        cls.center=c2

                
            elif R<0:
                if endAng1-startAng1>=0 and endAng1-startAng1<=math.pi: 
                        cls.endAngle=endAng1
                        cls.startAngle=startAng1
                        cls.center=c1
                elif endAng1-startAng1>=math.pi and endAng1-startAng1<=2*math.pi: 
                        cls.endAngle=endAng2
                        cls.startAng=startAng2
                        cls.center=c2
                elif endAng1-startAng1<=0 and endAng1-startAng1>=-math.pi:
                        cls.endAngle=endAng2
                        cls.startAng=startAng2
                        cls.center=c2
                elif endAng1-startAng1>=-2*math.pi and endAng1-startAng1<=-math.pi:
                        cls.endAngle=endAng1
                        cls.startAngle=startAng1
                        cls.center=c1
            cls.radius=r
            return[pty,cls.center,cls.radius,cls.startAngle,cls.endAngle]    
   
        elif type(ARCCMD) == ARCCMD_IJK:
            print('IJK')
            pty= ARCCMD.PlaneType
            
            i=ARCCMD.index
            startCoor=[0.0,0.0]
            endCoor=[0.0,0.0]
            I=ARCCMD.I
            J=ARCCMD.J
            K=ARCCMD.K
            center=[0.0,0.0]
            radius=0.0


                  
            if pty==Planetype.G17:
                  
                startCoor=[coor1[0],coor1[1]]
                endCoor=[coor2[0],coor2[1]]
                radius=math.sqrt(I*I+J*J)
                center=[startCoor[0]+I,startCoor[1]+J]
                
            elif pty==Planetype.G18:
                startCoor=[coor1[2],coor1[0]]
                endCoor=[coor2[2],coor2[0]]
                radius=math.sqrt(K*K+I*I)
                center=[startCoor[0]+K,startCoor[1]+I]
            else: ##g19
                startCoor=[coor1[1],coor1[2]]
                endCoor=[coor2[1],coor2[2]]
                radius=math.sqrt(J*J+K*K)
                center=[startCoor[0]+J,startCoor[1]+K]



            v1=[startCoor[0]-center[0],startCoor[1]-center[1]]
            v2=[endCoor[0]-center[0],endCoor[1]-center[1]]

            startAng1=0.0
            print(i,I,J,K,v1[0],radius)
            

            a=math.acos(v1[0]/radius)
            b=math.asin(v1[1]/radius)
            if a>=0 and b>=0:
                startAng1=a
            elif a>=0 and b<=0:
                startAng1=2*math.pi-a
            elif a<0 and b>0:
                startAng1=math.pi-a
            elif a<0 and b<0:
                startAng1=math.pi+a
            cls.startAngle=startAng1
            

            endAng1=0.0
            print(endCoor,center, v2[0],v2[1]/radius)

            p1=v2[0]/radius
            p2=v2[1]/radius
            if p1>1 and p1<1.01:
                p1=1
            if p2>1 and p2<1.01:
                p2=1
            if p1<-1 and p1>-1.01:
                p1=-1
            if p2<-1 and p2>-1.01:
                p2=-1
        

            a=math.acos(p1)
            b=math.asin(p2)
            
            if a>=0 and b>=0:
                endAng1=a
            elif a>=0 and b<=0:
                endAng1=2*math.pi-a
            elif a<0 and b>0:
                endAng1=math.pi-a
            elif a<0 and b<0:
                endAng1=math.pi+a
            cls.endAngle=endAng1
            cls.radius=radius
            cls.center=center

            return[pty,cls.center,cls.radius,cls.startAngle,cls.endAngle]


            

                
                



            
        else:
            print('wrong!')

class G03EXE():
    center=[]
    radius=0.0
    startAngle=0.0
    endAngle=0.0
    def __new__(cls,coor1,coor2,ARCCMD):
        if type(ARCCMD) == ARCCMD_R:
            print('R')
            pty= ARCCMD.PlaneType
            
            i=ARCCMD.index
            startCoor=[0.0,0.0]
            endCoor=[0.0,0.0]
            R=ARCCMD.R
           
      
            if pty==Planetype.G17:
                  
                startCoor=[coor1[0],coor1[1]]
                endCoor=[coor2[0],coor2[1]]
            elif pty==Planetype.G18:
                startCoor=[coor1[2],coor1[0]]
                endCoor=[coor2[2],coor2[0]]
            else: ##g19
                startCoor=[coor1[1],coor1[2]]
                endCoor=[coor2[1],coor2[2]]



            vec1=[endCoor[0]-startCoor[0],endCoor[1]-startCoor[1]]
            len1=math.sqrt(vec1[0]*vec1[0]+vec1[1]*vec1[1])
            A=0.0

            a=math.acos(vec1[0]/len1)
            b=math.asin(vec1[1]/len1)
            if a>=0 and b>=0:
                A=a
            elif a>=0 and b<=0:
                A=2*math.pi-a
            elif a<0 and b>0:
                A=math.pi+a
            elif a<0 and b<0:
                A=math.pi-a
            r=0.0
            if R>=0:
                r=R
            else:
                r=-R
                
            B=math.acos(len1/(2*r))    

            c1=[r*math.cos(A+B)+startCoor[0],r*math.sin(A+B)+startCoor[1]]
            c2=[r*math.cos(A-B)+startCoor[0],r*math.sin(A-B)+startCoor[1]]

            startInc1=[startCoor[0]-c1[0],startCoor[1]-c1[1]]
            startInc2=[startCoor[0]-c2[0],startCoor[1]-c2[1]]

            endInc1=[endCoor[0]-c1[0],endCoor[1]-c1[1]]
            endInc2=[endCoor[0]-c2[0],endCoor[1]-c2[1]]

            startAng1=0.0    

            a=math.acos(startInc1[0]/r)
            b=math.asin(startInc1[1]/r)
           
            startAng2=0.0    

            a=math.acos(startInc2[0]/r)
            b=math.asin(startInc2[1]/r)
            if a>=0 and b>=0:
                startAng2=a
            elif a>=0 and b<=0:
                startAng2=2*math.pi-a
            elif a<0 and b>0:
                startAng2=math.pi+a
            elif a<0 and b<0:
                startAng2=math.pi-a    

            endAng1=0.0    

            a=math.acos(endInc1[0]/r)
            b=math.asin(endInc1[1]/r)
            if a>=0 and b>=0:
                endAng1=a
            elif a>=0 and b<=0:
                endAng1=2*math.pi-a
            elif a<0 and b>0:
                endAng1=math.pi+a
            elif a<0 and b<0:
                endAng1=math.pi-a

            endAng2=0.0    

            a=math.acos(endInc2[0]/r)
            b=math.asin(endInc2[1]/r)
            if a>=0 and b>=0:
                endAng2=a
            elif a>=0 and b<=0:
                endAng2=2*math.pi-a
            elif a<0 and b>0:
                endAng2=math.pi+a
            elif a<0 and b<0:
                endAng2=math.pi-a

            if R>0:
                if endAng1-startAng1>0 and endAng1-startAng1<math.pi: 
                        cls.endAngle=endAng1
                        cls.startAngle=startAng1
                        cls.center=c1
                elif endAng1-startAng1>math.pi and endAng1-startAng1<2*math.pi: 
                        cls.endAngle=endAng2
                        cls.startAng=startAng2
                        cls.center=c2
                elif endAng1-startAng1<0 and endAng1-startAng1>-math.pi:
                        cls.endAngle=endAng2
                        cls.startAng=startAng2
                        cls.center=c2
                elif endAng1-startAng1>-2*math.pi and endAng1-startAng1<-math.pi:
                        cls.endAngle=endAng1
                        cls.startAngle=startAng1
                        cls.center=c1

                
            elif R<0:
                if endAng1-startAng1>=0 and endAng1-startAng1<=math.pi: 
                        cls.endAngle=endAng2
                        cls.startAngle=startAng2
                        cls.center=c2
                elif endAng1-startAng1>=math.pi and endAng1-startAng1<=2*math.pi: 
                        cls.endAngle=endAng1
                        cls.startAng=startAng1
                        cls.center=c1
                elif endAng1-startAng1<=0 and endAng1-startAng1>=-math.pi:
                        cls.endAngle=endAng1
                        cls.startAng=startAng1
                        cls.center=c1
                elif endAng1-startAng1>=-2*math.pi and endAng1-startAng1<=-math.pi:
                        cls.endAngle=endAng2
                        cls.startAngle=startAng2
                        cls.center=c2
            else:#R==0
                print('error')
                    
            cls.radius=r
            return[pty,cls.center,cls.radius,cls.startAngle,cls.endAngle] 

             
        elif type(ARCCMD) == ARCCMD_IJK:
            print('IJK')
            pty= ARCCMD.PlaneType
            
            i=ARCCMD.index
            startCoor=[0.0,0.0]
            endCoor=[0.0,0.0]
            I=ARCCMD.I
            J=ARCCMD.J
            K=ARCCMD.K
            center=[0.0,0.0]
            radius=0.0

            if pty==Planetype.G17:
                  
                startCoor=[coor1[0],coor1[1]]
                endCoor=[coor2[0],coor2[1]]
                radius=math.sqrt(I*I+J*J)
                center=[startCoor[0]+I,startCoor[1]+J]
                
            elif pty==Planetype.G18:
                startCoor=[coor1[2],coor1[0]]
                endCoor=[coor2[2],coor2[0]]
                radius=math.sqrt(K*K+I*I)
                center=[startCoor[0]+K,startCoor[1]+I]
            else: ##g19
                startCoor=[coor1[1],coor1[2]]
                endCoor=[coor2[1],coor2[2]]
                radius=math.sqrt(J*J+K*K)
                center=[startCoor[0]+J,startCoor[1]+K]



            v1=[startCoor[0]-center[0],startCoor[1]-center[1]]
            v2=[endCoor[0]-center[0],endCoor[1]-center[1]]

            startAng1=0.0    

            a=math.acos(v1[0]/radius)
            b=math.asin(v1[1]/radius)
            if a>=0 and b>=0:
                startAng1=a
            elif a>=0 and b<=0:
                startAng1=2*math.pi-a
            elif a<0 and b>0:
                startAng1=math.pi+a
            elif a<0 and b<0:
                startAng1=math.pi-a
            cls.startAngle=startAng1
            

            endAng1=0.0

            p1=v2[0]/radius
            p2=v2[1]/radius
            if p1>1 and p1<1.01:
                p1=1
            if p2>1 and p2<1.01:
                p2=1
            if p1<-1 and p1>-1.01:
                p1=-1
            if p2<-1 and p2>-1.01:
                p2=-1
        
            print(i,p1,p2)

            a=math.acos(p1)
            b=math.asin(p2)
            if a>=0 and b>=0:
                endAng1=a
            elif a>=0 and b<=0:
                endAng1=2*math.pi-a
            elif a<0 and b>0:
                endAng1=math.pi+a
            elif a<0 and b<0:
                endAng1=math.pi-a
            cls.endAngle=endAng1


            cls.center=center
            cls.radius=radius
            

            return[pty,cls.center,cls.radius,cls.startAngle,cls.endAngle]


            
        else:
            print('wrong!')
    





#start=[0,0,0]
#end=[100,200,300]
#g=ARCCMD_R(Planetype.G17,CWj.CW,3,100)

#a=r"C:\Users\dell\Desktop\NC SAMPLE.txt"
#d=Reader(a)

#cc=G01EXE(start,end)
#cd=G02EXE(d.ABSPOS,g)

#print(cd)
