import os, shutil, sys, re, getopt
#Functions (product,imagelookup,iostrain,filemove)
#import product,imagelookup,iostrain,filemove from iosutils
#import iosutils
from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat
from ios_nexus import fileprocessornxos
from ios_voice import fileprocessorvoice
from ios_security import fileprocessorsecurity

def cat6knam (filename):
	product = 'Network-Management/Catalyst-6500-NAM'
	array = filename.split('.')
	if array[0] == 'c6svc-nam':
		version = array[1].split('-')
		mainver = version[0] + '.' + version[1]
		fullver = version[0] + '.' + version[1] + '(' + version[2] + ')'
		if array[2] == 'patch':
			thissplit = array[3].split('-')
			patchver = thissplit[0] + '.' + thissplit[1]
			filepath = product + '/' + mainver + '/' + fullver + '/Patch ' + patchver
			filemove (filepath, filename)
		else:
			thissplit = array[1].split('-')
			mainver = thissplit[0] + '.' + thissplit[1]
			fullver = thissplit[0] + '.' + thissplit[1] + '(' + thissplit[2] + ')'
			filepath = product + '/' + mainver + '/' + fullver
			filemove (filepath, filename)
			

def vpn3000 (filename):
	product = 'VPN 3000'
	array = filename.split('.')
	first = list(array[0])
	second = list(array[3])
	mainver = first[8] + '.' + array[1]
	fullver = first[8] + '.' + array[1] + '(' + array[2] + ')' + second[0]
	filepath = product + '/' + mainver + '/' + fullver
	filemove (filepath, filename)

def anyconnect (filename):
	product = 'VPN AnyConnect Client'
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	if splitbydash[1] == 'EnableFIPS' and splitbydash[2] == 'win':
		imagecode = 'FIPS'
		supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'dart' and splitbydash[2] == 'win':
		imagecode = 'DART'
		supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'gina' and splitbydash[2] == 'win':
		if splitbydash[4] == 'web' and splitbydash[5] == 'deploy':
			imagecode = 'GINA-WEB-DEPLOY'
		elif splitbydash[4] == 'PRE' and splitbydash[5] == 'deploy':
			imagecode = 'GINA-PRE-DEPLOY'
		else:
			imagecode = 'GINA'
		supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'Linux_64':
		imagecode = 'CLIENT'
		supcode = 'LINUX 64'
		thissplit = splitbydash[2].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'linux' and splitbydash[2] == '64':
		imagecode = 'CLIENT'
		supcode = 'LINUX 64'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'predeploy' and splitbydash[2] == 'linux' and splitbydash[3] == '64':
		imagecode = 'PRE-DEPLOY'
		supcode = 'LINUX 64'
		thissplit = splitbydash[4].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'predeploy' and splitbydash[2] == 'linux':
		imagecode = 'PRE-DEPLOY'
		supcode = 'LINUX'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'linux':
		supcode = 'LINUX'
		if splitbydash[3] == 'EnableFIPS.tar.gz':
			imagecode = 'FIPS'
		elif splitbydash[3] == 'vpnapi.tar.gz':
			imagecode = 'VPN-API'
		else:
			imagecode = 'CLIENT'
		thissplit = splitbydash[2].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)

	elif splitbydash[3] == 'compliance' and splitbydash[1] == 'macosx':
		imagecode = 'ISE COMPLIANCE'
		supcode = 'MAC OS-X I386'
		thissplit = splitbydash[4].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/'  + imagecode + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
		

	elif splitbydash[1] == 'isecompliance' and splitbydash[2] == 'macosx':
		imagecode = 'ISE COMPLIANCE'
		supcode = 'MAC OS-X I386'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/'  + imagecode + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
		

	elif splitbydash[2] == 'compliance' and splitbydash[1] == 'win':
		imagecode = 'ISE COMPLIANCE'
		supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/'  + imagecode + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
		
	elif splitbydash[1] == 'macosx' and splitbydash[2] == 'i386':
		supcode = 'MAC OS-X I386'
		if splitbydash[4] == 'EnableFIPS.tar.gz':
			imagecode = 'FIPS'
		elif splitbydash[4] == 'vpnapi.tar.gz':
			imagecode = 'VPN-API'
		else:
			imagecode = 'CLIENT'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'macosx' and splitbydash[2] == 'powerpc':
		supcode = 'MAC OS-X POWERPC'
		if splitbydash[3] == 'EnableFIPS.tar.gz':
			imagecode = 'FIPS'
		elif splitbydash[3] == 'vpnapi.tar.gz':
			imagecode = 'VPN-API'
		else:
			imagecode = 'CLIENT'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'wince':
		if splitbydash[3] == 'activesync':
			supcode = 'WINDOWS-CE'
			imagecode = 'CLIENT - ACTIVESYNC'
			thissplit = splitbydash[4].split('.')
			mainver = thissplit[0] + '.' + thissplit[1]
			fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
			filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
			filemove (filepath, filename)
		else:
			supcode = 'WINDOWS-CE'
			imagecode = 'CLIENT'
			thissplit = splitbydash[3].split('.')
			mainver = thissplit[0] + '.' + thissplit[1]
			fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
			filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
			filemove (filepath, filename)
	elif splitbydash[1] == 'win' and splitbydash[2] == 'vpnapi':
		supcode = 'WINDOWS'
		imagecode = 'VPN-API'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
	elif splitbydash[1] == 'win':
		supcode = 'WINDOWS'
		if splitbydash[3] == 'web' and splitbydash[4] == 'deploy':
			imagecode = 'CLIENT-WEB-DEPLOY'
		elif splitbydash[3] == 'pre' and splitbydash[4] == 'deploy':
			imagecode = 'CLIENT-PRE-DEPLOY'
		else:
			imagecode = 'CLIENT'
		thissplit = splitbydash[2].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == 'isecompliance' and splitbydash[2] == 'win':
		imagecode = 'ISE COMPLIANCE'
		supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/'  + imagecode + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
			
	elif splitbydash[1] == 'iseposture':
		imagecode = 'ISE POSTURE'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
			
	elif splitbydash[1] == 'profileeditor':
		imagecode = 'PROFILE EDITOR'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
			
	elif splitbydash[1] == 'websecurity':
		imagecode = 'PROFILE EDITOR'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
			
	elif splitbydash[1] == 'amp':
		imagecode = 'AMP ENABLER'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
			
	elif splitbydash[1] == 'posture':
		imagecode = 'ISE POSTURE'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)
		
	elif splitbydash[1] == 'nam':
		imagecode = 'NETWORK ACCESS MODULE'
		if splitbydash[2] == 'macosx':
			supcode = 'MAC OS-X I386'
		elif splitbydash[2] == 'win':
			supcode = 'WINDOWS'
		thissplit = splitbydash[3].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode + '/'  + imagecode
		filemove (filepath, filename)

def csd (filename):
	chars = name[0:4]
	product = 'VPN Cisco Secure Desktop'
	array = filename.split('.')
	array2 = filename.split('-')
	if chars == 'csd_':
		supcode = 'HOST PACKAGE'
		array3 = filename.split('_')
		array4 = array3[1].split('-')
		thissplit = array4[0].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'macosx' and array2[3] == 'i386':
		supcode = 'MAC OS-X I386'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'macosx' and array2[3] == 'ppc':
		supcode = 'MAC OS-X POWERPC'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'windows':
		supcode = 'WINDOWS'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'wince':
		supcode = 'WINCE'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'linux' and array2[3] == 'i386':
		supcode = 'LINUX X86'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'linux' and array2[3] == 'x64':
		supcode = 'LINUX X64'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)
	elif array2[2] == 'linux' and array2[3] == 'x64':
		supcode = 'LINUX X64'
		thissplit = array2[1].split('.')
		mainver = thissplit[0] + '.' + thissplit[1]
		fullver = thissplit[0] + '.' + thissplit[1] + '.' + thissplit[2]
		filepath = product + '/' + mainver + '/' + fullver + '/'  + supcode
		filemove (filepath, filename)

def css (filename):
	array = list(filename)
	product = 'CSS'
	fullver = array[2] + array[3] + '.' + array[4] + array[5] + '.' + array[6] + '.' + array[7] + array[8]
	filepath = product + '/' + fullver
	filemove (filepath, filename)

def catos (filename):
	array = filename.split('.')
	version = array[1].split('-')
	mainver = version[0] + '.' + version[1]
	fullver = version[0] + '.' + version[1] + '(' + version[2] + ')'
	if array[0] == 'cat4000':
		prodname = product ('cat4000s12')
		imagecode = 'SUP-I-II'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat4000-cv':
		prodname = product ('cat4000s12')
		imagecode = 'SUP-I-II-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat4000-k8':
		prodname = product ('cat4000s12')
		imagecode = 'SUP-I-II'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat4000-k9':
		prodname = product ('cat4000s12')
		imagecode = 'SUP-I-II-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-supg':
		prodname = product ('cat5000')
		imagecode = 'SUP-III'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-supgk9':
		prodname = product ('cat5000')
		imagecode = 'SUP-III-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup':
		prodname = product ('cat5000')
		imagecode = 'SUP-II-G'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-supk9':
		prodname = product ('cat5000')
		imagecode = 'SUP-II-G-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup3':
		prodname = product ('cat5000')
		imagecode = 'SUP-III-G'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup3k9':
		prodname = product ('cat5000')
		imagecode = 'SUP-III-G-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup3cv':
		prodname = product ('cat5000')
		imagecode = 'SUP-III-G-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup3cvk9':
		prodname = product ('cat5000')
		imagecode = 'SUP-III-G-WITH-SSH-AND-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-atm':
		prodname = product ('cat5000')
		imagecode = 'ATM-MODULE'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat5000-sup8m':
		prodname = product ('cat5000')
		imagecode = 'SUP-8M'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup2':
		prodname = product ('cat6000')
		imagecode = 'SUP-2'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup2cv':
		prodname = product ('cat6000')
		imagecode = 'SUP-2-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup2k8' or array[0] == 'cat6000-sup2k9':
		prodname = product ('cat6000')
		imagecode = 'SUP-2-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup2cvk8' or array[0] == 'cat6000-sup2cvk9':
		prodname = product ('cat6000')
		imagecode = 'SUP-2-WITH-SSH-AND-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup':
		prodname = product ('cat6000')
		imagecode = 'SUP-1'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-supcv':
		prodname = product ('cat6000')
		imagecode = 'SUP-1-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-supk8' or array[0] == 'cat6000-supk9':
		prodname = product ('cat6000')
		imagecode = 'SUP-1-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-supcvk8' or array[0] == 'cat6000-supcvk9':
		prodname = product ('cat6000')
		imagecode = 'SUP-1-WITH-SSH-AND-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup720k8':
		prodname = product ('cat6000')
		imagecode = 'SUP-720'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup720cvk8':
		prodname = product ('cat6000')
		imagecode = 'SUP-720-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup720k9':
		prodname = product ('cat6000')
		imagecode = 'SUP-720-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup720cvk9':
		prodname = product ('cat6000')
		imagecode = 'SUP-720-WITH-SSH-AND-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup32pfc3k8':
		prodname = product ('cat6000')
		imagecode = 'SUP-32'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup32pfc3cvk8':
		prodname = product ('cat6000')
		imagecode = 'SUP-32-WITH-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup32pfc3k9':
		prodname = product ('cat6000')
		imagecode = 'SUP-32-WITH-SSH'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	elif array[0] == 'cat6000-sup32pfc3cvk9':
		prodname = product ('cat6000')
		imagecode = 'SUP-32-WITH-SSH-AND-CISCOVIEW'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	filemove (filepath, filename)

