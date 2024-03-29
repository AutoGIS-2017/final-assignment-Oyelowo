
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:15:11 2017

@author: oyeda
"""
import geopandas as gpd
import pandas as pd
import zipfile

#for 3
from bokeh.plotting import figure, save
from bokeh.models import Title
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper, GeoJSONDataSource
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
#from matplotlib import legend
import pysal as ps
import pandas as pd
import textwrap
from get_geom import get_geom
from fiona.crs import from_epsg
from bokeh.palettes import RdYlGn11 as palette2

# ===========================================================================
# When reading data from Bytes, you need to import it with BytesIO driver
# ===========================================================================
from io import BytesIO


# ============================================================
# H.T. General comments:
#  - It is nice that you have used classes (not covered in the course) and written the functionality of the tool as a module!
#  - You have quite a lot of duplicate code in here. It would have been good to wrap e.g. all reading parts from a Zipfile into a function instead of repeating the same code. 
#    There was an error in reading the data into Pandas from Zipfile, now it was needed to fix the same pieces of code to multiple places. 
#    If you would have used a function there would have been only one place where the code should have been fixed.



class AccessVizError(Exception):
    """Base class for exceptions in this AccessViz module."""
    pass


        #this will be usedd later to check which of the inputs are present or absent
def check_input(userinput, main_list):
    """
    This function checks which of the values in the list of the userinput is not in the mainlist.
    It was created to check which of the specified matrices by userinput is not present 
    in the travel time matrices. It also tells if all of the specified grid IDs are not present in the travel time matrices.
    
    userinput: this is a list specified.
    grid_ID_list: this is another list considered as the main list from which we can check if the elements of the userinput exists.
    """
    
    #put into an object the inputs are not in the matrix list(i.e which of the specified is not in the zipped matrices)
    absentinput= [i for i in userinput if i not in main_list]
    
    #check if all of the imputed values does not exist
    if len(absentinput)==len(userinput):
        print("all the inputs do not exist")
        
        #check for those that are not included in the matrices
    elif any(absentinput) not in main_list:
        #warn that they do not exist
        print("WARNING: ", str(absentinput).strip("[]"), " do not exist")
        #check how many of them are not in the matrices
        print(len(absentinput), "of the inputs are not included in the matrices\n")   
        
            

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

class explore:
                
    def extract_prompt(zipped_data_path, filepath, sep=";", file_format=".txt",separate_folders=False):
        """
        This function extracts matrices(files) from the zipped Helsinki Region Travel
        Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
        the specified input is not included in the matrices
        specified by use. 
        
        The function has thesame function as the function 'extract_files'. The only difference is that the user is prompted to input the values which should be separated by comma(,).
        
        zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.
        
        filepath: output filepath where the matrices files will be extracted to.
        
        sep(e.g ',' ,';', '\t)' : the separator of the columns of the extracted files. This works only if the files are extracted into thesame folder, i.e separate_folder=False.
             
        file_format(e.g. .txt, .csv): format of the extracted travel time matrices. This is also works only if the files are extracted into thesame folder, i.e separate_folder=False.
                    
        separate_folder(True/False): this determines if the files should be extracted into same folder or separate folders. Default value is False.    
        """
        
        
        # =====================================================================================================================================
        # H.T. Comment: This function did not work because the files were inside a Zipfile and reading the data with Pandas weren't working. 
        # Once the ttm-file is extracted or the bytes is read in with BytesIO wrapper, then I am able to read the data into Pandas. 
        # =====================================================================================================================================
        
    
        #this prompt the user to type in the YKR_ID. #This can also be done by just including the list in the argument.
        userinput= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
        
        #read the zipped travel time matrices
        data_zip = zipfile.ZipFile(zipped_data_path, "r")
        
        #Extract the name lists from the zipped file
        namelist= data_zip.namelist()
                
        #create an empty list which will be used later to include the available inputs out of 
        #the specified inputs by the user.
        m_list=[]

        #iterate over the userinput, to get all its element/values
        for element in userinput:
            
            #create a list of destination grid IDs from all the file names
            dest_ids=[i[-11:-4] for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            dest_ids_file=[i for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            
#            check if the specified grid id(i.e userinput) is in the list of ids created earlier
            if str(element) not in dest_ids:
                print("WARNING: The specified matrix {0} is not available\n".format(element))
                
            else:
                print("Matrix {0} is available".format(element))
                m_list.append(element)
                
                #check for the progress
                print("Processing file travel_times_to_{0}.txt.. Progress: {1}/{2}".format(element,len([i for i in range(len(m_list))]), len(userinput)))
                
                
#                find the index of the grid ID(element) in the destination ids list created earlier.
                element_index= dest_ids.index(str(element))
                
                #use this to find the corresponding file in the destination ids filename list created earlier
                element_file=dest_ids_file[element_index]
                
                
                # ==========================================================================================
                # You should not use a variable name 'bytes' because it is an built-in data type in Python
                # ==========================================================================================
                
                #check the size of each file
                #bytes = data_zip.read(element_file)
                b = data_zip.read(element_file)
        
                #print the file size
                print('has',len(b),'bytes\n')
                
                
                #export the matrices into different folders
                if separate_folders==True:
                    #extract the available travel time matrix out of the specified by the user.
                    
                    # ===================
                    # H.T. You can get the filepath from 'extract' function of zipfile that can be used to read the data into Pandas
                    # ===================
                    
                    #data_zip.extract(element_file, path= filepath)
                    
                    extracted_fp = data_zip.extract(element_file, path= filepath)
                    
                # =======================================================================
                # H.T. When reading bytes you need to read the 'bytes' with BytesIO
                # =======================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                tt_matrices= pd.read_csv(BytesIO(b), sep=";")
                
                #export all the files into thesame folder.
                if separate_folders==False:
                    #save the selected files into same folder
                    tt_matrices.to_csv(filepath + "/"+str(element)+ file_format, sep)      
             
        #check if all of the imputed values does not exist
        check_input(userinput=userinput, main_list=m_list)
            

    
    def extract(zipped_data_path, filepath,userinput, sep=";", file_format=".txt", separate_folders=False):
        """
        The function has thesame function as the function 'extract_prompt'. The only difference is that the user is not prompted to input the grid values but this should be specified in the parameter 'userinput'.
        This function extracts matrices(files) from the zipped Helsinki Region Travel
        Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
        the specified input is not included in the matrices
        specified by use. 
        
        The function has thesame function as the function 'extract_files'. The only difference is that the user is prompted to input the values which should be separated by comma(,).
        
        zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.
        
        filepath: output filepath where the matrices files will be extracted to.
        
        userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]
               
        sep(e.g ',' ,';', '\t)' : the separator of the columns of the extracted files. This works only if the files are extracted into thesame folder, i.e separate_folder=False.
             
        file_format(e.g. .txt, .csv): format of the extracted travel time matrices. This is also works only if the files are extracted into thesame folder, i.e separate_folder=False.
                    
        separate_folder(True/False): this determines if the files should be extracted into same folder or separate folders. Default value is False.    
        """
        
                
              #read the zipped travel time matrices
        data_zip = zipfile.ZipFile(zipped_data_path, "r")
        
        #Extract the name lists from the zipped file
        namelist= data_zip.namelist()
                
        #create an empty list which will be used later to include the available inputs out of 
        #the specified inputs by the user.
        m_list=[]

        #iterate over the userinput, to get all its element/values
        for element in userinput:
            
            #create a list of destination grid IDs from all the file names
            dest_ids=[i[-11:-4] for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            dest_ids_file=[i for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            
#            check if the specified grid id(i.e userinput) is in the list of ids created earlier
            if str(element) not in dest_ids:
                print("WARNING: The specified matrix {0} is not available\n".format(element))
                
            else:
                print("Matrix {0} is available".format(element))
                m_list.append(element)
                
                #check for the progress
                print("Processing file travel_times_to_{0}.txt.. Progress: {1}/{2}".format(element,len([i for i in range(len(m_list))]), len(userinput)))
                
                
#                find the index of the grid ID(element) in the destination ids list created earlier.
                element_index= dest_ids.index(str(element))
                
                #use this to find the corresponding file in the destination ids filename list created earlier
                element_file=dest_ids_file[element_index]
                
               # ==========================================================================================
                # You should not use a variable name 'bytes' because it is an built-in data type in Python
                # ==========================================================================================
                
                #check the size of each file
                #bytes = data_zip.read(element_file)
                b = data_zip.read(element_file)
        
                #print the file size
                print('has',len(b),'bytes\n')
                
                #export the matrices into different folders
                if separate_folders==True:
                    #extract the available travel time matrix out of the specified by the user.
                   
                    # ===================
                    # H.T. You can get the filepath from 'extract' function of zipfile that can be used to read the data into Pandas
                    #data_zip.extract(element_file, path= filepath)
                    
                    extracted_fp = data_zip.extract(element_file, path= filepath)
                    
                
                
                # =========================================================================
                # H.T. The 'element_file' is not a valid filepath and it produces and error
                # =========================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                    
                # =======================================================================
                # H.T. When reading bytes you need to read the 'bytes' with BytesIO
                # =======================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                tt_matrices= pd.read_csv(BytesIO(b), sep=";")
                
                #export all the files into thesame folder.
                if separate_folders==False:
                    #save the selected files into same folder
                    tt_matrices.to_csv(filepath + "/"+str(element)+ file_format, sep)      
             
        #check if all of the imputed values does not exist
        check_input(userinput=userinput, main_list=m_list)
            
            

# =============================================================================
# 2. AccessViz can create Shapefiles from the chosen Matrix text tables (e.g. travel_times_to_5797076.txt) 
# by joining the Matrix file with MetropAccess_YKR_grid Shapefile where from_id in Matrix file corresponds 
# to YKR_ID in the Shapefile. The tool saves the result in the output-folder that user has defined. 
# You should name the files in a way that it is possible to identify the ID from the name (e.g. 5797076)
# =============================================================================
  
    def merge_shp(zipped_data_path,userinput, grid_shp, filepath, separate_folder=False):
        """
        This creates Shapefiles from the chosen Matrix text tables
        (e.g. travel_times_to_5797076.txt) by joining the Matrix file with MetropAccess_YKR_grid 
        Shapefile where from_id in Matrix file corresponds to YKR_ID in the Shapefile. The tool 
        saves the result in the output-folder that user has defined. The output files 
         are named in a way that it is possible to identify the ID from the name (e.g. 5797076).
         
        zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.
        
        userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]
        
        grid_shp= this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time matrix(ces).
        
        filepath: output filepath where the matrices files will be extracted to.
               
        separate_folder: this determines if the files should be extracted into same folder or separate folders.
             
         
        """
        
        # =======================================================================================================
        # H.T. It was a bit unclear from the documentation that the 'grid_shp' should have been a GeoDataFrame. 
        # It would be better to mention that the grid_shp is a GeoDataFrame from that Shapefile. 
        # For better usability, it would have been better to ask for a filepath to the Shapefile and your function 
        # would take care of the reading in a similar manner as you do with the Zipfile. 
        # =======================================================================================================
        
        
        data_zip = zipfile.ZipFile(zipped_data_path, "r")
        
        #userinput= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
        namelist= data_zip.namelist()
        m_list=[]
        
        #iterate over the userinput, to get all its element/values
        for element in userinput:
            
            #create a list of destination grid IDs from all the file names
            dest_ids=[i[-11:-4] for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            dest_ids_file=[i for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            
#            check if the specified grid id(i.e userinput) is in the list of ids created earlier
            if str(element) not in dest_ids:
                print("WARNING: The specified matrix {0} is not available\n".format(element))
                
            else:
                print("Matrix {0} is available".format(element))
                m_list.append(element)
                
                #check for the progress
                print("Processing file travel_times_to_{0}.txt.. Progress: {1}/{2}".format(element,len([i for i in range(len(m_list))]), len(userinput)))
                
                
#                find the index of the grid ID(element) in the destination ids list created earlier.
                element_index= dest_ids.index(str(element))
                
                #use this to find the corresponding file in the destination ids filename list created earlier
                element_file=dest_ids_file[element_index]
                
                # ==========================================================================================
                # You should not use a variable name 'bytes' because it is an built-in data type in Python
                # ==========================================================================================
                
                #check the size of each file
                #bytes = data_zip.read(element_file)
                b = data_zip.read(element_file)
        
                #print the file size
                print('has',len(b),'bytes\n')
                
                # =======================================================================================
                # H.T. The 'element_file' is not a valid filepath and it produces and error. See above!
                # ======================================================================================
                    
                #tt_matrices= pd.read_csv(element_file, sep=";")
                
                # =======================================================================
                # H.T. When reading bytes you need to read the 'bytes' with BytesIO
                # =======================================================================
                
                #read the data
                tt_matrices= pd.read_csv(BytesIO(b), sep=";")
                
                merged_metro = pd.merge(grid_shp,tt_matrices,  left_on="YKR_ID", right_on="from_id")
                #print(merged_metro)
                #merged_metro.to_file(driver= 'ESRI Shapefile', filename= filepath+"/"+str(element)+".shp")
                 
                if separate_folder==True:
                        merged_metro.to_file(driver = 'ESRI Shapefile', filename= filepath+"/travel_times_to_" + str(element))                
                else:
                        merged_metro.to_file(driver = 'ESRI Shapefile', filename= filepath+"/travel_times_to_" + str(element) + ".shp")
               
                    
        #check if all of the imputed values does not exist
        check_input(userinput=userinput, main_list=m_list)
    
    
    
    
    # =============================================================================
# 3. AccessViz can visualize the travel times of selected YKR_IDs based on the 
# travel mode that the user specifies. It can save those maps into a folder that 
# user specifies. The output maps can be either static or interactive and user 
# can choose which one with a parameter. You can freely design yourself the 
# style of the map, colors, travel time intervals (classes) etc. Try to make 
# the map as informative as possible!
# =============================================================================




    def show_travel_mode(zipped_data_path,userinput, tt_col, filepath, grid_shp, sea=None, roads=None,train=None, 
            metro=None, roads_color='grey', metro_color='red', 
            train_color='blue',map_type='interactive', destination_style='circle', destination_color='blue',       
            classification='pysal_class', class_type="Quantiles", n_classes=8,
            multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, truncate=True, 
            pct_classes=[1,10,50,90,99,100],
            class_lower_limit="", class_upper_limit="", class_step="", 
            label_lower_limit="", label_upper_limit="", label_step=""):
        ''' This visualises the travel times of selected YKR_IDs based on the travel mode that the 
            user specifies. It can save those maps into a folder that is specified. The output maps
            can be either static or interactive and user can choose which one with a parameter. 
            By using the parameters, you can freely design yourself the style of the map, 
            travel time intervals (classes) etc.  You can decided to either visualise joined travel mode or not.
            You can also choose what kind of classificaation(either pysal class or User_Defined). The pysal_class
            option uses pysal classification which can be found here:http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify.
            With the user_defined classification, you can choose yourself how you wish to make the classifixation,
            inlcuding the lowest limit, uppermost limit and also the interval/break. This can also be done as you want it on the label/legend.
            the uppermost level shows those values that are greater than that level(e.g 60< or >60).
            This function also tells if a grid is empty(i.e no data). This grids with nodata have -1 value
            
            This creates Shapefiles from the chosen Matrix text tables
            (e.g. travel_times_to_5797076.txt) by joining the Matrix file with MetropAccess_YKR_grid 
            Shapefile where from_id in Matrix file corresponds to YKR_ID in the Shapefile. The tool 
            saves the result in the output-folder that user has defined. The output files 
             are named in a way that it is possible to identify the ID from the name (e.g. 5797076).
             
            zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.
            
            userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]
            
            tt_col: this is the travel mode which will be displayed in the map(e.g pt_r_tt, pt_r_d, walk_d, car_r_t)
            
            grid_shp= this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time matrix(ces).
            
            filepath: output filepath where the maps will be extracted to.
                 
            sea(default value=None): this is the shapefile of the sea around the region which will be displayed on the map if specified.
            
            roads(default value=None): this is the shapefile of the roads in the region which will be displayed on the map if specified.
            
            train(default value=None): this is the shapefile of the train rail line in the region which will be displayed on the map if specified.
            
            metro(default value=None): this is the shapefile of the metro rail line in the region which will be displayed on the map if specified.
                 
            roads_color, metro_color, train_color: these are used to choose the color for the various transportation means.
            
            map_type: options are(interactive or static). 
            
            destination_style(default= circle): options are(grid or cycle). This shows how you wish to highlight the destination grid.
        
            destination_color: color of the highlighted destination.
            
            classification(default='pysal_class'): options are('pysal_class' or 'user_defined').
            
            class_type(default="Quantiles"): Options include, 'Quantiles', 'Box_Plot', 'Equal_Interval, 'Fisher_Jenks',
                                            'HeadTail_Breaks','Jenks_Caspall', 'Max_P_Classifier', 'Natural_Breaks', 'Percentiles', and 'Std_Mean'.
                                            For more information: http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify

            n_classes(default=8): number of classes.
            
            multiples: used in Standard Deviation and Mean Map Classification(i.e Std_Mean). 
            
            pct_classes: used in for Percentiles Map Classification. In the pysal documentation, this is parameter is is 'pct'.
            
            pct: Fisher Jenks optimal classifier - mean based using random sample. 
            
            hinge: used in Box_Plot Map Classification.
            
            truncate: used in Fisher Jenks optimal classifier - mean based using random sample. 
            
            class_lower_limit, class_upper_limit, class_step: should be used for making the breaks for manually classifying the travel mode column.
                                                                
            
            label_lower_limit, label_upper_limit, label_step: This can be used for making the legend.
            label_lower_limit is the lowest limit allowed in the legen, label_step is the label/legend class interval, while
            the label_upper_limit level shows those values that are greater than that level(e.g 60< or >60)

        '''
        
        
        grid_shp=grid_shp.to_crs(from_epsg(3067))
        
        if roads is None:
            print('You have not included the roads route')
        else:
            roads=roads.to_crs(from_epsg(3067))
            rdfsource = GeoJSONDataSource(geojson=roads.to_json())
            
#            #Calculate the x and y coordinates of the roads (these contain MultiLineStrings).
#            roads['x'] = roads.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#                            
#            roads['y'] = roads.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#            
#             # Include only coordinates from roads (exclude 'geometry' column)
#            rdf = roads[['x', 'y']]
#            #this two rows had nan values which prevented me from saving the plot. I got the error:
#            #ValueError: Out of range float values are not JSON compliant.
#            #therefore, I had to remove the two rows
#            rdf.drop(39, inplace=True)
#            rdf.drop(158, inplace=True)
#            
#            rdfsource = ColumnDataSource(data=rdf)
         
        if train is None:
            print('You have not included the train route')
        else:
            train=train.to_crs(from_epsg(3067))
            tdfsource = GeoJSONDataSource(geojson=train.to_json())
            
            #Alternative without using GeoJSONDataSource
#            train['x'] = train.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#            
#            train['y'] = train.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#           
#            
#            tdf = train[['x','y']]
#            tdfsource = ColumnDataSource(data=tdf)
            
        if metro is None:
            print('You have not included the metro route')
        else:
            metro=metro.to_crs(from_epsg(3067))
            mdfsource = GeoJSONDataSource(geojson=metro.to_json())
            
            #alternative
#              #Calculate the x and y coordinates of metro.
#            metro['x'] = metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#            
#            metro['y'] = metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#                          
#            # Include only coordinates from metro (exclude 'geometry' column)
#            mdf = metro[['x','y']]
#            mdfsource = ColumnDataSource(data=mdf)
        if sea is None:
            print('You have not included the metro route')
        else:
   
            sea=sea.to_crs(from_epsg(3067))
            
            sea_source = GeoJSONDataSource(geojson=sea.to_json())
                            
                   
         #read the zipped travel time matrices
        data_zip = zipfile.ZipFile(zipped_data_path, "r")
        
        #userinput= [int(x) for x in input("list the ID-numbers you want to read and separate each by a comma(,): ").split(',')]
        namelist=data_zip.namelist()
        m_list=[]
        
                #iterate over the userinput, to get all its element/values
        for element in userinput:
            
            #create a list of destination grid IDs from all the file names
            dest_ids=[i[-11:-4] for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            dest_ids_file=[i for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            
#            check if the specified grid id(i.e userinput) is in the list of ids created earlier
            if str(element) not in dest_ids:
                print("WARNING: The specified matrix {0} is not available\n".format(element))
                
            else:
                print("Matrix {0} is available".format(element))
                m_list.append(element)
                
                #check for the progress
                print("Processing file travel_times_to_{0}.txt.. Progress: {1}/{2}".format(element,len([i for i in range(len(m_list))]), len(userinput)))
                
                
#                find the index of the grid ID(element) in the destination ids list created earlier.
                element_index= dest_ids.index(str(element))
                
                #use this to find the corresponding file in the destination ids filename list created earlier
                element_file=dest_ids_file[element_index]
                
                
                # ==========================================================================================
                # You should not use a variable name 'bytes' because it is an built-in data type in Python
                # ==========================================================================================
                
                #check the size of each file
                #bytes = data_zip.read(element_file)
                b = data_zip.read(element_file)
        
                #print the file size
                print('has',len(b),'bytes\n')
                
                    
                # =======================================================================
                # H.T. When reading bytes you need to read the 'bytes' with BytesIO
                # =======================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                tt_matrices= pd.read_csv(BytesIO(b), sep=";")
                
                #This is done to handle matrices with nodata at all. e.g: matrix"6016696"
                if tt_matrices['to_id'].max()==-1:
                    print('The MATRIX- {0} is empty and has nodata\n'.format(element))
                    
                else:
                    merged_metro = pd.merge(grid_shp,tt_matrices,  left_on="YKR_ID", right_on="from_id")
                    #print(merged_metro)
                    #Calculate the x and y coordinates of the grid.
                    merged_metro['x'] = merged_metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
        
                    merged_metro['y'] = merged_metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
                    
                    #NOTE: I CHOSE TO DEAL WITH NODATA BY EXCLUDING THEM.
                    merged_metro= merged_metro.loc[merged_metro.loc[:, tt_col]!=-1]
                    
                   
                    if classification =='pysal_class':
                        if class_type == "Natural_Breaks":
                            classifier = ps.Natural_Breaks.make(k=n_classes)
                        elif class_type == "Equal_Interval":
                            classifier = ps.Equal_Interval.make(k=n_classes)
                        elif class_type == "Box_Plot":
                            classifier = ps.Box_Plot.make(hinge)
                        elif class_type == "Fisher_Jenks":
                            classifier = ps.Fisher_Jenks.make(k=n_classes)
        #                elif class_type == "Fisher_Jenks_Sampled":
        #                    classifier = ps.Fisher_Jenks_Sampled.make(k=n_classes, pct=0.1)
                        elif class_type == "HeadTail_Breaks":
                            classifier = ps.HeadTail_Breaks.make(k=n_classes)
                        elif class_type == "Jenks_Caspall":
                            classifier = ps.Jenks_Caspall.make(k=n_classes)
                        elif class_type == "Jenks_Caspall_Forced":
                            classifier = ps.Jenks_Caspall_Forced.make(k=n_classes)
                        elif class_type == "Quantiles":
                            classifier = ps.Quantiles.make(k=n_classes)
                        elif class_type == "Percentiles":
                            classifier = ps.Percentiles.make(pct_classes)
                        elif class_type == "Std_Mean":
                            classifier = ps.Std_Mean.make(multiples)
                        mode_classif = merged_metro[[tt_col]].apply(classifier)
                       
                        
                        #Rename the columns of our classified columns.
                        mode_classif.columns = [tt_col+"_ud"]
                        
                        
                        #Join the classes back to the main data.
                        merged_metro = merged_metro.join(mode_classif)
                        
                            
                        merged_metro['label_' + tt_col ] = mode_classif
                            
                        
                    
                    elif classification == "user_defined":
                         #Next, we want to classify the travel times with 5 minute intervals until 200 minutes.
        
                        #Let’s create a list of values where minumum value is 5, maximum value is 200 and step is 5.
                        breaks = [x for x in range(class_lower_limit, class_upper_limit, class_step)]
                        #Now we can create a pysal User_Defined classifier and classify our travel time values.
                    
                        classifier = ps.User_Defined.make(bins=breaks)
                    
                        #walk_classif = data[['walk_t']].apply(classifier)
                        
                        mode_classif = merged_metro[[tt_col]].apply(classifier)
                        
                        
                        #Rename the columns of our classified columns.
                        mode_classif.columns = [tt_col+"_ud"]
                        #walk_classif.columns = ['walk_t_ud']
                        
                        #Join the classes back to the main data.
                        merged_metro = merged_metro.join(mode_classif)
                        
                        
                       #Create names for the legend (until certain minutes). The following will produce: e.g["0-5", "5-10", "10-15", ... , "60 <"]. 
                        #inside the range function, the label_lower_limit is added to the 
                        #label_step to give the stated lower_limit because they are first subtracted(i.e x - label_step)
                        #at the beginning.
                        names = ["%s-%s" % (x-label_step, x) for x in range(label_lower_limit + label_step, label_upper_limit, label_step)]
                        #         ["{0}kk{1}".format(x-5,x) for x in range(5, 200, 5)]   #alternative
                        
# =============================================================================
#                                you can try the below for further clarification
#                                 upper_limit = 60
#                                 step = 15
#                                 lower_limit=0
#                                 names = ["%s-%s " % (x-step, x) for x in range(lower_limit+ step, upper_limit, step)]
# =============================================================================
                                 
                        #Add legend label for over the label_upper_limit
                        names.append("%s<" % label_upper_limit)

                        
                        merged_metro['label_' + tt_col ] = None
                        
                        #Update rows with the class-names.
                        for i in range(len(names)):
                            merged_metro.loc[merged_metro[tt_col+"_ud"] == i, 'label_' + tt_col] = names[i]
                           
                        #Update all cells that didn’t get any value with "60 <"
                        #data['label_wt'] = data['label_wt'].fillna("%s <" % upper_limit)
                        
                        merged_metro['label_' + tt_col] = merged_metro['label_' + tt_col].fillna("%s<" % label_upper_limit)
                        
                    #Finally, we can visualize our layers with Bokeh, add a legend for travel times 
                    #and add HoverTools for Destination Point and the grid values (travel times).
                    # Select only necessary columns for our plotting to keep the amount of data minumum
                    df = merged_metro[['x', 'y',"YKR_ID", tt_col,tt_col+"_ud","from_id" ,'label_' + tt_col]]
                    dfsource = ColumnDataSource(data=df)
                    
                    df_dest_id= df.loc[df['YKR_ID']==element]
                    dfsource_dest_id = ColumnDataSource(data=df_dest_id)
                    # Specify the tools that we want to use
                    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
                    
                    # Flip the colors in color palette
                    palette2.reverse()
                    color_mapper = LogColorMapper(palette=palette2)
                    #color_mapper = ContinuousColorMapper(palette=palette4)
                 
                    
                    list_of_titles = ["walk_t: Travel time in minutes from origin to destination by walking",
                                                  "walk_d: Distance in meters of the walking route",
                                                "pt_r_tt: Travel time in minutes from origin to destination by public transportation in rush hour traffic(including waiting time at home)", 
                                                "pt_r_t:	 Travel time in minutes from origin to destination by public transportation in rush hour traffic(excluding waiting time at home)",
                                                "pt_r_d:	 Distance in meters of the public transportation route in rush hour traffic",
                                                "pt_m_tt: Travel time in minutes from origin to destination by public transportation in midday traffic(including waiting time at home)",
                                                "pt_m_t:	 Travel time in minutes from origin to destination by public transportation in midday traffic(excluding waiting time at home)",
                                                "pt_m_d:	 Distance in meters of the public transportation route in midday traffic",
                                                "car_r_t: Travel time in minutes from origin to destination by private car in rush hour traffic",
                                                "car_r_d: Distance in meters of the private car route in rush hour traffic",
                                                "car_m_t: Travel time in minutes from origin to destination by private car in midday traffic",
                                                "car_m_d: Distance in meters of the private car route in midday traffic"]
                                                                    
                    title=list_of_titles[tt_matrices.columns.get_loc(tt_col) - 2]
                    index=title.find('destination')
                    if 'destination' in title:
                        title_matrix=title[:index+len('destination')] + ' ' + str(element) +  title[index+len('destination'):]
                    #here, for the title. i got the location of the specified travel mode(tt_col), then, with its
        #                    with its index, i got the corresponsding location in the list which was arranged according to the
        #                    to the columns of the dataframe(tt_matrices) too. 2 is subracted(i.e -2) because, the list_of_titles
        #                    is shorter by 2, as it does not include from_id or to_id which are not variables of interest here but the travel modes only.
        
                    elif 'Distance' in title: 
                        title_matrix=title + ' to ' + str(element) 
                       
                    
                    if map_type=='interactive':
                    
                        
                        p = figure(title=title_matrix, tools=TOOLS,
                                     plot_width=800, plot_height=650, active_scroll = "wheel_zoom" )
                     
                        
                        
            #                    This can be used if you want a more generalised title
            #                    differentiating just travel times and distances and not the meanas.
            #                    if tt_col[-1]== 't':
            #                        p = figure(title="Travel times to The Grid", tools=TOOLS,
            #                               plot_width=800, plot_height=650, active_scroll = "wheel_zoom" )
            #                    elif tt_col[-1]== 'd':
            #                        p = figure(title="Travel distances to The Grid", tools=TOOLS,
            #                               plot_width=800, plot_height=650, active_scroll = "wheel_zoom" )
            #                   
                        
                        # Do not add grid line
                        p.grid.grid_line_color = None
                        
                        if sea is not None:
                            #add water
                            s= p.patches('xs', 'ys', source=sea_source, color='#6baed6', legend='Sea')
                                    
                        
                        # Add polygon grid and a legend for it
                        grid = p.patches('x', 'y', source=dfsource, name="grid",
                                 fill_color={'field': tt_col+"_ud", 'transform': color_mapper},
                                 fill_alpha=1.0, line_color="black", line_width=0.03, legend='label_' + tt_col)
                        
                        if roads is not None:
                            # Add roads
                            r = p.multi_line('xs', 'ys', source=rdfsource, color=roads_color, legend="roads")
                        if metro is not None:
                            # Add metro
                            m = p.multi_line('xs', 'ys', source=mdfsource, color=metro_color, line_dash='solid', legend="metro")
                            #other line dash option: 'solid' ,'dashed','dotted','dotdash','dashdot'

                        if train is not None:
                            # Add metro
                            tr = p.multi_line('xs', 'ys', source=tdfsource,line_cap='butt', line_width=2, line_dash='dashdot', color=train_color, legend="train")

                        
                        
                        # Modify legend location
                        p.legend.location = "top_right"
                        p.legend.orientation = "vertical"
                        
                        ghover = HoverTool(renderers=[grid])
                        ghover.tooltips=[("YKR-ID", "@from_id"),
                                        (tt_col, "@" + tt_col)]  
                        p.add_tools(ghover)
                        
#                           Insert a circle on top of the location(coords in EurefFIN-TM35FIN)
                                              
                        grid_centroid=merged_metro.loc[merged_metro['YKR_ID']==element, 'geometry'].values[0].centroid
                        dest_grid_x=grid_centroid.x 
                        dest_grid_y= grid_centroid.y
        
#                        Alternative to getting the centre of a grid:
                        #because, it  is a grid, the location of each cell has about 5 x and 
                        #y coordinates, hence, after finding the x for each grid, select 
                        #one of the x and y coordinates(the third, which is the centre of each grid) from the list.
#                        dest_grid_x = (df.loc[df["YKR_ID"]==element, 'x'].values[0])[2]
#                        dest_grid_y =  (df.loc[df["YKR_ID"]==element, 'y'].values[0])[2]
#                        

                        
                        if destination_style=='circle':
                        # Add two separate hover tools for the data
                            circle = p.circle(x=[dest_grid_x], y=[dest_grid_y], name="point", size=7, color=destination_color, legend= 'Destination')
                        
                            phover = HoverTool(renderers=[circle])
                            phover.tooltips=[("Destination Grid:", str(element))]
                            p.add_tools(phover)
                           
                        elif destination_style=='grid':
                            grid_dest_id= p.patches('x', 'y', source=dfsource_dest_id, name='grid', color=destination_color)
                        
                            ghover_dest_id = HoverTool(renderers=[grid_dest_id])
                            ghover_dest_id.tooltips=[("DESTINATION GRID", str(element))] 
                            p.add_tools(ghover_dest_id)
                       
                        
                
                      # Output filepath to HTML
                       
                        # Save the map
                        save(p, filepath + "/" +tt_col +"_" + str(element) + ".html")
                        
                    elif map_type=='static':
                        
                        
                        my_map = merged_metro.plot(column=tt_col, linewidth=0.02, legend=True, cmap="RdYlGn", scheme=class_type, k=n_classes, alpha=0.9)
                         # Add roads on top of the grid
                        if roads is not None:
                             # Add roads on top of the grid
                            # (use ax parameter to define the map on top of which the second items are plotted)
                            roads.plot(ax=my_map, color=roads_color, legend=True, linewidth=1.0)
                       
                        if metro is not None:
                            # Add metro on top of the previous map
                            metro.plot(ax=my_map, color=metro_color, legend=True, linewidth=1.2)
                        
                        if train is not None:
                            # Add metro on top of the previous map
                            train.plot(ax=my_map, color=train_color, legend=True, linestyle='dashdot', linewidth=1.2)
                                
                        
                        ## Insert a circle on top of the Central Railway Station (coords in EurefFIN-TM35FIN)
                        dest_grid_x = (df.loc[df["YKR_ID"]==element, 'x'].values[0])[2]
                        dest_grid_y =  (df.loc[df["YKR_ID"]==element, 'y'].values[0])[2]
          
                        dest_grid= gpd.GeoDataFrame()
                        
#                        Get the destination grid
                        dest_grid_loc = Point(dest_grid_x, dest_grid_y)
                        dest_grid["geometry"]=""
                        dest_grid.loc[1,"geometry"]=dest_grid_loc
                        #r_s["geometry"]=r_s["geometry"].to_crs(crs=gridCRS)
                        
                        dest_grid.plot(ax=my_map, color= destination_color, legend=True, linewidth=1.5)
                        
       
#                        plt.legend(["roads", "metro line",'train'])
                        #title_map=list_of_titles[tt_matrices.columns.get_loc(tt_col) - 2]
                        plt.title(title_matrix[:59] + '\n'+ title_matrix[59:], fontsize=8)
                        
                        #north arrow in the southeastern corner
                        my_map.text(x=df['x'].max()[2],y=df['y'].min()[2], s='N\n^', ha='center', fontsize=23, family='Courier new', rotation = 0)
                        
                        
                        #move legend to avoid overlapping the map
                        lege = my_map.get_legend()
                        lege.set_bbox_to_anchor((1.60, 0.9))
                        
                        #resize the map to fit in thr legend.
                        mapBox = my_map.get_position()
                        my_map.set_position([mapBox.x0, mapBox.y0, mapBox.width*0.6, mapBox.height*0.9])
                        my_map.legend(loc=2, prop={'size': 3})  
#                        plt.gca().add_artist(plt.legend(["roads", "metro line",'train']))
                        
                        
                        #plt.show()
                        
                        # Save the figure as png file with resolution of 300 dpi
                        outfp = filepath + "/" + "static_map_"+tt_col +"_" + str(element) + ".png"
                        plt.savefig(outfp, dpi=300)
        
                    
        #check if all of the imputed values does not exist
        check_input(userinput=userinput, main_list=m_list)
        
        
        
        
        
# =============================================================================
# 4. AccessViz can also compare travel times or travel distances between two 
# different travel modes (more than two travel modes are not allowed). Thus IF 
# the user has specified two travel modes (passed in as a list) for the AccessViz, 
# the tool will calculate the time/distance difference of those travel modes into 
# a new data column that should be created in the Shapefile. The logic of the 
# calculation is following the order of the items passed on the list where first 
# travel mode is always subtracted by the last one: travelmode1 - travelmode2. 
# The tool should ensure that distances are not compared to travel times and vice 
# versa. If the user chooses to compare travel modes to each other, you should 
# add the travel modes to the filename such as Accessibility_5797076_pt_vs_car.shp. 
# If the user has not specified any travel modes, the tool should only create the 
# Shapefile but not execute any calculations. It should be only possible to compare 
# two travel modes between each other at the time. Accepted travel modes are the 
# same ones that are found in the actual TravelTimeMatrix file (pt_r_tt, car_t, etc.). 
# If the user specifies something else, stop the program, and give advice what are 
# the acceptable values.
# =============================================================================




    def compare_travel_modes(zipped_data_path,userinput, filepath, grid_shp, sea=None, roads=None,
        train=None, metro=None,compare_mod=[], create_shapefiles=True, visualisation=True, 
        map_type='interactive', destination_style='circle', destination_color='blue',
        roads_color='grey', metro_color='red', train_color='yellow',classification='pysal_class', 
        class_type="Quantiles", n_classes=8, multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, 
        truncate=True, pct_classes=[1,10,50,90,99,100], class_lower_limit="", 
        class_upper_limit="", class_step="", label_lower_limit="", label_upper_limit="", 
        label_step=""):
        """
             The function compares travel times or travel distances between two different travel modes 
             (more than two travel modes are not allowed). Thus IF the user has specified two travel modes '
             (passed in as a list), the tool will calculate the time/distance difference 
             of those travel modes into a new data column that should be created in the Shapefile. The logic 
             of the calculation is following the order of the items passed on the list where first travel mode 
             is always subtracted by the last one: travelmode1 - travelmode2. The tool ensures that
             distances are not compared to travel times and vice versa. If the user chooses to compare travel
             modes to each other, the function adds the travel modes to the filename.  If the user specifies
             just one travel mode, error is raised and suggestion is given on the right thing to do.
             If the user has not specified any travel modes, the tool only creates the Shapefile but not 
             execute any calculations and also states this. It is only possible to compare two travel modes between each 
             other at the time. Accepted travel modes are the same ones that are found in the actual 
             TravelTimeMatrix file (pt_r_tt, car_t, etc.). If something else is specified, AccessViz error is raised and 
             the function suggests the acceptable values.
             
            The output maps are saved into a folder that is specified. The output maps
            can be either static or interactive and user can choose which one with a parameter. 
            By using the parameters, you can freely design yourself the style of the map, 
            travel time intervals (classes) etc.  You can decided to either visualise joined travel mode or not.
            You can also choose what kind of classificaation(either pysal class or User_Defined). The pysal_class
            option uses pysal classification which can be found here:http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify.
            With the user_defined classification, you can choose yourself how you wish to make the classifixation,
            inlcuding the lowest limit, uppermost limit and also the interval/break. This can also be done as you want it on the label/legend.
            the uppermost level shows those values that are greater than that level(e.g 60< or >60).
            This function also tells if a grid is empty(i.e no data). This grids with nodata have -1 value
            
            This creates Shapefiles from the chosen Matrix text tables
            (e.g. travel_times_to_5797076.txt) by joining the Matrix file with MetropAccess_YKR_grid 
            Shapefile where from_id in Matrix file corresponds to YKR_ID in the Shapefile. The tool 
            saves the result in the output-folder that user has defined. The output files 
             are named in a way that it is possible to identify the ID from the name (e.g. 5797076).
             
            zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.
            
            userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425].
            
            compare_mod: a list of the travel modes to be compared e.g(['pt_r_tt', 'car_r_t']). 
            
            create_shapefiles(default=True): this is used to specify if the shapefiles of the joined metropo_Acees grid
            and the travel time matrices should be created. if True, the compared mode(i.e travelmode1 - travelmode2) will be included in the calculation.
            
            visualisation(default=True): used to specify if you want to visualise the compared travel mode.
            
            grid_shp= this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time matrix(ces).
            
            filepath: output filepath where the maps will be extracted to.
                 
            sea(default value=None): this is the shapefile of the sea around the region which will be displayed on the map if specified.
            
            roads(default value=None): this is the shapefile of the roads in the region which will be displayed on the map if specified.
            
            train(default value=None): this is the shapefile of the train rail line in the region which will be displayed on the map if specified.
            
            metro(default value=None): this is the shapefile of the metro rail line in the region which will be displayed on the map if specified.
                 
            roads_color, metro_color, train_color: these are used to choose the color for the various transportation means.
            
            map_type: options are(interactive or static). 
            
            destination_style(default= circle): options are(grid or cycle). This shows how you wish to highlight the destination grid.
        
            destination_color: color of the highlighted destination.
            
            classification(default='pysal_class'): options are('pysal_class' or 'user_defined').
            
            class_type(default="Quantiles"): Options include, 'Quantiles', 'Box_Plot', 'Equal_Interval, 'Fisher_Jenks',
                                            'HeadTail_Breaks','Jenks_Caspall', 'Max_P_Classifier', 'Natural_Breaks', 'Percentiles', and 'Std_Mean'.
                                            For more information: http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify
    
            n_classes(default=8): number of classes.
            
            multiples: used in Standard Deviation and Mean Map Classification(i.e Std_Mean). 
            
            pct_classes: used in for Percentiles Map Classification. In the pysal documentation, this is parameter is is 'pct'.
            
            pct: Fisher Jenks optimal classifier - mean based using random sample. 
            
            hinge: used in Box_Plot Map Classification.
            
            truncate: used in Fisher Jenks optimal classifier - mean based using random sample. 
            
            class_lower_limit, class_upper_limit, class_step: should be used for making the breaks for manually classifying the travel mode column.
                                                                
            
            label_lower_limit, label_upper_limit, label_step: This can be used for making the legend.
            label_lower_limit is the lowest limit allowed in the legen, label_step is the label/legend class interval, while
            the label_upper_limit level shows those values that are greater than that level(e.g 60< or >60)


        """

        if create_shapefiles==False and visualisation==True and not compare_mod:
            raise AccessVizError("When visualising, you have to specify the two travel modes to compare. Check the 'userinput' and include, two travel modes")
        if not userinput:
            raise AccessVizError("You have not specified any travel time matrix to be merged with the grid. \n Check the parameter -'userinput'- and include a valid travel time matrix")
    
        if create_shapefiles==False and visualisation==False:
            raise AccessVizError("You have not specified any action to create shapefiles or visualise. \n Check the parameters!. Either 'create_shapefiles' or 'visualisation' has to be True.")
        
        grid_shp=grid_shp.to_crs(from_epsg(3067))
        
        
        # ============================================================================================================================================
        # H.T. If the user creates a static map, these GeoJSONDataSource conversions are not needed. Hence, these lines should be executed only if `map_type='interactive'`
        # ============================================================================================================================================
        
        if roads is None:
            print('You have not included the roads route')
        else:
            roads=roads.to_crs(from_epsg(3067))
            
            rdfsource = GeoJSONDataSource(geojson=roads.to_json())
#                   #Calculate the x and y coordinates of the roads (these contain MultiLineStrings).
#                roads['x'] = roads.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#                                
#                roads['y'] = roads.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#                
#                 # Include only coordinates from roads (exclude 'geometry' column)
#                rdf = roads[['x', 'y']]
#                #this two rows had nan values which prevented me from saving the plot. I got the error:
#                #ValueError: Out of range float values are not JSON compliant.
#                #therefore, I had to remove the two rows
#                rdf.drop(39, inplace=True)
#                rdf.drop(158, inplace=True)
            
         
        if train is None:
            print('You have not included the train route')
        else:
            train=train.to_crs(from_epsg(3067))
            tdfsource = GeoJSONDataSource(geojson=train.to_json())
            
#                train['x'] = train.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#                
#                train['y'] = train.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#               
#                
#                tdf = train[['x','y']]
#                tdfsource = ColumnDataSource(data=tdf)
            
        if metro is None:
            print('You have not included the metro route')
        else:
            metro=metro.to_crs(from_epsg(3067))
            mdfsource = GeoJSONDataSource(geojson=metro.to_json())
            
#                  #Calculate the x and y coordinates of metro.
#                metro['x'] = metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
#                
#                metro['y'] = metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
#                              
#                # Include only coordinates from metro (exclude 'geometry' column)
#                mdf = metro[['x','y']]
#                mdfsource = ColumnDataSource(data=mdf)
            
        if sea is None:
            print('You have not included the metro route')
        else:
   
            sea=sea.to_crs(from_epsg(3067))
            
            sea_source = GeoJSONDataSource(geojson=sea.to_json())
                                   

        #read the zipped travel time matrices
        data_zip = zipfile.ZipFile(zipped_data_path, "r")

        namelist=data_zip.namelist()
        m_list=[]
               #iterate over the userinput, to get all its element/values
        for element in userinput:
            
            #create a list of destination grid IDs from all the file names
            dest_ids=[i[-11:-4] for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            dest_ids_file=[i for i in namelist if i[-4:]=='.txt' and 'METADATA' not in i]
            
#            check if the specified grid id(i.e userinput) is in the list of ids created earlier
            if str(element) not in dest_ids:
                print("WARNING: The specified matrix {0} is not available\n".format(element))
                
            else:
                print("Matrix {0} is available".format(element))
                m_list.append(element)
                
                #check for the progress
                print("Processing file travel_times_to_{0}.txt.. Progress: {1}/{2}".format(element,len([i for i in range(len(m_list))]), len(userinput)))
                
                
#                find the index of the grid ID(element) in the destination ids list created earlier.
                element_index= dest_ids.index(str(element))
                
                #use this to find the corresponding file in the destination ids filename list created earlier
                element_file=dest_ids_file[element_index]
                 
                bytes = data_zip.read(element_file)
                    #print the file size
                print('has',len(bytes),'bytes\n')
               
                #read the data
                
                # =========================================================================
                # H.T. The 'element_file' is not a valid filepath and it produces and error
                # =========================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                    
                # =======================================================================
                # H.T. When reading bytes you need to read the 'bytes' with BytesIO
                # =======================================================================
                
                #read the data
                #tt_matrices= pd.read_csv(element_file, sep=";")
                tt_matrices= pd.read_csv(BytesIO(bytes), sep=";")
                
                column_list=[i for i in tt_matrices.columns]
                
#                create a list of elements in the listed travel modes but not a column name in the travel time dataframe.
                absent_col= [i for i in compare_mod if i not in column_list]
                
                #find if any of the items of the listed transport modes is/are not column(s) in the matrix dataframe
                if any(x not in column_list for x in compare_mod):
                    if len(absent_col)==1:
                        raise AccessVizError("The specified travel mode", str(absent_col).strip('[]'), "is not available. Accepted travel modes include:", str([i for i in tt_matrices.columns][2:]).strip('[]'))
#                    for plural(i.e more than one specified wrong travel modes)
                    elif len(absent_col)>1:
                        raise AccessVizError("The specified travel modes:", str(absent_col).strip('[]'), ", are not available. Accepted travel modes include:", str([i for i in tt_matrices.columns][2:]).strip('[]'))

                else:
                    if len(compare_mod)> 2:
                        raise AccessVizError("WARNING: More than two travel modes are not allowed. Specify only two similar travel modes(i.e either distance or time but not both at thesame time)")

                    elif len(compare_mod)==2:
                        if compare_mod[0]==compare_mod[1]:
                            raise AccessVizError("WARNING: You are comparing the same travel mode\n")

                        elif compare_mod[0][-1] != compare_mod[1][-1]:
                            raise AccessVizError("WARNING!:You cannot compare Travel Distance with Travel Time!!!\n")

                    elif len(compare_mod)==1:
                            raise AccessVizError("WARNING: You have specified just one travel mode. \n One travel mode is not allowed. \n Specify two travel modes in the list")
 
                   
                      
                    
                #This is done to handle matrices with nodata at all. e.g: matrix"6016696"
                if tt_matrices['to_id'].max()==-1:
                    print('The MATRIX- {0} is empty and has nodata\n'.format(element))
                    
                else:
                    merged_metro = pd.merge(grid_shp,tt_matrices,  left_on="YKR_ID", right_on="from_id")
                    
                    #check if list is empty.
                    if not compare_mod and create_shapefiles==True:
                      print('NOTE: You did not specify any travel mode. Therefore, only the travel time matrix' , element, 'and the grid shapefile will be produced ')
                      merged_metro.to_file(driver = 'ESRI Shapefile', filename= filepath+"/travel_times_to_" + str(element) + ".shp")
                
#                otherwise, if the right travel modes are specified, find their difference
                    else:
                        mode1=compare_mod[0] 
                        mode2=compare_mod[1]
                        tt_col=mode1+'_vs_' + mode2
                        
                        #Next I will calculate the difference but be mindful of the empty grids.
                        #when either or both of the modes is/are empty, the resultant difference
                        #should be nodata(i.e -1)
                        #create an empty column to imput the mode difference
                                                
                        merged_metro[tt_col]=""
                        mode1_vs_mode2=[]
                        for idx, rows in merged_metro.iterrows():
                            if rows[mode1]==-1 or rows[mode2]==-1:
                                difference=-1
                                mode1_vs_mode2.append(difference)
                            else:
                                difference= rows[mode1]-rows[mode2]
                                mode1_vs_mode2.append(difference)
                        merged_metro[tt_col]=mode1_vs_mode2


                        # ===========================================================================================================================================================================
                        # H.T. The above works but is unnecessarily complicated and most likely a bit slow approach.
                        # You could have dealed with the NoData values (-1) by replacing the -1 values with None and after
                        # this you could have only calculated the difference using basic calculation functionalities of Pandas ==> merged_metro[tt_col] = merged_metro[mode1] - merged_metro[mode2]
                        # ===========================================================================================================================================================================
                        
                                                
# =============================================================================
#                            alternative
#                             mode1_vs_mode2=[]
#                             for i in range(len(data)):
#                                 print(i)
#                                 if data.loc[i, "pt_r_tt"]!=-1 or data.loc[i,"car_r_t"]!=-1:
#                                     dat= data["pt_r_tt"] - data["car_r_t"]
#                                     mode1_vs_mode2.append(dat)
#                                 elif data.loc[i, "pt_r_tt"]==-1 or data.loc[i,"car_r_t"]==-1:
#                                     dat=-1
#                                     mode1_vs_mode2.append(dat)
#                             data["pt_diff_car_tt"] = mode1_vs_mode2
# =============================================================================
         
                        if create_shapefiles==True:
                            #now, export the result
                            merged_metro.to_file(driver = 'ESRI Shapefile', filename= filepath+"/travel_times_to_" + tt_col + "_" +str(element) + ".shp")
                        
                        
                        if visualisation==True:
                            #However, for the visualisation, there is need to exclude the nodata grids with -1
                            merged_metro= merged_metro.loc[merged_metro[ tt_col]!=-1]

                        
                             #Calculate the x and y coordinates of the grid. the create getCoords function in get_geom module is used.
                            merged_metro['x'] = merged_metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="x", axis=1)
                
                            merged_metro['y'] = merged_metro.apply(get_geom.getCoords, geom_col="geometry", coord_type="y", axis=1)
                        
                       
                            if classification =='pysal_class':
                                if class_type == "Natural_Breaks":
                                    classifier = ps.Natural_Breaks.make(k=n_classes)
                                elif class_type == "Equal_Interval":
                                    classifier = ps.Equal_Interval.make(k=n_classes)
                                elif class_type == "Box_Plot":
                                    classifier = ps.Box_Plot.make(hinge)
                                elif class_type == "Fisher_Jenks":
                                    classifier = ps.Fisher_Jenks.make(k=n_classes)
                #                elif class_type == "Fisher_Jenks_Sampled":
                #                    classifier = ps.Fisher_Jenks_Sampled.make(k=n_classes, pct=0.1)
                                elif class_type == "HeadTail_Breaks":
                                    classifier = ps.HeadTail_Breaks.make(k=n_classes)
                                elif class_type == "Jenks_Caspall":
                                    classifier = ps.Jenks_Caspall.make(k=n_classes)
                                elif class_type == "Jenks_Caspall_Forced":
                                    classifier = ps.Jenks_Caspall_Forced.make(k=n_classes)
                                elif class_type == "Quantiles":
                                    classifier = ps.Quantiles.make(k=n_classes)
                                elif class_type == "Percentiles":
                                    classifier = ps.Percentiles.make(pct_classes)
                                elif class_type == "Std_Mean":
                                    classifier = ps.Std_Mean.make(multiples)
                                mode_classif = merged_metro[[tt_col]].apply(classifier)
                               
                                
                                #Rename the columns of our classified columns.
                                mode_classif.columns = [tt_col+"_ud"]
                                
                                
                                #Join the classes back to the main data.
                                merged_metro = merged_metro.join(mode_classif)
                                
                                    
                                merged_metro['label_' + tt_col ] = mode_classif
                                    
                                
                            
                            elif classification == "User_Defined":
                                 #Next, classify the travel times with x(class_step) minute intervals until y(class_upper_limit) minutes.
                
                                #create a list of values where minumum value is class_lower_limit, maximum value is class_upper_limit and step is class_step.
                                breaks = [x for x in range(class_lower_limit, class_upper_limit, class_step)]
                                #Now we can create a pysal User_Defined classifier and classify our travel time values.
                                
#                                create the classifier
                                classifier = ps.User_Defined.make(bins=breaks)
                            
                               
#                                apply the classifier to the desired column which is the travel modes difference
                                mode_classif = merged_metro[[tt_col]].apply(classifier)
                                
                                
                                #Rename the columns of the classified column.
                                mode_classif.columns = [tt_col+"_ud"]
                                
                                
                                #Join the classes back to the main data.
                                merged_metro = merged_metro.join(mode_classif)
                                
                                #Create names for the legend (until certain minutes). The following will produce: e.g["0-5", "5-10", "10-15", ... , "60 <"]. 
                                #inside the range function, the label_lower_limit is added to the 
                                #label_step to give the stated lower_limit because they are first subtracted(i.e x - label_step)
                                #at the beginning.
                                names = ["%s-%s" % (x-label_step, x) for x in range(label_lower_limit + label_step, label_upper_limit, label_step)]
                                #         ["{0}kk{1}".format(x-5,x) for x in range(5, 200, 5)]   #alternative
                                
# =============================================================================
#                                you can try the below for further clarification
#                                 upper_limit = 60
#                                 step = 15
#                                 lower_limit=0
#                                 names = ["%s-%s " % (x-step, x) for x in range(lower_limit+ step, upper_limit, step)]
# =============================================================================
                               
                                
                                
                                
                                #Add legend label for over certain point.
                                names.append("%s<" % label_upper_limit)
                                
                                #Assign legend names for the classes.
                                merged_metro['label_' + tt_col ] = None
                                
                                #Update rows with the class-names.
                                for i in range(len(names)):
                                    merged_metro.loc[merged_metro[tt_col+"_ud"] == i, 'label_' + tt_col] = names[i]
                                   
                                #Update all cells that didn’t get any value with "label_upper_limit" e.g "40 <"
                                merged_metro['label_' + tt_col] = merged_metro['label_' + tt_col].fillna("%s<" % label_upper_limit)
                                
                            #Finally, we can visualize our layers with Bokeh, add a legend for travel times 
                            #and add HoverTools for Destination Point and the grid values (travel times).
                            # Select only necessary columns for our plotting to keep the amount of data minumum
                            df = merged_metro[['x','y',"YKR_ID",mode1,mode2, tt_col,tt_col+"_ud","from_id" ,'label_' + tt_col]]
                            dfsource = ColumnDataSource(data=df)
#                                dfsource = GeoJSONDataSource(geojson=merged_metro.to_json())
                            
                            df_dest_id= merged_metro.loc[merged_metro['YKR_ID']==element]
                            dfsource_dest_id = ColumnDataSource(data=df_dest_id)
#                                dfsource_dest_id = GeoJSONDataSource(geojson=df_dest_id.to_json())
                        
                            
                        
                            
                            
                            
                            # Specify the tools that we want to use
                            TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
                            
                            # Flip the colors in color palette
                            palette2.reverse()
                            color_mapper = LogColorMapper(palette=palette2)
                            #color_mapper = ContinuousColorMapper(palette=palette4)
                            
                            
                            
                         #This part is for automating the title
                            
                            list_of_titles = ["walk_t: Travel time in minutes from origin to destination by walking",
                                              "walk_d: Distance in meters of the walking route",
                                            "pt_r_tt: Travel time in minutes from origin to destination by public transportation in rush hour traffic(including waiting time at home)", 
                                            "pt_r_t: Travel time in minutes from origin to destination by public transportation in rush hour traffic(excluding waiting time at home)",
                                            "pt_r_d: Distance in meters of the public transportation route in rush hour traffic",
                                            "pt_m_tt: Travel time in minutes to destination by public transportation in midday traffic(including waiting time at home)",
                                            "pt_m_t: Travel time in minutes from origin to destination by public transportation in midday traffic(excluding waiting time at home)",
                                            "pt_m_d: Distance in meters of the public transportation route in midday traffic",
                                            "car_r_t: Travel time in minutes from origin to destination by private car in rush hour traffic",
                                            "car_r_d: Distance in meters of the private car route in rush hour traffic",
                                            "car_m_t: Travel time in minutes from origin to destination by private car in midday traffic",
                                            "car_m_d: Distance in meters of the private car route in midday traffic"]
                                                                
                            title_mod1=list_of_titles[tt_matrices.columns.get_loc(mode1) - 2]
                            title_mod2=list_of_titles[tt_matrices.columns.get_loc(mode2) - 2]
                            index=title_mod1.find('destination')
                            title_mat=title_mod1[:index+len('destination')] + ' ' + str(element) +  title_mod1[index+len('destination'):]
                            index_mode1 = title_mat.find(mode1 + str(':'))
                               
                            if 'destination' in title_mod1:
                                 if mode2[:2]=='pt':
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+  title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('public'):]).title() 
                                 elif mode2[:4]=='walk':
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+  title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('walking'):]).title()
                                 elif mode2[:3]=="car":
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+  title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('private'):]).title() 
                                    
                                        
                            
                            #here, for the title. i got the location of the specified travel mode(tt_col), then, with its
                #                    with its index, i got the corresponsding location in the list which was arranged according to the
                #                    to the columns of the dataframe(tt_matrices) too. 2 is subracted(i.e -2) because, the list_of_titles
                #                    is shorter by 2, as it does not include from_id or to_id which are not variables of interest here but the travel modes only.
                
                            elif 'Distance' in title_mod1: 
                                title_mat=title_mod1 + ' to ' + str(element) 
                                if mode2[:2]=='pt':
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+  title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('public'):]).title() 
                                elif mode2[:4]=='walk':
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+   title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('walking'):]).title() 
                                elif mode2[:3]=="car":
                                    title_matrix=  title_mat[:index_mode1 + len(mode1)] + ' vs ' + mode2 + (': Difference between'+  title_mat[index_mode1 + len(mode1)+1:] + ' vs ' + title_mod2[title_mod2.find('private'):]).title() 
                                    
                                
                               
                            
                            if map_type=='interactive':
                            
                                
                                p = figure(title=tt_col, tools=TOOLS,
                                             plot_width=850, plot_height=650, active_scroll = "wheel_zoom" )
                             
                                
                                #p.title.text=title_matrix
                                p.title.text_color = "blue"
                                p.title.text_font = "times"
                                p.title.text_font_style = "italic"
                                p.title.text_font_size='20px'
                                p.title.offset=-5.0
                                
                                p.add_layout(Title(text=title_matrix[len(tt_col)+1:][211:], text_font_size="11pt", text_font_style="bold"), 'above')   #sub
                                p.add_layout(Title(text=title_matrix[len(tt_col)+1:][102:211], text_font_size="11pt", text_font_style="bold"), 'above')    #sub
                                p.add_layout(Title(text=title_matrix[len(tt_col)+1:][:102], text_font_size="11pt",text_font_style="bold"),'above')       #main
                               
                     #                    This can be used if you want a more generalised title
                    #                    differentiating just travel times and distances and not the meanas.
                    #                    if tt_col[-1]== 't':
                    #                        p = figure(title="Travel times to The Grid", tools=TOOLS,
                    #                               plot_width=800, plot_height=650, active_scroll = "wheel_zoom" )
                    #                    elif tt_col[-1]== 'd':
                    #                        p = figure(title="Travel distances to The Grid", tools=TOOLS,
                    #                               plot_width=800, plot_height=650, active_scroll = "wheel_zoom" )
                    #                   
                                
                                # Do not add grid line
                                p.grid.grid_line_color = None
                                
                                
                                if sea is not None:
                                    #add water
                                    s= p.patches('xs', 'ys', source=sea_source, color='#6baed6', legend='Sea')
                                
                                # Add polygon grid and a legend for it
                                grid = p.patches('x', 'y', source=dfsource, name="grid",
                                         fill_color={'field': tt_col+"_ud", 'transform': color_mapper},
                                         fill_alpha=1.0, line_color="black", line_width=0.03, legend='label_' + tt_col)
                                if roads is not None:
                                    # Add roads
                                    #for GeoJSONDataSource xs and ys are used instead of x and y if I had used the normal way in bokeh
                                    r = p.multi_line('xs', 'ys', source=rdfsource, color=roads_color, legend="roads")
                                if metro is not None:
                                    # Add metro
                                    m = p.multi_line('xs', 'ys', source=mdfsource, color=metro_color, line_dash='solid', legend="metro")
                                    #other line dash option: 'solid' ,'dashed','dotted','dotdash','dashdot'

                                if train is not None:
                                    # Add train
                                    tr = p.multi_line('xs', 'ys', source=tdfsource,line_cap='butt', line_width=2, line_dash='dashdot', color=train_color, legend="train")

 
                                    

                                
                                # Modify legend location
                                p.legend.location = "top_right"
                                p.legend.orientation = "vertical"
                                
                                ghover = HoverTool(renderers=[grid])
                                ghover.tooltips=[("YKR-ID", "@from_id"),
                                                 (mode1, "@"+ mode1),
                                                 (mode2, "@"+ mode2),
                                                (mode1 +" minus "+ mode2, "@" + tt_col)]  
                                p.add_tools(ghover)
                                
                                  # Insert a circle on top of the location(coords in EurefFIN-TM35FIN)
                                #print(element)
                                #because, it  is a grid, the location of each cell has about s x and 
                                #y coordinates, hence, after finding the x for each grid, select 
                                #one of the x and y coordinates(the third, which is the centre of each grid) from the list.
                                #dest_grid_x = (df.loc[df["YKR_ID"]==element, 'x'].values[0])[2]
                                #dest_grid_y =  (df.loc[df["YKR_ID"]==element, 'y'].values[0])[2]
                                
                                #Alternative to getting the centre of a grid:
                                grid_centroid=merged_metro.loc[merged_metro['YKR_ID']==element, 'geometry'].values[0].centroid
                                dest_grid_x=grid_centroid.x 
                                dest_grid_y= grid_centroid.y
                                
                                if destination_style=='circle':
                                # Add two separate hover tools for the data
                                    circle = p.circle(x=[dest_grid_x], y=[dest_grid_y], name="point", size=7, color=destination_color, legend= 'Destination')
                                
                                    phover = HoverTool(renderers=[circle])
                                    phover.tooltips=[("Destination Grid:", str(element))]
                                    p.add_tools(phover)
                                   
                                elif destination_style=='grid':
                                    grid_dest_id= p.patches('x', 'y', source=dfsource_dest_id, name='grid', color=destination_color)
                                
                                    ghover_dest_id = HoverTool(renderers=[grid_dest_id])
                                    ghover_dest_id.tooltips=[("DESTINATION GRID", str(element))] 
                                    p.add_tools(ghover_dest_id)
                               
                                
                        
                              # Output filepath to HTML
                               
                                # Save the map
                                save(p, filepath + "/" +mode1 + "_vs_" + mode2 +"_" + str(element) + ".html")
                                
                            elif map_type=='static':
                                
                                
                                my_map = merged_metro.plot(column=tt_col, linewidth=0.02, legend=True, cmap="RdYlGn", scheme=class_type, k=n_classes, alpha=0.9)
                                
                                if roads is not None:
                                     # Add roads on top of the grid
                                    # (use ax parameter to define the map on top of which the second items are plotted)
                                    roads.plot(ax=my_map, color=roads_color, legend=True, linewidth=1.2)
                               
                                if metro is not None:
                                    # Add metro on top of the previous map
                                    metro.plot(ax=my_map, color=metro_color, legend=True, linewidth=2.0)
                                
                                if train is not None:
                                    # Add metro on top of the previous map
                                    train.plot(ax=my_map, color=train_color, legend=True, linewidth=2.0)
                            
                                
                                ## Insert a circle on top of the Central Railway Station (coords in EurefFIN-TM35FIN)
                                dest_grid_x = (df.loc[df["YKR_ID"]==element, 'x'].values[0])[2]
                                dest_grid_y =  (df.loc[df["YKR_ID"]==element, 'y'].values[0])[2]
                  
                                dest_grid= gpd.GeoDataFrame()
                                
                                dest_grid_loc = Point(dest_grid_x, dest_grid_y)
                                dest_grid["geometry"]=""
                                dest_grid.loc[1,"geometry"]=dest_grid_loc
                                #r_s["geometry"]=r_s["geometry"].to_crs(crs=gridCRS)
                                
                                dest_grid.plot(ax=my_map, color= "blue", legend=True, linewidth=1.5)
                                
               
                                #plt.legend(["roads", "metro line","Rautatientori"])
                                #title_map=list_of_titles[tt_matrices.columns.get_loc(tt_col) - 2]
                                plt.title(textwrap.fill(title_matrix, 65), fontsize=8)
                                

                                #north arrow in the southeastern corner
                                my_map.text(x=df['x'].max()[2],y=df['y'].min()[2], s='N\n^', ha='center', fontsize=23, family='Courier new', rotation = 0)
                                
                                
                                #move legend to avoid overlapping the map
                                lege = my_map.get_legend()
                                lege.set_bbox_to_anchor((1.60, 0.9))
                                
                                #resize the map to fit in thr legend.
                                mapBox = my_map.get_position()
                                my_map.set_position([mapBox.x0, mapBox.y0, mapBox.width*0.6, mapBox.height*0.9])
                                my_map.legend(loc=2, prop={'size': 3})                
                                
#                                    plt.show()
                                
                                # Save the figure as png file with resolution of 300 dpi
                                outfp = filepath + "/" + "static_map_"+ mode1 + "_vs_" + mode2 +"_" + str(element) + ".png"
                                plt.savefig(outfp, dpi=300)
                
                                    
        #check if all of the imputed values does not exist
        check_input(userinput=userinput, main_list=m_list)
                       
        #tell the user if no grid ID has been specified and the action taken as a result.                 
        merged_files=[i for i in userinput if i in m_list]
        if not compare_mod:
            if len(userinput)==1:
                
                print("NOTE: You have not specified the travel modes to compare, hence, the merged shapefile",str(merged_files).strip("[]"), "alone was produced")
            elif len(userinput)>1:
                print("NOTE: You have not specified the travel modes to compare, hence, the merged shapefiles- {0} -alone were produced".format(str(merged_files).strip("[]")))
  


  
   
    