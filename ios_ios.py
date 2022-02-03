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
	filename.startswith ("s72033-itpk9v") or
	filename.startswith ("s72033") and splitbydot[2].startswith ("SR")
	):
		prodname = product ("c7600s72033")
		imagecode = imagelookup(splitbydash[1])
		ios_classical (debug1,filename,prodname,imagecode)

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

	elif filename == "MC735X_9999999_9902350_05.05.58.01_00_SPRINT_005.031_000.spk":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEST")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7354_1102037_05.05.58.00_00_ATT_005.013_000.spk":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEAT")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC735X_9999999_9902574_05.05.58.00_00_GENNA_005.025_000.spk":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTECA")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "MC7304_1102029_05.05.58.00_00_TELSTRA_005.014_000.spk" or 
	filename == "MC7304_1102029_05.05.58.00_00_TELSTRA_005.013_000-2kMTU.spk"
	):
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEAU")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7304_9999999_9902674_05.05.58.00_00_GENEU-4G_005.026_000.spk":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEGB")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "MC7350_1102036_05.05.58.01_00_VZW_005.009_000.spk" or 
	filename == "MC7354MNA_1102407_05.05.58.01_00_VZW_005.005_000-2kMTU.spk" or 
	filename == "MC7350_1102036_05.05.58.01_00_Cisco_005.008_000-2kMTU.spk"
	):
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEVZ")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "MC7354MNA_1102407_05.05.58.01_00_VZW_005.006_000.spk" or 
	filename == "MC7354MNA_9999999_9902196_05.05.58.00_00_ATT_005.026_000.spk" or 
	filename == "MC735X_9999999_9902574_05.05.58.00_00_GENNA_005.025_000.spk"
	):
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("C819GWLTEMNAAK9")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename == "MC7354_1102037_05.05.58.00_00_Cisco_005.012_000-2kMTU.spk":
		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("EHWIC4GLTEAT")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename == "MC7354_9999999_05.05.58.00_00_USCellular_005.000_000.spk"
	):
		#Not able to place currently
		prodname = product ("ISRG2GENERIC")

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
	filename == "VA_A_39t_B_38r1_24o_rc1_SDK_4.14L.04A.bin" or 
	filename == "VA_A_39t_b_38r1_24o.bin"
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
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif filename in ["VAE2_A_39x3_B39x3_24o.SSA.bin","VAE2_A_39t_B39d_24m.SSA.bin"]:
		prodname = product ("c860vae2")
		imagecode = imagelookup ("dslfirmware")
		utilssinglemove (debug1,filename,prodname,imagecode)


	elif filename in ["C21031014bFU07192007.CDF", "C21041013iFU07192006.CDF", "C21031013gFU05122006.CDF", "C21031019aFU06192008_MAC14.CDF",
					"C21041013iFU07192006.CDF", "C21041014bFU07192007.CDF", "C21041019aFU06192008_MAC14.CDF", "C21041014bFU07192007.CDF"]:

		prodname = product ("ISRG2GENERIC")
		imagecode = imagelookup ("HWICCABLE")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("mica-modem-pw") or 
	filename.startswith("mica-pw")
	):
		prodname = product ("mica-modem")
		imagecode = imagelookup ("mica-modem")
		utilssinglemove (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith("c7600-fpd-pkg.122-18.SX") or 
	filename.startswith("c7600-fpd-pkg.122-18.ZY") or 
	filename.startswith("c6500-fpd-pkg")
	):
		prodname = product ("c6500")
		imagecode = imagelookup ("fpd")
		ios_classical (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c2900XL") or 
	filename.startswith ("c2900xl")
	):
		splitbydash = filename.split("-")
		prodname = product(splitbydash[0])
		imagecode = imagelookup(splitbydash[1])
		ios_classical (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("s2t54") or 
	filename.startswith ("s6t64") or 
	filename.startswith ("c6848x") or 
	filename.startswith ("c6880x") or 
	filename.startswith ("c1900") or 
	filename.startswith ("c2900") or 
	filename.startswith ("c2911a") or 
	filename.startswith ("c2951") or 
	filename.startswith ("vg3x0") or 
	filename.startswith ("vg350") or 
	filename.startswith ("c860vaew") or 
	filename.startswith ("c860vae2") or 
	filename.startswith ("c3900") or 
	filename.startswith ("c3900e") or 
	filename.startswith ("c800j") or 
	filename.startswith ("c900") or 
	filename.startswith ("c800m") or 
	filename.startswith ("ir800")
	):
		splitbydash = filename.split("-")
		prodname = product(splitbydash[0])
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c800-universalk9-mz.SPA.") or 
	filename.startswith ("c800-universalk9_npe-mz.SPA") or 
	filename.startswith ("c800-universalk9_iox-mz.SPA") or 
	filename.startswith ("c800-universalk9_iox_npe-mz.SPA")
	):
		splitbydash = filename.split("-")
		prodname = product("c800g2")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("cgr2010-universalk9_npe-mz.SPA.") or 
	filename.startswith ("cgr2010-universalk9-mz.SPA")
	):
		splitbydash = filename.split("-")
		prodname = product("cgr2010")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c5915-adventerprisek9-mz.SPA") or 
	filename.startswith ("c5915-entbase-mz.SPA")
	):
		splitbydash = filename.split("-")
		prodname = product("c5915")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c5921i86") or 
	filename.startswith ("c5921i86v") or 
	filename.startswith ("c5921x86") or 
	filename.startswith ("c5921x86ise")
	):
		splitbydash = filename.split("-")
		prodname = product("c5921i86")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c5930-adventerprisek9-mz.SPA")
	):
		splitbydash = filename.split("-")
		prodname = product("c5930")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c5940-adventerprisek9-mz.SPA") or 
	filename.startswith ("c5940-entbase-mz.SPA")
	):
		splitbydash = filename.split("-")
		prodname = product("c5940")
		imagecode = imagelookup(splitbydash[1])
		ios_spa (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("dsc-c5800-mz")
	):
		splitbydash = filename.split("-")
		prodname = product(splitbydash[1])
		imagecode = imagelookup(splitbydash[0])
		ios_classical (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c1000-universal")
	):
		splitbydash = filename.split("-")
		prodname = product(splitbydash[0])
		imagecode = imagelookup(splitbydash[1])
		ios_classical (debug1,filename,prodname,imagecode)

	elif (
	filename.startswith ("c1000")
	):
		splitbydash = filename.split("-")
		prodname = product ("c1000router")
		imagecode = imagelookup(splitbydash[1])
		ios_classical (debug1,filename,prodname,imagecode)

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

