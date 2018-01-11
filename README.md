# Final Assignment

Read the final assignment instructions from the [https://autogis.github.io](https://automating-gis-processes.github.io/2017/lessons/FA/final-assignment.html).

You should upload all your codes into this repository and write a **good documentation** how everything works.

**AccessViz**
-      _extract_prompt(zipped_data_path, filepath, sep=";", file_format=".txt",separate_folders=False):_
       
 This function extracts matrices(files) from the zipped Helsinki Region Travel
 Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
 the specified input is not included in the matrices
 specified by use. 

 The function has thesame function as the function 'extract_files'. The only difference is that the user is prompted to input the            values which should be separated by comma(,).

 -  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

 filepath: output filepath where the matrices files will be extracted to.

 sep(e.g ',' ,';', '\t)' : the separator of the columns of the extracted files. This works only if the files are extracted into              thesame folder, i.e separate_folder=False.

 file_format(e.g. .txt, .csv): format of the extracted travel time matrices. This is also works only if the files are extracted            into thesame folder, i.e separate_folder=False.

 separate_folder(True/False): this determines if the files should be extracted into same folder or separate folders. Default             value is False.    




-      _extract(zipped_data_path, filepath,userinput, sep=";", file_format=".txt", separate_folders=False):_

The function has thesame function as the function 'extract_prompt'. The only difference is that the user is prompted to input           the values which should be separated by comma(,).
This function extracts matrices(files) from the zipped Helsinki Region Travel
Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
the specified input is not included in the matrices
specified by use. 

The function has thesame function as the function 'extract_files'. The only difference is that the user is prompted to input the          values which should be separated by comma(,).

zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.

filepath: output filepath where the matrices files will be extracted to.

userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]

sep(e.g ',' ,';', '\t)' : the separator of the columns of the extracted files. This works only if the files are extracted into            thesame folder, i.e separate_folder=False.

file_format(e.g. .txt, .csv): format of the extracted travel time matrices. This is also works only if the files are extracted            into thesame folder, i.e separate_folder=False.

separate_folder(True/False): this determines if the files should be extracted into same folder or separate folders. Default             value is False.    


create_shp(zipped_data_path,userinput, grid_shp, filepath, separate_folder=False):

This creates Shapefiles from the chosen Matrix text tables
(e.g. travel_times_to_5797076.txt) by joining the Matrix file with MetropAccess_YKR_grid 
Shapefile where from_id in Matrix file corresponds to YKR_ID in the Shapefile. The tool 
saves the result in the output-folder that user has defined. The output files 
are named in a way that it is possible to identify the ID from the name (e.g. 5797076).

zipped_data_path: This is the path to the zipped Helsinki travel time matrices data which should be specified.

userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]

grid_shp= this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time                   matrix(ces).

filepath: output filepath where the matrices files will be extracted to.

separate_folder: this determines if the files should be extracted into same folder or separate folders.

         
         
         
 -     _show_travel_mode(zipped_data_path,userinput, tt_col, filepath, grid_shp, sea=None, roads=None,train=None, 
            metro=None, roads_color='grey', metro_color='red', 
            train_color='blue',map_type='interactive', destination_style='circle', destination_color='blue',       
            classification='pysal_class', class_type="Quantiles", n_classes=8,
            multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, truncate=True, 
            pct_classes=[1,10,50,90,99,100],
            class_lower_limit="", class_upper_limit="", class_step="", 
            label_lower_limit="", label_upper_limit="", label_step=""):_
            
            
This visualises the travel times of selected YKR_IDs based on the travel mode that the 
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

train(default value=None): this is the shapefile of the train rail line in the region which will be displayed on the map if           specified.

metro(default value=None): this is the shapefile of the metro rail line in the region which will be displayed on the map if             specified.

roads_color, metro_color, train_color: these are used to choose the color for the various transportation means.

map_type: options are(interactive or static). 

destination_style(default= circle): options are(grid or cycle). This shows how you wish to highlight the destination grid.

destination_color: color of the highlighted destination.

classification(default='pysal_class'): options are('pysal_class' or 'user_defined').

class_type(default="Quantiles"): Options include, 'Quantiles', 'Box_Plot', 'Equal_Interval, 'Fisher_Jenks',
                              'HeadTail_Breaks','Jenks_Caspall', 'Max_P_Classifier', 'Natural_Breaks', 'Percentiles', and                                             'Std_Mean'.

                              For more information:       http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify

n_classes(default=8): number of classes.

multiples: used in Standard Deviation and Mean Map Classification(i.e Std_Mean). 

pct_classes: used in for Percentiles Map Classification. In the pysal documentation, this is parameter is is 'pct'.

pct: Fisher Jenks optimal classifier - mean based using random sample. 

hinge: used in Box_Plot Map Classification.

truncate: used in Fisher Jenks optimal classifier - mean based using random sample. 

class_lower_limit, class_upper_limit, class_step: should be used for making the breaks for manually classifying the travel                mode column.                                                

label_lower_limit, label_upper_limit, label_step: This can be used for making the legend.
label_lower_limit is the lowest limit allowed in the legen, label_step is the label/legend class interval, while
the label_upper_limit level shows those values that are greater than that level(e.g 60< or >60)



-      _compare_travel_modes(zipped_data_path,userinput, filepath, grid_shp, sea=None, roads=None,
        train=None, metro=None,compare_mod=[], create_shapefiles=True, visualisation=True, 
        map_type='interactive', destination_style='circle', destination_color='blue',
        roads_color='grey', metro_color='red', train_color='yellow',classification='pysal_class', 
        class_type="Quantiles", n_classes=8, multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, 
        truncate=True, pct_classes=[1,10,50,90,99,100], class_lower_limit="", 
        class_upper_limit="", class_step="", label_lower_limit="", label_upper_limit="", 
        label_step="")_
        
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


