#--------------------------------------------------
#
#Create Point, Array, Polyline and Polygon objects
#
#--------------------------------------------------

import arcpy

point = arcpy.Point(2000, 1000)
print "Point X: {0}, Y: {1}".format(point.X, point.Y)

# Step 1 - item i.
pnt = arcpy.Point()
ary = arcpy.Array()

coords = [[100, 200],[200, 400],[300, 600],[600, 800],[500, 700]]
for coord in coords:
    pnt.X = coord[0]
    pnt.Y = coord[1]
    ary.add(pnt)

# Step 1 - item k.
polyLine = arcpy.Polyline(ary)
print "Number of points: {0}".format(polyLine.pointCount)

# Step 1  - item m.
polygon = arcpy.Polygon(ary)
print "Number of points: {0}".format(polygon.pointCount)