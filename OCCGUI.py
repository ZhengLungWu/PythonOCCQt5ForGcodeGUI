from OCC.GeomAPI import GeomAPI_PointsToBSpline
from OCC.TColgp import TColgp_Array1OfPnt


##display, start_display, add_menu, add_function_to_menu = init_display()
from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_Pnt, gp_Dir
from OCC.Geom import Geom_Line
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from FileReader import Reader

display, start_display, add_menu, add_function_to_menu = init_display()


def DisplayLines(psr):
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
    for i in range(len(psr)-1):
        
        array=TColgp_Array1OfPnt(1,2)
        array.SetValue(1,gp_Pnt(psr[i][0],psr[i][1],psr[i][2]))
        array.SetValue(2,gp_Pnt(psr[i+1][0],psr[i+1][1],psr[i+1][2]))
        bspline2 = GeomAPI_PointsToBSpline(array).Curve()
        path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()               


        
        #display.DisplayShape(path_edge)
        display.DisplayColoredShape(path_edge,'YELLOW')
    display.View_Iso()
    display.FitAll()
    start_display()

    



