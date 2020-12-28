from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname,utils_dev_v2_vf_imagecode,utils_dev_imagecode_v2_vf,utils_dev_imagecode_v2_vf_dash
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_wireless(debug1,filename):
	if debug1:
		print("\tModule#\t\tios_wireless")
	if debug1:
		print("\tSubroutine#\tfileprocessor_wireless")

	if filename == "MFG_CTVM_LARGE_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.103.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","103","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.131.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","131","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.135.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","135","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.140.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","140","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.6.101.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","6")
		verfour = util4digit("8","6","101","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.7.106.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","7")
		verfour = util4digit("8","7","106","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.8.111.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","111","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.8.120.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","120","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.5.140.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","140","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.8.111.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","111","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.8.120.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","120","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)

	elif (
	filename.startswith("AIR_CTVM_LARGE-K9_") or 
	filename.startswith("AIR_CTVM-K9_") or 
	filename.startswith("MFG_CTVM_")
	):
		prodname = product ("CTVM")
		wireless_controller_virtual (debug1,filename,prodname)

	elif (
	filename.startswith("AIR-AP1815-K9-ME-") 
	):
		prodname = product ("AP1815")
		workname = filename.replace(".tar","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".aes","")
		workname = workname.replace("AIR-AP1815-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP1830-K9-") 
	):
		newname = filename.split(".")
		prodname = product ("AP1830")
		workname = filename.replace(".tar","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".aes","")
		workname = workname.replace("AIR-AP1830-K9-","")
		if len(newname) > 2:
			wireless_all_dash_dot (debug1,filename,prodname,workname)
		else:
			wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP1850-K9-") 
	):
		newname = filename.split(".")
		prodname = product ("AP1850")
		workname = filename.replace(".tar","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".aes","")
		workname = workname.replace("AIR-AP1850-K9-","")
		if len(newname) > 2:
			wireless_all_dash_dot (debug1,filename,prodname,workname)
		else:
			wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("SWISMK9-") 
	):
		prodname = product ("SWISMK9")
		workname = filename.replace(".tar","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".aes","")
		workname = workname.replace("SWISMK9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("SWLC3750K9-") 
	):
		prodname = product ("SWLC3750K9")
		workname = filename.replace(".tar","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".aes","")
		workname = workname.replace("SWLC3750K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT5500-K9-") 
	):
		prodname = product ("CT5500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT5500-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT5500-LDPE-K9-") 
	):
		prodname = product ("CT5500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT5500-LDPE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CTVM-")
	):
		prodname = product ("CTVM")
		workname = filename.replace(".aes","")
		workname = workname.replace(".ova","")
		workname = workname.replace("AIR-CTVM-K9-","")
		workname = workname.replace("AIR-CTVM-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT2500-K9-") 
	):
		prodname = product ("CT2500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT2500-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLC4400-K9-") 
	):
		prodname = product ("WLC4400")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WLC4400-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLC4100-K9-") 
	):
		prodname = product ("WLC4100")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WLC4100-K9-","")
		newname = filename.split(".")
		if len(newname) > 2:
			wireless_all_dash_dot (debug1,filename,prodname,workname)
		else:
			wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLC2100-K9-") 
	):
		prodname = product ("WLC2100")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WLC2100-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLC2006-K9-") 
	):
		prodname = product ("WLC2006")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WLC2006-K9-","")
		newname = filename.split(".")
		if len(newname) > 2:
			wireless_all_dash_dot (debug1,filename,prodname,workname)
		else:
			wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT5520-K9-") 
	):
		prodname = product ("CT5520")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT5520-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT3504-K9-") 
	):
		prodname = product ("CT3504")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT3504-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT7500-K9-") 
	):
		prodname = product ("CT7500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT7500-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT8500-K9-") 
	):
		prodname = product ("CT8500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT8500-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLCM-K9-") 
	):
		prodname = product ("WLCM")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WLCM-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT8540-K9-") 
	):
		prodname = product ("CT8540")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-CT8540-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WISM2-K9-") 
	):
		prodname = product ("WISM2")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WISM2-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP1840-K9-ME-") 
	):
		prodname = product ("AP1840")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP1840-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP1540-K9-ME-") 
	):
		prodname = product ("AP1540")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP1540-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP1560-K9-ME-") 
	):
		prodname = product ("AP1560")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP1560-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP2800-K9-ME-") 
	):
		prodname = product ("AP2800")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP2800-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP3800-K9-ME-") 
	):
		prodname = product ("AP3800")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP3800-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP4800-K9-ME-") 
	):
		prodname = product ("AP4800")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP4800-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-AP4800-K9-ME-") 
	):
		prodname = product ("AP4800")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-AP4800-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WLC-SRE-K9-") 
	):
		prodname = product ("SRE")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-WLC-SRE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-6300-K9-ME-") or 
	filename.startswith("AIR-AP6300-K9-ME-") 
	):
		prodname = product ("AP6300")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace(".tar","")
		workname = workname.replace("AIR-6300-K9-ME-","")
		workname = workname.replace("AIR-AP6300-K9-ME-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-LOC2700-L-K9-") 
	):
		prodname = product ("LOC2700")
		workname = filename.replace(".bin.gz","")
		workname = workname.replace(".bin","")
		workname = workname.replace("AIR-LOC2700-L-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AP_BUNDLE_3500_") 
	):
		prodname = product ("CT3504")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AP_BUNDLE_3500_","")
		wireless_all_underscore (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT2500-AP_BUNDLE-K9-") 
	):
		prodname = product ("CT2500")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-CT2500-AP_BUNDLE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT5500-LDPE-AP_BUNDLE-K9-") 
	):
		prodname = product ("CT5500")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-CT5500-LDPE-AP_BUNDLE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-CT5500-AP_BUNDLE-K9-") 
	):
		prodname = product ("CT5500")
		workname = filename.replace(".aes","")
		workname = workname.replace(".zip","")
		workname = workname.replace("AIR-CT5500-AP_BUNDLE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
	filename.startswith("AIR-WISM2-AP_BUNDLE-K9-") 
	):
		prodname = product ("CT5500")
		workname = filename.replace(".aes","")
		workname = workname.replace("AIR-WISM2-AP_BUNDLE-K9-","")
		wireless_all_dash (debug1,filename,prodname,workname)

	elif (
		filename.startswith ("WGB350") and filename.endswith ("exe")
	):
		prodname = product ("c350")
		imagecode = imagelookup("WKGBDG")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename.startswith ("BR350") and filename.endswith ("exe")
	):
		prodname = product ("c350")
		imagecode = imagelookup("WRLBDG")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename == "AP350-Cisco-IOS-Upgrade-Image-v2.img"
	):
		prodname = product ("c350")
		imagecode = imagelookup("vxworks")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename == "AP1200-Cisco-IOS-Upgrade-Image-v3.img"
	):
		prodname = product ("c1200")
		imagecode = imagelookup("vxworks")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename == "webauth_bundle.zip" or 
		filename == "webauth_bundle-1.0.2.zip"
	):
		prodname = product ("wireless")
		imagecode = imagelookup("webauth")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("CiscoAironet-AP-to-LWAPP-Upgrade-Tool-") 
	):
		prodname = product ("wireless")
		imagecode = imagelookup("aptolwapp")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename == "Aironet-AP-Cisco-IOS-Conversion-Tool-v2.1.exe"
	):
		prodname = product ("wireless")
		imagecode = imagelookup("vxworkstoios")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("WCS-STANDARD-K9-") 
	):
		prodname = product ("wcs")
		workname = filename.replace(".bin","")
		workname = workname.replace(".exe","")
		workname = workname.replace("WCS-STANDARD-K9-","")
		wireless_all_dash_dot (debug1,filename,prodname,workname)

