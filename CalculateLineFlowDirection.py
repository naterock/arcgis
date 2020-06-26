# Import arcpy module
import arcpy


# Local variables:
inputLines = arcpy.GetParameterAsText(0)
fromDirection = arcpy.GetParameterAsText(1)
toDirection = arcpy.GetParameterAsText(2)
dirOutput = "in_memory\\DirLines"

# Process: Linear Directional Mean
arcpy.DirectionalMean_stats(inputLines, dirOutput, "DIRECTION", "FEATUREID")
print "Running Linear Directional Mean"

# Process: Join
arcpy.JoinField_management (inputLines, "FEATUREID", dirOutput, "FEATUREID")
print "Running Join"

# Process: Calculate Field (From Direction)
arcpy.CalculateField_management(inputLines, fromDirection, "TextValue( !AZ_DIR!)", "PYTHON", "def TextValue(FindCode):\\n if FindCode >= 330 or FindCode <= 30:\\n return \"N\"\\n elif FindCode > 30 and FindCode < 60:\\n return \"NE\"\\n elif FindCode >= 60 and FindCode <= 120:\\n return \"E\"\\n elif FindCode > 120 and FindCode < 150:\\n return \"SE\"\\n elif FindCode >= 150 and FindCode <= 210:\\n return \"S\"\\n elif FindCode > 210 and FindCode < 240:\\n return \"SW\"\\n elif FindCode >= 240 and FindCode <= 300:\\n return \"W\"\\n elif FindCode > 300 and FindCode< 330:\\n return \"NW\"\\n else:\\n return None")
print "Running Field Calculation 1"

# Process: Calculate Field (To Direction)
arcpy.CalculateField_management(inputLines, toDirection, "TextValue( !AZ_DIR!)", "PYTHON", "def TextValue(FindCode):\\n if FindCode >= 330 or FindCode <= 30:\\n return \"S\"\\n elif FindCode > 30 and FindCode < 60:\\n return \"SW\"\\n elif FindCode >= 60 and FindCode <= 120:\\n return \"W\"\\n elif FindCode > 120 and FindCode < 150:\\n return \"NW\"\\n elif FindCode >= 150 and FindCode <= 210:\\n return \"N\"\\n elif FindCode > 210 and FindCode < 240:\\n return \"NE\"\\n elif FindCode >= 240 and FindCode <= 300:\\n return \"E\"\\n elif FindCode > 300 and FindCode< 330:\\n return \"SE\"\\n else:\\n return None")
print "Running Field Calculation 2"

# Process: Remove Join
#arcpy.RemoveJoin_management(inputLines, dirOutput)
#print "Removing Join"
