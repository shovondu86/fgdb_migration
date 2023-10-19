# Data Migration Tool

Arcpy based Python script for Migrate the input File Geodatabase (FGDB) into the output File Geodatabase (FGDB).

## Installation

Python clone version of Arcgis pro 3

## Usage
Open with main.py using 
edit with IDLE (ArcGIS Pro)
(Or use a popular IDE like VScode or command line, make sure use Python of ArcGIS Pro 3 )
Go to Run menu and and click run module or just press F5

Enter Input FGDB path and Target FGDB path

e.g 
```python

Enter Input FGDB path:
D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\InputPolygonGDB.gdb

Enter Target FGDB path:
D:\Worspace_ArcGISPro\projects\Data_Migration_SG\script\TargetPolygonGDB.gdb

```

Cheking files: If input and target files exists in the path
If files are exist then execute the append tool
Migrate polygons if reference number that starts with SP_ and have 5 digits 

## Check results 
Open ArcGIS pro 3 
On the Map tab, in the Layer group, click Add Data Add Data and click Data Add Data.
Brows the Target FGDB and select TargetPolygonFC