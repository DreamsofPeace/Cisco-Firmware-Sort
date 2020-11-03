from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessorsecurity (debug1,filename):
	if debug1:
		print("\tModule#\tios_security")
	if debug1:
		print("\tSubroutine#\tfileprocessorsecurity")

	if(
	filename == "anyconnect_app_selector_1.0.zip" or 
	filename == "anyconnect_app_selector_2.0.zip"
	):
		prodname = product("anyconnect")
		imagecode = imagelookup("app_selector")
		sec_single_file (debug1,filename,prodname,imagecode)

	elif filename == "release_duration_tool.tar":
		prodname = product ("firepower")
		imagecode = imagelookup("fmc")
		filepath = filepath4 (prodname,imagecode,"5.4.0","5.4.0.9")
		filemove (filepath, filename)

	elif (
	filename.startswith("sg") and filename.endswith("zip") or 
	filename.startswith("sg") and filename.endswith("adi") or 
	filename.startswith("sg") and filename.endswith("adi-gz")
	):
		sec_css (debug1,filename)

	elif (
	filename == "cvdm-css-1.0_K9.zip" or 
	filename == "cvdm-css-1.0.zip"
	):
		sec_css (debug1,filename)

	elif(
	filename.startswith("np") and filename.endswith(".bin") or 
	filename.startswith("pdm") and filename.endswith(".bin") or 
	filename == "PIXtoASA_1_0.zip" or 
	filename == "PIX_to_ASA_1_0.dmg" or 
	filename == "PIXtoASAsetup_1_0.exe" or 
	filename.startswith("pix") and filename.endswith(".bin") or 
	filename.startswith("PIX") and filename.endswith(".bin")
	):
		prodname = product("pix")
		sec_pix (debug1,filename,prodname)

	elif(
	filename == "fwsm_migration_mac-1.0.18.zip" or 
	filename == "fwsm_migration_win-1.0.18.zip"
	):
		prodname = product("asa")
		imagecode = imagelookup("fwsmtoasasm")
		sec_single_file (debug1,filename,prodname,imagecode)

	elif(
	filename.startswith ("coeus") or 
	filename.startswith ("phoebe")
	):
		sec_ironportv (debug1,filename)

	elif(
	filename.startswith ("cisco-asa-fp2k") or 
	filename.startswith ("cisco-asa")
	):
		sec_fp_asa_module (debug1,filename)

	elif(
	filename == "firepower-mibs.zip"
	):
		prodname = product("firepower")
		imagecode = imagelookup("mibs")
		sec_single_file (debug1,filename,prodname,imagecode)

	elif(
	filename == "BOOTX64.EFI" or 
	filename == "grub.efi"
	):
		prodname = product("ise")
		imagecode = "2.4/APPLIANCE-BOOT-SECTOR"
		sec_single_file (debug1,filename,prodname,imagecode)

	elif filename.startswith("asdm"):
		sec_asa_asdm (debug1,filename)

	elif filename.startswith("c6svc-fwm-k9"):
		sec_fwsm (debug1,filename)

	elif filename.startswith("csd_"):
		sec_csd (debug1,filename)

	elif filename.startswith("asasfr"):
		sec_asa_fp_sys (debug1,filename)

	elif (
	filename.startswith("asav") or
	filename.startswith("asa")
	):
		sec_asa_firmware (debug1,filename)

	elif filename.startswith("Cisco_Firepower_SRU") or filename.startswith("Sourcefire_Rule_Update"):
		sec_fp_rules (debug1,filename)

	elif filename.startswith("Cisco_Firepower_GEODB") or filename.startswith("Sourcefire_Geodb"):
		sec_fp_geodb (debug1,filename)

	elif filename.startswith("Cisco_VDB_Fingerprint_Database") or filename.startswith("Sourcefire_VDB"):
		sec_fp_vdb (debug1,filename)

	elif filename.startswith("hostscan_"):
		sec_hostscan (debug1,filename)

	elif (
	filename.startswith("anyconnect") or 
	filename.startswith("hostscan-") or 
	filename.startswith("thirdparty") or 
	filename.startswith("tools-anyconnect") or 
	filename.startswith("sampleTransforms")
	):
		sec_anyconnect (debug1,filename)

	elif (
	filename.startswith("fxos") or 
	filename.startswith("firepower")
	):
		sec_fxos (debug1,filename)

	elif (
	filename.startswith("Sourcefire_3D_Defense_Center_S3_Patch") or 
	filename.startswith("Sourcefire_3D_Defense_Center_S3_Hotfix")
	):
		sec_sourcefire_fmc_patch (debug1,filename)

	elif filename.startswith("Cisco_FTD_Patch"):
		sec_sourcefire_ftd_patch (debug1,filename)

	elif (
	filename.startswith("Sourcefire_3D_Device_S3_Patch") or 
	filename.startswith("Sourcefire_3D_Device_VMware_Patch")
	):
		sec_sourcefire_device (debug1,filename)

	elif filename.startswith("Cisco_Network_Sensor"):
		sec_fp_asa_mode (debug1,filename)

	elif (
	filename.startswith("ise-pic") or 
	filename == "pic-2.2.0.470.SPA.x86_64.iso" or 
	filename == "pic-2.4.0.357.SPA.x86_64.iso"
	):
		sec_ise_pic (debug1,filename)

	elif (
		filename == "README_ISE_20_201_21_22" or 
		filename.startswith("PI") or 
		filename.startswith("ISE") or 
		filename.startswith("ise") or 
		filename.startswith("mac-spw-dmg") or 
		filename.startswith("webagent") or 
		filename.startswith("win_spw") or 
		filename.startswith("ACS-MigrationApplication")
	):
		sec_ise (debug1,filename)

	elif (
		filename.startswith("ACS") or 
		filename.startswith("Acs") or 
		filename.startswith("Clean") or 
		filename.startswith("UCP") or 
		filename.startswith("applAcs") or 
		filename.startswith("5-") or 
		filename == "ACS57BasePatch.tar.gz" or 
		filename == "ReadMe_for_ACS_5.6_Upgrade_Package-txt"
	):
		sec_acs (debug1,filename)

	elif (
		filename.startswith ("fcs-csm") or 
		filename.startswith ("fcs-mcp") or 
		filename.startswith ("csm")
	):
		sec_csm (debug1,filename)


	elif (
		filename.startswith ("UTD-STD-SIGNATURE")
	):
		sec_utd_signature (debug1,filename)

	elif (
	filename.startswith("iosxe-utd") or 
	filename.startswith("iox-iosxe-utd") or 
	filename.startswith("secapp-ucmk9") or 
	filename.startswith("iosxe-utd-ips")
	):
		sec_utd_engine (debug1,filename)

	elif (
	filename.startswith("Sourcefire_Defense_Center_S3") or 
	filename.startswith("Sourcefire_Defense_Center_Virtual64_VMware") or 
	filename.startswith("Cisco_Firepower_Management_Center_Virtual_VMware") or 
	filename.startswith("Cisco_Firepower_Management_Center_Virtual") or 
	filename.startswith("Cisco_Firepower_Management_Center_VMware")
	):
		sec_fp_mgmt (debug1,filename)

	else:
		messageunknownfile()

