from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessorvoice(debug1,filename):
	if debug1:
		print("\tModule#\t\tios_voice")
	if debug1:
		print("\tSubroutine#\tfileprocessorvoice")

	if filename.startswith("cmterm"):
		fileprocphone(debug1,filename)

	elif (
	filename == "vgc-main.1-3-1ES8-2.tar" or 
	filename == "vgc-main.1-3-2.tar" or 
	filename == "vgc-main.1-3-2ES3.tar" or 
	filename == "vgc-main_1-3-1es8-2_Readme.txt" or 
	filename == "vgc-main_1-3-2es3_Readme.txt"
	):
		prodname = product ("vg248")
		utilssingleprodname (debug1,filename,prodname)
	else:
		messageunknownfile()

def fileprocphone(debug1,filename):
	if filename.startswith("cmterm-3905"):
		prodname = product ("ipp3905")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-3905.","")
		file_proc_phone_noimage(debug1,filename,prodname,workname)

	elif filename.startswith("cmterm-7911_7906-sccp"):
		prodname = product ("ipp7911_7906")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7911_7906-sip"):
		prodname = product ("ipp7911_7906")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7914-sccp"):
		prodname = product ("ipp7914")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7914-sip"):
		prodname = product ("ipp7914")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7915"):
		prodname = product ("ipp7915")
		fileprocphone3digit(debug1,filename,prodname)

	elif filename.startswith("cmterm-7916"):
		prodname = product ("ipp7916")
		fileprocphone3digit(debug1,filename,prodname)

	elif filename.startswith("cmterm-7921-sccp"):
		prodname = product ("ipp7921")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7921-sip"):
		prodname = product ("ipp7921")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7931-sccp"):
		prodname = product ("ipp7931")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7931-sip"):
		prodname = product ("ipp7931")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7940_7960-sccp"):
		prodname = product ("ipp7940_7960")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7940_7960-sip"):
		prodname = product ("ipp7940_7960")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7940-7960"):
		prodname = product ("ipp7940_7960")
		fileprocphone3digittwo(debug1,filename,prodname)

	elif filename.startswith("cmterm-7941_7961-sccp"):
		prodname = product ("ipp7941_7961")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7941_7961-sip"):
		prodname = product ("ipp7941_7961")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7942_7962-sccp"):
		prodname = product ("ipp7942_7962")
		imagecode = imagelookup("sccp")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)

	elif filename.startswith("cmterm-7942_7962-sip"):
		prodname = product ("ipp7942_7962")
		imagecode = imagelookup("sip")
		fileprocphone3digittype(debug1,filename,prodname,imagecode)



	elif filename.startswith("cmterm-7970_7971-sccp"):
		prodname = product ("ipp7970_7971")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7970_7971-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7970_7971-sip"):
		prodname = product ("ipp7970_7971")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7970_7971-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7975-sccp"):
		prodname = product ("ipp7975")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7975-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7975-sip"):
		prodname = product ("ipp7975")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7975-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-8845_65-sip"):
		prodname = product ("ipp8845_65")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-8845_65-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-8845_65"):
		prodname = product ("ipp8845_65")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-8845_65.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7937-sccp"):
		prodname = product ("ipp7937")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7937-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7937-QED"):
		prodname = product ("ipp7937")
		imagecode = imagelookup("qed")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7937-QED-","")
		workname = workname.replace("-SCCP","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7937-"):
		prodname = product ("ipp7937")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7937-","")
		workname = workname.replace("-SCCP","")
		workname = workname.replace("-sccp","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7945_7965-sccp"):
		prodname = product ("ipp7945_7965")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7945_7965-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-7945_7965-sip"):
		prodname = product ("ipp7945_7965")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-7945_7965-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-894x-sccp"):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-894x-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-8941_8945-sccp"):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-8941_8945-sccp.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-894x-sip"):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-894x-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-8941_8945-sip"):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-8941_8945-sip.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-SIP8941_8945."):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-SIP8941_8945.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-SIP894x"):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sip")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-SIP894x.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-SCCP894x."):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-SCCP894x.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-SCCP8941_8945."):
		prodname = product ("ipp894x")
		imagecode = imagelookup("sccp")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-SCCP8941_8945.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-ata187-qed."):
		prodname = product ("ata187")
		imagecode = imagelookup("qed")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-ata187-qed.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-ata187."):
		prodname = product ("ata187")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-ata187.","")
		file_proc_phone_noimage(debug1,filename,prodname,workname)

	elif filename.startswith("cmterm-ata190-qed."):
		prodname = product ("ata190")
		imagecode = imagelookup("qed")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-ata190-qed.","")
		file_proc_phone_dash(debug1,filename,prodname,imagecode,workname)

	elif filename.startswith("cmterm-ata190."):
		prodname = product ("ata187")
		imagecode = imagelookup("qed")
		workname = file_proc_strip (debug1,filename)
		workname = workname.replace("cmterm-ata190.","")
		file_proc_phone_noimage(debug1,filename,prodname,workname)

	else:
		messageunknownfile()

