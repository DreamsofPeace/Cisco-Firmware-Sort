from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile

def fileprocessorios (debug1,filename):
	if debug1:
		print("\tModule# \tios_ios")
	if debug1:
		print("\tSubroutine#\tfileprocessorios")
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")

	if (
	filename.startswith ("sprom") or 
	filename.startswith ("epld-sup2") or 
	filename.startswith ("epld-6548getx") or 
	filename.startswith ("6509neba") or 
	filename.startswith ("6516agbic") or 
	filename.startswith ("6548getx") or 
	filename.startswith ("66748getx")
	):
		prodname = product("c6500")
		imagecode = imagelookup("sprom")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "sconvertit0-11.tar" or 
	filename == "sconvertit0-12.tar" or 
	filename == "wconvertit0-11.zip" or 
	filename == "wconvertit0-12.zip"
	):
		prodname = product("c6500")
		imagecode = imagelookup("config-converter")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7700_03.05.29.02_00_generic_000.000_001.cwe" or filename == "MC7700_ATT_03.05.10.02_00.cwe":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICCELLATT")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7750_VZW_03.05.10.06_00.cwe":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICCELLVZW")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7710_Global_03.05.29.02.cwe":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICCELLEU")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7710_Global_03.05.24.00A.cwe":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICCELLG")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7700_03.05.29.03_00_generic_000.000_001.cwe":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICCELLBE")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "VA_B_38V_d24m.bin" or 
	filename == "vdsl.bin.32bdslfw" or 
	filename == "vdsl.bin-A2pv6C035d_d23j" or 
	filename == "vdsl.bin-A2pv6C035j" or 
	filename == "VA_A_35l_B_35l_23j.bin" or 
	filename == "vdsl.bin-A2pv6C035l" or 
	filename == "VA_A_38k1_B_38h_24g1.bin" or 
	filename == "VA_A_39m_B_38h3_24h.bin" or 
	filename == "VA_A_39h_B_38h3_24h_j.bin" or 
	filename == "VA_A_39d_B_38h3_24h_1.bin" or 
	filename == "VA_A_38q_B_38r1_24j.bin" or 
	filename == "VA_A_39m_B_38h3_24h_o.bin" or 
	filename == "VA_A_39m_B_38u_24h.bin" or 
	filename == "VA_A_39t_B_35j_24m" or 
	filename == "VA_B_38V_d24m.bin" or 
	filename == "VA_A_39m_B_38u_24o_rc1_SDK_4.14L.04A-J.bin" or 
	filename == "VA_A_39t_B_38r1_24o_rc1_SDK_4.14L.04A.bin"
	):
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWICVADSLB")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "V3_07.axf" or 
	filename == "V3_09.axf" or 
	filename == "V3_12_1.axf" or 
	filename == "V3_12_2.axf" or 
	filename == "V3_12_3.axf" or 
	filename == "Release-Notes-V3.12.1" or 
	filename == "Release-Notes-V3.12.2" or 
	filename == "portware.2730.ios" or 
	filename == "Exp_V3_11.axf" or 
	filename == "Exp_V3_11_Release_Note.pdf" or 
	filename == "2730_rel_note" or 
	filename == "Exp_v10_10.spe"
	):
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("ISRG2PVDMODEM")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "VAEW_A_39x3_B39x3_24o.SSA.bin" or 
	filename == "VAEW_A_39t_B_39d_24m.SSA" or 
	filename == "VAEW_A_39d_B_39d_24g1.SSA.bin" or 
	filename == "VAEW_A_39f1_B_39d_24g1.SSA.bin"
	):
		prodname = product ("c860vaew")
		imagecode = imagelookup ("DSLFIRMWARE")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "VAE2_A_39x3_B39x3_24o.SSA.bin" or 
	filename == "VAE2_A_39t_B39d_24m.SSA.bin"
	 ):
		prodname = product ("c860vae2")
		imagecode = imagelookup ("DSLFIRMWARE")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("mica-modem-pw") or 
	filename.startswith("mica-pw")
	):
		prodname = product ("mica-modem")
		imagecode = imagelookup ("mica-modem")
		utilssinglemove (debug1,filename,prodname,imagecode)

	else:
		splitbydash = filename.split("-")
		prodname = product (splitbydash[0])
		imagecode = imagelookup (splitbydash[1])
		if prodname == "UNKNOWN":
			messageunknowndev()
		elif imagecode == "UNKNOWN":
			messageunknownfeat()
		else:
			ios_classical (debug1,filename,prodname,imagecode)

