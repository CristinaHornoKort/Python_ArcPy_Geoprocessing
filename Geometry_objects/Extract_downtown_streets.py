#----------------------------------------------------------------
#
#Extract (clip) downtown Corvallis streets to a new feature class
#
#----------------------------------------------------------------

import arcpy
arcpy.env.workspace = << Your geodatabase directory >>

pnt = arcpy.Point()
ary = arcpy.Array()

coords = [[1277000.0, 344000.0],[1283000.0, 344000.0],
          [1283000.0, 336000.0],[1277000.0, 336000.0]]

for coord in coords:
    pnt.X = coord[0]
    pnt.Y = coord[1]
    ary.add(pnt)

polygon = arcpy.Polygon(ary)

arcpy.Clip_analysis("StPaved", polygon, "DowntownStreets")