def wireless (filename):
	classify = filename.split('-')
	chars3 = filename[0:3]
	if chars3 == 'MFG':
		wirelesscontrollers(filename)
	elif (classify[1] == 'AP1540'
	 or classify[1] == 'AP1560'
	 or classify[1] == 'AP1815'
	 or classify[1] == 'AP1830'
	 or classify[1] == 'AP1850'
	 or classify[1] == 'AP2800'
	 or classify[1] == 'AP3800'
	 or classify[1] == 'AP4800'):
		ciscoap(filename)
	elif classify[0] == 'AIR':
		wirelesscontrollers(filename)
	elif classify[0] == 'SWISMK9':
		wirelesscontrollers(filename)
	elif classify[0] == 'SWLC3750K9':
		wirelesscontrollers(filename)

def ciscoap (filename):
	splitbydash = filename.split('-')
	splitbydot = filename.split('.')
	if (splitbydash[1] == 'AP1540'
	 or splitbydash[1] == 'AP1560'
	 or splitbydash[1] == 'AP1815'
	 or splitbydash[1] == 'AP1830'
	 or splitbydash[1] == 'AP1850'
	 or splitbydash[1] == 'AP2800'
	 or splitbydash[1] == 'AP3800'
	 or splitbydash[1] == 'AP4800'):
		if splitbydot[0] == "AIR-AP1830-K9-8":
			prodname = product (splitbydash[1])
			if prodname =="UNKNOWN":
				messageunknowndev()
			else:
				mainver = util2digit(splitbydash[3], splitbydash[4])
				fullver = util4digit(splitbydash[3], splitbydash[4], splitbydash[5], splitbydash[6])
				filepath = filepath3 (prodname,mainver,fullver)
				filemove (filepath, filename)
			
		elif splitbydash[3] == "ME":
			prodname = product (splitbydash[1])
			if prodname =="UNKNOWN":
				messageunknowndev()
			else:
				mainver = util2digit(splitbydash[4], splitbydash[5])
				fullver = util4digit(splitbydash[4], splitbydash[5], splitbydash[6], splitbydash[7])
				filepath = filepath4 (prodname,mainver,fullver,"MOBILITY")
				filemove (filepath, filename)
		else:
			prodname = product (splitbydash[1])
			if prodname =="UNKNOWN":
				messageunknowndev()
			else:
				mainver = util2digit(splitbydash[3], splitbydash[4])
				fullver = util4digit(splitbydash[3], splitbydash[4], splitbydash[5], splitbydash[6])
				filepath = filepath3 (prodname,mainver,fullver)
				filemove (filepath, filename)

def wirelesscontrollers (filename):
	classify = filename.split('-')
	chars3 = filename[0:3]
	if classify[0] == 'SWLC3750K9':
		prodname = product (classify[0])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		mainver = splitbydash[1] + '.' + splitbydash[2]
		fullver = splitbydash[1] + '.' + splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif chars3 == 'MFG':
		classifyus = filename.split('_')
		if classifyus[2] == 'LARGE':
			prodname = product (classifyus[1])
			vermain = util2digit (classifyus[3],classifyus[4])
			verfull = util4digit (classifyus[3],classifyus[4],classifyus[5],classifyus[6])
			filepath = prodname + '/' + vermain + '/' + verfull
			filemove (filepath, filename)
	elif classify[0] == 'SWISMK9':
		prodname = product (classify[0])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		mainver = splitbydash[1] + '.' + splitbydash[2]
		fullver = splitbydash[1] + '.' + splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WLCM':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		mainver = splitbydash[3] + '.' + splitbydash[4]
		fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WLC' and classify[1] == 'SRE':
		prodname = product (classify[2])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		mainver = splitbydash[3] + '.' + splitbydash[4]
		fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CTVM':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WLC4400':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WLC2100':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WISM':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WISM2':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'WLC2006':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT7500':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT8500':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT8500':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		else:
			mainver = splitbydash[2] + '.' + splitbydash[3]
			fullver = splitbydash[2] + '.' + splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT5500':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if classify[2] == 'AP_BUNDLE':
			mainver = splitbydash[4] + '.' + splitbydash[5]
			fullver = splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6] + '.' + splitbydash[7]
		elif splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		elif splitbydash[2] == 'LDPE':
			mainver = splitbydash[4] + '.' + splitbydash[5]
			fullver = splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6] + '.' + splitbydash[7] + '(RUSSIA)'
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT5520':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if classify[2] == 'AP_BUNDLE':
			mainver = splitbydash[4] + '.' + splitbydash[5]
			fullver = splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6] + '.' + splitbydash[7]
		elif splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		elif splitbydash[2] == 'LDPE':
			mainver = splitbydash[4] + '.' + splitbydash[5]
			fullver = splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6] + '.' + splitbydash[7] + '(RUSSIA)'
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)
	elif classify[0] == 'AIR' and classify[1] == 'CT2500':
		prodname = product (classify[1])
		splitbydot = filename.split('.')
		splitbydash = splitbydot[0].split('-')
		if classify[2] == 'AP_BUNDLE':
			mainver = splitbydash[4] + '.' + splitbydash[5]
			fullver = splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6] + '.' + splitbydash[7]
		elif splitbydash[2] == 'K9':
			mainver = splitbydash[3] + '.' + splitbydash[4]
			fullver = splitbydash[3] + '.' + splitbydash[4] + '.' + splitbydash[5] + '.' + splitbydash[6]
		filepath = prodname + '/' + mainver + '/' + fullver
		filemove (filepath, filename)


def ucs6100 (filename, prodname, imagecode):
	splitbydot = filename.split('.')
	mainver = splitbydot[1] + '.' + splitbydot[2]
	fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')' + splitbydot[4] + '(' + splitbydot[5] + ')' + splitbydot[6]
	filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	filemove (filepath, filename)

def ucsmanager (filename, prodname, imagename):
	splitbydot = filename.split('.')
	splitbydash = splitbydot[0].split('.')
	mainver = splitbydot[1] + '.' + splitbydot[2]
	fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
	if splitbydot[0] == 'ucs-k9-bundle-b-series':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'B-SERIES/'
	elif splitbydot[0] == 'ucs-k9-bundle-m-series':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'M-SERIES/'
	elif splitbydot[0] == 'ucs-k9-bundle-c-series':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'C-SERIES/'
	elif splitbydot[0] == 'ucs-k9-bundle-infra':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'INFRASTRUCTURE/'
	elif splitbydot[0] == 'ucs-6300-k9-bundle-infra':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'INFRASTRUCTURE-6300/'
	elif splitbydot[0] == 'ucs-6400-k9-bundle-infra':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'INFRASTRUCTURE-6400/'
	elif splitbydot[0] == 'ucs-mini-k9-bundle-infra':
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'INFRASTRUCTURE-MINI/'
	elif splitbydot[0] == 'ucs-bxxx-drivers':
#		localsplitbydot = filename.split('.')
		if splitbydash[3] == 'linux':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'B-SERIES/LINUX/'
		elif splitbydash[3] == 'windows':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'B-SERIES/WINDOWS/'
		elif splitbydash[3] == 'vmware':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'B-SERIES/VMWARE/'
		else:
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'B-SERIES/'
	elif splitbydot[0] == 'ucs-cxxx-drivers':
		if splitbydash[3] == 'linux':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'C-SERIES/LINUX/'
		elif splitbydash[3] == 'windows':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'C-SERIES/WINDOWS/'
		elif splitbydash[3] == 'vmware':
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'C-SERIES/VMWARE/'
		else:
			filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + 'C-SERIES/'
	else:
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver
	filemove (filepath, filename)

def ucsdrivers (filename, prodname, imagename):
	splitbydot = filename.split('.')
	mainver = splitbydot[1] + '.' + splitbydot[2]
	fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
	filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagename
	filemove (filepath, filename)

def ucsutils2 (filename, prodname):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	imagename = 'UTILS'
	
	if splitbydot[0] == 'ucs-bxxx-utils-linux':
		platform = 'B-SERIES'
		os = 'LINUX'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
#		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + os + '/' + platform
#		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + platform + '/' + os
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-b2xx-utils-linux':
		platform = 'B-SERIES'
		os = 'LINUX'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-bxxx-utils-vmware':
		platform = 'B-SERIES'
		os = 'VMWARE'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-b2xx-utils-vmware':
		platform = 'B-SERIES'
		os = 'VMWARE'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-bxxx-utils-windows':
		platform = 'B-SERIES'
		os = 'WINDOWS'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-b2xx-utils-windows':
		platform = 'B-SERIES'
		os = 'WINDOWS'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-cxxx-utils-vmware':
		platform = 'C-SERIES'
		os = 'VMWARE'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-cxxx-utils-efi':
		platform = 'C-SERIES'
		os = 'EFI'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-cxxx-utils-linux':
		platform = 'C-SERIES'
		os = 'LINUX'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	elif splitbydot[0] == 'ucs-cxxx-utils-windows':
		platform = 'C-SERIES'
		os = 'WINDOWS'
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + imagename + '-' + platform + '/' + mainver + '/' + fullver + '/' + os
		filemove (filepath, filename)
	
	
def ucsutils (filename, prodname):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	splitbydashsub = splitbydot[0].split('-')
	if splitbydash[1] == 'b2xx':
		imagename = 'B-SERIES/UTILS'
	elif splitbydash[1] == 'bxxx':
		imagename = 'B-SERIES/UTILS'
	elif splitbydash[1] == 'c2xx':
		imagename = 'C-SERIES/UTILS'
	elif splitbydash[1] == 'cxxx':
		imagename = 'C-SERIES/UTILS'
	else:
		imagename = 'UTILS'
	
	if splitbydashsub[3] == 'linux':
		temp = splitbydot[2].split('-')
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		thisos = 'LINUX'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydashsub[3] == 'vmware':
		temp = splitbydot[2].split('-')
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		thisos = 'VMWARE'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydashsub[3] == 'windows':
		temp = splitbydot[2].split('-')
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		thisos = 'WINDOWS'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydashsub[3] == 'efi':
		temp = splitbydot[2].split('-')
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		thisos = 'EFI'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydash[4] == 'windows.iso':
		temp = splitbydash[3].split('.')
		mainver = temp[0] + '.' + temp[1]
		fullver = temp[0] + '.' + temp[1] + '(' + temp[2] + ')'
		thisos = 'WINDOWS'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydash[4] == 'linux.iso':
		temp = splitbydash[3].split('.')
		mainver = temp[0] + '.' + temp[1]
		fullver = temp[0] + '.' + temp[1] + '(' + temp[2] + ')'
		thisos = 'LINUX'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydash[4] == 'vmware.iso':
		temp = splitbydash[3].split('.')
		mainver = temp[0] + '.' + temp[1]
		fullver = temp[0] + '.' + temp[1] + '(' + temp[2] + ')'
		thisos = 'VMWARE'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)
	elif splitbydash[4] == 'efi.iso':
		temp = splitbydash[3].split('.')
		mainver = temp[0] + '.' + temp[1]
		fullver = temp[0] + '.' + temp[1] + '(' + temp[2] + ')'
		thisos = 'EFI'
		filepath = prodname + '/' + imagename + '/' + mainver + '/' + fullver + '/' + thisos
		filemove (filepath, filename)


def spa (filename, prodname, imagecode):
	
	if prodname == 'UNKNOWN':
		messageunknowndev()
	elif imagecode == 'UNKNOWN':
		messageunknownfeat()
	else:
		splitbydot = filename.split('.')
		splitbydash = filename.split('-')
		myver = splitbydot[2].split('-')
		
		mynum = list(myver[0])
		thiscontrol = 0
		for myios in mynum:
			if thiscontrol == 0:
				iosversion = myios
				iosprimary = myios
				thiscontrol = thiscontrol + 1
			elif thiscontrol == 1:
				iosversion = iosversion + myios + '.'
				iosprimary = iosprimary + myios + '.'
				thiscontrol = thiscontrol + 1
			elif thiscontrol == 2:
				iosversion = iosversion + myios
				iosprimary = iosprimary + myios
				thiscontrol = thiscontrol + 1
		
		if splitbydot[2] == 'bin':
			iosversion = iosversion + '(' + myver[1] + ')'
		else:
			iosprimary = iostrain(splitbydot[3], iosprimary)
			iosversion = iosversion + '(' + myver[1] + ')' + splitbydot[3]
		filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
		filemove (filepath, filename)