def ios_classical (debug1,filename, prodname, imagecode):
	if debug1:
		print("\tSubroutine#\tios_classical")
	
	splitbydot = filename.split(".")
	splitbydash = filename.split("-")

	splitbydot[1] = splitbydot[1].replace("-", "")
	myversion = splitbydot[1].split("-")
	mynumber = list(myversion[0])
	if len(mynumber) == 5:
		twodigit = mynumber[0] + mynumber[1]
		vertwo = util2digit(twodigit,mynumber[2])
		fourdigit = mynumber[3] + mynumber[4]
		verthree = util2digit(vertwo,fourdigit)
		if len(splitbydot) > 2:
			if (
			splitbydot[2] != "bin" or 
			splitbydot[2] != "tar"
			):
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
	elif len(mynumber) == 4:
		twodigit = mynumber[0] + mynumber[1]
		vertwo = util2digit(twodigit,mynumber[2])
		verthree = util2digit(vertwo,mynumber[3])
		if len(splitbydot) > 2:
			if (
			splitbydot[2] != "bin" or 
			splitbydot[2] != "tar"
			):
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)


"""
		if splitbydot[2] == "bin":
			iosversion = iosversion + "(" + myversion[1] + ")"
		elif splitbydot[1] == "SPA":
			verid = list(splitbydot[2])
			vertwo = verid[0] + verid[1]
			vertwo = util2digit(vertwo,verid[2])
			verfull = util2digit(vertwo,verid[4])
			if splitbydot[3] != "bin":
				verfull = util2digit(verfull,splitbydot[3])
			filepath = filepath4(prodname,vertwo,verfull,imagecode)
			filemove (filepath, filename)
		else:
			iosprimary = iostrain(splitbydot[2], iosprimary)
			iosversion = iosversion + "(" + myversion[1] + ")" + splitbydot[2]
		if prodname == "Catalyst-6500" and imagecode == "FIELD PROGRAMABLE DEVICE":
			filepath = prodname + "/" + imagecode + "/" + iosprimary + "/" + iosversion
		elif splitbydash[0] == "c7600" and splitbydot[1] == "122-18":
			filepath = "Catalyst-6500" + "/" + imagecode + "/" + iosprimary + "/" + iosversion
		elif prodname == "7600" and imagecode == "FIELD PROGRAMABLE DEVICE":
			filepath = prodname + "-" + imagecode + "/" + iosprimary + "/" + iosversion
		elif splitbydot[0] == "s3223-adventerprisek9_wan-vz" or splitbydot[0] == "s72033-adventerprisek9_wan-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-adventerprise_wan-vz" or splitbydot[0] == "s72033-adventerprise_wan-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-advipservicesk9_wan-vz" or splitbydot[0] == "s72033-advipservicesk9_wan-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-ipbase-vz" or splitbydot[0] == "s72033-ipbase-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-ipbasek9-vz" or splitbydot[0] == "s72033-ipbasek9-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-ipservicesk9_wan-vz" or splitbydot[0] == "s72033-ipservicesk9_wan-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		elif splitbydot[0] == "s3223-ipservicesk9-vz" or splitbydot[0] == "s72033-ipservicesk9-vz":
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode + " - MODULAR"
		else:
			filepath = prodname + "/" + iosprimary + "/" + iosversion + "/" + imagecode
		filemove (filepath, filename)
"""