def ios_spa (debug1,filename, prodname, imagecode):
	if debug1:
		print("\tSubroutine#\tios_spa")

	splitbydot = filename.split(".")
	splitbydot[2] = splitbydot[2].replace("-", "")
	mynumber = list(splitbydot[2])
	twodigit = mynumber[0] + mynumber[1]
	vertwo = util2digit(twodigit,mynumber[2])
	verthree = util2digit(vertwo,mynumber[3])
	verfour = util2digit(verthree,splitbydot[3])
	vertwo = iostrain(splitbydot[3], vertwo)
	filepath = filepath4(prodname,vertwo,verfour,imagecode)
	filemove (filepath, filename)

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
			splitbydot[2] == "bin" or 
			splitbydot[2] == "tar"
			):
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
			elif (
			filename.startswith("c6500-fpd-pkg") or 
			filename.startswith("c7600-fpd-pkg")
			):
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,imagecode,vertwo,verthree)
				filemove (filepath, filename)
			else:
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
			splitbydot[2] == "bin" or 
			splitbydot[2] == "tar"
			):
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
			elif (
			filename.startswith("c6500-fpd-pkg") or 
			filename.startswith("c7600-fpd-pkg")
			):
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,imagecode,vertwo,verthree)
				filemove (filepath, filename)
			else:
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
	elif len(mynumber) == 6:
		twodigit = mynumber[0] + mynumber[1]
		vertwo = util2digit(twodigit,mynumber[2])
		fourdigit = mynumber[3] + mynumber[4] + mynumber[5]
		verthree = util2digit(vertwo,fourdigit)
		if len(splitbydot) > 2:
			if (
			splitbydot[2] == "bin" or 
			splitbydot[2] == "tar"
			):
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
			elif (
			filename.startswith("c6500-fpd-pkg") or 
			filename.startswith("c7600-fpd-pkg")
			):
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,imagecode,vertwo,verthree)
				filemove (filepath, filename)
			else:
				vertwo = iostrain(splitbydot[2], vertwo)
				verthree = util2digit(verthree,splitbydot[2])
				filepath = filepath4(prodname,vertwo,verthree,imagecode)
				filemove (filepath, filename)