def cat4500spa (filename, prodname, imagecode):
	
	if prodname == 'UNKNOWN':
		messageunknowndev()
	elif imagecode == 'UNKNOWN':
		messageunknownfeat()
	else:
		splitbydot = filename.split('.')
		splitbydash = filename.split('-')
		iosmain = list(splitbydot[6])
#		iostrain = iosmain[0] + iosmain[1] + '.' + iosmain[2]
#		iosversion = iosmain[0] + iosmain[1] + '.' + iosmain[2] + '(' + iosmain[4] + ')' + splitbydot[7] + '-' + splitbydot[2] + '.' + splitbydot[3] + '(' + splitbydot[4] + ')'  + splitbydot[5]
		iostrain = splitbydot[2] + '.' + splitbydot[3]  + splitbydot[5]
		iosversion = splitbydot[2] + '.' + splitbydot[3] + '(' + splitbydot[4] + ')'  + splitbydot[5]
	
		
		filepath = prodname + '/' + iostrain + '/' + iosversion + '/' + imagecode
		filemove (filepath, filename)

def acs5patches (filename):
	product = 'ACS'
	imagecode = 'PATCH'
	splitbydot = filename.split(".")
	splitbydash = splitbydot[0].split("-")
	version = splitbydash[0] + '.' + splitbydash[1] + '.' + splitbydash[2] + '.' + splitbydash[3]
	filepath = product + '/' + version + '/' + imagecode + '/' + splitbydash[4]
	filemove (filepath, filename)

def acs (filename):
	product = 'ACS'
	splitbydot = filename.split(".")
	splitbydash = filename.split("-")
	splitbydot2 = splitbydash[1].split('.')
	
	if splitbydash[2] == 'DOCs.zip':
		imagecode = 'DOCUMENTATION'


def mars (filename):
	product = 'MARS'
	splitbydot = filename.split(".")
	splitbydash = splitbydot[0].split("-")
	mainversion = splitbydash[1] + '.' + splitbydot[1]
	version = splitbydash[1] + '.' + splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	filepath = product + '/' + mainversion + '/' + version
	filemove (filepath, filename)



def nbar2 (filename):
	product = 'NBAR2'
	splitbydash = filename.split("-")
	if splitbydash[2] == 'asr1k':
		nbarsixteen (filename)
	elif splitbydash[2] == 'csr1000v':
		nbarsixteen (filename)
	elif splitbydash[2] == 'isr4000':
		nbarsixteen (filename)
	elif splitbydash[2] == 'isr4451':
		nbarsixteen (filename)
	elif splitbydash[2] == 'isr1100':
		nbarsixteen (filename)
	elif splitbydash[2] == 'asr1k':
		nbarsixteen (filename)
	elif splitbydash[2] == 'isrg2':
		nbarsixteen (filename)
	elif splitbydash[2] == 'cat3k':
		nbarsixteen (filename)
	elif splitbydash[2] == 'cat9k':
		nbarsixteen (filename)


def nbarsixteen (filename):
	product = 'NBAR2'
	splitbydash = filename.split("-")

	if splitbydash[2] == 'asr1k':
		nbarclassification (filename,'NBAR2','ASR-1K')
	elif splitbydash[2] == 'csr1000v':
		nbarclassification (filename,'NBAR2','CSR-1000V')
	elif splitbydash[2] == 'isr4000':
		nbarclassification (filename,'NBAR2','ISR-4000')
	elif splitbydash[2] == 'isr4451':
		nbarclassification (filename,'NBAR2','ISR-4000')
	elif splitbydash[2] == 'isr1100':
		nbarclassification (filename,'NBAR2','ISR-1100')
	elif splitbydash[2] == 'asr1k':
		nbarclassification (filename,'NBAR2','ASR-1K')
	elif splitbydash[2] == 'isrg2':
		nbarclassification (filename,'NBAR2','ISR-G2')
	elif splitbydash[2] == 'cat3k':
		nbarclassification (filename,'NBAR2','CAT-3K')
	elif splitbydash[2] == 'cat9k':
		nbarclassification (filename,'NBAR2','CAT-9K')

def nbarclassification (filename,product,prodcode):
	splitbydash = filename.split("-")
	splitbydot = filename.split(".")

	if prodcode == 'ASR-1K' or prodcode == 'CSR-1000V' or prodcode == 'ISR-4000' or prodcode == 'CAT-3K' or prodcode == 'CAT-9K' or prodcode == 'ISR-1100':
		if splitbydash[3] == '152' or splitbydash[3] == '153' or splitbydash[3] == '154' or splitbydash[3] == '155':
			listver = list(splitbydash[3])
			splitbydash[6] = splitbydash[6].replace(".pack","")
			fullver = splitbydash[6] + '-' + listver[0] + listver[1] + '.' + listver[1] + '-' + splitbydash[4]
			filepath = product + '/' + prodcode + '/' + fullver
			filemove (filepath, filename)
		else:
			main1 = list(splitbydash[3])
			if splitbydash[3] == "1612.1a":
				majorversion = "16.12.1a"
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + '/' + prodcode + '/' + nbarversion[5] + '-' + majorversion
				filemove (filepath, filename)
			elif splitbydash[3] == "1612.1":
				majorversion = "16.12.1"
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + '/' + prodcode + '/' + nbarversion[5] + '-' + majorversion
				filemove (filepath, filename)
			else:
				majorversion = main1[0] + main1[1] + '.' + main1[2] + '.' + main1[4]
				nbarversion = filename.replace(".pack","")
				nbarversion = nbarversion.split("-")
				filepath = product + '/' + prodcode + '/' + nbarversion[5] + '-' + majorversion
				filemove (filepath, filename)
	elif filename == "pp-adv-isrg2-153-1.T-3.1.0.pack":
		filepath = product + '/' + prodcode + '/' + '3.1.0-153-1.T'
		filemove (filepath, filename)
	elif prodcode == 'ISR-G2':
		workname = filename.replace("pp-adv-isrg2-","")
		workname = workname.replace(".pack","")
		spdash = workname.split("-")
		filepath = product + '/' + prodcode + '/' + spdash[3] + '-' + spdash[0] + '-' + spdash[1]
		filemove (filepath, filename)
	else:
		main1 = list(splitbydash[3])
		if splitbydash[3].startswith("1612"):
			majorversion = main1[0] + main1[1] + '.' + main1[2] + main1[3]
		else:
			majorversion = main1[0] + main1[1] + '.' + main1[2]
		minorversion = splitbydash[4].split(".")
		nbarversion = filename.replace(".pack","")
		nbarversion = nbarversion.split("-")
		filepath = product + '/' + prodcode + '/' + nbarversion[5] + '-' + majorversion+ '.' + main1[4]
		filemove (filepath, filename)

def ipsrecovery (filename):
	product = 'IPS'
	imagecode = 'RECOVERY IMAGE'
	splitbydash = filename.split('-')
	if filename == 'IPS-K9-r-1.1-a-5.0-1.pkg':
		filepath = product + '/E0/5.0(1)/' + imagecode
	else:
		version = splitbydash[5] + '(' + splitbydash[6] + ')'
		engine = splitbydash[7].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
	filemove (filepath, filename)

def csmips (filename):
	product = 'Cisco Security Manager'
	splitbydash = filename.split('-')
	if splitbydash[3] == 'AIM':
		imagecode = 'UPGRADE-AIM'
		version = splitbydash[5] + '(' + splitbydash[6] + ')'
		engine = splitbydash[7].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
		filemove (filepath, filename)
	elif splitbydash[3] == 'K9':
		imagecode = 'UPGRADE-OTHER'
		version = splitbydash[4] + '(' + splitbydash[5] + ')'
		engine = splitbydash[6].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
		filemove (filepath, filename)
	elif splitbydash[3] == 'SSC_5':
		imagecode = 'UPGRADE-AIP-SSC-5'
		version = splitbydash[5] + '(' + splitbydash[6] + ')'
		engine = splitbydash[7].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
		filemove (filepath, filename)
	elif splitbydash[3] == 'NME':
		imagecode = 'UPGRADE-NME'
		version = splitbydash[5] + '(' + splitbydash[6] + ')'
		engine = splitbydash[7].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
		filemove (filepath, filename)
	elif splitbydash[3] == 'sig':
		imagecode = 'SIGNATURES'
		version = splitbydash[4]
		engine = splitbydash[6].split('.')
		filepath = product + '/' + engine[0] + '/' + imagecode + '/' + version
		filemove (filepath, filename)
	elif splitbydash[3] == 'engine':
		imagecode = 'UPGRADE-ENGINE'
		temp = splitbydash[6].split('.')
		version = splitbydash[6] + '(' + temp[0] + ')'
		engine = splitbydash[4]
		filepath = product + '/' + engine + '/' + version + '/' + imagecode
		filemove (filepath, filename)

def ipssig (filename):
	product = 'IPS'
	imagecode = 'SIGNATURES'
	splitbydash = filename.split('-')
	version = splitbydash[2]
	engine = splitbydash[4].split('.')
	filepath = product + '/' + engine[0] + '/' + imagecode + '/' + version
	filemove (filepath, filename)


def ipssystem (filename):
	product = 'IPS'
	imagecode = 'SYSTEM UPGRADE'
	splitbydash = filename.split('-')
	if splitbydash[2] == 'sp':
		splitbydot = splitbydash[4].split('.')
		version = splitbydash[3] + '(' + splitbydot[0] + ')'
		filepath = product + '/' + 'E0' + '/' + version + '/' + imagecode
	else:
		version = splitbydash[2] + '(' + splitbydash[3] + ')'
		engine = splitbydash[4].split('.')
		filepath = product + '/' + engine[0] + '/' + version + '/' + imagecode
	filemove (filepath, filename)


def csm4 (filename):
	product = 'Cisco Security Manager'
	splitbydash = filename.split('-')
	if splitbydash[3] == 'rme':
		imagecode = 'RESOURCE MANAGER ESSENTIALS'
	if splitbydash[3] == 'mcp':
		imagecode = 'MONITORING CENTER FOR PERFORMANCE'
	if splitbydash[3] == 'sp1':
		imagecode = 'SERVICE PACK 1'
	if splitbydash[3] == 'sp2':
		imagecode = 'SERVICE PACK 2'
	if splitbydash[3] == 'sp3':
		imagecode = 'SERVICE PACK 3'
	if splitbydash[3] == 'sp4':
		imagecode = 'SERVICE PACK 4'
	if splitbydash[3] == 'sp5':
		imagecode = 'SERVICE PACK 5'
	if splitbydash[3] == 'win':
		imagecode = 'INSTALL'
	if splitbydash[3] == 'w2k':
		imagecode = 'INSTALL'
	splitall = list(splitbydash[2])
	splitbydash = splitbydot[0].split("-")
	version = splitall[0] + '.' + splitall[1] + '.' + splitall[2]
	filepath = product + '/' + version + '/' + imagecode
	filemove (filepath, filename)


def csmmcp (filename):
	product = 'Cisco Security Manager'
	imagecode = 'MANAGEMENT CENTER FOR PERFORMANCE'
	splitbydash = filename.split('-')
	if splitbydash[2] == '40':
		version = '4.0.0'
	elif splitbydash[2] == 'v30':
		version = '3.0.0'
	elif splitbydash[2] == 'v31':
		version = '3.1.0'
	else:
		splitall = list(splitbydash[2])
		version = splitall[0] + '.' + splitall[1] + '.' + splitall[2]
	filepath = product + '/' + version + '/' + imagecode
	filemove (filepath, filename)



