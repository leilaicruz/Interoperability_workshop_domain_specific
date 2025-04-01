

import xarray as xr 

netcdf_file="https://opendap.4tu.nl/thredds/dodsC/IDRA/2019/01/01/IDRA_2019-01-01_00-00_raw_data.nc" # this is an example of a netcdf dataset that is well documented, in the sense that it contains metadata for the convention used.
netcdf_file_2="https://opendap.4tu.nl/thredds/dodsC/data2/uuid/9604a1b0-13b6-4f23-bd6c-bb028591307c/wind-2008.nc" ## this an example of a netcdf dataset that is bad documented, in the sense that it doesnt contain metadata for the convention used


### A classic NetCDF file like this one can be broken down into 3 components - dimensions, variables and global attributes. The variables can be broken down into coordinate variables and data variables. Sometimes 
# ## they are displayed separately like here, but if you open a NetCDF file using different software the coordinate variables and data variables might be displayed together.

xrds = xr.open_dataset(netcdf_file_2)

## Look at the global attributes

print(xrds.attrs)

#### Conventions is probably the most important global attribute because it tells you (and a machine) 
# how to interpret the rest of the file. CF-1.8 refers to version 1.8 of the CF conventions, which you can find here:

#### https://cfconventions.org/ https://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html

## Look at the dimensions 

print(xrds.dims)

### individual dimensions

print(xrds.dims['time'])

## Look at coordinated and data variables

print(xrds.coords)

print(xrds.data_vars)

## Look at the coordinate variables

print(xrds.coords['time']) 

## Look at the coordinate variables values 

print(xrds.coords['time'].values)

## Look at the coordinate variables attributes

print(xrds.coords['time'].attrs) 