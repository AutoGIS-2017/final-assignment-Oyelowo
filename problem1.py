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

#ui is userinput
ui= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
#[int(x) for x in aa]
#6016696, 6015141, 5991603, 5991515, 5789455,9485399, 5789456, 4,2545,54646, 5802791, 8897

#xx="HelsinkiRegion_TravelTimeMatrix2015/6016xxx/travel_times_to_ 6016696.txt"
#xx[44:]
namelist= z.namelist()

#list of matrices
m_list=[]
for filename in namelist:
    for element in ui:
        if len(str(element))==7 and str(element) in filename:
            print(filename)
            print(namelist.index(filename))
            #slice the string
            m_list.append(element)
            f_slice=filename[44:]
            print("processing file {0}.. Progress: {1}/{2}".format(f_slice,len([i for i in range(len(m_list))]), len(m_list)))
            bytes = z.read(filename)
            print('has',len(bytes),'bytes')
            z.extract(filename)
print("WARNING: ", [i for i in ui if i not in m_list], ".txt does not exist")
            
#            if any(x in lk for x in ui)== False:
#                print('d')
            
     z.extract       
for i in bytes:
    print(i)    
            
            
            
            

        if str(element) not in filename:
            ele= 'HelsinkiRegion_TravelTimeMatrix2015/{0}xxx/travel_times_to_ {1}.txt'.format(str(element)[0:4],str(element))
            #nlk.append(ele)
            #[i for i in lk if i in namelist] 
            if any(x in lk for x in namelist)== False:
                nlk.append(element)








for filename in namelist:
    for element in ui:
        if str(element) in filename:
#            print(namelist.index(filename))
            #slice the string
            f_slice=filename[44:]
            print("processing file {0}.. Progress: {1}/{2}".format(f_slice,len(ui)-ui.index(element), len(ui)))
            bytes = z.read(filename)
            print('has',len(bytes),'bytes')































# =============================================================================
# ele= 'HelsinkiRegion_TravelTimeMatrix2015/{0}xxx/travel_times_to_ {1}.txt'.format(str(element)[0:3],str(element))
# 
# 
# d='HelsinkiRegion_TravelTimeMatrix2015/5787xxx/travel_times_to_ 5787544.txt'
# ff_slice= d[60:68]
# ff_slice
# 
# lk=[]
# for filename in namelist:
#     for element in ui:
#         if str(element) in filename:
#             ele= 'HelsinkiRegion_TravelTimeMatrix2015/{0}xxx/travel_times_to_ {1}.txt'.format(str(element)[0:4],str(element))
#             lk.append(ele)
#             [i for i in lk if i in namelist] 
#             if any(x in lk for x in namelist)== False:
#             
#                 print("rt")
#             print(ele)
#             print(namelist.index(filename))
#             #slice the string
#             f_slice=filename[44:]
#             print("processing file {0}.. Progress: {1}/{2}".format(f_slice,len(ui)-ui.index(element), len(ui)))
#             bytes = z.read(filename)
#             print('has',len(bytes),'bytes')
#     if str(element) not in filename:
#         print("fire")
#         
# 
# ele= 'HelsinkiRegion_TravelTimeMatrix2015/{0}xxx/travel_times_to_ {1}.txt'.format(str(element)[0:3],str(element))
# 
# 
# d='HelsinkiRegion_TravelTimeMatrix2015/5787xxx/travel_times_to_ 5787544.txt'
# ff_slice= d[60:68]
# ff_slice
# 
# L1 = ui
# L2 = namelist
# [i for i in L1 if i in L2]
# [2]
#print(any(x in lk for x in namelist))
#
#bytes 
# =============================================================================



 
# =============================================================================
    
    

# =============================================================================
# for filename in z.namelist():
#     print('File:', filename,)
#     bytes = z.read(filename)
#     print('has',len(bytes),'bytes')
#     break
# =============================================================================
