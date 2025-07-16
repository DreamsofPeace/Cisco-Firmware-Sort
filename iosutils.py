import os, shutil

def filemove (newpath, filename):
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	try:
		shutil.move(filename, newpath)
	except:
		print("There is a file with the same name at the destination!.")

def iostrain (train, version):
	if train.startswith("AA"):
		version = version + "AA"
	elif train.startswith("AX"):
		version = version + "AX"
	elif train.startswith("AY"):
		version = version + "AY"
	elif train.startswith("AZ"):
		version = version + "AZ"
	elif train.startswith("BC"):
		version = version + "BC"
	elif train.startswith("BT"):
		version = version + "BT"
	elif train.startswith("BW"):
		version = version + "BW"
	elif train.startswith("BX"):
		version = version + "BX"
	elif train.startswith("BY"):
		version = version + "BY"
	elif train.startswith("B"):
		version = version + "B"
	elif train.startswith("CX"):
		version = version + "CX"
	elif train.startswith("CY"):
		version = version + "CY"
	elif train.startswith("CZ"):
		version = version + "CZ"
	elif train.startswith("DA"):
		version = version + "DA"
	elif train.startswith("DB"):
		version = version + "DB"
	elif train.startswith("DC"):
		version = version + "DC"
	elif train.startswith("DD"):
		version = version + "DD"
	elif train.startswith("DX"):
		version = version + "DX"
	elif train.startswith("EA"):
		version = version + "EA"
	elif train.startswith("EB"):
		version = version + "EB"
	elif train.startswith("EC"):
		version = version + "EC"
	elif train.startswith("ED"):
		version = version + "ED"
	elif train.startswith("EH"):
		version = version + "EH"
	elif train.startswith("EJ"):
		version = version + "EJ"
	elif train.startswith("EK"):
		version = version + "EK"
	elif train.startswith("EO"):
		version = version + "EO"
	elif train.startswith("EU"):
		version = version + "EU"
	elif train.startswith("EV"):
		version = version + "EV"
	elif train.startswith("EWA"):
		version = version + "EWA"
	elif train.startswith("EW"):
		version = version + "EW"
	elif train.startswith("EX"):
		version = version + "EX"
	elif train.startswith("EY"):
		version = version + "EY"
	elif train.startswith("EZ"):
		version = version + "EZ"
	elif train.startswith("E"):
		version = version + "E"
	elif train.startswith("FX"):
		version = version + "FX"
	elif train.startswith("FY"):
		version = version + "FY"
	elif train.startswith("FZ"):
		version = version + "FZ"
	elif train.startswith("GA"):
		version = version + "GA"
	elif train.startswith("GB"):
		version = version + "GB"
	elif train.startswith("GCA"):
		version = version + "GCA"
	elif train.startswith("GC"):
		version = version + "GC"
	elif train.startswith("IRA"):
		version = version + "IRA"
	elif train.startswith("IRB"):
		version = version + "IRB"
	elif train.startswith("IRC"):
		version = version + "IRC"
	elif train.startswith("IRD"):
		version = version + "IRD"
	elif train.startswith("IRE"):
		version = version + "IRE"
	elif train.startswith("IRF"):
		version = version + "IRF"
	elif train.startswith("IRG"):
		version = version + "IRG"
	elif train.startswith("IRH"):
		version = version + "IRH"
	elif train.startswith("IRI"):
		version = version + "IRI"
	elif train.startswith("IXA"):
		version = version + "IXA"
	elif train.startswith("IXB"):
		version = version + "IXB"
	elif train.startswith("IXC"):
		version = version + "IXC"
	elif train.startswith("IXD"):
		version = version + "IXD"
	elif train.startswith("IXE"):
		version = version + "IXE"
	elif train.startswith("IXF"):
		version = version + "IXF"
	elif train.startswith("IXG"):
		version = version + "IXG"
	elif train.startswith("IXH"):
		version = version + "IXH"
	elif train.startswith("JAL"):
		version = version + "JAL"
	elif train.startswith("JAM"):
		version = version + "JAM"
	elif train.startswith("JAN"):
		version = version + "JAN"
	elif train.startswith("JAO"):
		version = version + "JAO"
	elif train.startswith("JAX"):
		version = version + "JAX"
	elif train.startswith("JAY"):
		version = version + "JAY"
	elif train.startswith("JAZ"):
		version = version + "JAZ"
	elif train.startswith("JAB"):
		version = version + "JAB"
	elif train.startswith("JA"):
		version = version + "JA"
	elif train.startswith("JBA"):
		version = version + "JBA"
	elif train.startswith("JBB"):
		version = version + "JBB"
	elif train.startswith("JBC"):
		version = version + "JBC"
	elif train.startswith("JBD"):
		version = version + "JBD"
	elif train.startswith("JBE"):
		version = version + "JBE"
	elif train.startswith("JB"):
		version = version + "JB"
	elif train.startswith("JCA"):
		version = version + "JCA"
	elif train.startswith("JCB"):
		version = version + "JCB"
	elif train.startswith("JCC"):
		version = version + "JCC"
	elif train.startswith("JCD"):
		version = version + "JCD"
	elif train.startswith("JCE"):
		version = version + "JCE"
	elif train.startswith("JC"):
		version = version + "JC"
	elif train.startswith("JDA"):
		version = version + "JDA"
	elif train.startswith("JDB"):
		version = version + "JDB"
	elif train.startswith("JDC"):
		version = version + "JDC"
	elif train.startswith("JDD"):
		version = version + "JDD"
	elif train.startswith("JD"):
		version = version + "JD"
	elif train.startswith("JEA"):
		version = version + "JEA"
	elif train.startswith("JEB"):
		version = version + "JEB"
	elif train.startswith("JEC"):
		version = version + "JEC"
	elif train.startswith("JED"):
		version = version + "JED"
	elif train.startswith("JEE"):
		version = version + "JEE"
	elif train.startswith("JE"):
		version = version + "JE"
	elif train.startswith("JFA"):
		version = version + "JFA"
	elif train.startswith("JFB"):
		version = version + "JFB"
	elif train.startswith("JFC"):
		version = version + "JFC"
	elif train.startswith("JFD"):
		version = version + "JFD"
	elif train.startswith("JF"):
		version = version + "JF"
	elif train.startswith("JGA"):
		version = version + "JGA"
	elif train.startswith("JGB"):
		version = version + "JGB"
	elif train.startswith("JGC"):
		version = version + "JGC"
	elif train.startswith("JGD"):
		version = version + "JGD"
	elif train.startswith("JG"):
		version = version + "JG"
	elif train.startswith("JHA"):
		version = version + "JHA"
	elif train.startswith("JHB"):
		version = version + "JHB"
	elif train.startswith("JHC"):
		version = version + "JHC"
	elif train.startswith("JH"):
		version = version + "JH"
	elif train.startswith("JI"):
		version = version + "JI"
	elif train.startswith("JJ"):
		version = version + "JJ"
	elif train.startswith("JK"):
		version = version + "JK"
	elif train.startswith("JL"):
		version = version + "JL"
	elif train.startswith("JMA"):
		version = version + "JMA"
	elif train.startswith("JMB"):
		version = version + "JMB"
	elif train.startswith("JMC"):
		version = version + "JMC"
	elif train.startswith("JM"):
		version = version + "JM"
	elif train.startswith("JN"):
		version = version + "JN"
	elif train.startswith("JX"):
		version = version + "JX"
	elif train.startswith("JPA"):
		version = version + "JPA"
	elif train.startswith("JPB"):
		version = version + "JPB"
	elif train.startswith("JPC"):
		version = version + "JPC"
	elif train.startswith("JPD"):
		version = version + "JPD"
	elif train.startswith("JPE"):
		version = version + "JPE"
	elif train.startswith("JPF"):
		version = version + "JPF"
	elif train.startswith("JPG"):
		version = version + "JPG"
	elif train.startswith("JPH"):
		version = version + "JPH"
	elif train.startswith("JPI"):
		version = version + "JPI"
	elif train.startswith("JPJ"):
		version = version + "JPJ"
	elif train.startswith("JPK"):
		version = version + "JPK"
	elif train.startswith("JPL"):
		version = version + "JPL"
	elif train.startswith("JPM"):
		version = version + "JPM"
	elif train.startswith("JPN"):
		version = version + "JPN"
	elif train.startswith("JPO"):
		version = version + "JPO"
	elif train.startswith("JPP"):
		version = version + "JPP"
	elif train.startswith("JPQ"):
		version = version + "JPQ"
	elif train.startswith("JPR"):
		version = version + "JPR"
	elif train.startswith("JPS"):
		version = version + "JPS"
	elif train.startswith("JPT"):
		version = version + "JPT"
	elif train.startswith("JPU"):
		version = version + "JPU"
	elif train.startswith("JPV"):
		version = version + "JPV"
	elif train.startswith("JPW"):
		version = version + "JPW"
	elif train.startswith("JPX"):
		version = version + "JPX"
	elif train.startswith("JPY"):
		version = version + "JPY"
	elif train.startswith("JPZ"):
		version = version + "JPZ"
	elif train.startswith("JP"):
		version = version + "JP"
	elif train.startswith("JY"):
		version = version + "JY"
	elif train.startswith("L"):
		version = version + "L"
	elif train.startswith("MB"):
		version = version + "MB"
	elif train.startswith("MC"):
		version = version + "MC"
	elif train.startswith("MDA"):
		version = version + "MDA"
	elif train.startswith("MDB"):
		version = version + "MDB"
	elif train.startswith("MD"):
		version = version + "MD"
	elif train.startswith("MIG"):
		version = version + "MIG"
	elif train.startswith("MRA"):
		version = version + "MRA"
	elif train.startswith("MRB"):
		version = version + "MRB"
	elif train.startswith("MR"):
		version = version + "MR"
	elif train.startswith("MX"):
		version = version + "MX"
	elif train.startswith("M"):
		version = version + "M"
	elif train.startswith("NA"):
		version = version + "NA"
	elif train.startswith("N"):
		version = version + "N"
	elif train.startswith("PBAS"):
		version = version + "PBAS"
	elif train.startswith("PBA"):
		version = version + "PBA"
	elif train.startswith("PBS"):
		version = version + "PBS"
	elif train.startswith("PB"):
		version = version + "PB"
	elif train.startswith("PC"):
		version = version + "PC"
	elif train.startswith("PIX"):
		version = version + "PIX"
	elif train.startswith("PI"):
		version = version + "PI"
	elif train.startswith("P"):
		version = version + "P"
	elif train.startswith("SBA"):
		version = version + "SBA"
	elif train.startswith("SBB"):
		version = version + "SBB"
	elif train.startswith("SBC"):
		version = version + "SBC"
	elif train.startswith("SBY"):
		version = version + "SBY"
	elif train.startswith("SB"):
		version = version + "SB"
	elif train.startswith("SCA"):
		version = version + "SCA"
	elif train.startswith("SCB"):
		version = version + "SCB"
	elif train.startswith("SCC"):
		version = version + "SCC"
	elif train.startswith("SCD"):
		version = version + "SCD"
	elif train.startswith("SCE"):
		version = version + "SCE"
	elif train.startswith("SCF"):
		version = version + "SCF"
	elif train.startswith("SCG"):
		version = version + "SCG"
	elif train.startswith("SCH"):
		version = version + "SCH"
	elif train.startswith("SCI"):
		version = version + "SCI"
	elif train.startswith("SCJ"):
		version = version + "SCJ"
	elif train.startswith("SCK"):
		version = version + "SCK"
	elif train.startswith("SCL"):
		version = version + "SCL"
	elif train.startswith("SCM"):
		version = version + "SCM"
	elif train.startswith("SC"):
		version = version + "SC"
	elif train.startswith("SEA"):
		version = version + "SEA"
	elif train.startswith("SEB"):
		version = version + "SEB"
	elif train.startswith("SEC"):
		version = version + "SEC"
	elif train.startswith("SED"):
		version = version + "SED"
	elif train.startswith("SEE"):
		version = version + "SEE"
	elif train.startswith("SEF"):
		version = version + "SEF"
	elif train.startswith("SEG"):
		version = version + "SEG"
	elif train.startswith("SE"):
		version = version + "SE"
	elif train.startswith("SGA"):
		version = version + "SGA"
	elif train.startswith("SG"):
		version = version + "SG"
	elif train.startswith("SRA"):
		version = version + "SRA"
	elif train.startswith("SRB"):
		version = version + "SRB"
	elif train.startswith("SRC"):
		version = version + "SRC"
	elif train.startswith("SRD"):
		version = version + "SRD"
	elif train.startswith("SRE"):
		version = version + "SRE"
	elif train.startswith("SL"):
		version = version + "SL"
	elif train.startswith("SM"):
		version = version + "SM"
	elif train.startswith("SNG"):
		version = version + "SNG"
	elif train.startswith("SNH"):
		version = version + "SNH"
	elif train.startswith("SNI"):
		version = version + "SNI"
	elif train.startswith("SN"):
		version = version + "SN"
	elif train.startswith("SO"):
		version = version + "SO"
	elif train.startswith("SP"):
		version = version + "SP"
	elif train.startswith("SQ"):
		version = version + "SQ"
	elif train.startswith("SRA"):
		version = version + "SRA"
	elif train.startswith("SRB"):
		version = version + "SRB"
	elif train.startswith("SRC"):
		version = version + "SRC"
	elif train.startswith("SRD"):
		version = version + "SRD"
	elif train.startswith("SRE"):
		version = version + "SRE"
	elif train.startswith("SR"):
		version = version + "SR"
	elif train.startswith("SS"):
		version = version + "SS"
	elif train.startswith("STE"):
		version = version + "STE"
	elif train.startswith("ST"):
		version = version + "ST"
	elif train.startswith("SU"):
		version = version + "SU"
	elif train.startswith("SVA"):
		version = version + "SVA"
	elif train.startswith("SVB"):
		version = version + "SVB"
	elif train.startswith("SVC"):
		version = version + "SVC"
	elif train.startswith("SVD"):
		version = version + "SVD"
	elif train.startswith("SVE"):
		version = version + "SVE"
	elif train.startswith("SVF"):
		version = version + "SVF"
	elif train.startswith("SV"):
		version = version + "SV"
	elif train.startswith("SW"):
		version = version + "SW"
	elif train.startswith("SXA"):
		version = version + "SXA"
	elif train.startswith("SXB"):
		version = version + "SXB"
	elif train.startswith("SXD"):
		version = version + "SXD"
	elif train.startswith("SXE"):
		version = version + "SXE"
	elif train.startswith("SXF"):
		version = version + "SXF"
	elif train.startswith("SXH"):
		version = version + "SXH"
	elif train.startswith("SXI"):
		version = version + "SXI"
	elif train.startswith("SXJ"):
		version = version + "SXJ"
	elif train.startswith("SX"):
		version = version + "SX"
	elif train.startswith("SYA"):
		version = version + "SYA"
	elif train.startswith("SYL"):
		version = version + "SYL"
	elif train.startswith("SY"):
		version = version + "SY"
	elif train.startswith("SZ"):
		version = version + "SZ"
	elif train.startswith("S"):
		version = version + "S"
	elif train.startswith("TPC"):
		version = version + "TPC"
	elif train.startswith("TO"):
		version = version + "TO"
	elif train.startswith("T"):
		version = version + "T"
	elif train.startswith("UZ"):
		version = version + "UZ"
	elif train.startswith("VZ"):
		version = version + "VZ"
	elif train.startswith("WC"):
		version = version + "WC"
	elif train.startswith("WO"):
		version = version + "WO"
	elif train.startswith("WX"):
		version = version + "WX"
	elif train.startswith("XA"):
		version = version + "XA"
	elif train.startswith("XB"):
		version = version + "XB"
	elif train.startswith("XC"):
		version = version + "XC"
	elif train.startswith("XD"):
		version = version + "XD"
	elif train.startswith("XE"):
		version = version + "XE"
	elif train.startswith("XF"):
		version = version + "XF"
	elif train.startswith("XG"):
		version = version + "XG"
	elif train.startswith("XH"):
		version = version + "XH"
	elif train.startswith("XI"):
		version = version + "XI"
	elif train.startswith("XJ"):
		version = version + "XJ"
	elif train.startswith("XK"):
		version = version + "XK"
	elif train.startswith("XL"):
		version = version + "XL"
	elif train.startswith("XM"):
		version = version + "XM"
	elif train.startswith("XNA"):
		version = version + "XNA"
	elif train.startswith("XNB"):
		version = version + "XNB"
	elif train.startswith("XNC"):
		version = version + "XNC"
	elif train.startswith("XND"):
		version = version + "XND"
	elif train.startswith("XNE"):
		version = version + "XNE"
	elif train.startswith("XO"):
		version = version + "XO"
	elif train.startswith("XP"):
		version = version + "XP"
	elif train.startswith("XQ"):
		version = version + "XQ"
	elif train.startswith("XR"):
		version = version + "XR"
	elif train.startswith("XS"):
		version = version + "XS"
	elif train.startswith("XT"):
		version = version + "XT"
	elif train.startswith("XU"):
		version = version + "XU"
	elif train.startswith("XV"):
		version = version + "XV"
	elif train.startswith("XW"):
		version = version + "XW"
	elif train.startswith("XX"):
		version = version + "XX"
	elif train.startswith("XY"):
		version = version + "XY"
	elif train.startswith("XZ"):
		version = version + "XZ"
	elif train.startswith("YA"):
		version = version + "YA"
	elif train.startswith("YB"):
		version = version + "YB"
	elif train.startswith("YC"):
		version = version + "YC"
	elif train.startswith("YD"):
		version = version + "YD"
	elif train.startswith("YE"):
		version = version + "YE"
	elif train.startswith("YF"):
		version = version + "YF"
	elif train.startswith("YG"):
		version = version + "YG"
	elif train.startswith("YH"):
		version = version + "YH"
	elif train.startswith("YI"):
		version = version + "YI"
	elif train.startswith("YJ"):
		version = version + "YJ"
	elif train.startswith("YK"):
		version = version + "YK"
	elif train.startswith("YL"):
		version = version + "YL"
	elif train.startswith("YM"):
		version = version + "YM"
	elif train.startswith("YN"):
		version = version + "YN"
	elif train.startswith("YO"):
		version = version + "YO"
	elif train.startswith("YP"):
		version = version + "YP"
	elif train.startswith("YQ"):
		version = version + "YQ"
	elif train.startswith("YR"):
		version = version + "YR"
	elif train.startswith("YS"):
		version = version + "YS"
	elif train.startswith("YT"):
		version = version + "YT"
	elif train.startswith("YU"):
		version = version + "YU"
	elif train.startswith("YV"):
		version = version + "YV"
	elif train.startswith("YW"):
		version = version + "YW"
	elif train.startswith("YX"):
		version = version + "YX"
	elif train.startswith("YZ"):
		version = version + "YZ"
	elif train.startswith("YZ"):
		version = version + "YZ"
	elif train.startswith("ZA"):
		version = version + "ZA"
	elif train.startswith("ZB"):
		version = version + "ZB"
	elif train.startswith("ZC"):
		version = version + "ZC"
	elif train.startswith("ZD"):
		version = version + "ZD"
	elif train.startswith("ZE"):
		version = version + "ZE"
	elif train.startswith("ZF"):
		version = version + "ZF"
	elif train.startswith("ZG"):
		version = version + "ZG"
	elif train.startswith("ZH"):
		version = version + "ZH"
	elif train.startswith("ZI"):
		version = version + "ZI"
	elif train.startswith("ZJ"):
		version = version + "ZJ"
	elif train.startswith("ZK"):
		version = version + "ZK"
	elif train.startswith("ZL"):
		version = version + "ZL"
	elif train.startswith("ZN"):
		version = version + "ZN"
	elif train.startswith("ZO"):
		version = version + "ZO"
	elif train.startswith("ZP"):
		version = version + "ZP"
	elif train.startswith("ZQ"):
		version = version + "ZQ"
	elif train.startswith("ZR"):
		version = version + "ZR"
	elif train.startswith("ZS"):
		version = version + "ZS"
	elif train.startswith("ZT"):
		version = version + "ZT"
	elif train.startswith("ZU"):
		version = version + "ZU"
	elif train.startswith("ZV"):
		version = version + "ZV"
	elif train.startswith("ZW"):
		version = version + "ZW"
	elif train.startswith("ZX"):
		version = version + "ZX"
	elif train.startswith("ZYA"):
		version = version + "ZYA"
	elif train.startswith("ZY"):
		version = version + "ZY"
	elif train.startswith("ZZ"):
		version = version + "ZZ"
	return version

