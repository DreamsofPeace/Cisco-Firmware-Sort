from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_iosxr (debug1,filename):
	if debug1:
		print("\tModule#\tios_security")
	if debug1:
		print("\tSubroutine#\tfileprocessorsecurity")

	if filename.startswith("ASR9K"):
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
		

def iosxr_asr9k (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9k")
	
