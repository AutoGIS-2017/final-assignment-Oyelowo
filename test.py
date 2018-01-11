
# -*- coding: utf-8 -*-

#import problem1
from problem1 import explore

from visualise_tt import visual
from problem4 import visual_comp

import geopandas as gpd
import pandas as pd
#import zipfile
from get_geom import get_geom
import numpy as np

#fp= "http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/"
fp=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT"
#zipped_data_path = zipfile.ZipFile((fp+"\HelsinkiRegion_TravelTimeMatrix2015.zip"), "r")
tt_zip_path=fp+"\HelsinkiRegion_TravelTimeMatrix2015.zip"
metropo=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\MetropAccess_YKR_grid\MetropAccess_YKR_grid_EurefFIN.shp"
index=tt_zip_path.rfind("\\") +1
tt_zip_path[index:][:-len('.zip')]



tt_zip_path.find('\\')

mtp= gpd.read_file(metropo)

mtp.crs
fp2=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\Exercise1"
sea=gpd.read_file(fp2 + "/sea.shp")
sea.crs
#sea=sea.to_crs(from_epsg(3067))


roads=gpd.read_file(fp2 + "/RoadNetwork.shp")

#sea= gpd.read_file(fp2 + "/Meri_hkiseutu.shp")


train=gpd.read_file(fp2 + "/Railway.shp")


roads_fp = r"C:\Users\oyeda\Desktop\AUTOGIS\AUTOGIS_PERIOD2\assignment5\data\roads.shp"
metro_fp = r"C:\Users\oyeda\Desktop\AUTOGIS\AUTOGIS_PERIOD2\assignment5\data\metro.shp"
#Read the data with Geopandas.


roads = gpd.read_file(roads_fp)

metro = gpd.read_file(metro_fp)


#namelist=data_zip.namelist()
#lowo.extractfilesPrompt1(data_zip=data_zip, filepath = fp+"/matrices", sep=",", file_format=".csv")


#For testing
#[int(x) for x in aa]
    #6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897
    
    #xx="HelsinkiRegion_TravelTimeMatrix2015/6016xxx/travel_times_to_ 6016696.txt"
    #xx[44:]
    
#bytes
#data_zip.read()
#data_zip.open(filename)
explore.create_shp(zipped_data_path=tt_zip_path, separate_folder=False, userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245], grid_shp=mtp, filepath= r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")
#zip2shp.readzipPrompt1(data_zip=data_zip, separate_folder=True, grid_shp=mtp, filepath= r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")

explore.create_shp2(tt_zip_path, separate_folder=True, userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245], grid_shp=mtp,filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")
#zip2shp.readzipPrompt2(data_zip=data_zip, grid_shp=mtp,filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged" )

userinput=[5991603]

hh=gpd.read_file(r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise\travel_times_to_pt_r_tt_vs_car_r_t_5991515.shp")


list(mtp.iloc[:,2])
p1.files_Prompt()
explore.extract_prompt(zipped_data_path= tt_zip_path, separate_folders=False, filepath= fp +"/matrices", sep=",", file_format='.txt')

explore.extract2(zipped_data_path= tt_zip_path, userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245]
             ,separate_folders=True, filepath= fp +"/matrices", sep=",", file_format='.txt')

userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245]
lowo.extractfilesPrompt2(data_zip= data_zip, filepath= fp +"/matrices", sep="\t")


zip2shp.readzipAll(data_zip=data_zip, userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245], grid_shp=mtp, filepath= r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")
zip2shp.readzipAllprompt(data_zip=data_zip, grid_shp=mtp, filepath= r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")
aa=gpd.read_file(r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged\mergedAll.shp")


visual.vis(data_zip, train=train, metro=metro, roads=roads,
           roads_color='grey', metro_color='red', train_color='blue',
           userinput=[5991,342,6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897,2524,245], 
           destination_style='circle', destination_color='blue',map_type='interactive',
           grid_shp=mtp, tt_col="car_r_t",n_classes=5, classification='pysal_class',  
           class_type='Equal_Interval' ,
           filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise")   
#Ensure that the CRS is the same than in the all layers
mtp['geometry'] = mtp['geometry'].to_crs(epsg=3067)
mtp.crs


#print(sea.geometry.get_values()[0])
#x=sea.x.values[0]
#import math
#x=[value for value in x if not math.isnan(value)]
#x
#
#
#y=sea.y.values[0]
#import math
#y=[value for value in y if not math.isnan(value)]
#y
#len(x)
#len(y)
#len(sea.geometry)



visual_comp.vis_compare(zipped_data_path= tt_zip_path, compare_mod=["pt_r_t","pt_r_tkt"],
        map_type='interactive',visualisation=True, userinput=[5991,342,6016696, 
        6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 
        8897,2524,245],  filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise", 
        grid_shp=mtp, destination_style='circle',  classification='User_Defined',
        n_classes=10, class_type="Quantiles", lower_limit=-50, upper_limit= 1000, step=700,
        label_upper_limit=200)   

visual_comp.vis_compare(zipped_data_path= tt_zip_path, roads=roads, compare_mod=["pt_r_tt","pt_r_t"],
        map_type='interactive',visualisation=True, userinput=[5991,342,6016696, 
        6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 
        8897,2524,245],  filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise", 
        grid_shp=mtp, destination_style='circle',  classification='User_Defined',
        n_classes=10, class_type="Quantiles", class_lower_limit=-15, class_upper_limit=200, 
        class_step=5, label_lower_limit=-10, label_upper_limit=30, label_step=5)   

explore.compare_travel_modes(zipped_data_path= tt_zip_path, sea=sea, roads=roads,train=train, metro=metro,compare_mod=['pt_r_tt', 'car_r_t'],
        map_type='interactive',create_shapefiles=False, visualisation=True, roads_color='grey', 
        metro_color='red', train_color='brown', userinput=[5991,342,6016696, 
        6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 
        8897,2524,245],  filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise", 
        grid_shp=mtp, destination_style='circle',  destination_color='blue', classification='User_Defined',
        n_classes=10, class_type="Quantiles", class_lower_limit=-15, class_upper_limit=200, 
        class_step=5, label_lower_limit=-10, label_upper_limit=60, label_step=10)   

visual_comp.vis_compare(zipped_data_path= tt_zip_path, sea=sea, roads=roads,train=train, metro=metro,compare_mod=['walk_t', 'car_r_t'],
                        filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise",
                        userinput=[5991,342,6016696, 
                        6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 
                        8897,2524,245],grid_shp=mtp, map_type='interactive', create_shapefiles=False,)

explore.compare_travel_modes()
explore.show_travel_mode()