def imagelookup(imagecode):
	imagecode_to_subdirectory = {
		"a2i5k8s": "IP-ATM-PLUS-IPSEC-56-NO-ISDN",
		"a2i5s": "IP-ATM-PLUS-NO-ISDN",
		"a2i8k8sv5": "IP-ATM-VOIP-VOATM-PLUS-IPSEC-56",
		"a2i8sv5": "IP-ATM-VOIP-VOATM",
		"a2ik8sv5": "IP-PLUS-VOIP-VOATM-IPSEC-56",
		"a2isv5": "IP-PLUS-VOIP-VOATM",
		"a2jk2sv5": "ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-3DES",
		"a2jk8sv5": "ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-56",
		"a2jk9sv5": "ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-3DES",
		"a2jsv5": "ENTERPRISE-PLUS-VOIP-VOATM",
		"a2jsv5x": "ENTERPRISE-PLUS-H323-MCM",
		"a3bik9no3rsx3": "IP-VOICE-IPX-SNA-FW-IDS-WAN-3DES",
		"a3i3r4": "IP-IBM-SNASW",
		"a3inro3sx3": "IP-PLUS-FW-IPX-SNA",
		"a3inrsx3c": "IP-PLUS-IPX-SNA",
		"a3is": "IP-PLUS-SNASW-PLUS",
		"a3jk2s": "ENTERPRISE-SNASW-PLUS-IPSEC-3DES",
		"a3jk2sv": "ENTERPRISE-SNASW-IPSEC-3DES",
		"a3jk8s": "ENTERPRISE-SNASW-IPSEC-56",
		"a3jk8sv": "ENTERPRISE-SNASW-IPSEC-56",
		"a3jk91s": "ENTERPRISE-SNASW-SSH-3DES",
		"a3jk9s": "ENTERPRISE-SNASW-IPSEC-3DES",
		"a3jk9sv": "ENTERPRISE-SNASW-IPSEC-3DES",
		"a3js": "ENTERPRISE-SNASW-PLUS",
		"a3js56i": "ENTERPRISE-SNASW-PLUS-IPSEC-56",
		"a3jsv": "ENTERPRISE-SNASW",
		"a3jsv56i": "ENTERPRISE-SNASW-IPSEC-56",
		"aciplgms": "PLUG-INS/MICROSOFT",
		"aciplgvc": "PLUG-INS/VCENTER",
		"aciplgvs": "PLUG-INS/VREALIZE",
		"acisim": "ACI-SIMULATOR",
		"acive": "ACI-VIRTUAL-EDGE",
		"acs_mig": "ACS-MIGRATION",
		"adjv": "ENTERPRISE-APPN",
		"adjv40": "ENTERPRISE-APPN-40",
		"adjv56": "ENTERPRISE-APPN-56",
		"ads": "DESKTOP-IBM",
		"ads40": "DESKTOP-IBM-40",
		"ads56": "DESKTOP-IBM-56",
		"adsv": "DESKTOP-IBM-APPN",
		"adventerprise": "ADVANCED-ENTERPRISE-SERVICES-NO-CRYPTO",
		"adventerprise_wan": "ADVANCED-ENTERPRISE-SERVICES-NO-CRYPTO",
		"adventerprisek9": "ADVANCED-ENTERPRISE-SERVICES",
		"adventerprisek9_ivs": "INT-VOICE-VIDEO-GK,-IPIP-GW,-TDMIP-GW-AES",
		"adventerprisek9_ivs_li": "INT-VOICE-VIDEO-GK,-IPIP-GW,-TDMIP-GW-AES,-LI",
		"adventerprisek9_li": "ADVANCED-ENTERPRISE-SERVICES-WITH-LAWFUL-INTERCEPT",
		"adventerprisek9_mw": "GGSN-RELEASE-6-IPSEC",
		"adventerprisek9_noli": "ADVANCED-ENTERPRISE-SERVICES-NO-LAWFUL-INTERCEPT",
		"adventerprisek9_npe": "ADVANCED-ENTERPRISE-SERVICES-NPE",
		"adventerprisek9_sna": "ADVANCED-ENTERPRISE-SERVICES-SNA",
		"adventerprisek9_wan": "ADVANCED-ENTERPRISE-SERVICES",
		"adviprank9": "RAN-OPTIMIZATION",
		"advipservices": "ADVANCED-IP-SERVICES-NO-CRYPTO",
		"advipservicesk9": "ADVANCED-IP-SERVICES",
		"advipservicesk9_li": "ADVANCED-IP-SERVICES-WITH-LAWFUL-INTERCEPT",
		"advipservicesk9_noli": "ADVANCED-IP-SERVICES-WITHOUT-LAWFUL-INTERCEPT",
		"advipservicesk9_npe": "ADVANCED-IP-SERVICES-NPE",
		"advipservicesk9_wan": "ADVANCED-IP-SERVICES",
		"advseck9": "ADVANCED-SECURITY",
		"advseck9_npe": "ADVANCED-SECURITY-NPE",
		"advsecurityk9": "ADVANCED-SECURITY",
		"advsecurityk9_npe": "ADVANCED-SECURITY-NPE",
		"aejs": "ENTERPRISE/APPN/DBCONN",
		"aejs": "ENTERPRISE-APPN-DBCONN",
		"aejs40": "ENTERPRISE/APPN/DBCONN 40",
		"aejs56i": "ENTERPRISE/APPN/DBCONN IPSEC 56",
		"aejsv": "ENTERPRISE-APPN-DBCONN",
		"aejsv40": "ENTERPRISE-APPN-DBCONN-40",
		"aejsv56i": "ENTERPRISE-APPN-DBCONNC-56",
		"ai3r4": "IP-IBM-APPN7",
		"ainr": "IP-IPX-IBM-APPN",
		"ajs": "ENTERPRISE-APPN-PLUS",
		"ajs40": "ENTERPRISE-APPN-PLUS-IPSEC-40",
		"ajs56i": "ENTERPRISE-APPN-PLUS-IPSEC-56",
		"ajsv": "ENTERPRISE-APPN",
		"ajsv40": "ENTERPRISE-APPN-40",
		"ajsv56": "ENTERPRISE-APPN-56",
		"ajsv56i": "ENTERPRISE-APPN-IPSEC-56",
		"amp": "ADVANCED-MALWARE-PROTECTION",
		"analogmodem": "ANALOG-MODEM",
		"android": "ANDROID",
		"anyconnect_posture": "POSTURE (FORMERLY HOST-SCAN)",
		"anyconnectnam": "NETWORK-ACCESS-MANAGER",
		"apbundle": "AP-BUNDLE",
		"apdp": "ACCESS-POINT-DEVICE-PACK",
		"apic": "APIC-CONTROLLER",
		"app_selector": "APP-SELECTOR",
		"appqoe": "QoE",
		"apsp": "ACCESS-POINT-SERVICE-PACK",
		"aptolwapp": "AP-TO-LWAPP-CONVERTER",
		"asdm": "ADAPTIVE-SECURITY-DEVICE-MANAGER",
		"asdmf": "ADAPTIVE-SECURITY-DEVICE-MANAGER-ASASM",
		"base": "BASE",
		"basevga": "BASE-VGA",
		"bin": "IP-IPX-APPLETALK",
		"bino3s": "IP-IPX-APPLETALK-PLUS-FW-IDS",
		"bino3s3": "IP-IPX-AT-FW-IDS-PLUS-BASIC",
		"binrsx3": "IP-VOICE-IPV6-IPX-APPLE-TALK",
		"bins": "IP-IPX-APPLETALK-PLUS",
		"bios": "BIOS",
		"bk2no3r2sv3y": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-3DES",
		"bk2no3r2sv3y7": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-3DES-ADSL",
		"bk2no3r2sy": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-3DES",
		"bk2no3r2sy7": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-3DES-ADSL",
		"bk2nor2sv3y": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-3DES",
		"bk2nor2sy": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-3DES",
		"bk8no3r2sv3": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-56",
		"bk8no3r2sv3y": "IP-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-56",
		"bk8no3r2sv3y7": "IP-ADSL-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-56",
		"bk8no3r2sv8y7": "IP-ADSL-IPX-AT-IBM-VOX-FW-IDS-PLUS-IPSEC-56",
		"bk8no3r2sy": "IP-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-56",
		"bk8no3r2sy7": "IP-ADSL-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-56",
		"bk8nor2sy": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-56",
		"bk9no3r2sv3y": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-3DES",
		"bk9no3r2sv3y7": "IP-ADSL-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-3DES",
		"bk9no3r2sv8y7": "IP-ADSL-IPX-AT-IBM-VOX-FW-IDS-PLUS-IPSEC-3DES",
		"bk9no3r2sy": "IP-PLUS-IPX-AT-IBM-FW_IDS-IPSEC-3DES",
		"bk9no3r2sy7": "IP-ADSL-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-3DES",
		"bno3r2sv3y56i": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-56",
		"bno3r2sv3y756i": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-56-ADSL",
		"bno3r2sy56i": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-56",
		"bno3r2sy756i": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-56-ADSL",
		"bnor2sv3y56i": "IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-56",
		"bnor2sy56": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-56",
		"bnor2sy56i": "IP-IPX-AT-IBM-FW-PLUS-IPSEC-56",
		"bnr2sv3y": "IP-IPX-AT-IBM-VOICE-PLUS",
		"bnr2sy": "IP-IPX-AT-IBM-PLUS",
		"bnr2sy40": "IP-IPX-AT-IBM-PLUS-40",
		"bnr2sy56": "IP-IPX-AT-IBM-PLUS-56",
		"bnr2sy56i": "IP-IPX-AT-IBM-PLUS-IPSEC-56",
		"bnr2sy7": "IP-ADSL-IPX-AT-IBM-PLUS",
		"bnr2y": "IP-IPX-AT-IBM",
		"bnsy": "IP-IPX-AT-PLUS",
		"bnsy40": "IP-IPX-AT-PLUS-40",
		"bnsy56": "IP-IPX-AT-PLUS-56",
		"bny": "IP-IPX-AT",
		"boot": "BOOT",
		"bridge_smus": "BRIDGE-SMUS",
		"broadband": "IP-BROADBAND",
		"bsy": "IP-AT-PLUS",
		"bsy40": "IP-AT-PLUS-40",
		"bsy56": "IP-AT-PLUS-56",
		"by": "IP-AT",
		"c": "REMOTE-ACCESS-SERVER-(RAS)",
		"c3h2": "STANDARD-COMMAND-CAPABLE",
		"c3h2l9s": "LONG-REACH-ETHERNET",
		"c3h2s": "ENTERPRISE-COMMAND-CAPABLE",
		"c5ik9s": "BASE-PDSN-3DES",
		"c5is": "BASE-PDSN",
		"c6ik9s": "ENHANCED-PDSN-WITH-CRYPTO",
		"c6is": "ENHANCED-PDSN",
		"C819GWLTEMNAAK9": "C819GW-LTE-MNA-AK9",
		"capacity-emulator": "CAPACITY-EMULATOR",
		"cat9k_iosxe": "UNIVERSAL",
		"cat9k_iosxe_npe": "UNIVERSAL-NPE",
		"cat9k_iosxeldpe": "UNIVERSAL-NO-DTLS",
		"cat9k_lite_iosxe": "UNIVERSAL-LITE",
		"cat9k_lite_iosxe_npe": "UNIVERSAL-LITE-NPE",
		"catalog": "DEVICE-CATALOG",
		"cboot": "BOOT",
		"certs": "CERTIFICATES",
		"cgv6": "CARRIER-GRADE-NAT-V4-V6",
		"ciscosoftwaremanager": "CISCO-SOFTWARE-MANAGER",
		"clean": "CLEAN-UTILITY",
		"client": "CLIENT",
		"cme": "CALL-MANAGER-EXPRESS",
		"cnbng": "PACKAGE-BROADBAND-NETWORK-GATEWAY",
		"configconvert": "CONFIG-CONVERTER",
		"config-converter": "CONFIG-CONVERTER",
		"control-plane": "CONTROL-PLANE",
		"core": "CORE-SOFTWARE",
		"core64": "CORE-SOFTWARE-X64",
		"core64k9": "CORE-SOFTWARE-X64-CRYPTO",
		"corek9": "CORE-SOFTWARE-CRYPTO",
		"cpld_update": "CPLD-UPDATE",
		"csd": "CISCO-SECURE-DESKTOP",
		"csfgeodb": "GeoDB-SRU-VDB/Geodb-6.4-AND-LATER",
		"csfrules": "GeoDB-SRU-VDB/Rules-6.4-AND-LATER",
		"csfvdb": "GeoDB-SRU-VDB/VDB-6.4-AND-LATER",
		"csg": "CSG2-RTU-SAMI-NO-CRYPTO",
		"csgk9": "CSG2-RTU-SAMI",
		"csmgeoip": "CSM-GEOIP-DB",
		"d": "IP-IPX-AT-DEC",
		"dart": "DIAGNOSTICS-AND-REPORTING",
		"data-plane": "DATA-PLANE",
		"dboot": "BOOT",
		"dboot2": "BOOT",
		"deploymentassistant": "DEPLOYMENT-ASSISTANT",
		"devicemgr": "DEVICE-MANAGER",
		"device-pack": "DEVICE-PACK",
		"dk2o3s": "DESKTOP-IBM-FW-IDS-IPSEC-3DES",
		"dk2o3sv": "DESKTOP-IBM-FW-IDS-IPSEC-3DES",
		"dk8o3s": "DESKTOP-IBM-FW-IDS-IPSEC-56",
		"dk8o3sv": "DESKTOP-IBM-FW-IDS-IPSEC-56",
		"dk8s": "DESKTOP-IBM-IPSEC-56",
		"dk8sv": "DESKTOP-IBM-IPSEC-56",
		"dk9o3s": "DESKTOP-IBM-FW-IDS-IPSEC-3DES",
		"dk9o3sv": "DESKTOP-IBM-FW-IDS-IPSEC-3DES",
		"dmon": "DMON",
		"do3s": "DESKTOP-IBM-FW-IDS",
		"do3s56i": "DESKTOP-IBM-FW-IDS-IPSEC-56",
		"do3sv": "DESKTOP-IBM-FW-IDS",
		"do3sv56i": "DESKTOP-IBM-FW-IDS-IPSEC-56",
		"docs": "DOCUMENTATION",
		"dos": "IP-IPX-AT-DEC-FW-PLUS",
		"drivers": "DRIVERS",
		"driverseseries": "DRIVERS",
		"driversucsb": "B-SERIES/DRIVERS",
		"driversucsc": "C-SERIES/DRIVERS",
		"driversucse": "E-SERIES/DRIVERS",
		"ds": "IP-IPX-AT-DEC-PLUS",
		"ds40": "IP-IPX-AT-DEC-PLUS-40",
		"ds56": "DESKTOP-IBM-56",
		"ds56i": "DESKTOP-IBM-IPSEC-56",
		"dsc": "DIAL-SHELF-CONTROLLER",
		"dsl": "DSL",
		"dslfirmware": "DSL-FIRMWARE",
		"dsv": "DESKTOP-IBM",
		"dsv40": "DESKTOP-IPSEC-40",
		"dsv56": "DESKTOP-IBM-IPSEC-56",
		"dsv56i": "DESKTOP-IBM-IPSEC-56",
		"eboot": "BOOT",
		"efi": "EFI",
		"EHWIC4GLTEAT": "EHWIC-4G-LTE-AT",
		"EHWIC4GLTEAU": "EHWIC-4G-LTE-AU",
		"EHWIC4GLTECA": "EHWIC-4G-LTE-CA",
		"EHWIC4GLTEGB": "EHWIC-4G-LTE-GB",
		"EHWIC4GLTEST": "EHWIC-4G-LTE-ST",
		"EHWIC4GLTEVZ": "EHWIC-4G-LTE-VZ",
		"EHWICCELLATT": "EHWIC-4G-LTE-A",
		"EHWICCELLBE": "EHWIC-4G-LTE-BE",
		"EHWICCELLEU": "EHWIC-4G-LTE-EU",
		"EHWICCELLG": "EHWIC-4G-LTE-G",
		"EHWICCELLVZW": "EHWIC-4G-LTE-V",
		"EHWICVADSLB": "EHWIC-VA-DSL-B-C886VA-C896VA",
		"emailsecurity": "EMAIL-SECURITY-APPLIANCE",
		"engine": "ENGINE",
		"engine0": "ENGINE-0",
		"engine1": "ENGINE-1",
		"engine2": "ENGINE-2",
		"engine3": "ENGINE-3",
		"engine4": "ENGINE-4",
		"entbase": "ENTERPRISE-BASE-NO-CRYPTO",
		"entbasek9": "ENTERPRISE-BASE",
		"entservices": "ENTERPRISE-SERVICES-NO-CRYPTO",
		"entservices_mw": "GGSN-RELEASE-6",
		"entservices_wan": "ENTERPRISE-SERVICES-NO-CRYPTO",
		"entservicesk9": "ENTERPRISE-SERVICES",
		"entservicesk9_wan": "ENTERPRISE-SERVICES",
		"epld": "FIRMWARE-EPLD",
		"events": "EVENTS",
		"export": "EXPORT-FILES",
		"expresswizard": "EXPRESS-WIZARD",
		"external-sso": "EXTERNAL-SSO",
		"f": "FRAD",
		"f2in": "LAN-FRAD-OSPF",
		"fabman": "FABRIC-MANAGER",
		"fdiagsbflc": "FIELD-DIAGNOSTICS-LINECARD-IMAGE",
		"fin": "FRAD-EIGRP",
		"fin-l": "LAN-FRAD",
		"fips": "FIPS",
		"firepower-mibs": "FIREPOWER-MIBS",
		"firmware": "FIRMWARE",
		"firmwareeseries": "FIRMWARE",
		"flashrecovery": "FLASH-RECOVERY",
		"fmc": "FIREPOWER-MANAGEMENT-CENTER",
		"fpasamode": "FIREPOWER-ASA-MODE/FIREPOWER-MODULE",
		"fpasamodule": "MODULE-ASA",
		"fpasasystem": "FIREPOWER-ASA-MODE/SYSTEM",
		"fpd": "FIELD-PROGRAMABLE-DEVICE",
		"fpftdmodule": "MODULE-FTD",
		"fpftdsoftware": "SOFTWARE-FTD",
		"fpga": "FPGA-UPGRADE",
		"fwsmtoasasm": "FWSM-TO-ASASM-CONVERSION",
		"fxos-k9": "FXOS",
		"fxos-k9-fpr4k-firmware": "FIRMWARE-4K",
		"fxos-k9-fpr9k-firmware": "FIRMWARE-9K",
		"fxos-k9-kickstart": "FXOS-RECOVERY/KICKSTART",
		"fxos-k9-manager": "FXOS-RECOVERY/MANAGER",
		"fxos-k9-system": "FXOS-RECOVERY/SYSTEM",
		"fxos-mibs-fp9k-fp4k": "FIREPOWER-MIBS-9K-4K",
		"g": "ISDN",
		"g4js": "ENTERPRISE-SSG",
		"g4p5": "NSP-SYSTEM",
		"g5jk8s": "ENTERPRISE-WIRELESS-IPSEC-56",
		"g5js": "ENTERPRISE-WIRELESS",
		"g6ik8s": "GGSN-4.0-IPSEC",
		"g6ik9s": "GGSN-4.0-3DES",
		"g6is": "GGSN-4.0-BASE",
		"g7is": "GGSN-SERIES-4-BASE",
		"g8ik8s": "GGSN-SERIES-6-IPSEC",
		"g8ik9s": "GGSN-SERIES-6-3DES",
		"g8is": "GGSN-SERIES-6-BASE",
		"gina": "GINA-MODULE",
		"goldenk9": "GOLDEN-IMAGE",
		"guestshell": "Nexus-Guestshell",
		"h1is": "MW-HOME-AGENT",
		"h2": "STANDARD",
		"hardware": "HARDWARE-PROGRAMMABLES",
		"hdiag": "DIAGNOSTICS",
		"hostscan": "HOST-SCAN",
		"hotfix": "HOTFIX",
		"html": "HTML",
		"huu": "HOST-UPGRADE-UTILITY",
		"HWIC3GGSM": "HWIC-3G-GSM",
		"HWICCABLE": "HWIC-CABLE",
		"hyperv": "HYPERv",
		"i": "IP",
		"i12o3s": "ACCELERATED-BB-WITH-FW-INTRUSION-DETECTION",
		"i12s": "ACCELERATED-BROADBAND-LAC-LNS-PTA",
		"i4s": "IP-PLUS",
		"i5": "IP-SERVICES-NO-CRYPTO",
		"i5k2": "IP-SERVICES",
		"i5k2l2q3": "IP-SERVICES",
		"i5k8s": "IP-PLUS-IPSEC-56-NO-ISDN",
		"i5k91": "IP-SERVICES",
		"i5k91l2q3": "IP-SERVICES",
		"i5k91s": "ENHANCED-L3-3DES",
		"i5k9s": "IP-PLUS-IPSEC-3DES-NO-ISDN",
		"i5q312": "IP-SERVICES",
		"i5q3l2": "IP-SERVICES-NO-CRYPTO",
		"i5s": "ENHANCED-L3",
		"i5su3": "MPEG-2-L3",
		"i6k2l2q4": "EI-AND-SI-CRYPTO",
		"i6k9o3s": "IP-SUBSET-IPSEC-56-FW-VOICE",
		"i6k9s": "IP-SUBSET-IPSEC-64-BIT-VOICE",
		"i6l2q4": "LONG-REACH-ETHERNET-NO-CRYPTO",
		"i6q4l2": "LAYER-2",
		"i6s": "IP-SUBSET-VOICE",
		"i9": "IP-BASE-NO-CRYPTO",
		"i9k2": "IP-BASE",
		"i9k2l2q3": "IP-BASE",
		"i9k91": "IP-BASE",
		"i9k91l2q3": "IP-BASE",
		"i9k91s": "L3-VOICE",
		"i9k91sc": "BASIC-L3-3DES",
		"i9q3l2": "IP-BASE-NO-CRYPTO",
		"i9s": "BASIC-L3",
		"i9su3": "MPEG-2-L2",
		"ik2o3s": "IP-FW-IDS-IPSEC-3DES",
		"ik2o3sv": "IP-FW-IDS-IPSEC-3DES",
		"ik2o3sx3": "IP-PLUS-3DES-FW",
		"ik2s": "IP-PLUS-IPSEC-3DES",
		"ik2sv": "IP-PLUS-IPSEC-3DES",
		"ik2sx3": "IP-PLUS-3DES",
		"ik8o3s": "IP-FW-IDS-IPSEC-56",
		"ik8o3sv": "IP-FW-IDS-IPSEC-56",
		"ik8os": "IP-FW-PLUS-IPSEC-56",
		"ik8s": "IP-PLUS-IPSEC-56",
		"ik8su2": "DOCSIS-2-WAY-BPI-IP+-LAWFUL-INTERCEPT",
		"ik8sv": "IP-IPSEC-56",
		"ik91s": "IP-PLUS-SSH-3DES",
		"ik9o3s": "IP-FW-IDS-IPSEC-3DES",
		"ik9o3s3": "IP-FW-IDS-PLUS-IPSEC-3DES-BASIC",
		"ik9o3s6": "IP-FW-IDS-PLUS-IPSEC-3DES-BASIC-NO-ATM",
		"ik9o3s7": "IP-FW-IDS-PLUS-IPSEC-3DES-BASIC-NO-VOICE",
		"ik9o3sv": "IP-FW-IDS-IPSEC-3DES",
		"ik9s": "IP-PLUS-IPSEC-3DES",
		"ik9su2": "IP-IPSEC-3DES-LAWFUL-INTERCEPT",
		"ik9sv": "IP-PLUS-IPSEC-3DES",
		"imgwrt": "IMAGE-WRITING",
		"in": "IP-BRIDGING",
		"ino3s3": "IP-IPX-FW-IDS-PLUS-BASIC",
		"ins": "IP-IPX-PLUS",
		"install": "INSTALL",
		"installer": "INSTALLER",
		"installer-ase": "INSTALLER-ASE",
		"inu": "NETWORK-LAYER-3-SWITCHING",
		"io": "IP-FW",
		"io3": "IP-FW-IDS",
		"io3s": "IP-FW-IDS",
		"io3s56i": "IP-FW-PLUS-IPSEC-56",
		"io3sv": "IP-FW-IDS",
		"io3sv56i": "IP-FW-IDS-IPSEC-56",
		"io3sx3": "IP-PLUS-FW",
		"io3sx356i": "IP-PLUS-IPSEC-56-FW",
		"ios56i": "IP-FW-PLUS-IPSEC-56",
		"iosxe": "UNIVERSAL",
		"iosxr": "IP-MPLS",
		"ipbase": "IP-BASE-NO-CRYPTO",
		"ipbase_access": "IP-BASE-ACCESS-ONLY-NO-CRYPTO",
		"ipbase_wan": "IP-BASE-NO-CRYPTO",
		"ipbasek9": "IP-BASE",
		"ipbasek9_access": "IP-BASE-ACCESS-ONLY",
		"ipbasek9_npe": "IP-BASE-NPE",
		"ipbasek9_wan": "IP-BASE",
		"ipbasek9npe": "IP-BASE-NPE",
		"ipbaselm": "IP-BASE-NO-CRYPTO-WITH-EXPRESS-SETUP",
		"ipbaselmk9": "IP-BASE-WITH-EXPRESS-SETUP",
		"ipran": "RAN-OPTIMIZATION-NO-CRYPTO",
		"iprank9": "RAN-OPTIMIZATION",
		"ipservices": "IP-SERVICES-NO-CRYPTO",
		"ipservices_wan": "IP-SERVICES-NO-CRYPTO",
		"ipservicesk9": "IP-SERVICES",
		"ipservicesk9_li": "IP-SERVICES-WITH-LAWFUL-INTERCEPT",
		"ipservicesk9_npe": "IP-SERVICES-NPE",
		"ipservicesk9_wan": "IP-SERVICES",
		"ipserviceslm": "IP-SERVICES-NO-CRYPTO-WITH-EXPRESS-SETUP",
		"ipserviceslmk9": "IP-SERVICES-WITH-EXPRESS-SETUP",
		"ipserviceslmk9_en": "IP-SERVICES-EXPRESS-SETUP-ENGLISH",
		"ipss7": "SS7-SIGNALING-LINK",
		"ipv": "IP-TRANSFER-POINT",
		"ipvoice": "IP-VOICE-NO-CRYPTO",
		"ipvoice_ivs": "INT-VOICE-VIDEO,-IPIP-GW,-TDMIP-GW",
		"ipvoicek9": "IP-VOICE",
		"is": "IP-PLUS",
		"is3x": "IP-H323-PLUS-BASIC",
		"is4": "IP-PLUS-BASIC-WITHOUT-SWITCHING",
		"is40": "IP-PLUS-40",
		"is5": "IP-PLUS-BASIC-WITHOUT-HD-ANALOG-AIM-ATM-VOICE",
		"is56": "IP-PLUS-56",
		"is56i": "IP-PLUS-IPSEC-56",
		"isecompliance": "ISE-COMPLIANCE",
		"iseposture": "ISE-POSTURE",
		"ISRG2PVDMODEM": "ISR-G2-DIGITAL-MODEM",
		"isu2": "IP-LAWFUL-INTERCEPT",
		"isv": "IP",
		"isv40": "IP-40",
		"isv56": "IP-56",
		"isv56i": "IP-IPSEC-56",
		"isx3": "IP-VOICE",
		"isx356i": "IP-PLUS-IPSEC-56",
		"itp": "IP-TRANSFER-POINT",
		"itpk9": "IP-MAP-GATEWAY-BASE",
		"itpk9v": "IP-TRANSFER-POINT",
		"itpv": "IP-TRANSFER-POINT",
		"itv": "IP-ACIP",
		"ix": "IP-H323",
		"j": "ENTERPRISE",
		"j1s3": "ENTERPRISE-BASIC",
		"jk2o3s": "ENTERPRISE-FW-IDS-PLUS-IPSEC-3DES",
		"jk2o3sv": "ENTERPRISE-FW-IDS-IPSEC-3DES",
		"jk2s": "ENTERPRISE-SSH-3DES-LAN-ONLY",
		"jk2sv": "ENTERPRISE-IPSEC-3DES",
		"jk8o3s": "ENTERPRISE-FW-IDS-IPSEC-56",
		"jk8o3sv": "ENTERPRISE-FW-IDS-IPSEC-56",
		"jk8os": "ENTERPRISE-FW-PLUS-IPSEC-56",
		"jk8s": "ENTERPRISE-IPSEC-56",
		"jk8sv": "ENTERPRISE-IPSEC-56",
		"jk9o3s": "ENTERPRISE-FW-IDS-IPSEC-3DES",
		"jk9o3sv": "ENTERPRISE-FW-MPLS-IPV6-SSH-3DES",
		"jk9s": "ENTERPRISE-IPSEC-3DES",
		"jk9s2": "VOICE-IP-TO-IP-VOICE-GATEWAY-IPSEC-3DES",
		"jk9su2": "ENTERPRISE-IPSEC-3DES-LAWFUL-INTERCEPT",
		"jk9su2_ivs": "INT-VOICE-VIDEO-IPIP-GW,-TDMIP-GW-LI",
		"jk9su2v": "ENTERPRISE-IPSEC-3DES-LAWFUL-INTERCEPT",
		"jk9sv": "ENTERPRISE-IPV6-SSH-3DES",
		"jo3s": "ENTERPRISE-FW-IDS",
		"jo3s56i": "ENTERPRISE-FW-IDS-IPSEC-56",
		"jo3sv": "ENTERPRISE-FW-IDS",
		"jo3sv56i": "ENTERPRISE-FW-IDS-IPSEC-56",
		"jos56": "ENTERPRISE-FW-PLUS-56",
		"jos56i": "ENTERPRISE-FW-PLUS-IPSEC-56",
		"js": "ENTERPRISE-PLUS",
		"js_ivs": "INT-VOICE-VIDEO-IPIP-GW,-TDMIP-GW",
		"js2": "VOICE-IP-TO-IP-VOICE-GATEWAY",
		"js40": "ENTERPRISE-PLUS-40",
		"js56": "ENTERPRISE-PLUS-56",
		"js56i": "ENTERPRISE-PLUS-IPSEC-56",
		"jsu2": "ENTERPRISE-LAWFUL-INTERCEPT",
		"jsv": "ENTERPRISE",
		"jsv40": "ENTERPRISE-40",
		"jsv56": "ENTERPRISE-56",
		"jsv56i": "ENTERPRISE-IPSEC-56",
		"jsx": "ENTERPRISE-PLUS-H323-MCM",
		"jx2": "ENTERPRISE-MCM",
		"k": "ENTERPRISE",
		"k1k2o3sv4y5": "SMALL-OFFICE+-VOICE-FW-IPSEC-3DES-(SGCP-and-H.323)",
		"k1k2sv4y5": "TELECOMMUTER+-VOICE-IPSEC-3DES-(SGCP-and-H.323)",
		"k1o3sv4y556i": "SMALL-OFFICE+-VOICE-FW-IDS-IPSEC-56-(SGCP-and-H.323)",
		"k1o3v4y5": "SMALL-OFFICE-VOICE-FW-IDS-(SGCP-and-H.323)",
		"k1sv4y556i": "TELECOMMUTER-VOICE-IPSEC-56-(SGCP-and-H.323)",
		"k1v4y5": "HOME-OFFICE-VOICE-(SGCP-and-H.323)",
		"k2": "ENTERPRISE-CIP2",
		"k2nosy6": "IP-IPX-FW-PLUS-IPSEC-3DES",
		"k2o3sv3y": "IP-FW-VOICE-PLUS-IPSEC-3DES",
		"k2o3sv3y7": "IP-FW-VOICE-PLUS-IPSEC-3DES-ADSL",
		"k2o3sy": "IP-FW-PLUS-IPSEC-3DES",
		"k2o3sy7": "IP-FW-PLUS-IPSEC-3DES-ADSL",
		"k2osv3y": "IP-FW-VOICE-PLUS-IPSEC-3DES",
		"k2osy": "IP-FW-PLUS-IPSEC-3DES",
		"k2osy6": "IP-FW-PLUS-IPSEC-3DES",
		"k2sv3y": "IP-VOICE-PLUS-IPSEC-3DES",
		"k2sv3y7": "IP-VOICE-PLUS-IPSEC-3DES-ADSL",
		"k2sy": "IP-PLUS-IPSEC-3DES",
		"k2sy7": "IP-PLUS-IPSEC-3DES-ADSL",
		"k3p": "SERVICE-PROVIDER-SECURED-SHELL-56",
		"k3pv": "SERVICE-PROVIDER-SECURED-SHELL-3DES",
		"k4p": "SERVICE-PROVIDER-SECURED-SHELL-3DES",
		"k4p10": "SERVICE-PROVIDER-SECURED-SHELL-3DES",
		"k4pv": "SERVICE-PROVIDER-SECURED-SHELL-56",
		"k4u2p10": "LAWFUL-INTERCEPT-SECURED-SHELL-3DES",
		"k8boot": "BOOT",
		"k8nosy6": "IP-IPX-FW-PLUS-IPSEC-56",
		"k8o3sv3y": "IP-VOICE-FW-IDS-PLUS-IPSEC",
		"k8o3sv3y7": "IP-ADSL-VOICE-FW-IDS-PLUS-IPSEC-56",
		"k8o3sv8y7": "IP-ADSL-VOX-FW-IDS-PLUS-IPSEC-56",
		"k8o3sy": "IP-FW-IDS-PLUS-IPSEC-56",
		"k8o3sy7": "IP-ADSL-FW-IDS-PLUS-IPSEC-56",
		"k8o3v9y5": "VOICE-H323-MGCP-SIP-FW-IPSEC56",
		"k8osy": "IP-FW-PLUS-IPSEC-56",
		"k8osy6": "IP-FW-PLUS-IPSEC-56",
		"k8p11u2": "LAWFUL-INTERCEPT-SECURED-SHELL-DES",
		"k8p4": "SERVICE-PROVIDER-IPSEC-56",
		"k8p6u2": "DOCSIS-BPI-LAWFUL-INTERCEPT",
		"k8p9": "SERVICE-PROVIDER-PLUS-IPSEC-3DES",
		"k8pu2": "DOCSIS-2-WAY-BPI-LAWFUL-INTERCEPT",
		"k8sv3y": "IP-VOICE-PLUS-IPSEC-56",
		"k8sv3y7": "IP-ADSL-VOICE-PLUS-IPSEC-56",
		"k8sv8y7": "IP-ADSL-VOX-PLUS-IPSEC-56",
		"k8sy": "IP-PLUS-IPSEC-56",
		"k8sy7": "IP-ADSL-PLUS-IPSEC-56",
		"k91p": "SERVICE-PROVIDER-SECURE-SHELL-3DES",
		"k91p11": "UP-TO-8K-SUBSCRIBERS-WITH-3DES",
		"k91p11u2": "UP-TO-8K-SUBSCRIBERS-WITH-LAWFUL-INTERCEPT-3DES",
		"k91pv": "SERVICE-PROVIDER-SECURED-SHELL-3DES",
		"k9nosy6": "IP-IPX-FW-PLUS-IPSEC-3DES",
		"k9o3s8y6": "IP-FW-PLUS-ISDN-DIAL-BACKUP-3DES-VPN",
		"k9o3sv3y": "IP-FW-VOICE-PLUS-IPSEC-3DES",
		"k9o3sv3y7": "IP-ADSL-VOICE-FW-IDS-PLUS-IPSEC-3DES",
		"k9o3sv8y7": "IP-ADSL-VOX-FW-IDS-PLUS-IPSEC-3DES",
		"k9o3sv9y5": "PERFORMANCE-SMALL-OFFICE-VOICE-FW-IPSEC-3DES",
		"k9o3sy": "BASIC-IP-FIREWALL-2-3DES-PLUS",
		"k9o3sy6": "IP-FW-PLUS-3DES",
		"k9o3sy7": "IP-ADSL-FW-IDS-PLUS-IPSEC-3DES",
		"k9o3y6": "IP-FW-3DES",
		"k9osv6y6": "IP-FW-VOICE-PLUS-3DES",
		"k9osy6": "IP-FW-PLUS-IPSEC-3DES",
		"k9oy1": "IP-FW-3DES",
		"k9oy6": "IP-FW-3DES",
		"k9p": "SERVICE-PROVIDER-SSH-3DES",
		"k9p11": "SERVICE-PROVIDER-SECURED-SHELL-3DES",
		"k9p11u2": "LAWFUL-INTERCEPT-SECURED-SHELL-3DES",
		"k9p12": "SERVICE-PROVIDER-WITH-CRYPTO",
		"k9p6u2": "DOCSIS-3DES-LAWFUL-INTERCEPT",
		"k9p9": "SERVICE-PROVIDER-PLUS-IPSEC-3DES",
		"k9p9u2": "SERVICE-PROVIDER-PLUS-IPSEC-3DES-LAWFUL-INTERCEPT",
		"k9pu2": "DOCSIS-3DES-LAWFUL-INTERCEPT",
		"k9sv3y": "BASIC-IP-VOICE-3DES-PLUS",
		"k9sv3y7": "IP-ADSL-VOICE-PLUS-IPSEC-3DES",
		"k9sv8y7": "IP-ADSL-VOX-PLUS-IPSEC-3DES",
		"k9sy": "BASIC-IP-3DES-PLUS",
		"k9sy7": "IP-ADSL-PLUS-IPSEC-3DES",
		"k9w7": "WIRELESS-LAN-AUTONOMOUS",
		"k9w8": "WIRELESS-LAN-LIGHTWEIGHT-FULL",
		"kboot": "BOOT",
		"kickstart": "KICKSTART",
		"kickstart-npe": "KICKSTART-NPE",
		"kubernetes": "KUBERNETES",
		"kvm": "KVM",
		"l2l3cvt": "L2-L3-CONVERSION",
		"lanbase": "LAN-BASE",
		"lanbasek9": "LAN-BASE-SSH",
		"lanbasek9_en": "LAN-BASE-SSH-ENGLISH",
		"lanbaselmk9": "LAN-BASE-SSH-WITH-EXPRESS-SETUP",
		"lanbaselmk9_en": "LAN-BASE-SSH-WITH-EXPRESS-SETUP-ENGLISH",
		"lanlite": "LAN-LITE",
		"lanlitek9": "LAN-LITE-SSH",
		"launcher": "LAUNCHER",
		"lc": "ATM-LINE-CARD",
		"lfbff": "ASA-FIREPOWER",
		"linux": "LINUX",
		"linuxbare": "LINUX",
		"log4j": "LOG4SHELL-FIXES",
		"logagent": "LOG-AGENT",
		"lsprel": "GeoDB-SRU-VDB/Lightweight-Security-Package",
		"m": "ATM",
		"m": "ATM-OC3-LANE",
		"macintosh": "MAC",
		"macos": "MACOSX",
		"macosxi386": "MACOSX-i386",
		"macosxpowerpc": "MACOSX-PowerPC",
		"mboot": "BOOT",
		"mcp": "MANAGEMENT-CENTER-FOR-PERFORMANCE",
		"metroaccess": "METRO-ACCESS-NO-CRYPTO",
		"metroaccessk9": "METRO-ACCESS",
		"metrobase": "METRO-BASE-NO-CRYPTO",
		"metrobasek9": "METRO-BASE",
		"metroipaccess": "METRO-IP-ACCESS-NO-CRYPTO",
		"metroipaccessk9": "METRO-IP-ACCESS",
		"mgmtctr": "MANAGEMENT-CENTER",
		"mibs": "MIBS",
		"mica-modem": "NEXTPORT-MODEM-FIRMWARE",
		"migrate_to_eXR": "64BIT-MIGRATION",
		"migration": "MIGRATION",
		"mini": "MINI",
		"mini-x64": "MINI-X64",
		"mp": "MAINTENANCE-PARTITION",
		"mpatch": "MODULARITY-PATCH",
		"mso": "MULTI-SITE-ORCHESTRATOR",
		"n9kacim": "NEXUS-9000-ACI-MODE",
		"nacagent": "NAC-AGENT",
		"nbar": "NBAR2",
		"ngfw": "NGFW",
		"ngfwv": "NGFWV",
		"no3sv3y": "IP-IPX-VOICE-FW-IDS-PLUS",
		"no3sv3y7": "IP-ADSL-IPX-VOICE-FW-IDS-PLUS",
		"no3sv8y7": "IP-ADSL-IPX-VOX-FW-IDS-PLUS",
		"no3sy": "IP-IPX-FW-IDS-PLUS",
		"no3sy7": "IP-ADSL-IPX-FW-IDS-PLUS",
		"nosv3y": "IP-IPX-FW-VOICE-PLUS",
		"nosy": "IP-IPX-FW-PLUS",
		"nosy656i": "IP-IPX-FW-PLUS-IPSEC-56",
		"np": "NEXTPORT-FIRMWARE",
		"nqy": "IP-IPX-ASYNC",
		"nr2sy": "IP-IPX-IBM-PLUS",
		"nr2sy40": "IP-IPX-IBM-PLUS-40",
		"nr2sy56": "IP-IPX-IBM-PLUS-56",
		"nr2y": "IP-IPX-IBM",
		"nsy": "IP-IPX-PLUS",
		"nsy40": "IP-IPX-PLUS-40",
		"nsy56": "IP-IPX-PLUS-56",
		"nsy6": "IP-IPX-PLUS",
		"nvm": "NETWORK-VISIBILITY-MODULE",
		"nvsat": "NVSATELLITE",
		"ny": "IP-IPX",
		"o3sv3y": "IP-VOICE-FW-IDS-PLUS",
		"o3sv3y56i": "IP-FW-VOICE-PLUS-IPSEC-56",
		"o3sv3y7": "IP-ADSL-VOICE-FW-IDS-PLUS",
		"o3sv3y756i": "IP-VOICE-FW-IDS-PLUS-IPSEC-56-ADSL",
		"o3sv8y7": "IP-ADSL-VOX-FW-IDS-PLUS",
		"o3sy56i": "IP-FW-IDS-PLUS-IPSEC-3DES",
		"o3sy6": "IP-FW-PLUS",
		"o3sy756i": "IP-FW-PLUS-IPSEC-56-ADSL",
		"o3y": "IP-FW-IDS",
		"oac": "OPEN-AGENT-CONTAINER",
		"occtoacl": "OCC-TO-ACL-CONVERTER",
		"osv3y": "IP-FW-VOICE-PLUS",
		"osv3y56i": "IP-FW-VOICE-PLUS-IPSEC-56",
		"osy56i": "IP-FW-PLUS-IPSEC-56",
		"osy6": "IP-FW-PLUS",
		"osy656i": "IP-FW-PLUS-IPSEC-56",
		"ov6y6": "IP-FW-VOICE",
		"oy": "IP-FW",
		"oy1": "IP-FW",
		"oy6": "IP-FW",
		"p": "SERVICE-PROVIDER",
		"p10": "EDGE-SERVICES-ROUTER",
		"p11": "EDGE-SERVICES-ROUTER",
		"p11u2": "UP-TO-8K-SUBSCRIBERS-WITH-LAWFUL-INTERCEPT",
		"p12": "SERVICE-PROVIDER",
		"p4": "SERVICE-PROVIDER",
		"p456i": "SERVICE-PROVIDER-ALTERNATE",
		"p7": "SERVICE-PROVIDER-WITH-PT-TARP",
		"p9": "SERVICE-PROVIDER-PLUS",
		"patch": "PATCH",
		"pdm": "PIX-DEVICE-MANAGER",
		"pixpasswordrecovery": "PASSWORD-RECOVERY",
		"PIXtoASA": "PIX-TO-ASA",
		"pk2o3sv": "SERVICE-PROVIDER-WITH-FW-AND-VIP-3DES",
		"pk2s": "SERVICE-PROVIDER-SSH-3DES-LAN-ONLY",
		"pk2sv": "SERVICE-PROVIDER-WITH-VIP-3DES",
		"pk9s": "IP-SSH-3DES-LAN-ONLY",
		"pk9sv": "IP-SSH-3DES",
		"pk9u2": "SERVICE-PROVIDER-IPSEC-3DES-LAWFUL-INTERCEPT",
		"po3sv": "SERVICE-PROVIDER-WITH-FW-AND-VIP",
		"poap": "POAP",
		"poap_ng": "POAP-NG",
		"profileeditor": "PROFILE-EDITOR",
		"ps": "SERVICE-PROVIDER-LAN-ONLY",
		"psv": "SERVICE-PROVIDER-WITH-VIP",
		"pv": "SERVICE-PROVIDER",
		"qed": "DEVICE-ENABLER",
		"qy": "IP-ASYNC",
		"rboot": "BOOT",
		"rcv": "RECOVERY",
		"rcvk9w8": "WIRELESS-LAN-LIGHTWEIGHT-RECOVERY",
		"restapi": "REST-API",
		"rme": "RESOURCE-MANAGER-ESSENTIALS",
		"rommon": "ROMMON",
		"rr": "ROUTE-REFLECTOR",
		"rrvga": "ROUTE-REFLECTOR-VGA",
		"s1": "SUP-1",
		"s1ek9": "SUP-1/BASE",
		"s2": "SUP-2",
		"s2ek9": "SUP-2",
		"s3": "SUP-3",
		"s3ek9": "SUP-3",
		"s4ek9": "SUP-4",
		"s5ek9": "SUP-5",
		"san-client": "SAN-CLIENT",
		"sccp": "SCCP",
		"scu": "SERVER-CONFIGURATION-UTILITY",
		"sfgeodb": "GeoDB-SRU-VDB/Geodb",
		"sfrules": "GeoDB-SRU-VDB/Rules",
		"sfvdb": "GeoDB-SRU-VDB/VDB",
		"signatures": "SIGNATURES",
		"silent-installer": "SILENT-INSTALLER",
		"sip": "SIP",
		"sipspawmak9": "WEBEX-NODE",
		"sm10g": "10-GIG-MODULE",
		"smu": "SMU",
		"sns35xx": "SNS-35xx",
		"sns36xx": "SNS-36xx",
		"sns37xx": "SNS-37xx",
		"solaris": "SOLARIS",
		"sourcefiredev": "SOURCEFIRE-8350",
		"sp1": "SERVICE-PACK-1",
		"sp10": "SERVICE-PACK-10",
		"sp11": "SERVICE-PACK-11",
		"sp12": "SERVICE-PACK-12",
		"sp2": "SERVICE-PACK-2",
		"sp3": "SERVICE-PACK-3",
		"sp4": "SERVICE-PACK-4",
		"sp5": "SERVICE-PACK-5",
		"sp6": "SERVICE-PACK-6",
		"sp7": "SERVICE-PACK-7",
		"sp8": "SERVICE-PACK-8",
		"sp9": "SERVICE-PACK-9",
		"specialbuild": "SPECIAL-BUILDS",
		"specialbuildfwupgrade": "SPECIAL-BUILDS-FIRMWARE-UPGRADE",
		"specialbuildlisp": "SPECIAL-BUILDS-LISP",
		"sprom": "SPROM-EPLD",
		"spservicesk9": "SERVICE-PROVIDER",
		"spw": "SUPPLICANT-PROVISIONING-WIZARD",
		"ssi": "STORAGE-SERVICE-INTERFACE",
		"stripped-firmware": "STRIPPED-FIRMWARE",
		"struts": "STRUTS-FIX",
		"sup": "SUP-1",
		"sup2": "SUP-2",
		"sup2cv": "SUP-2/CISCOVIEW",
		"sup2cvk8": "SUP-2/CISCOVIEW",
		"sup2cvk9": "SUP-2/CISCOVIEW-AND-SSH",
		"sup2k8": "SUP-2",
		"sup2k9": "SUP-2/SSH",
		"sup3": "SUP-3",
		"sup32pfc3cvk8": "SUP-32/CISCOVIEW",
		"sup32pfc3cvk9": "SUP-32/CISCOVIEW-AND-SSH",
		"sup32pfc3k8": "SUP-32/BASE",
		"sup32pfc3k9": "SUP-32/SSH",
		"sup3cv": "SUP-3/CISCOVIEW",
		"sup3cvk9": "SUP-3/CISCOVIEW-AND-SSH",
		"sup3k9": "SUP-3/SSH",
		"sup720cvk8": "SUP-720/CISCOVIEW",
		"sup720cvk9": "SUP-720/CISCOVIEW-AND-SSH",
		"sup720k8": "SUP-720/BASE",
		"sup720k9": "SUP-720/SSH",
		"sup8m": "SUP-1-8M",
		"supcv": "SUP-1/CISCOVIEW",
		"supcvk8": "SUP-1/CISCOVIEW",
		"supcvk9": "SUP-1/CISCOVIEW-AND-SSH",
		"supg": "SUP-3/BASE",
		"supgk9": "SUP-3/SSH",
		"supk8": "SUP-1",
		"supk9": "SUP-1/SSH",
		"supplicantpw": "SUPPLICANT-PROVISIONING-WIZARD",
		"sv12y10": "REDUCED-IP-ANALOG-VOICE-PLUS",
		"sv3y": "IP-VOICE-PLUS",
		"sv3y10": "REDUCED-IP-VOICE-PLUS",
		"sv3y40": "IP-VOICE-PLUS-IPSEC-40",
		"sv3y56": "IP-VOICE-PLUS-IPSEC-56",
		"sv3y56i": "IP-VOICE-PLUS-IPSEC-56",
		"sv3y7": "IP-ADSL-VOICE-PLUS",
		"sv3y7": "IP-VOICE-PLUS-ADSL",
		"sv3y756i": "IP-VOICE-PLUS-IPSEC-56-ADSL",
		"sv6y6": "IP-VOICE-PLUS",
		"sv8y": "IP-VOX-PLUS",
		"sv8y7": "IP-ADSL-VOX-PLUS",
		"sy": "IP-PLUS",
		"sy40": "IP-PLUS-40",
		"sy56": "IP-PLUS-56",
		"sy56i": "IP-PLUS-IPSEC-56",
		"sy6": "IP-PLUS",
		"sy7": "IP-ADSL-PLUS",
		"sy756i": "IP-PLUS-IPSEC-56-ADSL",
		"system": "SYSTEM",
		"system-npe": "SYSTEM-NPE",
		"telco": "TELCO-FEATURE-SET",
		"telcoent": "TELCO-PLUS-FEATURE-SET",
		"telcoentk9": "TELCO-PLUS-FEATURE-SET-IPSEC-3DES",
		"templates": "TEMPLATES",
		"thirdparty": "THIRD-PARTY-UTILS",
		"transforms": "TRANSFORMS",
		"translations": "TRANSLATIONS",
		"turboboot": "TURBO-BOOT",
		"u2p10": "LAWFUL-INTERCEPT",
		"ucmk9": "IOS-XE-SD-WAN",
		"ucsbundle": "BUNDLE",
		"ucslinux": "LINUX",
		"universal": "UNIVERSAL",
		"universal": "UNIVERSAL-NO-CRYPTO",
		"universal_cloud": "UNIVERSAL-CLOUD",
		"universal_cloud_esxi": "UNIVERSAL-CLOUD-ESXI",
		"universal_cloud_nfvis": "UNIVERSAL-CLOUD-NFVIS",
		"universal_kvm": "UNIVERSAL-KVM",
		"universal_lite": "UNIVERSAL-LITE-NO-CRYPTO",
		"universal_loud_kvm": "UNIVERSAL-CLOUD-KVM",
		"universalk9": "UNIVERSAL",
		"universalk9_en": "UNIVERSAL-ENGLISH",
		"universalk9_ias": "UNIVERSAL",
		"universalk9_ias_npe": "UNIVERSAL-NPE",
		"universalk9_iox": "UNIVERSAL-IOX",
		"universalk9_iox_npe": "UNIVERSAL-IOX-NPE",
		"universalk9_kvm": "UNIVERSAL-KVM",
		"universalk9_lite": "UNIVERSAL-LITE",
		"universalk9_noli": "UNIVERSAL-NO-LAWFUL-INTERCEPT",
		"universalk9_npe": "UNIVERSAL-NPE",
		"universalk9_npe_noli": "UNIVERSAL-NPE-NO-LAWFUL-INTERCEPT",
		"universalk9_wlc": "UNIVERSAL-WIRELESS",
		"universalk9azn": "UNIVERSAL-AZURE-CLOUD",
		"universalk9ldpe": "UNIVERSAL-NPE",
		"universalk9milplr": "UNIVERSAL-MILITARY",
		"universalk9npe": "UNIVERSAL-NPE",
		"universalk9npe_lite": "UNIVERSAL-LITE-NPE",
		"upgrade": "UPGRADE",
		"urtbundle": "UPGRADE-READINESS-TOOL",
		"usb_boot": "USB-BOOT",
		"utilsbseries": "B-SERIES/UTILS",
		"utilscseries": "C-SERIES/UTILS",
		"v6y6": "IP-VOICE",
		"va": "VIRTUAL-APPLIANCE",
		"vchtmlplug": "VCENTER-HTML-PLUGIN",
		"vcw-vfc-mz": "VCWare",
		"virtualapp": "VIRTUAL-APPLIANCE",
		"virtual-ovf": "OVF-DEFINITION-FILES",
		"vmware": "VMWARE",
		"vpnapi": "VPNAPI",
		"vxworks": "VXWorks",
		"vxworkstoios": "VXWorks-to-IOS-CONVERSION-TOOL",
		"w1is": "WIMAX-ASNGW-1.0-CRYPTO",
		"w3": "DISTRIBUTED-DIRECTOR-SYSTEM-SOFTWARE",
		"wboot": "BOOT",
		"webagent": "WEB-AGENT",
		"webauth": "WEBAUTH-BUNDLE",
		"websecurity": "WEB-SECURITY",
		"websecurity": "WEB-SECURITY-APPLIANCE",
		"wi": "ATM",
		"winarm64": "WINDOWS-ARM64",
		"wince": "WINDOWS-CE",
		"windows": "WINDOWS",
		"witness": "WITNESS-NODE",
		"WKGBDG": "WORKGROUP-BRIDGE",
		"wl": "ATM-WORKGROUP-LANE",
		"wp": "NSP",
		"wpk2": "ATM-LAYER-3-SSH-3DES",
		"WRLBDG": "WIRELESS-BRIDGE",
		"wt": "ATM-WORKGROUP-TRAFFIC-SHAPING",
		"xsd": "XML-SCHEMA",
		"xy": "UNKNOWN-FEATURE-SET",
		"y": "IP",
		"y1": "IP",
		"y2": "IP-OSPF-PIM",
		"y6": "IP",
		"y7": "IP-ADSL"
	}
	return imagecode_to_subdirectory.get(imagecode, "UNKNOWN")

