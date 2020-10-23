from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessorios (debug1,filename):
	if debug1:
		print("\tModule#\tios_ios")
	if debug1:
		print("\tSubroutine#\tfileprocessorios")
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")

	if (
	filename.startswith ("sprom") or 
	filename.startswith ("epld-sup2") or 
	filename.startswith ("epld-6548getx") or 
	filename.startswith ("6509neba") or 
	filename.startswith ("6516agbic") or 
	filename.startswith ("6548getx") or 
	filename.startswith ("66748getx")
	):
		prodname = product("c6500")
		imagecode = imagelookup("sprom")
		iossinglefile (filename,prodname,imagecode,debug1)

	elif (
	filename == "sconvertit0-11.tar" or 
	filename == "sconvertit0-12.tar" or 
	filename == "wconvertit0-11.zip" or 
	filename == "wconvertit0-12.zip"
	):
		prodname = product("c6500")
		imagecode = imagelookup("config-converter")
		iossinglefile (filename,prodname,imagecode,debug1)


def iossinglefile (filename,prodname,imagecode,debug1):
	if debug1:
		print("\tSubroutine#\tiossinglefile")
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)
