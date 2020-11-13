from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def file_proc_servers (filename,debug1):
	if debug1:
		print("\tModule#\t\tios_servers")
	if debug1:
		print("\tSubroutine#\tfile_proc_servers")
	if (
	filename == "B57BCMCD_v15.2.4.1.tgz" or 
	filename == "B57CiscoCD_T6.4.4.3-57712.zip" or 
	filename == "Intel_Windows_drv_MR_6.714.18.00_pv.zip" or 
	filename == "LSI_x64_Signed_Driver_5.2.116.64.zip" or 
	filename == "MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip" or 
	filename == "intel9.2.3.1023.tar" or 
	filename == "rste_4.5.0.1335_install.zip"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("driverseseries")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("DNAC") or filename.startswith("dnac"):
		prodname = product ("dnac")
		utilssingleprodname (debug1,filename,prodname)

	elif filename.startswith("ucs-catalog"):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("catalog")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("pid-ctlg"):
		prodname = product("c2xxm3")
		imagecode = imagelookup("catalog")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("delnorte2"):
		prodname = product("c2xxm3")
		imagecode = imagelookup("catalog")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename.startswith("plumas2"):
		prodname = product("c2xxm5")
		imagecode = imagelookup("catalog")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("Collector") or 
	filename.startswith ("collector") or 
	filename == "JeOS_Patch_To_Enable_ASD.zip"
	):
		prodname = product("cspc")
		utilssingleprodname (debug1,filename,prodname)

	elif (
	filename == "efi-obd-v12-07-18.diag" or 
	filename == "efi-obd-v13-10-15.diag" or 
	filename == "efi-obd-v13-7-3.diag"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("hdiag")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "huu-2.3.1.iso" or 
	filename == "huu-2.3.2.iso" or 
	filename == "huu-2.3.3.iso" or 
	filename == "huu-2.4.1.iso" or 
	filename == "huu-3.0.1.iso" or 
	filename == "huu-3.1.1.iso" or 
	filename == "huu_3.1.2.iso" or 
	filename == "huu_3.1.3.iso" or 
	filename == "huu_3.1.4.iso" or 
	filename == "huu_3.2.6.v3.iso" or 
	filename == "ucse-huu-2.1.1.iso" or 
	filename == "ucs-e100-huu-2.2.1.iso"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("huu")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "DW_16MB_release_1029.bin" or 
	filename == "DW_BIOS.bin.SPA" or 
	filename == "DW_Signed_Bios_Image.bin.SPA" or 
	filename == "1X0DBIOSv4.8" or 
	filename == "1X0SBIOSv4.8" or 
	filename == "Signed_EN_BIOS_1.5.0.4.bin.SPA" or 
	filename == "CIMC-3.2.8.bin" or 
	filename == "CIMC_2.4.1.bin" or 
	filename == "CIMC_2.4.2.bin" or 
	filename == "CIMC_3.0.1.bin" or 
	filename == "CIMC_3.0.2.bin" or 
	filename == "CIMC_3.1.1.bin" or 
	filename == "CIMC_3.1.2.bin" or 
	filename == "CIMC_3.1.3.bin" or 
	filename == "CIMC_3.1.4.bin" or 
	filename == "CIMC_3.2.1.REL.bin" or 
	filename == "CIMC_3.2.2.bin" or 
	filename == "CIMC_3.2.3.bin" or 
	filename == "CIMC_3.2.4.bin" or 
	filename == "CIMC_3.2.6.bin" or 
	filename == "CIMC_3.2.7.bin" or 
	filename == "Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA" or 
	filename == "Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA" or 
	filename == "Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA" or 
	filename == "Signed_DW_M1M2_Bios_Image_041015.bin.SPA" or 
	filename == "Signed_EN_BIOS_1.5.0.5.bin.SPA" or 
	filename == "Signed_EN_BIOS_1.5.0.6.bin.SPA" or 
	filename == "Signed_SW_M2_BIOS_1.5.0.6.bin.SPA" or 
	filename == "Signed_SW_M2_BIOS_1.5.0.7.bin.SPA" or 
	filename == "Signed_SW_M2_BIOS_1.5.0.8.bin.SPA" or 
	filename == "Signed_SW_M2_Bios_1.5.0.5.bin.SPA" or 
	filename == "UCSEDM3_BIOS_2.4.SPA" or 
	filename == "UCSEDM3_BIOS_2.5.SPA" or 
	filename == "UCSEDM3_BIOS_2.6.SPA" or 
	filename == "UCSE_CIMC_2.3.1.bin" or 
	filename == "UCSE_CIMC_2.3.2.bin" or 
	filename == "UCSE_CIMC_2.3.3.bin" or 
	filename == "UCSE_CIMC_2.3.5.bin" or 
	filename == "update_pkg-Mar-22-MR-rebuild.bin" or 
	filename == "update_pkg-ucse.combined.120808.bin" or 
	filename == "update_pkg-ucse.combined.REL.2.2.2.bin" or 
	filename == "update_pkg-ucse.combined.REL.2.2.1.bin" or 
	filename == "update_pkg-ucse.combined.REL.bin" or 
	filename == "SW_16MB_release_1102.bin" or 
	filename == "SW_Signed_Bios_Image.bin.SPA"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("firmwareeseries")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "UCS_docs_20110510.iso"
	):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("docs")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ucs") or 
	filename == "b2xx-m1-drivers-1.1.1j.iso" or 
	filename == "c2xx-m1-utils-1.0.2.iso"
	):
		file_proc_servers_ucs (debug1,filename)

	elif (
	filename.startswith("PI")
	):
		file_proc_servers_primeinfra (debug1,filename)

	elif (
	filename.startswith ("Cisco_ACI") or 
	filename.startswith ("acisim") or 
	filename.startswith ("aci-simulator") or 
	filename.startswith ("aci-apic") or 
	filename.startswith ("aci-msft-pkg") or 
	filename.startswith ("aci-n9000-dk9") or 
	filename.startswith ("apic-vrealize") or 
	filename.startswith ("esx-msc") or 
	filename.startswith ("msc") or 
	filename.startswith ("vcenter-plugin") or 
	filename.startswith ("tools-msc")
	):
		prodname = product("aci")
		file_proc_servers_aci(debug1,filename,prodname)

	elif (
	filename.startswith ("storfs-packages") or 
	filename.startswith ("HX-ESXi") or 
	filename.startswith ("HX-Kubernetes") or 
	filename.startswith ("Cisco-HX-Data-Platform-Installer") or
	filename.startswith ("HyperFlex-VC-HTML") or 
	filename.startswith ("hxcsi") or 
	filename.startswith ("HyperFlex-Witness-") or 
	filename.startswith ("HxClone-HyperV")
	):
		prodname = product("hyperflex")
		file_proc_servers_hyperflex(debug1,filename,prodname)

	elif (
	filename.startswith ("DCNM") or 
	filename.startswith ("dcnm")
	):
		prodname = product("dcnm")
		file_proc_servers_dcnm(debug1,filename,prodname)
	elif filename == "readme_10.2.1.ST.1":
		prodname = product("dcnm")
		filepath = filepath3(prodname,"10.2","10.2.1")
		filemove (filepath, filename)
	else:
		messageunknownfile()

