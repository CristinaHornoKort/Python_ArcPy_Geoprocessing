#------------------------------------------------------------------------------
#
#This script buffers points by 1000 ft, polygons by -750 ft, and polylines by 500 ft, 
#using the shapeType Describe property from each feature class in a geodatabase
#
#------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = << My geodatabse directory >>

fc_list = arcpy.ListFeatureClasses()
for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType == "Point":
        buffDist = '1000 feet'
    elif desc.shapeType == "Polyline":
        buffDist = '500 feet'
    elif desc.shapeType == "Polygon":
        buffDist = '-750 feet'
    arcpy.Buffer_analysis(in_features = featClass,
                    out_feature_class = featClass + "_Buff",
                    buffer_distance_or_field = buffDist)

print "Script completed"
