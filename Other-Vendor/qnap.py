import os, shutil, getopt, argparse

def product (prodcode):
	if prodcode == "TR-004":
		return "TR-004"
	elif prodcode == "TR-002":
		return "TR-002"
	elif prodcode == "TS-X31X":
		return "X31X"
	elif prodcode == "TS-X35A":
		return "X35A"
	elif prodcode == "TS-X32":
		return "X32"
	elif prodcode == "TS-X42":
		return "X42"
	else:
		return "UNKNOWN"

def filepath2 (a,b):
	return a + "/" + b

def filemove (newpath, filename):
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	try:
		shutil.move(filename, newpath)
	except:
		print("There is a file with the same name at the destination!.")

def process_file(filename,prod):
	if prod == "UNKNOWN":
		messageunclassifiable ()
	else:
		workname = filename.replace(".img","")
		workname = workname.replace(".zip","")
		myworkname = workname.split("-")
		filepath = filepath2(prod,myworkname[2])
		filemove (filepath, filename)



def messageunclassifiable ():
		print ("E001: This image is unknown, please update the script with the information about the image.", end="\n")

def stringtodigit (version):
	splitbydot = version.split(".")
	return ".".join(splitbydot)
#	z = a + "." + b
#	return z

def toplevel(directory):
	src = directory
	names = os.listdir(src)
	os.chdir(src)
	for filename in names:
		if os.path.isdir(filename):
			continue
		print (filename,end="\n")
		
		if filename == "TS-X31X_434.zip":
			prod = product("TS-X31X")
			filepath = filepath2(prod,"4.3.4")
			filemove (filepath, filename)
		elif (

		filename == "QTS_Patch_434.0455.0_arm_al.qfix" or 
		filename == "QTS_Patch_434.0455.0_arm_al.qfix.zip"
		):
			prod = product("TS-X31X")
			filepath = filepath2(prod,"4.3.4.0455")
			filemove (filepath, filename)
		elif filename.startswith("TR-004"):
			prod = product("TR-004")
			process_file(filename,prod)
		elif filename.startswith("TR-002"):
			prod = product("TR-002")
			process_file(filename,prod)
		elif filename.startswith("TS-X31X"):
			prod = product("TS-X31X")
			process_file(filename,prod)
		elif filename.startswith("TS-X35A"):
			prod = product("TS-X35A")
			process_file(filename,prod)
		elif filename.startswith("TS-X32"):
			prod = product("TS-X32")
			process_file(filename,prod)
		elif filename.startswith("TS-X42"):
			prod = product("TS-X42")
			process_file(filename,prod)
		else:
			continue
#		process_file(filename,prod)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--directory', help='Directory to sort', required=True)
	
	args = parser.parse_args()
	dirpass = args.directory

	toplevel(dirpass)
