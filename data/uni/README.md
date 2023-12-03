# TAMU-CC University Site

## Data Description

<img width="500" alt="university site" src="https://github.com/VV123/AI4Hydro/blob/main/imgs/WW01.png">

*Node*: index (e.g., v_i=1), coordinate, hydrological and climatic data are represented as node features. Manning's n describes the surface roughness of the pipe wall. A greater value of n indicates greater loss of head (energy) due to friction. 

*Edge*: coordinate, connectivity of nodes (e.g., <v_i, v_j>), material, slope, and other static pipe features. Invert is the inner bottom of the pipe (or manhole). Flow depth is measured from the elevation of invert.


## Files and Field Descriptions

- conduit.csv - node file
  - `id`
  - `start`
  - `end`

- junction.csv - edge file
  - `id`
