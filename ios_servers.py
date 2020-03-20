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
