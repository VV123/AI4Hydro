# TAMU-CC University Site

## Data Description as A Graph

<img width="500" alt="university site" src="https://github.com/VV123/AI4Hydro/blob/main/imgs/WW01.png">

`Node`: index (e.g., v_i=1), hydrological and climatic data are represented as node features. 

`Edge`: connectivity of nodes (e.g., <v_i, v_j>), material, slope, and other static edge features. 


## Files and Field Descriptions

- Node features - WW01_node.csv
  - `Length (ft)` The length of the sewer pipe between two manholes (unit: ft).
  - `Roughness` The roughness of the pipe materials (unitless). Larger roughness results in more friction loss. 
  - `Geom1(ft)` The diameter of the pipe (unit: ft). All pipes have circular sections.
  - `Slope (ft/ft)` The slope of the pipe (unitless), i.e., the elevation difference between the two ends of the pipe divided by the length of the pipe. 
  - `Max. |Flow| (cfs)` The maximum rate of the pipe flow during the simulation (unit: ft3/s).  
  - `Max. |Velocity| (ft/s)` The maximum (point) velocity of the pipe flow during the simulation (unit: ft/s). 
  - `Max/Full Flow` The ratio of the maximum simulated flow rate to the full flow capacity (in terms of flow rate) of the pipe (unitless). 
  - `Max/Full Depth` The ratio of the maximum simulated flow depth to the full flow capacity (in terms of flow depth) of the pipe (unitless).
  - `GISLENGTH (m)` The length of the sewer pipe between two manholes (unit: m).hl{(You may ingore this one.)

- Edge features - WW01_edge.csv
  - `Invert Elev. (ft)`The elevation of the bottom of the manhole, measured from a defined datum (unit: ft).
  - `Rim Elev. (ft)`  The elevation of the top of the manhole (typically at or slightly above the ground surface, measured from a defined datum (unit: ft).   
  - `Depth (ft)` The depth of the bottom of the manhole, measured from the ground surface (unit: ft). 
  - `Avg. Depth (ft)`  The average water depth in the manhole during the simulation (unit: ft). 
  - `Max. Depth (ft)`  The maximum water depth in the manhole during the simulation (unit: ft).
  - `Max. HGL (ft)` The maximum elevation of the hydraulic grade line (HGL) in the manhole during the simulation (unit: ft). HGL is the sum of the position head and the pressure head and describes the total energy of the fluid.
  - `Rep. Max. Depth (ft)` Representative values of the maximum water depth during the simulation (unit: ft).
  - `Max. Lat. Inflow (cfs)` The maximum rate of lateral inflows (runoff, groundwater flow, dry weather flow, etc.) during the simulation (unit: ft3/s). 
  - `Max. Total Inflow (cfs)` The maximum rate of all inflows during the simulation (unit: ft3/s). 
  - `Total Lat. Inflow (MG)` The volume of lateral inflows (runoff, groundwater flow, dry weather flow, etc.) during the simulation (unit: million gallon). 
  - `Total inflow (MG)` The volume of all inflows during the simulation (unit: million gallon).
  - `Min. Freeboard (ft)` The minimum freeboard depth (unit: ft), i.e., the different between the rim elevation and the maximum HGL.

- WW01_v3.csv
  
    Time series water depth for each node.

- Flow_rate.csv

    Processed file from Inflow Time Series_v3 folder. It includes the inflow rate for each node. 

