# -*- coding: utf-8 -*-
"""
Testing AccessViz of Oyelowo according the documentation

Created on Tue Jan 30 13:47:41 2018

@author: hentenka
"""

# Add the module to the path
import sys
mpath = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017_Assessment\Oyelowo\final-assignment-Oyelowo\AccessViz"
sys.path.insert(0, mpath)

from AccessViz import explore as expl
import geopandas as gpd



# Test Extract Prompt
# -------------------

# Filepath
matrix = r"C:\HY-Data\HENTENKA\Data\HelsinkiRegion_TravelTimeMatrix2015.zip"
outfp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017_Assessment\Oyelowo\data"
grid_fp = r"C:\HY-Data\HENTENKA\Data\MetropAccess_YKR_grid_EurefFIN.shp"
roads_fp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017\data\roads.shp"
vis_fp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017_Assessment\Oyelowo\data\Visualization"
separator = ';'
fformat = '.csv'
ids = [5961886, 5898414, 5963586, 1234566]

# The separate folders needs to be True for the tool to work (after editing it)
separate_folders = True

# Extract ttime files (works now after editing)
#expl.extract(zipped_data_path=matrix, filepath=outfp, userinput=ids, sep=separator, file_format=fformat, separate_folders=separate_folders)

# Merge functionality
# -------------------

# Read the shapefile
grid = gpd.read_file(grid_fp)

#expl.merge_shp(zipped_data_path=matrix, userinput=ids, grid_shp=grid, filepath=outfp, separate_folder=False)

# Create maps
# -----------

# Read roads
roads = gpd.read_file(roads_fp)

# Interactive map
expl.show_travel_mode(zipped_data_path=matrix, roads=roads, roads_color='grey', 
                      userinput=[6015141, 5991603, 5991515], 
                      destination_style='circle', destination_color='blue',map_type='interactive', 
                      grid_shp=grid, tt_col="car_r_t", n_classes=5, classification='pysal_class',
                      class_type='Equal_Interval', filepath=vis_fp)

# Static map
expl.show_travel_mode(zipped_data_path=matrix, roads=roads, roads_color='grey', 
                      userinput=[6015141, 5991603, 5991515], 
                      destination_style='circle', destination_color='blue',map_type='static', 
                      grid_shp=grid, tt_col="car_r_t", n_classes=5, classification='pysal_class',
                      class_type='Equal_Interval', filepath=vis_fp)

# Both visualizations work nicely! Good!


# Compare travel modes
# ====================

expl.compare_travel_modes(zipped_data_path=matrix, roads=roads, compare_mod=["pt_r_tt", "car_r_t"], create_shapefiles=True, visualisation=True, 
                             roads_color='grey', userinput=ids, destination_style='circle', destination_color='blue', map_type='interactive', 
                             grid_shp=grid, n_classes=5, classification='pysal_class',
                             class_type='Quantiles', filepath=vis_fp)

# Interactive visualization does not produce correct looking map. 

expl.compare_travel_modes(zipped_data_path=matrix, roads=roads, compare_mod=["pt_r_tt", "car_r_t"], create_shapefiles=True, visualisation=True, 
                             roads_color='grey', userinput=ids, destination_style='circle', destination_color='blue', map_type='static', 
                             grid_shp=grid, n_classes=5, classification='pysal_class',
                             class_type='Quantiles', filepath=vis_fp)

# Static map produces a map that looks valid.


