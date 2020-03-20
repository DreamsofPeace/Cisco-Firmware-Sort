from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def fileprocessorsecurity (filename):
	if filename.startswith("c6svc-fwm-k9"):
		sec_fwsm (filename)

	if filename.startswith("csd_"):
		sec_csd (filename)

	elif filename == "anyconnect_app_selector_2.0.zip":
		prodname = product("anyconnect")
		imagecode = imagelookup("app_selector")
		sec_single_file (filename,prodname,imagecode)

	elif filename.startswith("asdm"):
		sec_asa_asdm (filename)

	elif filename.startswith("Cisco_Firepower_SRU") or filename.startswith("Sourcefire_Rule_Update"):
		sec_fp_rules(filename)

	elif filename.startswith("Cisco_Firepower_GEODB") or filename.startswith("Sourcefire_Geodb"):
		sec_fp_geodb(filename)

	elif filename.startswith("Cisco_VDB_Fingerprint_Database") or filename.startswith("Sourcefire_VDB"):
		sec_fp_vdb(filename)

	elif filename.startswith("hostscan_"):
		sec_hostscan(filename)

	elif (
	filename.startswith("anyconnect") or 
	filename.startswith("hostscan-") or 
	filename.startswith("thirdparty") or 
	filename.startswith("tools-anyconnect") or 
	filename.startswith("sampleTransforms")
	):
		sec_anyconnect(filename)

	elif (
	filename.startswith("fxos") or 
	filename.startswith("firepower")
	):
		sec_fxos(filename)

	elif filename.startswith("Sourcefire_3D_Defense_Center_S3_Patch"):
		sec_sourcefire_fmc_patch(filename)
#	name.startswith("Cisco_FTD") or 
#	name.startswith("Cisco_Firepower_Threat") or 
#	name.startswith("Cisco_Network_Sensor") or 
#	name.startswith("firepower") or 
#	name.startswith("ftd")
#	):
#def sec_sourcefire (filename):
#	splitbydash = filename.split("-")
#	if splitbydash[0] == "Cisco_Firepower_Management_Center_Virtual":

def sec_sourcefire_fmc_patch (filename):
	prodname = product ("firepower")
	imagecode = imagelookup("fmc")
	imagecode2 = imagelookup("patch")
	workname = filename.replace(".sh.REL.tar", "")
	workname = workname.replace(".sh", "")
	splitbydash = workname.split("-")
	splitbydot = splitbydash[1].split(".")
	vertwo = util2digit (splitbydot[0],splitbydot[1])
	verfive = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	patchline = imagecode2 + splitbydot[3]
	filepath = filepath5 (prodname,imagecode,vertwo,verfive,patchline)
	filemove (filepath, filename)

def sec_fp_vdb (filename):
	splitbydash = filename.split("-")
	prodname = product ("firepower")
	if filename.startswith("Cisco_VDB_Fingerprint_Database"):
		imagecode = imagelookup("csfvdb")

	elif filename.startswith("Sourcefire_VDB"):
		imagecode = imagelookup("sfvdb")
	splitbydash[2] = splitbydash[2].replace(".sh", "")
	ver = util2digit (splitbydash[1],splitbydash[2])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fp_rules (filename):
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

def sec_fp_geodb (filename):
	splitbydash = filename.split("-")
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

