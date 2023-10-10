Partial water system 
- pipes.cvs
- manholes.csv


Node: index (e.g., v_i=1), coordinate, hydrological and climatic data are represented as node features. Water flow for a time period maybe every hour. The groundwater level predictions use daily or weekly average data, here I think hourly makes more sense and will defer to you.
Edge: coordinate, connectivity of nodes (e.g., <v_i, v_j>), material, slope, and other static pipe features.

Invert is the inner bottom of the pipe (or manhole). Flow depth is measured from the elevation of invert.

Manning's n describes the surface roughness of the pipe wall. A greater value of n indicates greater loss of head (energy) due to friction. 
