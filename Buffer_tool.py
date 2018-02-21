#--------------------------------------------------------------------------------
#
#el siguiente script ejecuta la herramienta de geoprocesamiento Buffer a los
#elementos contenidos dentro de una capa de entidad a una distancia especificada
#
#--------------------------------------------------------------------------------

import arcpy

arcpy.env.workspace = << Your geodatabase directory>>

# overwrite if the file allready exists
arcpy.env.overwriteOutput = True

# 3 arguments: Name of the input layer, name of the output layer, buffer distance 
arcpy.Buffer_analysis("InputLayerName", "BufferLayerResult", "1000 feet")

print "Script completed"