def wireless_all_underscore (debug1,filename,prodname,workname):
	if debug1:
		print("\tSubroutine#\twireless_all_underscore")
	splitbyuscore = workname.split("_")
	vertwo = util2digit(splitbyuscore[0],splitbyuscore[1])
	verfour = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)

def wireless_all_dash_dot (debug1,filename,prodname,workname):
	if debug1:
		print("\tSubroutine#\twireless_all_dash")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)

def wireless_all_dash (debug1,filename,prodname,workname):
	if debug1:
		print("\tSubroutine#\twireless_all_dash")
	splitbydash = workname.split("-")
	vertwo = util2digit(splitbydash[0],splitbydash[1])
	verfour = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)

def wireless_controller_virtual (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\twireless_controller_virtual")
	workname = filename.replace("AIR_CTVM_LARGE-K9_","")
	workname = filename.replace("AIR_CTVM_LARGE_","")
	workname = workname.replace("AIR_CTVM-K9_","")
	workname = workname.replace("MFG_CTVM_LARGE_","")
	workname = workname.replace("MFG_CTVM_","")
	workname = workname.replace(".ova","")
	workname = workname.replace(".iso","")
	workname = workname.replace(".aes","")
	splitbyuscore = workname.split("_")
	vertwo = util2digit(splitbyuscore[0],splitbyuscore[1])
	verfour = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)
