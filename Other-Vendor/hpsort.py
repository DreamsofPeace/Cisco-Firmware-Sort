import os, shutil, sys, re, getopt, argparse, hashlib

def filemove (newpath, filename):
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	try:
		shutil.move(filename, newpath)
	except:
		print("There is a file with the same name at the destination!.")

def product (prodcode):
	if prodcode == "6400-6300":
		prodname = "SWITCHES/HPE-ARUBA-6400-6300"
	elif prodcode == "6200":
		prodname = "SWITCHES/HPE-ARUBA-6200"
	elif prodcode == "6100":
		prodname = "SWITCHES/HPE-ARUBA-6100-6000"
	elif prodcode == "6100-6000":
		prodname = "SWITCHES/HPE-ARUBA-6100-6000"
	elif prodcode == "8320":
		prodname = "SWITCHES/HPE-ARUBA-8320"
	elif prodcode == "8360":
		prodname = "SWITCHES/HPE-ARUBA-8360"
	elif prodcode == "4100i":
		prodname = "SWITCHES/HPE-ARUBA-4100i"
	elif prodcode == "8325":
		prodname = "SWITCHES/HPE-ARUBA-8325"
	elif prodcode == "8400X":
		prodname = "SWITCHES/HPE-ARUBA-8400X"
	elif prodcode == "9300-32D":
		prodname = "SWITCHES/HPE-ARUBA-9300"
	elif prodcode == "9300":
		prodname = "SWITCHES/HPE-ARUBA-9300"
	elif prodcode == "10000":
		prodname = "SWITCHES/HPE-ARUBA-10000"
	elif prodcode == "A":
		prodname = "SWITCHES/HPE-ARUBA-2915(A)"
	elif prodcode == "C":
		prodname = "SWITCHES/HP-1600M-2400M-4000M-8000M(C)"
	elif prodcode == "H":
		prodname = "SWITCHES/HP-2600(H)"
	elif prodcode == "J":
		prodname = "SWITCHES/HP-5520(J)"
	elif prodcode == "K":
		prodname = "SWITCHES/HPE-ARUBA-5400zl(K)"
	elif prodcode == "KA":
		prodname = "SWITCHES/HPE-ARUBA-3800(KA)"
	elif prodcode == "KB":
		prodname = "SWITCHES/HPE-ARUBA-3810-5400zl2(KB)"
	elif prodcode == "P":
		prodname = "SWITCHES/HP-1810G-8-24(P)"
	elif prodcode == "N":
		prodname = "SWITCHES/HP-2810(N)"
	elif prodcode == "PA":
		prodname = "SWITCHES/HP-1800-8G(PA)"
	elif prodcode == "PB":
		prodname = "SWITCHES/HP-1800-24G(PB)"
	elif prodcode == "PK":
		prodname = "SWITCHES/HP-1800-48G(PK)"
	elif prodcode == "PL":
		prodname = "SWITCHES/HP-1810G-v2(PL)"
	elif prodcode == "PM":
		prodname = "SWITCHES/HP-1810-v2(PM)"
	elif prodcode == "PS":
		prodname = "SWITCHES/HP-1810G(PS)"
	elif prodcode == "Q":
		prodname = "SWITCHES/HP-2510-24(Q)"
	elif prodcode == "M":
		prodname = "SWITCHES/HP-3400cl-6500cl(M)"
	elif prodcode == "E":
		prodname = "SWITCHES/HP-5300xl(E)"
	elif prodcode == "I":
		prodname = "SWITCHES/HP-2824-2828(I)"
	elif prodcode == "CY":
		prodname = "SWITCHES/HP-EDGE-8100fl(CY)"
	elif prodcode == "L":
		prodname = "SWITCHES/HP-4200vl(L)"
	elif prodcode == "R":
		prodname = "SWITCHES/HPE-2610(R)"
	elif prodcode == "RA":
		prodname = "SWITCHES/HPE-ARUBA-2620(RA)"
	elif prodcode == "S":
		prodname = "SWITCHES/HP-2520(S)"
	elif prodcode == "T":
		prodname = "SWITCHES/HP-2900(T)"
	elif prodcode == "U":
		prodname = "SWITCHES/HPE-2510-48(U)"
	elif prodcode == "VA":
		prodname = "SWITCHES/HP-1700-8(VA)"
	elif prodcode == "VB":
		prodname = "SWITCHES/HP-1700-24(VB)"
	elif prodcode == "W":
		prodname = "SWITCHES/HP-2910(W)"
	elif prodcode == "WB":
		prodname = "SWITCHES/HPE-ARUBA-2920(WB)"
	elif prodcode == "WC":
		prodname = "SWITCHES/HPE-ARUBA-2930(WC)"
	elif prodcode == "Y":
		prodname = "SWITCHES/HPE-2510(Y)"
	elif prodcode == "YA":
		prodname = "SWITCHES/HPE-ARUBA-2530(YA)"
	elif prodcode == "YB":
		prodname = "SWITCHES/HPE-ARUBA-2530(YB)"
	elif prodcode == "YC":
		prodname = "SWITCHES/HPE-ARUBA-2540(YC)"
	elif prodcode == "api":
		prodname = "REST-API"
	elif prodcode == "sim":
		prodname = "SIMULATOR"
	elif prodcode == "mibs":
		prodname = "MIBS"
	elif prodcode == "NetEdit":
		prodname = "NetEdit"
	elif prodcode == "MAS":
		prodname = "SWITCHES/ARUBA-x500"
	elif prodcode == "6xx":
		prodname = "CONTROLLER/ARUBA-6x0"
	elif prodcode == "70xx":
		prodname = "CONTROLLER/ARUBA-70xx"
	elif prodcode == "72xx":
		prodname = "CONTROLLER/ARUBA-72xx"
	elif prodcode == "7280":
		prodname = "CONTROLLER/ARUBA-7280"
	elif prodcode == "90xx":
		prodname = "CONTROLLER/ARUBA-90xx"
	elif prodcode == "92xx":
		prodname = "CONTROLLER/ARUBA-92xx"
	elif prodcode == "MMC":
		prodname = "CONTROLLER/ARUBA-MOBILITY-MASTER"
	elif prodcode == "VMC":
		prodname = "CONTROLLER/ARUBA-VIRTUAL-MOBILITY-CONTROLLER"
	elif prodcode == "usb":
		prodname = "USB-CONSOLE"
	elif prodcode == "pdf":
		prodname = "DOCUMENTATION"
	elif prodcode == "webauth":
		prodname = "WEB-AUTH"
	elif prodcode == "zip":
		prodname = "ZIPS"
	elif prodcode == "vsr":
		prodname = "VSR-1000-JG811AAE"
	elif prodcode == "ArubaInstant_Vela":
		prodname = "Access-Points-Instant/203H-203R-207"
	elif prodcode == "ArubaInstant_Ursa":
		prodname = "Access-Points-Instant/300-303-303H-360"
	elif prodcode == "ArubaInstant_Hercules":
		prodname = "Access-Points-Instant/310-318-320-370-387"
	elif prodcode == "ArubaInstant_Lupus":
		prodname = "Access-Points-Instant/330"
	elif prodcode == "ArubaInstant_Draco":
		prodname = "Access-Points-Instant/340-510-518-570"
	elif prodcode == "ArubaInstant_Gemini":
		prodname = "Access-Points-Instant/500-500H-560"
	elif prodcode == "ArubaInstant_Scorpio":
		prodname = "Access-Points-Instant/530-550"
	elif prodcode == "ArubaInstant_Norma":
		prodname = "Access-Points-Instant/630-650"
	elif prodcode == "ArubaInstant_Centaurus":
		prodname = "Access-Points-Instant/210-220-228-270"
	elif prodcode == "psm":
		prodname = "Pensando"
	else:
		prodname = "UNKNOWN"
	return prodname


