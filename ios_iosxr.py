from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessor_iosxr (debug1,filename):
	if debug1:
		print("\tModule#\t\tios_iosxr")
	if debug1:
		print("\tSubroutine#\tfileprocessor_iosxr")

	splitbydot = filename.split(".")

	if (
	filename.startswith("asr9k-px-") and splitbydot[3].startswith("CSC") or 
	filename.startswith("asr9k-x64-") and splitbydot[3].startswith("CSC") or 
	filename.startswith("asr9k-sysadmin-") and splitbydot[3].startswith("CSC")
	):
		iosxr_asr9ksmu (debug1,filename)
	
	elif (
	filename.startswith("ASR9K") or 
	filename.startswith("ASR9k") or 
	filename.startswith("ASR9000") or 
	filename.startswith("asr9k")
	):
		iosxr_asr9k (debug1,filename)

	elif (
	filename.startswith("fullk9")
	):
		iosxr_asr9kv (debug1,filename)

	elif (
	filename.startswith("xrv9k")
	):
		iosxr_asr9kvsmu (debug1,filename)

	elif (
	filename == "XRV9K-docs-7.4.1.tar" or 
	filename == "XRV9000-docs-623.tar" or 
	filename == "XRV9000-docs-6225.tar"
	):
		prodname = product ("iosxrvfull")
		imagecode = imagelookup("docs")
		filepath = filepath2 (prodname,imagecode)
		filemove (filepath, filename)

	elif (
	filename == "xrvr-full-4.3.2.vmdk" or
	filename == "xrvr-fullk9-4.3.2.vmdk"
	):
		prodname = product ("iosxrvdemo")
		filepath = filepath2 (prodname,"4.3.2")
		filemove (filepath, filename)

	elif (
	filename.startswith("iosxrv-demo") or
	filename.startswith("iosxrv-k9-demo")
	):
		iosxr_iosxrv_demo (debug1,filename)
	else:
#		if prodname == "UNKNOWN":
#			messageunknowndev()
#		elif imagecode == "UNKNOWN":
#			messageunknownfeat()
		messageunknowndev()

