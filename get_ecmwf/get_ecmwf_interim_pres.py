#!/usr/bin/env /Users/wnwu/anaconda/bin/python
from ecmwfapi import ECMWFDataServer
    
server = ECMWFDataServer()
    
server.retrieve({
    'stream'    : "oper",
    'levelist'  : "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
    'levtype'   : "pl",
    'param'     : "130.128/133.128/157.128/203.128/246.128/247.128/248.128",
    'dataset'   : "interim",
    'step'      : "0",
    'grid'      : "0.75/0.75",
    'time'      : "00/06/12/18",
    'date'      : "2015-03-29/to/2015-03-29",
    'type'      : "an",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "interim_2015-03-29to2015-03-29_Pres.nc"
    })


#130.128 temp
#133.128 h2o
#157.128 relative humidity
#203.128 ozone mixing ratio
#246.128 Specific cloud liquid water 
#247.128 Specific cloud ice water 
#248.128 cloud cover