#A	Switch 2615-8-PoE and Switch 2915-8G-PoE
###C	1600M, 2400M, 2424M, 4000M, and 8000M
#CY	Switch 8100fl Series (8108fl and 8116fl)
#E	Switch 5300xl Series (5304xl, 5308xl, 5348xl, 5372xl, 5304xl-32G, and 5308xl-48G)
#F	Switch 2500 Series (2512 and 2524), Switch 2312, and Switch 2324
#G	Switch 4100gl Series (4104gl, 4108gl, 4140gl, 4148gl, and 4160gl)
###H	Switch 2600 Series, Switch 2600-PWR Series: H.07.81 and earlier, or H.08.55 and greater, Switch 2600-8-PWR requires H.08.80 or greater.Switch 6108: H.07.xx and earlier
#I	Switch 2800 Series (2824 and 2848)
#J	J.xx.xx.biz Secure Router 7000dl Series (7102dl and 7203dl)
#J	J.xx.xx.swi Switch 2520G Series (2520G-8-PoE, 2520G-24-PoE)
####K	3500 Series, 3500yl Series, 5400zl Series, 6200yl-24G Switch, Switch 6600 Series (6600-24G, 6600-24G-4XG, 6600-24XG, 6600-48G, 6600-48G-4XG), and 8200zl Series Switches
###KA	Switch 3800 Series
###KB	5400R zl2 Switch Series (5406R, 5406R-44G-PoE+/4SFP, 5406R-44G-PoE+/2SFP+, 5406R-8XGT/8SFP+, 5412R, 5412R-92G-PoE+/4SFP, and 5412R-92G-PoE+/2SFP+)
#L	Switch 4200vl Series (4202vl-72, 4202vl-48G, 4204vl, 4204vl-44G-4SFP, 4208vl, 4208vl-96, 4208vl-64G, and 4208vl-68G-4SFP)
#M	Switch 3400cl Series: M.08.51 though M.08.97, or M.10.01 and greater; Series 6400cl Series: M.08.51 though M.08.95, or M.08.99 to M.08.100 and greater.
####N	Switch 2810 Series (2810-24G and 2810-48G)
####P	Switch 1810G (1810G-8, 1810G-24)
###PA/PB	Switch 1800G Series (Switch 1800-8G - PA; Switch 1800-24G - PB)
###PK	Switch 1810-48G
###PL/PM	1810 v2 Switches (1810-8G v2, 1810-24G v2 - PL; 1810-8 v2, 1810-24 v2 - PM)
###PS	PS1810 Switches (PS1810-8G, PS1810-24G)
###Q	Switch 2510-24
###R	Switch 2610 Series (2610-24, 2610-48, 2610-24/12PWR, 2610-24-PWR, and 2610-48-PWR)
###RA	Switch 2620 Series
###S	Switch 2520 Series (2520-8-PoE, 2520-24-PoE)
###T	Switch 2900 Series
###U	Switch 2510-48
###VA/VB	Switch 1700 Series (Switch 1700-8 - VA and Switch 1700-24 - VB)
#W	Switch 2910al Series
#WA	HP Access Point 530
###WB	Switch 2920 Series
#WM	HP Access Point 10ag
#WS	HP Wireless Edge Services xl Module and the HP Redundant Wireless Services xl Module
#WT	HP Wireless Edge Services zl Module and the HP Redundant Wireless Services zl Module
#Y	Switch 2510G Series (2510G-24 and 2510G-48)
###YA	2530 Switches (2530-48, 2530-48-PoE+, 2530-8G, 2530-24G, 2530-48G, 2530-8G-PoE+, 2530-24G-PoE+, 2530-48G-PoE+, 2530-24G-2SFP+, 2530-48G-2SFP+, 2530-24G-PoE+-2SFP+, 2530-48G-PoE+-2SFP+)
###YB	2530 Switches (2530-8, 2530-24, 2530-8-PoE+, 2530-24-PoE+)
#Z	HP 6120G/XG and 6120XG Blade Switches


