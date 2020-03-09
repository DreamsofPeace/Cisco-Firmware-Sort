def fileprocessornxos (filename):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	if splitbydot[0] == 'nxos':
		if len(splitbydot) == 5:
			fileprocessornxos9kv8later(filename)
		elif len(splitbydot) == 7:
			fileprocessornxos9kv7(filename)
		elif len(splitbydot) == 7:
			fileprocessornxos9kv7(filename)
		elif splitbydot[1].startswith('CSC'):
			fileprocessornxos9kv8smu

def nexus5000 (filename, prodname, imagecode):
	splitbydot = filename.split('.')
	if splitbydot[1] != "9":
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')' + splitbydot[4] + '(' + splitbydot[5] + ')'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	else:
		mainver = splitbydot[1] + '.' + splitbydot[2]
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
		filepath = prodname + '/' + mainver + '/' + fullver + '/' + imagecode
	filemove (filepath, filename)

def nexus7000 (filename, prodname):
	splitbydot = filename.split('.')
	splitbydash = filename.split('-')
	if splitbydash[1] == 's1':
		sup = 'SUP-1'
	elif splitbydash[1] == 's2':
		sup = 'SUP-2'
	if len(splitbydash) == 4:
		if splitbydash[2] == 'dk9':
			if splitbydash[3].startswith('npe'):
				imagecode = 'SYSTEM - NO CRYPTO'
			else:
				imagecode = 'SYSTEM'
		elif splitbydash[2] == 'kickstart':
			if splitbydash[3].startswith('npe'):
				imagecode = 'KICKSTART - NO CRYPTO'
			else:
				imagecode = 'KICKSTART'
	elif len(splitbydash) == 3:
		if splitbydash[2].startswith('dk9'):
			imagecode = 'SYSTEM'
		elif splitbydash[2].startswith('kickstart'):
			imagecode = 'KICKSTART'

	mainver = splitbydot[1] + '.' + splitbydot[2]
	if len(splitbydot) == 7:
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')' + splitbydot[4] + '(' + splitbydot[5] + ')'
	else:
		fullver = splitbydot[1] + '.' + splitbydot[2] + '(' + splitbydot[3] + ')'
	filepath = prodname + '/' + sup + '/' + mainver + '/' + fullver
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

def fileprocessornxos9kv8later (filename):
	splitbydash = filename.split('-')
	splitbydot = filename.split('.')
	prodname = product (splitbydot[0])
	imagecode = "SYSTEM"
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
	filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)

def fileprocessornxos9kv7 (filename):
	splitbydash = filename.split('-')
	splitbydot = filename.split('.')
	#if splitbydot[4] == 'I7' or splitbydot[4] == 'i7':
	prodname = product ('nxosi7')
	imagecode = "SYSTEM"
	nxosver = util2digit (splitbydot[1],splitbydot[2])
	nxosfull = util5digit (splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
	filepath = filepath4 (prodname,nxosver,nxosfull,imagecode)
	filemove (filepath, filename)




