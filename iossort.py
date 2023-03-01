#!/use/bin/python
# -*- coding: utf-8 -*-

# Futures

# Generic/Built-in
import argparse
import getopt
import hashlib
import json
import os
import re
import shutil
import sys

# Other Libs

# Owned
from iosutils     import *
from ios_nexus    import fileprocessornxos
from ios_voice    import fileprocessorvoice
from ios_security import fileprocessorsecurity
from ios_iosxe    import fileprocessor_iosxe
from ios_iosxr    import fileprocessor_iosxr
from ios_servers  import file_proc_servers
from ios_ios      import fileprocessorios
from ios_wireless import fileprocessor_wireless

#Credits
__author__ = ""
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = ""

def nbar (filename):
	prodname = product ("ntwkmgmt")
	imagecode = imagelookup ("nbar")
	workname = filename.replace(".pack","")
	splitbydash = workname.split("-")
	if filename.startswith("pp-adv-nam-18-"):
		workname = workname.replace("pp-adv-nam-18-","")
		filepath = filepath3(prodname,imagecode,workname)
		filemove (filepath, filename)
	elif filename.startswith("pp-adv-nam-61-18-"):
		workname = workname.replace("pp-adv-nam-61-18-","")
		filepath = filepath3(prodname,imagecode,workname)
		filemove (filepath, filename)
	elif filename.startswith("pp-adv-csr1000v-153-2-S0a-15-"):
		workname = workname.replace("pp-adv-csr1000v-153-2-S0a-15-","")
		filepath = filepath3(prodname,imagecode,workname)
		filemove (filepath, filename)
	else:
		try:
			myver = splitbydash[6]
		except:
			myver = splitbydash[5]
		filepath = filepath3(prodname,imagecode,myver)
		filemove (filepath, filename)

def waas (filename):
	prodname = "WAAS"
	splitbydot = filename.split(".")
	splitbydash = filename.split("-")

	if splitbydash[0] == "waas":
		if splitbydash[1] == "x86_64":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if splitbydash[3] == "npe":
				imagecode = "SYSTEM-SOFTWARE - 64bit-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE - 64bit"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "universal":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if splitbydash[3] == "npe":
				imagecode = "SYSTEM-SOFTWARE-UNIVERSAL-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE-UNIVERSAL"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydot[4] == "sysimg":
			localdotsplit = splitbydash[1].split(".")
			mylead = localdotsplit[0].lstrip("waas-")
			mainver = mylead[0] + "." + localdotsplit[1]
			fullver = mylead[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "SYSTEM-SOFTWARE-32bit-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE-32bit"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "accelerator":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "ACCELERATOR-NPE"
			else:
				imagecode = "ACCELERATOR"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "kdump" and splitbydash[2] == "addon":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "KDUMP-ADDON-NPE"
			else:
				imagecode = "KDUMP-ADDON"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "kdump":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "KDUMP-NPE"
			else:
				imagecode = "KDUMP"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "rescue" and splitbydash[2] == "cdrom":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "RESCUE-CD-NPE"
			else:
				imagecode = "RESCUE-CD"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "rescue" and splitbydash[2] == "cdrom":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in filename or  "NPE" in filename:
				imagecode = "RESCUE-CD-NPE"
			else:
				imagecode = "RESCUE-CD"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

	elif splitbydash[1] == "vWAAS":
		if splitbydash[2] == "150":
			capacity = "150-Users"
		elif splitbydash[2] == "200":
			capacity = "200-Users"
		elif splitbydash[2] == "750":
			capacity = "750-Users"
		elif splitbydash[2] == "1300":
			capacity = "1300-Users"
		elif splitbydash[2] == "2500":
			capacity = "2500-Users"
		elif splitbydash[2] == "6k":
			capacity = "6000-Users"
		localdotsplit = splitbydash[3].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
		if splitbydash[4] == "npe":
			imagecode = "vWAAS - VMWare-NPE"
		else:
			imagecode = "vWAAS - VMWare"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == "Hv" and splitbydash[2] == "vWAAS":
		if splitbydash[3] == "150":
			capacity = "150-Users"
		elif splitbydash[3] == "200":
			capacity = "200-Users"
		elif splitbydash[3] == "750":
			capacity = "750-Users"
		elif splitbydash[3] == "1300":
			capacity = "1300-Users"
		elif splitbydash[3] == "2500":
			capacity = "2500-Users"
		elif splitbydash[3] == "6k":
			capacity = "6000-Users"
		localdotsplit = splitbydash[4].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
#		if len(splitbydash) == "7":
#			if splitbydash[7] == "npe.zip":
		if "npe" in filename:
			imagecode = "vWAAS - HyperV-NPE"
		else:
			imagecode = "vWAAS - HyperV"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == "ISR" and splitbydash[1] == "WAAS":
		localdotsplit = splitbydash[2].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
#		if len(splitbydash) == "7":
#			if splitbydash[7] == "npe.zip":
		if "npe" in filename or  "NPE" in filename:
			imagecode = "ISR-NPE"
		else:
			imagecode = "ISR"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == "sre":
		localdotsplit = splitbydash[3].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
		if "npe" in filename or  "NPE" in filename:
			imagecode = "SM-SRE-NPE"
		else:
			imagecode = "SM-SRE"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == "alarm":
		localdotsplit = splitbydash[4].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
		if "npe" in filename or  "NPE" in filename:
			imagecode = "ALARM-ERROR BOOKS-NPE"
		else:
			imagecode = "ALARM-ERROR BOOKS"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == "WAAS" or splitbydash[0] == "waas":
		localdotsplit = splitbydash[1].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2] + "." + localdotsplit[3]
		if "sysimg" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "SYSTEM-SOFTWARE-32bit-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE-32bit"
		elif "bin" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "BOOT-NPE"
			else:
				imagecode = "BOOT"
		elif "rescue" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "RESCUE CD-NPE"
			else:
				imagecode = "RESCUE CD"
		elif "Doc" in filename or "DOC" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "DOCUMENTATION-NPE"
			else:
				imagecode = "DOCUMENTATION"
		elif "npe" in filename or  "NPE" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "SM-SRE-NPE"
			else:
				imagecode = "SM-SRE"
		elif "npe" in filename or  "NPE" in filename:
			if "npe" in filename or  "NPE" in filename:
				imagecode = "ALARM-ERROR BOOKS-NPE"
			else:
				imagecode = "ALARM-ERROR BOOKS"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

def movebyfilename (name,productname,mainversion1,mainversion2,altversion,imglookup1,imglookup2):
	#Assumes that product is defined
	print (name,end="\n")