def util2digit (a,b):
	z = ".";
	y = (a,b)
	return z.join( y )

def util3digit (a,b,c):
	z = ".";
	y = (a,b,c)
	return z.join( y )

def util4digit (a,b,c,d):
	z = ".";
	y = (a,b,c,d)
	return z.join( y )

def util5digit (a,b,c,d,e):
	z = ".";
	y = (a,b,c,d,e)
	return z.join( y )

def filepath2 (a,b):
	z = "/";
	y = (a,b)
	return z.join( y )

def filepath3 (a,b,c):
	z = "/";
	y = (a,b,c)
	return z.join( y )

def filepath4 (a,b,c,d):
	z = "/";
	y = (a,b,c,d)
	return z.join( y )

def filepath5 (a,b,c,d,e):
	z = "/";
	y = (a,b,c,d,e)
	return z.join( y )


def base_directory_move (filename, prodname):
	filemove (prodname, filename)

def new_style_move (filename, prodname, workname, mysplit):
	if prodname == "UNKNOWN":
		message_unknown_device()
	else:
		splitbyuscore = workname.split(mysplit)
		if len(splitbyuscore) == 2:
			version2 = util2digit(splitbyuscore[0],splitbyuscore[1])
			filepath = filepath2(prodname,version2)
			filemove (filepath, filename)
		elif len(splitbyuscore) == 3:
			version2 = util2digit(splitbyuscore[0],splitbyuscore[1])
			version3 = util3digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2])
			filepath = filepath3(prodname,version2,version3)
			filemove (filepath, filename)
		elif len(splitbyuscore) == 4:
			version2 = util2digit(splitbyuscore[0],splitbyuscore[1])
			version3 = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
			filepath = filepath3(prodname,version2,version3)
			filemove (filepath, filename)
		elif len(splitbyuscore) == 5:
			version2 = util2digit(splitbyuscore[0],splitbyuscore[1])
			version3 = util5digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3],splitbyuscore[4])
			filepath = filepath3(prodname,version2,version3)
			filemove (filepath, filename)

