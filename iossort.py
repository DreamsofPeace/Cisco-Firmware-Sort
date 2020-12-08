import os, shutil, sys, re, getopt, argparse
import hashlib
from iosutils import product,imagelookup,iostrain,utilssinglemove,utilssingleprodname
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat,messageunknownfile
from iosutils import fileprocessorpagent,fileprocessorrommon
from ios_nexus import fileprocessornxos
from ios_voice import fileprocessorvoice
from ios_security import fileprocessorsecurity
from ios_iosxe import fileprocessor_iosxe
from ios_iosxr import fileprocessor_iosxr
from ios_servers import file_proc_servers
from ios_ios import fileprocessorios
from ios_wireless import fileprocessor_wireless

def catos (filename):
	array = filename.split(".")
	version = array[1].split("-")
	mainver = util2digit(version[0],version[1])
	fullver = util3digit(version[0],version[1],version[2])
	if array[0] == "cat4000":
		prodname = product ("cat4000s12")
		imagecode = "SUP-I-II"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat4000-cv":
		prodname = product ("cat4000s12")
		imagecode = "SUP-I-II-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat4000-k8":
		prodname = product ("cat4000s12")
		imagecode = "SUP-I-II"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat4000-k9":
		prodname = product ("cat4000s12")
		imagecode = "SUP-I-II-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-supg":
		prodname = product ("cat5000")
		imagecode = "SUP-III"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-supgk9":
		prodname = product ("cat5000")
		imagecode = "SUP-III-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup":
		prodname = product ("cat5000")
		imagecode = "SUP-II-G"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-supk9":
		prodname = product ("cat5000")
		imagecode = "SUP-II-G-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup3":
		prodname = product ("cat5000")
		imagecode = "SUP-III-G"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup3k9":
		prodname = product ("cat5000")
		imagecode = "SUP-III-G-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup3cv":
		prodname = product ("cat5000")
		imagecode = "SUP-III-G-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup3cvk9":
		prodname = product ("cat5000")
		imagecode = "SUP-III-G-WITH-SSH-AND-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-atm":
		prodname = product ("cat5000")
		imagecode = "ATM-MODULE"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat5000-sup8m":
		prodname = product ("cat5000")
		imagecode = "SUP-8M"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup2":
		prodname = product ("cat6000")
		imagecode = "SUP-2"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup2cv":
		prodname = product ("cat6000")
		imagecode = "SUP-2-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup2k8" or array[0] == "cat6000-sup2k9":
		prodname = product ("cat6000")
		imagecode = "SUP-2-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup2cvk8" or array[0] == "cat6000-sup2cvk9":
		prodname = product ("cat6000")
		imagecode = "SUP-2-WITH-SSH-AND-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup":
		prodname = product ("cat6000")
		imagecode = "SUP-1"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-supcv":
		prodname = product ("cat6000")
		imagecode = "SUP-1-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-supk8" or array[0] == "cat6000-supk9":
		prodname = product ("cat6000")
		imagecode = "SUP-1-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-supcvk8" or array[0] == "cat6000-supcvk9":
		prodname = product ("cat6000")
		imagecode = "SUP-1-WITH-SSH-AND-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup720k8":
		prodname = product ("cat6000")
		imagecode = "SUP-720"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup720cvk8":
		prodname = product ("cat6000")
		imagecode = "SUP-720-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup720k9":
		prodname = product ("cat6000")
		imagecode = "SUP-720-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup720cvk9":
		prodname = product ("cat6000")
		imagecode = "SUP-720-WITH-SSH-AND-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup32pfc3k8":
		prodname = product ("cat6000")
		imagecode = "SUP-32"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup32pfc3cvk8":
		prodname = product ("cat6000")
		imagecode = "SUP-32-WITH-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup32pfc3k9":
		prodname = product ("cat6000")
		imagecode = "SUP-32-WITH-SSH"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	elif array[0] == "cat6000-sup32pfc3cvk9":
		prodname = product ("cat6000")
		imagecode = "SUP-32-WITH-SSH-AND-CISCOVIEW"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
	filemove (filepath, filename)

def nbar2 (filename):
	product = "NBAR2"
	splitbydash = filename.split("-")
	if splitbydash[2] == "asr1k":
		nbarsixteen (filename)
	elif splitbydash[2] == "csr1000v":
		nbarsixteen (filename)
	elif splitbydash[2] == "isr4000":
		nbarsixteen (filename)
	elif splitbydash[2] == "isr4451":
		nbarsixteen (filename)
	elif splitbydash[2] == "isr1100":
		nbarsixteen (filename)
	elif splitbydash[2] == "asr1k":
		nbarsixteen (filename)
	elif splitbydash[2] == "isrg2":
		nbarsixteen (filename)
	elif splitbydash[2] == "cat3k":
		nbarsixteen (filename)
	elif splitbydash[2] == "cat9k":
		nbarsixteen (filename)

