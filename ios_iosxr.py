from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,util6digit,stringtolist
from iosutils import util2collapse
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
	filename == "CSM.zip" or 
	filename == "csm-3.5.2.zip" or 
	filename == "csm-4.0.zip"
	):
		prodname = product ("asr9k")
		imagecode = imagelookup("ciscosoftwaremanager")
		utilssinglemove (debug1,filename,prodname,imagecode)
	
	elif (
	filename.startswith("asr9k-cnbng-x64-")
	):
		prodname = product ("asr9k")
		imagecode = imagelookup("cnbng")
		workname = filename.replace("asr9k-cnbng-x64-","")
		workname = workname.replace("1.0.0.0-r","")
		workname = workname.replace("2.0.0.0-r","")
		workname = workname.replace(".x86_64.rpm","")
		postsplit = list(workname)
		if (
			workname.startswith("24") or
			workname.startswith("25") or
			workname.startswith("26") or
			workname.startswith("27") or
			workname.startswith("28") or
			workname.startswith("29")
			):
			if 4 == len(postsplit):
				ver3 = postsplit[0] + postsplit[1] + "." + postsplit[2] + "." + postsplit[3]
			elif 5 == len(postsplit):
				ver3 = postsplit[0] + postsplit[1] + "." + postsplit[2] + "." + postsplit[3] + postsplit[4]
			ver2 = postsplit[0] + postsplit[1] + "." + postsplit[2]
			filepath = filepath4 (prodname,ver2,ver3,imagecode)
			filemove (filepath, filename)

		else:
			if 4 == len(postsplit):
				verjoin = postsplit[1] + postsplit[2]
				vertwo   = util2digit(postsplit[0],verjoin)
				verthree = util3digit(postsplit[0],verjoin,postsplit[2])
				filepath = filepath4 (prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
			elif 3 == len(postsplit):
				vertwo   = util2digit(postsplit[0],postsplit[1])
				verthree = util3digit(postsplit[0],postsplit[1],postsplit[2])
				filepath = filepath4 (prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
			elif 5 == len(postsplit):
				place2 = postsplit[1] + postsplit[2]
				place3 = postsplit[3] + postsplit[4]
				vertwo   = util2digit(postsplit[0],place2)
				verthree = util3digit(postsplit[0],place2,place3)
				filepath = filepath4 (prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)

	elif (
	filename.startswith("ASR9K") or 
	filename.startswith("ASR9k") or 
	filename.startswith("ASR9000") or 
	filename.startswith("asr9k")
	):
		iosxr_asr9k (debug1,filename)

	elif (
	filename.startswith("fullk9") or
	filename.startswith("xrv9k") or
	filename.startswith("XRV9000-docs") or
	filename.startswith("XRV9K-docs")
	):
		prodname = product ("iosxrvfull")
		iosxr_iosxrv (debug1,filename,prodname)

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

	elif (
	filename.startswith("xrd-control-plane-container-")
	):
		prodname = product ("xrvcontainer")
		imagecode = imagelookup("control-plane")
		workname = filename.replace(".tgz","")
		workname = workname.replace("xrd-control-plane-container-x64.dockerv1.tgz-","")
		workname = workname.replace("xrd-control-plane-container-x64.dockerv1-","")
		workname = workname.replace("xrd-control-plane-container-x64.","")
		workname = workname.replace("xrd-control-plane-container-x86.","")
		iosxr_dot_workname_1ver (debug1,filename,prodname,imagecode,workname)

	elif (
	filename.startswith("xrd-vrouter-container-")
	):
		prodname = product ("xrvcontainer")
		imagecode = imagelookup("data-plane")
		workname = filename.replace(".tgz","")
		workname = workname.replace("xrd-vrouter-container-x64.dockerv1.tgz-","")
		workname = workname.replace("xrd-vrouter-container-x64.dockerv1-","")
		workname = workname.replace("xrd-vrouter-container-x64.","")
		workname = workname.replace("xrd-vrouter-container-x86.","")
		iosxr_dot_workname_1ver (debug1,filename,prodname,imagecode,workname)

	else:
#		if prodname == "UNKNOWN":
#			messageunknowndev()
#		elif imagecode == "UNKNOWN":
#			messageunknownfeat()
		messageunknowndev()

def iosxr_iosxrv (debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tiosxr_iosxrv")
	workname = filename.replace("fullk9-R-XRV9000-","")
	workname = workname.replace("-RRVG","")
	workname = workname.replace("-RR","")
	workname = workname.replace("-VG","")
	workname = workname.replace(".tar","")
	workname = workname.replace("XRV9K-docs-","")
	workname = workname.replace("XRV9000-docs-","")
	if filename.startswith("XRV9K-docs-"):
		splitbydot = workname.split(".")
		version2 = util2digit(splitbydot[0],splitbydot[1])
		imagecode = imagelookup("docs")
		filepath = filepath4 (prodname,version2,workname,imagecode)
		filemove (filepath, filename)
	elif filename.startswith("XRV9000-docs-"):
		splitbynone = list(workname)
		imagecode = imagelookup("docs")
		if len(splitbynone) == 3:
			version2 = util2digit(splitbynone[0],splitbynone[1])
			version3 = util3digit(splitbynone[0],splitbynone[1],splitbynone[2])
			filepath = filepath4 (prodname,version2,version3,imagecode)
			filemove (filepath, filename)
		elif len(splitbynone) == 4:
			version2 = util2digit(splitbynone[0],splitbynone[1])
			version3 = util3digit(splitbynone[0],splitbynone[1],util2collapse(splitbynone[2],splitbynone[3]))
			filepath = filepath4 (prodname,version2,version3,imagecode)
			filemove (filepath, filename)
	splitbynone = stringtolist(workname)
	if "CSC" in filename:
		workname = workname.replace("xrv9k-","")
		splitbydot = workname.split(".")
		imagecode = imagelookup("smu")
		version2 = util2digit(splitbydot[0],splitbydot[1])
		version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath5 (prodname,version2,version3,imagecode,splitbydot[2])
		filemove (filepath, filename)
	if filename.endswith("-RRVG.tar"):
		imagecode = imagelookup("rrvga")
	elif filename.endswith("-RR.tar"):
		imagecode = imagelookup("rr")
	elif filename.endswith("-VG.tar"):
		imagecode = imagelookup("basevga")
	elif filename.endswith(".tar"):
		imagecode = imagelookup("base")
	if splitbynone[2] == ".":
		splitbydot = workname.split(".")
		version2 = util2digit(splitbydot[0],splitbydot[1])
		version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath4 (prodname,version2,version3,imagecode)
		filemove (filepath, filename)
	elif (
	isinstance(splitbynone, list) and len(splitbynone) > 1 and
	splitbynone[0] == "2" and splitbynone[1] == "4" or
	splitbynone[0] == "2" and splitbynone[1] == "5" or
	splitbynone[0] == "2" and splitbynone[1] == "6" or
	splitbynone[0] == "2" and splitbynone[1] == "7" or
	splitbynone[0] == "2" and splitbynone[1] == "8" or
	splitbynone[0] == "2" and splitbynone[1] == "9"
	):
		version2 = util2digit(util2collapse(splitbynone[0],splitbynone[1]),splitbynone[2])
		version3 = util3digit(util2collapse(splitbynone[0],splitbynone[1]),splitbynone[2],splitbynone[3])
		filepath = filepath4 (prodname,version2,version3,imagecode)
		filemove (filepath, filename)

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
	
def iosxr_asr9k_workname (debug1,prodname,imagecode,filename,workname):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9k_workname")
	splitbydot = workname.split(".")
	version2 = util2digit(splitbydot[0],splitbydot[1])
	version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4 (prodname,version2,version3,imagecode)
	filemove (filepath, filename)

def iosxr_asr9k (debug1,filename):
	if debug1:
		print("\tSubroutine#\tiosxr_asr9k")
	prodname = product ("asr9k")
	if (
	"Turboboot.tar" in filename or
	"turboboot.tar" in filename
	):
		imagecode = imagelookup("turboboot")
		workname = filename.replace("turboboot.tar","")
		workname = workname.replace("Turboboot.tar","")
		workname = workname.replace("ASR9K-iosxr-Px-","")
		workname = workname.replace("ASR9K-iosxr-px-","")
		workname = workname.replace("ASR9k-iosxr-px-","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)

	elif (
	"bridge_smus.tar" in filename
	):
		imagecode = imagelookup("bridge_smus")
		workname = filename.replace("-bridge_smus.tar","")
		workname = workname.replace("ASR9K-iosxr-px-","")
		workname = workname.replace("ASR9k-iosxr-px-","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)
		
	elif (
	"ASR9K-x64-iosxr-k9-" in filename
	):
		imagecode = imagelookup("corek9")
		workname = filename.replace("ASR9K-x64-iosxr-k9-","")
		workname = workname.replace(".tar","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)

	elif (
	"ASR9K-x64-iosxr-" in filename
	):
		imagecode = imagelookup("core")
		workname = filename.replace("ASR9K-x64-iosxr-","")
		workname = workname.replace(".tar","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)

	elif (
	"asr9k-mini-x64-migrate_to_eXR" in filename
	):
		imagecode = imagelookup("migrate_to_eXR")
		workname = filename.replace("asr9k-mini-x64-migrate_to_eXR.tar-","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)

	elif (
	filename.startswith("ASR9K-x64-docs-") or 
	filename.startswith("ASR9K-px-docs-") or 
	filename.startswith("ASR9K-docs-")
	):
		imagecode = imagelookup("docs")
		workname = filename.replace("ASR9K-x64-docs-","")
		workname = workname.replace("ASR9K-px-docs-","")
		workname = workname.replace("ASR9K-docs-","")
		workname = workname.replace(".tar","")
		iosxr_asr9k_workname(debug1,prodname,imagecode,filename,workname)
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

	elif filename.startswith("asr9k-full-x64-migrate_to_eXR.tar"):
		imagecode = imagelookup("migrate_to_eXR")
		iosxr_dot1_ver3 (debug1,filename,prodname,imagecode)

	elif filename.startswith("asr9k-mini-x64-"):
		imagecode = imagelookup("mini-x64")
		iosxr_tab3_ver3 (debug1,filename,prodname,imagecode)

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

	elif filename.startswith("asr9k-vsm-cgv6"):
		imagecode = imagelookup("cgv6")
		workname = filename.replace("\n","")
		workname = workname.replace(".ova","")
		workname = workname.replace("asr9k-vsm-cgv6-","")
		workname = workname.replace("asr9k-vsm-cgv6.","")
		iosxr_dot_workname_1ver (debug1,filename,prodname,imagecode,workname)

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

def iosxr_dot_workname_1ver (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tSubroutine#\tiosxr_dot_workname")
	splitbydot = workname.split(".")
	if len(splitbydot) == 2:
		version = util2digit(splitbydot[0],splitbydot[1])
		filepath = filepath3 (prodname,version,imagecode)
	elif len(splitbydot) == 3:
		version = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		filepath = filepath3 (prodname,version,imagecode)
	elif len(splitbydot) == 4:
		version = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath3 (prodname,version,imagecode)
	elif len(splitbydot) == 5:
		version = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath3 (prodname,version,imagecode)
	elif len(splitbydot) == 6:
		version = util6digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
		filepath = filepath3 (prodname,version,imagecode)
	else:
		filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

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
