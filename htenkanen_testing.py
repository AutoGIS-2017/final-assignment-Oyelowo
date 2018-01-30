# -*- coding: utf-8 -*-
"""
Testing AccessViz of Oyelowo according the documentation

Created on Tue Jan 30 13:47:41 2018

@author: hentenka
"""

from AccessViz import explore as expl
import sys

# Add the module to the path
mpath = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017_Assessment\Oyelowo\final-assignment-Oyelowo\AccessViz"
sys.path.insert(0, mpath)

# Test Extract Prompt
# -------------------

# Filepath
matrix = r"C:\HY-Data\HENTENKA\Data\HelsinkiRegion_TravelTimeMatrix2015.zip"
outfp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\2017_Assessment\Oyelowo\data"
grid_fp = r"C:\HY-Data\HENTENKA\Data\MetropAccess_YKR_grid_EurefFIN.shp"
separator = ';'
fformat = '.csv'
ids = [5961886, 5898414, 5963586, 1234566]

# The separate folders needs to be True for the tool to work (after editing it)
separate_folders = True

# Extract ttime files (works now after editing)
#expl.extract(zipped_data_path=matrix, filepath=outfp, userinput=ids, sep=separator, file_format=fformat, separate_folders=separate_folders)

# Merge functionality
expl.merge_shp(zipped_data_path=matrix, userinput=ids, grid_shp=grid_fp, filepath=outfp, separate_folder=False)

