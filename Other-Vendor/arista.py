import os, shutil, getopt, argparse

def product (prodcode):
	if prodcode == "vEOS-lab":
		return "VEOS"
	elif prodcode == "vEOS64-lab":
		return "VEOS64"
	elif prodcode == "cEOS-lab":
		return "CEOS"
	elif prodcode == "cEOS64-lab":
		return "CEOS64"
	elif prodcode == "EOS":
		return "EOS"
	elif prodcode == "Aboot-veos":
		return "ABoot"
	else:
		return "UNKNOWN", "UNKNOWN"

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
		workname = filename.replace(".sha512sum","")
		workname = workname.replace(".md5sum","")
		workname = workname.replace(".tar.xz","")
		workname = workname.replace(".tar.tar","")
		workname = workname.replace(".swi","")
		workname = workname.replace("-combined.vmdk","")
		workname = workname.replace(".vmdk","")
		workname = workname.replace("-virtualbox.box","")
		workname = workname.replace("vEOS64-lab-","")
		workname = workname.replace("vEOS-lab-combined-","")
		workname = workname.replace("vEOS-lab-","")
		workname = workname.replace("cEOS-lab-","")
		workname = workname.replace("cEOS64-lab-","")
		workname = workname.replace("cEOS64-lab-","")
		workname = workname.replace("Aboot-veos-serial-","")
		workname = workname.replace("Aboot-veos-","")
		workname = workname.replace(".iso","")
		version = stringtodigit (workname)
		filepath = filepath2(prod,version)
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
		
		if filename == "cEOS.tar.xz":
			prod = product("cEOS-lab")
			process_file(filename,prod)
		elif filename.startswith("vEOS-lab"):
			prod = product("vEOS-lab")
			process_file(filename,prod)
		elif filename.startswith("vEOS64-lab"):
			prod = product("vEOS64-lab")
			process_file(filename,prod)
		elif filename.startswith("cEOS64-lab"):
			prod = product("cEOS64-lab")
			process_file(filename,prod)
		elif filename.startswith("cEOS-lab"):
			prod = product("cEOS-lab")
			process_file(filename,prod)
		elif filename.startswith("EOS"):
			prod = product("EOS")
			process_file(filename,prod)
		elif filename.startswith("Aboot-veos"):
			prod = product("Aboot-veos")
			process_file(filename,prod)
		else:
			continue

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--directory', help='Directory to sort', required=True)
	
	args = parser.parse_args()
	dirpass = args.directory

	toplevel(dirpass)