def product (prodcode):
	if prodcode == "apicem":
		prodname = "NETWORK-MANAGEMENT/APIC-EM"
	elif prodcode == "cspc":
		prodname = "NETWORK-MANAGEMENT/COMMON-SERVICES-PLATFORM-COLLECTOR"
	elif prodcode == "ccp":
		prodname = "NETWORK-MANAGEMENT/CONFIGURATION-PROFESSIONAL"
	elif prodcode == "ccpc":
		prodname = "NETWORK-MANAGEMENT/CONFIGURATION-PROFESSIONAL-CATALYST"
	elif prodcode == "cpi":
		prodname = "NETWORK-MANAGEMENT/CISCO-PRIME-INFRASTRUCTURE"
	elif prodcode == "dnac":
		prodname = "NETWORK-MANAGEMENT/DNA-CENTER"
	elif prodcode == "ttam":
		prodname = "NETWORK-MANAGEMENT/DNA-CENTER-TRAFFIC"
	elif prodcode == "cna":
		prodname = "NETWORK-MANAGEMENT/NETWORK-ASSISTANT"
	elif prodcode == "SSM_On-Prem":
		prodname = "NETWORK-MANAGEMENT/SMART LICENSE ON-PREM"
	elif prodcode == "ntwkmgmt":
		prodname = "NETWORK-MANAGEMENT"
	elif prodcode == "cworks":
		prodname = "NETWORK-MANAGEMENT/CiscoWorks"
	elif prodcode == "c1100tg":
		prodname = "NETWORK-MANAGEMENT/TERMINAL-SERVICES-GATEWAY"
	elif prodcode == "perfigocca":
		prodname = "NETWORK-MANAGEMENT/CISCO-CLEAN-ACCESS"
	elif prodcode == "cml":
		prodname = "NETWORK-MANAGEMENT/MODELING-LABS"
	elif prodcode == "cmlf":
		prodname = "NETWORK-MANAGEMENT/MODELING-LABS-FREE"
	elif prodcode == "refplat":
		prodname = "NETWORK-MANAGEMENT/MODELING-LABS-REFERENCE-PLATFORM"
	elif prodcode == "cimcs":
		prodname = "SERVERS/CIMC-SUPERVISOR"
	elif prodcode == "routers":
		prodname = "ROUTERS"
	elif prodcode == "ir1800":
		prodname = "ROUTERS/INDUSTRIAL/IR18XX"
	elif prodcode == "ir8100":
		prodname = "ROUTERS/INDUSTRIAL/IR8100"
	elif prodcode == "ir8340":
		prodname = "ROUTERS/INDUSTRIAL/IR8340"
	elif prodcode == "ons15530":
		prodname = "ROUTERS/OPTICAL/ONS-15530"
	elif prodcode == "ons15540":
		prodname = "ROUTERS/OPTICAL/ONS-15540"
	elif prodcode == "asr1000":
		prodname = "ROUTERS/ASR/ASR-1000"
	elif prodcode == "isrg3moduleslte":
		prodname = "ROUTERS/ISRG3/MODULES/LTE"
	elif prodcode == "iosxeissumatrix":
		prodname = "ROUTERS/IOS-XE-ISSU-MATRIX"
	elif prodcode == "iou":
		prodname = "ROUTERS/IOU"
	elif prodcode == "asr1000rp1":
		prodname = "ROUTERS/ASR/ASR-1000-RP1"
	elif prodcode == "asr1000rp2":
		prodname = "ROUTERS/ASR/ASR-1000-RP2"
	elif prodcode == "asr1000rpx86":
		prodname = "ROUTERS/ASR/ASR-1000-RP3"
	elif prodcode == "asr1000hx":
		prodname = "ROUTERS/ASR/ASR-1000HX"
	elif prodcode == "asr1001":
		prodname = "ROUTERS/ASR/ASR-1001"
	elif prodcode == "asr1001x":
		prodname = "ROUTERS/ASR/ASR-1001X"
	elif prodcode == "asr1002":
		prodname = "ROUTERS/ASR/ASR-1002"
	elif prodcode == "asr1002x":
		prodname = "ROUTERS/ASR/ASR-1002X"
	elif prodcode == "asr1002hx":
		prodname = "ROUTERS/ASR/ASR-1002HX"
	elif prodcode == "asr900":
		prodname = "ROUTERS/ASR/ASR-900"
	elif prodcode == "asr9k":
		prodname = "ROUTERS/ASR/ASR-9000"
	elif prodcode == "asr900rsp1":
		prodname = "ROUTERS/ASR/ASR-900-RSP1"
	elif prodcode == "asr900rsp2":
		prodname = "ROUTERS/ASR/ASR-900-RSP2"
	elif prodcode == "asr900rsp3":
		prodname = "ROUTERS/ASR/ASR-900-RSP3"
	elif prodcode == "asr901":
		prodname = "ROUTERS/ASR/ASR-901"
	elif prodcode == "asr901rsp1":
		prodname = "ROUTERS/ASR/ASR-901-RSP1"
	elif prodcode == "asr901rsp2":
		prodname = "ROUTERS/ASR/ASR-901-RSP2"
	elif prodcode == "asr901_sat":
		prodname = "ROUTERS/ASR/ASR-901-SAT"
	elif prodcode == "asr901sec":
		prodname = "ROUTERS/ASR/ASR-901-SEC"
	elif prodcode == "asr903":
		prodname = "ROUTERS/ASR/ASR-903"
	elif prodcode == "asr903rsp1":
		prodname = "ROUTERS/ASR/ASR-903-RSP1"
	elif prodcode == "asr903rsp2":
		prodname = "ROUTERS/ASR/ASR-903-RSP2"
	elif prodcode == "asr920":
		prodname = "ROUTERS/ASR/ASR-920"
	elif prodcode == "asr920igp":
		prodname = "ROUTERS/ASR/ASR-920IGP"
	elif prodcode == "urm":
		prodname = "ROUTERS/ATM/IGX-8400"
	elif prodcode == "rpm":
		prodname = "ROUTERS/ATM/MGX-8850"
	elif prodcode == "rpmxf":
		prodname = "ROUTERS/ATM/MGX-8850"
	elif prodcode == "sdwan":
		prodname = "ROUTERS/SD-WAN"
	elif prodcode == "c600":
		prodname = "ROUTERS/BRANCH/600"
	elif prodcode == "c800":
		prodname = "ROUTERS/BRANCH/800"
	elif prodcode == "c805":
		prodname = "ROUTERS/BRANCH/805"
	elif prodcode == "c806":
		prodname = "ROUTERS/BRANCH/806"
	elif prodcode == "c815":
		prodname = "ROUTERS/BRANCH/815"
	elif prodcode == "c820":
		prodname = "ROUTERS/BRANCH/820"
	elif prodcode == "c827v":
		prodname = "ROUTERS/BRANCH/827"
	elif prodcode == "c828":
		prodname = "ROUTERS/BRANCH/828"
	elif prodcode == "c831":
		prodname = "ROUTERS/BRANCH/831"
	elif prodcode == "c836":
		prodname = "ROUTERS/BRANCH/836"
	elif prodcode == "c837":
		prodname = "ROUTERS/BRANCH/837"
	elif prodcode == "c1004":
		prodname = "ROUTERS/BRANCH/1004"
	elif prodcode == "c1005":
		prodname = "ROUTERS/BRANCH/1005"
	elif prodcode == "cpa1005":
		prodname = "ROUTERS/BRANCH/1005"
	elif prodcode == "c1400":
		prodname = "ROUTERS/BRANCH/1400"
	elif prodcode == "c1600":
		prodname = "ROUTERS/BRANCH/1600"
	elif prodcode == "c1700":
		prodname = "ROUTERS/BRANCH/1700"
	elif prodcode == "c1710":
		prodname = "ROUTERS/BRANCH/1710"
	elif prodcode == "c2500":
		prodname = "ROUTERS/BRANCH/2500"
	elif prodcode == "igs":
		prodname = "ROUTERS/BRANCH/2500"
	elif prodcode == "c25fx":
		prodname = "ROUTERS/BRANCH/2500"
	elif prodcode == "c2511":
		prodname = "ROUTERS/BRANCH/2500"
	elif prodcode == "c2600":
		prodname = "ROUTERS/BRANCH/2600"
	elif prodcode == "c2611":
		prodname = "ROUTERS/BRANCH/2600"
	elif prodcode == "c2691":
		prodname = "ROUTERS/BRANCH/2691"
	elif prodcode == "c3620":
		prodname = "ROUTERS/BRANCH/3620"
	elif prodcode == "c3631":
		prodname = "ROUTERS/BRANCH/3631"
	elif prodcode == "c3640":
		prodname = "ROUTERS/BRANCH/3640"
	elif prodcode == "c3660":
		prodname = "ROUTERS/BRANCH/3660"
	elif prodcode == "c3725":
		prodname = "ROUTERS/BRANCH/3725"
	elif prodcode == "c3745":
		prodname = "ROUTERS/BRANCH/3745"
	elif prodcode == "c4000":
		prodname = "ROUTERS/BRANCH/4000"
	elif prodcode == "c4500":
		prodname = "ROUTERS/BRANCH/4700M"
	elif prodcode == "mc3810":
		prodname = "ROUTERS/BRANCH/MC-3810"
	elif prodcode == "branchmodules":
		prodname = "ROUTERS/BRANCH/MODULES"
	elif prodcode == "ni2":
		prodname = "ROUTERS/BROADBAND/NI-2"
	elif prodcode == "rfgw":
		prodname = "ROUTERS/BROADBAND/RF-Gateway 1"
	elif prodcode == "rfgwk10":
		prodname = "ROUTERS/BROADBAND/RF-Gateway 10"
	elif prodcode == "sb101":
		prodname = "ROUTERS/BROADBAND/SB-101"
	elif prodcode == "sb107":
		prodname = "ROUTERS/BROADBAND/SB-107"
	elif prodcode == "ubr920":
		prodname = "ROUTERS/BROADBAND/UBR-920"
	elif prodcode == "ubr925":
		prodname = "ROUTERS/BROADBAND/UBR-925"
	elif prodcode == "ubr10k":
		prodname = "ROUTERS/BROADBAND/UBR-10000/PRE1"
	elif prodcode == "ubr10k2":
		prodname = "ROUTERS/BROADBAND/UBR-10000/PRE2"
	elif prodcode == "ubr10k3":
		prodname = "ROUTERS/BROADBAND/UBR-10000/PRE3"
	elif prodcode == "ubr10k4":
		prodname = "ROUTERS/BROADBAND/UBR-10000/PRE4"
	elif prodcode == "ubr10k5":
		prodname = "ROUTERS/BROADBAND/UBR-10000/PRE5"
	elif prodcode == "ubr7100":
		prodname = "ROUTERS/BROADBAND/UBR-7100"
	elif prodcode == "ubr7200":
		prodname = "ROUTERS/BROADBAND/UBR-7200/NPEG1"
	elif prodcode == "ubr7200p":
		prodname = "ROUTERS/BROADBAND/UBR-7200/NPEG2"
	elif prodcode == "cva120":
		prodname = "ROUTERS/CABLE/CVA-120"
	elif prodcode == "cva120cvc":
		prodname = "ROUTERS/CABLE/CVA-120"
	elif prodcode == "esr6300":
		prodname = "ROUTERS/EMBEDDED/ESR-6300"
	elif prodcode == "c5915":
		prodname = "ROUTERS/EMBEDDED/5915"
	elif prodcode == "c5921i86":
		prodname = "ROUTERS/EMBEDDED/5921"
	elif prodcode == "c5921i86v":
		prodname = "ROUTERS/EMBEDDED/5921"
	elif prodcode == "c5940":
		prodname = "ROUTERS/EMBEDDED/5940"
	elif prodcode == "c5930":
		prodname = "ROUTERS/EMBEDDED/5930"
	elif prodcode == "ie9k":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/CATALYST-9300-INDUSTRIAL"
	elif prodcode == "cgr2010":
		prodname = "ROUTERS/GRID/CGR-2010"
	elif prodcode == "soho70":
		prodname = "ROUTERS/HOME-SMALL-BUSINESS/SOHO-70"
	elif prodcode == "soho71":
		prodname = "ROUTERS/HOME-SMALL-BUSINESS/SOHO-71"
	elif prodcode == "soho78":
		prodname = "ROUTERS/HOME-SMALL-BUSINESS/SOHO-78"
	elif prodcode == "soho91":
		prodname = "ROUTERS/HOME-SMALL-BUSINESS/SOHO-91"
	elif prodcode == "soho97":
		prodname = "ROUTERS/HOME-SMALL-BUSINESS/SOHO-97"
	elif prodcode == "igs":
		prodname = "ROUTERS/IGS"
	elif prodcode == "iosxe-sd-avc":
		prodname = "ROUTERS/IOSXE-AVC"
	elif prodcode == "iosxe-remote-mgmt":
		prodname = "ROUTERS/IOSXE-REMOTE-MGMT"
	elif prodcode == "c180x":
		prodname = "ROUTERS/ISRG1/1800"
	elif prodcode == "c1805":
		prodname = "ROUTERS/ISRG1/1805"
	elif prodcode == "c181x":
		prodname = "ROUTERS/ISRG1/1810"
	elif prodcode == "c1841":
		prodname = "ROUTERS/ISRG1/1841"
	elif prodcode == "c1841c":
		prodname = "ROUTERS/ISRG1/1841-CHINA"
	elif prodcode == "c1841ve":
		prodname = "ROUTERS/ISRG1/1841-VE"
	elif prodcode == "c1861":
		prodname = "ROUTERS/ISRG1/1861"
	elif prodcode == "c2800nm":
		prodname = "ROUTERS/ISRG1/2800nm"
	elif prodcode == "c2800nmc":
		prodname = "ROUTERS/ISRG1/2800nm-CHINA"
	elif prodcode == "c2800nmve":
		prodname = "ROUTERS/ISRG1/2800nmve"
	elif prodcode == "c2801":
		prodname = "ROUTERS/ISRG1/2801"
	elif prodcode == "c2801c":
		prodname = "ROUTERS/ISRG1/2801-CHINA"
	elif prodcode == "c3825":
		prodname = "ROUTERS/ISRG1/3825"
	elif prodcode == "c3825c":
		prodname = "ROUTERS/ISRG1/3825-CHINA"
	elif prodcode == "c3825nv":
		prodname = "ROUTERS/ISRG1/3825-NO-VPN"
	elif prodcode == "c3845":
		prodname = "ROUTERS/ISRG1/3845"
	elif prodcode == "c3845c":
		prodname = "ROUTERS/ISRG1/3845-CHINA"
	elif prodcode == "c3845nv":
		prodname = "ROUTERS/ISRG1/3845-NO-VPN"
	elif prodcode == "c850":
		prodname = "ROUTERS/ISRG1/850"
	elif prodcode == "c860":
		prodname = "ROUTERS/ISRG1/860"
	elif prodcode == "c870":
		prodname = "ROUTERS/ISRG1/870"
	elif prodcode == "c871":
		prodname = "ROUTERS/ISRG1/871"
	elif prodcode == "c890":
		prodname = "ROUTERS/ISRG1/890"
	elif prodcode == "ISRG1GENERIC":
		prodname = "ROUTERS/ISRG1/MODULES"
	elif prodcode == "c1900":
		prodname = "ROUTERS/ISRG2/1900"
	elif prodcode == "c1900-2900":
		prodname = "ROUTERS/ISRG2/1900-2900"
	elif prodcode == "c1900c":
		prodname = "ROUTERS/ISRG2/1900-CHINA"
	elif prodcode == "c2900":
		prodname = "ROUTERS/ISRG2/2900"
	elif prodcode == "c2911a":
		prodname = "ROUTERS/ISRG2/2911a"
	elif prodcode == "c2951":
		prodname = "ROUTERS/ISRG2/2951"
	elif prodcode == "c3900":
		prodname = "ROUTERS/ISRG2/3900"
	elif prodcode == "c3900e":
		prodname = "ROUTERS/ISRG2/3900E"
	elif prodcode == "c800m":
		prodname = "ROUTERS/ISRG2/800m"
	elif prodcode == "c800j":
		prodname = "ROUTERS/ISRG2/800J"
	elif prodcode == "c860vae":
		prodname = "ROUTERS/ISRG2/860-VAE"
	elif prodcode == "c860vae2":
		prodname = "ROUTERS/ISRG2/860-VAE2"
	elif prodcode == "c860vaej":
		prodname = "ROUTERS/ISRG2/860-VAEJ"
	elif prodcode == "c860vaew":
		prodname = "ROUTERS/ISRG2/860-VAEW"
	elif prodcode == "c880data":
		prodname = "ROUTERS/ISRG2/880"
	elif prodcode == "c880voice":
		prodname = "ROUTERS/ISRG2/880-CUBE"
	elif prodcode == "c890s":
		prodname = "ROUTERS/ISRG2/890"
	elif prodcode == "c900":
		prodname = "ROUTERS/ISRG2/900"
	elif prodcode == "ISRG2GENERIC":
		prodname = "ROUTERS/ISRG2/MODULES"
	elif prodcode == "c800g2":
		prodname = "ROUTERS/ISRG2/800"
	elif prodcode == "c800g3":
		prodname = "ROUTERS/ISRG3/800"
	elif prodcode == "ir1101":
		prodname = "ROUTERS/INDUSTRIAL/IR-1101"
	elif prodcode == "ir800":
		prodname = "ROUTERS/INDUSTRIAL/IR-800"
	elif prodcode == "c1000router":
		prodname = "ROUTERS/BRANCH/1000"
	elif prodcode == "c1100router":
		prodname = "ROUTERS/ISRG3/ISR-1100"
	elif prodcode == "isr1100be":
		prodname = "ROUTERS/ISRG3/ISR-1100X"
	elif prodcode == "isr4200":
		prodname = "ROUTERS/ISRG3/ISR-4200"
	elif prodcode == "isr4200-4300":
		prodname = "ROUTERS/ISRG3/ISR-4200-4300"
	elif prodcode == "isr4300":
		prodname = "ROUTERS/ISRG3/ISR-4300"
	elif prodcode == "isr4400":
		prodname = "ROUTERS/ISRG3/ISR-4400"
	elif prodcode == "isr4400v2":
		prodname = "ROUTERS/ISRG3/ISR-4461"
	elif prodcode == "mwr1900":
		prodname = "ROUTERS/MOBILE/MWR-1900"
	elif prodcode == "mwr1941":
		prodname = "ROUTERS/MOBILE/MWR-1941"
	elif prodcode == "mwr2941":
		prodname = "ROUTERS/MOBILE/MWR-2941"
	elif prodcode == "c3201":
		prodname = "ROUTERS/RUGGED/3201-AP"
	elif prodcode == "c3202":
		prodname = "ROUTERS/RUGGED/3202-AP"
	elif prodcode == "c3205":
		prodname = "ROUTERS/RUGGED/3205-AP"
	elif prodcode == "c3220":
		prodname = "ROUTERS/RUGGED/3220"
	elif prodcode == "c3230":
		prodname = "ROUTERS/RUGGED/3230"
	elif prodcode == "c3250":
		prodname = "ROUTERS/RUGGED/3250"
	elif prodcode == "c3270":
		prodname = "ROUTERS/RUGGED/3270"
	elif prodcode == "ncs4201":
		prodname = "ROUTERS/SP/NCS4201"
	elif prodcode == "ncs4202":
		prodname = "ROUTERS/SP/NCS4202"
	elif prodcode == "c10k":
		prodname = "ROUTERS/SP/10000/PRE1"
	elif prodcode == "c10k2":
		prodname = "ROUTERS/SP/10000/PRE2"
	elif prodcode == "c10k3":
		prodname = "ROUTERS/SP/10000/PRE3"
	elif prodcode == "c10k4":
		prodname = "ROUTERS/SP/10000/PRE4"
	elif prodcode == "c10700":
		prodname = "ROUTERS/SP/10700"
	elif prodcode == "c12k":
		prodname = "ROUTERS/SP/12000"
	elif prodcode == "c12kprp":
		prodname = "ROUTERS/SP/12000"
	elif prodcode == "gsr":
		prodname = "ROUTERS/SP/12000"
	elif prodcode == "XR12000":
		prodname = "ROUTERS/SP/12000-XR"
	elif prodcode == "c7000":
		prodname = "ROUTERS/SP/7000"
	elif prodcode == "c7100":
		prodname = "ROUTERS/SP/7100"
	elif prodcode == "c7200":
		prodname = "ROUTERS/SP/7200/NPEG1"
	elif prodcode == "c7200p":
		prodname = "ROUTERS/SP/7200/NPEG2"
	elif prodcode == "c7300":
		prodname = "ROUTERS/SP/7300"
	elif prodcode == "c7301":
		prodname = "ROUTERS/SP/7301"
	elif prodcode == "c7304":
		prodname = "ROUTERS/SP/7304"
	elif prodcode == "spa":
		prodname = "ROUTERS/SP/7304"
	elif prodcode == "c7400":
		prodname = "ROUTERS/SP/7400"
	elif prodcode == "rsp":
		prodname = "ROUTERS/SP/7500"
	elif prodcode == "c7600":
		prodname = "ROUTERS/SP/7600"
	elif prodcode == "c7600rsp72043":
		prodname = "ROUTERS/SP/7600/RSP720"
	elif prodcode == "rsp72043":
		prodname = "ROUTERS/SP/7600/RSP720"
	elif prodcode == "c7svcsami":
		prodname = "ROUTERS/SP/7600/SAMI"
	elif prodcode == "c7600s3223":
		prodname = "ROUTERS/SP/7600/SUP-32"
	elif prodcode == "c7600s72033":
		prodname = "ROUTERS/SP/7600/SUP-720"
	elif prodcode == "8000":
		prodname = "ROUTERS/SP/8000"
	elif prodcode == "csr1000v":
		prodname = "ROUTERS/VIRTUAL/CSR-1000V"
	elif prodcode == "csr1000v_milplr":
		prodname = "ROUTERS/VIRTUAL/CSR-1000V"
	elif prodcode == "vios":
		prodname = "ROUTERS/VIRTUAL/IOS-V"
	elif prodcode == "iosxrvdemo":
		prodname = "ROUTERS/VIRTUAL/IOS-XRv"
	elif prodcode == "iosxrvfull":
		prodname = "ROUTERS/VIRTUAL/IOS-XRv9000"
	elif prodcode == "xrvcontainer":
		prodname = "ROUTERS/VIRTUAL/IOS-XRv-CONTAINER"
	elif prodcode == "csa":
		prodname = "SECURITY/CISCO-SECURITY-AGENT"
	elif prodcode == "csm":
		prodname = "SECURITY/CISCO-SECURITY-MANAGER"
	elif prodcode == "asa":
		prodname = "SECURITY/FIREWALL/ASA"
	elif prodcode == "asacx":
		prodname = "SECURITY/FIREWALL/ASA-CX-MODULE"
	elif prodcode == "c6svc-fwm":
		prodname = "SECURITY/FIREWALL/CATALYST-6500-FWSM"
	elif prodcode == "firepower":
		prodname = "SECURITY/FIREWALL/FirePOWER"
	elif prodcode == "firepower1k":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-1xxx"
	elif prodcode == "firepower2k":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-2xxx"
	elif prodcode == "firepower3k":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-3xxx"
	elif prodcode == "firepower4k9k":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-4xxx-9xxx"
	elif prodcode == "firepower4200":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-42xx"
	elif prodcode == "firepowerisa3000":
		prodname = "SECURITY/FIREWALL/FirePOWER/ISA-3000"
	elif prodcode == "firepowertd":
		prodname = "SECURITY/FIREWALL/FirePOWER/VIRTUAL-FIREWALL"
	elif prodcode == "firepowerfmc":
		prodname = "SECURITY/FIREWALL/FirePOWER/FIREPOWER-MANAGEMENT-CENTER"
	elif prodcode == "pix":
		prodname = "SECURITY/FIREWALL/PIX"
	elif prodcode == "acs":
		prodname = "SECURITY/IDENTITY/ACS"
	elif prodcode == "ise":
		prodname = "SECURITY/IDENTITY/IDENTITY-SERVICES-ENGINE"
	elif prodcode == "isepic":
		prodname = "SECURITY/IDENTITY/IDENTITY-SERVICES-ENGINE-PIC"
	elif prodcode == "ciscoutd":
		prodname = "SECURITY/IOS-XE-UTD"
	elif prodcode == "ipsids":
		prodname = "SECURITY/IDS-IPS"
	elif prodcode == "ipsidsnm":
		prodname = "ROUTER-NM"
	elif prodcode == "ipsidsasa5585xssp10":
		prodname = "ASA5585-X-SSP_10"
	elif prodcode == "ipsidsasa5585xssp20":
		prodname = "ASA5585-X-SSP_20"
	elif prodcode == "ipsidsasa5585xssp40":
		prodname = "ASA5585-X-SSP_40"
	elif prodcode == "ipsidsasa5585xssp60":
		prodname = "ASA5585-X-SSP_60"
	elif prodcode == "ipsidsasa5512xssp":
		prodname = "ASA5512-X"
	elif prodcode == "ipsidsasa5515xssp":
		prodname = "ASA5515-X"
	elif prodcode == "ipsidsasa5525xssp":
		prodname = "ASA5525-X"
	elif prodcode == "ipsidsasa5545xssp":
		prodname = "ASA5545-X"
	elif prodcode == "ipsidsasa5555xssp":
		prodname = "ASA5555-X"
	elif prodcode == "ipsidsasassc":
		prodname = "ASA-AIPSSC"
	elif prodcode == "ipsidsasassm10":
		prodname = "ASA-AIPSSM-10"
	elif prodcode == "ipsidsasassm20":
		prodname = "ASA-AIPSSM-20"
	elif prodcode == "ipsidsasassm40":
		prodname = "ASA-AIPSSM-40"
	elif prodcode == "ipsidsipsadsm2":
		prodname = "IPS-Catalyst-6500-IDSM2"
	elif prodcode == "ipsidsipsaim":
		prodname = "IPS-AIM"
	elif prodcode == "ipsidsips4215":
		prodname = "IPS-4215"
	elif prodcode == "ipsidsips4240":
		prodname = "IPS-4240"
	elif prodcode == "ipsidsips4255":
		prodname = "IPS-4255"
	elif prodcode == "ipsidsips4260":
		prodname = "IPS-4260"
	elif prodcode == "ipsidsips4270":
		prodname = "IPS-4270"
	elif prodcode == "ipsidsips4345":
		prodname = "IPS-4345"
	elif prodcode == "ipsidsips4360":
		prodname = "IPS-4360"
	elif prodcode == "ipsidsips4510":
		prodname = "IPS-4510"
	elif prodcode == "ipsidsips4520":
		prodname = "IPS-4520"
	elif prodcode == "iosids":
		prodname = "SECURITY/IOS-IDS"
	elif prodcode == "ironport":
		prodname = "SECURITY/IRONPORT"
	elif prodcode == "mars":
		prodname = "SECURITY/MARS"
	elif prodcode == "vpn3000":
		prodname = "SECURITY/VPN-3000"
	elif prodcode == "anyconnect":
		prodname = "SECURITY/VPN-CLIENTS/ANYCONNECT (CISCO SECURE CLIENT)"
	elif prodcode == "vpnclient":
		prodname = "SECURITY/VPN-CLIENTS/IPSEC-CLIENT"
	elif prodcode == "aci":
		prodname = "SERVERS/APIC"
	elif prodcode == "css":
		prodname = "SERVERS/CSS"
	elif prodcode == "dcnm":
		prodname = "SERVERS/DATA-CENTER-NETWORK-MANAGER"
	elif prodcode == "dnac":
		prodname = "SERVERS/DNAC"
	elif prodcode == "hyperflex":
		prodname = "SERVERS/HYPERFLEX"
	elif prodcode == "onepk":
		prodname = "SERVERS/ONE-PK"
	elif prodcode == "ucsgeneric":
		prodname = "SERVERS/UCS"
	elif prodcode == "smallbusiness":
		prodname = "Small-Business"
	elif prodcode == "c125":
		prodname = "SERVERS/UCS/C-SERIES/C125M5"
	elif prodcode == "c200":
		prodname = "SERVERS/UCS/C-SERIES/C200M1-C200M2-C210M1-C210M2"
	elif prodcode == "c220":
		prodname = "SERVERS/UCS/C-SERIES/C220M3"
	elif prodcode == "c220m4":
		prodname = "SERVERS/UCS/C-SERIES/C220M4"
	elif prodcode == "c220m5":
		prodname = "SERVERS/UCS/C-SERIES/C220M5"
	elif prodcode == "c220m6":
		prodname = "SERVERS/UCS/C-SERIES/C220M6"
	elif prodcode == "c220m7":
		prodname = "SERVERS/UCS/C-SERIES/C220M7"
	elif prodcode == "c225m6":
		prodname = "SERVERS/UCS/C-SERIES/C225M6"
	elif prodcode == "c225m8":
		prodname = "SERVERS/UCS/C-SERIES/C225M8"
	elif prodcode == "c2x":
		prodname = "SERVERS/UCS/C-SERIES/C22M3-C22M4"
	elif prodcode == "c240":
		prodname = "SERVERS/UCS/C-SERIES/C240M3"
	elif prodcode == "c240m4":
		prodname = "SERVERS/UCS/C-SERIES/C240M4"
	elif prodcode == "c240m5":
		prodname = "SERVERS/UCS/C-SERIES/C240M5"
	elif prodcode == "c240m6":
		prodname = "SERVERS/UCS/C-SERIES/C240M6"
	elif prodcode == "c240m7":
		prodname = "SERVERS/UCS/C-SERIES/C240M7"
	elif prodcode == "c245m6":
		prodname = "SERVERS/UCS/C-SERIES/C245M6"
	elif prodcode == "c245m8":
		prodname = "SERVERS/UCS/C-SERIES/C245M8"
	elif prodcode == "c250":
		prodname = "SERVERS/UCS/C-SERIES/C250M1-C250M2"
	elif prodcode == "c260":
		prodname = "SERVERS/UCS/C-SERIES/C260M2"
	elif prodcode == "c2xxm3":
		prodname = "SERVERS/UCS/C-SERIES/C2XXM3"
	elif prodcode == "c2xxm4":
		prodname = "SERVERS/UCS/C-SERIES/C2XXM4"
	elif prodcode == "c2xxm5":
		prodname = "SERVERS/UCS/C-SERIES/C2XXM5"
	elif prodcode == "c2xxm6":
		prodname = "SERVERS/UCS/C-SERIES/C2XXM6"
	elif prodcode == "c2xxm7":
		prodname = "SERVERS/UCS/C-SERIES/C2XXM7"
	elif prodcode == "c3160":
		prodname = "SERVERS/UCS/C-SERIES/C3160"
	elif prodcode == "c3260":
		prodname = "SERVERS/UCS/C-SERIES/C3260"
	elif prodcode == "c420":
		prodname = "SERVERS/UCS/C-SERIES/C420M3"
	elif prodcode == "c460":
		prodname = "SERVERS/UCS/C-SERIES/C460M1-C460M2"
	elif prodcode == "c460m4":
		prodname = "SERVERS/UCS/C-SERIES/C460M4"
	elif prodcode == "c480m5":
		prodname = "SERVERS/UCS/C-SERIES/C480M5"
	elif prodcode == "ucsbseries":
		prodname = "SERVERS/UCS/B-SERIES/"
	elif prodcode == "ucscseries":
		prodname = "SERVERS/UCS/C-SERIES/"
	elif prodcode == "ucseseries":
		prodname = "SERVERS/UCS/E-SERIES/"
	elif prodcode == "e100":
		prodname = "SERVERS/UCS/E-SERIES/E1XX"
	elif prodcode == "ucs":
		prodname = "SERVERS/UCS/"
	elif prodcode == "c6400r":
		prodname = "SERVICE-GATEWAY/6400-NSP"
	elif prodcode == "c6400r2sp":
		prodname = "SERVICE-GATEWAY/6400-NSP"
	elif prodcode == "c6400s":
		prodname = "SERVICE-GATEWAY/6400-NSP"
	elif prodcode == "ni2":
		prodname = "SERVICE-GATEWAY/6XXX-DSL-Switch"
	elif prodcode == "m9100":
		prodname = "STORAGE/MDS-9100"
	elif prodcode == "m9200":
		prodname = "STORAGE/MDS-9200"
	elif prodcode == "m9250":
		prodname = "STORAGE/MDS-9250"
	elif prodcode == "m9500":
		prodname = "STORAGE/MDS-9500"
	elif prodcode == "m9700":
		prodname = "STORAGE/MDS-9700"
	elif prodcode == "ls1010":
		prodname = "SWITCHES/ATM/Lightspeed-1010"
	elif prodcode == "cbs30x0":
		prodname = "SWITCHES/BLADE-SWITCHES/CATALYST-3000-DELL-Blade"
	elif prodcode == "cbs31x0":
		prodname = "SWITCHES/BLADE-SWITCHES/CATALYST-3100-DELL-Blade"
	elif prodcode == "cigesm":
		prodname = "SWITCHES/BLADE-SWITCHES/IBM-Blade-Switch"
	elif prodcode == "cgesm":
		prodname = "SWITCHES/BLADE-SWITCHES/IBM-Blade-Switch"
	elif prodcode == "cmicr":
		prodname = "SWITCHES/CATALYST/Catalyst-Micro-Switches"
	elif prodcode == "cat1200":
		prodname = "SWITCHES/CATALYST/Catalyst-1200"
	elif prodcode == "cat1600":
		prodname = "SWITCHES/CATALYST/Catalyst-1600"
	elif prodcode == "cat1900":
		prodname = "SWITCHES/CATALYST/Catalyst-1900"
	elif prodcode == "c2350":
		prodname = "SWITCHES/CATALYST/Catalyst-2350"
	elif prodcode == "c2360":
		prodname = "SWITCHES/CATALYST/Catalyst-2360"
	elif prodcode == "cat2800":
		prodname = "SWITCHES/CATALYST/Catalyst-2800"
	elif prodcode == "c2800":
		prodname = "SWITCHES/CATALYST/Catalyst-2800"
	elif prodcode == "c29atm":
		prodname = "SWITCHES/CATALYST/Catalyst-2900-ATM"
	elif prodcode == "c2900XL":
		prodname = "SWITCHES/CATALYST/Catalyst-2900XL"
	elif prodcode == "c2900xl":
		prodname = "SWITCHES/CATALYST/Catalyst-2900XL"
	elif prodcode == "c2918":
		prodname = "SWITCHES/CATALYST/Catalyst-2918"
	elif prodcode == "c2928":
		prodname = "SWITCHES/CATALYST/Catalyst-2928"
	elif prodcode == "c2940":
		prodname = "SWITCHES/CATALYST/Catalyst-2940"
	elif prodcode == "cat2948g":
		prodname = "SWITCHES/CATALYST/Catalyst-2948G"
	elif prodcode == "c2950":
		prodname = "SWITCHES/CATALYST/Catalyst-2950"
	elif prodcode == "c2950lre":
		prodname = "SWITCHES/CATALYST/Catalyst-2950-LRE"
	elif prodcode == "c2955":
		prodname = "SWITCHES/CATALYST/Catalyst-2955"
	elif prodcode == "c2960":
		prodname = "SWITCHES/CATALYST/Catalyst-2960"
	elif prodcode == "c2960l":
		prodname = "SWITCHES/CATALYST/Catalyst-2960L"
	elif prodcode == "c2960s":
		prodname = "SWITCHES/CATALYST/Catalyst-2960S"
	elif prodcode == "c2960x":
		prodname = "SWITCHES/CATALYST/Catalyst-2960X"
	elif prodcode == "c2970":
		prodname = "SWITCHES/CATALYST/Catalyst-2970"
	elif prodcode == "c2975":
		prodname = "SWITCHES/CATALYST/Catalyst-2975"
	elif prodcode == "cat3000":
		prodname = "SWITCHES/CATALYST/Catalyst-3000"
	elif prodcode == "c3500xl":
		prodname = "SWITCHES/CATALYST/Catalyst-3500XL"
	elif prodcode == "c3500XL":
		prodname = "SWITCHES/CATALYST/Catalyst-3500XL"
	elif prodcode == "c3550":
		prodname = "SWITCHES/CATALYST/Catalyst-3550"
	elif prodcode == "c3560":
		prodname = "SWITCHES/CATALYST/Catalyst-3560"
	elif prodcode == "c3560e":
		prodname = "SWITCHES/CATALYST/Catalyst-3560E"
	elif prodcode == "c3560x":
		prodname = "SWITCHES/CATALYST/Catalyst-3560X"
	elif prodcode == "c3750":
		prodname = "SWITCHES/CATALYST/Catalyst-3750"
	elif prodcode == "c3750e":
		prodname = "SWITCHES/CATALYST/Catalyst-3750E"
	elif prodcode == "c3750me":
		prodname = "SWITCHES/METRO/Catalyst-3750ME"
	elif prodcode == "c3750x":
		prodname = "SWITCHES/CATALYST/Catalyst-3750X"
	elif prodcode == "cat3k_caa":
		prodname = "SWITCHES/CATALYST/Catalyst-3850-3650"
	elif prodcode == "cat4000":
		prodname = "SWITCHES/CATALYST/Catalyst-4000"
	elif prodcode == "cat4000s12":
		prodname = "SWITCHES/CATALYST/Catalyst-4000-SUP-I-II"
	elif prodcode == "c4224":
		prodname = "SWITCHES/CATALYST/Catalyst-4224"
	elif prodcode == "cat4232":
		prodname = "SWITCHES/CATALYST/Catalyst-4232"
	elif prodcode == "cat4500":
		prodname = "SWITCHES/CATALYST/Catalyst-4500"
	elif prodcode == "cat4500e":
		prodname = "SWITCHES/CATALYST/Catalyst-4500E"
	elif prodcode == "c4500e":
		prodname = "SWITCHES/CATALYST/Catalyst-4500E"
	elif prodcode == "cat4500es8":
		prodname = "SWITCHES/CATALYST/Catalyst-4500E-SUP8E"
	elif prodcode == "cat4840g":
		prodname = "SWITCHES/CATALYST/Catalyst-4840G"
	elif prodcode == "cat5000":
		prodname = "SWITCHES/CATALYST/Catalyst-5000"
	elif prodcode == "ce500":
		prodname = "SWITCHES/CATALYST/Catalyst-500E"
	elif prodcode == "c6500":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800"
	elif prodcode == "cat6000":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800"
	elif prodcode == "c6sup":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC1"
	elif prodcode == "c6sup11":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC1"
	elif prodcode == "c6sup12":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC2"
	elif prodcode == "c6k222":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2"
	elif prodcode == "c6sup22":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2"
	elif prodcode == "s222":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2"
	elif prodcode == "s2t54":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2T"
	elif prodcode == "s3223":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-32-MSFC2"
	elif prodcode == "s32p3":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-32-PISA"
	elif prodcode == "s72033":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-720-MSFC3"
	elif prodcode == "s6t64":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-6T"
	elif prodcode == "c6848x":
		prodname = "SWITCHES/CATALYST/Catalyst-6840-X"
	elif prodcode == "c6880x":
		prodname = "SWITCHES/CATALYST/Catalyst-6880-X"
	elif prodcode == "c8000be":
		prodname = "ROUTERS/CATALYST/Catalyst-8300-Edge"
	elif prodcode == "c8000aep":
		prodname = "ROUTERS/CATALYST/Catalyst-8500-Edge"
	elif prodcode == "c8000aes":
		prodname = "ROUTERS/CATALYST/Catalyst-8500L-Edge"
	elif prodcode == "cat8510c":
		prodname = "SWITCHES/CATALYST/Catalyst-8510CSR"
	elif prodcode == "cat8510m":
		prodname = "SWITCHES/CATALYST/Catalyst-8510MSR"
	elif prodcode == "cat8540c":
		prodname = "SWITCHES/CATALYST/Catalyst-8540CSR"
	elif prodcode == "cat8540m":
		prodname = "SWITCHES/CATALYST/Catalyst-8540MSR"
	elif prodcode == "cat9k":
		prodname = "SWITCHES/CATALYST/Catalyst-9000"
	elif prodcode == "cat9k_lite":
		prodname = "SWITCHES/CATALYST/Catalyst-9200"
	elif prodcode == "c1000":
		prodname = "SWITCHES/COMPACT/Catalyst-1000"
	elif prodcode == "c2960c405":
		prodname = "SWITCHES/COMPACT/Catalyst-2960C"
	elif prodcode == "c2960c405ex":
		prodname = "SWITCHES/COMPACT/Catalyst-2960CG"
	elif prodcode == "c2960cx":
		prodname = "SWITCHES/COMPACT/Catalyst-2960CX"
	elif prodcode == "c3560c":
		prodname = "SWITCHES/COMPACT/Catalyst-3560C"
	elif prodcode == "c3560c405":
		prodname = "SWITCHES/COMPACT/Catalyst-3560C"
	elif prodcode == "c3560c405ex":
		prodname = "SWITCHES/COMPACT/Catalyst-3560CG"
	elif prodcode == "c3560cx":
		prodname = "SWITCHES/COMPACT/Catalyst-3560CX"
	elif prodcode == "cdb":
		prodname = "SWITCHES/COMPACT/CATALYST-DIGITAL-BUILDING"
	elif prodcode == "c2020":
		prodname = "SWITCHES/EMBEDDED/2020"
	elif prodcode == "ess3x00":
		prodname = "SWITCHES/EMBEDDED/3300"
	elif prodcode == "cgs2520":
		prodname = "SWITCHES/GRID/CGS-2520"
	elif prodcode == "grwicdes":
		prodname = "SWITCHES/GRID/CGS-Module"
	elif prodcode == "ie2000":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-2000"
	elif prodcode == "ie2000u":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-2000U"
	elif prodcode == "ies":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-3000"
	elif prodcode == "ie3010":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-3010"
	elif prodcode == "ie31xx":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-3100"
	elif prodcode == "ie3x00":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-3x00"
	elif prodcode == "ie4000":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-4000"
	elif prodcode == "ie4010":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-4010"
	elif prodcode == "ie5000":
		prodname = "SWITCHES/INDUSTRIAL-ETHERNET/IE-5000"
	elif prodcode == "ir8340":
		prodname = "ROUTERS/INDUSTRIAL/IR8340"
	elif prodcode == "s6523":
		prodname = "SWITCHES/METRO/Catalyst-6500ME"
	elif prodcode == "me1200":
		prodname = "SWITCHES/METRO/ME-1200"
	elif prodcode == "ucs_ctrlr":
		prodname = "SWITCHES/METRO/ME-1200/UCS-CONTROLLLER"
	elif prodcode == "me240x":
		prodname = "SWITCHES/METRO/ME-2400"
	elif prodcode == "me2600x":
		prodname = "SWITCHES/METRO/ME-2600X"
	elif prodcode == "me340x":
		prodname = "SWITCHES/METRO/ME-3400"
	elif prodcode == "me360x":
		prodname = "SWITCHES/METRO/ME-3600"
	elif prodcode == "me360x_t":
		prodname = "SWITCHES/METRO/ME-3600"
	elif prodcode == "me380x":
		prodname = "SWITCHES/METRO/ME-3800"
	elif prodcode == "c2960sm":
		prodname = "SWITCHES/MODULES/Catalyst-2960-SERVICE-MODULE"
	elif prodcode == "c3kx":
		prodname = "SWITCHES/MODULES/Catalyst-3000-SERVICE-MODULE"
	elif prodcode == "c4gwy":
		prodname = "SWITCHES/CATALYST/Catalyst-4500/ACCESS-GATEWAY-MODULE"
	elif prodcode == "c5atm":
		prodname = "SWITCHES/CATALYST/Catalyst-5000/ATM"
	elif prodcode == "c5rsfc":
		prodname = "SWITCHES/CATALYST/Catalyst-5000/ROUTE-SWITCH-FEATURE-CARD"
	elif prodcode == "c5rsm":
		prodname = "SWITCHES/CATALYST/Catalyst-5000/ROUTE-SWITCH-MODULE"
	elif prodcode == "c6atm":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/ATM"
	elif prodcode == "wscmm":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/CMM"
	elif prodcode == "wsidsm2":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/IDSM2"
	elif prodcode == "c6msfc":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC1"
	elif prodcode == "c6msfc2":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC2"
	elif prodcode == "c6msfc2a":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC2A"
	elif prodcode == "c6msfc3":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC3"
	elif prodcode == "c6svc5fmwam":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM"
	elif prodcode == "c6svc6fmwam":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM"
	elif prodcode == "c6svcimwam":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM"
	elif prodcode == "svcmwam":
		prodname = "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM"
	elif prodcode == "c8000v":
		prodname = "ROUTERS/VIRTUAL/Catalyst-8000V"
	elif prodcode == "Nexus":
		prodname = "SWITCHES/NEXUS/"
	elif prodcode == "n1000v":
		prodname = "SWITCHES/NEXUS/Nexus-1000v"
	elif prodcode == "n3000":
		prodname = "SWITCHES/NEXUS/Nexus-3000"
	elif prodcode == "n3500":
		prodname = "SWITCHES/NEXUS/Nexus-3500"
	elif prodcode == "n4000":
		prodname = "SWITCHES/NEXUS/Nexus-4000"
	elif prodcode == "n5000":
		prodname = "SWITCHES/NEXUS/Nexus-5000"
	elif prodcode == "n6000":
		prodname = "SWITCHES/NEXUS/Nexus-6000-5600"
	elif prodcode == "n7000":
		prodname = "SWITCHES/NEXUS/Nexus-7000"
	elif prodcode == "n7700":
		prodname = "SWITCHES/NEXUS/Nexus-7700"
	elif prodcode == "n9000":
		prodname = "SWITCHES/NEXUS/Nexus-9000"
	elif prodcode == "nxos":
		prodname = "SWITCHES/NEXUS/Nexus-9000-3000"
	elif prodcode == "nxosv":
		prodname = "SWITCHES/NEXUS/Nexus-9000V"
	elif prodcode == "Nexus":
		prodname = "SWITCHES/NEXUS/"
	elif prodcode == "nxosgeneric":
		prodname = "SWITCHES/NEXUS/"
	elif prodcode == "s5400":
		prodname = "SWITCHES/ROCKWELL-STRATIX/5400"
	elif prodcode == "s5410":
		prodname = "SWITCHES/ROCKWELL-STRATIX/5410"
	elif prodcode == "s5700":
		prodname = "SWITCHES/ROCKWELL-STRATIX/5700"
	elif prodcode == "s5800":
		prodname = "SWITCHES/ROCKWELL-STRATIX/5800-IOS-XE"
	elif prodcode == "mica-modem":
		prodname = "UNIVERSAL-GATEWAY/"
	elif prodcode == "c5200":
		prodname = "UNIVERSAL-GATEWAY/AS-5200"
	elif prodcode == "c5300":
		prodname = "UNIVERSAL-GATEWAY/AS-5300"
	elif prodcode == "c5300XM":
		prodname = "UNIVERSAL-GATEWAY/AS-5300XM"
	elif prodcode == "c5350":
		prodname = "UNIVERSAL-GATEWAY/AS-5350"
	elif prodcode == "c5350XM":
		prodname = "UNIVERSAL-GATEWAY/AS-5350XM"
	elif prodcode == "c5400":
		prodname = "UNIVERSAL-GATEWAY/AS-5400"
	elif prodcode == "c5400XM":
		prodname = "UNIVERSAL-GATEWAY/AS-5400XM"
	elif prodcode == "c5800":
		prodname = "UNIVERSAL-GATEWAY/AS-5800"
	elif prodcode == "c5850":
		prodname = "UNIVERSAL-GATEWAY/AS-5850"
	elif prodcode == "c5850tb":
		prodname = "UNIVERSAL-GATEWAY/AS-5850ERSC"
	elif prodcode == "usbconsole":
		prodname = "USB-CONSOLE"
	elif prodcode == "vg200":
		prodname = "VOICE/GATEWAY/VG-200"
	elif prodcode == "voice":
		prodname = "VOICE"
	elif prodcode == "vg20x":
		prodname = "VOICE/GATEWAY/VG-202"
	elif prodcode == "vg20xxm":
		prodname = "VOICE/GATEWAY/VG-20x-XM"
	elif prodcode == "vg224":
		prodname = "VOICE/GATEWAY/VG-224"
	elif prodcode == "vg248":
		prodname = "VOICE/GATEWAY/VG-248"
	elif prodcode == "vg3x0":
		prodname = "VOICE/GATEWAY/VG-310-320"
	elif prodcode == "vg350":
		prodname = "VOICE/GATEWAY/VG-350"
	elif prodcode == "vg400":
		prodname = "VOICE/GATEWAY/VG-400"
	elif prodcode == "vg420":
		prodname = "VOICE/GATEWAY/VG-420"
	elif prodcode == "vg450":
		prodname = "VOICE/GATEWAY/VG-450"
	elif prodcode == "vgd":
		prodname = "VOICE/GATEWAY/VGD"
	elif prodcode == "c2420":
		prodname = "VOICE/IAD/2420-IAD"
	elif prodcode == "c2430":
		prodname = "VOICE/IAD/2430-IAD"
	elif prodcode == "c2435":
		prodname = "VOICE/IAD/2435-IAD"
	elif prodcode == "ics7700":
		prodname = "VOICE/ICS-7700"
	elif prodcode == "ipp3905":
		prodname = "VOICE/IP-PHONES/3905"
	elif prodcode == "ipp7911_7906":
		prodname = "VOICE/IP-PHONES/7906_7911"
	elif prodcode == "ipp7914":
		prodname = "VOICE/IP-PHONES/7914"
	elif prodcode == "ipp7915":
		prodname = "VOICE/IP-PHONES/7915"
	elif prodcode == "ipp7916":
		prodname = "VOICE/IP-PHONES/7916"
	elif prodcode == "ipp7921":
		prodname = "VOICE/IP-PHONES/7921"
	elif prodcode == "ipp7931":
		prodname = "VOICE/IP-PHONES/7931"
	elif prodcode == "ipp7937":
		prodname = "VOICE/IP-PHONES/7937-CONFERENCE-PHONE"
	elif prodcode == "ipp7940_7960":
		prodname = "VOICE/IP-PHONES/7940_7960"
	elif prodcode == "ipp7941_7961":
		prodname = "VOICE/IP-PHONES/7941_7961"
	elif prodcode == "ipp7942_7962":
		prodname = "VOICE/IP-PHONES/7942_7962"
	elif prodcode == "ipp7945_7965":
		prodname = "VOICE/IP-PHONES/7945_7965"
	elif prodcode == "ipp7970_7971":
		prodname = "VOICE/IP-PHONES/7970_7971"
	elif prodcode == "ipp7975":
		prodname = "VOICE/IP-PHONES/7975"
	elif prodcode == "ipp8845_65":
		prodname = "VOICE/IP-PHONES/8845_8865"
	elif prodcode == "ipp894x":
		prodname = "VOICE/IP-PHONES/894x"
	elif prodcode == "ata187":
		prodname = "VOICE/ATA/ATA-187"
	elif prodcode == "ata190":
		prodname = "VOICE/ATA/ATA-190"
	elif prodcode == "uc500":
		prodname = "VOICE/UC-500"
	elif prodcode == "wireless":
		prodname = "WIRELESS"
	elif prodcode == "c1100":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1100"
	elif prodcode == "c1130":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1130"
	elif prodcode == "c1140":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1140"
	elif prodcode == "c1200":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1200"
	elif prodcode == "c1240":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1240"
	elif prodcode == "c1250":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1250"
	elif prodcode == "c1310":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1310"
	elif prodcode == "c1520":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1500-Mesh-AP"
	elif prodcode == "c1570":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1570"
	elif prodcode == "c1550":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-1550"
	elif prodcode == "c350":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-350"
	elif prodcode == "c520":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-521"
	elif prodcode == "ap1g1":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G1-(700)"
	elif prodcode == "ap1g2":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G2-(1600)"
	elif prodcode == "ap1g3":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G3-(IR829-1530)"
	elif prodcode == "ap1g4":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G4-(1810-1830-1850)"
	elif prodcode == "ap1g5":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G5-(1540-1800-1815)"
	elif prodcode == "ap1g6":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G6-(c9117)"
	elif prodcode == "ap1g6a":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G6a-(c9130)"
	elif prodcode == "ap1g7":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP1G7-(C9115-9120)"
	elif prodcode == "ap3g1":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP3G1-(1260,3500)"
	elif prodcode == "ap3g2":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP3G2-(1600,1700,2600,2700,3600,3700)"
	elif prodcode == "c3700":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP3G2-(1600,1700,2600,2700,3600,3700)"
	elif prodcode == "ap3g3":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP3G3-(2800,3800,4800,1560,6300)"
	elif prodcode == "ap801":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP801-(861W,88xW,1911W-Routers)"
	elif prodcode == "ap802":
		prodname = "WIRELESS/ACCESS-POINT/AIRONET-AP802-(812,819,886VA-W,887VA-W,89xW-Routers)"
	elif prodcode == "AP1540":
		prodname = "WIRELESS/ACCESS-POINT/AP1540"
	elif prodcode == "AP1560":
		prodname = "WIRELESS/ACCESS-POINT/AP1560"
	elif prodcode == "AP1810w":
		prodname = "WIRELESS/ACCESS-POINT/AP1810w"
	elif prodcode == "AP1815":
		prodname = "WIRELESS/ACCESS-POINT/AP1815"
	elif prodcode == "AP1830":
		prodname = "WIRELESS/ACCESS-POINT/AP1830"
	elif prodcode == "AP1840":
		prodname = "WIRELESS/ACCESS-POINT/AP1840"
	elif prodcode == "AP1850":
		prodname = "WIRELESS/ACCESS-POINT/AP1850"
	elif prodcode == "AP2800":
		prodname = "WIRELESS/ACCESS-POINT/AP2800"
	elif prodcode == "AP3800":
		prodname = "WIRELESS/ACCESS-POINT/AP3800"
	elif prodcode == "AP4800":
		prodname = "WIRELESS/ACCESS-POINT/AP4800"
	elif prodcode == "AP6300":
		prodname = "WIRELESS/ACCESS-POINT/AP6300"
	elif prodcode == "ISR1100AC":
		prodname = "WIRELESS/ACCESS-POINT/ISR-AP1100AC"
	elif prodcode == "CT2500":
		prodname = "WIRELESS/CONTROLLER/2500"
	elif prodcode == "CT5500":
		prodname = "WIRELESS/CONTROLLER/5500"
	elif prodcode == "CT5520":
		prodname = "WIRELESS/CONTROLLER/5520"
	elif prodcode == "ct5760":
		prodname = "WIRELESS/CONTROLLER/5760"
	elif prodcode == "SWLC3750K9":
		prodname = "WIRELESS/CONTROLLER/CATALYST-3750"
	elif prodcode == "SWISMK9":
		prodname = "WIRELESS/CONTROLLER/CATALYST-6500-WISM"
	elif prodcode == "WISM":
		prodname = "WIRELESS/CONTROLLER/CATALYST-6500-WISM"
	elif prodcode == "WISM2":
		prodname = "WIRELESS/CONTROLLER/CATALYST-6500-WISM2"
	elif prodcode == "C9800-40":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800-40"
	elif prodcode == "C9800-80":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800-80"
	elif prodcode == "C9800-AP":
		prodname = "WIRELESS/ACCESS-POINT/CATALYST-9800-ACCESS-POINTS"
	elif prodcode == "C9800-APC":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9100-ACCESS-POINTS"
	elif prodcode == "C9800-CL":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800-CL"
	elif prodcode == "C9800-L":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800-L"
	elif prodcode == "CW9800H":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800H"
	elif prodcode == "CW9800M":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800M"
	elif prodcode == "C9800-SW":
		prodname = "WIRELESS/CONTROLLER/CATALYST-9800-SW"
	elif prodcode == "CT3504":
		prodname = "WIRELESS/CONTROLLER/3500"
	elif prodcode == "CT7500":
		prodname = "WIRELESS/CONTROLLER/CT7500"
	elif prodcode == "CT8500":
		prodname = "WIRELESS/CONTROLLER/CT8500"
	elif prodcode == "LOC2700":
		prodname = "WIRELESS/CONTROLLER/LOCATION-2700"
	elif prodcode == "WLCM":
		prodname = "WIRELESS/CONTROLLER/NM-NME"
	elif prodcode == "SRE":
		prodname = "WIRELESS/CONTROLLER/NM-SRE"
	elif prodcode == "CTVM":
		prodname = "WIRELESS/CONTROLLER/Virtual"
	elif prodcode == "WLC2006":
		prodname = "WIRELESS/CONTROLLER/WLC2006"
	elif prodcode == "WLC2100":
		prodname = "WIRELESS/CONTROLLER/WLC2100"
	elif prodcode == "WLC4100":
		prodname = "WIRELESS/CONTROLLER/WLC4100"
	elif prodcode == "WLC4400":
		prodname = "WIRELESS/CONTROLLER/WLC4400"
	elif prodcode == "WLC7500":
		prodname = "WIRELESS/CONTROLLER/WLC7500"
	elif prodcode == "CT8540":
		prodname = "WIRELESS/CONTROLLER/WLC8540"
	elif prodcode == "wcs":
		prodname = "WIRELESS/CONTROLLER/WCS"
	elif prodcode == "ccg110":
		prodname = "WIRELESS/GATEWAYS/CATALYST-WIRELESS-GATEWAY"
	elif prodcode == "cg":
		prodname = "WIRELESS/GATEWAYS/CATALYST-CELLULAR-GATEWAY"
	elif prodcode == "ucspe":
		prodname = "DEVELOPER-TOOLS/UCS-PLATFORM-EMULATOR"
	else:
		prodname = "UNKNOWN"
	return prodname