#	print (name,end="\t")
#	print (mainversion1,end="\t")
#	print (len(mainversion1),end="\t")
##	print (mainversion2,end="\t")
#	print (len(mainversion2),end="\t")
##	print (altversion,end="\t")
#	print (len(altversion),end="\t")
##	print (imglookup1,end="\t")
#	print (len(imglookup1),end="\t")
##	print (imglookup2,end="\t")
#	print (len(imglookup2),end="\n")
	'''
		if mainversion1 and not mainversion2:
	        if altversion:
	            if imglookup1 and not imglookup2:
	                if imglookup1 == "patch":

	        else: # don't need this bit: if len(altversion) == 0:
	            if imglookup1 and imglookup2:

	            elif imglookup1 and not imglookup2:

	    if not mainversion1 and not mainversion2 and not altversion:
	            if imglookup1 and not imglookup2:

	            elif imglookup1 and imglookup2:

	        elif altversion and imglookup1:
	'''
	if mainversion1 and not mainversion2 and altversion and imglookup1 and not imglookup2:
	#1,0,1,1,0
		prodname  = product(productname)
		imagecode = imagelookup(imglookup1)
		filepath  = filepath3 (mainversion1,imagecode,altversion)
		utilssinglemove (debug1,name,prodname,filepath)
	elif not mainversion1 and not mainversion2 and altversion and imglookup1 and not imglookup2:
	#0,0,1,1,0
		prodname  = product(productname)
		imagecode = imagelookup(imglookup1)
		filepath  = filepath2 (imagecode,altversion)
		utilssinglemove (debug1,name,prodname,filepath)
	elif mainversion1 and not mainversion2 and not altversion and imglookup1 and not imglookup2:
	#1,0,0,1,0
		prodname  = product(productname)
		imagecode = imagelookup(imglookup1)
		filepath  = filepath2 (mainversion1,imagecode)
		utilssinglemove (debug1,name,prodname,filepath)
	elif mainversion1 and not mainversion2 and not altversion and imglookup1 and imglookup2:
	#1,0,0,1,1
		prodname  = product(productname)
		icode1 = imagelookup(imglookup1)
		icode2 = imagelookup(imglookup2)
		filepath  = filepath3 (mainversion1,icode1,icode2)
		utilssinglemove (debug1,name,prodname,filepath)
	elif mainversion1 and mainversion2 and not altversion and imglookup1 and not imglookup2:
	#1,1,0,1,0
		prodname  = product(productname)
		imagecode = imagelookup(imglookup1)
		filepath  = filepath3 (mainversion1,mainversion2,imagecode)
		utilssinglemove (debug1,name,prodname,filepath)


def toplevel(filename):
	src = filename
	names = os.listdir(src)
	os.chdir(src)
	
	if filefilter is not None:
		with open(filefilter) as jsonfile:
#			global loadedjson
			loadedjson = json.load(jsonfile)
#		print (loadedjson)
	for name in names:
		if filefilter is not None:
			if name in loadedjson:
				myproduct = loadedjson[name]['product']
				mainversion1 = loadedjson[name]['mainversion1']
				mainversion2 = loadedjson[name]['mainversion2']
				altversion = loadedjson[name]['altversion']
				imglookup1 = loadedjson[name]['imglookup1']
				imglookup2 = loadedjson[name]['imglookup2']
				movebyfilename (name,myproduct,mainversion1,mainversion2,altversion,imglookup1,imglookup2)
	#	else:
	names = os.listdir(src)
	for name in names:
		if os.path.isdir(name):
			continue	
		elif name.endswith(".part"):
			continue
		
		if debug0 != True:
			print(name)
		if debug1:
			print("\tModule#\t\tiossort")
			print("\tSubroutine#\ttoplevel")
		
