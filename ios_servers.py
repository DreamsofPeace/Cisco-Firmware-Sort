from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def file_proc_servers (filename):
	if filename.startswith("ucs"):
		file_proc_servers_ucs (filename)
	else:
		messageunknownfile()

def file_proc_servers_ucs (filename):
	splitbydash = filename.split("-")

	if filename.startswith("ucs-catalog"):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("catalog")
		file_proc_servers_ucs_single (filename,prodname,imagecode)

	elif (
	name == "B57BCMCD_v15.2.4.1.tgz" or 
	name == "B57CiscoCD_T6.4.4.3-57712.zip" or 
	name == "Intel_Windows_drv_MR_6.714.18.00_pv.zip" or 
	name == "LSI_x64_Signed_Driver_5.2.116.64.zip" or 
	name == "MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip" or 
	name == "intel9.2.3.1023.tar" or 
	name == "rste_4.5.0.1335_install.zip" or 
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("driverseseries")
		file_proc_servers_ucs_single (filename,prodname,imagecode)

	elif (
	name == "efi-obd-v12-07-18.diag" or 
	name == "efi-obd-v13-10-15.diag" or 
	name == "efi-obd-v13-7-3.diag"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("hdiag")
		file_proc_servers_ucs_single (filename,prodname,imagecode)

	elif (
	name == "huu-2.3.1.iso" or 
	name == "huu-2.3.2.iso" or 
	name == "huu-2.3.3.iso" or 
	name == "huu-2.4.1.iso" or 
	name == "huu-3.0.1.iso" or 
	name == "huu-3.1.1.iso" or 
	name == "huu_3.1.2.iso" or 
	name == "huu_3.1.3.iso" or 
	name == "huu_3.1.4.iso" or 
	name == "huu_3.2.6.v3.iso" or 
	name == "ucse-huu-2.1.1.iso"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("huu")
		file_proc_servers_ucs_single (filename,prodname,imagecode)

	elif (
	name == "DW_16MB_release_1029.bin" or 
	name == "DW_BIOS.bin.SPA" or 
	name == "DW_Signed_Bios_Image.bin.SPA" or 
	name == "1X0DBIOSv4.8" or 
	name == "Signed_EN_BIOS_1.5.0.4.bin.SPA" or 
	name == "CIMC-3.2.8.bin" or 
	name == "CIMC_2.4.1.bin" or 
	name == "CIMC_2.4.2.bin" or 
	name == "CIMC_3.0.1.bin" or 
	name == "CIMC_3.0.2.bin" or 
	name == "CIMC_3.1.1.bin" or 
	name == "CIMC_3.1.2.bin" or 
	name == "CIMC_3.1.3.bin" or 
	name == "CIMC_3.1.4.bin" or 
	name == "CIMC_3.2.1.REL.bin" or 
	name == "CIMC_3.2.2.bin" or 
	name == "CIMC_3.2.3.bin" or 
	name == "CIMC_3.2.4.bin" or 
	name == "CIMC_3.2.6.bin" or 
	name == "CIMC_3.2.7.bin" or 
	name == "Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA" or 
	name == "Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA" or 
	name == "Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA" or 
	name == "Signed_DW_M1M2_Bios_Image_041015.bin.SPA" or 
	name == "Signed_EN_BIOS_1.5.0.5.bin.SPA" or 
	name == "Signed_EN_BIOS_1.5.0.6.bin.SPA" or 
	name == "Signed_SW_M2_BIOS_1.5.0.6.bin.SPA" or 
	name == "Signed_SW_M2_BIOS_1.5.0.7.bin.SPA" or 
	name == "Signed_SW_M2_BIOS_1.5.0.8.bin.SPA" or 
	name == "Signed_SW_M2_Bios_1.5.0.5.bin.SPA" or 
	name == "UCSEDM3_BIOS_2.4.SPA" or 
	name == "UCSEDM3_BIOS_2.5.SPA" or 
	name == "UCSEDM3_BIOS_2.6.SPA" or 
	name == "UCSE_CIMC_2.3.1.bin" or 
	name == "UCSE_CIMC_2.3.2.bin" or 
	name == "UCSE_CIMC_2.3.3.bin" or 
	name == "UCSE_CIMC_2.3.5.bin" or 
	name == "update_pkg-Mar-22-MR-rebuild.bin" or 
	name == "update_pkg-ucse.combined.120808.bin" or 
	name == "update_pkg-ucse.combined.REL.2.2.2.bin" or 
	name == "update_pkg-ucse.combined.REL.bin"
	):
		prodname = product("ucseseries")
		imagecode = imagelookup("firmwareeseries")
		file_proc_servers_ucs_single (filename,prodname,imagecode)


	elif filename.startswith("ucs-utils"):
		prodname = product("ucsgeneric")
		imagecode = imagelookup("utils")

	elif (
	filename.startswith("ucs-drivers") or 
	filename.startswith("ucs-b2xx-drivers") or 
	filename.startswith("ucs-bxxx-drivers") or 
	filename.startswith("ucs-c2xx-drivers") or 
	filename.startswith("ucs-cxxx-drivers") or 
	filename.startswith("ucs-cxxx-fw")
	):
		if filename == "ucs-drivers.1.0.2.iso":
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif filename.startswith("ucs-cxxx-drivers") or filename.startswith("ucs-c2xx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsc")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif filename.startswith("ucs-cxxx-fw"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsc")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif filename.startswith("ucs-bxxx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif filename.startswith("ucs-b2xx-drivers"):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("driversucsb")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)

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
		file_proc_servers_p2_d3 (filename,prodname,imagecode)

	elif (
	filename.startswith("ucs-b2xx-utils") or 
	filename.startswith("ucs-bxxx-utils") or 
	filename.startswith("ucs-c2xx-utils") or 
	filename.startswith("ucs-cxxx-utils")
	):
		if (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-vmware.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbvmware")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-windows.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbwindows")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-b2xx-utils-") and filename.endswith("-linux.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsblinux")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-vmware.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscvmware")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-windows.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscwindows")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-linux.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilclinux")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-c2xx-utils-") and filename.endswith("-efi.iso")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilcefi")
			file_proc_servers_p3_d3 (filename,prodname,imagecode)

		elif (
		filename.startswith("ucs-bxxx-utils-vmware") or 
		filename.startswith("ucs-b2xx-utils-vmware")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbvmware")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-cxxx-utils-vmware") or 
		filename.startswith("ucs-c2xx-utils-vmware")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscvmware")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-bxxx-utils-windows") or 
		filename.startswith("ucs-b2xx-utils-windows")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsbwindows")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-cxxx-utils-windows") or 
		filename.startswith("ucs-c2xx-utils-windows")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscwindows")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-bxxx-utils-linux") or 
		filename.startswith("ucs-b2xx-utils-linux")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsblinux")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-cxxx-utils-linux") or 
		filename.startswith("ucs-c2xx-utils-linux")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilsclinux")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)
		elif (
		filename.startswith("ucs-cxxx-utils-efi") or 
		filename.startswith("ucs-c2xx-utils-efi")
		):
			prodname = product("ucsgeneric")
			imagecode = imagelookup("utilscefi")
			file_proc_servers_p2_d3 (filename,prodname,imagecode)


	elif splitbydash[0] == "ucs" and splitbydash[2] == "huu":
		prodname = product(splitbydash[1])
		imagecode = imagelookup(splitbydash[2])
		file_proc_servers_p3_d3 (filename,prodname,imagecode)

def file_proc_servers_ucs_single (filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def file_proc_servers_p2_d3 (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def file_proc_servers_p3_d3 (filename,prodname,imagecode):
	splitbydash = filename.split("-", 3)
	splitbydot = splitbydash[3].split(".")
	splitbydot[2] = splitbydot[2].replace("-vmware.iso", "")
	splitbydot[2] = splitbydot[2].replace("-efi.iso", "")
	splitbydot[2] = splitbydot[2].replace("-linux.iso", "")
	splitbydot[2] = splitbydot[2].replace("-windows.iso", "")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)
