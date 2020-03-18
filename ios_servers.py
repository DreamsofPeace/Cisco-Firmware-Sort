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
		prodname = product("ucs")
		imagecode = imagelookup("catalog")
		file_proc_servers_ucs_single (filename,prodname,imagecode)
	if splitbydash[0] == "ucs" and splitbydash[2] == "huu":
		prodname = product(splitbydash[1])
		imagecode = imagelookup(splitbydash[2])
		file_proc_servers_ucs_p3 (filename,prodname,imagecode)

def file_proc_servers_ucs_single (filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def file_proc_servers_ucs_p3 (filename,prodname,imagecode):
	splitbydash = filename.split("-", 3)
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)