def message_unknown_device ():
	print ("This device is unknown.")

def process_pdf (filename):
	prodname = product ("pdf")
	base_directory_move (filename, prodname)

def process_zip (filename):
	prodname = product ("zip")
	base_directory_move (filename, prodname)

def process_vsr (filename,prodname):
	if filename == "VSR1000_7.10.E0321.zip":
		version = util3digit("3","2","1")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.E0321P01.zip":
		version = util4digit("3","2","1","P01")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.E0322.zip":
		version = util3digit("3","2","2")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.E0322P01.zip":
		version = util4digit("3","2","2","P01")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.E0324.zip":
		version = util3digit("3","2","4")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.E0621P09-X64.zip":
		version = util4digit("6","2","1","P09")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.R0202.zip":
		version = util3digit("2","0","2")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.R0203.zip":
		version = util3digit("2","0","3")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.R0204.zip":
		version = util3digit("2","0","4")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.R0204P01.zip":
		version = util4digit("2","0","4","P01")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_7.10.R0621P18-X64.zip":
		version = util4digit("6","2","1","P18")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_HPE-CMW710-E0325-X64.zip":
		version = util3digit("3","2","5")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_HPE-CMW710-E0518-X64.zip":
		version = util3digit("5","1","8")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_HPE-CMW710-E0519L03-X64.zip":
		version = util4digit("5","1","9","L03")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_HPE-CMW710-R0326-X64.zip":
		version = util3digit("3","2","6")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR1000_HPE-CMW710-R0327L01-X64.zip":
		version = util4digit("3","2","7","L01")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR_7.10.E0101P01-B.zip":
		version = util4digit("1","0","1","P01-B")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)
	elif filename == "VSR_7.10.E0102.zip":
		version = util3digit("1","0","2")
		vprod = prodname + "/" +  version
		base_directory_move (filename, vprod)