def nbarsixteen (filename):
	product = "NBAR2"
	splitbydash = filename.split("-")

	if splitbydash[2] == "asr1k":
		nbarclassification (filename,"NBAR2","ASR-1K")
	elif splitbydash[2] == "csr1000v":
		nbarclassification (filename,"NBAR2","CSR-1000V")
	elif splitbydash[2] == "isr4000":
		nbarclassification (filename,"NBAR2","ISR-4000")
	elif splitbydash[2] == "isr4451":
		nbarclassification (filename,"NBAR2","ISR-4000")
	elif splitbydash[2] == "isr1100":
		nbarclassification (filename,"NBAR2","ISR-1100")
	elif splitbydash[2] == "asr1k":
		nbarclassification (filename,"NBAR2","ASR-1K")
	elif splitbydash[2] == "isrg2":
		nbarclassification (filename,"NBAR2","ISR-G2")
	elif splitbydash[2] == "cat3k":
		nbarclassification (filename,"NBAR2","CAT-3K")
	elif splitbydash[2] == "cat9k":
		nbarclassification (filename,"NBAR2","CAT-9K")

def nbarclassification (filename,product,prodcode):
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")

	if prodcode == "ASR-1K" or prodcode == "CSR-1000V" or prodcode == "ISR-4000" or prodcode == "CAT-3K" or prodcode == "CAT-9K" or prodcode == "ISR-1100":
		if splitbydash[3] == "152" or splitbydash[3] == "153" or splitbydash[3] == "154" or splitbydash[3] == "155":
			listver = list(splitbydash[3])
			splitbydash[6] = splitbydash[6].replace(".pack","")
			fullver = splitbydash[6] + "-" + listver[0] + listver[1] + "." + listver[1] + "-" + splitbydash[4]
			filepath = product + "/" + prodcode + "/" + fullver
			filemove (filepath, filename)
		else:
			main1 = list(splitbydash[3])
			if splitbydash[3] == "1612.1a":
				majorversion = "16.12.1a"
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + "/" + prodcode + "/" + nbarversion[5] + "-" + majorversion
				filemove (filepath, filename)
			elif splitbydash[3] == "1612.1":
				majorversion = "16.12.1"
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + "/" + prodcode + "/" + nbarversion[5] + "-" + majorversion
				filemove (filepath, filename)
			else:
				majorversion = main1[0] + main1[1] + "." + main1[2] + "." + main1[4]
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + "/" + prodcode + "/" + nbarversion[5] + "-" + majorversion
				filemove (filepath, filename)
	elif filename == "pp-adv-isrg2-153-1.T-3.1.0.pack":
		filepath = product + "/" + prodcode + "/" + "3.1.0-153-1.T"
		filemove (filepath, filename)
	elif prodcode == "ISR-G2":
		workname = filename.replace("pp-adv-isrg2-","")
		workname = workname.replace(".pack","")
		spdash = workname.split("-")
		filepath = product + "/" + prodcode + "/" + spdash[3] + "-" + spdash[0] + "-" + spdash[1]
		filemove (filepath, filename)
	else:
		main1 = list(splitbydash[3])
		if splitbydash[3].startswith("1612"):
			majorversion = main1[0] + main1[1] + "." + main1[2] + main1[3]
		else:
			majorversion = main1[0] + main1[1] + "." + main1[2]
		minorversion = splitbydash[4].split(".")
		nbarversion = filename.replace(".pack","")
		nbarversion = nbarversion.split("-")
		filepath = product + "/" + prodcode + "/" + nbarversion[5] + "-" + majorversion+ "." + main1[4]
		filemove (filepath, filename)

def ipsrecovery (filename):
	product = "IPS"
	imagecode = "RECOVERY IMAGE"
	splitbydash = filename.split("-")
	if filename == "IPS-K9-r-1.1-a-5.0-1.pkg":
		filepath = product + "/E0/5.0(1)/" + imagecode
	else:
		version = splitbydash[5] + "(" + splitbydash[6] + ")"
		engine = splitbydash[7].split(".")
		filepath = product + "/" + engine[0] + "/" + version + "/" + imagecode
	filemove (filepath, filename)

def ipssig (filename):
	product = "IPS"
	imagecode = "SIGNATURES"
	splitbydash = filename.split("-")
	version = splitbydash[2]
	engine = splitbydash[4].split(".")
	filepath = product + "/" + engine[0] + "/" + imagecode + "/" + version
	filemove (filepath, filename)

def ipssystem (filename):
	product = "IPS"
	imagecode = "SYSTEM UPGRADE"
	splitbydash = filename.split("-")
	if splitbydash[2] == "sp":
		splitbydot = splitbydash[4].split(".")
		version = splitbydash[3] + "(" + splitbydot[0] + ")"
		filepath = product + "/" + "E0" + "/" + version + "/" + imagecode
	else:
		version = splitbydash[2] + "(" + splitbydash[3] + ")"
		engine = splitbydash[4].split(".")
		filepath = product + "/" + engine[0] + "/" + version + "/" + imagecode
	filemove (filepath, filename)

