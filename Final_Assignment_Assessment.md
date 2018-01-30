# Final Assignment - Evaluation criteria 2017

## Scoring system

Following things should be evaluated from the final work of each student. These are general guidelines for evaluating the work.

- Total points from the final assignment = **50 points** (+5 additional points, see the last point below)

- From each functionality (Steps 1-4, up to 40 points all together) the student can get 10 points where one should evaluate:

  - Are the desired functionalities working as they should --> Up to **7 points** at max.
  - Is the code well documented? Is the code easy to read and follow? Are the variable names reasonable? --> Up to **2 points** at max.
  - Is the code written in a modular way? Using functions etc. --> Up to **1 points** at max.

- Is the work well documented? (Up to 10 points):

  - Is there a **general description** in the beginning of the code(s) about what the code does and **for what it is used for** and **a name of the programmer?** --> Up to **1 point**
  - Are the functions / functionalities described in the code? --> Up to **3 points**
  - Is there a reasonable description about for what purpose the tool is used in the main documentation of the tool, i.e. repo's README.md document (a generic description)? --> Up to **3 points**
    - For what the tool can be used for? What kind of things it can solve / answer for?
    - Are there links to (possible) data that is used with the tool?

  - Is there an explanation and examples how the tool should be used? --> Up to **3 points**
    - As guideline, think that a person without prior knowledge about the tool would come and would like to use it..Could he manage with the documentation given?

- Additional points for other merits in the work that serve some points --> Up to **5 points** at maximum.
  - Can be given if e.g.
     - something in the work is exceptionally well done
     - some problem in the code is solved in a "smart" way
     - the work is exceptionally well documented
     - the visualizations are exceptionally good
     - additional features are added (steps 5-6, or some other features that were not required)

## Grading

Grades:

 - 5 --> 90 % or more of the points received (i.e. > 45 points)
 - 4 --> 80 % or more of the points received (i.e. > 40 points)
 - 3 --> 70 % or more of the points received (i.e. > 35 points)
 - 2 --> 60 % or more of the points received (i.e. > 30 points)
 - 1 --> 50 % or more of the points received (i.e. > 25 points)

## What the tool should do?

**AccessViz** is a set of tools that can be used for managing and helping to analyze
Helsinki Region Travel Time Matrix data (2013 / 2015) that can be downloaded from
`here <http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix/>`_.
Read also the description of the dataset from the web-pages so that you get familiar with the data.

AccessViz tool package has following main functionalities (i.e. functions) that should work independently:

1. AccessViz finds from the data folder all the matrices that user has specified by assigning a list of integer values that should correspond to YKR-IDs found from the attribute table of a Shapefile called `MetropAccess_YKR_grid.shp <http://www.helsinki.fi/science/accessibility/data/MetropAccess-matka-aikamatriisi/MetropAccess_YKR_grid.zip>`_.
If the ID-number that the user has specified does not exist in the data folders, the tools should warn about this to the user but still continue running.
The tool should also inform the user about the execution process: tell the user what file is currently under process and how many files there are left
(e.g. "Processing file travel_times_to_5797076.txt.. Progress: 3/25").

 - 7.5 points

2. AccessViz can create Shapefiles from the chosen Matrix text tables (e.g. *travel_times_to_5797076.txt*) by joining the Matrix file with
MetropAccess_YKR_grid Shapefile  where ``from_id`` in Matrix file corresponds to ``YKR_ID`` in the Shapefile. The tool saves the result in the output-folder
that user has defined. You should name the files in a way that it is possible to identify the ID from the name (e.g. 5797076).

  - 5 points

3. AccessViz can visualize the travel times of selected YKR_IDs based on the travel mode that the user specifies. It can save those maps into a folder that user specifies. The output
maps can be either **static** or **interactive** and user can choose which one with a parameter. You can freely design yourself the style of the map, colors, travel time intervals (classes)
etc. Try to make the map as informative as possible!

  - 10 points

4. AccessViz can also compare **travel times** or **travel distances** between two different travel modes (more than two travel modes are not allowed).
Thus IF the user has specified two travel modes (passed in as a list) for the AccessViz, the tool will calculate the time/distance difference of those travel modes
into a new data column that should be created in the Shapefile. The logic of the calculation is following the order of the items passed on the list where first
travel mode is always subtracted by the last one: ``travelmode1 - travelmode2``.
The tool should ensure that distances are not compared to travel times and vice versa. If the user chooses to compare travel modes to each other,
you should add the travel modes to the filename such as ``Accessibility_5797076_pt_vs_car.shp``. If the user has not specified any travel modes,
the tool should only create the Shapefile but not execute any calculations. It should be only possible to compare two travel modes between each other at the time.
Accepted travel modes are the same ones that are found in the actual TravelTimeMatrix file (pt_r_tt, car_t, etc.).
If the user specifies something else, stop the program, and give advice what are the acceptable values.

  - 10 points
  
Additionally, you should choose and implement one of the following functionalities:

  - 7.5 points

5. (option 1). Bundled with AccessViz there is also a separate interactive map that shows the YKR grid values in Helsinki region. The purpose of the map is to help the user to choose the YKR-IDs that s/he is interested to visualize / analyze.

6. (option 2). AccessViz can also visualize the travel mode comparisons that were described in step 4. You can design the style of the map yourself, but try to make it as informative as possible!

7. (option 3). AccessViz can also visualize shortest path routes (walking, cycling, and/or driving) using OpenStreetMap data from Helsinki Region. The impedance value for the routes can be distance (as was shown in Lesson 7) or time (optional for the most advanced students). This functionality can also be a separate program (it is not required to bundle include this with the rest of the AccessViz tool)


- Additional points can be given if more than one additional functionality was implemented (up to 5 points in total for the whole work)

## Documentation (10 points)
  
- Is there a **general description** in the beginning of the code(s) about what the code does and **for what it is used for** and **a name of the programmer?**
  - Up to **1 point**

- Are the functions / functionalities described in the code? --> Up to **3 points**

- Is there a reasonable description about for what purpose the tool is used in the main documentation of the tool, i.e. repo's README.md document (a generic description)? --> Up to **3 points**
    - For what the tool can be used for? What kind of things it can solve / answer for?
    - Are there links to (possible) data that is used with the tool

- Is there an explanation and examples how the tool should be used? --> Up to **3 points**
    - As guideline, think that a person without prior knowledge about the tool would come and would like to use it..Could he manage with the documentation given?