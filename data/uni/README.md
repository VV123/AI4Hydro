# TAMU-CC University Site

## Data Description as A Graph

<img width="500" alt="university site" src="https://github.com/VV123/AI4Hydro/blob/main/imgs/WW01.png">

`Node`: index (e.g., v_i=1), hydrological and climatic data are represented as node features. 

`Edge`: connectivity of nodes (e.g., <v_i, v_j>), material, slope, and other static edge features. 


## Files and Field Descriptions

- Node file
  - `id`
  - `coordinate`
  - `Invert` is the inner bottom of the pipe (or manhole)
  - `Flow depth` is measured from the elevation of the invert.

- Edge file
  - `Invert Elev. (ft)`The elevation of the bottom of the manhole, measured from a defined datum (unit: ft).
  -  `Rim Elev. (ft)`  The elevation of the top of the manhole (typically at or slightly above the ground surface, measured from a defined datum (unit: ft).   
  -  `Depth (ft)` The depth of the bottom of the manhole, measured from the ground surface (unit: ft). 
  -  `Avg. Depth (ft)`  The average water depth in the manhole during the simulation (unit: ft). 

     Max. Depth (ft)& Float & 0.03 - 0.26 & The maximum water depth in the manhole during the simulation (unit: ft).\\

     Max. HGL (ft)& Integer/Float & -5.28 - 1.91 & The maximum elevation of the hydraulic grade line (HGL) in the manhole during the simulation (unit: ft). HGL is the sum of the position head and the pressure head and describes the total energy of the fluid. \\ 

     Rep. Max. Depth (ft)& Float & 0.03 - 0.26 & Representative values of the maximum water depth during the simulation (unit: ft).\\

     Max. Lat. Inflow (cfs)& Integer/Float & 0 - 0.01  & The maximum rate of lateral inflows (runoff, groundwater flow, dry weather flow, etc.) during the simulation (unit: ft3/s). \\

     Max. Total Inflow (cfs)& Integer/Float & 0 - 0.13 & The maximum rate of all inflows during the simulation (unit: ft3/s). \\

     Total Lat. Inflow (MG)& Float & 0.001 - 0.007 & The volume of lateral inflows (runoff, groundwater flow, dry weather flow, etc.) during the simulation (unit: million gallon). \\ 

     Total inflow (MG)& Float & 0.001 - 0.106 & The volume of all inflows during the simulation (unit: million gallon)\\

     Min. Freeboard (ft)& Integer/Float & 6.58 - 20.28 & The minimum freeboard depth (unit: ft), i.e., the different between the rim elevation and the maximum HGL.\\ 
