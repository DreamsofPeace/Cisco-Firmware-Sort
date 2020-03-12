from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def fileprocessornxos (filename):
	splitbydash = filename.split('-')
	splitbydot = filename.split('.')
	if filename == "ssd_c400_upgrade_6.1.2.I2.2a.tar":
		prodname = product('nxos')
		imagecode = imagelookup('firmware')
		nexussinglefile (filename,prodname,imagecode)
	elif filename == "n9000-epld-secure-boot-update.img":
		prodname = product('nxos')
		imagecode = imagelookup('epld')
		nexussinglefile (filename,prodname,imagecode)
	elif filename == "nxos-n3kbios.bin" or filename == "n3k_bios_release_rn.pdf":
		prodname = product('n3000')
		imagecode = imagelookup('bios')
		nexussinglefile (filename,prodname,imagecode)
	elif splitbydot[0] == 'n9000-epld':
		prodname = product('nxos')
		imagecode = imagelookup('epld')
		if splitbydot[1] == "6" or splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode)
		else:
			fileprocnxosthreedigit(filename,prodname,imagecode)
	elif splitbydot[0] == 'nxosv-final':
		prodname = product('nxosv')
		imagecode = imagelookup('system')
		if splitbydot[1] == "6" or splitbydot[1] == "7":
			fileprocnxosfivedigit (filename,prodname,imagecode)
		else:
			fileprocnxosthreedigit(filename,prodname,imagecode)
	elif splitbydot[0] == 'nxos':
		prodname = product('nxos')
		if len(splitbydot) == 5:
			imagecode = imagelookup('system')
			fileprocnxosthreedigit(filename,prodname,imagecode)
		elif len(splitbydot) == 7:
			imagecode = imagelookup('system')
			fileprocnxosfivedigit(filename,prodname,imagecode)
		elif len(splitbydot) == 7:
			imagecode = imagelookup('system')
			fileprocnxosfivedigit(filename,prodname,imagecode)
		elif splitbydot[1].startswith('CSC'):
			imagecode = imagelookup('smu')
			fileprocessornxos9ksmu(filename,prodname,imagecode)
	elif splitbydash[0] == "n5000":
		prodname = product(splitbydash[0])
		if splitbydot[0] == "n5000-uk9-kickstart":
			imagecode = imagelookup('kickstart')
			fileprocnxosfivedigit(filename,prodname,imagecode)
		elif splitbydot[0] == "n5000-uk9":
			imagecode = imagelookup('system')
			fileprocnxosfivedigit(filename,prodname,imagecode)
	elif splitbydash[0] == "n6000":
		prodname = product(splitbydash[0])
		if splitbydot[0] == "n6000-uk9-kickstart":
			imagecode = imagelookup('kickstart')
			fileprocnxosfivedigit(filename,prodname,imagecode)
		elif splitbydot[0] == "n6000-uk9":
			imagecode = imagelookup('system')
			fileprocnxosfivedigit(filename,prodname,imagecode)
	elif splitbydash[0] == "n3000":
		prodname = product(splitbydash[0])
		if splitbydot[0] == "n3000-uk9-kickstart":
			imagecode = imagelookup('kickstart')
			fileprocnxosfivedigit(filename,prodname,imagecode)
		elif splitbydot[0] == "n3000-uk9":
			imagecode = imagelookup('system')
			fileprocnxosfivedigit(filename,prodname,imagecode)

def nexussinglefile (filename,prodname,imagecode):
	filepath = filepath2 (prodname,imagecode)
	filemove (filepath, filename)