def asr1000 (filename, prodname, imagecode):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
#	splitbydot[1] = splitbydot[1].lstrip('0')
#	splitbydot[2] = splitbydot[2].lstrip('0')
#	splitbydot[3] = splitbydot[3].lstrip('0')
#	splitbydot[4] = splitbydot[4].rstrip('t')
#	splitbydot[5] = splitbydot[5].rstrip('t')
	if splitbydot[3] =='bin':
		mysplit = splitbydot[1].split('-')
		main = list(mysplit[0])
		iosprimary = splitbydot[1] + '.' + splitbydot[2]
#		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '-' + main[0] + main[1] + '.' + main[2] + '(' + mysplit[1] + ')' + splitbydot[6]
		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	elif splitbydot[4] =='S':
		mysplit = splitbydot[5].split('-')
		main = list(mysplit[0])
		iosprimary = splitbydot[1] + '.' + splitbydot[2]
#		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '-' + main[0] + main[1] + '.' + main[2] + '(' + mysplit[1] + ')' + splitbydot[6]
		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	elif splitbydot[4] =='SPA':
		mysplit = splitbydot[5].split('-')
		main = list(mysplit[0])
		iosprimary = splitbydot[1] + '.' + splitbydot[2]
		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	else:
		mysplit = splitbydot[4].split('-')
		main = list(mysplit[0])
		iosprimary = splitbydot[1] + '.' + splitbydot[2]
#		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3] + '-' + main[0] + main[1] + '.' + main[2] + '(' + mysplit[1] + ')' + splitbydot[5]
		iosversion = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
	filemove (filepath, filename)

def cat29003500 (filename, prodname, imagecode):
	myworkname = filename.replace(".tar", "")
	myworkname = myworkname.replace(".bin", "")

	splitbydash = myworkname.split('-')
	splitbydot = myworkname.split('.')

#c3500XL-c3h2s-mz.120-5.4.WC.1.bin
#c3500XL-c3h2s-mz.120-5.4.WC.1
#c3500xl-c3h2s-mz.120-5.WC2.tar
#c3500xl-c3h2s-mz.120-5.WC2
#	print (len(splitbydot), end='\n')
	if len(splitbydot) == 3:
		#listver = stringtolist (splitbydot[0])
#		if splitbydot[1] == '120-5':
		if splitbydot[1] == '120-5':
			if splitbydot[2].startswith("XW"):
				iosversion = '12.0XW'
				iosmain ='12.0(5)'
				filepath = prodname + '/' + iosversion + '/' + iosmain + splitbydot[2] + '/' + imagecode
				filemove (filepath, filename)
			elif splitbydot[2].startswith("WC"):
				iosversion = '12.0WC'
				iosmain ='12.0(5)'
				filepath = prodname + '/' + iosversion + '/' + iosmain + splitbydot[2] + '/' + imagecode
				filemove (filepath, filename)
	#		elif splitbydot[2].startswith("SA"):
	#			iosversion = '11.2SA'
	#			iosmain ='11.2(8)'
	#			filepath = prodname + '/' + iosversion + '/' + iosmain + splitbydot[2] + '/' + imagecode
	#			filemove (filepath, filename)
	#	elif splitbydash[3] == '112.8':
	#		elif splitbydash[4].startswith("SA"):
	#			iosversion = '11.2SA'
	#			iosmain ='11.2(8)'
	#			filepath = prodname + '/' + iosversion + '/' + iosmain + splitbydot[2] + '/' + imagecode
	#			filemove (filepath, filename)


#	if len(splitbydash) == '4':
#		if splitbydash[1] == "hs" and splitbydash[2] == "mz":
##			version = splitbydot[4].replace(".bin", "")
##			version = splitbydot[4].replace(".tar", "")
#			splitbydot = filename.split('.')
#			listver = stringtolist (splitbydot[0])
#			iosmain = util3digit (listver[0],listver[1],listver[2])
#			iosversion = iosmain + '(' + splitbydot[1] + ')' + splitbydot[2] + '(' + splitbydot[4] + ')'
#			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
#			print(filepath)
#		#	filemove (filepath, filename)
		
#	if len(splittest) == '6':
#		workname = filename.rstrip(".bin")
#		splitbydash = workname.split('-')
#		firstver = splitbydash[3].split('.')
#		mainver = list(firstver[0])
#		iosprimary = mainver[0] + mainver[1] + '.' + mainver[2]
#		iosversion  = iosprimary + '(' + firstver[1] + ')' + firstver[2] + '(' + splitbydash[5] + ')'
#		filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
##		print(filepath)
#		filemove (filepath, filename)
#	else:
#		splitbydot = filename.split('.')
#		splitbydash = splitbydot[1].split('-')
#		mainver = list(splitbydash[0])
#		iosprimary = mainver[0] + mainver[1] + '.' + mainver[2]
#		iosversion  = iosprimary + '(' + splitbydash[1] + ')' + splitbydot[2]
#		filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
##		print(filepath)
#		filemove (filepath, filename)


def m9100class (filename):
	product = 'MDS 9100'
	mds9100 = filename.split(".")
	if mds9100[0] == 'm9100-s1ek9-kickstart-mz':
		imagecode = 'KICKSTART'
		gencode = 'GEN 1'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	elif mds9100[0] == 'm9100-s1ek9-mz':
		imagecode = 'SYSTEM-SOFTWARE'
		gencode = 'GEN 1'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	elif mds9100[0] == 'm9100-s2ek9-mz':
		imagecode = 'SYSTEM-SOFTWARE'
		gencode = 'GEN 2'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	elif mds9100[0] == 'm9100-s2ek9-kickstart-mz':
		imagecode = 'KICKSTART'
		gencode = 'GEN 2'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	elif mds9100[0] == 'm9100-s3ek9-mz':
		imagecode = 'SYSTEM-SOFTWARE'
		gencode = 'GEN 3'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	elif mds9100[0] == 'm9100-s3ek9-kickstart-mz':
		imagecode = 'KICKSTART'
		gencode = 'GEN 3'
		mds9100primary = mds9100[1] + '.' + mds9100[2]
		mds9100ver = mds9100[1] + '.' + mds9100[2] + '(' + mds9100[3] + ')'
		filepath = product + '/' + gencode +'/' + mds9100primary + '/' + mds9100ver + '/' + imagecode
		filemove (filepath, filename)
	

def m9200 (filename, prodname):
	if prodname == 'UNKNOWN':
		messageunknowndev()
	else:
		splitbydash = name.split("-")
		splitbydot = name.split(".")
		if splitbydash[2].startswith('kickstart'):
			imagecode = 'KICKSTART'
		elif splitbydash[2].startswith('mz'):
			imagecode = 'SYSTEM-SOFTWARE'
		if splitbydash[1] == 'ek9':
			gen = 'GEN 1'
		elif splitbydash[1] == 's2ek9':
			gen = 'GEN 2'
		mdsprimary = splitbydot[1] + '.' + splitbydot[2]
		mdsver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + gen + '/' + mdsprimary + '/' + mdsver + '/' + imagecode
		filemove (filepath, filename)


def m9250 (filename, product):
	product = 'MDS 9250'
	splitbydash = name.split("-")
	splitbydot = name.split(".")
	
	nxosmain = splitbydot[1] + '.' + splitbydot[2]
	nxosfull = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
	
	if splitbydash[2] == 'kickstart':
		imagecode = 'KICKSTART'
		try:
			splitbydash[4] == 'npe'
		except:
			imagecode = 'KICKSTART'
			filepath = product + '/' + nxosmain +'/' + nxosfull + '/' + imagecode
			filemove (filepath, filename)
		else:
			imagecode = 'KICKSTART NO CRYPTO'
			filepath = product + '/' + nxosmain +'/' + nxosfull + '/' + imagecode
			filemove (filepath, filename)
	elif splitbydash[2] == 'mz':
		imagecode = 'SYSTEM'
		try:
			splitbydash[3] == 'npe'
		except:
			imagecode = 'SYSTEM'
			filepath = product + '/' + nxosmain +'/' + nxosfull + '/' + imagecode
			filemove (filepath, filename)
		else:
			imagecode = 'SYSTEM NO CRYPTO'
			filepath = product + '/' + nxosmain +'/' + nxosfull + '/' + imagecode
			filemove (filepath, filename)

def m9500class (filename):
	mds9500 = name.split(".")
	if mds9500[0] == 'm9500-sf1ek9-kickstart-mz':
		product = 'MDS-9500'
		imagecode = 'KICKSTART'
		supcode = 'SUP-1'
		imagetype = '1'
	elif mds9500[0] == 'm9500-sf1ek9-mz':
		product = 'MDS-9500'
		imagecode = 'SYSTEM-SOFTWARE'
		supcode = 'SUP-1'
		imagetype = '1'
	elif mds9500[0] == 'm9500-sf2ek9-kickstart-mz':
		product = 'MDS-9500'
		imagecode = 'KICKSTART'
		imagetype = '1'
		supcode = 'SUP-2'
	elif mds9500[0] == 'm9500-sf2ek9-mz':
		product = 'MDS-9500'
		imagecode = 'SYSTEM-SOFTWARE'
		supcode = 'SUP-2'
		imagetype = '1'
	elif mds9500[0] == 'm9700-sf3ek9-kickstart-mz':
		product = 'MDS-9700'
		imagecode = 'KICKSTART'
		supcode = 'SUP-3'
		imagetype = '1'
	elif mds9500[0] == 'm9700-sf3ek9-mz':
		product = 'MDS-9700'
		imagecode = 'SYSTEM'
		supcode = 'SUP-3'
		imagetype = '1'
	elif mds9500[0] == 'm9000-epld-1':
		product = 'MDS-9500'
		imagecode = 'EPLD'
		imagetype = '2'
	elif mds9500[0] == 'm9000-epld-2':
		product = 'MDS-9500'
		imagecode = 'EPLD'
		imagetype = '2'
	elif mds9500[0] == 'm9000-epld-3':
		product = 'MDS-9500'
		imagecode = 'EPLD'
		imagetype = '2'
	elif mds9500[0] == 'm9000-epld-4':
		product = 'MDS-9500'
		imagecode = 'EPLD'
		imagetype = '2'
	elif mds9500[0] == 'm9000-epld-5':
		product = 'MDS-9500'
		imagecode = 'EPLD'
		imagetype = '2'
	elif mds9500[0] == 'm9000-ek9-ssi-mz':
		product = 'MDS-9500'
		imagecode = 'SSI'
		imagetype = '3'
	if imagetype == '1':
		mds9500primary = mds9500[1] + '.' + mds9500[2]
		mds9500ver = mds9500[1] + '.' + mds9500[2] + '(' + mds9500[3] + ')'
		filepath = product + '/' + supcode + '/' + mds9500primary + '/' + mds9500ver + '/' + imagecode
		filemove (filepath, filename)
	elif imagetype == '2':
		vercode = name.lstrip("m9000-epld-")
		thisver = vercode.split(".")
		mds9500primary = thisver[0] + '.' + thisver[1]
		mds9500ver = thisver[0] + '.' + thisver[1] + '(' + thisver[2] + ')'
		filepath = product + '/' + imagecode + '/' + mds9500primary + '/' + mds9500ver
		filemove (filepath, filename)
	elif imagetype == '3':
		mds9500primary = mds9500[1] + '.' + mds9500[2]
		mds9500ver = mds9500[1] + '.' + mds9500[2] + '(' + mds9500[3] + ')'
		filepath = product + '/' + imagecode + '/' + mds9500primary + '/' + mds9500ver
		filemove (filepath, filename)
	