def waas (filename):
	prodname = "WAAS"
	splitbydot = name.split(".")
	splitbydash = name.split("-")

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
			if "npe" in name or  "NPE" in name:
				imagecode = "SYSTEM-SOFTWARE-32bit-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE-32bit"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "accelerator":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = "ACCELERATOR-NPE"
			else:
				imagecode = "ACCELERATOR"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "kdump" and splitbydash[2] == "addon":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = "KDUMP-ADDON-NPE"
			else:
				imagecode = "KDUMP-ADDON"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "kdump":
			localdotsplit = splitbydash[2].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = "KDUMP-NPE"
			else:
				imagecode = "KDUMP"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "rescue" and splitbydash[2] == "cdrom":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = "RESCUE-CD-NPE"
			else:
				imagecode = "RESCUE-CD"
			filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == "rescue" and splitbydash[2] == "cdrom":
			localdotsplit = splitbydash[3].split(".")
			mainver = localdotsplit[0] + "." + localdotsplit[1]
			fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
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
		if "npe" in name:
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
		if "npe" in name or  "NPE" in name:
			imagecode = "ISR-NPE"
		else:
			imagecode = "ISR"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == "sre":
		localdotsplit = splitbydash[3].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
		if "npe" in name or  "NPE" in name:
			imagecode = "SM-SRE-NPE"
		else:
			imagecode = "SM-SRE"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == "alarm":
		localdotsplit = splitbydash[4].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2]
		if "npe" in name or  "NPE" in name:
			imagecode = "ALARM-ERROR BOOKS-NPE"
		else:
			imagecode = "ALARM-ERROR BOOKS"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == "WAAS" or splitbydash[0] == "waas":
		localdotsplit = splitbydash[1].split(".")
		mainver = localdotsplit[0] + "." + localdotsplit[1]
		fullver = localdotsplit[0] + "." + localdotsplit[1] + "." + localdotsplit[2] + "." + localdotsplit[3]
		if "sysimg" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "SYSTEM-SOFTWARE-32bit-NPE"
			else:
				imagecode = "SYSTEM-SOFTWARE-32bit"
		elif "bin" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "BOOT-NPE"
			else:
				imagecode = "BOOT"
		elif "rescue" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "RESCUE CD-NPE"
			else:
				imagecode = "RESCUE CD"
		elif "Doc" in name or "DOC" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "DOCUMENTATION-NPE"
			else:
				imagecode = "DOCUMENTATION"
		elif "npe" in name or  "NPE" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "SM-SRE-NPE"
			else:
				imagecode = "SM-SRE"
		elif "npe" in name or  "NPE" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = "ALARM-ERROR BOOKS-NPE"
			else:
				imagecode = "ALARM-ERROR BOOKS"
		filepath = prodname + "/" + mainver + "/" + fullver + "/" + imagecode
		filemove (filepath, filename)

