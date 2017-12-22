# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:15:11 2017

@author: oyeda
"""
import geopandas as gpd
import zipfile
#fp= "http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/"
fp=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT"
z = zipfile.ZipFile((fp+"\HelsinkiRegion_TravelTimeMatrix2015.zip"), "r")
metropo=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\MetropAccess_YKR_grid\MetropAccess_YKR_grid_EurefFIN.shp"

mtp= gpd.read_file(metropo)
#for i,rows in z.
# =============================================================================
# 1. AccessViz finds from the data folder all the matrices that user has 
# specified by assigning a list of integer values that should correspond to 
# YKR-IDs found from the attribute table of a Shapefile called
# MetropAccess_YKR_grid.shp. If the ID-number that the user has specified does
# not exist in the data folders, the tools should warn about this to the user 
# but still continue running. The tool should also inform the user about the 
# execution process: tell the user what file is currently under process and how 
# many files there are left 
# (e.g. “Processing file travel_times_to_5797076.txt.. Progress: 3/25”).
# =============================================================================

#aa= raw_input()
#x= input("list the ID-numbers you want to read: ")  
#aa= [int(x) for x in input().split()] #with this, you only need to separate by space

#alternative
#s = input()
#numbers = list(map(int, s.split()))


#aa= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
#print("these are the numbers{0}".format(aa))
#type(aa)

aa= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
#[int(x) for x in aa]
#6016696, 6015141, 5991603, 5991515

#xx="HelsinkiRegion_TravelTimeMatrix2015/6016xxx/travel_times_to_ 6016696.txt"
#xx[44:]
nl= z.namelist()

for f in nl:
    for i in aa:
        if str(i) in f:
            #slice the string
            f_slice=f[44:]
            print("processing file {0}..{1}".format(f_slice, len(aa)-aa.index(i)),"/",len(aa))

     
# =============================================================================
    
    

# =============================================================================
# for filename in z.namelist():
#     print('File:', filename,)
#     bytes = z.read(filename)
#     print('has',len(bytes),'bytes')
#     break
# =============================================================================
