from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_wireless(debug1,filename):
	if debug1:
		print("\tModule#\t\tios_wireless")
	if debug1:
		print("\tSubroutine#\tfileprocessor_wireless")

	if (
	filename.startswith("AIR_CTVM_LARGE-K9_") or 
	filename.startswith("AIR_CTVM-K9_")
	):
		prodname = product ("CTVM")
		wireless_controller_virtual (debug1,filename,prodname)

def wireless_controller_virtual (debug1,filename,prodname):
	workname = filename.replace("AIR_CTVM_LARGE-K9_","")
	workname = workname.replace("AIR_CTVM-K9_","")
	workname = workname.replace(".ova","")
	workname = workname.replace(".aes","")
	splitbyuscore = workname.split("_")
	vertwo = util2digit(splitbyuscore[0],splitbyuscore[1])
	verfour = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)
