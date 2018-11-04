import astropy
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# filename should be like: '20160601_12579.fits'
# Load data from fits file and return number of cuts in the scan, 2D Emap and Tmap
def loadAndProcessData(filename, Eindex=7, Tindex=8):
	hdulist = fits.open(filename)
	hdu1 = hdulist[1]
	imgData = hdu1.data
	numAngCuts = hdu1.header['NAXIS2']
	imgE = np.array([imgData[i][Eindex] for i in range(numAngCuts)])
	imgT = np.array([imgData[i][Tindex] for i in range(numAngCuts)])

	return numAngCuts, imgE, imgT


# Plot full scale raw Emap and Tmap
def rawETMap(emap, tmap, scale=False):
	plt.figure(figsize=[14, 4])
	plt.subplot(1,2,1)
	plt.imshow(emap, aspect='auto')
	plt.title('Energy Dispersion Map')
	plt.ylabel('rotation angle')
	plt.subplot(1,2,2)
	plt.imshow(tmap, aspect='auto')
	plt.title('Time Dispersion Map')
	plt.show()


# xlim and ylim should be a tuple specifies the x/ymin and x/ymax
def stackEDCsPlot(emap, delY=100, numCuts=20, xlim=(-10, 750), ylim=(-10, 2200)):
	colors = cm.winter(np.linspace(0, 1, numCuts))
	delY = delY

	plt.figure()
	for i in range(numCuts):
		plt.plot(emap[i] + (delY * i), color=colors[i])
	plt.ylim(ylim)
	plt.xlim(xlim)
	plt.xlabel("Energy (pixel)")
	plt.ylabel("Angle (pixel)")
	plt.show()


def scaleEDC(edc):
    return edc/max(edc)


def scaleAndShiftEDC(edc):
    return (edc/max(edc))-0.5


def loadAllData():
	mapFolder = []
	
	fileIndex = ['0531_12572', '0531_12573', '0531_12574', '0601_12575', '0601_12576', '0601_12577', '0601_12578', '0601_12579']
	for ind in fileIndex:
		numcuts, imgE, imgT=loadAndProcessData('Bi2Se3/2016'+ind+'.fits')
		mapFolder.append([numcuts, imgE, imgT])


	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170201/20170202_13356.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170201/20170202_13357.fits')
	mapFolder.append([numcuts, imgE, imgT])

	fileIndex = ['13388', '13389', '13390']
	for ind in fileIndex:
		numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170525_'+ind+'.fits')
		mapFolder.append([numcuts, imgE, imgT])

	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170531_13423.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170531_13425.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170602_13459.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170609_13476.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170525/20170609_13477.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170809/20170809_13490.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170809/20170809_13491.fits')
	mapFolder.append([numcuts, imgE, imgT])
	numcuts, imgE, imgT = loadAndProcessData('Bi2Se3/20170809/20170828_13493.fits')
	mapFolder.append([numcuts, imgE, imgT])

	print("Number of raw map =", len(mapFolder))

	# Select EDCs:
	thred = [250, 250, 250, 350, 250, 250, 250, 380, 700, 700, 400, 400, 350, 400, 400, 900, 400, 400, 500, 500, 500]
	counts = []
	edcStack = []

	for index in range(len(mapFolder)):
		count = 0
		for i in range(len(mapFolder[index][1])):
			if (max(mapFolder[index][1][i]) > thred[index]):
				count += 1
				edcStack.append(mapFolder[index][1][i])
		counts.append(count)
	edcStack = np.array(edcStack)
	print("total data point =", sum(counts))

	trimEDCs = np.array([edcStack[i][:1693] for i in range(len(edcStack))])
	print("trimEDCs.shape =",trimEDCs.shape)

	return mapFolder, edcStack, trimEDCs

