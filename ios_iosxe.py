from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname,utils_dev_v2_vf_imagecode,utils_dev_imagecode_v2_vf
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

	elif filename == "asr1000rp1-advipservicesk9.V152_1_S1_CSCTR15153_3.bin":
		prodname = product ("asr1000rp1")
		utilssingleprodname (debug1,filename,prodname)

	elif filename == "asr903rsp1-universalk9_npe.V154_3_S3_SR637267017_1.bin":
		prodname = product ("asr903rsp1")
		utilssingleprodname (debug1,filename,prodname)

	elif filename == "asr1000rp1-adventerprisek9.BLD_V122_33_XNC_ASR_RLS3_THROTTLE_LATEST_20090513_080032.bin":
		prodname = product ("asr1000rp1")
		utilssingleprodname (debug1,filename,prodname)

	elif (
	filename.startswith("isr1100-bootloader")
	):
		prodname = product ("c1100router")
		imagecode = imagelookup ("rommon")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("C8000-2N2S") or
	filename.startswith("C8000-1N")
	):
		prodname = product ("c8000be")
		imagecode = imagelookup ("rommon")
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
#4221 & 4221X
	elif filename.startswith("isr4200-firmware_nim_xdsl"):
		prodname = product ("isr4200")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4200_cpld_update"):
		prodname = product ("isr4200")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4200-universalk9"):
		prodname = product ("isr4200")
		temp = splitbydot[0].replace("isr4200-","")
		imagecode = imagelookup(temp)
		fileproc_iosxe (debug1,filename,prodname,imagecode)
#4351, 4331, 4331-DC, 4321
	elif filename.startswith("isr4300-hw-programmables"):
		prodname = product ("isr4300")
		imagecode = imagelookup ("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4300_cpld_update"):
		prodname = product ("isr4300")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)