def fileprocessorrommon (debug1,filename):
	if debug1:
		print("\tModule#\tiosutils")
	if debug1:
		print("\tSubroutine#\tfileprocessorrommon")
	basepath = "ROMMON"
	if (
	filename == "asr900_15_6_43r_s_rommon.pkg" or 
	filename == "rsp2_15_6_15r_s_rommon.pkg" or 
	filename == "rsp2_15_6_19r_s_rommon.pkg" or 
	filename == "rsp2_15_6_30r_s_rommon.pkg" or 
	filename == "rsp2_rommon_15_4_3r_S5.pkg"
	):
		prodname = product("asr900")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("asr1000") or 
	filename == "ASR1000_RM_16_3_2R.bin"
	):
		prodname = product("asr1000")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("c6msfc2") or 
	filename.startswith("c6msfc2a") or 
	filename.startswith("c6msfc3") or 
	filename.startswith("c6ksup32") or 
	filename.startswith("c6ksup3") or 
	filename.startswith("c6dfc") or 
	filename.startswith("c6dfc3") or 
	filename.startswith("c2lc") or 
	filename.startswith("c6ksup720") or 
	filename.startswith("sup6t_rm") or 
	filename.startswith("pyramid_rm2") or 
	filename.startswith("cat6000-CPBOOT") or 
	filename.startswith("cat6000-sup2-rm2")
	):
		prodname = product("c6500")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename == "transformer_rm.bin.SPA.152-02r.SYS1" or 
	filename.startswith("c6840x_rm")
	):
		prodname = product("c6848x")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("governator_rm") or 
	filename.startswith("c6880x_rm")
	):
		prodname = product("c6880x")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C1800_RM2")
	):
		prodname = product("c180x")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C1841_RM2")
	):
		prodname = product("c1841")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C2800NM_RM2")
	):
		prodname = product("c2800nm")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("c805u")
	):
		prodname = product("c805")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C820_RM_ALT")
	):
		prodname = product("c820")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C860_RM2")
	):
		prodname = product("c860")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C860VAE2_RM2")
	):
		prodname = product("c860vae2")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C870_RM_ALT")
	):
		prodname = product("c870")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C880_RM2")
	):
		prodname = product("c880data")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C880s_RM")
	):
		prodname = product("c800g2")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C890_RM2") or 
	filename.startswith("C891x_RM2")
	):
		prodname = product("c890")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C890s_RM2")
	):
		prodname = product("c890s")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C2801_RM2")
	):
		prodname = product("c2801")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C1100-rommon")
	):
		prodname = product("c1100router")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3631_RM2")
	):
		prodname = product("c3631")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C2691_RM2")
	):
		prodname = product("c2691")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C2951_RM2")
	):
		prodname = product("c2951")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3725_RM2")
	):
		prodname = product("c3725")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3745_RM2")
	):
		prodname = product("c3745")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C7200")
	):
		prodname = product("c7200")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C7301")
	):
		prodname = product("c7301")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C7304")
	):
		prodname = product("c7304")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C7304")
	):
		prodname = product("c7304")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("firmwareupgrade")
	):
		prodname = product("cat4500es8")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("cat4000")
	):
		prodname = product("cat4000")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("cat4500")
	):
		prodname = product("cat4500")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("asr903-rommon")
	):
		prodname = product("asr903")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("asr920")
	):
		prodname = product("asr920")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("AS5400XM_RM")
	):
		prodname = product("c5400XM")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("COUGAR_RM")
	):
		prodname = product("cat8540c")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3945E_RM2")
	):
		prodname = product("c3900e")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3800_RM2")
	):
		prodname = product("c3845")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("MANOPT_RM")
	):
		prodname = product("ons15540")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3900_RM2")
	):
		prodname = product("c3900")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("VG3X0_RM")
	):
		prodname = product("vg3x0")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("VG224_RM2")
	):
		prodname = product("vg224")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("RPMXF_RM")
	):
		prodname = product("rpm")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("MWR1900_RM2")
	):
		prodname = product("mwr1900")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C2400_RM2")
	):
		prodname = product("c2430")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C3200_RM_ALT")
	):
		prodname = product("c3230")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C1900_2900_RM2")
	):
		prodname = product("c1900-2900")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C10700_RM2")
	):
		prodname = product("c10700")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("isr4200_4300_rommon")
	):
		prodname = product("isr4200-4300")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("isr4300-rommon")
	):
		prodname = product("isr4300")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("isr4400_rommon") or 
	filename.startswith("isr4400-rommon")
	):
		prodname = product("isr4400")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("isr4400v2_rommon")
	):
		prodname = product("isr4400v2")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("ROMMON") and filename.endswith("tar") or 
	filename.startswith("rommon") and filename.endswith("tar")
	):
		prodname = product("asr9k")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("rsp720_10ge_rp-rm2") or 
	filename.startswith("rsp720_10ge_sp-rm2") or 
	filename.startswith("rsp720_rp-rm2") or 
	filename.startswith("rsp720_sp-rm2")
	):
		prodname = product("c7600")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C5940_RM_ALT")
	):
		prodname = product("c5940")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C5915_RM")
	):
		prodname = product("c5915")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename.startswith("C9800-80-rommon")
	):
		prodname = product("C9800-80")
		filepath = filepath2(prodname,basepath)
		filemove (filepath, filename)
	elif (
	filename == "Rommon-123-8r.YH13-notes" or 
	filename == "Rommon-124-22r.YB5-notes" or 
	filename == "Rommon-151-1r.T4-notes" or 
	filename == "Rommon-151-1r.T5-notes" or 
	filename == "Rommon-150-1r.M12-notes"
	):
		filemove (basepath, filename)

