
**System layout**

<img width="566" alt="Screen Shot 2023-10-21 at 4 59 27 PM" src="https://github.com/VV123/AI4Hydro/assets/9030237/8660b1a6-800d-4c8e-af31-f1f47905deb0">

**Data Files**
- manholes.csv - describes nodes
- pipes.cvs - describes edges

*Node*: index (e.g., v_i=1), coordinate, hydrological and climatic data are represented as node features. Manning's n describes the surface roughness of the pipe wall. A greater value of n indicates greater loss of head (energy) due to friction. 

*Edge*: coordinate, connectivity of nodes (e.g., <v_i, v_j>), material, slope, and other static pipe features. Invert is the inner bottom of the pipe (or manhole). Flow depth is measured from the elevation of invert.