#		if hashsha512 == True:
#			hasher = hashlib.sha512()
#			with open(name, 'rb') as afile:
#				buf = afile.read()
#				hasher.update(buf)
#			print("SHA512:", end =" ")
#			print(hasher.hexdigest())
#		if hashsha256 == True:
#			hasher = hashlib.sha256()
#			with open(name, 'rb') as afile:
#				buf = afile.read()
#				hasher.update(buf)
#			print("SHA256:", end =" ")
#			print(hasher.hexdigest())
#		if hashmd5 == True:
#			hasher = hashlib.md5()
#			with open(name, 'rb') as afile:
#				buf = afile.read()
#				hasher.update(buf)
#			print("MD5:", end =" ")
#			print(hasher.hexdigest())

		splitbydot = name.split(".")
		classify = name.split("-")
		splitbydash = name.split("-")
		splitbydashsub = splitbydot[0].split("-")
		
		thisstring = splitbydot.pop()
		splitbydot.append(thisstring)

		if (
			name == "Thumbs.db" or
			name.endswith("DS_Store") or
			name.endswith("hash") or
			name.endswith("part")
		):
			continue
		elif name == "cat9k_fpga_upgrade_utility.pdf":
			fileprocessor_iosxe(debug1,name)
		elif name == "Exp_V3_11_Release_Note.pdf":
			fileprocessorios(debug1,name)
		elif name.endswith("pdf"):
			continue

		elif (
			name in [
				"cat9k.16121.0911.bin",
				"cat9k.16121_au.bin"
				"cat9k_iosxe.V171_1S_TES2.SPA.bin",
				"cat9k_bidir_updated.bin",
				"cat9k_fraport_bidir.bin",
				"cat9k_iosxe.16.12-xFSU-eft1.bin",
				"cat9k_iosxe.16.12-xFSU-eft2.bin",
				"cat9k_iosxe.16.12-xFSU-eft3.bin",
				"cat9k_private_image_802.3bt.bin",
				"cat9k_iosxe.BLD_V171_EFT-1.SSA.bin",
				"cat9k_iosxe.BLD_V171_EFT-2.SSA.bin",
				"cat9k_iosxe.16.09.01.CSCvk69552.SPA.smu.bin",
				"cat9k_iosxe.16.09.01.CSCvk69552.SPA.smu.txt"
				] or
			name.startswith("cat9k") and "THROTTLE_LATEST" in name or
			name.startswith("cat9k") and "prd" in name or
			name.startswith("cat9k") and "eft" in name
		):
			prodname = product("cat9k")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name == "s2t54-adventerprisek9-mz.SSA"
		):
			prodname = product("s2t54")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("C9800-40-") and "THROTTLE" in name
		):
			prodname = product ("C9800-40")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)
		elif (
		name.startswith("C9800-80-") and "THROTTLE" in name
		):
			prodname = product ("C9800-80")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("C9800-L-") and "THROTTLE" in name
		):
			prodname = product ("C9800-L")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"C9800-CL-universalk9.2019-04-26_10.55_bachidam.0.CSCvo94596.SSA.apdp.bin",
				"C9800-CL-universalk9.2019-05-13_15.09_sisharm2.SSA.bin",
				"C9800-CL-universalk9.2019-05-16_19.27_sisharm2.SSA.bin",
				"C9800-CL-universalk9.2019-07-09_07.29_ghalwasi.SSA.bin",
				"C9800-CL-universalk9.2019-08-07_14.47_raghasin.SSA.bin",
				"C9800-CL-universalk9.2019-09-16_14.42_gbks.SSA.bin"
				] or
		name.startswith("C9800-CL-") and "THROTTLE" in name or
		name.startswith("C9800-CL-") and "eft" in name or
		name.startswith("C9800-CL-") and "prd" in name
		):
			prodname = product ("C9800-CL")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("C9800-SW-") and "THROTTLE" in name or
		name == "C9800-SW-iosxe-wlc.V171_1S_TES2.SPA.bin"
		):
			prodname = product ("C9800-SW")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name == "c1100-universalk9.V16_12_0_136.SSA.bin" or
		name.startswith("c1100-") and "prd" in name or
		name.startswith("c1100-") and "eft" in name
		):
			prodname = product ("c1100router")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name == "asr1000rp1-adventerprisek9.BLD_V122_33_XNC_ASR_RLS3_THROTTLE_LATEST_20090513_080032.bin" or
		name == "asr1000rp1-advipservicesk9.V152_1_S1_CSCTR15153_3.bin"
		):
			prodname = product ("asr1000rp1")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name == "asr1000rpx86-universalk9.V1612_1_CVE_2019_1649.SPA.bin"
		):
			prodname = product ("asr1000rpx86")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name == "c180x-advipservicesk9-mz.V124_15_T1-CSCsk94464-ES.bin"
		):
			prodname = product ("c180x")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"c3900e-universalk9-mz.SSA.152-4.M.CSCtw93694.bin",
				"c3900e-universalk9-mz.SSA.152-4.M.CSCtw93694_Feb16.bin",
				"c3900e-universalk9-mz.SSA.154-20160808061644.skaliath-NIGHTLY_V154_3_M_THROTTLE_201608041309-104-CSCva77149.bin",
				"c3900e-universalk9-mz.SSA.154-20160819103204.skaliath-PRE_RELEASE_FC1_V154_3_M6-105-CSCva77149.bin"
				]
		):
			prodname = product ("c3900")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"cat3k_caa-universalk9.2017-04-24_21.14_phkotamr.SSA.bin",
				"cat3k_caa-universalk9.2017-05-26_21.07_phkotamr.SSA.bin",
				"cat3k_caa-universalk9.2017-06-13_16.05_phkotamr.SSA.bin",
				"cat3k_caa-universalk9.SSA.03.07.05.E5.662.152-3.6.62.E5.bin",
				"cat3k_caa-universalk9.SSA.03.07.05.E5.662.152-3.6.62.E5.txt",
				] or
			name.startswith("cat3k") and "THROTTLE_LATEST" in name
		):
			prodname = product ("cat3k_caa")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name.startswith("isr4300") and "THROTTLE_LATEST" in name
		):
			prodname = product ("isr4300")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name.startswith("isr4400") and "THROTTLE_LATEST" in name
		):
			prodname = product ("isr4400")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"csr1000v-universalk9.16.09.01.CSCvk69552.SPA.smu.bin",
				"csr1000v-universalk9.16.09.01.CSCvk69552.txt",
				] or
			name.startswith("csr1000v") and "THROTTLE_LATEST" in name
		):
			prodname = product ("csr1000v")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name.startswith("asr1000") and "THROTTLE_LATEST" in name
		):
			prodname = product ("asr1000")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name.startswith("asr1001x") and "THROTTLE_LATEST" in name or
			name.startswith("asr1001x") and "prd" in name or
			name.startswith("asr1001x") and "eft" in name
		):
			prodname = product ("asr1000")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name.startswith("asr1002x") and "THROTTLE_LATEST" in name
		):
			prodname = product ("asr1002x")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name == "n7000-s1-epld.5.2.0.266.gimg" or
			name.startswith("dino-lisp")
		):
			prodname = product ("n7000")
			imagecode = imagelookup ("specialbuildlisp")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name == "C9100-universalk9_me.BLD_V1612_THROTTLE_LATEST_20190619_023732.zip"
		):
			prodname = product ("C9800-AP")
			imagecode = imagelookup ("specialbuild")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		".cv50." in name and name.endswith(".zip")  or
		".cv50." in name and name.endswith(".readme")  or
		".cv53." in name and name.endswith(".zip")  or
		".cv53." in name and name.endswith(".readme")  or
		".cv61." in name and name.endswith(".zip")  or
		".cv61." in name and name.endswith(".readme")  or
		"nmidb." in name and name.endswith(".zip")  or
		"nmidb." in name and name.endswith(".readme")  or
		"cvw6.1" in name and name.endswith(".tar")  or
		"cvw6.1" in name and name.endswith(".zip")  or
		".RME43." in name and name.endswith(".zip") or
		name == "Mwr1900.zip" or
		name == "CVCrossLaunch.zip" or
		name == "psumeta_cwcv6_1_5.xml" or
		name == "Cat6000IOS.zip"
		):
			prodname = product ("cworks")
			imagecode = imagelookup ("rme")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name == "VMS_2_3_DST_Patch_Windows_K9.tar"
		):
			prodname = product ("cworks")
			imagecode = imagelookup ("patch")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name == "Patch-CSCsc85405.tar.gz"
		):
			prodname = product ("perfigocca")
			imagecode = imagelookup ("patch")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"c3750-dmon-mz.122-25r.SEC",
				"c3750-dmon-mz-122-25r.SEE4",
				]
		):
			prodname = product ("c3750")
			imagecode = imagelookup ("hdiag")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
				"AnyConnect-CSA.zip",
				"CSD-for-CSA-updates.zip",
				]
		):
			prodname = product ("csa")
			imagecode = imagelookup ("export")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("i86bi") or
		name.startswith("I86BI")
		):
			prodname = product ("iou")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("vios") or
		name.startswith("vIOS")
		):
			prodname = product("vios")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("ata") or
		name.startswith("cmterm") or
		name.startswith("vgc-main") or
		name.startswith("CME") or
		name.startswith("cme")
		):
			fileprocessorvoice(debug1,name)

		elif (
		"tsjspgen" in name or
		"tpcgen" in name or
		"tpgen" in name or
		"tpcgenx" in name or
		"tscgen" in name or
		"tscgenx" in name or
		"tipv6" in name
		):
			fileprocessorpagent(name)

		elif(
			name in [
			"Rommon-123-8r.YH13-notes",
			"Rommon-124-22r.YB5-notes",
			"Rommon-151-1r.T4-notes",
			"Rommon-151-1r.T5-notes",
			"Rommon-150-1r.M12-notes",
			"asr900_15_6_43r_s_rommon.pkg",
			"ASR1000_RM_16_3_2R.bin",
			"C2400_RM2.symbols.123-7r.T2"
			] or
		"srec" in name or
		"rommon" in name or
		"ROMMON" in name or
		"promupgrade" in name or
		"governator" in name or
		"C7200_NPEG1_RM" in name or
		"C7200_NPEG2_RM" in name or
		"C7200_NPEG1_BOOT_ROM" in name or
		"c6880x_rm" in name or
		"cat6000-CPBOOT" in name or
		"tinyrom" in name or
		name.startswith("firmwareupgrade") or
		name.startswith("transformer_rm") or
		name.startswith("sup6t_rm") or
		name.startswith("asr920-rommon")
		):
			fileprocessorrommon(debug1,name)

		elif (
		name.startswith("n3000") or
		name.startswith("n3500") or
		name.startswith("n4000") or
		name.startswith("n5000") or
		name.startswith("n6000") or
		name.startswith("n7000") or
		name.startswith("n7700") or
		name.startswith("n9000") or
		name.startswith("nxosv") or
		name.startswith("nexus9300v") or
		name.startswith("nexus9500v") or
		name.startswith("nxos") or
		name.startswith("oac") or
		name.startswith("n5000_poap_script") or
		name.startswith("n6000_poap_script") or
		name.startswith("poap_script") or
		name.startswith("poap_ng") or
		name.startswith("Nexus1000v") or
		name.startswith("Nexus1000v") or
		name.startswith("Nexus1000V") or
		name.startswith("Nexus1000V5") or
		name.startswith("n1000vh-dk9") or
		name.startswith("nexus-1000v") or
		name == "n3k_bios_release_rn.pdf" or
		name.startswith("ssd_c400_upgrade") or
		name == "upgrade_m500_firmware.tar.gz" or
		name == "ntp-1.0.1-7.0.3.I2.2d.lib32_n9000.rpm" or
		name == "ntp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm" or
		name == "ntp-1.0.2-7.0.3.I2.2e.lib32_n9000.rpm" or
		name == "nxos.nsqos_lc_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm" or
		name == "nxos.nsqos_sup_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm" or
		name == "vxlan-2.0.1.0-9.2.3.lib32_n9000.rpm" or
		name == "snmp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm" or
		name == "L2-L3_CT.zip" or
		name.startswith("n9000-epld") or
		name.startswith("guestshell")
		):
			fileprocessornxos(name,debug1)

		elif (
			name in [
			"np.0.8.11.1.spe",
			"np.0.8.11.2.spe",
			"np.0.10.8.0.spe",
			"np.6.106.spe",
			"np.6.93.spe",
			"np.7.16.spe",
			"np.7.9.spe",
			"np.8.8.1.spe",
			"np.spe"
			]
		):
			prodname = product ("mica-modem")
			imagecode = imagelookup ("np")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("adsl_alc")
		):
			prodname = product ("ISRG1GENERIC")
			imagecode = imagelookup ("DSLFIRMWARE")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("8705_") or
		name.startswith("8775_") or
		name.startswith("8790_")
		):
			prodname = product ("ISRG1GENERIC")
			imagecode = imagelookup ("HWIC3GGSM")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif name.startswith("vcw-vfc-mz"):
			prodname = product ("c5350")
			imagecode = imagelookup (splitbydot[0])
			utilssinglemove (debug1,name,prodname,imagecode)

		elif name.startswith("c3600-2600-analog-fw"):
			prodname = product ("branchmodules")
			imagecode = imagelookup ("analogmodem")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
			"ASR1K-fpga_prog.16.0.1.xe.bin",
			"isr-hw-programmables.03.13.02.S.154-3.S2-ext.SPA.pkg",
			"isr-hw-programmables.03.15.03.S.155-2.S3-ext.SPA.pkg",
			"nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg",
			"nim_vab_phy_fw_A39x3_B39x3_Bond39t.pkg"
			] or
		name.endswith ("comp_matrix.xml") or
		name.startswith ("WP76xx") or
		name.startswith("C9800-") or
		name.startswith("CAT3650_WEBAUTH_BUNDLE") or
		name.startswith("CAT3850_WEBAUTH_BUNDLE") or
		name.startswith("asr1000") or
		name.startswith("asr1000rp1") or
		name.startswith("asr1000rp2") or
		name.startswith("asr1000rpx86") or
		name.startswith("asr1001") or
		name.startswith("asr1001x") or
		name.startswith("asr1002") or
		name.startswith("asr1002x") or
		name.startswith("asr900rsp1") or
		name.startswith("asr900rsp2") or
		name.startswith("asr900rsp3") or
		name.startswith("asr901") or
		name.startswith("asr901rsp1") or
		name.startswith("asr901rsp2") or
		name.startswith("asr903rsp1") or
		name.startswith("asr903rsp2") or
		name.startswith("asr920") or
		name.startswith("asr920igp") or
		name.startswith("c1100-ucmk9") or
		name.startswith("c1100-universalk9") or
		name.startswith("c1100_gfast_") or
		name.startswith("c1100_phy_") or
		name.startswith("c8000aep") or
		name.startswith("c8000be") or
		name.startswith("c8000v") or
		name.startswith("cat3k_caa") or
		name.startswith("cat4500es8") or
		name.startswith("cat9k") or
		name.startswith("csr1000v") or
		name.startswith("csr1000v_milplr") or
		name.startswith("ct5760") or
		name.startswith("ess3x00") or
		name.startswith("ie3x00") or
		name.startswith("ie9k") or
		name.startswith("iosxe-remote-mgmt") or
		name.startswith("iosxe-sd-avc") or
		name.startswith("ir1101") or
		name.startswith("isr4200") or
		name.startswith("isr4300") or
		name.startswith("isr4400") or
		name.startswith("isr4400v2") or
		name.startswith("s5800") or
		name.startswith("ttam") or
		name.startswith("vg400") or
		name.startswith("vg420") or
		name.startswith("vg450")
		):
			fileprocessor_iosxe(debug1,name)


		elif (
			name in [
			"ACS-4.1.1.23-CSTacacs-SW-CSCsg97429-Readme.txt",
			"ACS-4.1.1.23-CSTacacs-SW-CSCsg97429.zip",
			"ACS57BasePatch.tar.gz",
			"APIC_FMC_Remediation_module_1.0.1_7.tgz",
			"APIC_FMC_Remediation_module_1.0.2_1.tgz",
			"APIC_FirePOWER_Remediation_Module_2.0.1.1.tgz",
			"APIC_Secure_Firewall_Remediation_Module_2.0.2.1.tgz",
			"BOOTX64.EFI",
			"PIX_to_ASA_1_0.dmg",
			"PIXtoASA_1_0.zip",
			"PIXtoASAsetup_1_0.exe",
			"README-occ-121.rtf",
			"README_ISE_20_201_21_22",
			"README_WebAgent.txt",
			"ReadMe_for_ACS_5.6_Upgrade_Package-txt",
			"Secure_Workload_Remediation_Module_1.0.3.tgz",
			"VPN-5.0.00.0340-MSI.exe",
			"VPNDisable_ServiceProfile.xml",
			"VPN_Client_Support_Matrix2.txt",
			"Vista-VPN-Troubleshooting.txt",
			"WebSecurityCert.zip",
			"anyconnect_app_selector_1.0.zip",
			"anyconnect_app_selector_2.0.zip",
			"cisco_vpn_auth.jar",
			"citrix_plugin_howto.doc",
			"cvdm-css-1.0.zip",
			"cvdm-css-1.0_K9.zip",
			"fcs-csa-hotfix-5.2.0.238-w2k3-k9-CSM.zip",
			"fcs-csamc-4.5.1.616-CSA-Policy-Descriptions.zip",
			"firepower-mibs.zip",
			"grub.efi",
			"occ-121.gz",
			"occ-121.zip",
			"pic-2.2.0.470.SPA.x86_64.iso",
			"pic-2.4.0.357.SPA.x86_64.iso",
			"pnLogAgent_1.1.zip",
			"pnLogAgent_4-1-3.zip",
			"pnLogAgent_4-1-3.zip.txt",
			"pxGrid_Mitigation_Remediation_v1.0.tgz",
			"rawrite.exe",
			"rdp_09.11.2012.jar",
			"release_duration_tool.tar",
			"vpn30xxboot-4.0.Rel.hex",
			"webAgent_1-0.zip",
			"webAgent_1-0.zip.txt",
			"webAgent_1-1.zip",
			"webAgent_1-1.zip.txt"
			] or
		name.startswith("128MB.sdf") or
		name.startswith("256MB.sdf") or
		name.startswith("5-") or
		name.startswith("ACS") or
		name.startswith("Acs") or
		name.startswith("CSCvn17524") or
		name.startswith("CSM4") and name.endswith("Service_Pack1.exe") or
		name.startswith("CSM4") and name.endswith("Service_Pack2.exe") or
		name.startswith("CUCM-CSA-") or
		name.startswith("CiscoCM-CSA-") or
		name.startswith("CiscoCVP-CSA-") or
		name.startswith("CiscoICM-CSA-") or
		name.startswith("CiscoISE") or
		name.startswith("CiscoISN-CSA-") or
		name.startswith("CiscoPA-CSA-") or
		name.startswith("CiscoUnity-CSA-") or
		name.startswith("Cisco_FTD") or
		name.startswith("Cisco_Firepower") or
		name.startswith("Cisco_Firepower_GEODB") or
		name.startswith("Cisco_Firepower_SRU") or
		name.startswith("Cisco_Firepower_Threat") or
		name.startswith("Cisco_Network_Sensor") or
		name.startswith("Cisco_VDB_Fingerprint_Database") or
		name.startswith("Clean") or
		name.startswith("FMT-CP-Config-Extractor") or
		name.startswith("Firepower") or
		name.startswith("Firepower_Migration_Tool") or
		name.startswith("IDS") or
		name.startswith("IDS-sig-") and name.endswith(".readme.txt") or
		name.startswith("IDS-sig-") and name.endswith(".zip") or
		name.startswith("IOS-S") and name.endswith("-CLI.pkg") or
		name.startswith("IOS-S") and name.endswith(".zip") or
		name.startswith("IPS") or
		name.startswith("ISE") or
		name.startswith("PIX") and name.endswith(".bin") or
		name.startswith("PIX") or
		name.startswith("SNS-35x5-BIOS") or
		name.startswith("SNS-35x5-firmware") or
		name.startswith("SNS-36xx-BIOS") or
		name.startswith("SNS-36xx-HUU") or
		name.startswith("SNS-36xx-firmware") or
		name.startswith("Sourcefire") or
		name.startswith("UCP") or
		name.startswith("UTD-STD-SIGNATURE") or
		name.startswith("VPN3000") or
		name.startswith("anyconnect") or
		name.startswith("applAcs") or
		name.startswith("asa") or
		name.startswith("asasfr") or
		name.startswith("asdm") or
		name.startswith("bh") and name.endswith(".bin") or
		name.startswith("c6svc-fwm-k9") or
		name.startswith("cda") and name.endswith("iso") or
		name.startswith("cisco-asa") or
		name.startswith("cisco-ftd") or
		name.startswith("cisco-secure-client") or
		name.startswith("coeus") or
		name.startswith("csd") or
		name.startswith("csm") or
		name.startswith("csm-maxmind-geolitecity-") or
		name.startswith("csmars") or
		name.startswith("external-sso") or
		name.startswith("fcs-CSM") or
		name.startswith("fcs-cms") or
		name.startswith("fcs-csamc") or
		name.startswith("fcs-csm") or
		name.startswith("fcs-mcp") or
		name.startswith("fcs-rme") or
		name.startswith("firepower") or
		name.startswith("ftd") or
		name.startswith("fwsm_migration") or
		name.startswith("fxos") or
		name.startswith("hostscan") or
		name.startswith("iosxe-utd") or
		name.startswith("iosxe-utd-ips") or
		name.startswith("iox-iosxe-utd") or
		name.startswith("ise") or
		name.startswith("ise-pic") or
		name.startswith("lsp-rel-") or
		name.startswith("mac-spw-dmg") or
		name.startswith("np") and name.endswith(".bin") or
		name.startswith("pdm") and name.endswith(".bin") or
		name.startswith("phoebe") or
		name.startswith("pix") and name.endswith(".bin") or
		name.startswith("pix") or
		name.startswith("sampleTransforms") or
		name.startswith("secapp-ucmk9") or
		name.startswith("secapp-utd") or
		name.startswith("sg") and name.endswith("adi") or
		name.startswith("sg") and name.endswith("adi-gz") or
		name.startswith("sg") and name.endswith("zip") or
		name.startswith("thirdparty") or
		name.startswith("tools-anyconnect") or
		name.startswith("tools-cisco-secure-client") or
		name.startswith("upd-pkg-SNS-35x5-cimc") or
		name.startswith("upd-pkg-SNS-36xx-cimc") or
		name.startswith("update-") and name.endswith ("-major-K9.zip") or
		name.startswith("vpn3000") or
		name.startswith("vpn3002") or
		name.startswith("vpn3005") or
		name.startswith("vpnclient") or
		name.startswith("webagent") or
		name.startswith("win_spw") or
		name.startswith("zeus")
		):
			fileprocessorsecurity(debug1,name,filename)

		elif (
			name in [
			"1X0DBIOSv4.8",
			"1X0SBIOSv4.8",
			"B57BCMCD_v15.2.4.1.tgz",
			"B57CiscoCD_T6.4.4.3-57712.zip",
			"BashFix-update-0-x86_64.tar.gz",
			"CSCwb00526.sh",
			"CSCwb00526.sh.zip", 
			"DW_16MB_release_1029.bin",
			"DW_BIOS.bin.SPA",
			"DW_Signed_Bios_Image.bin.SPA",
			"Datacenter_Technology_Pack-1.0.53.ubf",
			"Datacenter_Technology_Pack_Update_1_Patch-1.0.58.ubf",
			"GlibcFix-pi22-update-0-x86_64.tar.gz",
			"InstallerUpdateBE-1.0.5.tar.gz",
			"Intel_Windows_drv_MR_6.714.18.00_pv.zip",
			"JeOS_Patch_To_Enable_ASD.zip",
			"LSI_x64_Signed_Driver_5.2.116.64.zip",
			"MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip",
			"PrimeInfra.pem",
			"SW_16MB_release_1102.bin",
			"SW_Signed_Bios_Image.bin.SPA",
			"Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA",
			"Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA",
			"Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA",
			"Signed_DW_M1M2_Bios_Image_041015.bin.SPA",
			"Signed_EN_BIOS_1.5.0.4.bin.SPA",
			"Signed_EN_BIOS_1.5.0.5.bin.SPA",
			"Signed_EN_BIOS_1.5.0.6.bin.SPA",
			"Signed_SW_M2_BIOS_1.5.0.6.bin.SPA",
			"Signed_SW_M2_BIOS_1.5.0.7.bin.SPA",
			"Signed_SW_M2_BIOS_1.5.0.8.bin.SPA",
			"Signed_SW_M2_Bios_1.5.0.5.bin.SPA",
			"UCSEDM3_BIOS_2.4.SPA",
			"UCSEDM3_BIOS_2.5.SPA",
			"UCSEDM3_BIOS_2.6.SPA",
			"UCSE_CIMC_2.3.1.bin",
			"UCSE_CIMC_2.3.2.bin",
			"UCSE_CIMC_2.3.3.bin",
			"UCSE_CIMC_2.3.5.bin",
			"UCS_docs_20110510.iso",
			"b2xx-m1-drivers-1.1.1j.iso",
			"c2xx-m1-utils-1.0.2.iso",
			"ca_technology_package-2.1.0.0.41.ubf",
			"cspc28backupscript.zip",
			"efi-obd-v12-07-18.diag",
			"efi-obd-v13-10-15.diag",
			"efi-obd-v13-7-3.diag",
			"huu-2.3.1.iso",
			"huu-2.3.2.iso",
			"huu-2.3.3.iso",
			"huu-2.4.1.iso",
			"huu-3.0.1.iso",
			"huu-3.1.1.iso",
			"huu_3.1.2.iso",
			"huu_3.1.3.iso",
			"huu_3.1.4.iso",
			"huu_3.2.6.v3.iso",
			"intel9.2.3.1023.tar",
			"operations_center_pi_2_1_2_enable_update.ubf",
			"pi212_20141118_01.ubf",
			"pi212_PIGEN_CSCur43834_01.ubf",
			"readme_10.2.1.ST.1",
			"rhel-vulnerability-patch-pnp-2.2.0.14.tar.gz",
			"rste_4.5.0.1335_install.zip",
			"ucse-huu-2.1.1.iso",
			"update_pkg-Mar-22-MR-rebuild.bin",
			"update_pkg-ucse.combined.120808.bin",
			"update_pkg-ucse.combined.REL.2.2.1.bin",
			"update_pkg-ucse.combined.REL.2.2.2.bin",
			"update_pkg-ucse.combined.REL.bin"
			] or
		name.startswith("APIC-EM-") or
		name.startswith("C200M1-") or
		name.startswith("CIMC_") and name.endswith(".bin") or
		name.startswith("CSLU_Installer") or
		name.startswith("Cisco-HX-Data-Platform-Installer") or
		name.startswith("CiscoPI") or
		name.startswith("CiscoPI3.4.pem") or
		name.startswith("CiscoPI3.5.pem") or
		name.startswith("Cisco_ACI") or
		name.startswith("Collector") or
		name.startswith("DCNM") or
		name.startswith("DNAC-") or
		name.startswith("Device-Pack") or
		name.startswith("DnacPreCheckASSESMENTUbf") or
		name.startswith("HX-ESXi") or
		name.startswith("HX-Kubernetes") or
		name.startswith("HxClone-HyperV") or
		name.startswith("HyperFlex-VC-HTML") or
		name.startswith("HyperFlex-Witness-") or
		name.startswith("PI") or
		name.startswith("PI-APL-") or
		name.startswith("PI-UCS-APL-") or
		name.startswith("PI-Upgrade-") or
		name.startswith("PI-VA-") or
		name.startswith("PNP-GATEWAY-VM-") or
		name.startswith("SSMS") or
		name.startswith("SSM_On-Prem") or
		name.startswith("UCSC-C220-M5-") or
		name.startswith("UCSC-C240-M5-") or
		name.startswith("aci-apic") or
		name.startswith("aci-msft-pkg") or
		name.startswith("aci-n9000-dk9") or
		name.startswith("aci-simulator") or
		name.startswith("aci-vpod") or
		name.startswith("acisim") or
		name.startswith("apic-vrealize") or
		name.startswith("apic_em_update-apic-") or
		name.startswith("cisco-HX-Data-Platform-Installer") or
		name.startswith("cisco-prime-pnp") or
		name.startswith("cisco-prime-pnp-app-k9-") or
		name.startswith("collector") or
		name.startswith("dcnm") or
		name.startswith("delnorte") or
		name.startswith("delnorte2") or
		name.startswith("dnac") or
		name.startswith("esx-msc") or
		name.startswith("hostUpgrade_v") or
		name.startswith("hostupgrade_v") or
		name.startswith("hxcsi") or
		name.startswith("msc") or
		name.startswith("pi") or
		name.startswith("pid-ctlg") or
		name.startswith("plumas") or
		name.startswith("plumas2") or
		name.startswith("pnp-") or
		name.startswith("ssms") or
		name.startswith("storfs-packages") or
		name.startswith("tools-msc") or
		name.startswith("ucs") or
		name.startswith("ucs-cxx") or
		name.startswith("update_pkg-ucse") or
		name.startswith("vcenter-plugin")
		):
			file_proc_servers(name,debug1)

		elif (
			name in [
			"xrvr-fullk9-4.3.2.vmdk",
			"xrvr-full-4.3.2.vmdk",
			"xrv9k-fullk9-x.qcow2-6.0.0"
			] or
		name.startswith("ASR9K") or
		name.startswith("ASR9k") or
		name.startswith("CSM.zip") or
		name.startswith("Cisco_TMS_") or
		name.startswith("SP_") or
		name.startswith("Sightline") or
		name.startswith("TMS_") or
		name.startswith("XR12000") or
		name.startswith("XRV9000") or
		name.startswith("XRV9K") or
		name.startswith("asr9k") or
		name.startswith("csm-") or
		name.startswith("csm-3.5.2.zip") or
		name.startswith("csm-4.0.zip") or
		name.startswith("fullk9-R-XRV9000") or
		name.startswith("iosxrv") or
		name.startswith("xrv9k")
		):
			fileprocessor_iosxr(debug1,name)

		elif (
			name in [
			"2730_rel_note",
			"Exp_V3_11.axf",
			"Exp_v10_10.spe",
			"Release-Notes-V3.12.1",
			"Release-Notes-V3.12.2",
			"fw_upgrade.tcl",
			"portware.2730.ios",
			"sconvertit0-11.tar",
			"sconvertit0-12.tar",
			"sprint_v16904_package.tar",
			"wconvertit0-11.zip",
			"wconvertit0-12.zip"
			] or
		name.startswith("6509neba") or
		name.startswith("6516agbic") or
		name.startswith("6548getx") or
		name.startswith("66748getx") or
		name.startswith("MC7304") and name.endswith ("spk") or
		name.startswith("MC7350") and name.endswith ("spk") or
		name.startswith("MC7354") and name.endswith ("spk") or
		name.startswith("MC735X") and name.endswith ("spk") or
		name.startswith("MC7700") or
		name.startswith("MC7710") or
		name.startswith("MC7750") or
		name.startswith("V3_") and name.endswith ("axf") or
		name.startswith("VAE2_") and name.endswith ("bin") or
		name.startswith("VAEW_") and name.endswith ("bin") or
		name.startswith("VA_") or
		name.startswith("c2900XL") or
		name.startswith("c2900xl") or
		name.startswith("c3500XL") or
		name.startswith("c3500xl") or
		name.startswith("epld-6548getx") or
		name.startswith("epld-sup2") or
		name.startswith("mica-modem-pw") or
		name.startswith("mica-pw") or
		name.startswith("sprom") or
		name.startswith("vdsl.bin")
		):
			fileprocessorios(debug1,name)

		elif (
		name.startswith("CUMC")
		):
			continue

		elif (
			name in [
			"Cisco_usbconsole_driver.zip",
			"Cisco_usbconsole_driver_3_1.zip",
			"asr-9xx_usbconsole_drivers.zip"
			]
		):
			prodname = product ("usbconsole")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("8705_") or
		name.startswith("8775_") or
		name.startswith("8790_")
		):
			continue

		elif (
		name.startswith("vios")
		):
			continue

		elif (
		name == "p1021_c800.V1.1.0.bin" or
		name == "PRL_60779.prl"
		):
			continue

		elif (
		name == "all-in-one-VM-1.2.1-194.ova" or
		name == "all-in-one-VM-1.3.0.181.ova"
		):
			prodname = product ("onepk")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("cat1900")
		):
			prodname = product ("cat1900")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("cat2800") or
		name.startswith("cat2820")
		):
			prodname = product ("cat2800")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name == "README.SWT"
		):
			prodname = product ("cat1600")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name == "epsboot.ima"
		):
			prodname = product ("cat3000")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("CPO") and name.endswith("zip") or
		name.startswith("MIBS") or
		name.startswith("SDM-V25.zip") or
		name.startswith("c6svc-nam") or
		name.startswith("ciscocm") or
		name.startswith("copfiles_iOS96.zip") or
		name.startswith("s52000tc") or
		name.startswith("sdmv10.zip") or
		name.startswith("uccx")
		):
			continue

		elif (
		name.startswith("axsm_") or
		name.startswith("axsmxg_") or
		name.startswith("pxm45_") or
		name == "mgx8880rel5600mib.tar"
		):
			#MGX8850
			continue

		elif (
		name.startswith("Sx500") or
		name.startswith("Sx350") or
		name.startswith("Sx300") or
		name.startswith("Sx250") or
		name.startswith("Sx220") or
		name.startswith("Sx200") or
		name.startswith("MIBs_Sx500") or
		name.startswith("SPA30x_SPA50x_") or
		name.startswith("AP541N-K9")
		):
			prodname = product ("smallbusiness")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("c1200-k9") or
		name.startswith("c1200-rcvk9w8") or
		name.startswith("c1100-k9") or
		name.startswith("c1100-rcvk9w8")
		):
			fileprocessorios (debug1,name)

		elif (
		name.startswith("c1200") or
		name.startswith("dmp") or
		name.startswith("nmp")
		):
			prodname = product ("cat1200")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name == "c3750-dmon-mz-122-25r.SEE4" or
		name == "c3750-dmon-mz.122-25r.SEC"
		):
			prodname = product ("c3750")
			imagecode = imagelookup ("hdiag")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
			"17_1_1t_mib.zip",
			"17_2_1_mib.zip",
			"17_2_1a_mib.zip",
			"mibs_1610.zip",
			"mibs_1611.zip",
			"mibs_16121.zip",
			"mibs_16121s.zip",
			"mibs_16121t.zip",
			"mibs_16122s.zip",
			"mibs_16123.zip",
			"mibs_16124a.zip",
			"mibs_16125.zip"
			] or
		name.startswith ("Standard-MIBS-Cisco_")
		):
			prodname = product ("wireless")
			imagecode = imagelookup ("mibs")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
			name in [
			"AP350-Cisco-IOS-Upgrade-Image-v2.img",
			"AP1200-Cisco-IOS-Upgrade-Image-v3.img",
			"Aironet-AP-Cisco-IOS-Conversion-Tool-v2.1.exe",
			"webauth_bundle-1.0.2.zip"
			] or
		name.startswith ("c1100") or
		name.startswith ("AIR") or
		name.startswith ("SWISMK9") or
		name.startswith ("SWLC3750K9") or
		name.startswith ("AIR_CTVM_LARGE-K9") or
		name.startswith ("AIR_CTVM-K9") or
		name.startswith ("MFG_CTVM") or
		name.startswith ("AP_BUNDLE") or
		name.startswith ("WCS-STANDARD-K9") or
		name.startswith ("ISR-AP1100AC") or
		name.startswith ("CiscoAironet-AP-to-LWAPP-Upgrade-Tool") or
		name.startswith ("BR350") and name.endswith ("exe") or
		name.startswith ("WGB350") and name.endswith ("exe")
		):
			fileprocessor_wireless(debug1,name)

		elif (
		name.startswith ("m9000") or
		name.startswith ("m9100") or
		name.startswith ("m9200") or
		name.startswith ("m9250") or
		name.startswith ("m9300") or
		name.startswith ("m9500") or
		name.startswith ("m9700")
		):
			fileprocessornxos(name,debug1)

		elif (
		name == "CPUpdate.xml" or
		name.startswith("Cisco-config-pro") or
		name.startswith("cisco-config-pro")
		):
			prodname = product ("ccp")
			utilssingleprodname (debug1,name,prodname)

		elif (
		name == "cna-1_0-windows-k9-installer.1-0-1a.exe" or
		name.startswith("cna-mac-k9") or
		name.startswith("cna-windows-k9")
		):
			prodname = product ("cna")
			utilssingleprodname (debug1,name,prodname)

