from ccf_s1d import compute_ccf
import glob
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

# Define the wavelength bands for the demo
bands = {'demo': [1600, 1650]}

# Get the list of files matching the pattern 'data/*s1d*AB.fits'
# we only check odometers starting with 257 to have a reasonable number of files
files = np.array(glob.glob('data/257*s1d*AB.fits'))
# Define the path to the mask file
mask_file = 'mask/V347AUR_neg.fits'

# Initialize an array to store the MJDMID values for each file
MJDMIDs = np.zeros_like(files, dtype=float)

# Loop through each file to extract the MJDMID from the FITS header
for i, file in enumerate(files):
    hdr = fits.getheader(file)
    MJDMIDs[i] = hdr['MJDMID']

# Sort the files by MJDMID
sort_order = np.argsort(MJDMIDs)
MJDMIDs = MJDMIDs[sort_order]
files = files[sort_order]


# Construct a color palette for the CCFs in order of MJDMID
colors = plt.cm.viridis(np.linspace(0, 1, len(files)))

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Loop through each file to compute and plot the CCF
for i, file in enumerate(files):
    # Compute the CCF for the current file
    tbl = compute_ccf(file, mask_file, bands=bands, outdir='./ccf_demo')

    # Extract the velocity shifts (dvs) and the CCF values for the 'demo' band
    dv = tbl['dvs']
    ccf = tbl['demo']
    # Normalize each CCF with its median
    ccf /= np.nanmedian(ccf)
    # Plot the CCF with the corresponding color from the palette
    ax.plot(dv, ccf, color=colors[i], alpha = 0.6)

# Add a color bar with the MJDMID values
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=MJDMIDs.min(), vmax=MJDMIDs.max()))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('MJDMID')

# Add a grid
plt.grid(color='gray', linestyle='--', linewidth=0.5)
# Set the x-axis label
plt.xlabel('Velocity (km/s)')
# Set the y-axis label
plt.ylabel('Normalized CCF')
# Set the plot title
plt.title('CCF for Different Files')
# Display the plot
plt.show()