def fileprocessorpagent (filename):
	filepath = "ROUTERS/PAGENT/"
	filemove (filepath, filename)

def util2digit (a,b):
	z = a + "." + b
	return z

def util3digit (a,b,c):
	z = a + "." + b + "." + c
	return z

def util4digit (a,b,c,d):
	z = a + "." + b + "." + c + "." + d
	return z

def util5digit (a,b,c,d,e):
	z = a + "." + b + "." + c + "." + d + "." + e
	return z

def util6digit (a,b,c,d,e,f):
	z = a + "." + b + "." + c + "." + d + "." + e + "." + f
	return z

def stringtolist (a):
	return list(a)

def filepath2 (a,b):
	z = a + "/" + b
	return z

def filepath3 (a,b,c):
	z = a + "/" + b + "/" + c
	return z

def filepath4 (a,b,c,d):
	z = a + "/" + b + "/" + c + "/" + d
	return z

def filepath5 (a,b,c,d,e):
	z = a + "/" + b + "/" + c + "/" + d + "/" + e
	return z

def filepath6 (a,b,c,d,e,f):
	z = a + "/" + b + "/" + c + "/" + d + "/" + e + "/" + f
	return z

def util2collapse (a,b):
	return a + b

def utilssinglemove (debug1,filename,prodname,imagecode):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutilssinglemove")
	filepath = filepath2 (prodname,imagecode) 
	filemove (filepath, filename)

