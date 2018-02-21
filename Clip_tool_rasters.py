#--------------------------------------------------------------------------------
#
#el siguiente script ejecuta la herramienta de geoprocesamiento Clip para 
#recortar un conjunto de rasters utilizando la extension de otro raster
#
#--------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = r'<< your directory >>'

desc = arcpy.Describe(" << path to your clip raster here >> ")
rasExtent = desc.extent
ras_List = arcpy.ListRasters()

for name in ras_List:
    arcpy.Clip_management(name, str(rasExtent), "{}_clip".format(name))

#Alternate way to acces the Clip_management geoprocessing tool is to
# specify the toolbox alias and them the name in the form of:
# arcpy.<toolbox alias>.<toolname>()
# Alternate code for line 16 above is:
#arcpy.management.Clip(name, str(rasExtent), "{}_clip".format(name))

print "Script completed"