def toplevel(filename,hashsha512,hashsha256,hashmd5,hashfile,debug0,debug1):
	src = filename
	names = os.listdir(src)
	os.chdir(src)
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
		
		if hashsha512 == True:
			hasher = hashlib.sha512()
			with open(name, 'rb') as afile:
				buf = afile.read()
				hasher.update(buf)
			print("SHA512:", end =" ")
			print(hasher.hexdigest())
		if hashsha256 == True:
			hasher = hashlib.sha256()
			with open(name, 'rb') as afile:
				buf = afile.read()
				hasher.update(buf)
			print("SHA256:", end =" ")
			print(hasher.hexdigest())
		if hashmd5 == True:
			hasher = hashlib.md5()
			with open(name, 'rb') as afile:
				buf = afile.read()
				hasher.update(buf)
			print("MD5:", end =" ")
			print(hasher.hexdigest())

		splitbydot = name.split(".")
		classify = name.split("-")
		splitbydash = name.split("-")
		splitbydashsub = splitbydot[0].split("-")
		
		thisstring = splitbydot.pop()
		splitbydot.append(thisstring)

		if name == "Thumbs.db":
			continue
		elif name.endswith("DS_Store"):
			continue
		elif name.endswith("hash"):
			continue
		elif name.endswith("part"):
			continue
		elif name == "cat9k_fpga_upgrade_utility.pdf":
			fileprocessor_iosxe(debug1,name)
		elif name.endswith("pdf"):
			continue

		if (
		name.startswith("ata") or 
		name.startswith("cmterm")
		):
			fileprocessorvoice(debug1,name)

		elif (
		"tsjspgen" in name or 
		"tpcgen" in name or 
		"tpgen" in name or 
		"tpcgenx" in name or 
		"tscgen" in name or 
		"tscgenx" in name
		):
			fileprocessorpagent(name)

		elif(
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
		name == "Rommon-123-8r.YH13-notes" or 
		name == "Rommon-124-22r.YB5-notes" or 
		name == "Rommon-151-1r.T4-notes" or 
		name == "Rommon-151-1r.T5-notes" or 
		name == "Rommon-150-1r.M12-notes" or 
		name == "asr900_15_6_43r_s_rommon.pkg" or 
		name == "ASR1000_RM_16_3_2R.bin" or 
		name == "C2400_RM2.symbols.123-7r.T2" or 
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
		name.startswith("n5000_poap_script") or 
		name.startswith("n6000_poap_script") or 
		name.startswith("poap_ng") or 
		name.startswith("Nexus1000v") or 
		name.startswith("Nexus1000v") or 
		name.startswith("Nexus1000V") or 
		name.startswith("Nexus1000V5") or 
		name.startswith("n1000vh-dk9") or 
		name.startswith("nexus-1000v") or 
		name == "n3k_bios_release_rn.pdf" or 
		name == "ssd_c400_upgrade_6.1.2.I2.2a.tar" or 
		name == "ssd_c400_upgrade_6.1.2.I2.3.tar" or 
		name == "ssd_c400_upgrade_6.1.2.I2.2.tar" or 
		name == "ssd_c400_upgrade_6.1.2.I2.1.tar" or 
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
		name.startswith("np.0.8.11.1.spe") or 
		name.startswith("np.0.8.11.2.spe") or 
		name.startswith("np.6.106.spe") or 
		name.startswith("np.6.93.spe") or 
		name.startswith("np.7.16.spe") or 
		name.startswith("np.7.9.spe") or 
		name.startswith("np.8.8.1.spe") or 
		name.startswith("np.spe")
		):
			prodname = product ("mica-modem")
			imagecode = imagelookup ("np")
			filepath = prodname + "/" + imagecode
			filemove (filepath, name)

		elif (
		name.startswith("adsl_alc")
		):
			prodname = product ("ISRG1GENERIC")
			imagecode = imagelookup ("DSLFIRMWARE")
			filepath = prodname + "/" + imagecode
			filemove (filepath, name)

		elif (
		name.startswith("8705_") or 
		name.startswith("8775_") or 
		name.startswith("8790_")
		):
			prodname = product ("ISRG1GENERIC")
			imagecode = imagelookup ("HWIC3GGSM")
			filepath = prodname + "/" + imagecode
			filemove (filepath, name)

		elif name.startswith("vcw-vfc-mz"):
			prodname = product ("c5350")
			imagecode = imagelookup (splitbydot[0])
			filepath = prodname + "/" + imagecode
			filemove (filepath, name)

		elif name.startswith("c3600-2600-analog-fw"):
			prodname = product ("branchmodules")
			imagecode = imagelookup ("analogmodem")
			filepath = prodname + "/" + imagecode
			filemove (filepath, name)

		elif splitbydot[0] == "oac":
			filepath = "Switches/Nexus/Nexus-Open-Agent-Container"
			filemove (filepath, name)

		elif (
		splitbydot[0] == "C9800-40-universalk9_wlc" or 
		splitbydot[0] == "C9800-80-universalk9_wlc" or 
		splitbydot[0] == "C9800-CL-universalk9" or 
		splitbydot[0] == "C9800-L-universalk9_wlc" or 
		splitbydot[0] == "C9800-SW-iosxe-wlc" or 
		splitbydot[0] == "C9800-AP-universalk9" or 
		splitbydash[0] == "asr1000" or 
		splitbydash[0] == "asr1001" or 
		splitbydash[0] == "asr1001x" or 
		splitbydash[0] == "asr1002" or 
		splitbydash[0] == "asr1002x" or 
		splitbydash[0] == "asr1000rp1" or 
		splitbydash[0] == "asr1000rp2" or 
		splitbydash[0] == "asr1000rpx86" or 
		splitbydash[0] == "asr900rsp1" or 
		splitbydash[0] == "asr900rsp2" or 
		splitbydash[0] == "asr901" or 
		splitbydash[0] == "asr901sec" or 
		splitbydash[0] == "asr901rsp1" or 
		splitbydash[0] == "asr901rsp2" or 
		splitbydash[0] == "asr903rsp1" or 
		splitbydash[0] == "asr903rsp2" or 
		splitbydash[0] == "asr903rsp2" or 
		splitbydash[0] == "asr920" or 
		splitbydash[0] == "csr1000v" or 
		splitbydash[0] == "csr1000v_milplr" or 
		splitbydash[0] == "ie3x00" or 
		name.startswith("isr4400") or 
		name.startswith("isr4300") or 
		name.startswith("isr4200") or 
		name.startswith("ir1101") or 
		name.startswith("isr4400v2") or 
		name.startswith("c1100-universalk9") or 
		name.startswith("c1100-ucmk9") or 
		name.startswith("cat4500es8") or 
		name.startswith("cat4500e") or 
		name == "asr1000-hw-programmables.16.08.01.SPA.pkg" or 
		name == "isr-hw-programmables.03.13.02.S.154-3.S2-ext.SPA.pkg" or 
		name == "isr-hw-programmables.03.15.03.S.155-2.S3-ext.SPA.pkg" or 
		name == "ASR1K-fpga_prog.16.0.1.xe.bin" or 
		name.startswith("cat3k_caa") or 
		name.startswith("cat9k") or 
		name.startswith("ess3x00") or 
		name.startswith("s5800") or 
		name.startswith("vg400") or 
		name.startswith("vg450") or 
		name.startswith("CAT3650_WEBAUTH_BUNDLE") or 
		name.startswith("CAT3850_WEBAUTH_BUNDLE") or 
		name.startswith("iosxe-sd-avc") or 
		name.startswith("iosxe-remote-mgmt") or 
		name == "c1100_gfast_phy_fw_A43j2.pkg" or 
		name == "c1100_gfast_phy_fw_A43r_B43r.pkg" or 
		name == "c1100_phy_fw_A39x3_B39x3.pkg" or 
		name == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg" or 
		name == "nim_vab_phy_fw_A39x3_B39x3_Bond39t.pkg"
		):
			fileprocessor_iosxe(debug1,name)

		elif (
		name.startswith("ucs") or 
		name.startswith("update_pkg-ucse") or 
		name.startswith("pid-ctlg") or 
		name.startswith("delnorte2") or 
		name.startswith("plumas2") or 
		name == "Signed_EN_BIOS_1.5.0.4.bin.SPA" or 
		name == "1X0DBIOSv4.8" or 
		name == "1X0SBIOSv4.8" or 
		name == "B57BCMCD_v15.2.4.1.tgz" or 
		name == "B57CiscoCD_T6.4.4.3-57712.zip" or 
		name == "CIMC-3.2.8.bin" or 
		name == "CIMC_2.4.1.bin" or 
		name == "CIMC_2.4.2.bin" or 
		name == "CIMC_3.0.1.bin" or 
		name == "CIMC_3.0.2.bin" or 
		name == "CIMC_3.1.1.bin" or 
		name == "CIMC_3.1.2.bin" or 
		name == "CIMC_3.1.3.bin" or 
		name == "CIMC_3.1.4.bin" or 
		name == "CIMC_3.2.1.REL.bin" or 
		name == "CIMC_3.2.2.bin" or 
		name == "CIMC_3.2.3.bin" or 
		name == "CIMC_3.2.4.bin" or 
		name == "CIMC_3.2.6.bin" or 
		name == "CIMC_3.2.7.bin" or 
		name == "DW_16MB_release_1029.bin" or 
		name == "DW_BIOS.bin.SPA" or 
		name == "DW_Signed_Bios_Image.bin.SPA" or 
		name == "Intel_Windows_drv_MR_6.714.18.00_pv.zip" or 
		name == "LSI_x64_Signed_Driver_5.2.116.64.zip" or 
		name == "MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip" or 
		name == "Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA" or 
		name == "Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA" or 
		name == "Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA" or 
		name == "Signed_DW_M1M2_Bios_Image_041015.bin.SPA" or 
		name == "Signed_EN_BIOS_1.5.0.5.bin.SPA" or 
		name == "Signed_EN_BIOS_1.5.0.6.bin.SPA" or 
		name == "Signed_SW_M2_BIOS_1.5.0.6.bin.SPA" or 
		name == "Signed_SW_M2_BIOS_1.5.0.7.bin.SPA" or 
		name == "Signed_SW_M2_BIOS_1.5.0.8.bin.SPA" or 
		name == "Signed_SW_M2_Bios_1.5.0.5.bin.SPA" or 
		name == "UCSEDM3_BIOS_2.4.SPA" or 
		name == "UCSEDM3_BIOS_2.5.SPA" or 
		name == "UCSEDM3_BIOS_2.6.SPA" or 
		name == "UCSE_CIMC_2.3.1.bin" or 
		name == "UCSE_CIMC_2.3.2.bin" or 
		name == "UCSE_CIMC_2.3.3.bin" or 
		name == "UCSE_CIMC_2.3.5.bin" or 
		name == "efi-obd-v12-07-18.diag" or 
		name == "efi-obd-v13-10-15.diag" or 
		name == "efi-obd-v13-7-3.diag" or 
		name == "ucse-huu-2.1.1.iso" or 
		name == "huu-2.3.1.iso" or 
		name == "huu-2.3.2.iso" or 
		name == "huu-2.3.3.iso" or 
		name == "huu-2.4.1.iso" or 
		name == "huu-3.0.1.iso" or 
		name == "huu-3.1.1.iso" or 
		name == "huu_3.1.2.iso" or 
		name == "huu_3.1.3.iso" or 
		name == "huu_3.1.4.iso" or 
		name == "huu_3.2.6.v3.iso" or 
		name == "intel9.2.3.1023.tar" or 
		name == "rste_4.5.0.1335_install.zip" or 
		name == "update_pkg-Mar-22-MR-rebuild.bin" or 
		name == "update_pkg-ucse.combined.120808.bin" or 
		name == "update_pkg-ucse.combined.REL.2.2.1.bin" or 
		name == "update_pkg-ucse.combined.REL.2.2.2.bin" or 
		name == "update_pkg-ucse.combined.REL.bin" or 
		name == "SW_16MB_release_1102.bin" or 
		name == "SW_Signed_Bios_Image.bin.SPA" or 
		name == "UCS_docs_20110510.iso" or 
		name == "c2xx-m1-utils-1.0.2.iso" or 
		name == "b2xx-m1-drivers-1.1.1j.iso" or 
		name.startswith ("Cisco_ACI") or 
		name.startswith ("acisim") or 
		name.startswith ("aci-simulator") or 
		name.startswith ("aci-apic") or 
		name.startswith ("aci-msft-pkg") or 
		name.startswith ("aci-n9000-dk9") or 
		name.startswith ("apic-vrealize") or 
		name.startswith ("esx-msc") or 
		name.startswith ("msc") or 
		name.startswith ("vcenter-plugin") or 
		name.startswith ("tools-msc") or 
		name.startswith ("storfs-packages") or 
		name.startswith ("HX-ESXi") or 
		name.startswith ("HX-Kubernetes") or 
		name.startswith ("Cisco-HX-Data-Platform-Installer") or 
		name.startswith ("HyperFlex-VC-HTML") or 
		name.startswith ("hxcsi") or 
		name.startswith ("HyperFlex-Witness-") or 
		name.startswith ("HxClone-HyperV") or 
		name.startswith ("DCNM") or 
		name.startswith ("dcnm") or 
		name.startswith ("Collector") or 
		name.startswith ("collector") or 
		name == "readme_10.2.1.ST.1" or 
		name == "JeOS_Patch_To_Enable_ASD.zip" or 
		name.startswith ("apic_em_update-apic-") or 
		name.startswith ("APIC-EM-") or 
		name.startswith ("CiscoPI3.4.pem") or 
		name.startswith ("CiscoPI3.5.pem")
		):
			file_proc_servers(name,debug1)


		elif (
		name.startswith ("5-") or 
		name.startswith ("ACS") or 
		name.startswith ("Acs") or 
		name.startswith ("Cisco_FTD") or 
		name.startswith ("Cisco_Firepower") or 
		name.startswith ("Cisco_Firepower_GEODB") or 
		name.startswith ("Cisco_Firepower_SRU") or
		name.startswith ("Cisco_Firepower_Threat") or 
		name.startswith ("Cisco_Network_Sensor") or 
		name.startswith ("Cisco_VDB_Fingerprint_Database") or
		name.startswith ("Clean") or 
		name.startswith ("Firepower") or 
		name.startswith ("ISE") or 
		name.startswith ("PIX") and name.endswith(".bin") or 
		name.startswith ("PIX") or 
		name.startswith ("PI") or 
		name.startswith ("Sourcefire") or
		name.startswith ("UCP") or 
		name.startswith ("UTD-STD-SIGNATURE") or 
		name.startswith ("applAcs") or 
		name.startswith ("asasfr") or 
		name.startswith ("asa") or 
		name.startswith ("asdm") or 
		name.startswith ("bh") and name.endswith(".bin") or 
		name.startswith ("cisco-asa") or 
		name.startswith ("coeus") or 
		name.startswith ("csd") or 
		name.startswith ("csm") or 
		name.startswith ("csmars") or 
		name == "pnLogAgent_1.1.zip" or 
		name == "pnLogAgent_4-1-3.zip" or 
		name == "pnLogAgent_4-1-3.zip.txt" or 
		name == "README_WebAgent.txt" or 
		name == "webAgent_1-0.zip" or 
		name == "webAgent_1-0.zip.txt" or 
		name == "webAgent_1-1.zip" or 
		name == "webAgent_1-1.zip.txt" or 
		name.startswith ("fcs-csm") or 
		name.startswith ("csm-maxmind-geolitecity-") or 
		name.startswith ("fcs-mcp") or 
		name.startswith ("firepower") or 
		name.startswith ("ftd") or 
		name.startswith ("fwsm_migration") or 
		name.startswith ("fxos") or 
		name.startswith ("hostscan") or
		name.startswith ("iosxe-utd") or
		name.startswith ("iosxe-utd-ips") or
		name.startswith ("iox-iosxe-utd") or
		name.startswith ("ise") or 
		name.startswith ("ise-pic") or 
		name.startswith ("mac-spw-dmg") or 
		name.startswith ("np") and name.endswith(".bin") or 
		name.startswith ("pdm") and name.endswith(".bin") or 
		name.startswith ("phoebe") or 
		name.startswith ("pix") and name.endswith(".bin") or 
		name.startswith ("pix") or 
		name.startswith ("sampleTransforms") or 
		name.startswith ("secapp-ucmk9") or
		name.startswith ("secapp-utd") or
		name.startswith ("thirdparty") or 
		name.startswith ("tools-anyconnect") or 
		name.startswith ("webagent") or 
		name.startswith ("win_spw") or 
		splitbydash[0] == "anyconnect" or 
		splitbydot[0] == "c6svc-fwm-k9" or 
		splitbydot[0] == "cisco-ftd" or
		name == "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429-Readme.txt" or 
		name == "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429.zip" or 
		name == "ACS57BasePatch.tar.gz" or 
		name == "BOOTX64.EFI" or 
		name == "PIX_to_ASA_1_0.dmg" or 
		name == "PIXtoASA_1_0.zip" or 
		name == "PIXtoASAsetup_1_0.exe" or 
		name == "README_ISE_20_201_21_22" or 
		name == "ReadMe_for_ACS_5.6_Upgrade_Package-txt" or 
		name == "WebSecurityCert.zip" or 
		name == "anyconnect_app_selector_1.0.zip" or 
		name == "anyconnect_app_selector_2.0.zip" or 
		name == "firepower-mibs.zip" or 
		name == "grub.efi" or 
		name == "pic-2.2.0.470.SPA.x86_64.iso" or 
		name == "pic-2.4.0.357.SPA.x86_64.iso" or 
		name == "release_duration_tool.tar" or 
		name == "cvdm-css-1.0_K9.zip" or 
		name == "cvdm-css-1.0.zip" or 
		name == "occ-121.gz" or 
		name == "occ-121.zip" or 
		name == "README-occ-121.rtf" or 
		name.startswith("sg") and name.endswith("zip") or 
		name.startswith("sg") and name.endswith("adi") or 
		name.startswith("sg") and name.endswith("adi-gz") or 
		name == "vpn30xxboot-4.0.Rel.hex" or 
		name.startswith ("VPN3000") or 
		name.startswith ("vpn3000") or 
		name.startswith ("vpn3002") or 
		name.startswith ("vpn3005") or 
		name.startswith ("CSM4") and name.endswith("Service_Pack1.exe") or 
		name.startswith ("CSM4") and name.endswith("Service_Pack2.exe") or 
		name.startswith ("cda") and name.endswith("iso") or 
		name == "cisco_vpn_auth.jar" or 
		name == "pxGrid_Mitigation_Remediation_v1.0.tgz" or 
		name == "rawrite.exe" or 
		name == "VPNDisable_ServiceProfile.xml" or 
		name == "citrix_plugin_howto.doc"
		):
			fileprocessorsecurity(debug1,name)

		elif (
		name == "xrvr-fullk9-4.3.2.vmdk" or 
		name == "xrv9k-fullk9-x.qcow2-6.0.0" or 
		name.startswith("fullk9-R-XRV9000") or 
		name.startswith("asr9k") or 
		name.startswith("xrv9k") or 
		name.startswith("ASR9K") or 
		name.startswith("XR12000") or 
		name.startswith("csm-") or 
		name.startswith("Sightline") or 
		name.startswith("SP_") or 
		name.startswith("TMS_") or 
		name.startswith("Cisco_TMS_")
		):
			fileprocessor_iosxr(debug1,name)

		elif (
		name.startswith ("sprom") or 
		name.startswith ("epld-sup2") or 
		name.startswith ("epld-6548getx") or 
		name.startswith ("6509neba") or 
		name.startswith ("6516agbic") or 
		name.startswith ("6548getx") or 
		name.startswith ("66748getx") or 
		name == "sconvertit0-11.tar" or 
		name == "sconvertit0-12.tar" or 
		name == "wconvertit0-11.zip" or 
		name == "wconvertit0-12.zip" or 
		name == "2730_rel_note" or 
		name == "Exp_V3_11.axf" or 
		name == "Exp_V3_11_Release_Note.pdf" or 
		name == "Exp_v10_10.spe" or 
		name == "MC7700_03.05.29.02_00_generic_000.000_001.cwe" or 
		name == "MC7700_03.05.29.03_00_generic_000.000_001.cwe" or 
		name == "MC7700_ATT_03.05.10.02_00.cwe" or 
		name == "MC7710_Global_03.05.24.00A.cwe" or 
		name == "MC7710_Global_03.05.29.02.cwe" or 
		name == "MC7750_VZW_03.05.10.06_00.cwe" or 
		name.startswith ("MC735X") and name.endswith ("spk") or 
		name.startswith ("MC7354") and name.endswith ("spk") or 
		name.startswith ("MC7350") and name.endswith ("spk") or 
		name.startswith ("MC7304") and name.endswith ("spk") or 
		name == "fw_upgrade.tcl" or 
		name == "sprint_v16904_package.tar" or 
		name == "Release-Notes-V3.12.1" or 
		name == "Release-Notes-V3.12.2" or 
		name == "V3_07.axf" or 
		name == "V3_09.axf" or 
		name == "V3_12_1.axf" or 
		name == "V3_12_2.axf" or 
		name == "V3_12_3.axf" or 
		name == "VAE2_A_39t_B39d_24m.SSA.bin" or 
		name == "VAE2_A_39x3_B39x3_24o.SSA.bin" or 
		name == "VAEW_A_39d_B_39d_24g1.SSA.bin" or 
		name == "VAEW_A_39f1_B_39d_24g1.SSA.bin" or 
		name == "VAEW_A_39t_B_39d_24m.SSA" or 
		name == "VAEW_A_39x3_B39x3_24o.SSA.bin" or 
		name == "VA_A_35l_B_35l_23j.bin" or 
		name == "VA_A_38k1_B_38h_24g1.bin" or 
		name == "VA_A_38q_B_38r1_24j.bin" or 
		name == "VA_A_39d_B_38h3_24h_1.bin" or 
		name == "VA_A_39h_B_38h3_24h_j.bin" or 
		name == "VA_A_39m_B_38h3_24h.bin" or 
		name == "VA_A_39m_B_38h3_24h_o.bin" or 
		name == "VA_A_39m_B_38u_24h.bin" or 
		name == "VA_A_39m_B_38u_24o_rc1_SDK_4.14L.04A-J.bin" or 
		name == "VA_A_39t_B_35j_24m" or 
		name == "VA_A_39t_b_38r1_24o.bin" or 
		name == "VA_A_39t_B_38r1_24o_rc1_SDK_4.14L.04A.bin" or 
		name == "VA_B_38V_d24m.bin" or 
		name == "portware.2730.ios" or 
		name == "vdsl.bin-A2pv6C035d_d23j" or 
		name == "vdsl.bin-A2pv6C035j" or 
		name == "vdsl.bin-A2pv6C035l" or 
		name == "vdsl.bin.32bdslfw" or 
		name.startswith("mica-modem-pw") or 
		name.startswith("mica-pw") or 	
		name.startswith("c2900XL") or 
		name.startswith("c2900xl") or 
		name.startswith("c3500XL") or 
		name.startswith("c3500xl")
		):
			fileprocessorios(debug1,name)

		elif (
		name.startswith("CUMC")
		):
			continue

		elif (
		name == "Cisco_usbconsole_driver.zip" or 
		name == "Cisco_usbconsole_driver_3_1.zip" or 
		name == "asr-9xx_usbconsole_drivers.zip"
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
		name.startswith("uccx") or 
		name.startswith("s52000tc") or 
		name.startswith("ciscocm") or 
		name.startswith("CPO") and name.endswith("zip") or 
		name.startswith("128MB.sdf") or 
		name.startswith("256MB.sdf") or 
		name.startswith("MIBS") or 
		name.startswith("sdmv10.zip") or 
		name.startswith("SDM-V25.zip") or 
		name.startswith("c6svc-nam") or 
		name.startswith("CSD-for-CSA-updates.zip") or 
		name.startswith("copfiles_iOS96.zip")
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
		name.startswith("SPA30x_SPA50x_")
		):
			#Small Business
			continue

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
		name.startswith ("c1100") or 
		name.startswith ("AIR") or 
		name.startswith ("SWISMK9") or 
		name.startswith ("SWLC3750K9") or 
		name.startswith ("AIR_CTVM_LARGE-K9") or 
		name.startswith ("AIR_CTVM-K9") or 
		name.startswith ("MFG_CTVM") or 
		name.startswith ("AP_BUNDLE") or 
		name.startswith ("CiscoAironet-AP-to-LWAPP-Upgrade-Tool") or 
		name == "AP350-Cisco-IOS-Upgrade-Image-v2.img" or 
		name == "AP1200-Cisco-IOS-Upgrade-Image-v3.img" or 
		name.startswith ("WGB350") and name.endswith ("exe") or 
		name == "webauth_bundle.zip" or 
		name == "webauth_bundle-1.0.2.zip"
		):
			fileprocessor_wireless(debug1,name)

		elif (
		name.startswith ("m9000") or 
		name.startswith ("m9100") or 
		name.startswith ("m9200") or 
		name.startswith ("m9250") or 
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

		elif (
		name == "SDM-V25.zip"
		):
			continue
#			prodname = product ("ccp")
#			utilssingleprodname (debug1,name,prodname)

		elif (
		name.startswith("c3560cx-cwml") or 
		name.startswith("c2960x-cwml") or 
		name.startswith("c2960l-cwml") or 
		name.startswith("c2960cx-cwml") or 
		name.startswith("c2960-cwml") or 
		name.startswith("c2960c405-cwml") or 
		name.startswith("c1000-cwml")
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
#			standardios (name, prodname, imagecode)
			fileprocessorios (debug1,name)

		elif splitbydot[0] == "dsc-c5800-mz":
			imagecode = imagelookup (splitbydash[0])
			prodname = product (splitbydash[1])
#			standardios (name, prodname, imagecode)
			fileprocessorios (debug1,name)

		elif splitbydash[0] == "cat6000" or splitbydash[0] == "cat5000" or splitbydot[0] == "cat4000" or splitbydot[0] == "cat4000-cv" or splitbydot[0] == "cat4000-k8" or splitbydot[0] == "cat4000-k9":
			catos (name)

		elif splitbydash[0] == "fcs" and splitbydash[1] == "rme" and splitbydash[2] == "430":
			filepath = "Cisco Security Manager/4.0.0/RESOURCE MANAGER ESSENTIALS"
			filemove (filepath, name)

		elif splitbydash[0] == "IPS" and splitbydash[1] == "K9" and splitbydash[2] == "r":
			ipsrecovery(name)

		elif splitbydash[0] == "IPS" and splitbydash[1] == "K9":
			ipssystem(name)

		elif splitbydash[0] == "IPS" and splitbydash[1] == "sig":
			ipssig(name)

		elif splitbydot[0] == "c10k-fpd-pkg":
			prodname = "Routers/SP/10000"
			imagecode = imagelookup (splitbydash[1])
#			standardios (name, prodname, imagecode)
			fileprocessorios (debug1,name)

		elif splitbydash[0] == "all":
			prodname = "OnePK"
			if name == "all-in-one-VM-1.2.1-194.ova":
				filepath = prodname + "/" + "1.2/" + "1.2(1)194"
				filemove (filepath, name)
			elif name == "all-in-one-VM-1.3.0.181.ova":
				filepath = prodname + "/" + "1.3/" + "1.3(0)181"
				filemove (filepath, name)

		elif splitbydash[0] == "pp" and splitbydash[1] == "adv":
			nbar2 (name)

		else:
#			imagecode = imagelookup (splitbydash[1])
#			prodname = product (splitbydash[0])
#			standardios (name, prodname, imagecode)
			fileprocessorios (debug1,name)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--directory', help='Directory to sort', required=True)
	parser.add_argument('-hs','--hashsha512', help='Hash File using the SHA 512 Algorithm', action='store_true', required=False)
	parser.add_argument('-hs1','--hashsha256', help='Hash File using the SHA 256 Algorithm', action='store_true', required=False)
	parser.add_argument('-hs3','--hashmd5', help='Hash File using the MD5 Algorithm', action='store_true', required=False)
	parser.add_argument('-hf','--hashfile', help='File with Hash Info. Format is FILENAME,MD5HASH,SHA512HASH. Additional columns are ignored', action='store_true', required=False)
	parser.add_argument('-d0','--debug0', help='Debug Level 0 (No Output) (NYI)', action='store_true', required=False)
	parser.add_argument('-d1','--debug1', help='Print Debug Commands (Level 1) (partially implemented)', action='store_true', required=False)
	
	args = parser.parse_args()
	dirpass = args.directory
	hashsha512 = args.hashsha512
	hashsha256 = args.hashsha256
	hashmd5    = args.hashmd5
	hashfile   = args.hashfile
	debug1     = args.debug1
	debug0     = args.debug0

	toplevel(dirpass,hashsha512,hashsha256,hashmd5,hashfile,debug0,debug1)