#		elif (
#		name == "SDM-V25.zip"
#		):
#			continue
#			prodname = product ("ccp")
#			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("c1000-cwml") or
		name.startswith("c2960-cwml") or
		name.startswith("c2960c405-cwml") or
		name.startswith("c2960cx-cwml") or
		name.startswith("c2960l-cwml") or
		name.startswith("c2960x-cwml") or
		name.startswith("c3560cx-cwml") or 
		name.startswith("cdb-cwml")
		):
			prodname = product ("ccpc")
			utilssingleprodname (debug1,name,prodname)

		elif splitbydot[0] == "c675" or splitbydot[1] == "c675":
			filepath = "Other"
			filemove (filepath, name)

		elif splitbydot[0] == "c678cap" or splitbydot[1] == "c678cap":
			filepath = "Other"
			filemove (filepath, name)

		elif splitbydot[0] == "c678dmt" or splitbydot[1] == "c678dmt":
			filepath = "Other"
			filemove (filepath, name)

		elif splitbydot[0] == "spa-fpd":
			thistemp = splitbydot[0]
			splitbydashsub = thistemp.split("-")
			imagecode = imagelookup (splitbydashsub[1])
			prodname = product (splitbydashsub[0])
			fileprocessorios (debug1,name)

		elif splitbydot[0] == "dsc-c5800-mz":
			imagecode = imagelookup (splitbydash[0])
			prodname = product (splitbydash[1])
			fileprocessorios (debug1,name)

		elif splitbydot[0] == "c10k-fpd-pkg":
			prodname = product ("c10k")
			imagecode = imagelookup (splitbydash[1])
			fileprocessorios (debug1,name)

		elif (
		name.startswith("pp-adv")
		):
			nbar (name)

		elif (
		name.startswith("xcpa")
		):
			nbar (name)

		elif (
		name.startswith("s6523-mp001")
		):
			prodname = product ("s6523")
			imagecode = imagelookup ("mpatch")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("s3223-mp001")
		):
			prodname = product ("s3223")
			imagecode = imagelookup ("mpatch")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif (
		name.startswith("s72033-mp001")
		):
			prodname = product ("s72033")
			imagecode = imagelookup ("mpatch")
			utilssinglemove (debug1,name,prodname,imagecode)

		elif name.startswith("cat4000."):
			prodname = product ("cat4000")
			imagecode = imagelookup ("sup")
			workname = name.replace(".bin","")
			workname = workname.replace("cat4000.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat4000-cv."):
			prodname = product ("cat4000")
			imagecode = imagelookup ("supcv")
			workname = name.replace(".bin","")
			workname = workname.replace("cat4000-cv.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat4000-k8."):
			prodname = product ("cat4000")
			imagecode = imagelookup ("supk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat4000-k8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat4000-k9."):
			prodname = product ("cat4000")
			imagecode = imagelookup ("supk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat4000-k9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-supg."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("supg")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-supg.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-supgk9."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("supgk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-supgk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("sup")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup3."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("supg")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup3.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup8m."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("sup8m")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup8m.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-atm."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("m")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-atm.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup3cv."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("sup3cv")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup3cv.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup3cvk9."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("sup3cvk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup3cvk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat5000-sup3k9."):
			prodname = product ("cat5000")
			imagecode = imagelookup ("sup3k9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat5000-sup3k9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-supcv."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("supcv")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-supcv.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-supcvk8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("supcvk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-supcvk8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-supcvk9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("supcvk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-supcvk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-supk8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("supk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-supk8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-supk9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("supk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-supk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2cv."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2cv")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2cv.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2cvk8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2cvk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2cvk8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2cvk9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2cvk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2cvk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2k8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2k8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2k8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup2k9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup2k9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup2k9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup32pfc3cvk8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup32pfc3cvk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup32pfc3cvk8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup32pfc3cvk9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup32pfc3cvk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup32pfc3cvk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup32pfc3k8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup32pfc3k8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup32pfc3k8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup32pfc3k9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup32pfc3k9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup32pfc3k9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup720cvk8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup720cvk8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup720cvk8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup720cvk9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup720cvk9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup720cvk9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup720k8."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup720k8")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup720k8.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat6000-sup720k9."):
			prodname = product ("cat6000")
			imagecode = imagelookup ("sup720k9")
			workname = name.replace(".bin","")
			workname = workname.replace("cat6000-sup720k9.","")
			utils_dev_imagecode_v2_vf_dash (debug1,name,prodname,imagecode,workname)

		elif name.startswith("cat4500e"):
			if "SPA" in name:
				fileprocessor_iosxe(debug1,name)
			else:
				fileprocessorios (debug1,name)

		elif name.startswith("mre_workflow_signed"):
			continue

		else:
			fileprocessorios (debug1,name)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--directory',       help='Directory to sort', required=True)
#	parser.add_argument('-hs','--hashsha512',     help='Hash File using the SHA 512 Algorithm', action='store_true', required=False)
#	parser.add_argument('-hs1','--hashsha256',    help='Hash File using the SHA 256 Algorithm', action='store_true', required=False)
#	parser.add_argument('-hs3','--hashmd5',       help='Hash File using the MD5 Algorithm', action='store_true', required=False)
#	parser.add_argument('-hf','--hashfile',       help='File with Hash Info. Format is FILENAME,MD5HASH,SHA512HASH. Additional columns are ignored', action='store_true', required=False)
	parser.add_argument('-d0','--debug0',         help='Debug Level 0 (No Output) (NYI)', action='store_true', required=False)
	parser.add_argument('-d1','--debug1',         help='Print Debug Commands (Level 1) (partially implemented)', action='store_true', required=False)
#	parser.add_argument('-ff','--filefilter',     help='First Run moves files based on json file.', action='store_true', required=False)
#	parser.add_argument('-ff','--filefilter',     help='Sort files based on json.', type=ascii, required=False)
	parser.add_argument('-ff','--filefilter',     help='Sort files based on json.', required=False)
	
	global dirpass
#	global hashsha512
#	global hashsha256
#	global hashmd5
#	global hashfile
	global debug1
	global debug0
	global filefilter
#	global filefiltername

	args = parser.parse_args()
	dirpass        = args.directory
#	hashsha512     = args.hashsha512
#	hashsha256     = args.hashsha256
#	hashmd5        = args.hashmd5
#	hashfile       = args.hashfile
	debug1         = args.debug1
	debug0         = args.debug0
	filefilter     = args.filefilter
#	filefiltername = args.filefiltername
	

	toplevel(dirpass)
