import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import sys
g_name = get_pkg_data_filename(r'/home/harshini/project_HST_images/F125.fits')
r_name = get_pkg_data_filename(r'/home/harshini/project_HST_images/F160.fits')
i_name = get_pkg_data_filename(r'/home/harshini/project_HST_images/F814.fits')
g = fits.open(g_name)[0].data
r = fits.open(r_name)[0].data
i = fits.open(i_name)[0].data
ID=sys.argv[1]
outfile=ID+".png"
rgb_default = make_lupton_rgb(i, r, g, Q=10,stretch=0.2,filename=outfile)
#rgb_default = make_lupton_rgb(i, g, Q=10,stretch=0.5,filename="default.jpeg")
#plt.imshow(rgb_default, origin='lower')
