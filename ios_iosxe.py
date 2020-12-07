from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_iosxe(debug1,filename):
	if debug1:
		print("\tModule#\t\tios_iosxe")
	if debug1:
		print("\tSubroutine#\tfileprocessor_iosxe")

	splitbydot = filename.split(".")
	splitbydash = filename.split("-")

	if (
	filename == "cat9k_iosxe.16.00.00fpgautility.SPA.bin" or 
	filename == "cat9k_fpga_upgrade_utility.pdf"
	):
		prodname = product ("cat9k")
		imagecode = imagelookup ("fpga")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "asr1000rpx86-universalk9.V1612_1_CVE_2019_1649.SPA.bin":
		prodname = product ("asr1000rpx86")
		imagecode = imagelookup ("hardware")
		utilssingleprodname (debug1,filename,prodname)

	elif (
	filename == "c1100_phy_fw_A39x3_B39x3.pkg" or 
	filename == "c1100_gfast_phy_fw_A43r_B43r.pkg" or 
	filename == "c1100_gfast_phy_fw_A43j2.pkg"
	):
		prodname = product ("c1100router")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "nim_vab_phy_fw_A39x3_B39x3_Bond39t.pkg" or 
	filename == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg" or 
	filename == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg" or 
	filename.startswith("isr4300-firmware_nim_xdsl")
	):
		prodname = product ("isr4300")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("iosxe-sd-avc")
	):
		prodname = product ("iosxe-sd-avc")
		utilssingleprodname (debug1,filename,prodname)

	elif (
	filename.startswith("iosxe-remote-mgmt")
	):
		prodname = product ("iosxe-remote-mgmt")
		utilssingleprodname (debug1,filename,prodname)

	elif (
	filename.startswith("CAT3650_WEBAUTH_BUNDLE") or 
	filename.startswith("CAT3850_WEBAUTH_BUNDLE")
	):
		prodname = product ("cat3k_caa")
		imagecode = imagelookup ("webauth")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4200-firmware_nim_xdsl"):
		prodname = product ("isr4200")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4400-firmware_nim_xdsl"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4400v2-firmware_nim_xdsl"):
		prodname = product ("isr4400v2")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4300-hw-programmables"):
		prodname = product ("isr4300")
		imagecode = imagelookup ("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr-hw-programmables"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4200_cpld_update"):
		prodname = product ("isr4200")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4300_cpld_update"):
		prodname = product ("isr4300")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4400_cpld_update"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4400v2_cpld_update"):
		prodname = product ("isr4400v2")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("asr1000-hw-programmables") or 
	filename.startswith("asr1002x-hw-programmables") or 
	filename == "ASR1K-fpga_prog.16.0.1.xe.bin"
	):
		prodname = product ("asr1000")
		imagecode = imagelookup("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("asr1000rpx86-hw-programmables")
	):
		prodname = product ("asr1000rpx86")
		imagecode = imagelookup("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("cat9k_iosxe") or filename.startswith("cat9k_lite"):
		if filename.startswith("cat9k_iosxe"):
			prodname = product ("cat9k")
		elif filename.startswith("cat9k_lite"):
			prodname = product ("cat9k_lite")
		if prodname == "UNKNOWN":
			messageunknownfile ()
		else:
			if filename.endswith("smu.bin"):
				imagecode = imagelookup("smu")
				fileproc_iosxe (filename,prodname,imagecode)
			else:
				imagecode = imagelookup(splitbydot[0])
				fileproc_iosxe (filename,prodname,imagecode)

	elif filename.startswith("cat3k_caa"):
		prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if (
		filename.startswith("cat3k_caa-universalk9.SPA") or 
		filename.startswith("cat3k_caa-universalk9ldpe.SPA")
		):
			fileproc_iosxe_3 (filename,prodname,imagecode)
		else:
			fileproc_iosxe(filename,prodname,imagecode)

	elif (
	splitbydot[0] == "C9800-40-universalk9_wlc" or 
	splitbydot[0] == "C9800-80-universalk9_wlc" or 
	splitbydot[0] == "C9800-CL-universalk9" or 
	splitbydot[0] == "C9800-L-universalk9_wlc" or 
	splitbydot[0] == "C9800-SW-iosxe-wlc" or 
	splitbydot[0] == "C9800-AP-universalk9"
	):
		fileproccontroller (filename)

	elif "ucmk9" in filename:
		if splitbydash[0] == "c1100":
			prodname = product ("c1100router")
		else:
			prodname = product (splitbydash[0])
		imagecode = imagelookup("ucmk9")
		fileproc_sdwan (filename,prodname,imagecode)

	else:
		if splitbydash[0] == "c1100":
			prodname = product ("c1100router")
		else:
			prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if prodname == "UNKNOWN":
			messageunknowndev()
		elif imagecode == "UNKNOWN":
			messageunknownfeat()
		else:
			fileproc_iosxe(filename,prodname,imagecode)

def fileproccontroller (filename):
	if filename.startswith("C9800-40-universalk9_wlc"):
		prodname = product ("C9800-40")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-80-universalk9_wlc"):
		prodname = product ("C9800-80")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-CL-universalk9"):
		prodname = product ("C9800-CL")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-L-universalk9_wlc"):
		prodname = product ("C9800-L")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-SW-iosxe-wlc"):
		prodname = product ("C9800-SW")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-AP-universalk9"):
		prodname = product ("C9800-AP")
		fileproc_iosxe_noimagecode (filename,prodname)

def fileproc_iosxe_noimagecode (filename,prodname):
	splitbydot = filename.split(".")
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath3(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath3(prodname,iosmain,iosfull)
		filemove (filepath, filename)

def fileproc_iosxe_3 (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[2],splitbydot[3])
		iosfull = util3digit(splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)

def fileproc_iosxe (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)


def fileproc_sdwan (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	iosmain = util2digit(splitbydot[1],splitbydot[2])
	iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	prodname = prodname.replace("Routers/ISRG3/", "")
	prodname = prodname.replace("Routers/ASR/", "")
	filepath = filepath4(imagecode,prodname,iosmain,iosfull)
	filemove (filepath, filename)