def standardios (filename, prodname, imagecode):
	
	if prodname == 'UNKNOWN':
		messageunknowndev()
	elif imagecode == 'UNKNOWN':
		messageunknownfeat()
	else:
		splitbydot = filename.split('.')
		splitbydash = filename.split('-')
		myver = splitbydot[1].split('-')
		
		mynum = list(myver[0])
		thiscontrol = 0
		for myios in mynum:
			if thiscontrol == 0:
				iosversion = myios
				iosprimary = myios
				thiscontrol = thiscontrol + 1
			elif thiscontrol == 1:
				iosversion = iosversion + myios + '.'
				iosprimary = iosprimary + myios + '.'
				thiscontrol = thiscontrol + 1
			elif thiscontrol == 2:
				iosversion = iosversion + myios
				iosprimary = iosprimary + myios
				thiscontrol = thiscontrol + 1
				
		if splitbydot[2] == 'bin':
			iosversion = iosversion + '(' + myver[1] + ')'
		else:
			iosprimary = iostrain(splitbydot[2], iosprimary)
			iosversion = iosversion + '(' + myver[1] + ')' + splitbydot[2]
		if prodname == 'Catalyst-6500' and imagecode == 'FIELD PROGRAMABLE DEVICE':
			filepath = prodname + '/' + imagecode + '/' + iosprimary + '/' + iosversion
		elif splitbydash[0] == 'c7600' and splitbydot[1] == '122-18':
			filepath = 'Catalyst-6500' + '/' + imagecode + '/' + iosprimary + '/' + iosversion
		elif prodname == '7600' and imagecode == 'FIELD PROGRAMABLE DEVICE':
			filepath = prodname + '-' + imagecode + '/' + iosprimary + '/' + iosversion
		elif splitbydot[0] == 's3223-adventerprisek9_wan-vz' or splitbydot[0] == 's72033-adventerprisek9_wan-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-adventerprise_wan-vz' or splitbydot[0] == 's72033-adventerprise_wan-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-advipservicesk9_wan-vz' or splitbydot[0] == 's72033-advipservicesk9_wan-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-ipbase-vz' or splitbydot[0] == 's72033-ipbase-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-ipbasek9-vz' or splitbydot[0] == 's72033-ipbasek9-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-ipservicesk9_wan-vz' or splitbydot[0] == 's72033-ipservicesk9_wan-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		elif splitbydot[0] == 's3223-ipservicesk9-vz' or splitbydot[0] == 's72033-ipservicesk9-vz':
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode + ' - MODULAR'
		else:
			filepath = prodname + '/' + iosprimary + '/' + iosversion + '/' + imagecode
		filemove (filepath, filename)

def isr4k (filename, prodname, imagecode):
	if filename.startswith('isr4200-hw-programmables'):
		prodname = product ('isr4200')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4300-hw-programmables'):
		prodname = product ('isr4300')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4400-hw-programmables'):
		prodname = product ('isr4400')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4400v2-hw-programmables'):
		prodname = product ('isr4400v2')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4200-firmware_nim_xdsl'):
		prodname = product ('isr4200')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4300-firmware_nim_xdsl'):
		prodname = product ('isr4300')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename.startswith('isr4400-firmware_nim_xdsl'):
		prodname = product ('isr4400')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename == "nim_vab_phy_fw_A39x3_B39x3_Bond39t.pkg":
		prodname = product ('isr4300')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	elif filename == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg":
		prodname = product ('isr4300')
		filepath = prodname + '/' + 'Hardware'
		filemove (filepath, filename)
	else:
		splitbydot = filename.split('.')
		splitbydash = filename.split('-')
		splitbydot[3] = splitbydot[3].replace("-serial", "")
		iosmain = util2digit (splitbydot[1],splitbydot[2])
		iosversion = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
		if prodname == 'UNKNOWN':
			messageunknowndev()
		elif imagecode == 'UNKNOWN':
			messageunknownfeat()
		elif imagecode == 'IOS-XE-SD-WAN':
			prodname = 'IOS-XE-SD-WAN' + '/' + prodname
			#workname = splitbydot[3].rstrip('-serial')
			splitbydot[3] = splitbydot[3].replace("-serial", "")
			if imagecode == 'SPA':
				filepath = prodname + '/' + iosmain + '/' + iosversion
			else:
				filepath = prodname + '/' + iosmain + '/' + iosversion + '/' + imagecode
			filemove (filepath, filename)
		elif splitbydot[4].startswith('CSC') and splitbydot[6]  == 'smu':
			filepath = prodname + '/' + iosmain + '/' + iosversion + '/' + 'SMU' + '/' + splitbydot[4]
			filemove (filepath, filename)
		else:
			if imagecode == 'SPA':
				filepath = prodname + '/' + iosmain + '/' + iosversion
			else:
				filepath = prodname + '/' + iosmain + '/' + iosversion + '/' + imagecode
			filemove (filepath, filename)

def ucschuu (filename):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	if splitbydash[1] == 'c200':
		product = 'UCS/C-SERIES/HOST UPGRADE UTILITY/C200'
	elif splitbydash[1] == 'c220':
		product = 'UCS/C-SERIES/HOST UPGRADE UTILITY/C220'
	elif splitbydash[1] == 'c220m4':
		product = 'UCS/C-SERIES/HOST UPGRADE UTILITY/C220-M4'
	elif splitbydash[1] == 'c240':
		product = 'UCS/C-SERIES/HOST UPGRADE UTILITY/C240'
	vername = splitbydash[3]
	vername = vername.strip ('.iso')
	filepath = product + '/' + vername
	filemove (filepath, filename)

def ucscdrivers (filename):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	if splitbydash[1] == 'cxxx':
		product = 'UCS/DRIVERS-C-SERIES'
	elif splitbydash[1] == 'c2xx':
		product = 'UCS/DRIVERS-C-SERIES'
	elif splitbydash[1] == 'bxxx':
		product = 'UCS/DRIVERS-B-SERIES'
	elif splitbydash[1] == 'b2xx':
		product = 'UCS/DRIVERS-B-SERIES'
	versionmain = splitbydot[1] + '.' + splitbydot[2]
	versionfull = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
	filepath = product + '/' + versionmain + '/' + versionfull
	filemove (filepath, filename)

def iosxrv9k (filename):
	splitbydash = filename.split('-')
	prodname = product("iosxrvfull")
	number = list (splitbydash[3])
	iosmain = util2digit (number[0],number[1])
	iosfull = util3digit (number[0],number[1],number[2])
	filepath = prodname + '/' + iosmain + '/' + iosfull + '/'
	filemove (filepath, filename)

def asr9k (filename):
	splitbydash = filename.split('-')
	prodname = product("asr9k")
	filepath = prodname + '/'
	filemove (filepath, filename)

def iosxrv (filename, prodname, imagecode):

	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	splitbydot2 = splitbydash[3].split('.')
	if splitbydash[2] == 'k9':
		iosmain = splitbydot2[0] + '.' + splitbydot2[1]
		iosfull = splitbydot2[0] + '.' + splitbydot2[1] + '.' + splitbydot2[2]
		filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode
		filemove (filepath, filename)
	else:
		imagecode = 'DEMO WITH CRYPTO'
		iosmain = splitbydash2[3] + '.' + splitbydot[1]
		iosfull = splitbydash2[3] + '.' + splitbydot[1] + '.' + splitbydot[2]
		filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode
		filemove (filepath, filename)

def ios_xe_signature (filename):
	splitbydash = filename.split('-')
	prodname = 'IOS-XE-UTD'
	prodcode = 'SIGNATURES'
	filepath = prodname + '/' + prodcode + '/' + splitbydash[3] + '/' + splitbydash[4]
	filemove (filepath, filename)

def waas (filename):
	prodname = "WAAS"
	splitbydot = name.split('.')
	splitbydash = name.split('-')


	if splitbydash[0] == 'waas':
		if splitbydash[1] == 'x86_64':
			localdotsplit = splitbydash[2].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if splitbydash[3] == 'npe':
				imagecode = 'SYSTEM-SOFTWARE - 64bit-NPE'
			else:
				imagecode = 'SYSTEM-SOFTWARE - 64bit'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'universal':
			localdotsplit = splitbydash[2].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if splitbydash[3] == 'npe':
				imagecode = 'SYSTEM-SOFTWARE-UNIVERSAL-NPE'
			else:
				imagecode = 'SYSTEM-SOFTWARE-UNIVERSAL'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydot[4] == 'sysimg':
			localdotsplit = splitbydash[1].split('.')
			mylead = localdotsplit[0].lstrip('waas-')
			mainver = mylead[0] + '.' + localdotsplit[1]
			fullver = mylead[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'SYSTEM-SOFTWARE-32bit-NPE'
			else:
				imagecode = 'SYSTEM-SOFTWARE-32bit'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'accelerator':
			localdotsplit = splitbydash[2].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'ACCELERATOR-NPE'
			else:
				imagecode = 'ACCELERATOR'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'kdump' and splitbydash[2] == 'addon':
			localdotsplit = splitbydash[3].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'KDUMP-ADDON-NPE'
			else:
				imagecode = 'KDUMP-ADDON'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'kdump':
			localdotsplit = splitbydash[2].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'KDUMP-NPE'
			else:
				imagecode = 'KDUMP'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'rescue' and splitbydash[2] == 'cdrom':
			localdotsplit = splitbydash[3].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'RESCUE-CD-NPE'
			else:
				imagecode = 'RESCUE-CD'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)

		elif splitbydash[1] == 'rescue' and splitbydash[2] == 'cdrom':
			localdotsplit = splitbydash[3].split('.')
			mainver = localdotsplit[0] + '.' + localdotsplit[1]
			fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
			if "npe" in name or  "NPE" in name:
				imagecode = 'RESCUE-CD-NPE'
			else:
				imagecode = 'RESCUE-CD'
			filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
			filemove (filepath, filename)


	elif splitbydash[1] == 'vWAAS':
		if splitbydash[2] == '150':
			capacity = '150-Users'
		elif splitbydash[2] == '200':
			capacity = '200-Users'
		elif splitbydash[2] == '750':
			capacity = '750-Users'
		elif splitbydash[2] == '1300':
			capacity = '1300-Users'
		elif splitbydash[2] == '2500':
			capacity = '2500-Users'
		elif splitbydash[2] == '6k':
			capacity = '6000-Users'
		localdotsplit = splitbydash[3].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
		if splitbydash[4] == 'npe':
			imagecode = 'vWAAS - VMWare-NPE'
		else:
			imagecode = 'vWAAS - VMWare'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == 'Hv' and splitbydash[2] == 'vWAAS':
		if splitbydash[3] == '150':
			capacity = '150-Users'
		elif splitbydash[3] == '200':
			capacity = '200-Users'
		elif splitbydash[3] == '750':
			capacity = '750-Users'
		elif splitbydash[3] == '1300':
			capacity = '1300-Users'
		elif splitbydash[3] == '2500':
			capacity = '2500-Users'
		elif splitbydash[3] == '6k':
			capacity = '6000-Users'
		localdotsplit = splitbydash[4].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
#		if len(splitbydash) == '7':
#			if splitbydash[7] == 'npe.zip':
		if "npe" in name:
			imagecode = 'vWAAS - HyperV-NPE'
		else:
			imagecode = 'vWAAS - HyperV'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == 'ISR' and splitbydash[1] == 'WAAS':
		localdotsplit = splitbydash[2].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
#		if len(splitbydash) == '7':
#			if splitbydash[7] == 'npe.zip':
		if "npe" in name or  "NPE" in name:
			imagecode = 'ISR-NPE'
		else:
			imagecode = 'ISR'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == 'sre':
		localdotsplit = splitbydash[3].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
		if "npe" in name or  "NPE" in name:
			imagecode = 'SM-SRE-NPE'
		else:
			imagecode = 'SM-SRE'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

	elif splitbydash[1] == 'alarm':
		localdotsplit = splitbydash[4].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2]
		if "npe" in name or  "NPE" in name:
			imagecode = 'ALARM-ERROR BOOKS-NPE'
		else:
			imagecode = 'ALARM-ERROR BOOKS'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

	elif splitbydash[0] == 'WAAS' or splitbydash[0] == 'waas':
		localdotsplit = splitbydash[1].split('.')
		mainver = localdotsplit[0] + '.' + localdotsplit[1]
		fullver = localdotsplit[0] + '.' + localdotsplit[1] + '.' + localdotsplit[2] + '.' + localdotsplit[3]
		if "sysimg" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'SYSTEM-SOFTWARE-32bit-NPE'
			else:
				imagecode = 'SYSTEM-SOFTWARE-32bit'
		elif "bin" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'BOOT-NPE'
			else:
				imagecode = 'BOOT'
		elif "rescue" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'RESCUE CD-NPE'
			else:
				imagecode = 'RESCUE CD'
		elif "Doc" in name or "DOC" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'DOCUMENTATION-NPE'
			else:
				imagecode = 'DOCUMENTATION'
		elif "npe" in name or  "NPE" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'SM-SRE-NPE'
			else:
				imagecode = 'SM-SRE'
		elif "npe" in name or  "NPE" in name:
			if "npe" in name or  "NPE" in name:
				imagecode = 'ALARM-ERROR BOOKS-NPE'
			else:
				imagecode = 'ALARM-ERROR BOOKS'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
		filemove (filepath, filename)

