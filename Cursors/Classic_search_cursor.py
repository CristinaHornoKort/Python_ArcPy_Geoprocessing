import arcpy

flds = "ESTAB; ADDR; EMP; NAME"

cur = arcpy.SearchCursor( << File path>> , "", "", flds)
for row in cur:
    print row.NAME, row.ESTAB, row.ADDR, row.EMP

del cur