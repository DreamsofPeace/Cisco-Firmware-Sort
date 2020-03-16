from iosutils import product,imagelookup,iostrain
from iosutils import filemove,filepath2,filepath3,filepath4,filepath5
from iosutils import util2digit,util3digit,util4digit,util5digit,stringtolist
from iosutils import messageunknowndev,messageunknownfeat

def fileprocessorsecurity (filename):
	if filename.startswith('c6svc-fwm-k9'):
		firewallfwsm (filename)

def firewallfwsm (filename):
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