def aci (filename):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	product = "APIC"
	if splitbydot[0].startswith('Cisco_ACI_Virtual_Edge_'):
		workname = filename.rstrip('-pkg.zip')
		workname = workname.lstrip('Cisco_ACI_Virtual_Edge_')
		splitbydot = workname.split('.')
		versiontwo = splitbydot[0] + '.' + splitbydot[1]
		versionthree = splitbydot[0] + '.' + splitbydot[1] + '(' + splitbydot[2] + ')'
		filepath = product + '/ACI-VIRTUAL-EDGE/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)
	elif splitbydash[0] == 'aci' and splitbydash[1] == 'apic' and splitbydash[2].startswith('dk9'):
		versiontwo = splitbydot[1] + '.' + splitbydot[2]
		versionthree = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = product + '/APIC-CONTROLLER/' + '/' + versiontwo + '/' + versionthree 
		filemove (filepath, filename)
	elif splitbydash[0] == 'aci' and splitbydash[1] == 'n9000' and splitbydash[2].startswith('dk9'):
		versiontwo = splitbydot[1] + '.' + splitbydot[2]
		versionthree = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = product + '/NEXUS-9000-ACI-MODE/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)
	elif splitbydash[0] == 'aci' and splitbydash[1] == 'msft' and splitbydash[2] == 'pkg':
		workname = filename.lstrip('aci-msft-pkg-')
		splitbydot = workname.split('.')
		versiontwo = splitbydot[0] + '.' + splitbydot[1]
		versionthree = splitbydot[0] + '.' + splitbydot[1] + '(' + splitbydot[2] + ')'
		filepath = product + '/MICROSOFT-PLUGIN/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)
	elif splitbydash[0] == 'apic' and splitbydash[1] == 'vrealize':
		workname = filename.lstrip('apic-vrealize-')
		splitbydot = workname.split('.')
		versiontwo = splitbydot[0] + '.' + splitbydot[1]
		versionthree = splitbydot[0] + '.' + splitbydot[1] + '(' + splitbydot[2] + ')'
		filepath = product + '/VREALIZE-PLUGIN/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)
	elif splitbydash[0] == 'vcenter' and splitbydash[1] == 'plugin':
		workname = filename.lstrip('vcenter-plugin-')
		splitbydot = workname.split('.')
		versiontwo = splitbydot[0] + '.' + splitbydot[1]
		versionthree = splitbydot[0] + '.' + splitbydot[1] + '(' + splitbydot[2] + ')'
		filepath = product + '/VCENTER-PLUGIN/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)
	elif splitbydash[0] == 'aci' and splitbydash[1] == 'msft' and splitbydash[2] == 'pkg':
		workname = filename.lstrip('aci-msft-pkg-')
		splitbydot = workname.split('.')
		versiontwo = splitbydot[0] + '.' + splitbydot[1]
		versionthree = splitbydot[0] + '.' + splitbydot[1] + '(' + splitbydot[2] + ')'
		filepath = product + '/NEXUS-9000-ACI-MODE/'  + '/' + versiontwo + '/' + versionthree
		filemove (filepath, filename)


def cat9k (filename):
####	if filename.startswith('cat9k_iosxeldpe'):
####		imagecode = imagelookup ('cat9k_iosxeldpe')
####		print (imagecode, end="\n")
####		iosxethreedigit(filename,prodname,imagecode)
####	elif filename.startswith('cat9k_iosxe'):
####		imagecode = imagelookup ('cat9k_iosxe')
####		print (imagecode, end="\n")
####		iosxethreedigit(filename,prodname,imagecode)
####	elif filename.startswith('cat9k_iosxe_npe'):
####		imagecode = imagelookup ('cat9k_iosxe_npe')
####		print (imagecode, end="\n")
####		iosxethreedigit(filename,prodname,imagecode)
####	elif filename.startswith('cat9k_lite_iosxe'):
####		imagecode = imagelookup ('cat9k_lite_iosxe')
####		print (imagecode, end="\n")
####		iosxethreedigit(filename,prodname,imagecode)
####	elif filename.startswith('cat9k_lite_iosxe_npe'):
####		imagecode = imagelookup ('cat9k_lite_iosxe_npe')
####		print (imagecode, end="\n")
	splitbydot = filename.split('.')
	prodname = product ('cat9k')
	imagecode = imagelookup (splitbydot[0])
	iosxethreedigit(filename,prodname,imagecode)