def sec_single_file(filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def sec_fxos_firmware (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	version = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath3 (prodname,imagecode,version)
	filemove (filepath, filename)

def sec_fxos_firmware_recovery (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	splitbydot[4] = splitbydot[4].strip("N")
	versiontwo  = util2digit(splitbydot[4],splitbydot[5])
	versionfull = util4digit(splitbydot[4],splitbydot[5],splitbydot[6],splitbydot[7])
	filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
	filemove (filepath, filename)

def sec_fxos_firmware_d4_1_4 (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	versiontwo  = util2digit(splitbydot[1],splitbydot[2])
	versionfull = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
	filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
	filemove (filepath, filename)

def sec_fxos (filename):
	prodname = product("firepower")
	splitbydot = filename.split(".")
	if splitbydot[0] == "fxos-k9-fpr4k-firmware":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware(filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-k9-manager" or splitbydot[0] == "fxos-k9":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_d4_1_4(filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-k9-system" or splitbydot[0] == "fxos-k9-kickstart":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_recovery(filename,prodname,imagecode)

	elif splitbydot[0] == "fxos-mibs-fp9k-fp4k" or splitbydot[0] == "firepower-mibs":
		imagecode = imagelookup(splitbydot[0])
		sec_fxos_firmware_d4_1_4(filename,prodname,imagecode)

def sec_asa_asdm (filename):
	prodname = product("asdm")

def sec_fwsm (filename):
	splitbydot = filename.split(".")
	splitbydash = splitbydot[1].split("-")
	vertwo = util2digit(splitbydash[0],splitbydash[1])
	verthree = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	prodname = product("c6svc-fwm")
	filepath = filepath3(prodname,vertwo,verthree)
	filemove (filepath, filename)

def firewallpix (filename):
	prodname = product("pix")
	pixversion = list(filename)
	pix = pixversion[3] + "." + pixversion[4] + "(" + pixversion[5] + ")"
	pixprimary = pixversion[3] + "." + pixversion[4]
	filepath = product + "/" + pixprimary + "/" + pix
	filemove (filepath, filename)

def sec_hostscan (filename):
	splitbyuscore = filename.split("_")
	splitbyuscore[1] = splitbyuscore[1].replace("-k9.pkg", "")
	splitbydot = splitbyuscore[1].split(".")
	prodname = product("anyconnect")
	imagecode = imagelookup("hostscan")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_csd (filename):
	splitbyuscore = filename.split("_")
	splitbyuscore[1] = splitbyuscore[1].replace("-k9.pkg", "")
	splitbydot = splitbyuscore[1].split(".")
	prodname = product("anyconnect")
	imagecode = imagelookup("csd")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p1_d3_u (filename,prodname,imagecode):
	splitbyuscore = filename.split("_")
	splitbydot = splitbyuscore[1].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p1_d3_v (filename,prodname,imagecode):
	splitbydash = filename.split("-")
	splitbydot = splitbydash[1].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p2_d3_v (filename,prodname,imagecode):
	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p3_d3_v (filename,prodname,imagecode):
	splitbydash = filename.split("-")
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p4_d3_v (filename,prodname,imagecode):
	splitbydash = filename.split("-")
	splitbydot = splitbydash[4].split(".")
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect (filename):
	prodname = product("anyconnect")
	splitbydash = filename.split("-")

	if (
	filename.startswith("thirdparty_") and filename.endswith("_3eTI_Docs.zip")
	):
		imagecode = imagelookup("thirdparty")
		sec_anyconnect_p1_d3_u (filename,prodname,imagecode)

	elif (
	filename.startswith("sampleTransforms-")
	):
		imagecode = imagelookup("transforms")
		sec_anyconnect_p1_d3_v (filename,prodname,imagecode)

	elif(
	filename.startswith("hostscan-posture-macosx-i386-") and filename.endswith("-pre-deploy-k9.dmg") or 
	filename.startswith("hostscan-posture-linux-x64-") and filename.endswith("-pre-deploy-k9.tar.gz")
	):
		imagecode = imagelookup("iseposture")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-posture-win-") or 
	filename.startswith("anyconnect-posture-mac-")
	):
		imagecode = imagelookup("iseposture")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif splitbydash[1] == "isecompliance" and splitbydash[2] == "win" or splitbydash[2] == "macosx":
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-compliance-")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-compliance-")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.endswith("-isecompliance-predeploy-k9.msi") or 
	filename.endswith("-isecompliance-webdeploy-k9.pkg") or 
	filename.endswith("-isecompliance-predeploy-k9.dmg")
	):
		imagecode = imagelookup("isecompliance")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("hostscan-win-") and filename.endswith("-pre-deploy-k9.msi")
	):
		imagecode = imagelookup("hostscan")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-macosx-i386-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux-64-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-win-vpnapi-")
	):
		imagecode = imagelookup("vpnapi")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macos-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux64-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-linux-") and filename.endswith("-vpnapi.tar.gz") or 
	filename.startswith("anyconnect-win-") and filename.endswith("-vpnapi.zip")
	):
		imagecode = imagelookup("vpnapi")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-") and filename.endswith("-EnableFIPS.tar.gz") or 
	filename.startswith("anyconnect-macosx-powerpc-") and filename.endswith("-EnableFIPS.tar.gz") or 
	filename.startswith("anyconnect-linux-64-") and filename.endswith("-EnableFIPS.tar.gz")
	):
		imagecode = imagelookup("fips")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-") and filename.endswith("-EnableFIPS.tar.gz")
	):
		imagecode = imagelookup("fips")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif splitbydash[1] == "EnableFIPS" and splitbydash[2] == "win":
		imagecode = imagelookup("fips")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif splitbydash[1] == "dart" and splitbydash[2] == "win":
		imagecode = imagelookup("dart")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif splitbydash[1] == "gina" and splitbydash[2] == "win":
		imagecode = imagelookup("gina")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif filename.startswith("anyconnect-gina-"):
		imagecode = imagelookup("gina")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif filename.startswith("anyconnect-profileeditor-win"):
		imagecode = imagelookup(splitbydash[1])
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-") and filename.endswith("-nvm-standalone-k9.msi") or 
	filename.startswith("anyconnect-macos-") and filename.endswith("-nvm-standalone.dmg") or 
	filename.startswith("anyconnect-linux64-") and filename.endswith("-nvm-standalone.tar.gz")
	):
		imagecode = imagelookup("nvm")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-nvm-win-")
	):
		imagecode = imagelookup("nvm")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-wince-ARMv4I-activesync-")
	):
		imagecode = imagelookup("wince")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-wince-ARMv4I-")
	):
		imagecode = imagelookup("wince")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-arm64-")
	):
		imagecode = imagelookup("winarm64")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-k9-")
	):
		imagecode = imagelookup("win")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-win-")
	):
		imagecode = imagelookup("win")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-k9-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-k9-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-i386-")
	):
		imagecode = imagelookup("macosxi386")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macosx-powerpc-")
	):
		imagecode = imagelookup("macosxpowerpc")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-macos-")
	):
		imagecode = imagelookup("macos")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-predeploy-linux-64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p4_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-predeploy-linux-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-k9-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux64-") or 
	filename.startswith("anyconnect-Linux_64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-64-")
	):
		imagecode = imagelookup("linux64")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-linux-")
	):
		imagecode = imagelookup("linux")
		sec_anyconnect_p2_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-nam-win-")
	):
		imagecode = imagelookup("anyconnectnam")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-websecurity-win-")
	):
		imagecode = imagelookup("websecurity")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("tools-anyconnect-win-") and filename.endswith("-profileeditor-k9.msi")
	):
		imagecode = imagelookup("profileeditor")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("tools-anyconnect-win-") and filename.endswith("-transforms.zip")
	):
		imagecode = imagelookup("transforms")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

	elif (
	filename.startswith("anyconnect-amp-win-")
	):
		imagecode = imagelookup("amp")
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)
	elif (
	filename.startswith("anyconnect-translations-")
	):
		imagecode = imagelookup("translations")
		sec_single_file (filename,prodname,imagecode)