def dirwalk (src,hashsha512,hashfile):

	names = os.listdir(src)
	os.chdir(src)
	for filename in names:
		if os.path.isdir(filename):
			continue
		if filename.endswith(".part"):
			continue
		print(filename)

		if (
			filename == "Thumbs.db" or
			filename == ".DS_Store" or
			filename == ".DS_Store.hash"
		):
			continue
		elif filename.endswith("pdf"):
			process_pdf(filename)
		elif (
			filename == "16.04_July2017device-api-v3.0.zip" or 
			filename == "16.02_device-rest-api.zip" or
			filename == "16.02_Aug2017device-api-v1.0.zip" or
			"API" in filename or 
			"api" in filename
			):
			prodname = product ("api")
			base_directory_move (filename, prodname)

		elif (
		filename.startswith("mibs") or 
		filename.startswith("MIBS") or 
		filename.startswith("MIBs") or 
		filename.startswith("standard-mibs_") or 
		filename.startswith("aruba-mibs_")
		):
			prodname = product ("mibs")
			base_directory_move (filename, prodname)
		elif "NetEdit" in filename:
			prodname = product ("NetEdit")
			base_directory_move (filename, prodname)
		elif (
			"Simulator" in filename or
			filename.startswith("ArubaOS-CX_") and filename.endswith("_ova.zip")
			):
			prodname = product ("sim")
			base_directory_move (filename, prodname)
		elif filename == "HTML_Templates_Web-Auth-Custom-HTML-Templates-Feb2012.zip":
			prodname = product ("webauth")
			base_directory_move (filename, prodname)
		elif (
		filename == "USB-Console-Drivers-Aug2013.zip" or 
		filename == "USB-Console-Disable-Serial-Num.reg" or 
		filename == "USB-Console-Info-Aug2013.pdf" or 
		filename == "USB-Console-Installer-Win32bit.EXE" or 
		filename == "USB-Console-Installer-Win64bit.EXE"
		):
			prodname = product ("usb")
			base_directory_move (filename, prodname)
		elif filename == "ArubaOS-CX_8320_10.00.0008.swi":
			prodname = product ("8320")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_8320_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename == "YB.15.16.0006.swi":
			prodname = product ("YB")
			workname = filename.replace(".swi","")
			workname = workname.replace("YB_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Centaurus_"):
			prodname = product ("ArubaInstant_Centaurus")
			workname = filename.replace("ArubaInstant_Centaurus_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Draco_"):
			prodname = product ("ArubaInstant_Draco")
			workname = filename.replace("ArubaInstant_Draco_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Gemini_"):
			prodname = product ("ArubaInstant_Gemini")
			workname = filename.replace("ArubaInstant_Gemini_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Hercules_"):
			prodname = product ("ArubaInstant_Hercules")
			workname = filename.replace("ArubaInstant_Hercules_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Lupus_"):
			prodname = product ("ArubaInstant_Lupus")
			workname = filename.replace("ArubaInstant_Lupus_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Norma_"):
			prodname = product ("ArubaInstant_Norma")
			workname = filename.replace("ArubaInstant_Norma_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Scorpio_"):
			prodname = product ("ArubaInstant_Scorpio")
			workname = filename.replace("ArubaInstant_Scorpio_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Ursa_"):
			prodname = product ("ArubaInstant_Ursa")
			workname = filename.replace("ArubaInstant_Ursa_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaInstant_Vela_"):
			prodname = product ("ArubaInstant_Vela")
			workname = filename.replace("ArubaInstant_Vela_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS-CX_10000_"):
			prodname = product ("10000")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_10000_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_4100i_"):
			prodname = product ("4100i")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_4100i_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_6100-6000_"):
			prodname = product ("6100-6000")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_6100-6000_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_6100_"):
			prodname = product ("6100")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_6100_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_6200_"):
			prodname = product ("6200")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_6200_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_6400-6300"):
			prodname = product ("6400-6300")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_6400-6300_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_8320"):
			prodname = product ("8320")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_8320_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_8325"):
			prodname = product ("8325")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_8325_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_8360"):
			prodname = product ("8360")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_8360_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_8400X"):
			prodname = product ("8400X")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_8400X_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_9300-32D_"):
			prodname = product ("9300")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_9300-32D_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS-CX_9300_"):
			prodname = product ("9300")
			workname = filename.replace(".swi","")
			workname = workname.replace("ArubaOS-CX_9300_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("ArubaOS_6xx_"):
			prodname = product ("6xx")
			workname = filename.replace("ArubaOS_6xx_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_70xx_"):
			prodname = product ("70xx")
			workname = filename.replace("ArubaOS_70xx_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_7280_"):
			prodname = product ("7280")
			workname = filename.replace("ArubaOS_7280_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_72xx_"):
			prodname = product ("72xx")
			workname = filename.replace("ArubaOS_72xx_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_90xx_"):
			prodname = product ("90xx")
			workname = filename.replace("ArubaOS_90xx_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_92xx_"):
			prodname = product ("92xx")
			workname = filename.replace("ArubaOS_92xx_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_MAS_"):
			prodname = product ("MAS")
			workname = filename.replace("ArubaOS_MAS_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_MMC_"):
			prodname = product ("MMC")
			workname = filename.replace("ArubaOS_MMC_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_MM_"):
			prodname = product ("MMC")
			workname = filename.replace("ArubaOS_MM_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("ArubaOS_VMC_"):
			prodname = product ("VMC")
			workname = filename.replace("ArubaOS_VMC_","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("A_"):
			prodname = product ("A")
			workname = filename.replace(".swi","")
			workname = workname.replace("A_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("CY"):
			prodname = product ("CY")
			workname = filename.replace(".swi","")
			workname = workname.replace("CY.","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("E_"):
			prodname = product ("E")
			workname = filename.replace(".swi","")
			workname = workname.replace("E_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("H_"):
			prodname = product ("H")
			workname = filename.replace(".swi","")
			workname = workname.replace("H_","")
		elif filename.startswith("I_"):
			prodname = product ("I")
			workname = filename.replace(".swi","")
			workname = workname.replace("I_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("J_"):
			prodname = product ("J")
			workname = filename.replace(".swi","")
			workname = workname.replace(".zip","")
			workname = workname.replace("J_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("K."):
			prodname = product ("K")
			workname = filename.replace(".swi","")
			workname = workname.replace("K.","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("KA_"):
			prodname = product ("KA")
			workname = filename.replace(".swi","")
			workname = workname.replace("KA_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("KB_"):
			prodname = product ("KB")
			workname = filename.replace(".swi","")
			workname = workname.replace(".zip","")
			workname = workname.replace("KB_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("K_"):
			prodname = product ("K")
			workname = filename.replace(".swi","")
			workname = workname.replace("K_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("L_"):
			prodname = product ("L")
			workname = filename.replace(".swi","")
			workname = workname.replace("L_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("M_"):
			prodname = product ("M")
			workname = filename.replace(".swi","")
			workname = workname.replace("M_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("N"):
			prodname = product ("N")
			workname = filename.replace(".swi","")
			workname = filename.replace(".zip","")
			workname = workname.replace("N_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("P."):
			prodname = product ("P")
			workname = filename.replace(".stk","")
			workname = workname.replace(".zip","")
			workname = workname.replace("P.","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("PA."):
			prodname = product ("PA")
			workname = filename.replace(".stk","")
			workname = workname.replace(".zip","")
			workname = workname.replace("PA.","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("PL."):
			prodname = product ("PL")
			workname = filename.replace(".img","")
			workname = workname.replace(".zip","")
			workname = workname.replace("PL.","")
			new_style_move (filename, prodname, workname, ".")
		elif filename.startswith("PL_"):
			prodname = product ("PL")
			workname = filename.replace(".img","")
			workname = workname.replace("PL_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("PM_"):
			prodname = product ("PM")
			workname = filename.replace(".img","")
			workname = workname.replace("PM_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("Q_"):
			prodname = product ("Q")
			workname = filename.replace(".swi","")
			workname = workname.replace("Q_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("RA_"):
			prodname = product ("RA")
			workname = filename.replace(".swi","")
			workname = workname.replace("RA_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("R_"):
			prodname = product ("R")
			workname = filename.replace(".swi","")
			workname = workname.replace(".zip","")
			workname = workname.replace("R_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("S_"):
			prodname = product ("S")
			workname = filename.replace(".swi","")
			workname = workname.replace("S_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("U_"):
			prodname = product ("U")
			workname = filename.replace(".swi","")
			workname = workname.replace(".zip","")
			workname = workname.replace("U_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("WB_"):
			prodname = product ("WB")
			workname = filename.replace(".swi","")
			workname = workname.replace("WB_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("WC_"):
			prodname = product ("WC")
			workname = filename.replace(".swi","")
			workname = workname.replace("WC_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("W_"):
			prodname = product ("W")
			workname = filename.replace(".swi","")
			workname = workname.replace("W_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("YA_"):
			prodname = product ("YA")
			workname = filename.replace(".swi","")
			workname = workname.replace("YA_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("YB_"):
			prodname = product ("YB")
			workname = filename.replace(".swi","")
			workname = workname.replace("YB_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("YC_"):
			prodname = product ("YC")
			workname = filename.replace(".swi","")
			workname = workname.replace("YC_","")
			new_style_move (filename, prodname, workname, "_")
		elif filename.startswith("Y_"):
			prodname = product ("Y")
			workname = filename.replace(".swi","")
			workname = workname.replace(".zip","")
			workname = workname.replace("Y_","")
			new_style_move (filename, prodname, workname, "_")

		elif (
		filename == "VSR1000_7.10.E0321.zip" or 
		filename == "VSR1000_7.10.E0321P01.zip" or 
		filename == "VSR1000_7.10.E0322.zip" or 
		filename == "VSR1000_7.10.E0322P01.zip" or 
		filename == "VSR1000_7.10.E0324.zip" or 
		filename == "VSR1000_7.10.E0621P09-X64.zip" or 
		filename == "VSR1000_7.10.R0202.zip" or 
		filename == "VSR1000_7.10.R0203.zip" or 
		filename == "VSR1000_7.10.R0204.zip" or 
		filename == "VSR1000_7.10.R0204P01.zip" or 
		filename == "VSR1000_7.10.R0621P18-X64.zip" or 
		filename == "VSR1000_HPE-CMW710-E0325-X64.zip" or 
		filename == "VSR1000_HPE-CMW710-E0518-X64.zip" or 
		filename == "VSR1000_HPE-CMW710-E0519L03-X64.zip" or 
		filename == "VSR1000_HPE-CMW710-R0326-X64.zip" or 
		filename == "VSR1000_HPE-CMW710-R0327L01-X64.zip" or 
		filename == "VSR_7.10.E0101P01-B.zip" or 
		filename == "VSR_7.10.E0102.zip"
		):
			prodname = product ("vsr")
			process_vsr(filename,prodname)
		elif (
		filename.startswith("pen-install") or
		filename.startswith("psm.apulu") or
		filename.startswith("psm.dss") or
		filename.startswith("psm_upgrade_bundle_")
		):
			prodname = product ("psm")
			workname = filename.replace("psm.apulu.","")
			workname = workname.replace("pen-install.dss.","")
			workname = workname.replace("psm.dss.","")
			workname = workname.replace("psm_upgrade_bundle_","")
			workname = workname.replace(".tar","")
			workname = workname.replace(".iso","")
			workname = workname.replace(".ova","")
			workname = workname.replace(".qcow2","")
			workname = workname.replace("-",".")
			filepath = prodname + "/" +  workname
			filemove (filepath, filename)

		elif filename.endswith(".zip"):
			process_zip(filename)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--directory', help='Directory to sort', required=True)
	parser.add_argument('-ha512','--hashsha512', help='Hash File using the SHA 512 Algorithm', action='store_true', required=False)
	parser.add_argument('-f','--hashfile', help='File with Hash Info. JSON Formating', action='store_true', required=False)
	
	args = parser.parse_args()
	inputdir = args.directory
	hashsha512 = args.hashsha512
	hashfile   = args.hashfile
	if not hashfile:
		hashfile = "hp.json"

	dirwalk(inputdir,hashsha512,hashfile)
