import arcpy
import os

arcpy.env.workspace = "Database Servers\instance_name.gds\database (VERSION:dbo.DEFAULT)"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)