def sec_single_file (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_single_file")
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def sec_fp_mgmt (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_utd_engine")
	prodname = product("firepower")
	imagecode = imagelookup("fmc")
	splitbydash = filename.split("-")
	if (
	filename.startswith("Sourcefire_Defense_Center_S3") or 
	filename.startswith("Sourcefire_Defense_Center_Virtual64_VMware") or 
	filename.startswith("Cisco_Firepower_Management_Center_Virtual_VMware") or 
	filename.startswith("Cisco_Firepower_Management_Center_Virtual") or 
	filename.startswith("Cisco_Firepower_Management_Center_VMware")
	):
		version = splitbydash[1]
		filepath = filepath3(prodname,imagecode,version)
		filemove (filepath, filename)

def sec_asa_fp_sys (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_asa_fp_sys")
	prodname =  product("firepower")
	imagecode = imagelookup("fpasasystem")
	splitbydash = filename.split("-")
#	splitbydot = splitbydash[2].split(".")
	if filename.startswith("asasfr-5500x-boot"):
		imagecode2 = imagelookup("boot")
		filepath = filepath4(prodname,imagecode,splitbydash[3],imagecode2)
		filemove (filepath, filename)
	elif filename.startswith("asasfr-boot"):
		imagecode2 = imagelookup("boot")
		filepath = filepath4(prodname,imagecode,splitbydash[2],imagecode2)
		filemove (filepath, filename)
	elif filename.startswith("asasfr-sys"):
		imagecode2 = imagelookup("system")
		filepath = filepath4(prodname,imagecode,splitbydash[2],imagecode2)
		filemove (filepath, filename)
	
def sec_utd_engine (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_utd_engine")
	prodname =  product("ciscoutd")
	imagecode = imagelookup("engine")
	filepath = filepath2(prodname,imagecode)
	filemove (filepath, filename)

def sec_utd_signature (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_utd_signature")
	splitbydash = filename.split("-")
	prodname =  product("ciscoutd")
	imagecode = imagelookup("signatures")
	filepath = filepath4(prodname,imagecode,splitbydash[3],splitbydash[4])
	filemove (filepath, filename)

def sec_ironportv (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_ironportv")
	splitbydash = filename.split("-")
	if filename.startswith ("coeus"):
		prodname = product("ironport")
		imagecode = imagelookup("websecurity")
	elif filename.startswith ("phoebe"):
		prodname = product("ironport")
		imagecode = imagelookup("emailsecurity")
	vertwo = util4digit(splitbydash[1],splitbydash[2])
	verfour = util4digit(splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
	filepath = filepath4 (prodname,imagecode,splitbydash[1],vertwo,verfour)
	filemove (filepath, filename)

def sec_fp_asa_mode (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fp_asa_mode")
	prodname = product("firepower")
	imagecode = imagelookup("fpasamode")
	if filename == "Cisco_Network_Sensor_Patch-6.0.1-29.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.1","6.0.1.0")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_A-6.2.0.1-10.sh":
		filepath = filepath4 (prodname,imagecode,"6.2.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_AF-6.1.0.2-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_DK-5.4.0.10-1.sh":
		filepath = filepath4 (prodname,imagecode,"5.4.0","5.4.0.9")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_O-6.0.0.999-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.0","6.0.0.1")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_H-6.2.3.999-5.sh.REL.tar":
		filepath = filepath4 (prodname,imagecode,"6.2.3","6.2.3.3")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_BN-6.2.2.999-5.sh.REL.tar":
		filepath = filepath4 (prodname,imagecode,"6.2.2","6.2.2.4")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_Hotfix_BW-6.2.0.999-6.sh":
		filepath = filepath4 (prodname,imagecode,"6.2.0","6.2.0.5")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.0.999-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.0.999-2.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.1.999-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-29.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-30.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
		filemove (filepath, filename)
	elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-32.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
		filemove (filepath, filename)
	elif filename.startswith("Cisco_Network_Sensor_Upgrade"):
		splitbydash = filename.split("-")
		filepath = filepath4 (prodname,imagecode,splitbydash[1],"INSTALL")
		filemove (filepath, filename)
	else:
		splitbydash = filename.split("-")
		splitbydot = splitbydash[1].split(".")
		verthree = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4 (prodname,imagecode,verthree,verfour)
		filemove (filepath, filename)

def sec_fp_asa_module (debug1,filename):
	prodname = product("firepower")
	imagecode = imagelookup("fpasamodule")
	splitbydot = filename.split(".")
	if splitbydot[4] == "SPA":
		verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4 (prodname,imagecode,verthree,verthree)
		filemove (filepath, filename)
	else:
		verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		verfour = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath4 (prodname,imagecode,verthree,verfour)
		filemove (filepath, filename)

def sec_csm (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_csm")
	prodname = product ("csm")
	if filename.startswith("csm-maxmind-geolitecity"):
		imagecode = imagelookup("csmgeoip")
		sec_csm_geoip (debug1,filename,prodname,imagecode)

def sec_csm_geoip (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_csm_geoip")
	workname = filename.replace("csm-maxmind-geolitecity-","")
	workname = workname.replace(".zip","")
	mylist = list(workname)
	myyear = mylist[0] + mylist[1] + mylist[2] + mylist[3]
	filepath = filepath3 (prodname,imagecode,myyear)
	filemove (filepath, filename)


def sec_pix (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_pix")

	if filename.startswith("np") and filename.endswith(".bin"):
		imagecode = imagelookup("pixpasswordrecovery")
		sec_single_file (debug1,filename,prodname,imagecode)
	elif filename.startswith("pdm") and filename.endswith(".bin"):
		imagecode = imagelookup("pdm")
		sec_single_file (debug1,filename,prodname,imagecode)
	elif filename == "PIXtoASA_1_0.zip":
		imagecode = imagelookup("PIXtoASA")
		sec_single_file (debug1,filename,prodname,imagecode)
	elif filename == "PIX_to_ASA_1_0.dmg":
		imagecode = imagelookup("PIXtoASA")
		sec_single_file (debug1,filename,prodname,imagecode)
	elif filename == "PIXtoASAsetup_1_0.exe":
		imagecode = imagelookup("PIXtoASA")
		sec_single_file (debug1,filename,prodname,imagecode)

def sec_asa_firmware (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_asa_firmware")

	if (
	filename.startswith("asa9") or 
	filename.startswith("asav9") or 
	filename.startswith("asa871")
	):
		prodname = product ("asa")
		sec_asa_firmware_v9 (debug1,filename,prodname)

	elif (
	filename.startswith("asa7") or 
	filename.startswith("asa8")
	):
		prodname = product ("asa")
		sec_asa_firmware_v7_8 (debug1,filename,prodname)

	elif (
	filename.startswith("asa-restapi")
	):
		prodname = product ("asa")
		sec_asa_rest_api (debug1,filename,prodname)
	else:
		messageunknownfile()

def sec_asa_rest_api (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_asa_rest_api")
	splitbydash = filename.split("-")
	imagecode = imagelookup("restapi")
	mylist = list(splitbydash[2])
	if len(mylist) == 3:
		myver = util3digit(mylist[0],mylist[1],mylist[2])
	elif len(mylist) == 4:
		myver = util4digit(mylist[0],mylist[1],mylist[2],mylist[3])
	elif len(mylist) == 6:
		v3 = mylist[3] + mylist[4] + mylist[5]
		myver = util4digit(mylist[0],mylist[1],mylist[2],v3)
	filepath = filepath3 (prodname,imagecode,myver)
	filemove (filepath, filename)


def sec_asa_firmware_v9 (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_asa_firmware_v9")
	splitbydash = filename.split("-")
#	print (len(splitbydash), end="\n")

	if (
	filename == "asa9101-smp-k8.bin" or 
	filename == "asav9101.vhdx" or 
	filename == "asav9101.qcow2" or 
	filename == "asav9101.zip"
	):
		filepath = filepath3 (prodname,"9.10","9.10.1")
		filemove (filepath, filename)

	elif len(splitbydash) == 1:
		workname = filename.replace("asav", "")
		workname = workname.replace("asa", "")
		splitbydot = workname.split(".")
		verlist = list(splitbydot[0])
		vertwo = util2digit(verlist[0],verlist[1])
		verthree = util3digit(verlist[0],verlist[1],verlist[2])
		filepath = filepath3 (prodname,vertwo,verthree)
		filemove (filepath, filename)

	elif (
	len(splitbydash) == 2
	):
		if (
		filename.endswith(".ova") or
		filename.endswith(".qcow2") or
		filename.endswith(".vmdk") or
		filename.endswith(".vhdx") or
		filename.endswith(".zip")
		):
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			workname = workname.replace(".qcow2", "")
			workname = workname.replace(".ova", "")
			workname = workname.replace(".vmdk", "")
			workname = workname.replace(".vhdx", "")
			workname = workname.replace(".zip", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verfour = util4digit(verlist[0],verlist[1],verlist[2],mysplitdashworkname[1])
			filepath = filepath3 (prodname,vertwo,verfour)
			filemove (filepath, filename)
		else:
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verthree = util3digit(verlist[0],verlist[1],verlist[2])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)

	elif (
	len(splitbydash) == 3
	):
		if (
		filename == "asa9101-lfbff-k8.SPA"
		):
			imagecode = imagelookup("lfbff")
			filepath = filepath4 (prodname,imagecode,"9.10","9.10.1")
			filemove (filepath, filename)

		elif (
		splitbydash[1] == "smp" and
		splitbydash[2] == "k8.bin"
		):
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verthree = util3digit(verlist[0],verlist[1],verlist[2])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)

		elif (
		splitbydash[2] == "k8.bin"
		):
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
			filepath = filepath3 (prodname,vertwo,verfour)
			filemove (filepath, filename)

		elif (
		splitbydash[1] == "lfbff" or
		splitbydash[2] == "k8.SPA"
		):
			imagecode = imagelookup("lfbff")
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verthree = util3digit(verlist[0],verlist[1],verlist[2])
			filepath = filepath4 (prodname,imagecode,vertwo,verthree)
			filemove (filepath, filename)
		elif (
		splitbydash[0] == "asav9" or
		splitbydash[0] == "asa9"
		):
			workname = filename.replace(".qcow2", "")
			workname = workname.replace(".vhdx", "")
			workname = workname.replace(".zip", "")
			workname = workname.replace("asav", "")
			workname = workname.replace("asa", "")
			workname = workname.replace("-smp-k8.bin", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
			verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)

	elif (
	len(splitbydash) == 4
	):
		if (
		splitbydash[2] == "smp" and
		splitbydash[3] == "k8.bin"
		):
			workname = filename.replace(".qcow2", "")
			workname = workname.replace(".vhdx", "")
			workname = workname.replace(".zip", "")
			workname = workname.replace("asav", "")
			workname = workname.replace("asa", "")
			workname = workname.replace("-smp-k8.bin", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
			filepath = filepath3 (prodname,vertwo,verfour)
			filemove (filepath, filename)
		elif (
		splitbydash[2] == "lfbff" and
		splitbydash[3] == "k8.SPA"
		):
			imagecode = imagelookup("lfbff")
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(verlist[0],verlist[1])
			verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
			filepath = filepath4 (prodname,imagecode,vertwo,verfour)
			filemove (filepath, filename)
		elif (
		splitbydash[0] == "asav9" or
		splitbydash[0] == "asa9"
		):
			workname = filename.replace(".qcow2", "")
			workname = workname.replace(".vhdx", "")
			workname = workname.replace(".zip", "")
			workname = workname.replace("asav", "")
			workname = workname.replace("asa", "")
			workname = workname.replace("-smp-k8.bin", "")
			mysplitdashworkname = workname.split("-")
			verlist = list(mysplitdashworkname[0])
			vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
			verthree = util4digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2],mysplitdashworkname[3])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)

	elif (
	len(splitbydash) == 5
	):
		if (
		splitbydash[3] == "smp" and
		splitbydash[4] == "k8.bin"
		):
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
			verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)
		elif (
		splitbydash[3] == "lfbff" and
		splitbydash[4] == "k8.SPA"
		):
			imagecode = imagelookup("lfbff")
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
			verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
			filepath = filepath4 (prodname,imagecode,vertwo,verthree)
			filemove (filepath, filename)

	elif (
	len(splitbydash) == 6
	):
		if (
		splitbydash[4] == "smp" and
		splitbydash[5] == "k8.bin"
		):
			workname = filename.replace("asav", "")
			workname = workname.replace("asa", "")
			mysplitdashworkname = workname.split("-")
			vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
			verthree = util4digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2],mysplitdashworkname[3])
			filepath = filepath3 (prodname,vertwo,verthree)
			filemove (filepath, filename)

	else:
		messageunknownfile()

def sec_asa_firmware_v7_8 (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_asa_firmware_v7_8")
	workname = filename.replace("asa", "")
	splitbydash = workname.split("-")

	if (
	len(splitbydash) == 2 or 
	len(splitbydash) == 3 and 
	filename.endswith("-smp-k8.bin")
	):
		verlist = list(splitbydash[0])
		vertwo = util2digit(verlist[0],verlist[1])
		verthree = util3digit(verlist[0],verlist[1],verlist[2])
		filepath = filepath3 (prodname,vertwo,verthree)
		filemove (filepath, filename)

	elif (
	filename.startswith("asa871") and
	filename.endswith(".ova")
	):
		verlist = list(splitbydash[0])
		splitbydash[1] = splitbydash[1].replace(".ova", "")
		verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
		filepath = filepath3 (prodname,vertwo,verfour)
		filemove (filepath, filename)
	else:
		verlist = list(splitbydash[0])
		vertwo = util2digit(verlist[0],verlist[1])
		verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
		filepath = filepath3 (prodname,vertwo,verfour)
		filemove (filepath, filename)

def sec_acs (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_acs")
	prodname = product ("acs")

	if (
	filename.startswith("Clean-")
	):
		imagecode = imagelookup("clean")
		sec_acs_vfour_patch (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("5-")
	):
		imagecode = imagelookup("patch")
		sec_acs_patch (filename,prodname,imagecode)

	elif (
		filename == "ACS57BasePatch.tar.gz"
	):
		imagecode = imagelookup("patch")
		filepath = filepath4 (prodname,"5.7.0.15",imagecode,"0")
		filemove (filepath, filename)

	elif (
		filename == "ACS_5.0.0.21_ADE_OS_1.2_upgrade.tar.gpg"
	):
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.0.0.21",imagecode)
		filemove (filepath, filename)

	elif (
		filename == "ReadMe_for_ACS_5.6_Upgrade_Package-txt"
	):
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.6.0.22",imagecode)
		filemove (filepath, filename)

	elif (
		filename == "applAcs_4.1.1.23_ACS-4.1-CSTacacs-CSCsg97429.zip" or 
		filename == "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429.zip" or 
		filename == "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429-Readme.txt"
	):
		imagecode = imagelookup("patch")
		filepath = filepath4 (prodname,"4.1.1.23",imagecode,"CSTacacs-CSCsg97429")
		filemove (filepath, filename)

	elif (
		filename == "ACS-5.0.0.21.iso" or 
		filename == "ACS_5.1.0.44.tar.gz" or 
		filename == "ACS_5.2.0.26.tar.gz" or 
		filename == "ACS_5.3.0.40.tar.gz" or 
		filename == "ACS_5.4.0.46.0a.tar.gz" or 
		filename == "ACS_5.5.0.46.tar.gz" or 
		filename == "ACS_5.6.0.22.tar.gz" or 
		filename == "ACS_5.7.0.15.tar.gz" or 
		filename == "ACS_5.8.0.32.tar.gz" or 
		filename == "ACS_5.8.1.4.tar.gz" or 
		filename == "ACS_v5.1.0.44.iso" or 
		filename == "ACS_v5.2.0.26.iso" or 
		filename == "ACS_v5.3.0.40.iso" or 
		filename == "ACS_v5.4.0.46.0a.iso" or 
		filename == "ACS_v5.5.0.46.iso" or 
		filename == "ACS_v5.6.0.22.iso" or 
		filename == "ACS_v5.7.0.15.iso" or 
		filename == "ACS_v5.8.0.32.iso" or 
		filename == "ACS_v5.8.1.4.iso" or 
		filename == "ACS_55_USB_Installation_tool.zip" or 
		filename == "ACS_56_USB_Installation_tool.zip" or 
		filename == "ACS_57_USB_Installation_tool.zip" or 
		filename == "ACS_581_USB_Installation_tool.zip" or 
		filename == "ACS_58_USB_Installation_tool.zip"
	):
		sec_acs_vfiveinstall (filename,prodname)

	elif (
	filename.startswith("ACS-4") or 
	filename.startswith("Acs-4") or 
	filename.startswith("Acs_4") or 
	filename.startswith("applAcs_4")
	):
		sec_acs_vfour (filename,prodname)
	else:
		messageunknownfile()

def sec_acs_vfiveinstall (filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_acs_vfiveinstall")

	if filename == "ACS_55_USB_Installation_tool.zip":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.5.0.46",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_56_USB_Installation_tool.zip":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.6.0.22",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_57_USB_Installation_tool.zip":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.7.0.15",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_58_USB_Installation_tool.zip":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.8.0.32",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_581_USB_Installation_tool.zip":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.8.1.4",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.1.0.44.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.1.0.44",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.2.0.26.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.2.0.26",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.3.0.40.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.3.0.40",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.4.0.46.0a.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.4.0.46",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.5.0.46.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.5.0.46",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.6.0.22.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.6.0.22",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.7.0.15.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.7.0.15",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.8.0.32.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.8.0.32",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_5.8.1.4.tar.gz":
		imagecode = imagelookup("upgrade")
		filepath = filepath3 (prodname,"5.8.1.4",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS-5.0.0.21.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.0.0.21",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.1.0.44.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.1.0.44",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.2.0.26.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.2.0.26",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.3.0.40.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.3.0.40",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.4.0.46.0a.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.4.0.46",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.5.0.46.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.5.0.46",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.6.0.22.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.6.0.22",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.7.0.15.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.7.0.15",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.8.0.32.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.8.0.32",imagecode)
		filemove (filepath, filename)

	elif filename == "ACS_v5.8.1.4.iso":
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,"5.8.1.4",imagecode)
		filemove (filepath, filename)

def sec_acs_vfour (filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_acs_vfour")

	if filename.endswith("-DOCs.zip"):
		imagecode = imagelookup("docs")
		sec_acs_vfour_software (debug1,filename,prodname,imagecode)

	elif filename.endswith("-BIN-K9.zip"):
		imagecode = imagelookup("install")
		sec_acs_vfour_software (debug1,filename,prodname,imagecode)

	elif (
	filename.endswith("-SW.zip") or 
	filename.endswith("-RA.zip") or 
	filename.endswith("-SW.exe") or 
	filename.endswith("-SW-Readme.txt") or 
	filename.endswith(".txt") or 
	filename.endswith("-Clean.zip") or 
	filename.startswith("applAcs_") and filename.endswith(".zip")
	):
		imagecode = imagelookup("patch")
		sec_acs_vfour_patch (debug1,filename,prodname,imagecode)

def sec_acs_vfour_software (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_acs_vfour_software")
	workname = filename.replace("-BIN-K9.zip", "")
	workname = workname.replace("-DOCs.zip", "")
	workname = workname.replace("ACS-", "")
	splitbydot = workname.split(".")
	verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath3 (prodname,verfour,imagecode)
	filemove (filepath, filename)

def sec_acs_vfour_patch (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_acs_vfour_patch")
	workname = filename.replace("-SW.zip", "")
	workname = workname.replace("-SW.exe", "")
	workname = workname.replace("-RA.zip", "")
	workname = workname.replace("-K9.zip", "")
	workname = workname.replace("-Clean.zip", "")
	workname = workname.replace("-SW-Readme.txt", "")
	workname = workname.replace("Acs-", "")
	workname = workname.replace("ACS-", "")
	workname = workname.replace("Acs_", "")
	workname = workname.replace("ACS_", "")
	workname = workname.replace("Clean-", "")
	splitbydot = workname.split(".")
	verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4 (prodname,verfour,imagecode,splitbydot[4])
	filemove (filepath, filename)

def sec_acs_patch (filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_acs_patch")
	workname = filename.replace(".tar.gpg","")
	splitbydash = workname.split("-")
	verfour = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
	filepath = filepath4 (prodname,verfour,imagecode,splitbydash[4])
	filemove (filepath, filename)

def sec_ise (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_iseh")
	prodname = product ("ise")

	if (
	filename == "README_ISE_20_201_21_22" or 
	filename == "ise-applystrutsfix-signed.x86_64.tar.gz" or 
	filename == "ise-rollbackstrutsfix-signed.x86_64.tar.gz"
	):
		imagecode = imagelookup("struts")
		sec_single_file (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ise-patchbundle-")
	):
		imagecode = imagelookup("patch")
		sec_ise_patch (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ISE-") and filename.endswith("ova") or 
	filename.startswith("ise-") and filename.endswith("iso")
	):
		imagecode = imagelookup("install")
		sec_ise_install (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ise-upgradebundle-")
	):
		imagecode = imagelookup("upgrade")
		sec_ise_upgrade (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ise-urtbundle-")
	):
		imagecode = imagelookup("urtbundle")
		sec_ise_urtbundle (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("win_spw-") and
	filename.endswith("-isebundle.zip") or 
	filename.startswith("mac-spw-dmg-") and
	filename.endswith("-isebundle.zip")
	):
		imagecode = imagelookup("supplicantpw")
		sec_ise_spw (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ACS-MigrationApplication-")
	):
		imagecode = imagelookup("acs_mig")
		sec_ise_acs_mig (debug1,filename,prodname,imagecode)

	else:
		messageunknownfile()

def sec_ise_acs_mig (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_acs_mig")
	workname = filename.replace("ACS-MigrationApplication-","")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	filepath = filepath3 (prodname,vertwo,imagecode)
	filemove (filepath, filename)

def sec_ise_spw (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_spw")
	workname = filename.replace("win_spw-","")
	workname = workname.replace("mac-spw-dmg-","")
	workname = workname.replace("-isebundle.zip","")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	filepath = filepath3 (prodname,vertwo,imagecode)
	filemove (filepath, filename)

def sec_ise_upgrade (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_upgrade")

	if filename =="ise-upgradebundle-1.4.x-to-2.2.0.470.1808.x86_64.tar.gz":
		vertwo = "2.2"

	elif filename =="ise-upgradebundle-2.0.x-2.3.x-to-2.4.0.357.SPA.x86_64.tar.gz":
		vertwo = "2.4"

	elif filename =="ise-upgradebundle-2.0.x-to-2.1.0.474.SPA.x86_64.tar.gz":
		vertwo = "2.1"

	elif filename =="ise-upgradebundle-2.0.x-to-2.2.0.470.1808.SPA.x86_64.tar.gz":
		vertwo = "2.2"

	elif filename =="ise-upgradebundle-2.0.x-to-2.2.0.470.SPA.x86_64.tar.gz":
		vertwo = "2.2"

	elif filename =="ise-upgradebundle-2.0.x-to-2.3.0.298.1808.SPA.x86_64.tar.gz":
		vertwo = "2.3"

	elif filename =="ise-upgradebundle-2.1.x-2.4.x-to-2.6.0.156.SPA.x86_64.tar.gz":
		vertwo = "2.6"

	elif filename =="ise-upgradebundle-2.2.0.470.1808.SPA.x86_64.tar.gz":
		vertwo = "2.2"

	elif filename =="ise-upgradebundle-2.2.0.470.SPA.x86_64.tar.gz":
		vertwo = "2.2"

	elif filename =="ise-upgradebundle-2.2.x-2.6.x-to-2.7.0.356.SPA.x86_64.tar.gz":
		vertwo = "2.7"

	elif filename =="ise-upgradebundle-2.3.0.298.SPA.x86_64.tar.gz":
		vertwo = "2.3"
	filepath = filepath3 (prodname,vertwo,imagecode)
	filemove (filepath, filename)

def sec_ise_install (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_install")
	workname = filename.replace("ise-","")
	workname = workname.replace("ISE-","")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	filepath = filepath3 (prodname,vertwo,imagecode)
	filemove (filepath, filename)

def sec_ise_patch (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_patch")
	workname = filename.replace("ise-patchbundle-","")
	splitbydot = workname.split(".")
	splitbydash = workname.split("-")
	patchnum = splitbydash[1].replace("Patch","")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	filepath = filepath4 (prodname,vertwo,imagecode,patchnum)
	filemove (filepath, filename)

def sec_ise_urtbundle (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_ise_urtbundle")
	workname = filename.replace("ise-patchbundle-","")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	filepath = filepath3 (prodname,vertwo,imagecode)
	filemove (filepath, filename)

def sec_ise_pic (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_ise_pic")
	prodname = product ("isepic")

	if filename.startswith("pic-"):
		sec_ise_pic_orig (filename,prodname)

	elif filename.startswith("ise-pic-"):
		sec_ise_pic_current (filename,prodname)
	else:
		messageunknownfile()

def sec_ise_pic_orig (filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_ise_pic_orig")
	splitbydot = filename.split(".")
	splitbydot[0] = splitbydot[0].replace("pic-","")
	imagecode = imagelookup("install")
	verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath3 (prodname,verfour,imagecode)
	filemove (filepath, filename)

def sec_ise_pic_current (filename,prodname):
	if debug1:
		print("\tSubroutine#\tsec_ise_pic_current")
	splitbydash = filename.split("-")

	if filename.startswith("ise-pic-patchbundle-"):
		splitbydash[4] = splitbydash[4].replace("Patch", "")
		version = splitbydash[3]
		imagecode = imagelookup("patch")
		filepath = filepath4 (prodname,version,imagecode,splitbydash[4])
		filemove (filepath, filename)

	elif filename.startswith("ise-pic-"):
		version = splitbydash[2]
		imagecode = imagelookup("install")
		filepath = filepath3 (prodname,version,imagecode)
		filemove (filepath, filename)
	else:
		messageunknownfile()

def sec_sourcefire_fmc_patch (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_sourcefire_fmc_patch")
	prodname = product ("firepower")
	imagecode = imagelookup("fmc")
	if filename == "Sourcefire_3D_Defense_Center_S3_Patch-5.4.1-59.sh":
		filepath = filepath4 (prodname,imagecode,"5.4.1","5.4.1")
		filemove (filepath, filename)
	elif filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_A-6.2.0.1-10.sh":
		filepath = filepath4 (prodname,imagecode,"6.2.0","6.2.0")
		filemove (filepath, filename)
	elif filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_AJ-6.1.0.2-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","6.1.0.1")
		filemove (filepath, filename)
	elif filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_AZ-6.1.0.3-1.sh":
		filepath = filepath4 (prodname,imagecode,"6.1.0","6.1.0.2")
		filemove (filepath, filename)
	elif (
	filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_BN-6.2.2.999-5.sh.REL.tar" or 
	filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_BS-6.2.2.5-3.sh.REL.tar"
	):
		filepath = filepath4 (prodname,imagecode,"6.2.0","6.2.2.4")
		filemove (filepath, filename)
	elif filename == "Sourcefire_3D_Defense_Center_S3_Hotfix_K-6.0.0.2-3.sh":
		filepath = filepath4 (prodname,imagecode,"6.0.0","6.0.0.1")
		filemove (filepath, filename)
	else:
#		imagecode2 = imagelookup("patch")
		workname = filename.replace(".sh.REL.tar", "")
		workname = workname.replace(".sh", "")
		splitbydash = workname.split("-")
		splitbydot = splitbydash[1].split(".")
		verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
		verfour = util4digit (splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
#		patchline = imagecode2 + splitbydot[3]
#		filepath = filepath5 (prodname,imagecode,vertwo,verfive,patchline)
		filepath = filepath4 (prodname,imagecode,verthree,verfour)
		filemove (filepath, filename)

def sec_sourcefire_ftd_patch (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_sourcefire_ftd_patch")
	prodname = product ("firepower")
	imagecode = imagelookup("ngfw")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[1].split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4 (prodname,imagecode,vertwo,verfour)
	filemove (filepath, filename)

def sec_sourcefire_device (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_sourcefire_device")
	prodname = product ("firepower")
	imagecode = imagelookup("sourcefiredev")
	if filename == "Sourcefire_3D_Device_S3_Patch-6.0.1-29.sh":
		filepath = filepath3 (prodname,imagecode,"6.0.1")
		filemove (filepath, filename)
	else:
		splitbydash = filename.split("-")
		splitbydot = splitbydash[1].split(".")
		vertwo = util2digit(splitbydot[0],splitbydot[1])
		verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4 (prodname,imagecode,vertwo,verfour)
		filemove (filepath, filename)

def sec_fp_vdb (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fp_vdb")
	splitbydash = filename.split("-")
	prodname = product ("firepower")

	if filename.startswith("Cisco_VDB_Fingerprint_Database"):
		imagecode = imagelookup("csfvdb")

	elif filename.startswith("Sourcefire_VDB"):
		imagecode = imagelookup("sfvdb")
	splitbydash[2] = splitbydash[2].replace(".sh.REL.tar", "")
	splitbydash[2] = splitbydash[2].replace(".sh", "")
	ver = util2digit (splitbydash[1],splitbydash[2])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fp_rules (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fp_rules")
	splitbydash = filename.split("-")
	prodname = product ("firepower")

	if filename.startswith("Cisco_Firepower_SRU"):
		imagecode = imagelookup("csfrules")

	elif filename.startswith("Sourcefire_Rule_Update"):
		imagecode = imagelookup("sfrules")
	ver = util4digit (splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fp_geodb (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fp_geodb")
	splitbydash = filename.split("-")
	splitbydash[4] = splitbydash[4].replace(".sh.REL.tar", "")
	splitbydash[4] = splitbydash[4].replace(".sh", "")
	prodname = product ("firepower")

	if filename.startswith("Cisco_Firepower_GEODB"):
		imagecode = imagelookup("csfgeodb")

	elif filename.startswith("Sourcefire_Geodb"):
		imagecode = imagelookup("sfgeodb")
	ver = util4digit (splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fxos_firmware (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_fxos_firmware")
	splitbydot = filename.split(".")
	version = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath3 (prodname,imagecode,version)
	filemove (filepath, filename)

def sec_fxos_firmware_recovery (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_fxos_firmware_recovery")
	splitbydot = filename.split(".")
	splitbydot[4] = splitbydot[4].strip("N")
	versiontwo = util2digit(splitbydot[4],splitbydot[5])
	versionfull = util4digit(splitbydot[4],splitbydot[5],splitbydot[6],splitbydot[7])
	filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
	filemove (filepath, filename)

def sec_fxos_firmware_d4_1_4 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_fxos_firmware_d4_1_4")
	splitbydot = filename.split(".")
	versiontwo = util2digit(splitbydot[1],splitbydot[2])
	versionfull = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
	filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
	filemove (filepath, filename)

def sec_fxos (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fxos")
	prodname = product("firepower")
	splitbydot = filename.split(".")

	if splitbydot[0] == "fxos-k9-fpr4k-firmware":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware (debug1,filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-k9-fpr9k-firmware":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware (debug1,filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-k9-manager" or splitbydot[0] == "fxos-k9":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_d4_1_4 (debug1,filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-k9-system" or splitbydot[0] == "fxos-k9-kickstart":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_recovery (debug1,filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-mibs-fp9k-fp4k" or splitbydot[0] == "firepower-mibs":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_d4_1_4 (debug1,filename,prodname,imagecode)

def sec_asa_asdm (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_asa_asdm")

	if filename == "asdm508.bin":
		prodname = product("asa")
		imagecode = imagelookup("asdm")
		vertwo = util2digit("5","0")
		verthree = util3digit("5","0","8")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)

	elif filename == "asdm-demo-722.msi":
		prodname = product("asa")
		imagecode = imagelookup("asdm")
		vertwo = util2digit("7","2")
		verthree = util3digit("7","2","2")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)

	elif filename == "asdm-openjre-7122.bin":
		prodname = product("asa")
		imagecode = imagelookup("asdm")
		vertwo = util2digit("7","1")
		verfour = util4digit("7","1","2","2")
		filepath = filepath4(prodname,imagecode,vertwo,verfour)

	elif filename == "asdm-openjre-7131.bin":
		prodname = product("asa")
		imagecode = imagelookup("asdm")
		vertwo = util2digit("7","1")
		verfour = util4digit("7","1","3","1")
		filepath = filepath4(prodname,imagecode,vertwo,verfour)
		filemove (filepath, filename)

	elif (
	filename.endswith("f.bin") or 
	filename.endswith("f.msi")
	):
		prodname = product("asa")
		imagecode = imagelookup("asdmf")
		sec_asa_asdm_to_ver (debug1,filename,prodname,imagecode)

	else:
		prodname = product("asa")
		imagecode = imagelookup("asdm")
		sec_asa_asdm_to_ver (debug1,filename,prodname,imagecode)

def sec_asa_asdm_to_ver (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_asa_asdm_to_ver")
#	workname = filename.replace("asdm-","")
	workname = filename.replace("f.bin","")
	workname = workname.replace(".bin","")
	workname = workname.replace(".msi","")
	splitbydash = workname.split("-")

	if len(splitbydash) == 2:
		sbd1 = list(splitbydash[1])
		vertwo = util2digit(sbd1[0],sbd1[1])
		verthree = util3digit(sbd1[0],sbd1[1],sbd1[2])
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)

	elif len(splitbydash) == 3:
		sbd1 = list(splitbydash[1])
		if len(sbd1) == 4:
			vertwo = util2digit(sbd1[0],sbd1[1])
			joint = sbd1[1] + sbd1[2]
			verfull = util3digit(sbd1[0],joint,sbd1[3])
		elif len(sbd1) == 3:
			vertwo = util2digit(sbd1[0],sbd1[1])
			verfull = util3digit(sbd1[0],sbd1[1],sbd1[2])
		filepath = filepath4(prodname,imagecode,vertwo,verfull)
		filemove (filepath, filename)

	elif len(splitbydash) == 4:
		if splitbydash[1] == "openjre":
			sbd1 = list(splitbydash[2])
			if len(sbd1) == 4:
				vertwo = util2digit(sbd1[0],sbd1[1])
				joint = sbd1[1] + sbd1[2]
				verfull = util3digit(sbd1[0],joint,sbd1[3])
			elif len(sbd1) == 3:
				vertwo = util2digit(sbd1[0],sbd1[1])
				verfull = util3digit(sbd1[0],sbd1[1],sbd1[2])
			filepath = filepath4(prodname,imagecode,vertwo,verfull)
			filemove (filepath, filename)

	else:
		messageunknownfile ()

def sec_fwsm (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_fwsm")
	splitbydot = filename.split(".")
	splitbydash = splitbydot[1].split("-")
	vertwo = util2digit(splitbydash[0],splitbydash[1])
	verthree = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	prodname = product("c6svc-fwm")
	filepath = filepath3(prodname,vertwo,verthree)
	filemove (filepath, filename)

def sec_hostscan (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_hostscan")
	splitbyuscore = filename.split("_")
	splitbyuscore[1] = splitbyuscore[1].replace("-k9.pkg", "")
	splitbydot = splitbyuscore[1].split(".")
	prodname = product("anyconnect")
	imagecode = imagelookup("hostscan")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_csd (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_csd")
	splitbyuscore = filename.split("_")
	splitbyuscore[1] = splitbyuscore[1].replace("-k9.pkg", "")
	splitbydot = splitbyuscore[1].split(".")
	prodname = product("anyconnect")
	imagecode = imagelookup("csd")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p1_d3_u (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect_p1_d3_u")
	splitbyuscore = filename.split("_")
	splitbydot = splitbyuscore[1].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p1_d3_v (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect_p1_d3_v")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[1].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect_p2_d3_v")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect_p3_d3_v")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect_p4_d3_v")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[4].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_anyconnect")
	prodname = product("anyconnect")
	splitbydash = filename.split("-")

	if (
	filename.startswith("thirdparty_") and filename.endswith("_3eTI_Docs.zip")
	):
		imagecode = imagelookup("thirdparty")
		sec_anyconnect_p1_d3_u (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("sampleTransforms-")
	):
		imagecode = imagelookup("transforms")
		sec_anyconnect_p1_d3_v (debug1,filename,prodname,imagecode)

	elif(
	filename.startswith("hostscan-posture-macosx-i386-") and filename.endswith("-pre-deploy-k9.dmg") or 
	filename.startswith("hostscan-posture-linux-x64-") and filename.endswith("-pre-deploy-k9.tar.gz")
	):
		imagecode = imagelookup("iseposture")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-posture-win-") or 
	filename.startswith("anyconnect-posture-mac-")
	):
		imagecode = imagelookup("iseposture")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif splitbydash[1] == "isecompliance" and splitbydash[2] == "win" or splitbydash[2] == "macosx":
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-compliance-")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-compliance-")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.endswith("-isecompliance-predeploy-k9.msi") or 
	filename.endswith("-isecompliance-webdeploy-k9.pkg") or 
	filename.endswith("-isecompliance-predeploy-k9.dmg")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("hostscan-win-") and filename.endswith("-pre-deploy-k9.msi")
	):
		imagecode = imagelookup("hostscan")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-macosx-i386-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux-64-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-win-vpnapi-")
	):
		imagecode = imagelookup("vpnapi")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macos-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux64-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-win-") and filename.endswith("-vpnapi.zip")
	):
		imagecode = imagelookup("vpnapi")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-") and filename.endswith("-EnableFIPS.tar.gz") or 
	filename.startswith("anyconnect-macosx-powerpc-") and filename.endswith("-EnableFIPS.tar.gz") or 
	filename.startswith("anyconnect-linux-64-") and filename.endswith("-EnableFIPS.tar.gz")
	):
		imagecode = imagelookup("fips")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-") and filename.endswith("-EnableFIPS.tar.gz")
	):
		imagecode = imagelookup("fips")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif splitbydash[1] == "EnableFIPS" and splitbydash[2] == "win":
		imagecode = imagelookup("fips")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif splitbydash[1] == "dart" and splitbydash[2] == "win":
		imagecode = imagelookup("dart")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif splitbydash[1] == "gina" and splitbydash[2] == "win":
		imagecode = imagelookup("gina")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif filename.startswith("anyconnect-gina-"):
		imagecode = imagelookup("gina")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif filename.startswith("anyconnect-profileeditor-win"):
		imagecode = imagelookup(splitbydash[1])
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-") and filename.endswith("-nvm-standalone-k9.msi") or 
	filename.startswith("anyconnect-macos-") and filename.endswith("-nvm-standalone.dmg") or 
	filename.startswith("anyconnect-linux64-") and filename.endswith("-nvm-standalone.tar.gz")
	):
		imagecode = imagelookup("nvm")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-nvm-win-")
	):
		imagecode = imagelookup("nvm")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-wince-ARMv4I-activesync-")
	):
		imagecode = imagelookup("wince")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-wince-ARMv4I-")
	):
		imagecode = imagelookup("wince")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-arm64-")
	):
		imagecode = imagelookup("winarm64")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-k9-")
	):
		imagecode = imagelookup("win")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-")
	):
		imagecode = imagelookup("win")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-k9-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-k9-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-")
	):
		imagecode = imagelookup("macosxpowerpc")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macos-")
	):
		imagecode = imagelookup("macos")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-predeploy-linux-64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p4_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-predeploy-linux-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-k9-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux64-") or 
	filename.startswith("anyconnect-Linux_64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-nam-win-")
	):
		imagecode = imagelookup("anyconnectnam")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-websecurity-win-")
	):
		imagecode = imagelookup("websecurity")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("tools-anyconnect-win-") and filename.endswith("-profileeditor-k9.msi")
	):
		imagecode = imagelookup("profileeditor")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("tools-anyconnect-win-") and filename.endswith("-transforms.zip")
	):
		imagecode = imagelookup("transforms")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-amp-win-")
	):
		imagecode = imagelookup("amp")
		sec_anyconnect_p3_d3_v (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-translations-")
	):
		imagecode = imagelookup("translations")
		sec_single_file (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-android-")
	):
		imagecode = imagelookup("android")
		sec_anyconnect_p2_d3_v (debug1,filename,prodname,imagecode)


def sec_css (debug1,filename):
	if debug1:
		print("\tSubroutine#\tsec_css")
	workname = filename.strip("sg")
	workname = workname.strip("adi-gz")
	workname = workname.strip("adi")
	workname = workname.strip("zip")
	verarray = list(workname)
	prodname = product("css")
	if filename == "cvdm-css-1.0_K9.zip":
		imagecode = imagelookup("devicemgr")
		filepath = filepath2 (prodname,imagecode)
		filemove (filepath, filename)
	if filename == "cvdm-css-1.0.zip":
		imagecode = imagelookup("devicemgr")
		filepath = filepath2 (prodname,imagecode)
		filemove (filepath, filename)
	if len(verarray) == 7:
		verp3 = verarray[5] + verarray[6] + verarray[7]
	else:
		verp3 = verarray[5] + verarray[6]
	verp1 = verarray[0] + verarray[1]
	verp2 = verarray[2] + verarray[3]
	verfull = util4digit(verp1,verp2,verarray[4],verp3)
	filepath = filepath4 (prodname,verp1,verp2,verfull)
	filemove (filepath, filename)