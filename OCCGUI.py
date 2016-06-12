from OCC.GeomAPI import GeomAPI_PointsToBSpline
from OCC.TColgp import TColgp_Array1OfPnt
import math
#import UI

##display, start_display, add_menu, add_function_to_menu = init_display()
from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_Pnt
#from OCC.Geom import Geom_Line
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from FileReader import Reader

from GcodeAnalyser import G02EXE,G03EXE

display, start_display, add_menu, add_function_to_menu = init_display()


#def DisplayLines(psr):
    ##psr=Reader.ABSPOS
   # mylines=[]
    #p1s=[]
    #line_dirs=[]
    #for i in range(1,len(psr)):
     #   p1s.append(gp_Pnt(psr[i][0],psr[i][1],psr[i][2]))
      #  q=gp_Dir(psr[i][0]-psr[i-1][0],psr[i][1]-psr[i-1][1],psr[i][2]-psr[i-1][2])
       # line_dirs.append(q)

    #for i in range(len(p1s)):
        #c=Geom_Line(p1s[i],line_dirs[i]).Lin()
        
        #c=BRepBuilderAPI_MakeEdge(c)
        #c.Build()
        #c=c.Shape()
        #mylines.append(c)
 #   for i in range(len(psr)-1):
        
  #      array=TColgp_Array1OfPnt(1,2)
   #     array.SetValue(1,gp_Pnt(psr[i][0],psr[i][1],psr[i][2]))
    #    array.SetValue(2,gp_Pnt(psr[i+1][0],psr[i+1][1],psr[i+1][2]))
     #   bspline2 = GeomAPI_PointsToBSpline(array).Curve()
      #  path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()

class Display:  
    def DisplayG00Line(coor1,coor2):
            coors=[coor1,[coor2[0],coor1[1],coor1[2]],[coor2[0],coor2[1],coor1[2]],coor2]
            for i in range(3):
                array=TColgp_Array1OfPnt(1,2)
                array.SetValue(1,gp_Pnt(coors[i][0],coors[i][1],coors[i][2]))
                array.SetValue(2,gp_Pnt(coors[i+1][0],coors[i+1][1],coors[i+1][2]))
                bspline2 = GeomAPI_PointsToBSpline(array).Curve()
                path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()
                display.DisplayColoredShape(path_edge,'YELLOW')



    def DisplayG01Line(coor1,coor2):
            array=TColgp_Array1OfPnt(1,2)
            array.SetValue(1,gp_Pnt(coor1[0],coor1[1],coor1[2]))
            array.SetValue(2,gp_Pnt(coor2[0],coor2[1],coor2[2]))
            bspline2 = GeomAPI_PointsToBSpline(array).Curve()
            path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()
            display.DisplayColoredShape(path_edge,'GREEN')


    def DisplayG02Arc(coor1,coor2,ARCCMD):
            f=G02EXE(coor1,coor2,ARCCMD)
            print(f)
            pty=f[0]
            center=f[1]
            radius=f[2]
            startA=f[3]
            endA=f[4]
            if endA-startA>=0:
                endA=-2*math.pi+endA

            dis=endA-startA
            dis=dis/30

            array=TColgp_Array1OfPnt(1,30)
            if pty=='xy':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(radius*math.cos(startA+dis*i)+center[0],radius*math.sin(startA+dis*i)+center[1],coor1[2]))
                array.SetValue(30,gp_Pnt(radius*math.cos(endA)+center[0],radius*math.sin(endA)+center[1],coor1[2]))

            elif pty=='zx':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(radius*math.sin(startA+dis*i)+center[1],coor1[1],radiud*math.cos(startA+dis*i)+center[0]))
                array.SetValue(30,gp_Pnt(radius*math.sin(endA)+center[1],coor1[1],radiud*math.cos(endA)+center[0]))

            elif pty=='yz':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(coor1[0],radiud*math.cos(startA+dis*i)+center[0],radius*math.sin(startA+dis*i)+center[1]))
                array.SetValue(30,gp_Pnt(coor1[0],radiud*math.cos(endA)+center[0],radius*math.sin(endA)+center[1]))

            bspline2 = GeomAPI_PointsToBSpline(array).Curve()
            path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()
            display.DisplayColoredShape(path_edge,'RED')
                
    def DisplayG03Arc(coor1,coor2,ARCCMD):
            f=G03EXE(coor1,coor2,ARCCMD)
            pty=f[0]
            center=f[1]
            radius=f[2]
            startA=f[3]
            endA=f[4]
            if endA-startA<=0:
                startA=-2*math.pi+startA

            dis=endA-startA
            dis=dis/30

            array=TColgp_Array1OfPnt(1,30)
            if pty=='xy':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(radius*math.cos(startA+dis*i)+center[0],radius*math.sin(startA+dis*i)+center[1],coor1[2]))
                array.SetValue(30,gp_Pnt(radius*math.cos(endA)+center[0],radius*math.sin(endA)+center[1],coor1[2]))

            elif pty=='zx':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(radius*math.sin(startA+dis*i)+center[1],coor1[1],radiud*math.cos(startA+dis*i)+center[0]))
                array.SetValue(30,gp_Pnt(radius*math.sin(endA)+center[1],coor1[1],radiud*math.cos(endA)+center[0]))

            elif pty=='yz':
                for i in range(29):
                    array.SetValue(i+1,gp_Pnt(coor1[0],radiud*math.cos(startA+dis*i)+center[0],radius*math.sin(startA+dis*i)+center[1]))
                array.SetValue(30,gp_Pnt(coor1[0],radiud*math.cos(endA)+center[0],radius*math.sin(endA)+center[1]))

            bspline2 = GeomAPI_PointsToBSpline(array).Curve()
            path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()
            display.DisplayColoredShape(path_edge,'BLUE')                             
        
            
        
    






def ShowGPath(Reader):
        G00Line=Reader.G00Line
        G01Line=Reader.G01Line
        G02Line=Reader.G02Line
        G03Line=Reader.G03Line
        abspos=Reader.ABSPOS
        #print(abspos)
        G02rec=Reader.G02REC
        print(Reader.G02REC)
        G03rec=Reader.G03REC

        for i in range(1,len(abspos)):
            for j in range (len(G00Line)):
                if G00Line[j]==i:
                    Display.DisplayG00Line(abspos[i-1],abspos[i])
            for j in range(len(G01Line)):
                if G01Line[j]==i:
                    Display.DisplayG01Line(abspos[i-1],abspos[i])
            for j in range(len(G02Line)):
                if G02Line[j]==i:
                    #print('yyy')
                    for k in range (len(G02rec)):
                        if G02rec[k].index==i:
                            #print('xxx')
                            print(G02rec[k].PlaneType)
                            Display.DisplayG02Arc(abspos[i-1],abspos[i],G02rec[k])
            for j in range(len (G03Line)):
                if G03Line[j]==i:
                    for k in range(len(G03rec)):
                        if G03rec[k].index==i:
                            Display.DisplayG03Arc(abspos[i-1],abspos[i],G03rec[k])
                            
                    
        display.View_Iso()
        display.FitAll()
        start_display() 


        
        






        
        #display.DisplayShape(path_edge)
       # display.DisplayColoredShape(path_edge,'YELLOW')
   

    



