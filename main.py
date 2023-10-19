
# Name: Append Tool
# Description: Migrate the input File Geodatabase (FGDB) into the output File Geodatabase (FGDB)
# Author: Shovon, Mahmud
# Date: 18102023
# Dependecny: Python clone version of Arcgis pro 3,

# Import system modules 
import arcpy
import os

# Get current working directory
current_working_directory = os.getcwd()
print(current_working_directory)
# Set environment settings
arcpy.env.workspace = current_working_directory
arcpy.env.overwriteOutput = True


print('Enter Input FGDB path:')
Input_FGDB_path = input()
print('Input FGDB path, ' + Input_FGDB_path)

print('Enter Target FGDB path:')
Target_FGDB_path = input()
print('Target FGDB path, ' + Target_FGDB_path)

#field mapping between input FC and target FC
#Fixed Mismatch field and rest field will be same
def fieldmapping(inFeature,outFeature):
    iFields = [field.name for field in arcpy.ListFields(inFeature) if field.name not in ("REFNum", "Water_CATCH")] 
    fieldMappings = arcpy.FieldMappings()
    fieldMappings.addTable(outFeature)
    fieldMappings.addTable(inFeature)

    fields_to_be_map = []
    fields_to_be_map.append(('ReferenceNumber', 'REFNum')) 
    fields_to_be_map.append(('WaterCatchment', 'Water_CATCH'))

    for fldmap in fields_to_be_map:
        field_to_map_index = fieldMappings.findFieldMapIndex(fldmap[0])
        field_to_map = fieldMappings.getFieldMap(field_to_map_index)
        field_to_map.addInputField(inFeature, fldmap[1])
        fieldMappings.replaceFieldMap(field_to_map_index, field_to_map)
    return  fieldMappings  

# Set variables
#Input_FGDB_path=r"D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\gdb\InputPolygonGDB.gdb"
#Target_FGDB_path =r"D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\gdb\TargetPolygonGDB.gdb"
InputPolygonFC=Input_FGDB_path+"\InputPolygonFC"
TargetPolygonFC=Target_FGDB_path+"\TargetPolygonFC"
#fieldMappings = r'ReferenceNumber "Test Field" true true false 255 Text 0 0,First,#,Input Polygon,REFNum,0,255;AccuracyStatus "Accuracy Status" true true false 255 Text 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,AccuracyStatus,0,255;State "State" true true false 255 Text 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,State,0,255;Enabled "Enabled" true true false 2 Short 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,Enabled,-1,-1;Remarks "Remarks" true true false 255 Text 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,Remarks,0,255;Diameter "Diameter" true true false 8 Double 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,Diameter,-1,-1;BaseThickness "Base Thickness" true true false 4 Long 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,BaseThickness,-1,-1;ChamberDimension1 "Chamber Dimension 1" true true false 4 Long 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,ChamberDimension1,-1,-1;ChamberDimension2 "Chamber Dimension 2" true true false 4 Long 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,ChamberDimension2,-1,-1;WaterCatchment "Water Catchment" true true false 255 Text 0 0,First,#,Input Polygon,Water_CATCH,0,255;PlantCode "PlantCode" true true false 2 Short 0 0,First,#,D:\Worspace_ArcGISPro\projects\Data_Migration_SG\New folder\test_gdb\InputPolygonGDB.gdb\InputPolygonFC,PlantCode,-1,-1'
fieldMappings=fieldmapping(InputPolygonFC,TargetPolygonFC)
expression="""REFNum LIKE '%SP%' AND CHAR_LENGTH("REFNum") = 8"""


#Cheking files: If input and target files exists in the path
#If files are exist then execute the append tool
if arcpy.Exists(InputPolygonFC) and arcpy.Exists(TargetPolygonFC):
    print("Running...")

    result=arcpy.management.Append(
    inputs=InputPolygonFC,
    target=TargetPolygonFC,
    schema_type="NO_TEST",
    field_mapping=fieldMappings,
    subtype="",
    expression=expression,
    update_geometry="NOT_UPDATE_GEOMETRY" 
)
    print(arcpy.GetMessages())


else:
    arcpy.AddError("{0} or {1} is not found.".format(InputPolygonFC,TargetPolygonFC))
    

