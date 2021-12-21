from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname,utils_dev_v2_vf_imagecode,utils_dev_imagecode_v2_vf
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessornxos (filename,debug1):
	if debug1:
		print("\tModule#\t\tios_nexus")
	if debug1:
		print("\tSubroutine#\tfileprocessornxos")
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")

	if (
	filename.startswith("ssd_c400_upgrade") or 
	filename == "upgrade_m500_firmware.tar.gz"
	):
		prodname = product("nxos")
		imagecode = imagelookup("firmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "n9000-epld-secure-boot-update.img":
		prodname = product("nxos")
		imagecode = imagelookup("epld")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "poap_script.py" or 
	filename == "poap_script.tcl"
	):
		prodname = product("n3500")
		imagecode = imagelookup("poap")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "L2-L3_CT.zip":
		prodname = product("n1000v")
		imagecode = imagelookup("l2l3cvt")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "nxos-n3kbios.bin" or 
	filename == "n3k_bios_release_rn.pdf"
	):
		prodname = product("n3000")
		imagecode = imagelookup("bios")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "nxos.9.3.4-capacity-emulator.tgz":
		prodname = product("nxos")
		imagecode = imagelookup("capacity-emulator")
		workname = filename.replace("-capacity-emulator.tgz","")
		workname = workname.replace("nxos.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif filename == "ntp-1.0.1-7.0.3.I2.2d.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2d/NTP"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "ntp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2e/NTP"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "ntp-1.0.2-7.0.3.I2.2e.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2e/NTP"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "nxos.nsqos_lc_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2e/QoS"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "nxos.nsqos_sup_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2e/QoS"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "snmp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/7.0/7.0.3.I2.2e/SNMP"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "vxlan-2.0.1.0-9.2.3.lib32_n9000.rpm":
		prodname = product("nxos")
		imagecode = imagelookup("smu")
		imagecode = imagecode + "/9.2/9.2.3/VXLAN"
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("n6000_poap_script"):
		prodname = product("n6000")
		imagecode = imagelookup("poap")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("poap_ng"):
		prodname = product("Nexus")
		imagecode = imagelookup("poap_ng")
		workname = filename.replace(".py","")
		workname = workname.replace("poap_ng.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif (
	filename.startswith("Nexus1000v") or 
	filename.startswith("Nexus1000V")
	):
		prodname = product("n1000v")
		fileprocnxos1000v (debug1,filename,prodname)

	elif splitbydot[0] == "n9000-epld":
		prodname = product("nxos")
		imagecode = imagelookup("epld")
		if splitbydot[1] == "6" or splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)

	elif splitbydot[0] == "n9000-dk9":
		prodname = product("n9000")
		if splitbydot[1] == "6" or splitbydot[1] == "7":
			if splitbydot[6].startswith("CSC"):
				imagecode = imagelookup("smu")
				fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
			else:
				imagecode = imagelookup("system")
				fileprocnxosfivedigit (filename,prodname,imagecode,debug1)

	elif splitbydot[0] == "n7000-s1-epld" or splitbydot[0] == "n7000-s2-epld":
		prodname = product("n7000")
		imagecode = imagelookup("epld")
		if splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)

	elif (
	splitbydot[0] == "nxos" or 
	splitbydot[0] == "nxos64"
	):
		prodname = product("nxos")
		if len(splitbydot) == 5:
			imagecode = imagelookup("system")
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
		elif len(splitbydot) == 6:
			imagecode = imagelookup("system")
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
		elif len(splitbydot) == 7:
			imagecode = imagelookup("system")
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		elif len(splitbydot) == 7:
			imagecode = imagelookup("system")
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		elif splitbydot[1].startswith("CSC"):
			imagecode = imagelookup("smu")
			fileprocessornxos9ksmu(filename,prodname,imagecode,debug1)

	elif splitbydash[0] == "n6000":
		prodname = product(splitbydash[0])
		if splitbydot[0] == "n6000-uk9-kickstart":
			imagecode = imagelookup("kickstart")
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		elif splitbydot[0] == "n6000-uk9":
			imagecode = imagelookup("system")
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)

	elif splitbydash[0] == "n7000":
		prodname = product(splitbydash[0])
		if splitbydash[1] == "s1":
			imagecode = imagelookup("s1")
			nexus7ksliceandice (filename,prodname,imagecode,debug1)
		elif splitbydash[1] == "s2":
			imagecode = imagelookup("s2")
			nexus7ksliceandice (filename,prodname,imagecode,debug1)

	elif splitbydash[0] == "n7700":
		prodname = product(splitbydash[0])
		if splitbydash[1] == "s2":
			imagecode = imagelookup("s2")
			nexus7ksliceandice (filename,prodname,imagecode,debug1)
		elif splitbydash[1] == "s3":
			imagecode = imagelookup("s3")
			nexus7ksliceandice (filename,prodname,imagecode,debug1)

	elif filename.startswith("n3000"):
		prodname = product("n3000")
		if filename.startswith("n3000-uk9-kickstart."):
			imagecode = imagelookup("kickstart")
			workname = filename.replace(".bin","")
			workname = workname.replace("n3000-uk9-kickstart.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("n3000-compact"):
			imagecode = imagelookup("system")
			workname = filename.replace(".bin","")
			workname = workname.replace("n3000-compact.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("n3000_xsd."):
			imagecode = imagelookup("xsd")
			workname = filename.replace(".tar.gz","")
			workname = workname.replace("n3000_xsd.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		else:
			imagecode = imagelookup("system")
			workname = filename.replace(".bin","")
			workname = workname.replace("n3000-uk9.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("guestshell"):
		prodname = product("Nexus")
		imagecode = imagelookup("guestshell")
		workname = filename.replace(".ova","")
		workname = workname.replace("guestshell.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("oac"):
		prodname = product("Nexus")
		imagecode = imagelookup("oac")
		workname = filename.replace(".ova","")
		workname = workname.replace("oac.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif (
	filename.startswith("nxosv-final") or 
	filename.startswith("nxosv") or 
	filename.startswith("nexus9300v") or 
	filename.startswith("nexus9500v")
	):
		prodname = product("nxosv")
		imagecode = imagelookup("system")
		workname = filename.replace(".box","")
		workname = workname.replace(".ova","")
		workname = workname.replace(".qcow2","")
		workname = workname.replace(".vmdk","")
		workname = workname.replace("nxosv-final.","")
		workname = workname.replace("nxosv.","")
		workname = workname.replace("nexus9300v.","")
		workname = workname.replace("nexus9500v64.","")
		workname = workname.replace("nexus9500v.","")
		utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif (
	filename.startswith("n3500") or 
	filename.startswith("poap_script.6") or 
	filename.startswith("poap_script_n3k.")
	):
		prodname = product("n3500")
		if filename.startswith("n3500-uk9-kickstart."):
			imagecode = imagelookup("kickstart")
			workname = filename.replace(".bin","")
			workname = workname.replace("n3500-uk9-kickstart.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)
		elif (
		filename.startswith("poap_script.") or 
		filename.startswith("poap_script_n3k.")
		):
			imagecode = imagelookup("poap")
			workname = filename.replace(".py","")
			workname = workname.replace(".tcl","")
			workname = workname.replace("poap_script_n3k.","")
			workname = workname.replace("poap_script.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		else:
			imagecode = imagelookup("system")
			workname = filename.replace(".bin","")
			workname = workname.replace("n3500-uk9.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif splitbydash[0] == "n4000":
		prodname = product("n4000")
		workname = filename.replace(".bin","")
		workname = workname.replace("n4000-bk9-kickstart.","")
		workname = workname.replace("n4000-bk9.","")
		if filename.startswith("n4000-bk9-kickstart."):
			imagecode = imagelookup("kickstart")
		else:
			imagecode = imagelookup("system")
		utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif (
	filename.startswith("n5000") or 
	filename.startswith("poap_script")
	):
		prodname = product("n5000")
		if filename.startswith("n5000-uk9-kickstart."):
			imagecode = imagelookup("kickstart")
			workname = filename.replace(".bin","")
			workname = workname.replace("n5000-uk9-kickstart.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)
		elif (
		filename.startswith("n5000_poap_script.") or 
		filename.startswith("poap_script.")
		):
			imagecode = imagelookup("poap")
			workname = filename.replace(".py","")
			workname = workname.replace(".tcl","")
			workname = workname.replace("n5000_poap_script.","")
			workname = workname.replace("poap_script.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("n5000_xsd."):
			imagecode = imagelookup("xsd")
			workname = filename.replace(".tar.gz","")
			workname = workname.replace("n5000_xsd.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		else:
			imagecode = imagelookup("system")
			workname = filename.replace(".bin","")
			workname = workname.replace("n5000-uk9.","")
			utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname)

	elif (
	splitbydash[0] == "m9000" or 
	splitbydash[0] == "m9500"
	):
		prodname = product("m9500")
		if filename.startswith("m9000-pkg1.") and filename.endswith(".epld"):
			imagecode = imagelookup("epld")
			workname = filename.replace(".epld","")
			workname = workname.replace("m9000-pkg1.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-epld-") and filename.endswith(".img"):
			imagecode = imagelookup("epld")
			workname = filename.replace(".img","")
			workname = workname.replace("m9000-epld-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-ek9-ssi-mz.") and filename.endswith(".bin"):
			imagecode = imagelookup("ssi")
			workname = filename.replace(".bin","")
			workname = workname.replace("m9000-ek9-ssi-mz.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9500-sf1ek9-kickstart-mz."):
			imagecode = imagelookup("s1ek9")
			workname = filename.replace(".bin","")
			workname = workname.replace("m9500-sf1ek9-kickstart-mz.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9500-sf1ek9-mz."):
			imagecode = imagelookup("s1ek9")
			workname = filename.replace(".bin","")
			workname = workname.replace("m9500-sf1ek9-mz.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9500-sf2ek9-kickstart-mz."):
			imagecode = imagelookup("s2ek9")
			workname = filename.replace(".bin","")
			workname = workname.replace("m9500-sf2ek9-kickstart-mz.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9500-sf2ek9-mz."):
			imagecode = imagelookup("s2ek9")
			workname = filename.replace(".bin","")
			workname = workname.replace("m9500-sf2ek9-mz.","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-cd-npe-"):
			imagecode = imagelookup("fabman")
			workname = filename.replace(".zip","")
			workname = workname.replace("m9000-cd-npe-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-cd-"):
			imagecode = imagelookup("fabman")
			workname = filename.replace(".zip","")
			workname = workname.replace("m9000-cd-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-fm-update-"):
			imagecode = imagelookup("fabman")
			workname = filename.replace(".jar","")
			workname = workname.replace("m9000-fm-update-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-fm-"):
			imagecode = imagelookup("fabman")
			workname = filename.replace(".jar","")
			workname = workname.replace("m9000-fm-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)
		elif filename.startswith("m9000-sha-"):
			imagecode = imagelookup("fabman")
			workname = filename.replace(".npe.jar","")
			workname = workname.replace("m9000-sha-","")
			utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif splitbydash[0] == "m9100":
		prodname = product("m9100")
		workname = filename.replace(".bin","")
		workname = workname.replace("m9100-","")
		if workname.startswith("s1ek9-"):
			imagecode = imagelookup("s1ek9")
			workname = workname.replace("s1ek9-","")
		elif workname.startswith("s2ek9-"):
			imagecode = imagelookup("s2ek9")
			workname = workname.replace("s2ek9-","")
		elif workname.startswith("s3ek9-"):
			imagecode = imagelookup("s3ek9")
			workname = workname.replace("s3ek9-","")
		elif workname.startswith("s5ek9-"):
			imagecode = imagelookup("s5ek9")
			workname = workname.replace("s5ek9-","")
		else:
			messageunknowndev()
		workname = workname.replace("kickstart-mz.","")
		workname = workname.replace("kickstart-mz-npe.","")
		workname = workname.replace("mz.","")
		workname = workname.replace("mz-npe.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif splitbydash[0] == "m9200":
		prodname = product("m9200")
		workname = filename.replace(".bin","")
		workname = workname.replace("m9200-","")
		if workname.startswith("s1ek9-"):
			imagecode = imagelookup("s1ek9")
			workname = workname.replace("s1ek9-","")
		elif workname.startswith("s2ek9-"):
			imagecode = imagelookup("s2ek9")
			workname = workname.replace("s2ek9-","")
		elif workname.startswith("s3ek9-"):
			imagecode = imagelookup("s3ek9")
			workname = workname.replace("s3ek9-","")
		elif workname.startswith("s5ek9-"):
			imagecode = imagelookup("s5ek9")
			workname = workname.replace("s5ek9-","")
		else:
			messageunknowndev()
		workname = workname.replace("kickstart-mz.","")
		workname = workname.replace("kickstart-mz-npe.","")
		workname = workname.replace("mz.","")
		workname = workname.replace("mz-npe.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif splitbydash[0] == "m9250":
		prodname = product("m9250")
		workname = filename.replace(".bin","")
		workname = workname.replace("m9250-","")
		if workname.startswith("s5ek9-"):
			imagecode = imagelookup("s5ek9")
			workname = workname.replace("s5ek9-","")
		else:
			messageunknowndev()
		workname = workname.replace("kickstart-mz.","")
		workname = workname.replace("kickstart-mz-npe.","")
		workname = workname.replace("mz.","")
		workname = workname.replace("mz-npe.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	elif splitbydash[0] == "m9700":
		prodname = product("m9700")
		workname = filename.replace(".bin","")
		workname = workname.replace("m9700-","")
		if workname.startswith("s3ek9-"):
			imagecode = imagelookup("s3ek9")
			workname = workname.replace("s3ek9-","")
		elif workname.startswith("s4ek9-"):
			imagecode = imagelookup("s4ek9")
			workname = workname.replace("s4ek9-","")
		else:
			messageunknowndev()
		workname = workname.replace("kickstart-mz.","")
		workname = workname.replace("kickstart-mz-npe.","")
		workname = workname.replace("mz.","")
		workname = workname.replace("mz-npe.","")
		utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname)

	else:
		messageunknownfile()

def nexus7ksliceandice (filename,prodname,supcode,debug1):
	if debug1:
		print("\tSubroutine#\tnexus7ksliceandice")
	splitbydot = filename.split(".")
	if splitbydot[0] == "n7000-s1-kickstart-npe" or splitbydot[0] == "n7000-s2-kickstart-npe" or splitbydot[0] == "n7700-s2-kickstart-npe" or splitbydot[0] == "n7700-s3-kickstart-npe":
		prodname = prodname + "/" + supcode
		imagecode = imagelookup("kickstart-npe")
		if splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
	elif splitbydot[0] == "n7000-s1-kickstart" or splitbydot[0] == "n7000-s2-kickstart" or splitbydot[0] == "n7700-s2-kickstart" or splitbydot[0] == "n7700-s3-kickstart":
		prodname = prodname + "/" + supcode
		imagecode = imagelookup("kickstart")
		if splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
	elif splitbydot[0] == "n7000-s1-dk9-npe" or splitbydot[0] == "n7000-s2-dk9-npe" or splitbydot[0] == "n7700-s2-dk9-npe" or splitbydot[0] == "n7700-s3-dk9-npe":
		prodname = prodname + "/" + supcode
		imagecode = imagelookup("system-npe")
		if splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
	elif (
	splitbydot[0] == "n7000-s1-dk9" or 
	splitbydot[0] == "n7000-s2-dk9" or 
	splitbydot[0] == "n7700-s2-dk9" or 
	splitbydot[0] == "n7700-s3-dk9" or 
	splitbydot[0] == "n7000-s1-epld" or 
	splitbydot[0] == "n7000-s2-epld" or 
	splitbydot[0] == "n7700-s2-epld" or 
	splitbydot[0] == "n7700-s3-epld"
	):
		prodname = prodname + "/" + supcode
		if splitbydot[1] == "7":
			if splitbydot[6].startswith("CSC"):
				imagecode = imagelookup("smu")
				fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
			elif splitbydot[0].endswith("epld"):
				imagecode = imagelookup("epld")
				fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
			else:
				imagecode = imagelookup("system")
				fileprocnxosfivedigit (filename,prodname,imagecode,debug1)
		else:
			if splitbydot[4].startswith("CSC"):
				imagecode = imagelookup("smu")
				fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
			elif splitbydot[0].endswith("epld"):
				imagecode = imagelookup("epld")
				fileprocnxosthreedigit (filename,prodname,imagecode,debug1)
			else:
				imagecode = imagelookup("system")
				fileprocnxosthreedigit (filename,prodname,imagecode,debug1)

def utilssinglemove (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tnexussinglefile")
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def fileprocessornxosplatform7700v8 (filename):
	if debug1:
		print("\tSubroutine#\tfileprocessornxosplatform7700v8")
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")
	if filename.startswith == "n7700-s2-kickstart-npe":
		imagecode = "KICKSTART-NPE"
	elif filename.startswith == "n7700-s2-kickstart":
		imagecode = "KICKSTART"
	elif filename.startswith == "n7700-s2-dk9-npe":
		imagecode = "SYSTEM-NPE"
	elif filename.startswith == "n7700-s2-dk9":
		imagecode = "SYSTEM"
	if splitbydash[0] == "n7700":
		prodname = product (splitbydash[0])
		if splitbydash[1] == "s2":
			imagecode = "SUP-2"
		elif splitbydash[1] == "s3":
			imagecode = "SUP-3"
		iosmain = util2digit (splitbydot[1],splitbydot[2])
		iosfull = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = prodname + "/" + iosmain + "/" + iosfull + "/" + imagecode

def fileprocnxosthreedigit (filename,prodname,imagecode,debug1):
	if debug1:
		print("\tSubroutine#\tfileprocnxosthreedigit")
	splitbydot = filename.split(".")
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
	if imagecode == "FIRMWARE-EPLD":
		filepath = filepath4 (prodname,imagecode,nxosver,nxosfull)
	elif imagecode == "SMU":
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,splitbydot[4])
	else:
		filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)

def fileprocnxosfivedigit (filename,prodname,imagecode,debug1):
	if debug1:
		print("\tSubroutine#\tfileprocnxosfivedigit")
	splitbydot = filename.split(".")
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util5digit (splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
	if imagecode == "FIRMWARE-EPLD":
		filepath = filepath4 (prodname,imagecode,nxosver,nxosfull)
	elif imagecode == "SMU":
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,splitbydot[6])
	else:
		filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)

def fileprocnxos1000v (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfileprocnxos1000v")
	if (
	filename.startswith("Nexus1000v.5.2.1.SV") or 
	filename.startswith("Nexus1000v.4.2.1.SV") or 
	filename.startswith("nexus1000v.4.2.1.SV") or 
	filename.startswith("Nexus1000v.4.0.4.SV")
	):
		workname = filename.replace("-pkg.zip","")
		workname = workname.replace("zip","")
		splitbydot = workname.split(".")
		imagecode = imagelookup("vmware")
		nxosfull = util3digit (splitbydot[4],splitbydot[5],splitbydot[6])
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
	elif filename == "Nexus1000v-4.0.4.SV1.1.zip":
		imagecode = imagelookup("vmware")
		nxosfull = util2digit ("SV1","1")
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
	elif filename == "Nexus1000v-4.0.4.SV1.3.zip":
		imagecode = imagelookup("vmware")
		nxosfull = util2digit ("SV1","3")
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
	elif (
	filename.startswith("Nexus1000v.5.2.1.SK")
	):
		workname = filename.replace("-pkg.zip","")
		workname = workname.replace("zip","")
		splitbydot = workname.split(".")
		imagecode = imagelookup("kvm")
		nxosfull = util3digit (splitbydot[4],splitbydot[5],splitbydot[6])
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
	elif (
	filename.startswith("Nexus1000V.5.2.1.SM")
	):
		workname = filename.replace("-pkg.zip","")
		workname = workname.replace("zip","")
		splitbydot = workname.split(".")
		imagecode = imagelookup("hyperv")
		nxosfull = util3digit (splitbydot[4],splitbydot[5],splitbydot[6])
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
	elif filename == "Nexus1000V5.2.1.SM1.5.2.zip":
		imagecode = imagelookup("hyperv")
		nxosfull = util3digit ("SM1","5","2")
		filepath = filepath3 (prodname,imagecode,nxosfull)
		filemove (filepath, filename)
		

def fileprocessornxos9ksmu (filename,prodname,imagecode,debug1):
	if debug1:
		print("\tSubroutine#\tfileprocessornxos9ksmu")
	splitbydot = filename.split(".")
	csc = splitbydot[1].replace("-n9k_ALL-1","")
	csc = csc.replace("_EOR-n9k_EOR-1","")
	csc = csc.replace("_TOR-n9k_TOR-1","")
	csc = csc.replace("_eth-n9k_TOR-1","")
	csc = csc.replace("_eth-n9k_EOR-1","")
	csc = csc.replace("-n9k_EOR-1","")
	csc = csc.replace("-n9k_TOR-1","")
	csc = csc.replace("_modular_lc-1","")
	csc = csc.replace("_modular_sup-1","")
	csc = csc.replace("01-1","")
	csc = csc.replace("-1","")
	if splitbydot[3] == "0-9":
		digitone = "9"
	elif splitbydot[3] == "0-10":
		digitone = "10"
	elif splitbydot[3] == "0-8":
		digitone = "8"
	elif splitbydot[3] == "0-7" or splitbydot[3] == "1-7":
		digitone = "7"
	if digitone == "9" or digitone == "10":
		nxosver = util2digit (digitone,splitbydot[4])
		nxosfull = util3digit (digitone,splitbydot[4],splitbydot[5])
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,csc)
		filemove (filepath, filename)
	elif digitone == "7":
		nxosver = util2digit (digitone,splitbydot[4])
		nxosfull = util5digit (digitone,splitbydot[4],splitbydot[5],splitbydot[6],splitbydot[7])
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,csc)
		filemove (filepath, filename)
