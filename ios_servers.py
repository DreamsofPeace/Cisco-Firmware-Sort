from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def file_proc_servers (filename):
	if filename.startswith("ucs"):
		file_proc_servers_ucs (filename)

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
	filename.startswith("ucs-cxxx-drivers") or 
	filename.startswith("ucs-bxxx-drivers")
	):
		file_proc_servers_ucs_drivers (filename)
	elif (
	filename.startswith("ucs-k9-bundle") or 
	filename.startswith("ucs-k9-bundle-b-series") or 
	filename.startswith("ucs-k9-bundle-c-series") or 
	filename.startswith("ucs-k9-bundle-infra") or 
	filename.startswith("ucs-k9-bundle-m-series") or 
	filename.startswith("ucs-mini-k9-bundle-infra")
	):
		file_proc_servers_ucs_bundle (filename)
	elif splitbydash[0] == "ucs" and splitbydash[2] == "huu":
		prodname = product(splitbydash[1])
		imagecode = imagelookup(splitbydash[2])
		file_proc_servers_p3_d3 (filename,prodname,imagecode)

def file_proc_servers_ucs_single (filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def file_proc_servers_ucs_bundle (filename):
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	prodname = product("ucsgeneric")
	imagecode = imagelookup("ucsbundle")
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def file_proc_servers_ucs_drivers (filename):
	splitbydash = filename.split("-",)
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	prodname = product("ucsgeneric")
	if filename == "ucs-drivers.1.0.2.iso":
		imagecode = imagelookup("driversucsb")
	elif filename.startswith("ucs-cxxx-drivers"):
		imagecode = imagelookup("driversucsc")
	elif filename.startswith("ucs-bxxx-drivers"):
		imagecode = imagelookup("driversucsb")
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def file_proc_servers_p3_d3 (filename,prodname,imagecode):
	splitbydash = filename.split("-", 3)
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)
