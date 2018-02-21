#------------------------------------------------------------------------------------
#
#el siguiente script documenta las propiedades de los campos de una clase de entidad
#e imprime los resultados en un archivo de texto
#
#------------------------------------------------------------------------------------


#import required modules
import arcpy
import os

#set workspace
wksp = << Your directory >>
arcpy.env.workspace = os.path.join(wksp, << Your geodatabase's name >>)

#create list of fields from feature class
field_list = arcpy.ListFields(<< Name of your File >>)
#example ("MyTxtFile")

#open new text file and add header lines
txtFile = open(os.path.join(wksp, << Name of your .txt File >>), "w")
#example ("MyTxtFile.txt")
txtFile.write("Field information" + "\n")
txtFile.write("-------------------------------------" + "\n")
#loop through list of fields
for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(
         field.name, field.type, field.length)
	#write each field's properties to text file
    txtFile.write(line)

#close text file
txtFile.close()
print "Script completed"
