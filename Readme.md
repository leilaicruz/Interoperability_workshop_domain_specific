# How to use this workshop

- set up a Virtual python environment using conda (more recommended than pip for this case)

`conda env create -f environment.yml `

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

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leilaicruz/Interoperability_workshop_domain_specific/HEAD?urlpath=%2Fdoc%2Ftree%2Fparticipants_live_code.ipynb)

Go to Binder notebook [here](https://mybinder.org/v2/gh/leilaicruz/Interoperability_workshop_domain_specific/ef45d7c58253be63a43dd08a7f18135c83a30965?urlpath=lab%2Ftree%2Fparticipants_live_code.ipynb)
