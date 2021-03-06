from kapteyn import maputils
import numpy
from service import *

# Fig 2 in celestial article (Calabretta et al) shows a  positive cdelt1
fignum = 2                   # id of script and plot
fig = plt.figure(figsize=figsize)
frame = fig.add_axes(plotbox)
title = r"""Plate Carree projection (CAR), non oblique with:
$(\alpha_0,\delta_0,\phi_p) = (120^\circ,0^\circ,0^\circ)$. (Cal. fig.2)"""
header = {'NAXIS'  : 2, 'NAXIS1': 100, 'NAXIS2': 80,
          'CTYPE1' : 'RA---CAR',
          'CRVAL1' : 120.0, 'CRPIX1' : 50, 'CUNIT1' : 'deg', 'CDELT1' : 5.0,
          'CTYPE2' : 'DEC--CAR',
          'CRVAL2' : 0.0, 'CRPIX2' : 40, 'CUNIT2' : 'deg', 'CDELT2' : 5.0,
          'LONPOLE': 0.0
         }
X = numpy.arange(0,380.0,30.0);
Y = numpy.arange(-90,100,30.0)  # i.e. include +90 also
f = maputils.FITSimage(externalheader=header)
annim = f.Annotatedimage(frame)
grat = annim.Graticule(header, axnum=(1,2), 
                       wylim=(-90,90.0), wxlim=(0,360),
                       startx=X, starty=Y)
header['CRVAL1'] = 0.0
border = annim.Graticule(header, axnum=(1,2), 
                         wylim=(-90,90.0), wxlim=(-180,180),
                         startx=(180-epsilon,-180+epsilon, 0), 
                         starty=(-90,0,90))
lat_world = list(range(-60, 61, 30))
lon_world = list(range(-30,301,30))
labkwargs0 = {'color':'r', 'va':'top', 'ha':'right'}
labkwargs1 = {'color':'b', 'va':'bottom', 'ha':'right'}
doplot(frame, fignum, annim, grat, title, 
       lat_world=lat_world, lon_world=lon_world,
       labkwargs0=labkwargs0, labkwargs1=labkwargs1,
       markerpos=markerpos)