def utilssingleprodname (debug1,filename,prodname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutilssingleprodname")
	filemove (prodname, filename)

def utils_dev_vf (debug1,filename,prodname,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_vf")
	if prodname == "UNKNOWN":
		messageunknowndev()
	else:
		splitbydot = workname.split(".")
		if len(splitbydot) == 2:
			version2 = util2digit(splitbydot[0],splitbydot[1])
		elif len(splitbydot) == 3:
			version2 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		elif len(splitbydot) == 4:
			version2 = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		elif len(splitbydot) == 5:
			version2 = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		elif len(splitbydot) == 6:
			version2 = util6digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
		filepath = filepath2(prodname,version2)
		filemove (filepath, filename)

def utils_dev_v2_vf (debug1,filename,prodname,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_v2_vf")
	if prodname == "UNKNOWN":
		messageunknowndev()
	else:
		splitbydot = workname.split(".")
		if len(splitbydot) == 3:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		elif len(splitbydot) == 4:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		elif len(splitbydot) == 5:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		elif len(splitbydot) == 5:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util6digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
		filepath = filepath3(prodname,version2,version3)
		filemove (filepath, filename)

def utils_dev_v2_vf_imagecode (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_v2_vf_imagecode")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydot = workname.split(".")
		if len(splitbydot) == 3:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		elif len(splitbydot) == 4:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		elif len(splitbydot) == 5:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		filepath = filepath4(prodname,version2,version3,imagecode)
		filemove (filepath, filename)

def utils_dev_imagecode_v2_vf (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_imagecode_v2_vf")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydot = workname.split(".")
		if len(splitbydot) == 3:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		elif len(splitbydot) == 4:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		elif len(splitbydot) == 5:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		elif len(splitbydot) == 6:
			version2 = util2digit(splitbydot[0],splitbydot[1])
			version3 = util6digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
		filepath = filepath4(prodname,imagecode,version2,version3)
		filemove (filepath, filename)

def utils_dev_imagecode_vf (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_imagecode_v2_vf")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydot = workname.split(".")
		if len(splitbydot) == 3:
			version3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
		elif len(splitbydot) == 4:
			version3 = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
		elif len(splitbydot) == 5:
			version3 = util5digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
		elif len(splitbydot) == 6:
			version3 = util6digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4],splitbydot[5])
		filepath = filepath3(prodname,imagecode,version3)
		filemove (filepath, filename)

def utils_dev_v2_vf_imagecode_dash (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_v2_vf_imagecode_dash")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydash = workname.split("-")
		if len(splitbydash) == 3:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
		elif len(splitbydash) == 4:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
		elif len(splitbydash) == 5:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util5digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
		filepath = filepath4(prodname,version2,version3,imagecode)
		filemove (filepath, filename)

def utils_dev_imagecode_v2_vf_dash (debug1,filename,prodname,imagecode,workname):
	if debug1:
		print("\tModule#\t\tiosutils")
		print("\tSubroutine#\tutils_dev_imagecode_v2_vf_dash")
	if prodname == "UNKNOWN":
		messageunknowndev()
	elif imagecode == "UNKNOWN":
		messageunknownfeat()
	else:
		splitbydash = workname.split("-")
		if len(splitbydash) == 3:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
		elif len(splitbydash) == 4:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util4digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3])
		elif len(splitbydash) == 5:
			version2 = util2digit(splitbydash[0],splitbydash[1])
			version3 = util5digit(splitbydash[0],splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
		filepath = filepath4(prodname,imagecode,version2,version3)
		filemove (filepath, filename)

def messageunknowndev ():
		print ("E001: This device type is unknown, please update the script with the information about the image.", end="\n")
def messageunknownfeat ():
		print ("E002: This feature set is unknown, please update the script with the information about the image.", end="\n")
def messageunknownfile ():
		print ("E003: This file in not classifiable, please update the script with the information about the image.", end="\n")
def messageunknownversion ():
		print ("E004: This version is unknown, please update the script with the information about the image.", end="\n")
