from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_wireless(debug1,filename):
	if debug1:
		print("\tModule#\t\tios_wireless")
	if debug1:
		print("\tSubroutine#\tfileprocessor_wireless")

	if filename == "MFG_CTVM_LARGE_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.103.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","103","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.131.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","131","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.135.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","135","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.5.140.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","140","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.6.101.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","6")
		verfour = util4digit("8","6","101","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.7.106.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","7")
		verfour = util4digit("8","7","106","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.8.111.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","111","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_LARGE_8.8.120.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","120","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.3.143.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","3")
		verfour = util4digit("8","3","143","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.5.140.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","5")
		verfour = util4digit("8","5","140","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.8.111.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","111","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif filename == "MFG_CTVM_SMALL_8.8.120.0.iso":
		prodname = product ("CTVM")
		vertwo = util2digit("8","8")
		verfour = util4digit("8","8","120","0")
		filepath = filepath3(prodname,vertwo,verfour)
		filemove (filepath, filename)
	elif (
	filename.startswith("AIR_CTVM_LARGE-K9_") or 
	filename.startswith("AIR_CTVM-K9_") or 
	filename.startswith("MFG_CTVM_")
	):
		prodname = product ("CTVM")
		wireless_controller_virtual (debug1,filename,prodname)

def wireless_controller_virtual (debug1,filename,prodname):
	workname = filename.replace("AIR_CTVM_LARGE-K9_","")
	workname = filename.replace("AIR_CTVM_LARGE_","")
	workname = workname.replace("AIR_CTVM-K9_","")
	workname = workname.replace("MFG_CTVM_LARGE_","")
	workname = workname.replace("MFG_CTVM_","")
	workname = workname.replace(".ova","")
	workname = workname.replace(".iso","")
	workname = workname.replace(".aes","")
	splitbyuscore = workname.split("_")
	vertwo = util2digit(splitbyuscore[0],splitbyuscore[1])
	verfour = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
	filepath = filepath3(prodname,vertwo,verfour)
	filemove (filepath, filename)
