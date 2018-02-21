#-------------------------------------------------------------------------------------
#
#Read text file of field values, populate existing feature class using da InsertCursor
#
#-------------------------------------------------------------------------------------

# Import the ArcPy module and time module
import arcpy
import time

# Set the current workspace path
arcpy.env.workspace = << Your directory >>

# Capture CPU seconds
startTime = time.clock()
# Obtain current year value
yr = time.localtime().tm_year

# Variable assignments
featClass = "MajorAttractions"
fld1, fld2, fld3, fld4, fld5, fld6, fld7, fld8 = 'NAME', 'ESTAB', 'ADDR', \
                                                 'CITYNM', 'ZIP', 'EMP', \
                                                 'ACRES','SHAPE@XY'
i = 0

# Open text file in read mode
f = file( <<File path >>, "r")
line = f.readline()  # Header line

# Establish da InsertCursor on feature class.
c = arcpy.da.InsertCursor(featClass, (fld1, fld2, fld3, fld4, fld5, fld6,
                                     fld7, fld8))
# Loop through lines in text file
for line in f.readlines():
    # Obtain list of values from current line
    row = line.split(",")
    # Strip off end of line character from last item in list
    yVal = row[9]
    yVal.rstrip()
        
    # float needed for X&Y values, X&Y passed as tuple to SHAPE@XY token
    xyVal = (float(row[8]), float(yVal))
    c.insertRow((row[1], row[2], row[3], row[4], row[5], row[6], row[7], xyVal))
    i += 1
    
endTime = time.clock()
elapsedTime = endTime - startTime
print "Elapsed time: {0} to insert {1} rows".format(elapsedTime, i)

# Close file and cursor
f.close()
del c