def file_proc_servers_dcnm (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_dcnm")
	splitbydot = filename.split(".")
	vertwo = util2digit (splitbydot[1],splitbydot[2])
	verthree = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
	if filename.startswith ("dcnm-installer-x64-windows"):
		imagecode = imagelookup("installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-installer-windows"):
		imagecode = imagelookup("installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-installer-x64-linux"):
		imagecode = imagelookup("installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-installer-linux"):
		imagecode = imagelookup("installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-installer-solaris"):
		imagecode = imagelookup("installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("DCNMUpgradeTool"):
		imagecode = imagelookup("upgrade")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif (
	filename.startswith ("dcnm-va-templates") or 
	filename.startswith ("dcnm_fabricpath_fabric_templates") or 
	filename.startswith ("dcnm_deprecated_templates") or 
	filename.startswith ("dcnm_ip_vxlan_fabric_templates")
	):
		imagecode = imagelookup("templates")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-va"):
		imagecode = imagelookup("va")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-se"):
		imagecode = imagelookup("installer-ase")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-se"):
		imagecode = imagelookup("installer-ase")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-silent-installer-properties"):
		imagecode = imagelookup("silent-installer")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-san-client"):
		imagecode = imagelookup("san-client")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-device-pack"):
		imagecode = imagelookup("device-pack")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("dcnm-va-ovf-kvm-files"):
		imagecode = imagelookup("virtual-ovf")
		filepath = filepath4(prodname,vertwo,verthree,imagecode)
		filemove (filepath, filename)


def file_proc_servers_hyperflex (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_hyperflex")
	if filename.startswith ("storfs-packages"):
		workname = filename.replace("storfs-packages-", "")
		workname = workname.replace(".tgz", "")
		splitbydot = workname.split(".")
		vertwo = util2digit (splitbydot[0],splitbydot[1])
		verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
		imagecode = imagelookup("upgrade")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)
	elif filename.startswith ("HX-ESXi"):
		workname = filename.replace("HX-ESXi-", "")
		splitbydash = workname.split("-")
		imagecode = imagelookup("vmware")
		filepath = filepath3(prodname,imagecode,splitbydash[0])
		filemove (filepath, filename)
	elif filename.startswith ("HX-Kubernetes"):
		workname = filename.replace("HX-Kubernetes-", "")
		splitbydot = workname.split(".")
		vertwo = util2digit (splitbydot[0],splitbydot[1])
		verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
		imagecode = imagelookup("kubernetes")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)
	elif filename.startswith ("Cisco-HX-Data-Platform-Installer"):
		workname = filename.replace("Cisco-HX-Data-Platform-Installer-v", "")
		workname = workname.replace("p1-esx.ova", "")
		workname = workname.replace("-esx.ova", "")
		workname = workname.replace("-hyperv.vhdx.zip", "")
		splitbydot = workname.split(".")
		vertwo = util2digit (splitbydot[0],splitbydot[1])
		verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
		imagecode = imagelookup("install")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)
	elif filename.startswith ("HyperFlex-VC-HTML"):
		imagecode = imagelookup("vchtmlplug")
		filepath = filepath2(prodname,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("hxcsi"):
		imagecode = imagelookup("kubernetes")
		filepath = filepath2(prodname,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("HyperFlex-Witness-"):
		imagecode = imagelookup("witness")
		filepath = filepath2(prodname,imagecode)
		filemove (filepath, filename)
	elif filename.startswith ("HxClone-HyperV"):
		workname = filename.replace("HxClone-HyperV-v", "")
		workname = workname.replace(".ps1", "")
		splitbydot = workname.split(".")
		vertwo = util2digit (splitbydot[0],splitbydot[1])
		verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
		imagecode = imagelookup("install")
		filepath = filepath4(prodname,imagecode,vertwo,verthree)
		filemove (filepath, filename)


def file_proc_servers_aci (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_aci")
	if (
	filename.startswith("tools-msc-") or 
	filename.startswith("esx-msc-") or 
	filename.startswith("msc-")
	):
		imagecode = imagelookup("mso")
		workname = filename.replace("tools-msc-", "")
		workname = workname.replace("esx-msc-", "")
		workname = workname.replace("msc-", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("Cisco_ACI_Virtual_Edge_")
	):
		imagecode = imagelookup("acive")
		workname = filename.replace("Cisco_ACI_Virtual_Edge_", "")
		workname = workname.replace("-pkg.zip", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("aci-apic-dk9.")
	):
		imagecode = imagelookup("apic")
		workname = filename.replace("aci-apic-dk9.", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("aci-msft-pkg-")
	):
		imagecode = imagelookup("aciplgms")
		workname = filename.replace("aci-msft-pkg-", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("vcenter-plugin-")
	):
		imagecode = imagelookup("aciplgvc")
		workname = filename.replace("vcenter-plugin-", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("apic-vrealize-")
	):
		imagecode = imagelookup("aciplgvs")
		workname = filename.replace("apic-vrealize-", "")
		if debug1:
			print ("\t\tWorkname#\t", end="")
			print (workname, end="\n")
		splitbydot = workname.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		if debug1:
			print ("\t\tFilepath#\t", end="")
			print (filepath, end="\n")
		filemove (filepath, filename)
	elif (
	filename.startswith("aci-n9000-dk9.")
	):
		imagecode = imagelookup("n9kacim")
		workname = filename.replace("aci-n9000-dk9.", "")
		splitbydot = filename.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("acisim-")
	):
		imagecode = imagelookup("acisim")
		workname = filename.replace("acisim-", "")
		workname = workname.replace("_part1.ova", "")
		workname = workname.replace("_part2.ova", "")
		workname = workname.replace("_part3.ova", "")
		workname = workname.replace("_part4.ova", "")
		workname = workname.replace("-",".")
		splitbydot = workname.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)
	elif (
	filename.startswith("aci-simulator-dk9.")
	):
		imagecode = imagelookup("acisim")
		workname = filename.replace("aci-simulator-dk9.", "")
		splitbydot = workname.split(".")
		ver2 = util2digit(splitbydot[0],splitbydot[1])
		ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4(prodname,imagecode,ver2,ver3)
		filemove (filepath, filename)

	else:
		messageunknownfile()

def file_proc_servers_primeinfra (debug1,filename):
	splitbydash = filename.split("-")
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_primeinfra")

def file_proc_servers_ucs (debug1,filename):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_ucs")
	splitbydash = filename.split("-")

	if filename.startswith("ucs-utils"):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("utils")

	elif (
	filename.startswith("ucs-drivers") or 
	filename.startswith("ucs-b2xx-drivers") or 
	filename.startswith("ucs-bxxx-drivers") or 
	filename.startswith("ucs-c2xx-drivers") or 
	filename.startswith("ucs-cxxx-drivers") or 
	filename.startswith("ucs-cxxx-fw") or 
	filename == "b2xx-m1-drivers-1.1.1j.iso"
	):
		if filename == "ucs-drivers.1.0.2.iso":
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)
		elif filename == "b2xx-m1-drivers-1.1.1j.iso":
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsc")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)
		elif filename.startswith("ucs-cxxx-drivers") or filename.startswith("ucs-c2xx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsc")
			file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)
		elif filename.startswith("ucs-cxxx-fw"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsc")
			file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)
		elif filename.startswith("ucs-bxxx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)
		elif filename.startswith("ucs-b2xx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ucs_k9_bundle") or 
	filename.startswith("ucs-k9-bundle") or 
	filename.startswith("ucs-k9-bundle-b-series") or 
	filename.startswith("ucs-k9-bundle-c-series") or 
	filename.startswith("ucs-k9-bundle-infra") or 
	filename.startswith("ucs-k9-bundle-m-series") or 
	filename.startswith("ucs-mini-k9-bundle-infra") or 
	filename.startswith("ucs-6300-k9-bundle-infra") or 
	filename.startswith("ucs-6400-k9-bundle-infra")
	):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("ucsbundle")
		file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("ucs-b2xx-utils") or 
	filename.startswith("ucs-bxxx-utils") or 
	filename.startswith("ucs-c2xx-utils") or 
	filename.startswith("ucs-cxxx-utils") or 
	filename == "c2xx-m1-utils-1.0.2.iso"
	):
		if (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-vmware.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("vmware")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename == "c2xx-m1-utils-1.0.2.iso"
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			utilssinglemove (debug1,filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-windows.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("windows")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-linux.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("ucslinux")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-vmware.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("vmware")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-windows.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("windows")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-linux.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("ucslinux")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-efi.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("efi")
			file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2)

		elif (
		filename.startswith("ucs-bxxx-utils-vmware") or 
		filename.startswith("ucs-b2xx-utils-vmware")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("vmware")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-cxxx-utils-vmware") or 
		filename.startswith("ucs-c2xx-utils-vmware")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("vmware")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-bxxx-utils-windows") or 
		filename.startswith("ucs-b2xx-utils-windows")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("windows")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-cxxx-utils-windows") or 
		filename.startswith("ucs-c2xx-utils-windows")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("windows")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-bxxx-utils-linux") or 
		filename.startswith("ucs-b2xx-utils-linux")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbseries")
			imagecode2 = imagelookup("ucslinux")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-cxxx-utils-linux") or 
		filename.startswith("ucs-c2xx-utils-linux")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("ucslinux")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)
		elif (
		filename.startswith("ucs-cxxx-utils-efi") or 
		filename.startswith("ucs-c2xx-utils-efi")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscseries")
			imagecode2 = imagelookup("efi")
			file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2)


	elif splitbydash[0] == "ucs" and splitbydash[2] == "huu":
		prodname = product(splitbydash[1])
		imagecode = imagelookup(splitbydash[2])
		file_proc_servers_p3_d3 (debug1,filename,prodname,imagecode)

def file_proc_servers_p2_d3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_p2_d3")
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def file_proc_servers_p2_d3_utils (debug1,filename,prodname,imagecode,imagecode2):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_p2_d3_utils")
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath5(prodname,imagecode,ver2,ver3,imagecode2)
	filemove (filepath, filename)

def file_proc_servers_p3_d3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_p3_d3")
	splitbydash = filename.split("-", 3)
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def file_proc_servers_p3_d3_utils (debug1,filename,prodname,imagecode,imagecode2):
	if debug1:
		print("\tSubroutine#\tfile_proc_servers_p3_d3_utils")
	splitbydash = filename.split("-", 3)
	splitbydot = splitbydash[3].split(".")
	workname = splitbydot[2].replace("-vmware.iso", "")
	workname = workname.replace("-efi.iso", "")
	workname = workname.replace("-linux.iso", "")
	workname = workname.replace("-windows.iso", "")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],workname)
	filepath = filepath5(prodname,imagecode,ver2,ver3,imagecode2)
	filemove (filepath, filename)
