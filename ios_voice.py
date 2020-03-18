from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def fileprocessorvoice(filename):
	if filename.startswith("cmterm"):
		fileprocphone(filename)

def fileprocphone(filename):
	if filename.startswith("cmterm-3905"):
		prodname = product ("ipp3905")
		fileprocphone3digit(filename,prodname)

	elif filename.startswith("cmterm-7911_7906-sccp"):
		prodname = product ("ipp7911_7906")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7911_7906-sip"):
		prodname = product ("ipp7911_7906")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7914-sccp"):
		prodname = product ("ipp7914")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7914-sip"):
		prodname = product ("ipp7914")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7915"):
		prodname = product ("ipp7915")
		fileprocphone3digit(filename,prodname)

	elif filename.startswith("cmterm-7916"):
		prodname = product ("ipp7916")
		fileprocphone3digit(filename,prodname)

	elif filename.startswith("cmterm-7921-sccp"):
		prodname = product ("ipp7921")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7921-sip"):
		prodname = product ("ipp7921")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7931-sccp"):
		prodname = product ("ipp7931")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7931-sip"):
		prodname = product ("ipp7931")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7940_7960-sccp"):
		prodname = product ("ipp7940_7960")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7940_7960-sip"):
		prodname = product ("ipp7940_7960")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7940-7960"):
		prodname = product ("ipp7940_7960")
		fileprocphone3digittwo(filename,prodname)

	elif filename.startswith("cmterm-7941_7961-sccp"):
		prodname = product ("ipp7941_7961")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7941_7961-sip"):
		prodname = product ("ipp7941_7961")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7942_7962-sccp"):
		prodname = product ("ipp7942_7962")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7942_7962-sip"):
		prodname = product ("ipp7942_7962")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7945_7965-sccp"):
		prodname = product ("ipp7945_7965")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7945_7965-sip"):
		prodname = product ("ipp7945_7965")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7970_7971-sccp"):
		prodname = product ("ipp7970_7971")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7970_7971-sip"):
		prodname = product ("ipp7970_7971")
		fileprocphone3digitsip(filename,prodname)

	elif filename.startswith("cmterm-7975-sccp"):
		prodname = product ("ipp7975")
		fileprocphone3digitsccp(filename,prodname)

	elif filename.startswith("cmterm-7975-sip"):
		prodname = product ("ipp7975")
		fileprocphone3digitsip(filename,prodname)



def fileprocphone3digit(filename,prodname):
	splitbydot = filename.split(".")
	splitbydash = splitbydot[1].split("-")
	ver2 = util2digit(splitbydash[0],splitbydash[1])
	ver3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	filepath = filepath3(prodname,ver2,ver3)
	filemove (filepath, filename)

def fileprocphone3digittwo(filename,prodname):
	splitbydash = filename.split("-")
#	if splitbydash[4] == "sip.cop":
#		fileprocphone3digitsip(filename,prodname)
#	elif splitbydash[4] == "-sccp.cop":
#		fileprocphone3digitsccp(filename,prodname)

def fileprocphone3digitsip(filename,prodname):
	imagecode = imagelookup("sip")
	splitbydot = filename.split(".")
	splitbydash = splitbydot[1].split("-")
	ver2 = util2digit(splitbydash[0],splitbydash[1])
	ver3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	filepath = filepath4(prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def fileprocphone3digitsccp(filename,prodname):
	imagecode = imagelookup("sccp")
	splitbydot = filename.split(".")
	splitbydash = splitbydot[1].split("-")
	ver2 = util2digit(splitbydash[0],splitbydash[1])
	ver3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	filepath = filepath4(prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)
