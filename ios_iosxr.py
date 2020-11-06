from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_iosxr (debug1,filename):
	if debug1:
		print("\tModule#\tios_security")
	if debug1:
		print("\tSubroutine#\tfileprocessorsecurity")

	if (
	filename.startswith("ASR9K") or 
	filename.startswith("asr9k")
	):
		iosxr_asr9k (debug1,filename)

	else:
#		if prodname == "UNKNOWN":
#			messageunknowndev()
#		elif imagecode == "UNKNOWN":
#			messageunknownfeat()
		messageunknowndev()

def iosxr_asr9k (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9k")
	prodname = product ("asr9k")
	if filename.startswith("ASR9K-iosxr-px") and filename.endswith("turboboot.tar"):
		imagecode = imagelookup("turboboot")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-px") and filename.endswith(".bridge_smus.tar"):
		imagecode = imagelookup("bridge_smus")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-px-docs-"):
		imagecode = imagelookup("docs")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)

def iosxr_tab3_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_tab3_ver3")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)
