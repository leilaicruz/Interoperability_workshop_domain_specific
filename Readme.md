# How to use this workshop

- set up a Virtual python environment using conda (more recommended than pip for this case)

`conda env create -f Lesson_development/environment.yml `

`conda activate netcdf_python`

🚨 Important
-  conda-forge versions are built against correct libraries for OPeNDAP.
- Always use conda-forge channel to get properly compiled scientific libraries for remote NetCDF access.
- If you only use pip, you risk missing underlying C libraries like libnetcdf and libhdf5.

## After activation

`python --version`
# Should say 3.12.x

`conda list netcdf4`
# Should list netcdf4 installed

`ncdump -h https://opendap.4tu.nl/thredds/dodsC/IDRA/2019/01/01/IDRA_2019-01-01_00-00_raw_data.nc`
# Should succeed

# Set up a Binder notebook for participants. 