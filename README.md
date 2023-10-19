# Data Migration Tool

ArcPy based Python script to migrate the input File Geodatabase (FGDB) into the output File Geodatabase (FGDB).

## Installation

Python clone version of Arcgis pro 3

## Steps to RUN the script:
1. Right click "main.py" and select "Edit with IDLE (ArcGIS Pro)"
(Or use a popular IDE like VScode or command line, make sure use Python of ArcGIS Pro 3 )
2. Go to Run menu and and click run module or just press F5
3. Enter Input FGDB path and Target FGDB path

e.g 
```
Enter Input FGDB path:
D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\InputPolygonGDB.gdb

Enter Target FGDB path:
D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\TargetPolygonGDB.gdb

```
## Checking files: If input and target files exists in the path
then execute the append tool
Migrate polygons if reference number that starts with SP_ and have 5 digits
If file not found it will show "Filename not found" 

## Check results 
Open ArcGIS pro 3 
On the Map tab, in the Layer group, click "Add Data" and then click "add data to the map".
Browse the Target FGDB and select TargetPolygonFC