def iosxr_iosxrv_demo (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_iosxrv_demo")
	prodname = product ("iosxrvdemo")
	workname = filename.replace("iosxrv-demo.ova-","")
	workname = workname.replace("iosxrv-demo.vmdk-","")
	workname = workname.replace(".vmdk","")
	workname = workname.replace(".ova","")
	workname = workname.replace("iosxrv-k9-demo-","")
	workname = workname.replace("iosxrv-demo-","")
	splitbydot = workname.split(".")
	verthree= util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath2 (prodname,verthree)
	filemove (filepath, filename)

def iosxr_asr9kv (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9kv")
	prodname = product ("iosxrvfull")
	workname = filename.replace(".tar", "")
	splitbydash = workname.split("-")
	if filename.endswith("-RRVG.tar"):
		imagecode = imagelookup("rrvga")
	elif filename.endswith("-RR.tar"):
		imagecode = imagelookup("rr")
	elif filename.endswith("-VG.tar"):
		imagecode = imagelookup("basevga")
	else:
		imagecode = imagelookup("base")
	verlist = list(splitbydash[3])
	if len(verlist) == 4:
		verfull = util4digit(verlist[0],verlist[1],verlist[2],verlist[3])
		vertwo = util2digit(verlist[0],verlist[1])
	elif len(verlist) == 3:
		verfull = util3digit(verlist[0],verlist[1],verlist[2])
		vertwo = util2digit(verlist[0],verlist[1])
	filepath = filepath4 (prodname,vertwo,verfull,imagecode)
	filemove (filepath, filename)

def iosxr_asr9kvsmu (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9kvsmu")
	prodname = product ("iosxrvfull")
	imagecode = imagelookup("smu")
	workname = filename.replace("xrv9k-sysadmin-", "")
	workname = workname.replace("xrv9k-", "")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	versmu = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath5 (prodname,vertwo,versmu,imagecode,splitbydot[3])
	filemove (filepath, filename)

def iosxr_asr9ksmu (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9ksmu")
	prodname = product ("asr9k")
	imagecode = imagelookup("smu")
	workname = filename.replace("asr9k-px-", "")
	workname = workname.replace("asr9k-x64-", "")
	workname = workname.replace("asr9k-sysadmin-", "")
	splitbydot = workname.split(".")
	vertwo = util2digit(splitbydot[0],splitbydot[1])
	versmu = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath5 (prodname,vertwo,versmu,imagecode,splitbydot[3])
	filemove (filepath, filename)

def iosxr_asr9k (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9k")
	prodname = product ("asr9k")
	if (
	filename.startswith("ASR9K-iosxr-px") and filename.endswith("turboboot.tar") or 
	filename.startswith("ASR9K-iosxr-px") and filename.endswith("Turboboot.tar")
	):
		imagecode = imagelookup("turboboot")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("ASR9K-iosxr-px") and filename.endswith("bridge_smus.tar") or 
	filename.startswith("ASR9k-iosxr-px") and filename.endswith("bridge_smus.tar")
	):
		imagecode = imagelookup("bridge_smus")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("ASR9K-iosxr-") and filename.endswith("bridge_smus.tar")
	):
		imagecode = imagelookup("bridge_smus")
		iosxr_tab2_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("ASR9K-px-docs-") or 
	filename.startswith("ASR9K-x64-docs")
	):
		imagecode = imagelookup("docs")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif (
	filename.startswith("asr9k-") and filename.endswith("sp-1.0.0.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp1.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp2.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp3.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp4.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp5.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp6.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp7.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp8.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp9.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp10.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp11.tar") or 
	filename.startswith("asr9k-") and filename.endswith("sp12.tar")
	):
		iosxr_service_pack  (debug1,filename,prodname)
	elif filename.startswith("asr9k-mini-x64-migrate_to_eXR.tar"):
		imagecode = imagelookup("migrate_to_eXR")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-mini-x64-migrate_to_eXR"):
		imagecode = imagelookup("migrate_to_eXR")
		iosxr_dot1_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-full-x64-migrate_to_eXR"):
		imagecode = imagelookup("migrate_to_eXR")
		iosxr_dot1_ver3 (debug1,filename,prodname,imagecode)
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
	elif filename.startswith("ASR9K-iosxr-p-k9"):
		imagecode = imagelookup("corek9")
		iosxr_tab4_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-px-"):
		imagecode = imagelookup("core")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("ASR9K-iosxr-p-"):
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
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)
	elif filename.startswith("asr9k-goldenk9-x64-"):
		imagecode = imagelookup("goldenk9")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)

def iosxr_dot1_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_dot1_ver3")
	splitbydot = filename.split(".")
	ver2 = util2digit(splitbydot[1],splitbydot[2])
	ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

def iosxr_tab2_ver3 (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tiosxr_tab3_ver3")
	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)

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
	if filename.endswith("sp1.tar"):
		imagecode = imagelookup("sp1")
	elif filename.endswith("sp2.tar"):
		imagecode = imagelookup("sp2")
	elif filename.endswith("sp3.tar"):
		imagecode = imagelookup("sp3")
	elif filename.endswith("sp4.tar"):
		imagecode = imagelookup("sp4")
	elif filename.endswith("sp5.tar"):
		imagecode = imagelookup("sp5")
	elif filename.endswith("sp6.tar"):
		imagecode = imagelookup("sp6")
	elif filename.endswith("sp7.tar"):
		imagecode = imagelookup("sp7")
	elif filename.endswith("sp8.tar"):
		imagecode = imagelookup("sp8")
	elif filename.endswith("sp9.tar"):
		imagecode = imagelookup("sp9")
	elif filename.endswith("sp10.tar"):
		imagecode = imagelookup("sp10")
	elif filename.endswith("sp11.tar"):
		imagecode = imagelookup("sp11")
	elif filename.endswith("sp12.tar"):
		imagecode = imagelookup("sp12")
	elif filename.endswith("sp-1.0.0.tar"):
		imagecode = imagelookup("sp1")

	splitbydash = filename.split("-")
	splitbydot = splitbydash[2].split(".")
	ver2 = util2digit(splitbydot[0],splitbydot[1])
	ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,ver2,ver3,imagecode)
	filemove (filepath, filename)
