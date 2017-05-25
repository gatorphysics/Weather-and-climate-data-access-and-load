from ecmwfapi import ECMWFDataServer
    
server = ECMWFDataServer()
    
server.retrieve({
    'stream'    : "oper",
    'levtype'   : "sfc",
    'param'     : "172.128/165.128/166.128/167.128/134.128/164.128/78.128/79.128/235.128",
    'dataset'   : "interim",
    'step'      : "0",
    'grid'      : "0.75/0.75",
    'time'      : "00/06/12/18",
    'date'      : "2015-03-29/to/2015-03-29",
    'type'      : "an",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "interim_2015-03-29to2015-03-29_surf.nc"
    })

#172.128  land-sea mask
#165.128  10-m U wind
#166.128  10-m V wind
#167.128  2-m temperature
#134.128  Surface pressure
#164.128  Total cloud cover
#78.128   Total colum liquid water
#79.128   Total colum ice water
#235.128  skin temp

