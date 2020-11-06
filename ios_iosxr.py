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
	filename.startswith("ASR9000") or 
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
	elif filename.startswith("ASR9K-iosxr-px") and filename.endswith("bridge_smus.tar"):
		imagecode = imagelookup("bridge_smus")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("ASR9K-px-docs-") or 
	filename.startswith("ASR9K-x64-docs")
	):
		imagecode = imagelookup("docs")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("asr9k-px-") and filename.endswith("-sp1.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp2.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp3.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp4.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp5.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp6.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp7.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp8.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp9.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp10.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp11.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith("-sp12.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp1.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp2.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp3.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp4.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp5.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp6.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp7.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp8.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp9.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp10.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp11.tar") or 
	filename.startswith("asr9k-px-") and filename.endswith(".sp12.tar")
	):
		imagecode = imagelookup("docs")
		iosxr_service_pack  (debug1,filename,prodname)
	elif filename.startswith("asr9k-mini-x64-migrate_to_eXR"):
		imagecode = imagelookup("migrate_to_eXR")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-mini-x64-"):
		imagecode = imagelookup("mini-x64")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-vsm-cgv6"):
		imagecode = imagelookup("cgv6")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-x64-iosxr-px-k9"):
		imagecode = imagelookup("core64k9")
		iosxr_tab5_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-x64-iosxr-px"):
		imagecode = imagelookup("core64")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-px-k9"):
		imagecode = imagelookup("corek9")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-px-"):
		imagecode = imagelookup("core")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9000-iosxr-k9"):
		imagecode = imagelookup("corek9")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-k9"):
		imagecode = imagelookup("corek9")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-ncs500x-nV-px"):
		imagecode = imagelookup("nvsat")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-9000v-nV-x64"):
		imagecode = imagelookup("nvsat")
		iosxr_nv_x64 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-x64-usb_boot"):
		imagecode = imagelookup("usb_boot")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)

def iosxr_tab3_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_tab3_ver3")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[3].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def iosxr_tab4_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_tab4_ver3")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[4].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def iosxr_tab5_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_tab5_ver3")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[5].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def iosxr_nv_x64 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_nv_x64")
	splitbydash = filename.split("-")
	splitbydot = list(splitbydash[5])
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def iosxr_service_pack (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tiosxr_service_pack")
	if filename.endswith(".sp1.tar"):
		imagecode = imagelookup("sp1")
	elif filename.endswith(".sp2.tar"):
		imagecode = imagelookup("sp2")
	elif filename.endswith(".sp3.tar"):
		imagecode = imagelookup("sp3")
	elif filename.endswith(".sp4.tar"):
		imagecode = imagelookup("sp4")
	elif filename.endswith(".sp5.tar"):
		imagecode = imagelookup("sp5")
	elif filename.endswith(".sp6.tar"):
		imagecode = imagelookup("sp6")
	elif filename.endswith(".sp7.tar"):
		imagecode = imagelookup("sp7")
	elif filename.endswith(".sp8.tar"):
		imagecode = imagelookup("sp8")
	elif filename.endswith(".sp9.tar"):
		imagecode = imagelookup("sp9")
	elif filename.endswith(".sp10.tar"):
		imagecode = imagelookup("sp10")
	elif filename.endswith(".sp11.tar"):
		imagecode = imagelookup("sp11")
	elif filename.endswith(".sp12.tar"):
		imagecode = imagelookup("sp12")
	elif filename.endswith("-sp1.tar"):
		imagecode = imagelookup("sp1")
	elif filename.endswith("-sp2.tar"):
		imagecode = imagelookup("sp2")
	elif filename.endswith("-sp3.tar"):
		imagecode = imagelookup("sp3")
	elif filename.endswith("-sp4.tar"):
		imagecode = imagelookup("sp4")
	elif filename.endswith("-sp5.tar"):
		imagecode = imagelookup("sp5")
	elif filename.endswith("-sp6.tar"):
		imagecode = imagelookup("sp6")
	elif filename.endswith("-sp7.tar"):
		imagecode = imagelookup("sp7")
	elif filename.endswith("-sp8.tar"):
		imagecode = imagelookup("sp8")
	elif filename.endswith("-sp9.tar"):
		imagecode = imagelookup("sp9")
	elif filename.endswith("-sp10.tar"):
		imagecode = imagelookup("sp10")
	elif filename.endswith("-sp11.tar"):
		imagecode = imagelookup("sp11")
	elif filename.endswith("-sp12.tar"):
		imagecode = imagelookup("sp12")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)
