import xarray as xr
import numpy as np
import pandas as pd

# Step 1: Define initial data (your original dataset)
times = pd.date_range("2023-01-01", periods=10, freq='H')
v_wind = np.random.rand(10) * 10  # Example data

ds = xr.Dataset(
    data_vars={
        "v_wind": ("time", v_wind, {
            "units": "m s-1"
        }),
    },
    coords={
        "time": times,
    },
    attrs={
        "title": "DENlab wind data, raw, 2008"
    }
)

# Step 2: Add latitude, longitude, height coordinates explicitly
ds = ds.assign_coords(
    latitude=52.0,
    longitude=4.3,
    height=10.0
)

# Step 3: Add CF-compliant attributes explicitly
# Latitude attributes
ds["latitude"].attrs.update({
    "units": "degrees_north",
    "standard_name": "latitude"
})

# Longitude attributes
ds["longitude"].attrs.update({
    "units": "degrees_east",
    "standard_name": "longitude"
})

# Height attributes
ds["height"].attrs.update({
    "units": "m",
    "standard_name": "height",
    "positive": "up"
})

# Time attributes
ds["time"].attrs.update({
    "standard_name": "time",
    "axis": "T",
    "long_name": "Time of measurement"
})

# Data variable attributes
ds["v_wind"].attrs.update({
    "standard_name": "northward_wind",
    "long_name": "Northward component of wind velocity"
})

# Global attributes for CF-compliance
ds.attrs.update({
    "Conventions": "CF-1.10",
    "institution": "Delft University of Technology",
    "source": "DENlab Wind Sensor",
    "history": f"Converted to CF conventions on {pd.Timestamp.now()}"
})

# Step 4: Save to a CF-compliant NetCDF file
ds.to_netcdf("denlab_wind_cf.nc")

print("CF-compliant NetCDF file created: 'denlab_wind_cf.nc'")
