from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def fileprocessorsecurity (filename):
	if filename.startswith('c6svc-fwm-k9'):
		sec_fwsm (filename)
####	elif filename.startswith('thirdparty'):
####		sec_anyconnect(filename)
	elif filename == "anyconnect_app_selector_2.0.zip":
		prodname = product('anyconnect')
		imagecode = imagelookup('app_selector')
		sec_single_file (filename,prodname,imagecode)
	elif filename.startswith('asdm'):
		sec_asa_asdm (filename)
	elif filename.startswith('Cisco_Firepower_SRU') or filename.startswith('Sourcefire_Rule_Update'):
		sec_fp_rules(filename)
	elif filename.startswith('Cisco_Firepower_GEODB') or filename.startswith('Sourcefire_Geodb'):
		sec_fp_geodb(filename)
	elif filename.startswith('Cisco_VDB_Fingerprint_Database') or filename.startswith('Sourcefire_VDB'):
		sec_fp_vdb(filename)
	elif filename.startswith('anyconnect'):
		sec_anyconnect(filename)
	elif filename.startswith('hostscan_'):
		sec_hostscan(filename)
#	elif filename.startswith('tools-anyconnect'):
#		sec_anyconnect(filename)
#	elif filename.startswith('sampleTransforms'):
#		sec_anyconnect(filename)
#	name.startswith('Cisco_FTD') or 
#	name.startswith('Cisco_Firepower_Threat') or 
#	name.startswith('Cisco_Network_Sensor') or 
#	name.startswith('firepower') or 
#	name.startswith('fxos') or 
#	name.startswith('ftd')
#	):

