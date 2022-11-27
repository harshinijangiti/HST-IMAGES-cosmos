#!/usr/bin/python3
#this program creates a cutout of size 20 arcsec X 20 arcsec around RA,DEC=53.09964, -27.79427 from the F125 image of goods -south data
# this script works with gzipped fits file also
import sys
from astropy.nddata import Cutout2D
from astropy import units as u
zoomSize = u.Quantity((3,3), u.arcsec)
from astropy import wcs
from astropy.io import fits
#fname='goodss_3dhst.v4.0.F125W_orig_sci.fits.gz'
fname=sys.argv[1]
hdulist = fits.open(fname)
w = wcs.WCS(hdulist[0].header)
data=fits.getdata(fname,ext=0)
from astropy.coordinates import SkyCoord
RA=sys.argv[2]
DEC=sys.argv[3]
#position = SkyCoord(53.09964, -27.79427, unit="deg")
position = SkyCoord(RA, DEC, unit="deg")
cutout = Cutout2D(data, position, zoomSize, wcs=w)
xdu = fits.PrimaryHDU(cutout.data)
xdu.header = hdulist[0].header
xdu.header.update(cutout.wcs.to_header())
outfile=fname[0:4] + ".fits"
xdu.writeto(outfile,overwrite=True)

