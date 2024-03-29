# Final Assignment

Read the final assignment instructions from the [https://autogis.github.io](https://automating-gis-processes.github.io/2017/lessons/FA/final-assignment.html).

# Total points

## Final assignment

You got **45.75 / 50** points from the final assignment (grade 5/5)! Excellent work! There were some minor things that could be improved but altogether, good programming. 
See more details about the grading criteria from [Final_Assignment_Assessment.md](Final_Assignment_Assessment.md).
  
## Course grade
  
You got **113 / 115 points** (grade 5/5) from the Exercises (Period II)! And 5/5 from the final assignment.  
 
Your **final grade** from the course is: **5 / 5**. Excellent work!


# AccessViz
  
  [You can select a desired grid ID from interactive map here.](https://autogis-2017.github.io/final-assignment-Oyelowo/AccessViz/YKR_grid_values.html)
 
  
AccessViz module can be used to explore the Heslinki travel time matrices to analyse and visualise the Accessibility of various places in the area by different modes of transportation. More information can be found on the [Accessibility group page](http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/). 

_AccessViz can:_

- extract specified file(s). The file has to be specified by the destination grid ID,

- merge the  files with the shapefile of the grid map of Helsinki Metropolitan Area.

- visualise the specified travel mode.

- compare two travel mode for accessibility analysis.

 _Also:_
- shows activity progress.

- tells if a destination grid file is entirely empty(i.e has -1 throughout). NB: This was noticed that there is at least one file like this e.g. 6016696.

- it also shows which and how many of the specified destination grid file is not included in the main zipped travel time/distance matrices file.

- options to either create shapefiles alone or visualise or both.

-  wide range of options to classify the travel time/distance, using predefined pysal classes or self-defined classes.
option to export files into thesame or separate folders



**The module can be used as below:**

**from AccessViz import explore**

Here, the name of the package is AccessViz, the module is AccessViz while the functions can be found in the class "explore".

By importing this way, the functions can be called as below:

**_e.g, explore.extract, explore.merge_shp etc._**

It is also possible to import the module directly as:

**import AccessViz**

When this is done, the functions can be used as in the below example:
**AccessViz.explore.merge_shp**

However, it is recommended to shorten the name when importing. For example:

**from AccessViz import explore as expl**


Different functions in the AccessViz module include: **_extract_prompt, extract, merge_shp, show_travel_mode and compare_travel_modes._** See below for the documentation.

This [source code can be found here](https://github.com/AutoGIS-2017/final-assignment-Oyelowo/blob/master/AccessViz/AccessViz.py).
It is also important to use the module [get_geom](https://github.com/AutoGIS-2017/final-assignment-Oyelowo/blob/master/AccessViz/get_geom.py) which AccessViz depends on in some parts.

NOTE: for the travel time matrices, the file path of the zipped file should be specified while for the MetropoAcess grid, the shapefile can be loaded with the geopandas module.  

**LINKS TO THE VARIOUS DATA USED/NEEDED:**

-  shapefiles for the Sea, metro rail line, roads can train rail line(Railway) can be found in my [repository](https://github.com/AutoGIS-2017/final-assignment-Oyelowo/tree/master/data).

-  Travel time matrices and metropo Access grid shapefile: http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/. Various attributes(including the travel modes) in the travel time matrices are:

### ATTRIBUTES
-    from_id:	ID number of the origin grid cell'

-    to_id:	ID number of the destination grid cell

-    walk_t:	Travel time in minutes from origin to destination by walking

-    walk_d:	Distance in meters of the walking route

-  pt_r_tt:	Travel time in minutes from origin to destination by public transportation in rush hour traffic; whole travel chain has been taken into acount including the waiting time at home.

-  pt_r_t:	Travel time in minutes from origin to destination by public transportation in rush hour traffic; whole travel chain has been taken into account excluding the waiting time at home.

-  pt_r_d:	Distance in meters of the public transportation route in rush hour traffic.

-  pt_m_tt:	Travel time in minutes from origin to destination by public transportation in midday traffic; whole travel chain has been taken into acount including the waiting time at home.

-  pt_m_t:	Travel time in minutes from origin to destination by public transportation in midday traffic; whole travel chain has been taken into account excluding the waiting time at home.

-  pt_m_d:	Distance in meters of the public transportation route in midday traffic.

-  car_r_t: 	Travel time in minutes from origin to destination by private car in rush hour traffic; the whole travel chain has been taken into account (see “Methods” section below).

-  car_r_d:	Distance in meters of the private car route in rush hour traffic.

-  car_m_t:	Travel time in minutes from origin to destination by private car in midday traffic; the whole travel chain has been taken into account (see “Methods” section below).

-  car_m_d:	Distance in meters of the private car route in midday traffic


## FIRST FUNCTION: extract_prompt
-      extract_prompt(zipped_data_path, filepath, sep=";", file_format=".txt",separate_folders=False):
       
 _This function extracts matrices(files) from the zipped Helsinki Region Travel
 Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
 the specified input is not included in the matrices
 specified by use._
 
 _The function has the same function as the function 'extract'. The only difference is that the user is prompted to input the            values which should be separated by comma(,)._

 -  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

 -  **_filepath:_** output filepath where the matrices files will be extracted to.

 -  **_sep(e.g ',' ,';', '\t)' :_** the separator of the columns of the extracted files. This works only if the files are extracted into              thesame folder, i.e separate_folder=False.

 -   **_file_format(e.g. .txt, .csv):_** format of the extracted travel time matrices. This is also works only if the files are extracted into thesame folder, i.e separate_folder=False.

 -  **_separate_folder(True/False):_** this determines if the files should be extracted into same folder or separate folders. Default             value is False.    

       **EXAMPLE OF USAGE:**
       **_explore.extract_prompt(zipped_data_path= "C:/Users/oyedayo/HelsinkiRegion_TravelTimeMatrix2015.zip", separate_folders=False, filepath= "C:/Users/oyedayo/matrices", sep=",", file_format='.txt')_**



## SECOND FUNCTION: extract

-      extract(zipped_data_path, filepath,userinput, sep=";", file_format=".txt", separate_folders=False):

_The function has thesame function as the function 'extract_prompt'. The only difference is that the user is prompted to input           the values which should be separated by comma(,).
This function extracts matrices(files) from the zipped Helsinki Region Travel
Time Matrix, according to the specified userinputs(matrix ID) which is the grid YKR_ID. It also states if
the specified input is not included in the matrices
specified by use._

_The function has thesame function as the function 'extract_files'. The only difference is that the user is not prompted to input the grid values but this should be specified in the parameter 'userinput'._

-  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

-  **_filepath:_** output filepath where the matrices files will be extracted to.

-  **_userinput:_** these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]

-  **_sep(e.g ',' ,';', '\t'):_** the separator of the columns of the extracted files. This works only if the files are extracted into            thesame folder, i.e separate_folder=False.

-  **_file_format(e.g. .txt, .csv):_** format of the extracted travel time matrices. This is also works only if the files are extracted            into thesame folder, i.e separate_folder=False.

-  **_separate_folder(True/False):_** this determines if the files should be extracted into same folder or separate folders. Default             value is False.    

**EXAMPLE OF USAGE:**
**_explore.extract(zipped_data_path= "C:/Users/oyedayo/HelsinkiRegion_TravelTimeMatrix2015.zip", userinput=[6016696, 6015141, 5991603 ],separate_folders=True separate_folders=False, filepath= "C:/Users/oyedayo/matrices", sep=",", file_format='.txt')_**


## THIRD FUNCTION: merge_shp

-      merge_shp(zipped_data_path,userinput, grid_shp, filepath, separate_folder=False):

_This creates Shapefiles from the chosen Matrix text tables
(e.g. travel_times_to_5797076.txt) by joining the Matrix file with MetropAccess_YKR_grid 
Shapefile where from_id in Matrix file corresponds to YKR_ID in the Shapefile. The tool 
saves the result in the output-folder that user has defined. The output files 
are named in a way that it is possible to identify the ID from the name (e.g. 5797076)._

-  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

-  **_userinput:_** these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]

-  **_grid_shp:_** this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time                   matrix(ces).

-  **_filepath:_** output filepath where the matrices files will be extracted to.

-  **_separate_folder:_** this determines if the files should be extracted into same folder or separate folders.
       
      **EXAMPLE OF USAGE:**
      
      **_explore.merge_shp(zipped_data_path="C:/Users/oyedayo/HelsinkiRegion_TravelTimeMatrix2015.zip", separate_folder=False, userinput=[6016696, 6015141, 5991603 ], grid_shp= shape_file_of_the_MetropAccess_YKR_grid, filepath= r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\merged")_**

         
     
## FOURTH FUNCTION: show_travel_mode
         
 -     show_travel_mode(zipped_data_path,userinput, tt_col, filepath, grid_shp, sea=None, roads=None,train=None, 
            metro=None, roads_color='grey', metro_color='red', 
            train_color='blue',map_type='interactive', destination_style='circle', destination_color='blue',       
            classification='pysal_class', class_type="Quantiles", n_classes=8,
            multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, truncate=True, 
            pct_classes=[1,10,50,90,99,100],
            class_lower_limit="", class_upper_limit="", class_step="", 
            label_lower_limit="", label_upper_limit="", label_step=""):
            
            
_This visualises the travel times of selected YKR_IDs based on the travel mode that the 
user specifies. It can save those maps into a folder that is specified. The output maps
can be either static or interactive and user can choose which one with a parameter. 
By using the parameters, you can freely design yourself the style of the map, 
travel time intervals (classes) etc.  You can decided to either visualise joined travel mode or not.
You can also choose what kind of classificaation(either pysal class or User_Defined). The pysal_class
option uses pysal classification which can be found on the [pysal page](http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify).
With the user_defined classification, you can choose yourself how you wish to make the classifixation,
inlcuding the lowest limit, uppermost limit and also the interval/break. This can also be done as you want it on the label/legend.
the uppermost level shows those values that are greater than that level(e.g 60< or >60).
This function also tells if a grid is empty(i.e no data). This grids with nodata have -1 value_

-  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

-  **_userinput:_** these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425]

-  **_tt_col:_** this is the travel mode which will be displayed in the map(e.g pt_r_tt, pt_r_d, walk_d, car_r_t)

-  **_grid_shp:_** this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time matrix(ces).

-  **_filepath:_** output filepath where the maps will be extracted to.

-  **_sea(default value=None):_** this is the shapefile of the sea around the region which will be displayed on the map if specified.

-  **_roads(default value=None):_** this is the shapefile of the roads in the region which will be displayed on the map if specified.

-  **_train(default value=None):_** this is the shapefile of the train rail line in the region which will be displayed on the map if           specified.

-  **_metro(default value=None):_** this is the shapefile of the metro rail line in the region which will be displayed on the map if             specified.

-  **_roads_color, metro_color, train_color:_** these are used to choose the color for the various transportation means.

-  **_map_type:_** options are(interactive or static). 

-  **_destination_style(default= circle):_** options are(grid or cycle). This shows how you wish to highlight the destination grid.

-  **_destination_color:_** color of the highlighted destination.

-  **_classification(default='pysal_class'):_** options are('pysal_class' or 'user_defined').

-  **_class_type(default="Quantiles"):_** Options include, 'Quantiles', 'Box_Plot', 'Equal_Interval, 'Fisher_Jenks',
                              'HeadTail_Breaks','Jenks_Caspall', 'Max_P_Classifier', 'Natural_Breaks', 'Percentiles', and                                             'Std_Mean'.  You can fund more information on the [pysal page](http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify).

-  **_n_classes(default=8):_** number of classes.

-  **_multiples:_** used in Standard Deviation and Mean Map Classification(i.e Std_Mean). 

-  **_pct_classes:_** used in for Percentiles Map Classification. In the pysal documentation, this is parameter is is 'pct'.

-  **_pct:_** Fisher Jenks optimal classifier - mean based using random sample. 

-  **_hinge:_** used in Box_Plot Map Classification.

-  **_truncate:_** used in Fisher Jenks optimal classifier - mean based using random sample. 

-  **_class_lower_limit, class_upper_limit, class_step:_** should be used for making the breaks for manually classifying the travel                mode column.                                                

-  **_label_lower_limit, label_upper_limit, label_step:_** This can be used for making the legend.
label_lower_limit is the lowest limit allowed in the legen, label_step is the label/legend class interval, while
the label_upper_limit level shows those values that are greater than that level(e.g 60< or >60)

  **EXAMPLE OF USAGE:**
  **_explore.show_travel_mode(zipped_data_path="C:/Users/oyedayo/HelsinkiRegion_TravelTimeMatrix2015.zip", train=train_shapefile,                      metro=metroline_shapefile, roads=roads_shapefile,
           roads_color='grey', metro_color='red', train_color='blue',userinput=[6015141, 5991603, 5991515], 
           destination_style='circle', destination_color='blue',map_type='interactive',
           grid_shp=mtp, tt_col="car_r_t", n_classes=5, classification='pysal_class',  
           class_type='Equal_Interval', filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise")_**

## FIFTH FUNCTION: compare_travel_modes

-      compare_travel_modes(zipped_data_path,userinput, filepath, grid_shp, sea=None, roads=None,
        train=None, metro=None,compare_mod=[], create_shapefiles=True, visualisation=True, 
        map_type='interactive', destination_style='circle', destination_color='blue',
        roads_color='grey', metro_color='red', train_color='yellow',classification='pysal_class', 
        class_type="Quantiles", n_classes=8, multiples=[-2, -1, 1, 2],  pct=0.1, hinge=1.5, 
        truncate=True, pct_classes=[1,10,50,90,99,100], class_lower_limit="", 
        class_upper_limit="", class_step="", label_lower_limit="", label_upper_limit="", 
        label_step="")
        
_The function compares travel times or travel distances between two different travel modes 
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
the function suggests the acceptable values._

_The output maps are saved into a folder that is specified. The output maps
can be either static or interactive and user can choose which one with a parameter. 
By using the parameters, you can freely design yourself the style of the map, 
travel time intervals (classes) etc.  You can decided to either visualise joined travel mode or not.
You can also choose what kind of classificaation(either pysal class or User_Defined). The pysal_class
option uses pysal classification which can be found on the [pysal page](http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify).
With the user_defined classification, you can choose yourself how you wish to make the classifixation,
inlcuding the lowest limit, uppermost limit and also the interval/break. This can also be done as you want it on the label/legend.
the uppermost level shows those values that are greater than that level(e.g 60< or >60).
This function also tells if a grid is empty(i.e no data). This grids with nodata have -1 value_



-  **_zipped_data_path:_** This is the path to the zipped Helsinki travel time matrices data which should be specified.

userinput: these are the grid IDs which should be input as a list. e.g, userinput=[542563,625425].

-  **_compare_mod:_** a list of the travel modes to be compared e.g(['pt_r_tt', 'car_r_t']). 

-  **_create_shapefiles(default=True):_** this is used to specify if the shapefiles of the joined metropo_Acees grid
and the travel time matrices should be created. if True, the compared mode(i.e travelmode1 - travelmode2) will be included in the calculation.

-  **visualisation(default=True):_** used to specify if you want to visualise the compared travel mode.

-  **_grid_shp:_** this is the grid shapefile of the area which includes the grids IDs and will be joined with the travel time matrix(ces).

-  **_filepath:_** output filepath where the maps will be extracted to.

-  **_sea(default value=None):_** this is the shapefile of the sea around the region which will be displayed on the map if specified.

-  **_roads(default value=None):_** this is the shapefile of the roads in the region which will be displayed on the map if specified.

-  **_train(default value=None):_** this is the shapefile of the train rail line in the region which will be displayed on the map if           specified.

-  **_metro(default value=None):_** this is the shapefile of the metro rail line in the region which will be displayed on the map if             specified.

-  **_roads_color, metro_color, train_color:_** these are used to choose the color for the various transportation means.

-  **_map_type:_** options are(interactive or static). 

-  **_destination_style(default= circle):_** options are(grid or cycle). This shows how you wish to highlight the destination grid.

-  **_destination_color:_** color of the highlighted destination.

-  **_classification(default='pysal_class'):_** options are('pysal_class' or 'user_defined').

-  **_class_type(default="Quantiles"):_** Options include, 'Quantiles', 'Box_Plot', 'Equal_Interval, 'Fisher_Jenks',
                              'HeadTail_Breaks','Jenks_Caspall', 'Max_P_Classifier', 'Natural_Breaks', 'Percentiles', and                                             'Std_Mean'.
For more information: You can check the [pysal page](http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html#pysal.esda.mapclassify).

-  **_n_classes(default=8):_** number of classes.

-  **_multiples:_** used in Standard Deviation and Mean Map Classification(i.e Std_Mean). 

-  **_pct_classes:_** used in for Percentiles Map Classification. In the pysal documentation, this is parameter is is 'pct'.

-  **_pct:_** Fisher Jenks optimal classifier - mean based using random sample. 

-  **_hinge:_** used in Box_Plot Map Classification.

-  **_truncate:_** used in Fisher Jenks optimal classifier - mean based using random sample. 

-  **_class_lower_limit, class_upper_limit, class_step:_** should be used for making the breaks for manually classifying the travel                mode column.                                                

-  **_label_lower_limit, label_upper_limit, label_step:_** This can be used for making the legend.
label_lower_limit is the lowest limit allowed in the legen, label_step is the label/legend class interval, while
the label_upper_limit level shows those values that are greater than that level(e.g 60< or >60).


  **EXAMPLE OF USAGE:**
  
   **_explore.compare_travel_modes(zipped_data_path="C:/Users/oyedayo/HelsinkiRegion_TravelTimeMatrix2015.zip", train=train_shapefile,                      metro=metroline_shapefile, roads=roads_shapefile, compare_mod=["pt_r_tt", "car_r_t"], create_shapefiles=True,                          visualisation=True, roads_color='grey', metro_color='red', train_color='blue', userinput=[6015141, 5991603, 5991515], 
           destination_style='circle', destination_color='blue',map_type='interactive',
           grid_shp=mtp, tt_col="car_r_t",n_classes=5, classification='pysal_class',  
           class_type='Equal_Interval' , filepath=r"C:\Users\oyeda\Desktop\AUTOGIS\FINAL_ASSIGNMENT\visualise")_**

