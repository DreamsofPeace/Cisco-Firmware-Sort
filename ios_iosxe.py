from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_iosxe(filename):
	splitbydot = filename.split(".")
	splitbydash = filename.split("-")
	if filename == "cat9k_iosxe.16.00.00fpgautility.SPA.bin":
		prodname = product ("cat9k")
		fileproc_iosxe (filename,prodname,"Hardware")

	elif filename.startswith("cat9k_iosxe") or filename.startswith("cat9k_lite"):
		if filename.startswith("cat9k_iosxe"):
			prodname = product ("cat9k")
		elif filename.startswith("cat9k_lite"):
			prodname = product ("cat9k_lite")
		if prodname == "UNKNOWN":
			messageunknownfile ()
		else:
			if filename.endswith("smu.bin"):
				imagecode = imagelookup("smu")
				fileproc_iosxe (filename,prodname,imagecode)
			else:
				imagecode = imagelookup(splitbydot[0])
				fileproc_iosxe (filename,prodname,imagecode)

	elif filename.startswith("cat3k_caa"):
		prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if splitbydot[2] == "03":
			fileproc_iosxe_3 (filename,prodname,imagecode)
		else:
			fileproc_iosxe(filename,prodname,imagecode)

	elif (
	splitbydot[0] == "C9800-40-universalk9_wlc" or 
	splitbydot[0] == "C9800-80-universalk9_wlc" or 
	splitbydot[0] == "C9800-CL-universalk9" or 
	splitbydot[0] == "C9800-L-universalk9_wlc" or 
	splitbydot[0] == "C9800-SW-iosxe-wlc"
	):
		fileproccontroller (filename)

	else:
		prodname = product (splitbydash[0])
		mdash = splitbydot[0].split("-")
		imagecode = imagelookup(mdash[1])
		if prodname == "UNKNOWN":
			messageunknowndev()
		elif imagecode == "UNKNOWN":
			messageunknownfeat()
		else:
			fileproc_iosxe(filename,prodname,imagecode)

def fileproccontroller (filename):
	if filename.startswith("C9800-40-universalk9_wlc"):
		prodname = product ("C9800-40")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-80-universalk9_wlc"):
		prodname = product ("C9800-80")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-CL-universalk9"):
		prodname = product ("C9800-CL")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-L-universalk9_wlc"):
		prodname = product ("C9800-L")
		fileproc_iosxe_noimagecode (filename,prodname)
	elif filename.startswith("C9800-SW-iosxe-wlc"):
		prodname = product ("C9800-SW")
		fileproc_iosxe_noimagecode (filename,prodname)

def fileproc_iosxe_noimagecode (filename,prodname):
	splitbydot = filename.split(".")
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath3(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath3(prodname,iosmain,iosfull)
		filemove (filepath, filename)

def fileproc_iosxe_3 (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[2],splitbydot[3])
		iosfull = util3digit(splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)

def fileproc_iosxe (filename,prodname,imagecode):
	splitbydot = filename.split(".")
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,"SMU",iosfull,splitbydot[4])
		filemove (filepath, filename)
	elif imagecode == "Hardware":
		filepath = filepath2 (prodname,imagecode)
		filemove (filepath, filename)
	else:
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)
