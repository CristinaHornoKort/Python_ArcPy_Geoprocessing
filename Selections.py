#------------------------------------------------------------------------------
#
#Create new Maritime climate and Historic Attractions layer
#Determine the historic attractions within the maritime climate
#and copy the results to a new feature class
#
#------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = << Your geodatabase directory >>

#Add field delimiters to be used in SQL expressions
newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"TYPE")
newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"ESTAB")

#Join SQL expressions 
# TYPE = 'Maritime'
# ESTAB > 0 and ESTAB < 1956
maritimeSQLExp = newField1 + " = " + "'Maritime'"
historicSQLExp = newField2 + " > 0 and " + newField2 + " < 1956"

#Create feature layers:
#MakeFeatureLayer_management("in_features", "out_layer", where_clause)
arcpy.MakeFeatureLayer_management("Climate", "MaritimeLyr", maritimeSQLExp)
arcpy.MakeFeatureLayer_management("MajorAttractions", "HistoricLyr", historicSQLExp)

#Spatial selection to found Historic Attractions included in Maritime Climate features
#SelectLayerByLocation_management("in_layer", "overlay_type", "select_features", "search_distance", "selection_type")
arcpy.SelectLayerByLocation_management("HistoricLyr", "COMPLETELY_WITHIN", "MaritimeLyr", "", "NEW_SELECTION")

#count number of features returned in tool results
featCount = arcpy.GetCount_management("HistoricLyr")
print "Number of historic features selected: {}".format(featCount)

#Create new feature class from results
#CopyFeatures_management("in_features", "out_feature_class")
arcpy.CopyFeatures_management("HistoricLyr", "MaritimeAttractions")

#delete feature layers from memory
arcpy.Delete_management("MaritimeLyr")
arcpy.Delete_management("HistoricLyr")

print "Script completed"