def sec_fp_vdb (filename):
	splitbydash = filename.split('-')
	prodname = product ('firepower')
	if filename.startswith('Cisco_VDB_Fingerprint_Database'):
		imagecode = imagelookup('csfvdb')
	elif filename.startswith('Sourcefire_VDB'):
		imagecode = imagelookup('sfvdb')
	splitbydash[2] = splitbydash[2].replace(".sh", "")
	ver = util2digit (splitbydash[1],splitbydash[2])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fp_rules (filename):
	splitbydash = filename.split('-')
	prodname = product ('firepower')
	if filename.startswith('Cisco_Firepower_SRU'):
		imagecode = imagelookup('csfrules')
	elif filename.startswith('Sourcefire_Rule_Update'):
		imagecode = imagelookup('sfrules')
	ver = util4digit (splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_fp_geodb (filename):
	splitbydash = filename.split('-')
	splitbydash[4] = splitbydash[4].replace(".sh", "")
	prodname = product ('firepower')
	if filename.startswith('Cisco_Firepower_GEODB'):
		imagecode = imagelookup('csfgeodb')
	elif filename.startswith('Sourcefire_Geodb'):
		imagecode = imagelookup('sfgeodb')
	ver = util4digit (splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
	#Intended File Format (Product, Image Path, Year, Version
	filepath = filepath4 (prodname,imagecode,splitbydash[1],ver)
	filemove (filepath, filename)

def sec_single_file(filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)
	
def firepowerftd (filename):
	prodname = product('firepower')
	filepath = prodname
	filemove (filepath, filename)

def firepower (filename):
	prodname = product('firepower')
	splitbydot = name.split('.')
	splitbydash = name.split('-')
	splitbydash0 = splitbydot[0].split('-')
	if splitbydash0[0] == 'firepower':
		if splitbydash0[1] == 'mibs':
			imagecode = "MIBS"
			iosmain = splitbydot[1] + '.' + splitbydot[2]
			iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
			filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
			filemove (filepath, filename)
	elif splitbydash0[0] == 'fxos':
		if splitbydash0[1] == 'mibs' and splitbydash0[2] == 'fp9k' and splitbydash0[3] == 'fp4k':
			imagecode = "MIBS-9K-4K"
			iosmain = splitbydot[1] + '.' + splitbydot[2]
			iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
			filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
			filemove (filepath, filename)
		elif len(splitbydash0) >= 3:
			if splitbydash0[2] == 'fpr4k' and splitbydash0[3] == 'firmware':
				imagecode = "FIRMWARE-4K"
				iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
				filepath = prodname + '/' + imagecode + '/' + iosfull
				filemove (filepath, filename)
			elif splitbydash0[1] == 'k9' and splitbydash0[2] == 'manager':
				imagecode = "SYSTEM/MANAGER"
				iosmain = splitbydot[1] + '.' + splitbydot[2]
				iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
				filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
				filemove (filepath, filename)
			elif splitbydash0[1] == 'k9' and splitbydash0[2] == 'system':
				imagecode = "SYSTEM/SYSTEM"
				iosmain = splitbydot[1] + '.' + splitbydot[2]
				iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
				filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
				filemove (filepath, filename)
			elif splitbydash0[1] == 'k9' and splitbydash0[2] == 'kickstart':
				imagecode = "SYSTEM/KICKSTART"
				iosmain = splitbydot[1] + '.' + splitbydot[2]
				iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
				filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
				filemove (filepath, filename)
		elif splitbydash0[1]:
			imagecode = "IMAGE"
			iosmain = splitbydot[1] + '.' + splitbydot[2]
			iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '.' + splitbydot[4]
			filepath = prodname + '/' + imagecode + '/' + iosmain + '/' + iosfull
			filemove (filepath, filename)

def sec_asa_asdm (filename):
	prodname = product('asdm')

def sec_fwsm (filename):
	splitbydot = filename.split('.')
	splitbydash = splitbydot[1].split('-')
	vertwo = util2digit(splitbydash[0],splitbydash[1])
	verthree = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
	prodname = product('c6svc-fwm')
	filepath = filepath3(prodname,vertwo,verthree)
	filemove (filepath, filename)

def firewallpix (filename):
	prodname = product('pix')
	pixversion = list(filename)
	pix = pixversion[3] + '.' + pixversion[4] + '(' + pixversion[5] + ')'
	pixprimary = pixversion[3] + '.' + pixversion[4]
	filepath = product + '/' + pixprimary + '/' + pix
	filemove (filepath, filename)


def sec_hostscan (filename):
	splitbyuscore = filename.split('_')
	splitbyuscore[1] = splitbyuscore[1].replace("-k9.pkg", "")
	splitbydot = splitbyuscore[1].split('.')
	prodname = product('anyconnect')
	imagecode = imagelookup('hostscan')
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p3_d3_v (filename,prodname,imagecode):
	splitbydash = filename.split('-')
	splitbydash = filename.split('-')
	splitbydot = splitbydash[3].split('.')
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect_p3_d4_v (filename,prodname,imagecode):
	splitbydash = filename.split('-')
	splitbydot = splitbydash[3].split('.')
	ver2 = util2digit (splitbydot[0],splitbydot[1])
	ver3 = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
	filepath = filepath4(prodname,imagecode,ver2,ver3)
	filemove (filepath, filename)

def sec_anyconnect (filename):
	prodname = product('anyconnect')
	splitbydash = filename.split('-')
	if splitbydash[1] == 'iseposture' and splitbydash[2] == 'win':
		imagecode = imagelookup('iseposturewin')
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'iseposture' and splitbydash[2] == 'mac':
		imagecode = imagelookup('iseposturemac')
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'isecompliance' and splitbydash[2] == 'win':
		imagecode = imagelookup('isecompliancewin')
		sec_anyconnect_p3_d4_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'isecompliance' and splitbydash[2] == 'mac':
		imagecode = imagelookup('isecompliancemac')
		sec_anyconnect_p3_d4_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'isecompliance' and splitbydash[2] == 'mac':
		imagecode = imagelookup('isecompliancemac')
		sec_anyconnect_p3_d4_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'EnableFIPS' and splitbydash[2] == 'win':
		imagecode = imagelookup('fips')
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'dart' and splitbydash[2] == 'win':
		imagecode = imagelookup('dart')
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)
	elif splitbydash[1] == 'gina' and splitbydash[2] == 'win':
		imagecode = imagelookup('gina')
		sec_anyconnect_p3_d3_v (filename,prodname,imagecode)