def file_proc_strip (debug1,filename):
	if debug1:
		print("\tSubroutine#\tfile_proc_strip")
	workname = filename.replace(".k3.cop.sgn","")
	workname = workname.replace(".cop.sgn","")
	workname = workname.replace(".cop","")
	workname = workname.replace(".zip","")
	workname = workname.replace(".exe","")
	return workname

def file_proc_phone_dash(debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tSubroutine#\tfile_proc_phone_dash")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydash = workname.split("-")
		if debug1:
			print(len(splitbydash), end="\n")
		if len(splitbydash) == 3:
			version = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
			filepath = filepath3(prodname,version,imagecode)
			filemove (filepath, filename)
		elif len(splitbydash) == 4:
			version = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
			filepath = filepath3(prodname,version,imagecode)
			filemove (filepath, filename)
		elif len(splitbydash) == 5:
			version = util5digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
			filepath = filepath3(prodname,version,imagecode)
			filemove (filepath, filename)

def file_proc_phone_noimage(debug1,filename,prodname,workname):
	if debug1:
		print("\tSubroutine#\tfile_proc_phone_noimage")
	if prodname == "UNKNOWN":
		messageunknowndev()
	else:
		splitbydash = workname.split("-")
		if len(splitbydash) == 3:
			version = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
			filepath = filepath2(prodname,version)
			filemove (filepath, filename)
		elif len(splitbydash) == 4:
			version = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
			filepath = filepath2(prodname,version)
			filemove (filepath, filename)
		elif len(splitbydash) == 5:
			version = util5digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
			filepath = filepath2(prodname,version)
			filemove (filepath, filename)
	

def fileprocphone3digit(debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfileprocphone3digit")
	if prodname == "UNKNOWN":
		messageunknownfile()
	else:
		splitbydot = filename.split(".")
		splitbydash = splitbydot[1].split("-")
		ver2 = util2digit(splitbydash[0],splitbydash[1])
		ver3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
		filepath = filepath3(prodname,ver2,ver3)
		filemove (filepath, filename)

def fileprocphone3digittwo(debug1,filename,prodname):
	if debug1:
		print("\tSubroutine#\tfileprocphone3digittwo")
	if prodname == "UNKNOWN":
		messageunknownfile()
	else:
		splitbydash = filename.split("-")
#	if splitbydash[4] == "sip.cop":
#		fileprocphone3digitsip(debug1,filename,prodname)
#	elif splitbydash[4] == "-sccp.cop":
#		fileprocphone3digitsccp(debug1,filename,prodname)

def fileprocphone3digittype(debug1,filename,prodname,imagecode):
	if debug1:
		print("\tSubroutine#\tfileprocphone3digittype")
	if prodname == "UNKNOWN" or imagecode == "UNKNOWN":
		messageunknownfile()
	else:
		splitbydot = filename.split(".")
		splitbydash = splitbydot[1].split("-")
		ver2 = util2digit(splitbydash[0],splitbydash[1])
		ver3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
		filepath = filepath4(prodname,ver2,ver3,imagecode)
		filemove (filepath, filename)