def nexus1000v (filename):
	prodname = 'Nexus 1000V'
	thisdot = filename.split('.')
	splitbydot = filename.split('.')
	if filename == 'Nexus1000V5.2.1.SM1.5.2.zip':
		filepath = 'Nexus 1000V/HyperV/5.2/5.2(1)SM1(5.2)'
		filemove (filepath, filename)
		return
	elif filename == 'n1000vh-dk9.5.2.1.SM1.5.1.zip':
		filepath = 'Nexus 1000V/HyperV/5.2/5.2(1)SM1(5.1)'
		filemove (filepath, filename)
		return
	elif filename == 'Nexus1000v-4.0.4.SV1.1.zip':
		filepath = 'Nexus 1000V/VMWare/4.0/4.0(4)SV1(1)'
		filemove (filepath, filename)
		return
	elif filename == 'Nexus1000v-4.0.4.SV1.3.zip':
		filepath = 'Nexus 1000V/VMWare/4.0/4.0(4)SV1(3)'
		filemove (filepath, filename)
		return
	mytype = thisdot[4][0:2]
	if mytype == 'SV':
		platform = 'VMWare'
	elif mytype == 'SK':
		platform = 'KVM'
	elif mytype == 'SM':
		platform = 'HyperV'
	mainver = splitbydot[1] + '.' + splitbydot[2]
	if splitbydot[6] == 'zip':
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')' + splitbydot[4] + '(' + splitbydot[5] + ')'
	else:
		splitbydot[6] = splitbydot[6].strip ('-pkg')
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')' + splitbydot[4] + '(' + splitbydot[5] + '.' + splitbydot[6] + ')'
	filepath = prodname + '/' + platform + '/' + mainver + '/' + fullver
	filemove (filepath, filename)

def fileprocessornxosplatform7700v8 (filename):
	splitbydash = filename.split('-')
	splitbydot = filename.split('.')
	if filename.startswith == "n7700-s2-kickstart-npe":
		imagecode = "KICKSTART-NPE"
	elif filename.startswith == "n7700-s2-kickstart":
		imagecode = "KICKSTART"
	elif filename.startswith == "n7700-s2-dk9-npe":
		imagecode = "SYSTEM-NPE"
	elif filename.startswith == "n7700-s2-dk9":
		imagecode = "SYSTEM"
	if splitbydash[0] == "n7700":
		prodname = product (splitbydash[0])
		if splitbydash[1] == "s2":
			imagecode = "SUP-2"
		elif splitbydash[1] == "s3":
			imagecode = "SUP-3"
		iosmain = util2digit (splitbydot[1],splitbydot[2])
		iosfull = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
		filepath = prodname + '/' + iosmain + '/' + iosfull + '/' + imagecode

def fileprocnxosthreedigit (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
	if imagecode == "EPLD":
		filepath = filepath4 (prodname,imagecode,nxosver,nxosfull)
	else:
		filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)

def fileprocnxosfivedigit (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util5digit (splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
	if imagecode == "EPLD":
		filepath = filepath4 (prodname,imagecode,nxosver,nxosfull)
	else:
		filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)

def fileprocessornxos9ksmu (filename,prodname,imagecode):
	splitbydot = filename.split('.')
	csc = splitbydot[1].replace("-n9k_ALL-1","")
	csc = csc.replace("_EOR-n9k_EOR-1","")
	csc = csc.replace("_TOR-n9k_TOR-1","")
	csc = csc.replace("_eth-n9k_TOR-1","")
	csc = csc.replace("_eth-n9k_EOR-1","")
	csc = csc.replace("-n9k_EOR-1","")
	csc = csc.replace("-n9k_TOR-1","")
	csc = csc.replace("_modular_lc-1","")
	csc = csc.replace("_modular_sup-1","")
	csc = csc.replace("01-1","")
	csc = csc.replace("-1","")
	if splitbydot[3] == '0-9':
		digitone = '9'
	elif splitbydot[3] == '0-8':
		digitone = '8'
	elif splitbydot[3] == '0-7':
		digitone = '7'
	if digitone == '9':
		nxosver = util2digit (digitone,splitbydot[4])
		nxosfull = util3digit (digitone,splitbydot[4],splitbydot[5])
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,csc)
		filemove (filepath, filename)
	elif digitone == '7':
		nxosver = util2digit (digitone,splitbydot[4])
		nxosfull = util5digit (digitone,splitbydot[4],splitbydot[5],splitbydot[6],splitbydot[7])
		filepath = filepath5 (prodname,imagecode,nxosver,nxosfull,csc)
		filemove (filepath, filename)