# 4451, 4431
	elif filename.startswith("isr4400-firmware_nim_xdsl"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr4400_cpld_update"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("cpld_update")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("isr-hw-programmables"):
		prodname = product ("isr4400")
		imagecode = imagelookup ("hardware")
		utilssinglemove (debug1,filename,prodname,imagecode)
#ISR 4461
	elif filename.startswith("isr4400v2-firmware_nim_xdsl"):
		prodname = product ("isr4400v2")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
		filename.startswith("isr4400v2_cpld_update") or
		filename.startswith("isr4400v2-hw-programmable")
		):
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

	elif (
		filename.startswith("cat9k_iosxe") or 
		filename.startswith("cat9k_lite")
		):
		if filename.startswith("cat9k_iosxe"):
			prodname = product ("cat9k")
		elif filename.startswith("cat9k_lite"):
			prodname = product ("cat9k_lite")
		if prodname == "UNKNOWN":
			messageunknownfile ()
		else:
			if filename.endswith("smu.bin"):
				imagecode = imagelookup("smu")
				fileproc_iosxe (debug1,filename,prodname,imagecode)
			elif filename.endswith("apdp.bin"):
				imagecode = imagelookup("apdp")
				fileproc_iosxe (debug1,filename,prodname,imagecode)
			elif filename.endswith("apsp.bin"):
				imagecode = imagelookup("apsp")
				fileproc_iosxe (debug1,filename,prodname,imagecode)
			else:
				imagecode = imagelookup(splitbydot[0])
				fileproc_iosxe (debug1,filename,prodname,imagecode)

	elif filename.startswith("cat3k_caa"):
		prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if (
		filename.startswith("cat3k_caa-universalk9.SPA") or 
		filename.startswith("cat3k_caa-universalk9ldpe.SPA")
		):
			fileproc_iosxe_3 (debug1,filename,prodname,imagecode)
		else:
			fileproc_iosxe(debug1,filename,prodname,imagecode)

	elif filename.startswith("cat4500es8"):
		mdash = splitbydot[0].split("-")
		prodname = product (mdash[0])
		imagecode = imagelookup(mdash[1])
		fileproc_iosxe_3 (debug1,filename,prodname,imagecode)

	elif filename.startswith("ct5760"):
		mdash = splitbydot[0].split("-")
		prodname = product (mdash[0])
		imagecode = imagelookup(mdash[1])
		fileproc_iosxe_3 (debug1,filename,prodname,imagecode)

	elif (
		filename.startswith("WP76xx") or
		filename.startswith("WP7601") or
		filename.startswith("WP7603")
		):
		prodname = product ("isrg3moduleslte")
		utilssingleprodname (debug1,filename,prodname)

	elif filename.endswith("comp_matrix.xml"):
		prodname = product ("iosxeissumatrix")
		utilssingleprodname (debug1,filename,prodname)

	elif filename.startswith("cat4500e"):
		prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if (
		filename.startswith("cat4500e-universalk9") or 
		filename.startswith("cat4500e-universal") or 
		filename.startswith("cat4500e-universalk9_lite") or 
		filename.startswith("cat4500e-universal_lite")
		):
			fileproc_iosxe_3 (debug1,filename,prodname,imagecode)
		else:
			fileproc_iosxe(debug1,filename,prodname,imagecode)

	elif (
		filename.startswith("C9800-") or 
		filename.startswith("CW9800H") or
		filename.startswith("CW9800M")
		):
		fileproccontroller (debug1,filename)

	elif filename.startswith("ie9k_"):
		if filename.startswith("ie9k_iosxe_npe."):
			prodname = product ("ie9k")
			imagecode = imagelookup("cat9k_iosxe_npe")
			workname = filename.replace("ie9k_iosxe_npe.","")
			workname = workname.replace(".SPA.bin","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("ie9k_iosxe"):
			prodname = product ("ie9k")
			imagecode = imagelookup("iosxe")
			workname = filename.replace("ie9k_iosxe.","")
			workname = workname.replace(".SPA.bin","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("appqoe-dre"):
		prodname = product ("sdwan")
		imagecode = imagelookup("appqoe")
		filepath = filepath2(prodname,imagecode)
		filemove (filepath, filename)

	elif filename.startswith("c8000v"):
		if filename.startswith("c8000v-universalk9_16G_serial"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_16G_serial_efi"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_16G_vga"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_16G_vga_efi"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_8G_serial"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_8G_serial_efi"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_8G_vga"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_8G_vga_efi"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9_vga"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		elif filename.startswith("c8000v-universalk9"):
			prodname = product ("c8000v")
			imagecode = imagelookup("universalk9")
		fileproc_iosxe(debug1,filename,prodname,imagecode)
#		print (prodname, end="\n")
#		splitbydot = filename.split(".")
#		iosmain = util2digit(splitbydot[1],splitbydot[2])
#		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
#		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
#		filemove (filepath, filename)

	elif filename.startswith("c1100tg"):
			prodname = product ("c1100tg")
			imagecode = imagelookup("universalk9")
			fileproc_iosxe(debug1,filename,prodname,imagecode)
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
			fileproc_iosxe(debug1,filename,prodname,imagecode)

def fileproccontroller (debug1,filename):
	if debug1:
		print("\tSubroutine#\tfileproccontroller")
	if filename.startswith("C9800-AP-universalk9."):
		prodname = product ("C9800-APC")
		imagecode = imagelookup("universalk9")
		workname = filename.replace("C9800-AP-universalk9.","")
		workname = workname.replace(".zip","")
		file_prepare_standard_iosxe (debug1,filename,prodname,imagecode,workname)
	elif filename.startswith("C9800-40-universalk9_wlc"):
		prodname = product ("C9800-40")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("C9800-80-universalk9_wlc"):
		prodname = product ("C9800-80")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("C9800-CL-universalk9_kvm"):
		prodname = product ("C9800-CL")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("C9800-CL-universalk9"):
		prodname = product ("C9800-CL")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("C9800-L-universalk9_wlc"):
		prodname = product ("C9800-L")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("C9800-SW-iosxe-wlc"):
		prodname = product ("C9800-SW")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("CW9800H"):
		prodname = product ("CW9800H")
		fileproc_iosxe_controller (debug1,filename,prodname)
	elif filename.startswith("CW9800M"):
		prodname = product ("CW9800M")
		fileproc_iosxe_controller (debug1,filename,prodname)

def fileproc_iosxe_controller (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfileproc_iosxe_controller")
	if filename.endswith(".tar.gz"):
		imagecode = imagelookup("universal_cloud")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif "nfvis" in filename:
		imagecode = imagelookup("universal_cloud_nfvis")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif "esxi" in filename:
		imagecode = imagelookup("universal_cloud_esxi")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif "kvm" in filename:
		imagecode = imagelookup("universal_cloud_kvm")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif filename.endswith(".qcow2"):
		imagecode = imagelookup("universal_kvm")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif filename.endswith(".ova"):
		imagecode = imagelookup("install")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif "-wlc-universalk9." in filename:
		imagecode = imagelookup("universalk9")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif filename.endswith(".iso"):
		imagecode = imagelookup("install")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif filename.endswith(".bin"):
		imagecode = imagelookup("upgrade")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("C9800-80-universalk9_wlc.") or 
	filename.startswith("C9800-40-universalk9_wlc.") or 
	filename.startswith("C9800-L-universalk9_wlc.")
	):
		imagecode = imagelookup("universalk9")
		fileproc_iosxe (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("C9800-80-universalk9_kvm.") or 
	filename.startswith("C9800-40-universalk9_kvm.") or 
	filename.startswith("C9800-CL-universalk9_kvm.") or 
	filename.startswith("C9800-L-universalk9_kvm.") or 
	filename.startswith("C9800-CL-universalk9.") and filename.endswith(".run") 
	):
		imagecode = imagelookup("universalk9_kvm")
		fileproc_iosxe (debug1,filename,prodname,imagecode)

'''Image Names (9800-80, 9800-40, and 9800-L):
    C9800-80-universalk9_wlc.17.06.01.SPA.bin
    C9800-40-universalk9_wlc.17.06.01.SPA.bin
    C9800-L-universalk9_wlc.17.06.01.SPA.bin
Image Names (9800-CL):
    Cloud: C9800-CL-universalk9.17.06.01.SPA.bin
    Hyper-V/ESXi/KVM: C9800-CL-universalk9.17.06.01.iso, C9800-CL-universalk9.17.06.01.ova
    KVM: C9800-CL-universalk9.17.06.01.qcow2
    NFVIS: C9800-CL-universalk9.17.06.01.tar.gz
'''
#	if filename.startswith("C9800-CL-universalk9."):
#	if filename.startswith("C9800-40-universalk9_wlc") or 
#	if filename.startswith("C9800-80-universalk9_wlc") or 
#	if filename.startswith("C9800-AP-universalk9") or 
#	if filename.startswith("C9800-CL-universalk9") or 
#	if filename.startswith("C9800-CL-universalk9_kvm") or 
#	if filename.startswith("C9800-L-universalk9_wlc") or 
#	if filename.startswith("C9800-SW-iosxe-wlc")

def fileproc_iosxe_noimagecode (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfileproc_iosxe_noimagecode")
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
		filepath = filepath3(prodname,iosmain,iosfull)
		filemove (filepath, filename)

def fileproc_iosxe_3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tfileproc_iosxe_3")
	splitbydot = filename.split(".")
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		imagecode2 = imagelookup("smu")
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath5(prodname,iosmain,iosfull,imagecode2,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[2],splitbydot[3])
		iosfull = util3digit(splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)

def fileproc_iosxe (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tfileproc_iosxe")
	splitbydot = filename.split(".")
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")	
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		imagecode2 = imagelookup("smu")
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath5(prodname,iosmain,iosfull,imagecode2,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)

def file_prepare_standard_iosxe (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tSubroutine#\tfile_prepare_standard_iosxe")
	splitbydot = workname.split(".")
	if len(splitbydot) == 3:
		version_main = util2digit(splitbydot[0],splitbydot[1])
		version_full = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,version_main,version_full,imagecode)
		filemove (filepath, filename)
	