def iosxeclassification (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	if prodname == 'UNKNOWN':
		messageunknowndev()
	elif imagecode == 'UNKNOWN':
		messageunknownfeat()
	else:
		if splitbydot[1] == '03':
			iosxevthree(filename,prodname,imagecode)
		elif splitbydot[1] == '17':
			iosxethreedigit(filename,prodname,imagecode)
		elif splitbydot[1] == '16':
			iosxethreedigit(filename,prodname,imagecode)
		else:
			iosxevthree(filename,prodname,imagecode)

def iosxevthree (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	if splitbydot[1] == '02':
		iosmain = splitbydot[1] + '.' + splitbydot[2]
		iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
		filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode
		filemove (filepath, filename)
	elif (splitbydot[7] == 'pkg' or 
	 splitbydot[7] == 'bin'):
		iosmain = splitbydot[1] + '.' + splitbydot[2]
		iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
		filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode
		filemove (filepath, filename)

def iosxethreedigit (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	splitbydot[3] = splitbydot[3].replace("-serial", "")
	splitbydot[3] = splitbydot[3].replace("-nfvis", "")
	splitbydot[3] = splitbydot[3].replace("-esxi", "")
	splitbydot[3] = splitbydot[3].replace("-kvm", "")
	#Checks to make sure that it is a regular firmware image, not a SMU
	if splitbydot[4] == 'SPA' or splitbydot[4] == 'run' or splitbydot[4] == 'iso' or splitbydot[4] == 'ova' or splitbydot[4] == 'qcow2' or splitbydot[4] == 'tar':
	#	iosmain = splitbydot[1] + '.' + splitbydot[2]
	#	iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
	#	filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode
		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,iosmain,iosfull,imagecode)
		filemove (filepath, filename)
	elif splitbydot[4].startswith('CSC') and splitbydot[6]  == 'smu':
		#iosmain = splitbydot[1] + '.' + splitbydot[2]
		#iosfull = splitbydot[1] + '.' + splitbydot[2] + '.' + splitbydot[3]
#		filepath = prodname + '/' + 'SMU' + '/' + iosfull + '/' + splitbydot[4]
#		iosmain = util2digit(splitbydot[1],splitbydot[2])
		iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = filepath4(prodname,'SMU',iosfull,splitbydot[4])
		filemove (filepath, filename)


def scriptusage ():
	print ("-h: This Help Messagen")
	print ("-d: Directory\n")
	print ("-h: Compute MD5 hash\n")

#def fileprocessorios (filename):

#def fileprocessoriosxe (filename):

#def fileprocessoriosxr (filename):

def fileprocessorasa (filename):
	if filename == 'anyconnect_app_selector_2.0.zip':
		filepath = 'ASA/APP-SELECTOR/2.0/'
		filemove (filepath, filename)
	elif filename.startswith("hostscan"):
		filepath = 'ASA/Hostscan/'
		filemove (filepath, filename)
	else:
		filepath = 'ASA/'
		filemove (filepath, filename)

def fileprocessorfirepower (filename):
	if filename.startswith('Sourcefire_Rule'):
		fileprocessorfprules (filename)
	elif filename.startswith('Sourcefire_VDB'):
		fileprocessorfpvdb (filename)
	elif filename.startswith('Sourcefire_Geodb'):
		fileprocessorfpgeodb (filename)

#def fileprocessorwireless (filename):

def fileprocessorrommon (filename):
	filepath = "ROMMON/"
	filemove (filepath, filename)

def fileprocessorpagent (filename):
	filepath = "Routers/PAGENT/"
	filemove (filepath, filename)

def filepreprocessor (filename):
	if filename.startswith("iosxrv") or filename.startswith("fullk9"):
		fileprocessoriosxr(filename)
	elif filename.startswith("asa") or filename.startswith("hostscan") or "anyconnect" in filename:
		fileprocessorasa(filename)

def toplevel(filename):
	src = filename
	names = os.listdir(src)
	os.chdir(src)
	for name in names:
		if os.path.isdir(name):
			continue	
		elif name.endswith('.part'):
			continue
		
		print(name)
		
		splitbydot = name.split('.')
		classify = name.split('-')
		splitbydash = name.split('-')
		splitbydashsub = splitbydot[0].split('-')
		
		thisstring = splitbydot.pop()
		splitbydot.append(thisstring)

		if name == "Thumbs.db":
			continue
		elif name.endswith("DS_Store"):
			continue
		elif name.endswith("hash"):
			continue
#		elif name.endswith("pdf"):
#			continue
		elif name.endswith("part"):
			continue
		
		chars3 = name[0:3]
		chars4 = name[0:4]
		chars5 = name[0:5]
		chars6 = name[0:6]
		chars7 = name[0:7]
		chars8 = name[0:8]
		chars9 = name[0:9]
		chars10 = name[0:10]
		
		if name.startswith("asa") or name.startswith("hostscan") or "anyconnect" in name:
			filepreprocessor (name)

		elif name.startswith("ata"):
			fileprocessorvoice(name)

		elif "tsjspgen" in name or "tpcgen" in name or "tpgen" in name or "tpcgenx" in name or "tscgen" in name or "tscgenx" in name:
			fileprocessorpagent(name)

		elif(
		"srec" in name or 
		"rommon" in name or 
		"ROMMON" in name or 
		"promupgrade" in name or 
		"governator" in name or 
		"C7200_NPEG2_RM" in name or 
		"c6880x_rm" in name or 
		name == "Rommon-123-8r.YH13-notes" or 
		name == "Rommon-124-22r.YB5-notes" or 
		name == "Rommon-151-1r.T5-notes" or 
		name == "Rommon-150-1r.M12-notes" or 
		name.startswith('firmwareupgrade')
		):
			fileprocessorrommon(name)

		elif (
		name.startswith('n3000') or 
		name.startswith('n3500') or 
		name.startswith('n4000') or 
		name.startswith('n5000') or 
		name.startswith('n6000') or 
		name.startswith('n7000') or 
		name.startswith('n7700') or 
		name.startswith('n9000') or 
		name.startswith('nxosv') or 
		name.startswith('nxos') or 
		name.startswith('n5000_poap_script') or 
		name.startswith('n6000_poap_script') or 
		name.startswith('poap_ng') or 
		name.startswith('Nexus1000v') or 
		name.startswith('Nexus1000v') or 
		name.startswith('Nexus1000V') or 
		name.startswith('Nexus1000V5') or 
		name.startswith('n1000vh-dk9') or 
		name.startswith('nexus-1000v') or 
		name == "n3k_bios_release_rn.pdf"
		):
			fileprocessornxos(name)

		elif name.startswith('cmterm'):
			fileprocessorvoice(name)

		elif name == "nim_vab_phy_fw_A39x3_B39x3_Bond39t.pkg":
			imagecode = imagelookup ('isr4300')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg":
			imagecode = imagelookup ('isr4300')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name == "nim_vab_phy_fw_A39t_B39g1_Bond39t.pkg":
			imagecode = imagelookup ('isr4300')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('isr4200-firmware_nim_xdsl'):
			prodname = product ('isr4200')
			imagecode = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('isr4300-firmware_nim_xdsl'):
			imagecode = imagelookup ('isr4300')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('isr4400-firmware_nim_xdsl'):
			imagecode = imagelookup ('isr4400')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('isr4400v2-firmware_nim_xdsl'):
			imagecode = imagelookup ('isr4400v2')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('isr4300-hw-programmables'):
			imagecode = imagelookup ('isr4300')
			prodname = "Hardware"
			isr4k(name,imagecode,prodname)

		elif name.startswith('DNAC') or name.startswith('dnac'):
			imagecode = product ('dnac')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "cat9k_iosxe.16.00.00fpgautility.SPA.bin":
			prodname = product ('cat9k')
			imagecode = "Hardware"
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "MC7700_03.05.29.02_00_generic_000.000_001.cwe" or name == "MC7700_ATT_03.05.10.02_00.cwe":
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICCELLATT")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "MC7750_VZW_03.05.10.06_00.cwe":
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICCELLVZW")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "MC7710_Global_03.05.29.02.cwe":
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICCELLEU")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "MC7710_Global_03.05.24.00A.cwe":
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICCELLG")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name == "MC7700_03.05.29.03_00_generic_000.000_001.cwe":
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICCELLBE")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('n5000_poap_script'):
			prodname = product ('n5000')
			imagecode = imagelookup (splitbydot[0])
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('n6000_poap_script'):
			prodname = product ('n6000')
			imagecode = imagelookup (splitbydot[0])
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name == "VA_B_38V_d24m.bin" or 
		name == "vdsl.bin.32bdslfw" or 
		name == "vdsl.bin-A2pv6C035d_d23j" or 
		name == "vdsl.bin-A2pv6C035j" or 
		name == "VA_A_35l_B_35l_23j.bin" or 
		name == "vdsl.bin-A2pv6C035l" or 
		name == "VA_A_38k1_B_38h_24g1.bin" or 
		name == "VA_A_39m_B_38h3_24h.bin" or 
		name == "VA_A_39h_B_38h3_24h_j.bin" or 
		name == "VA_A_39d_B_38h3_24h_1.bin" or 
		name == "VA_A_38q_B_38r1_24j.bin" or 
		name == "VA_A_39m_B_38h3_24h_o.bin" or 
		name == "VA_A_39m_B_38u_24h.bin" or 
		name == "VA_A_39t_B_35j_24m" or 
		name == "VA_B_38V_d24m.bin" or 
		name == "VA_A_39m_B_38u_24o_rc1_SDK_4.14L.04A-J.bin" or 
		name == "VA_A_39t_B_38r1_24o_rc1_SDK_4.14L.04A.bin"
		 ):
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ("EHWICVADSLB")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name == 'V3_07.axf'
		 or name == 'V3_09.axf'
		 or name == 'V3_12_1.axf'
		 or name == 'V3_12_2.axf'
		 or name == 'V3_12_3.axf'
		 or name == 'Release-Notes-V3.12.1'
		 or name == 'Release-Notes-V3.12.2'
		 or name == 'portware.2730.ios'
		 or name == 'Exp_V3_11.axf'
		 or name == '2730_rel_note'
		 or name == 'Exp_v10_10.spe'):
			prodname = product ('ISRG2GENERIC')
			imagecode = imagelookup ('ISRG2PVDMODEM')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name == 'VAEW_A_39x3_B39x3_24o.SSA.bin'
		 or name == 'VAEW_A_39t_B_39d_24m.SSA'
		 or name == 'VAEW_A_39d_B_39d_24g1.SSA.bin'
		 or name == 'VAEW_A_39f1_B_39d_24g1.SSA.bin'):
			prodname = product ('c860vaew')
			imagecode = imagelookup ('DSLFIRMWARE')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name == 'c1100_phy_fw_A39x3_B39x3.pkg'
		 or name == 'c1100_gfast_phy_fw_A43r_B43r.pkg'
		 or name == 'c1100_gfast_phy_fw_A43j2.pkg'
		):
			prodname = product ('c1100router')
			imagecode = imagelookup ('DSLFIRMWARE')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name == 'VAE2_A_39x3_B39x3_24o.SSA.bin'
		 or name == 'VAE2_A_39t_B39d_24m.SSA.bin'):
			prodname = product ('c860vae2')
			imagecode = imagelookup ('DSLFIRMWARE')

		elif (
		name.startswith('mica-modem-pw') or 
		name.startswith('mica-pw')
		):
			prodname = product ('mica-modem')
			imagecode = imagelookup ("mica-modem")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (
		name.startswith('np.0.8.11.1.spe') or 
		name.startswith('np.0.8.11.2.spe') or 
		name.startswith('np.6.106.spe') or 
		name.startswith('np.6.93.spe') or 
		name.startswith('np.7.16.spe') or 
		name.startswith('np.7.9.spe') or 
		name.startswith('np.8.8.1.spe') or 
		name.startswith('np.spe')
		):
			prodname = product ('mica-modem')
			imagecode = imagelookup ("np")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (name.startswith('adsl_alc')
		):
			prodname = product ('ISRG1GENERIC')
			imagecode = imagelookup ("DSLFIRMWARE")
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif (
		name.startswith('Cisco_Firepower_SRU') or
		name.startswith('Cisco_VDB_Fingerprint_Database') or
		name.startswith('Cisco_Firepower_GEODB') or 
		name.startswith('Sourcefire_Rule_Update') or
		name.startswith('Sourcefire_VDB') or
		name.startswith('Sourcefire_Geodb') or 
		name.startswith('Cisco_FTD') or 
		name.startswith('Cisco_Firepower_Threat') or 
		name.startswith('Cisco_Network_Sensor') or 
		name.startswith('firepower') or 
		name.startswith('fxos') or 
		name.startswith('ftd')
		):
			fileprocessorsecurity(name)


		elif name == "ssd_c400_upgrade_6.1.2.I2.2a.tar":
			fileprocessornxos(name)

		elif name.startswith('n9000-epld'):
			fileprocessornxos(name)
		
		elif name.startswith('isr4200_cpld_update'):
			prodname = product ('isr4200')
			imagecode = imagelookup ('cpld_update')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('isr4300_cpld_update'):
			prodname = product ('isr4300')
			imagecode = imagelookup ('cpld_update')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('isr4400_cpld_update'):
			prodname = product ('isr4400')
			imagecode = imagelookup ('cpld_update')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('isr4400v2_cpld_update'):
			prodname = product ('isr4400v2')
			imagecode = imagelookup ('cpld_update')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('vcw-vfc-mz'):
			prodname = product ('c5350')
			imagecode = imagelookup (splitbydot[0])
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif name.startswith('c3600-2600-analog-fw'):
			prodname = product ('branchmodules')
			imagecode = imagelookup ('analogmodem')
			filepath = prodname + '/' + imagecode
			filemove (filepath, name)

		elif splitbydot[0] == "oac":
			filepath = "Switches/Nexus/Nexus-Open-Agent-Container"
			filemove (filepath, name)

		elif name.startswith('c2900XL'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydash[1])
			cat29003500 (name, prodname, imagecode)

		elif name.startswith('c2900xl'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydash[1])
			cat29003500 (name, prodname, imagecode)

		elif name.startswith('c3500XL'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydash[1])
			cat29003500 (name, prodname, imagecode)

		elif name.startswith('c3500xl'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydash[1])
			cat29003500 (name, prodname, imagecode)

		elif name.startswith('ess3x00'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydashsub[1])
			iosxeclassification (name, prodname, imagecode)

		elif name.startswith('cat3k_caa') and splitbydot[1] =='16':
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydashsub[1])
			iosxeclassification (name, prodname, imagecode)

		elif name.startswith('s5800'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydashsub[1])
			iosxeclassification (name, prodname, imagecode)

		elif name.startswith('vg400') or name.startswith('vg450'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydashsub[1])
			iosxeclassification (name, prodname, imagecode)

		elif splitbydot[0] == 'C9800-40-universalk9_wlc' or splitbydot[0] == 'C9800-80-universalk9_wlc' or splitbydot[0] == 'C9800-80-universalk9_wlc' or splitbydot[0] == 'C9800-CL-universalk9':
			prodname = product (splitbydash[0])
			if prodname == 'UNKNOWN':
				messageunknowndev()
			else:
				if name.startswith('C9800-40-'):
					prodname = prodname + '-40'
					imagecode = imagelookup (splitbydashsub[2])
				elif name.startswith('C9800-80-'):
					prodname = prodname + '-80'
					imagecode = imagelookup (splitbydashsub[2])
				elif name.startswith('C9800-L-'):
					prodname = prodname + '-L'
					imagecode = imagelookup (splitbydashsub[2])
				elif name.startswith('C9800-CL-'):
					prodname = prodname + '-CL'
					imagecode = imagelookup (splitbydashsub[2])
				if imagecode == 'UNKNOWN':
					messageunknownfeat()
				else:
					iosxeclassification (name, prodname, imagecode)

		elif (splitbydash[0] == 'asr1000' or 
		 splitbydash[0] == 'asr1001' or 
		 splitbydash[0] == 'asr1001x' or 
		 splitbydash[0] == 'asr1002' or 
		 splitbydash[0] == 'asr1002x' or 
		 splitbydash[0] == 'asr1000rp1' or 
		 splitbydash[0] == 'asr1000rp2' or 
		 splitbydash[0] == 'asr1000rpx86' or 
		 splitbydash[0] == 'asr900rsp1' or 
		 splitbydash[0] == 'asr900rsp2' or 
#		 splitbydash[0] == 'asr901' or 
		 splitbydash[0] == 'asr901sec' or 
		 splitbydash[0] == 'asr901rsp1' or 
		 splitbydash[0] == 'asr901rsp2' or 
		 splitbydash[0] == 'asr903rsp1' or 
		 splitbydash[0] == 'asr903rsp2' or 
		 splitbydash[0] == 'asr903rsp2' or 
		 splitbydash[0] == 'asr920' or 
		 splitbydash[0] == 'csr1000v' or 
		 splitbydash[0] == 'csr1000v_milplr' or 
		 splitbydash[0] == 'ie3x00' or 
		 splitbydash[0] == 'isr4400' or 
		 splitbydash[0] == 'isr4300' or 
		 splitbydash[0] == 'isr4200' or 
		 splitbydash[0] == 'ir1101' or 
		 splitbydash[0] == 'isr4400v2'):
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydashsub[1])
			iosxeclassification (name, prodname, imagecode)

		elif (splitbydot[0] == 'c1100-universalk9_ias' or 
		 splitbydot[0] == 'c1100-universalk9_ias_npe' or 
		 splitbydot[0] == 'c1100-ucmk9' or 
		 splitbydot[0] == 'c1100-universalk9' or 
		 splitbydot[0] == 'c1100-universalk9_npe'):
			prodname = product ('c1100router')
			mydash = splitbydot[0].split('-')
			imagecode = imagelookup (mydash[1])
			iosxeclassification (name, prodname, imagecode)

		elif splitbydash[0] == 'c1100':
			prodname = "Wireless/Access-Point/Aironet-1100"
			imagecode = imagelookup (splitbydash[1])
			standardios (name, prodname, imagecode)

		elif splitbydot[0] == 'c6svc-fwm-k9':
			fileprocessorsecurity(name)

		elif name.startswith('asdm'):
			fileprocessorsecurity(name)

		elif name.startswith('pix') or name.startswith('PIX'):
			fileprocessorsecurity(name)




















		elif chars5 == 'cat9k':
			cat9k(name)







		elif splitbydash[0] == 'AIR' or classify[0] == 'SWISMK9' or classify[0] == 'SWLC3750K9' or chars3 == 'MFG':
			wireless(name)

		elif chars9 == 'Cisco_ACI':
			aci(name)

		elif chars5 == 'm9100':
			m9100class(name)

		elif chars5 == 'm9500' or chars5 == 'm9000' or chars5 == 'm9700':
			m9500class(name)
	#	elif chars8 == 'cat4500e':
	##		cat4500es7class(name)

		elif chars7 == 'vpn3000' or chars7 == 'vpn3002' or chars7 == 'vpn3005':
			vpn3000(name)


		elif splitbydot[0] == 'c6svc-nam':
			cat6knam(name)

		elif splitbydash[0] == 'anyconnect':
			anyconnect(name)

		elif chars3 == 'csd':
			csd(name)

		elif name.startswith('sg') and name.endswith('zip') or name.endswith('adi') or name.endswith('adi-gz'):
			css(name)

		elif splitbydash[0] == 'ucs' and splitbydash[2] == 'huu':
			ucschuu (name)

		elif splitbydash[0] == 'ucs' and splitbydash[2].startswith('drivers'):
			ucscdrivers (name)

		elif name == 'ucs-b2xx-utils-1.3.1e-linux.iso':
			filepath = 'UCS/UTILS/1.3/1.3(1e)/LINUX/B-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-b2xx-utils-1.3.1e-vmware.iso':
			filepath = 'UCS/UTILS/1.3/1.3(1e)/VMWARE/B-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-b2xx-utils-1.3.1e-windows.iso':
			filepath = 'UCS/UTILS/1.3/1.3(1e)/WINDOWS/B-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-c2xx-utils-1.1.1d-efi.iso':
			filepath = 'UCS/UTILS/1.1/1.1(1d)/EFI/C-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-c2xx-utils-1.2.1-efi.iso':
			filepath = 'UCS/UTILS/1.2/1.2(1)/EFI/C-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-c2xx-utils-1.2.1-vmware.iso':
			filepath = 'UCS/UTILS/1.2/1.2(1)/VMWARE/C-SERIES'
			filemove (filepath, name)

		elif name == 'ucs-c460-m1-drivers-1.1.2b.iso':
			filepath = 'UCS/DRIVERS/1.1/1.1(2b)/C-SERIES'
			filemove (filepath, name)

		elif splitbydash[0] == 'ucs' and splitbydash[1] == '6100':
			if splitbydot[0] == 'ucs-6100-k9-kickstart':
				imagecode = "KICKSTART"
			elif splitbydot[0] == 'ucs-6100-k9-system':
				imagecode = "SYSTEM"
			prodname = 'UCS'
			ucs6100 (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs_6100_k9_kickstart':
			prodname = 'UCS'
			imagecode = 'KICKSTART'
			ucs6100 (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs_6100_k9_system':
			prodname = 'UCS'
			imagecode = 'SYSTEM'
			ucs6100 (name, prodname, imagecode)

		elif splitbydash[0] == 'ucs' and splitbydash[1] == 'manager' or splitbydot[0] == 'ucs_manager_k9':
			imagecode = 'MANAGER'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydashsub[0] == 'ucs' and splitbydashsub[1] == 'catalog':
			imagecode = 'CATALOG'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs-k9-bundle-infra' or splitbydot[0] == 'ucs_k9_bundle' or splitbydot[0] == 'ucs-6300-k9-bundle-infra' or splitbydot[0] == 'ucs-mini-k9-bundle-infra' or splitbydot[0] == 'ucs-6400-k9-bundle-infra':
			imagecode = 'BUNDLE'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs-k9-bundle-b-series':
			imagecode = 'BUNDLE'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs-k9-bundle-m-series':
			imagecode = 'BUNDLE'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs-k9-bundle-c-series':
			imagecode = 'BUNDLE'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'ucs_k9_bundle':
			imagecode = 'BUNDLE'
			prodname = 'UCS'
			ucsmanager (name, prodname, imagecode)

		elif name == 'UCS_docs_20110510.iso':
			filepath = 'UCS/DOCS/2011-05-10'
			filemove (filepath, name)

		elif name == 'ucs-drivers.1.0.2.iso':
			filepath = 'UCS/DRIVERS/1.0/1.0(2)'
			filemove (filepath, name)

		elif splitbydashsub[0] == 'ucs':
			if splitbydash[2] == 'utils':
				prodname = 'UCS'
				ucsutils2 (name, prodname)
			elif splitbydashsub[1] == 'bxxx' or splitbydashsub[1] == 'b2xx'  and splitbydashsub[2] == 'drivers':
				imagecode = 'DRIVERS'
				prodname = 'UCS'
				ucsmanager (name, prodname, imagecode)
			elif splitbydashsub[1] == 'cxxx' and splitbydashsub[2] == 'drivers':
				imagecode = 'DRIVERS'
				prodname = 'UCS'
				ucsmanager (name, prodname, imagecode)
			elif splitbydashsub[1] == 'c460' and splitbydashsub[3] == 'drivers':
				imagecode = 'DRIVERS-C-SERIES'
				prodname = 'UCS'
				ucsmanager (name, prodname, imagecode)
			elif splitbydashsub[2] == 'drivers':
				imagecode = 'DRIVERS'
				prodname = 'UCS'
				ucsmanager (name, prodname, imagecode)

		elif splitbydot[0] == 'c675' or splitbydot[1] == 'c675':
			filepath = 'Other'
			filemove (filepath, name)

		elif splitbydot[0] == 'c678cap' or splitbydot[1] == 'c678cap':
			filepath = 'Other'
			filemove (filepath, name)

		elif splitbydot[0] == 'c678dmt' or splitbydot[1] == 'c678dmt':
			filepath = 'Other'
			filemove (filepath, name)

		elif splitbydot[0] == 'spa-fpd':
			thistemp = splitbydot[0]
			splitbydashsub = thistemp.split('-')
			imagecode = imagelookup (splitbydashsub[1])
			prodname = product (splitbydashsub[0])
			standardios (name, prodname, imagecode)

		elif splitbydot[0] == 'dsc-c5800-mz':
			imagecode = imagelookup (splitbydash[0])
			prodname = product (splitbydash[1])
			standardios (name, prodname, imagecode)

		elif splitbydash[0] == 'cat6000' or splitbydash[0] == 'cat5000' or splitbydot[0] == 'cat4000' or splitbydot[0] == 'cat4000-cv' or splitbydot[0] == 'cat4000-k8' or splitbydot[0] == 'cat4000-k9':
			catos (name)

		elif splitbydash[0] == 'fcs' and splitbydash[1] == 'csm':
			csm4(name)

		elif splitbydash[0] == 'fcs' and splitbydash[1] == 'mcp':
			csmmcp(name)

		elif splitbydash[0] == 'fcs' and splitbydash[1] == 'rme' and splitbydash[2] == '430':
			filepath = 'Cisco Security Manager/4.0.0/RESOURCE MANAGER ESSENTIALS'
			filemove (filepath, name)

		elif name == 'c2xx-m1-utils-1.0.2.iso':
			filepath = 'UCS/C-SERIES/UTILS/1.0/1.0(2)'
			filemove (filepath, name)
#		elif splitbydot[1] == 'tar' and splitbydot[2] == 'gpg':
#			acs5patches(name)

		elif name == 'ACS_5.0.0.21_ADE_OS_1.2_upgrade.tar.gpg':
			filepath = 'ACS/5.0.0.21/OS Upgrade'
			filemove (filepath, name)

		elif name == 'ACS-5.0.0.21.iso':
			filepath = 'ACS/5.0.0.21/Install'
			filemove (filepath, name)

		elif name == 'ACS_v5.2.0.26.iso':
			filepath = 'ACS/5.2.0.26/Install'
			filemove (filepath, name)

		elif name == 'ACS_5.2.0.26.tar.gz':
			filepath = 'ACS/5.2.0.26/Upgrade'
			filemove (filepath, name)

		elif name == 'ACS_v5.1.0.44.iso':
			filepath = 'ACS/5.1.0.44/Install'
			filemove (filepath, name)

		elif name == 'ACS_5.1.0.44.tar.gz':
			filepath = 'ACS/5.1.0.44/Upgrade'
			filemove (filepath, name)

		elif splitbydash[0] == 'IPS' and splitbydash[1] == 'CS' and splitbydash[2] == 'MGR':
			csmips(name)

		elif splitbydash[0] == 'IPS' and splitbydash[1] == 'K9' and splitbydash[2] == 'r':
			ipsrecovery(name)

		elif splitbydash[0] == 'IPS' and splitbydash[1] == 'K9':
			ipssystem(name)

		elif splitbydash[0] == 'IPS' and splitbydash[1] == 'sig':
			ipssig(name)

		elif splitbydash[0] == 'csmars':
			mars(name)

		elif splitbydash[0] == 'Acs' or splitbydash[0] == 'ACS':
			acs(name)

		elif splitbydot[1] == 'SPA':
			if splitbydash[0] == 'cat4500e':
				thissplit = splitbydot[0].split('-')
				imagecode = imagelookup (thissplit[1])
				prodname = product (splitbydash[0])
				cat4500spa (name, prodname, imagecode)
			elif splitbydash[0] == 'cat4500es8':
				thissplit = splitbydot[0].split('-')
				imagecode = imagelookup (thissplit[1])
				prodname = product (splitbydash[0])
				cat4500spa (name, prodname, imagecode)
			else:
				imagecode = imagelookup (splitbydash[1])
				prodname = product (splitbydash[0])
				spa (name, prodname, imagecode)


		elif splitbydash[0] == 'm9200':
			prodname = product (splitbydash[0])
			m9200 (name, prodname)

		elif splitbydash[0] == 'm9250':
			prodname = product (splitbydash[0])
			m9250 (name, prodname)

		elif splitbydot[0] == 'c10k-fpd-pkg':
			prodname = 'Routers/SP/10000'
			imagecode = imagelookup (splitbydash[1])
			standardios (name, prodname, imagecode)

		elif splitbydash[0] == 'XR12000':
			prodname = product (splitbydash[0])
			imagecode = imagelookup (splitbydash[1])
			iosxrv (name, prodname, imagecode)

		elif splitbydash[0] == 'all':
			prodname = 'OnePK'
			if name == 'all-in-one-VM-1.2.1-194.ova':
				filepath = prodname + '/' + '1.2/' + '1.2(1)194'
				filemove (filepath, name)
			elif name == 'all-in-one-VM-1.3.0.181.ova':
				filepath = prodname + '/' + '1.3/' + '1.3(0)181'
				filemove (filepath, name)

		elif splitbydash[0] == 'pp' and splitbydash[1] == 'adv':
			nbar2 (name)

		elif splitbydot[0] == 'ucs_ctrlr':
			imagecode = imagelookup (splitbydash[1])
			prodname = product (splitbydash[0])
			standardios (name, prodname, imagecode)

		elif splitbydash[0] == 'UTD' and splitbydash[1] == 'STD' and splitbydash[2] == 'SIGNATURE':
			ios_xe_signature (name)

		elif splitbydash[1] == 'vWAAS' or splitbydash[2] == 'vWAAS' or splitbydash[0] == 'WAAS' or splitbydash[1] == 'WAAS' or splitbydash[0] == 'waas':
			waas (name)

		elif splitbydash[0] == 'aci' or splitbydash[0] == 'apic' or splitbydash[0] == 'vcenter' and splitbydash[1] == 'plugin':
			aci (name)

		elif splitbydash[0] == 'full' or splitbydash[0] == 'fullk9':
			iosxrv9k (name)

		elif splitbydash[0] == 'ASR9000' or splitbydash[0] == 'ASR9K' or splitbydash[0] == 'asr9k':
			asr9k (name)

		else:
			imagecode = imagelookup (splitbydash[1])
			prodname = product (splitbydash[0])
			standardios (name, prodname, imagecode)

if __name__ == "__main__":
	toplevel(sys.argv[1])
