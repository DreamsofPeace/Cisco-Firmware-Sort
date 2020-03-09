import os, shutil, sys, re, getopt

def iostrain (train, version):
	#Return a software train.
	if train.startswith('AA'):
		version = version + 'AA'
	elif train.startswith('AX'):
		version = version + 'AX'
	elif train.startswith('AY'):
		version = version + 'AY'
	elif train.startswith('AZ'):
		version = version + 'AZ'
	elif train.startswith('BC'):
		version = version + 'BC'
	elif train.startswith('BT'):
		version = version + 'BT'
	elif train.startswith('BW'):
		version = version + 'BW'
	elif train.startswith('BX'):
		version = version + 'BX'
	elif train.startswith('BY'):
		version = version + 'BY'
	elif train.startswith('B'):
		version = version + 'B'
	elif train.startswith('CX'):
		version = version + 'CX'
	elif train.startswith('CY'):
		version = version + 'CY'
	elif train.startswith('CZ'):
		version = version + 'CZ'
	elif train.startswith('DA'):
		version = version + 'DA'
	elif train.startswith('DB'):
		version = version + 'DB'
	elif train.startswith('DC'):
		version = version + 'DC'
	elif train.startswith('DD'):
		version = version + 'DD'
	elif train.startswith('DX'):
		version = version + 'DX'
	elif train.startswith('EA'):
		version = version + 'EA'
	elif train.startswith('EB'):
		version = version + 'EB'
	elif train.startswith('EC'):
		version = version + 'EC'
	elif train.startswith('ED'):
		version = version + 'ED'
	elif train.startswith('EH'):
		version = version + 'EH'
	elif train.startswith('EJ'):
		version = version + 'EJ'
	elif train.startswith('EK'):
		version = version + 'EK'
	elif train.startswith('EO'):
		version = version + 'EO'
	elif train.startswith('EU'):
		version = version + 'EU'
	elif train.startswith('EV'):
		version = version + 'EV'
	elif train.startswith('EWA'):
		version = version + 'EWA'
	elif train.startswith('EW'):
		version = version + 'EW'
	elif train.startswith('EX'):
		version = version + 'EX'
	elif train.startswith('EY'):
		version = version + 'EY'
	elif train.startswith('EZ'):
		version = version + 'EZ'
	elif train.startswith('E'):
		version = version + 'E'
	elif train.startswith('FX'):
		version = version + 'FX'
	elif train.startswith('FY'):
		version = version + 'FY'
	elif train.startswith('FZ'):
		version = version + 'FZ'
	elif train.startswith('GA'):
		version = version + 'GA'
	elif train.startswith('GB'):
		version = version + 'GB'
	elif train.startswith('GCA'):
		version = version + 'GCA'
	elif train.startswith('GC'):
		version = version + 'GC'
	elif train.startswith('IRA'):
		version = version + 'IRA'
	elif train.startswith('IRB'):
		version = version + 'IRB'
	elif train.startswith('IRC'):
		version = version + 'IRC'
	elif train.startswith('IRD'):
		version = version + 'IRD'
	elif train.startswith('IRE'):
		version = version + 'IRE'
	elif train.startswith('IRF'):
		version = version + 'IRF'
	elif train.startswith('IRG'):
		version = version + 'IRG'
	elif train.startswith('IRH'):
		version = version + 'IRH'
	elif train.startswith('IRI'):
		version = version + 'IRI'
	elif train.startswith('IXA'):
		version = version + 'IXA'
	elif train.startswith('IXB'):
		version = version + 'IXB'
	elif train.startswith('IXC'):
		version = version + 'IXC'
	elif train.startswith('IXD'):
		version = version + 'IXD'
	elif train.startswith('IXE'):
		version = version + 'IXE'
	elif train.startswith('IXF'):
		version = version + 'IXF'
	elif train.startswith('IXG'):
		version = version + 'IXG'
	elif train.startswith('IXH'):
		version = version + 'IXH'
	elif train.startswith('JAL'):
		version = version + 'JAL'
	elif train.startswith('JAM'):
		version = version + 'JAM'
	elif train.startswith('JAN'):
		version = version + 'JAN'
	elif train.startswith('JAO'):
		version = version + 'JAO'
	elif train.startswith('JAX'):
		version = version + 'JAX'
	elif train.startswith('JAY'):
		version = version + 'JAY'
	elif train.startswith('JAZ'):
		version = version + 'JAZ'
	elif train.startswith('JA'):
		version = version + 'JA'
	elif train.startswith('JBA'):
		version = version + 'JBA'
	elif train.startswith('JBB'):
		version = version + 'JBB'
	elif train.startswith('JBC'):
		version = version + 'JBC'
	elif train.startswith('JBD'):
		version = version + 'JBD'
	elif train.startswith('JBE'):
		version = version + 'JBE'
	elif train.startswith('JB'):
		version = version + 'JB'
	elif train.startswith('JCA'):
		version = version + 'JCA'
	elif train.startswith('JCB'):
		version = version + 'JCB'
	elif train.startswith('JCC'):
		version = version + 'JCC'
	elif train.startswith('JCD'):
		version = version + 'JCD'
	elif train.startswith('JCE'):
		version = version + 'JCE'
	elif train.startswith('JC'):
		version = version + 'JC'
	elif train.startswith('JDA'):
		version = version + 'JDA'
	elif train.startswith('JDB'):
		version = version + 'JDB'
	elif train.startswith('JDC'):
		version = version + 'JDC'
	elif train.startswith('JDD'):
		version = version + 'JDD'
	elif train.startswith('JD'):
		version = version + 'JD'
	elif train.startswith('JEA'):
		version = version + 'JEA'
	elif train.startswith('JEB'):
		version = version + 'JEB'
	elif train.startswith('JEC'):
		version = version + 'JEC'
	elif train.startswith('JED'):
		version = version + 'JED'
	elif train.startswith('JEE'):
		version = version + 'JEE'
	elif train.startswith('JE'):
		version = version + 'JE'
	elif train.startswith('JFA'):
		version = version + 'JFA'
	elif train.startswith('JFB'):
		version = version + 'JFB'
	elif train.startswith('JFC'):
		version = version + 'JFC'
	elif train.startswith('JFD'):
		version = version + 'JFD'
	elif train.startswith('JF'):
		version = version + 'JF'
	elif train.startswith('JGA'):
		version = version + 'JGA'
	elif train.startswith('JGB'):
		version = version + 'JGB'
	elif train.startswith('JGC'):
		version = version + 'JGC'
	elif train.startswith('JGD'):
		version = version + 'JGD'
	elif train.startswith('JG'):
		version = version + 'JG'
	elif train.startswith('JHA'):
		version = version + 'JHA'
	elif train.startswith('JHB'):
		version = version + 'JHB'
	elif train.startswith('JHC'):
		version = version + 'JHC'
	elif train.startswith('JH'):
		version = version + 'JH'
	elif train.startswith('JI'):
		version = version + 'JI'
	elif train.startswith('JJ'):
		version = version + 'JJ'
	elif train.startswith('JK'):
		version = version + 'JK'
	elif train.startswith('JL'):
		version = version + 'JL'
	elif train.startswith('JMA'):
		version = version + 'JMA'
	elif train.startswith('JMB'):
		version = version + 'JMB'
	elif train.startswith('JMC'):
		version = version + 'JMC'
	elif train.startswith('JM'):
		version = version + 'JM'
	elif train.startswith('JN'):
		version = version + 'JN'
	elif train.startswith('JX'):
		version = version + 'JX'
	elif train.startswith('JY'):
		version = version + 'JY'
	elif train.startswith('L'):
		version = version + 'L'
	elif train.startswith('MB'):
		version = version + 'MB'
	elif train.startswith('MC'):
		version = version + 'MC'
	elif train.startswith('MDA'):
		version = version + 'MDA'
	elif train.startswith('MDB'):
		version = version + 'MDB'
	elif train.startswith('MD'):
		version = version + 'MD'
	elif train.startswith('MIG'):
		version = version + 'MIG'
	elif train.startswith('MRA'):
		version = version + 'MRA'
	elif train.startswith('MRB'):
		version = version + 'MRB'
	elif train.startswith('MR'):
		version = version + 'MR'
	elif train.startswith('MX'):
		version = version + 'MX'
	elif train.startswith('M'):
		version = version + 'M'
	elif train.startswith('NA'):
		version = version + 'NA'
	elif train.startswith('N'):
		version = version + 'N'
	elif train.startswith('PBAS'):
		version = version + 'PBAS'
	elif train.startswith('PBA'):
		version = version + 'PBA'
	elif train.startswith('PBS'):
		version = version + 'PBS'
	elif train.startswith('PB'):
		version = version + 'PB'
	elif train.startswith('PC'):
		version = version + 'PC'
	elif train.startswith('PIX'):
		version = version + 'PIX'
	elif train.startswith('PI'):
		version = version + 'PI'
	elif train.startswith('P'):
		version = version + 'P'
	elif train.startswith('SBA'):
		version = version + 'SBA'
	elif train.startswith('SBB'):
		version = version + 'SBB'
	elif train.startswith('SBC'):
		version = version + 'SBC'
	elif train.startswith('SBY'):
		version = version + 'SBY'
	elif train.startswith('SB'):
		version = version + 'SB'
	elif train.startswith('SCA'):
		version = version + 'SCA'
	elif train.startswith('SCB'):
		version = version + 'SCB'
	elif train.startswith('SCC'):
		version = version + 'SCC'
	elif train.startswith('SCD'):
		version = version + 'SCD'
	elif train.startswith('SCE'):
		version = version + 'SCE'
	elif train.startswith('SCF'):
		version = version + 'SCF'
	elif train.startswith('SCG'):
		version = version + 'SCG'
	elif train.startswith('SCH'):
		version = version + 'SCH'
	elif train.startswith('SCI'):
		version = version + 'SCI'
	elif train.startswith('SCJ'):
		version = version + 'SCJ'
	elif train.startswith('SCK'):
		version = version + 'SCK'
	elif train.startswith('SCL'):
		version = version + 'SCL'
	elif train.startswith('SCM'):
		version = version + 'SCM'
	elif train.startswith('SC'):
		version = version + 'SC'
	elif train.startswith('SEA'):
		version = version + 'SEA'
	elif train.startswith('SEB'):
		version = version + 'SEB'
	elif train.startswith('SEC'):
		version = version + 'SEC'
	elif train.startswith('SED'):
		version = version + 'SED'
	elif train.startswith('SEE'):
		version = version + 'SEE'
	elif train.startswith('SEF'):
		version = version + 'SEF'
	elif train.startswith('SEG'):
		version = version + 'SEG'
	elif train.startswith('SE'):
		version = version + 'SE'
	elif train.startswith('SGA'):
		version = version + 'SGA'
	elif train.startswith('SG'):
		version = version + 'SG'
	elif train.startswith('SRA'):
		version = version + 'SRA'
	elif train.startswith('SRB'):
		version = version + 'SRB'
	elif train.startswith('SRC'):
		version = version + 'SRC'
	elif train.startswith('SRD'):
		version = version + 'SRD'
	elif train.startswith('SRE'):
		version = version + 'SRE'
	elif train.startswith('SL'):
		version = version + 'SL'
	elif train.startswith('SM'):
		version = version + 'SM'
	elif train.startswith('SNG'):
		version = version + 'SNG'
	elif train.startswith('SNH'):
		version = version + 'SNH'
	elif train.startswith('SNI'):
		version = version + 'SNI'
	elif train.startswith('SN'):
		version = version + 'SN'
	elif train.startswith('SO'):
		version = version + 'SO'
	elif train.startswith('SP'):
		version = version + 'SP'
	elif train.startswith('SQ'):
		version = version + 'SQ'
	elif train.startswith('SRA'):
		version = version + 'SRA'
	elif train.startswith('SRB'):
		version = version + 'SRB'
	elif train.startswith('SRC'):
		version = version + 'SRC'
	elif train.startswith('SRD'):
		version = version + 'SRD'
	elif train.startswith('SRE'):
		version = version + 'SRE'
	elif train.startswith('SR'):
		version = version + 'SR'
	elif train.startswith('SS'):
		version = version + 'SS'
	elif train.startswith('STE'):
		version = version + 'STE'
	elif train.startswith('ST'):
		version = version + 'ST'
	elif train.startswith('SU'):
		version = version + 'SU'
	elif train.startswith('SVA'):
		version = version + 'SVA'
	elif train.startswith('SVB'):
		version = version + 'SVB'
	elif train.startswith('SVC'):
		version = version + 'SVC'
	elif train.startswith('SVD'):
		version = version + 'SVD'
	elif train.startswith('SVE'):
		version = version + 'SVE'
	elif train.startswith('SVF'):
		version = version + 'SVF'
	elif train.startswith('SV'):
		version = version + 'SV'
	elif train.startswith('SW'):
		version = version + 'SW'
	elif train.startswith('SXA'):
		version = version + 'SXA'
	elif train.startswith('SXB'):
		version = version + 'SXB'
	elif train.startswith('SXD'):
		version = version + 'SXD'
	elif train.startswith('SXE'):
		version = version + 'SXE'
	elif train.startswith('SXF'):
		version = version + 'SXF'
	elif train.startswith('SXH'):
		version = version + 'SXH'
	elif train.startswith('SXI'):
		version = version + 'SXI'
	elif train.startswith('SXJ'):
		version = version + 'SXJ'
	elif train.startswith('SX'):
		version = version + 'SX'
	elif train.startswith('SYA'):
		version = version + 'SYA'
	elif train.startswith('SYL'):
		version = version + 'SYL'
	elif train.startswith('SY'):
		version = version + 'SY'
	elif train.startswith('SZ'):
		version = version + 'SZ'
	elif train.startswith('S'):
		version = version + 'S'
	elif train.startswith('TPC'):
		version = version + 'TPC'
	elif train.startswith('TO'):
		version = version + 'TO'
	elif train.startswith('T'):
		version = version + 'T'
	elif train.startswith('UZ'):
		version = version + 'UZ'
	elif train.startswith('VZ'):
		version = version + 'VZ'
	elif train.startswith('WC'):
		version = version + 'WC'
	elif train.startswith('WO'):
		version = version + 'WO'
	elif train.startswith('WX'):
		version = version + 'WX'
	elif train.startswith('XA'):
		version = version + 'XA'
	elif train.startswith('XB'):
		version = version + 'XB'
	elif train.startswith('XC'):
		version = version + 'XC'
	elif train.startswith('XD'):
		version = version + 'XD'
	elif train.startswith('XE'):
		version = version + 'XE'
	elif train.startswith('XF'):
		version = version + 'XF'
	elif train.startswith('XG'):
		version = version + 'XG'
	elif train.startswith('XH'):
		version = version + 'XH'
	elif train.startswith('XI'):
		version = version + 'XI'
	elif train.startswith('XJ'):
		version = version + 'XJ'
	elif train.startswith('XK'):
		version = version + 'XK'
	elif train.startswith('XL'):
		version = version + 'XL'
	elif train.startswith('XM'):
		version = version + 'XM'
	elif train.startswith('XNA'):
		version = version + 'XNA'
	elif train.startswith('XNB'):
		version = version + 'XNB'
	elif train.startswith('XNC'):
		version = version + 'XNC'
	elif train.startswith('XND'):
		version = version + 'XND'
	elif train.startswith('XNE'):
		version = version + 'XNE'
	elif train.startswith('XO'):
		version = version + 'XO'
	elif train.startswith('XP'):
		version = version + 'XP'
	elif train.startswith('XQ'):
		version = version + 'XQ'
	elif train.startswith('XR'):
		version = version + 'XR'
	elif train.startswith('XS'):
		version = version + 'XS'
	elif train.startswith('XT'):
		version = version + 'XT'
	elif train.startswith('XU'):
		version = version + 'XU'
	elif train.startswith('XV'):
		version = version + 'XV'
	elif train.startswith('XW'):
		version = version + 'XW'
	elif train.startswith('XX'):
		version = version + 'XX'
	elif train.startswith('XY'):
		version = version + 'XY'
	elif train.startswith('XZ'):
		version = version + 'XZ'
	elif train.startswith('YA'):
		version = version + 'YA'
	elif train.startswith('YB'):
		version = version + 'YB'
	elif train.startswith('YC'):
		version = version + 'YC'
	elif train.startswith('YD'):
		version = version + 'YD'
	elif train.startswith('YE'):
		version = version + 'YE'
	elif train.startswith('YF'):
		version = version + 'YF'
	elif train.startswith('YG'):
		version = version + 'YG'
	elif train.startswith('YH'):
		version = version + 'YH'
	elif train.startswith('YI'):
		version = version + 'YI'
	elif train.startswith('YJ'):
		version = version + 'YJ'
	elif train.startswith('YK'):
		version = version + 'YK'
	elif train.startswith('YL'):
		version = version + 'YL'
	elif train.startswith('YM'):
		version = version + 'YM'
	elif train.startswith('YN'):
		version = version + 'YN'
	elif train.startswith('YO'):
		version = version + 'YO'
	elif train.startswith('YP'):
		version = version + 'YP'
	elif train.startswith('YQ'):
		version = version + 'YQ'
	elif train.startswith('YR'):
		version = version + 'YR'
	elif train.startswith('YS'):
		version = version + 'YS'
	elif train.startswith('YT'):
		version = version + 'YT'
	elif train.startswith('YU'):
		version = version + 'YU'
	elif train.startswith('YV'):
		version = version + 'YV'
	elif train.startswith('YW'):
		version = version + 'YW'
	elif train.startswith('YX'):
		version = version + 'YX'
	elif train.startswith('YZ'):
		version = version + 'YZ'
	elif train.startswith('YZ'):
		version = version + 'YZ'
	elif train.startswith('ZA'):
		version = version + 'ZA'
	elif train.startswith('ZB'):
		version = version + 'ZB'
	elif train.startswith('ZC'):
		version = version + 'ZC'
	elif train.startswith('ZD'):
		version = version + 'ZD'
	elif train.startswith('ZE'):
		version = version + 'ZE'
	elif train.startswith('ZF'):
		version = version + 'ZF'
	elif train.startswith('ZG'):
		version = version + 'ZG'
	elif train.startswith('ZH'):
		version = version + 'ZH'
	elif train.startswith('ZI'):
		version = version + 'ZI'
	elif train.startswith('ZJ'):
		version = version + 'ZJ'
	elif train.startswith('ZK'):
		version = version + 'ZK'
	elif train.startswith('ZL'):
		version = version + 'ZL'
	elif train.startswith('ZN'):
		version = version + 'ZN'
	elif train.startswith('ZO'):
		version = version + 'ZO'
	elif train.startswith('ZP'):
		version = version + 'ZP'
	elif train.startswith('ZQ'):
		version = version + 'ZQ'
	elif train.startswith('ZR'):
		version = version + 'ZR'
	elif train.startswith('ZS'):
		version = version + 'ZS'
	elif train.startswith('ZT'):
		version = version + 'ZT'
	elif train.startswith('ZU'):
		version = version + 'ZU'
	elif train.startswith('ZV'):
		version = version + 'ZV'
	elif train.startswith('ZW'):
		version = version + 'ZW'
	elif train.startswith('ZX'):
		version = version + 'ZX'
	elif train.startswith('ZYA'):
		version = version + 'ZYA'
	elif train.startswith('ZY'):
		version = version + 'ZY'
	elif train.startswith('ZZ'):
		version = version + 'ZZ'
	return version

def imagelookup (imagecode):
	#Returns an Image Type based from the if/elseif table below.
	if imagecode == 'sm10g':
		subdirectory = '10-GIG-MODULE'
	elif imagecode == 'i12o3s':
		subdirectory = 'ACCELERATED-BB-WITH-FW-INTRUSION-DETECTION'
	elif imagecode == 'i12s':
		subdirectory = 'ACCELERATED-BROADBAND-LAC-LNS-PTA'
	elif imagecode == 'adventerprisek9':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES'
	elif imagecode == 'adventerprisek9_wan':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES'
	elif imagecode == 'adventerprisek9_npe':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'adventerprisek9_li':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES-WITH-LAWFUL-INTERCEPT'
	elif imagecode == 'adventerprisek9_sna':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES-WITH-SNA-SWITCHING'
	elif imagecode == 'adventerprise':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES-NO-CRYPTO'
	elif imagecode == 'adventerprise_wan':
		subdirectory = 'ADVANCED-ENTERPRISE-SERVICES-NO-CRYPTO'
	elif imagecode == 'advipservicesk9':
		subdirectory = 'ADVANCED-IP-SERVICES'
	elif imagecode == 'advipservicesk9_wan':
		subdirectory = 'ADVANCED-IP-SERVICES'
	elif imagecode == 'advipservicesk9_npe':
		subdirectory = 'ADVANCED-IP-SERVICES-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'advipservicesk9_li':
		subdirectory = 'ADVANCED-IP-SERVICES-WITH-LAWFUL-INTERCEPT'
	elif imagecode == 'advipservices':
		subdirectory = 'ADVANCED-IP-SERVICES-NO-CRYPTO'
	elif imagecode == 'advipservicesk9_noli':
		subdirectory = 'ADVANCED-IP-SERVICES-WITHOUT-LAWFUL-INTERCEPT'
	elif imagecode == 'advsecurityk9':
		subdirectory = 'ADVANCED-SECURITY'
	elif imagecode == 'advseck9':
		subdirectory = 'ADVANCED-SECURITY'
	elif imagecode == 'advsecurityk9_npe':
		subdirectory = 'ADVANCED-SECURITY-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'advseck9_npe':
		subdirectory = 'ADVANCED-SECURITY-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'm':
		subdirectory = 'ATM'
	elif imagecode == 'lc':
		subdirectory = 'ATM-LINE-CARD'
	elif imagecode == 'wl':
		subdirectory = 'ATM-WORKGROUP-LANE'
	elif imagecode == 'wt':
		subdirectory = 'ATM-WORKGROUP-TRAFFIC-SHAPING'
	elif imagecode == 'wpk2':
		subdirectory = 'ATM-LAYER-3-SSH-3DES'
	elif imagecode == 'c5is':
		subdirectory = 'BASE-PDSN'
	elif imagecode == 'c5ik9s':
		subdirectory = 'BASE-PDSN-3DES'
	elif imagecode == 'i9s':
		subdirectory = 'BASIC-L3'
	elif imagecode == 'i9k91sc':
		subdirectory = 'BASIC-L3-3DES'
	elif imagecode == 'k9sy':
		subdirectory = 'BASIC-IP-3DES-PLUS'
	elif imagecode == 'k9o3sy':
		subdirectory = 'BASIC-IP-FIREWALL-2-3DES-PLUS'
	elif imagecode == 'k9sv3y':
		subdirectory = 'BASIC-IP-VOICE-3DES-PLUS'
	elif imagecode == 'boot':
		subdirectory = 'BOOT'
	elif imagecode == 'cboot':
		subdirectory = 'BOOT'
	elif imagecode == 'dboot':
		subdirectory = 'BOOT'
	elif imagecode == 'dboot2':
		subdirectory = 'BOOT'
	elif imagecode == 'eboot':
		subdirectory = 'BOOT'
	elif imagecode == 'k8boot':
		subdirectory = 'BOOT'
	elif imagecode == 'kboot':
		subdirectory = 'BOOT'
	elif imagecode == 'mboot':
		subdirectory = 'BOOT'
	elif imagecode == 'wboot':
		subdirectory = 'BOOT'
	elif imagecode == 'csgk9':
		subdirectory = 'CSG2-RTU-SAMI'
	elif imagecode == 'csg':
		subdirectory = 'CSG2-RTU-SAMI-NO-CRYPTO'
	elif imagecode == 'dsv':
		subdirectory = 'DESKTOP-IBM'
	elif imagecode == 'dk8s':
		subdirectory = 'DESKTOP-IBM-IPSEC-56'
	elif imagecode == 'dk8sv':
		subdirectory = 'DESKTOP-IBM-IPSEC-56'
	elif imagecode == 'ds56i':
		subdirectory = 'DESKTOP-IBM-IPSEC-56'
	elif imagecode == 'dsv56i':
		subdirectory = 'DESKTOP-IBM-IPSEC-56'
	elif imagecode == 'do3s':
		subdirectory = 'DESKTOP-IBM-FW-IDS'
	elif imagecode == 'do3sv':
		subdirectory = 'DESKTOP-IBM-FW-IDS'
	elif imagecode == 'dk2o3sv':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-3DES'
	elif imagecode == 'dk9o3s':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-3DES'
	elif imagecode == 'dk9o3sv':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-3DES'
	elif imagecode == 'dk8o3s':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-56'
	elif imagecode == 'dk8o3sv':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-56'
	elif imagecode == 'do3s56i':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-56'
	elif imagecode == 'do3sv56i':
		subdirectory = 'DESKTOP-IBM-FW-IDS-IPSEC-56'
	elif imagecode == 'hdiag':
		subdirectory = 'DIAGNOSTICS'
	elif imagecode == 'dsc':
		subdirectory = 'DIAL-SHELF-CONTROLLER'
	elif imagecode == 'w3':
		subdirectory = 'DISTRIBUTED-DIRECTOR-SYSTEM-SOFTWARE'
	elif imagecode == 'dmon':
		subdirectory = 'DMON'
	elif imagecode == 'ik8su2':
		subdirectory = 'DOCSIS-2-WAY-BPI-IP+-LAWFUL-INTERCEPT'
	elif imagecode == 'k8pu2':
		subdirectory = 'DOCSIS-2-WAY-BPI-LAWFUL-INTERCEPT'
	elif imagecode == 'k9p6u2':
		subdirectory = 'DOCSIS-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'k8p6u2':
		subdirectory = 'DOCSIS-BPI-LAWFUL-INTERCEPT'
	elif imagecode == 'dsl':
		subdirectory = 'DSL'
	elif imagecode == 'p10':
		subdirectory = 'EDGE-SERVICES-ROUTER'
	elif imagecode == 'p11':
		subdirectory = 'EDGE-SERVICES-ROUTER'
	elif imagecode == 'i6k2l2q4':
		subdirectory = 'EI-AND-SI-CRYPTO'
	elif imagecode == 'i5s':
		subdirectory = 'ENHANCED-L3'
	elif imagecode == 'i5k91s':
		subdirectory = 'ENHANCED-L3-3DES'
	elif imagecode == 'c6is':
		subdirectory = 'ENHANCED-PDSN'
	elif imagecode == 'c6ik9s':
		subdirectory = 'ENHANCED-PDSN-WITH-CRYPTO'
	elif imagecode == 'j':
		subdirectory = 'ENTERPRISE'
	elif imagecode == 'jsv':
		subdirectory = 'ENTERPRISE'
	elif imagecode == 'k':
		subdirectory = 'ENTERPRISE'
	elif imagecode == 'entbasek9':
		subdirectory = 'ENTERPRISE-BASE'
	elif imagecode == 'entbase':
		subdirectory = 'ENTERPRISE-BASE-NO-CRYPTO'
	elif imagecode == 'j1s3':
		subdirectory = 'ENTERPRISE-BASIC'
	elif imagecode == 'c3h2s':
		subdirectory = 'ENTERPRISE-COMMAND-CAPABLE'
	elif imagecode == 'jk9o3sv':
		subdirectory = 'ENTERPRISE-FW-MPLS-IPV6-SSH-3DES'
	elif imagecode == 'jk2sv':
		subdirectory = 'ENTERPRISE-IPSEC-3DES'
	elif imagecode == 'jk9s':
		subdirectory = 'ENTERPRISE-IPSEC-3DES'
	elif imagecode == 'jk9su2':
		subdirectory = 'ENTERPRISE-IPSEC-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'jk9su2v':
		subdirectory = 'ENTERPRISE-IPSEC-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'jk8s':
		subdirectory = 'ENTERPRISE-IPSEC-56'
	elif imagecode == 'jk8sv':
		subdirectory = 'ENTERPRISE-IPSEC-56'
	elif imagecode == 'jsv56i':
		subdirectory = 'ENTERPRISE-IPSEC-56'
	elif imagecode == 'jk9sv':
		subdirectory = 'ENTERPRISE-IPV6-SSH-3DES'
	elif imagecode == 'jsu2':
		subdirectory = 'ENTERPRISE-LAWFUL-INTERCEPT'
	elif imagecode == 'jx2':
		subdirectory = 'ENTERPRISE-MCM'
	elif imagecode == 'js':
		subdirectory = 'ENTERPRISE-PLUS'
	elif imagecode == 'js56':
		subdirectory = 'ENTERPRISE-PLUS-56'
	elif imagecode == 'js56i':
		subdirectory = 'ENTERPRISE-PLUS-IPSEC-56'
	elif imagecode == 'a2jsv5':
		subdirectory = 'ENTERPRISE-PLUS-VOIP-VOATM'
	elif imagecode == 'a2jk2sv5':
		subdirectory = 'ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-3DES'
	elif imagecode == 'a2jk9sv5':
		subdirectory = 'ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-3DES'
	elif imagecode == 'a2jk8sv5':
		subdirectory = 'ENTERPRISE-PLUS-VOIP-VOATM-IPSEC-56'
	elif imagecode == 'a2jsv5x':
		subdirectory = 'ENTERPRISE-PLUS-H323-MCM'
	elif imagecode == 'jsx':
		subdirectory = 'ENTERPRISE-PLUS-H323-MCM'
	elif imagecode == 'entservicesk9':
		subdirectory = 'ENTERPRISE-SERVICES'
	elif imagecode == 'entservicesk9_wan':
		subdirectory = 'ENTERPRISE-SERVICES'
	elif imagecode == 'entservices':
		subdirectory = 'ENTERPRISE-SERVICES-NO-CRYPTO'
	elif imagecode == 'entservices_wan':
		subdirectory = 'ENTERPRISE-SERVICES-NO-CRYPTO'
	elif imagecode == 'g4js':
		subdirectory = 'ENTERPRISE-SSG'
	elif imagecode == 'jk2s':
		subdirectory = 'ENTERPRISE-SSH-3DES-LAN-ONLY'
	elif imagecode == 'g5js':
		subdirectory = 'ENTERPRISE-WIRELESS'
	elif imagecode == 'g5jk8s':
		subdirectory = 'ENTERPRISE-WIRELESS-IPSEC-56'
	elif imagecode == 'ajs':
		subdirectory = 'ENTERPRISE-APPN-PLUS'
	elif imagecode == 'ajs40':
		subdirectory = 'ENTERPRISE-APPN-PLUS-IPSEC-40'
	elif imagecode == 'ajs56i':
		subdirectory = 'ENTERPRISE-APPN-PLUS-IPSEC-56'
	elif imagecode == 'k2':
		subdirectory = 'ENTERPRISE-CIP2'
	elif imagecode == 'jk8os':
		subdirectory = 'ENTERPRISE-FW-PLUS-IPSEC-56'
	elif imagecode == 'jos56i':
		subdirectory = 'ENTERPRISE-FW-PLUS-IPSEC-56'
	elif imagecode == 'jo3s':
		subdirectory = 'ENTERPRISE-FW-IDS'
	elif imagecode == 'jo3sv':
		subdirectory = 'ENTERPRISE-FW-IDS'
	elif imagecode == 'jk2o3sv':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-3DES'
	elif imagecode == 'jk9o3s':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-3DES'
	elif imagecode == 'io3s56i':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-56'
	elif imagecode == 'jk8o3s':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-56'
	elif imagecode == 'jk8o3sv':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-56'
	elif imagecode == 'jo3s56i':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-56'
	elif imagecode == 'jo3sv56i':
		subdirectory = 'ENTERPRISE-FW-IDS-IPSEC-56'
	elif imagecode == 'jk2o3s':
		subdirectory = 'ENTERPRISE-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'a3jsv':
		subdirectory = 'ENTERPRISE-SNASW'
	elif imagecode == 'a3jk2sv':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-3DES'
	elif imagecode == 'a3jk9s':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-3DES'
	elif imagecode == 'a3jk9sv':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-3DES'
	elif imagecode == 'a3jk8s':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-56'
	elif imagecode == 'a3jk8sv':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-56'
	elif imagecode == 'a3jsv56i':
		subdirectory = 'ENTERPRISE-SNASW-IPSEC-56'
	elif imagecode == 'a3js':
		subdirectory = 'ENTERPRISE-SNASW-PLUS'
	elif imagecode == 'a3jk91s':
		subdirectory = 'ENTERPRISE-SNASW-SSH-3DES'
	elif imagecode == 'fdiagsbflc':
		subdirectory = 'FIELD-DIAGNOSTICS-LINECARD-IMAGE'
	elif imagecode == 'fpd':
		subdirectory = 'FIELD-PROGRAMABLE-DEVICE'
	elif imagecode == 'f':
		subdirectory = 'FRAD'
	elif imagecode == 'fin':
		subdirectory = 'FRAD-EIGRP'
	elif imagecode == 'g6ik9s':
		subdirectory = 'GGSN-4.0-(3DES)'
	elif imagecode == 'g6is':
		subdirectory = 'GGSN-4.0-(BASE)'
	elif imagecode == 'g6ik8s':
		subdirectory = 'GGSN-4.0-(IPSEC)'
	elif imagecode == 'entservices_mw':
		subdirectory = 'GGSN-RELEASE-6'
	elif imagecode == 'adventerprisek9_mw':
		subdirectory = 'GGSN-RELEASE-6-(IPSEC)'
	elif imagecode == 'g7is':
		subdirectory = 'GGSN-SERIES-4-BASE'
	elif imagecode == 'g8ik9s':
		subdirectory = 'GGSN-SERIES-6-(3DES)'
	elif imagecode == 'g8ik8s':
		subdirectory = 'GGSN-SERIES-6-(IPSEC)'
	elif imagecode == 'g8is':
		subdirectory = 'GGSN-SERIES-6-BASE'
	elif imagecode == 'k1v4y5':
		subdirectory = 'HOME-OFFICE-VOICE-(SGCP-and-H.323)'
	elif imagecode == 'html':
		subdirectory = 'HTML'
	elif imagecode == 'adventerprisek9_ivs':
		subdirectory = 'INT-VOICE-VIDEO-GK,-IPIP-GW,-TDMIP-GW-AES'
	elif imagecode == 'adventerprisek9_ivs_li':
		subdirectory = 'INT-VOICE-VIDEO-GK,-IPIP-GW,-TDMIP-GW-AES,-LI'
	elif imagecode == 'js_ivs':
		subdirectory = 'INT-VOICE-VIDEO-IPIP-GW,-TDMIP-GW'
	elif imagecode == 'jk9su2_ivs':
		subdirectory = 'INT-VOICE-VIDEO-IPIP-GW,-TDMIP-GW-LI'
	elif imagecode == 'ipvoice_ivs':
		subdirectory = 'INT-VOICE-VIDEO,-IPIP-GW,-TDMIP-GW'
	elif imagecode == 'i':
		subdirectory = 'IP'
	elif imagecode == 'isv':
		subdirectory = 'IP'
	elif imagecode == 'y':
		subdirectory = 'IP'
	elif imagecode == 'y1':
		subdirectory = 'IP'
	elif imagecode == 'y6':
		subdirectory = 'IP'
	elif imagecode == 'i9k2':
		subdirectory = 'IP-BASE'
	elif imagecode == 'i9k2l2q3':
		subdirectory = 'IP-BASE'
	elif imagecode == 'i9k91':
		subdirectory = 'IP-BASE'
	elif imagecode == 'i9k91l2q3':
		subdirectory = 'IP-BASE'
	elif imagecode == 'ipbasek9':
		subdirectory = 'IP-BASE'
	elif imagecode == 'ipbasek9_wan':
		subdirectory = 'IP-BASE'
	elif imagecode == 'ipbasek9_access':
		subdirectory = 'IP-BASE-ACCESS-ONLY'
	elif imagecode == 'ipbase_access':
		subdirectory = 'IP-BASE-ACCESS-ONLY-NO-CRYPTO'
	elif imagecode == 'ipbasek9_npe':
		subdirectory = 'IP-BASE-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'ipbasek9npe':
		subdirectory = 'IP-BASE-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'ipbaselmk9':
		subdirectory = 'IP-BASE-WITH-EXPRESS-SETUP'
	elif imagecode == 'i9':
		subdirectory = 'IP-BASE-NO-CRYPTO'
	elif imagecode == 'i9q3l2':
		subdirectory = 'IP-BASE-NO-CRYPTO'
	elif imagecode == 'ipbase':
		subdirectory = 'IP-BASE-NO-CRYPTO'
	elif imagecode == 'ipbase_wan':
		subdirectory = 'IP-BASE-NO-CRYPTO'
	elif imagecode == 'ipbaselm':
		subdirectory = 'IP-BASE-NO-CRYPTO-WITH-EXPRESS-SETUP'
	elif imagecode == 'broadband':
		subdirectory = 'IP-BROADBAND'
	elif imagecode == 'oy1':
		subdirectory = 'IP-FW'
	elif imagecode == 'ik2s':
		subdirectory = 'IP-IPSEC-3DES'
	elif imagecode == 'ik9su2':
		subdirectory = 'IP-IPSEC-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'ik8sv':
		subdirectory = 'IP-IPSEC-56'
	elif imagecode == 'isv56i':
		subdirectory = 'IP-IPSEC-56'
	elif imagecode == 'isu2':
		subdirectory = 'IP-LAWFUL-INTERCEPT'
	elif imagecode == 'itpk9':
		subdirectory = 'IP-MAP-GATEWAY-BASE'
	elif imagecode == 'i4s':
		subdirectory = 'IP-PLUS'
	elif imagecode == 'is':
		subdirectory = 'IP-PLUS'
	elif imagecode == 'sy':
		subdirectory = 'IP-PLUS'
	elif imagecode == 'sy6':
		subdirectory = 'IP-PLUS'
	elif imagecode == 'is40':
		subdirectory = 'IP-PLUS-40'
	elif imagecode == 'is56':
		subdirectory = 'IP-PLUS-56'
	elif imagecode == 'is5':
		subdirectory = 'IP-PLUS-BASIC-WITHOUT-HD-ANALOG-AIM-ATM-VOICE'
	elif imagecode == 'is4':
		subdirectory = 'IP-PLUS-BASIC-WITHOUT-SWITCHING'
	elif imagecode == 'ik2sv':
		subdirectory = 'IP-PLUS-IPSEC-3DES'
	elif imagecode == 'ik9s':
		subdirectory = 'IP-PLUS-IPSEC-3DES'
	elif imagecode == 'ik9sv':
		subdirectory = 'IP-PLUS-IPSEC-3DES'
	elif imagecode == 'i5k9s':
		subdirectory = 'IP-PLUS-IPSEC-3DES-NO-ISDN'
	elif imagecode == 'ik8s':
		subdirectory = 'IP-PLUS-IPSEC-56'
	elif imagecode == 'is56i':
		subdirectory = 'IP-PLUS-IPSEC-56'
	elif imagecode == 'k8sy':
		subdirectory = 'IP-PLUS-IPSEC-56'
	elif imagecode == 'i5k8s':
		subdirectory = 'IP-PLUS-IPSEC-56-NO-ISDN'
	elif imagecode == 'bk9no3r2sy':
		subdirectory = 'IP-PLUS-IPX-AT-IBM-FW_IDS-IPSEC-3DES'
	elif imagecode == 'ik91s':
		subdirectory = 'IP-PLUS-SSH-3DES'
	elif imagecode == 'a2isv5':
		subdirectory = 'IP-PLUS-VOIP-VOATM'
	elif imagecode == 'a2ik8sv5':
		subdirectory = 'IP-PLUS-VOIP-VOATM-IPSEC-56'
	elif imagecode == 'ik2sx3':
		subdirectory = 'IP-PLUS-3DES'
	elif imagecode == 'ik2o3sx3':
		subdirectory = 'IP-PLUS-3DES-FW'
	elif imagecode == 'io3sx3':
		subdirectory = 'IP-PLUS-FW'
	elif imagecode == 'a3inro3sx3':
		subdirectory = 'IP-PLUS-FW-IPX-SNA'
	elif imagecode == 'isx356i':
		subdirectory = 'IP-PLUS-IPSEC-56'
	elif imagecode == 'io3sx356i':
		subdirectory = 'IP-PLUS-IPSEC-56-FW'
	elif imagecode == 'a3inrsx3c':
		subdirectory = 'IP-PLUS-IPX-SNA'
	elif imagecode == 'a3is':
		subdirectory = 'IP-PLUS-SNASW-PLUS'
	elif imagecode == 'i5k2':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'i5k2l2q3':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'i5k91':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'i5k91l2q3':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'i5q312':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'ipservicesk9':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'ipservicesk9_wan':
		subdirectory = 'IP-SERVICES'
	elif imagecode == 'ipservicesk9_npe':
		subdirectory = 'IP-SERVICES-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'ipserviceslmk9':
		subdirectory = 'IP-SERVICES-WITH-EXPRESS-SETUP'
	elif imagecode == 'ipservicesk9_li':
		subdirectory = 'IP-SERVICES-WITH-LAWFUL-INTERCEPT'
	elif imagecode == 'i5':
		subdirectory = 'IP-SERVICES-NO-CRYPTO'
	elif imagecode == 'i5q3l2':
		subdirectory = 'IP-SERVICES-NO-CRYPTO'
	elif imagecode == 'ipservices':
		subdirectory = 'IP-SERVICES-NO-CRYPTO'
	elif imagecode == 'ipservices_wan':
		subdirectory = 'IP-SERVICES-NO-CRYPTO'
	elif imagecode == 'ipserviceslm':
		subdirectory = 'IP-SERVICES-NO-CRYPTO-WITH-EXPRESS-SETUP'
	elif imagecode == 'pk9sv':
		subdirectory = 'IP-SSH-3DES'
	elif imagecode == 'pk9s':
		subdirectory = 'IP-SSH-3DES-LAN-ONLY'
	elif imagecode == 'i6k9o3s':
		subdirectory = 'IP-SUBSET-IPSEC-56-FW-VOICE'
	elif imagecode == 'i6k9s':
		subdirectory = 'IP-SUBSET-IPSEC-64-BIT-VOICE'
	elif imagecode == 'i6s':
		subdirectory = 'IP-SUBSET-VOICE'
	elif imagecode == 'ipv':
		subdirectory = 'IP-TRANSFER-POINT'
	elif imagecode == 'itp':
		subdirectory = 'IP-TRANSFER-POINT'
	elif imagecode == 'itpk9v':
		subdirectory = 'IP-TRANSFER-POINT'
	elif imagecode == 'itpv':
		subdirectory = 'IP-TRANSFER-POINT'
	elif imagecode == 'ipvoicek9':
		subdirectory = 'IP-VOICE'
	elif imagecode == 'ipvoice':
		subdirectory = 'IP-VOICE-NO-CRYPTO'
	elif imagecode == 'y7':
		subdirectory = 'IP-ADSL'
	elif imagecode == 'sy7':
		subdirectory = 'IP-ADSL-PLUS'
	elif imagecode == 'k9sy7':
		subdirectory = 'IP-ADSL-PLUS-IPSEC-3DES'
	elif imagecode == 'k8sy7':
		subdirectory = 'IP-ADSL-PLUS-IPSEC-56'
	elif imagecode == 'k9o3sy7':
		subdirectory = 'IP-ADSL-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'k8o3sy7':
		subdirectory = 'IP-ADSL-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'bnr2sy7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-PLUS'
	elif imagecode == 'bk9no3r2sy7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'bk8no3r2sy7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'bk9no3r2sv3y7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'bk8no3r2sv3y7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'bk9no3r2sv8y7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-VOX-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'bk8no3r2sv8y7':
		subdirectory = 'IP-ADSL-IPX-AT-IBM-VOX-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'no3sy7':
		subdirectory = 'IP-ADSL-IPX-FW-IDS-PLUS'
	elif imagecode == 'no3sv3y7':
		subdirectory = 'IP-ADSL-IPX-VOICE-FW-IDS-PLUS'
	elif imagecode == 'no3sv8y7':
		subdirectory = 'IP-ADSL-IPX-VOX-FW-IDS-PLUS'
	elif imagecode == 'sv3y7':
		subdirectory = 'IP-ADSL-VOICE-PLUS'
	elif imagecode == 'k9sv3y7':
		subdirectory = 'IP-ADSL-VOICE-PLUS-IPSEC-3DES'
	elif imagecode == 'k8sv3y7':
		subdirectory = 'IP-ADSL-VOICE-PLUS-IPSEC-56'
	elif imagecode == 'o3sv3y7':
		subdirectory = 'IP-ADSL-VOICE-FW-IDS-PLUS'
	elif imagecode == 'k9o3sv3y7':
		subdirectory = 'IP-ADSL-VOICE-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'k8o3sv3y7':
		subdirectory = 'IP-ADSL-VOICE-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'sv8y7':
		subdirectory = 'IP-ADSL-VOX-PLUS'
	elif imagecode == 'k9sv8y7':
		subdirectory = 'IP-ADSL-VOX-PLUS-IPSEC-3DES'
	elif imagecode == 'k8sv8y7':
		subdirectory = 'IP-ADSL-VOX-PLUS-IPSEC-56'
	elif imagecode == 'o3sv8y7':
		subdirectory = 'IP-ADSL-VOX-FW-IDS-PLUS'
	elif imagecode == 'k9o3sv8y7':
		subdirectory = 'IP-ADSL-VOX-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'k8o3sv8y7':
		subdirectory = 'IP-ADSL-VOX-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'qy':
		subdirectory = 'IP-ASYNC'
	elif imagecode == 'by':
		subdirectory = 'IP-AT'
	elif imagecode == 'a2i5k8s':
		subdirectory = 'IP-ATM-PLUS-IPSEC-56-NO-ISDN'
	elif imagecode == 'a2i5s':
		subdirectory = 'IP-ATM-PLUS-NO-ISDN'
	elif imagecode == 'a2i8sv5':
		subdirectory = 'IP-ATM-VOIP-VOATM'
	elif imagecode == 'a2i8k8sv5':
		subdirectory = 'IP-ATM-VOIP-VOATM-PLUS-IPSEC-56'
	elif imagecode == 'in':
		subdirectory = 'IP-BRIDGING'
	elif imagecode == 'io':
		subdirectory = 'IP-FW'
	elif imagecode == 'oy':
		subdirectory = 'IP-FW'
	elif imagecode == 'oy6':
		subdirectory = 'IP-FW'
	elif imagecode == 'k9o3y6':
		subdirectory = 'IP-FW-3DES'
	elif imagecode == 'k9oy1':
		subdirectory = 'IP-FW-3DES'
	elif imagecode == 'k9oy6':
		subdirectory = 'IP-FW-3DES'
	elif imagecode == 'osy6':
		subdirectory = 'IP-FW-PLUS'
	elif imagecode == 'k2osy6':
		subdirectory = 'IP-FW-PLUS-IPSEC-3DES'
	elif imagecode == 'k9osy6':
		subdirectory = 'IP-FW-PLUS-IPSEC-3DES'
	elif imagecode == 'ik8os':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'ios56i':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'k8osy':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'k8osy6':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'osy56i':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'osy656i':
		subdirectory = 'IP-FW-PLUS-IPSEC-56'
	elif imagecode == 'io3':
		subdirectory = 'IP-FW-IDS'
	elif imagecode == 'io3s':
		subdirectory = 'IP-FW-IDS'
	elif imagecode == 'io3sv':
		subdirectory = 'IP-FW-IDS'
	elif imagecode == 'o3y':
		subdirectory = 'IP-FW-IDS'
	elif imagecode == 'ik2o3s':
		subdirectory = 'IP-FW-IDS-IPSEC-3DES'
	elif imagecode == 'ik2o3sv':
		subdirectory = 'IP-FW-IDS-IPSEC-3DES'
	elif imagecode == 'ik9o3s':
		subdirectory = 'IP-FW-IDS-IPSEC-3DES'
	elif imagecode == 'ik9o3sv':
		subdirectory = 'IP-FW-IDS-IPSEC-3DES'
	elif imagecode == 'ik8o3s':
		subdirectory = 'IP-FW-IDS-IPSEC-56'
	elif imagecode == 'ik8o3sv':
		subdirectory = 'IP-FW-IDS-IPSEC-56'
	elif imagecode == 'io3sv56i':
		subdirectory = 'IP-FW-IDS-IPSEC-56'
	elif imagecode == 'o3sy56i':
		subdirectory = 'IP-FW-IDS-PLUS-IPSEC-3DES'
	elif imagecode == 'ik9o3s3':
		subdirectory = 'IP-FW-IDS-PLUS-IPSEC-3DES-BASIC'
	elif imagecode == 'ik9o3s6':
		subdirectory = 'IP-FW-IDS-PLUS-IPSEC-3DES-BASIC-NO-ATM'
	elif imagecode == 'ik9o3s7':
		subdirectory = 'IP-FW-IDS-PLUS-IPSEC-3DES-BASIC-NO-VOICE'
	elif imagecode == 'k8o3sy':
		subdirectory = 'IP-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'o3sy6':
		subdirectory = 'IP-FW-PLUS'
	elif imagecode == 'k9o3sy6':
		subdirectory = 'IP-FW-PLUS-3DES'
	elif imagecode == 'k9o3s8y6':
		subdirectory = 'IP-FW-PLUS-ISDN-DIAL-BACKUP-3DES-VPN'
	elif imagecode == 'ov6y6':
		subdirectory = 'IP-FW-VOICE'
	elif imagecode == 'k9osv6y6':
		subdirectory = 'IP-FW-VOICE-PLUS-3DES'
	elif imagecode == 'k9o3sv3y':
		subdirectory = 'IP-FW-VOICE-PLUS-IPSEC-3DES'
	elif imagecode == 'ix':
		subdirectory = 'IP-H323'
	elif imagecode == 'is3x':
		subdirectory = 'IP-H323-PLUS-BASIC'
	elif imagecode == 'ai3r4':
		subdirectory = 'IP-IBM-APPN7'
	elif imagecode == 'a3i3r4':
		subdirectory = 'IP-IBM-SNASW'
	elif imagecode == 'ny':
		subdirectory = 'IP-IPX'
	elif imagecode == 'k2nosy6':
		subdirectory = 'IP-IPX-FW-PLUS-IPSEC-3DES'
	elif imagecode == 'nosy656i':
		subdirectory = 'IP-IPX-FW-PLUS-IPSEC-56'
	elif imagecode == 'nsy':
		subdirectory = 'IP-IPX-PLUS'
	elif imagecode == 'nsy6':
		subdirectory = 'IP-IPX-PLUS'
	elif imagecode == 'bin':
		subdirectory = 'IP-IPX-APPLETALK'
	elif imagecode == 'bins':
		subdirectory = 'IP-IPX-APPLETALK-PLUS'
	elif imagecode == 'bino3s':
		subdirectory = 'IP-IPX-APPLETALK-PLUS-FW-IDS'
	elif imagecode == 'nqy':
		subdirectory = 'IP-IPX-ASYNC'
	elif imagecode == 'bny':
		subdirectory = 'IP-IPX-AT'
	elif imagecode == 'bnsy':
		subdirectory = 'IP-IPX-AT-PLUS'
	elif imagecode == 'bnsy40':
		subdirectory = 'IP-IPX-AT-PLUS-40'
	elif imagecode == 'bnsy56':
		subdirectory = 'IP-IPX-AT-PLUS-56'
	elif imagecode == 'd':
		subdirectory = 'IP-IPX-AT-DEC'
	elif imagecode == 'ds':
		subdirectory = 'IP-IPX-AT-DEC-PLUS'
	elif imagecode == 'ds40':
		subdirectory = 'IP-IPX-AT-DEC-PLUS-40'
	elif imagecode == 'dos':
		subdirectory = 'IP-IPX-AT-DEC-FW-PLUS'
	elif imagecode == 'bino3s3':
		subdirectory = 'IP-IPX-AT-FW-IDS-PLUS-BASIC'
	elif imagecode == 'bnr2y':
		subdirectory = 'IP-IPX-AT-IBM'
	elif imagecode == 'bnr2sy':
		subdirectory = 'IP-IPX-AT-IBM-PLUS'
	elif imagecode == 'bk8nor2sy':
		subdirectory = 'IP-IPX-AT-IBM-FW-PLUS-IPSEC-56'
	elif imagecode == 'bk8no3r2sy':
		subdirectory = 'IP-IPX-AT-IBM-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'bno3r2sy56i':
		subdirectory = 'IP-IPX-AT-IBM-FW-PLUS-IPSEC-56'
	elif imagecode == 'bnor2sy56i':
		subdirectory = 'IP-IPX-AT-IBM-FW-PLUS-IPSEC-56'
	elif imagecode == 'bk9no3r2sv3y':
		subdirectory = 'IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-3DES'
	elif imagecode == 'bk8no3r2sv3':
		subdirectory = 'IP-IPX-AT-IBM-FW-VOICE-PLUS-IPSEC-56'
	elif imagecode == 'bnr2sv3y':
		subdirectory = 'IP-IPX-AT-IBM-VOICE-PLUS'
	elif imagecode == 'bk8no3r2sv3y':
		subdirectory = 'IP-IPX-AT-IBM-VOICE-FW-IDS-PLUS-IPSEC-56'
	elif imagecode == 'nosy':
		subdirectory = 'IP-IPX-FW-PLUS'
	elif imagecode == 'k9nosy6':
		subdirectory = 'IP-IPX-FW-PLUS-IPSEC-3DES'
	elif imagecode == 'k8nosy6':
		subdirectory = 'IP-IPX-FW-PLUS-IPSEC-56'
	elif imagecode == 'no3sy':
		subdirectory = 'IP-IPX-FW-IDS-PLUS'
	elif imagecode == 'ino3s3':
		subdirectory = 'IP-IPX-FW-IDS-PLUS-BASIC'
	elif imagecode == 'no3sv3y':
		subdirectory = 'IP-IPX-VOICE-FW-IDS-PLUS'
	elif imagecode == 'iosxr':
		subdirectory = 'IP-MPLS'
	elif imagecode == 'y2':
		subdirectory = 'IP-OSPF-PIM'
	elif imagecode == 'k2sy':
		subdirectory = 'IP-PLUS-IPSEC-3DES'
	elif imagecode == 'sy56i':
		subdirectory = 'IP-PLUS-IPSEC-56'
	elif imagecode == 'isx3':
		subdirectory = 'IP-VOICE'
	elif imagecode == 'v6y6':
		subdirectory = 'IP-VOICE'
	elif imagecode == 'sv3y':
		subdirectory = 'IP-VOICE-PLUS'
	elif imagecode == 'sv6y6':
		subdirectory = 'IP-VOICE-PLUS'
	elif imagecode == 'k8sv3y':
		subdirectory = 'IP-VOICE-PLUS-IPSEC-56'
	elif imagecode == 'o3sv3y':
		subdirectory = 'IP-VOICE-FW-IDS-PLUS'
	elif imagecode == 'k8o3sv3y':
		subdirectory = 'IP-VOICE-FW-IDS-PLUS-IPSEC'
	elif imagecode == 'binrsx3':
		subdirectory = 'IP-VOICE-IPV6-IPX-APPLE-TALK'
	elif imagecode == 'a3bik9no3rsx3':
		subdirectory = 'IP-VOICE-IPX-SNA-FW-IDS-WAN-3DES'
	elif imagecode == 'sv8y':
		subdirectory = 'IP-VOX-PLUS'
	elif imagecode == 'g':
		subdirectory = 'ISDN'
	elif imagecode == 'i9k91s':
		subdirectory = 'L3-VOICE'
	elif imagecode == 'lanbase':
		subdirectory = 'LAN-BASE'
	elif imagecode == 'lanbasek9':
		subdirectory = 'LAN-BASE-SSH'
	elif imagecode == 'lanbaselmk9':
		subdirectory = 'LAN-BASE-SSH-WITH-EXPRESS-SETUP'
	elif imagecode == 'fin-l':
		subdirectory = 'LAN-FRAD'
	elif imagecode == 'f2in':
		subdirectory = 'LAN-FRAD-OSPF'
	elif imagecode == 'lanlite':
		subdirectory = 'LAN-LITE'
	elif imagecode == 'lanlitek9':
		subdirectory = 'LAN-LITE-SSH'
	elif imagecode == 'u2p10':
		subdirectory = 'LAWFUL-INTERCEPT'
	elif imagecode == 'k4u2p10':
		subdirectory = 'LAWFUL-INTERCEPT-SECURED-SHELL-3DES'
	elif imagecode == 'k9p11u2':
		subdirectory = 'LAWFUL-INTERCEPT-SECURED-SHELL-3DES'
	elif imagecode == 'k8p11u2':
		subdirectory = 'LAWFUL-INTERCEPT-SECURED-SHELL-DES'
	elif imagecode == 'i6q4l2':
		subdirectory = 'LAYER-2'
	elif imagecode == 'c3h2l9s':
		subdirectory = 'LONG-REACH-ETHERNET'
	elif imagecode == 'i6l2q4':
		subdirectory = 'LONG-REACH-ETHERNET-NO-CRYPTO'
	elif imagecode == 'metroaccessk9':
		subdirectory = 'METRO-ACCESS'
	elif imagecode == 'metroaccess':
		subdirectory = 'METRO-ACCESS-NO-CRYPTO'
	elif imagecode == 'metrobasek9':
		subdirectory = 'METRO-BASE'
	elif imagecode == 'metrobase':
		subdirectory = 'METRO-BASE-NO-CRYPTO'
	elif imagecode == 'metroipaccessk9':
		subdirectory = 'METRO-IP-ACCESS'
	elif imagecode == 'metroipaccess':
		subdirectory = 'METRO-IP-ACCESS-NO-CRYPTO'
	elif imagecode == 'i9su3':
		subdirectory = 'MPEG-2-L2'
	elif imagecode == 'i5su3':
		subdirectory = 'MPEG-2-L3'
	elif imagecode == 'h1is':
		subdirectory = 'MW-HOME-AGENT'
	elif imagecode == 'wp':
		subdirectory = 'NSP'
	elif imagecode == 'g4p5':
		subdirectory = 'NSP-SYSTEM'
	elif imagecode == 'k9o3sv9y5':
		subdirectory = 'PERFORMANCE-SMALL-OFFICE-VOICE-FW-IPSEC-3DES'
	elif imagecode == 'adviprank9':
		subdirectory = 'RAN-OPTIMIZATION'
	elif imagecode == 'iprank9':
		subdirectory = 'RAN-OPTIMIZATION'
	elif imagecode == 'ipran':
		subdirectory = 'RAN-OPTIMIZATION-NO-CRYPTO'
	elif imagecode == 'rcv':
		subdirectory = 'RECOVERY'
	elif imagecode == 'sv12y10':
		subdirectory = 'REDUCED-IP-ANALOG-VOICE-PLUS'
	elif imagecode == 'sv3y10':
		subdirectory = 'REDUCED-IP-VOICE-PLUS'
	elif imagecode == 'c':
		subdirectory = 'REMOTE-ACCESS-SERVER-(RAS)'
	elif imagecode == 'p':
		subdirectory = 'SERVICE-PROVIDER'
	elif imagecode == 'p12':
		subdirectory = 'SERVICE-PROVIDER'
	elif imagecode == 'p4':
		subdirectory = 'SERVICE-PROVIDER'
	elif imagecode == 'pv':
		subdirectory = 'SERVICE-PROVIDER'
	elif imagecode == 'spservicesk9':
		subdirectory = 'SERVICE-PROVIDER'
	elif imagecode == 'pk9u2':
		subdirectory = 'SERVICE-PROVIDER-IPSEC-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'k8p4':
		subdirectory = 'SERVICE-PROVIDER-IPSEC-56'
	elif imagecode == 'ps':
		subdirectory = 'SERVICE-PROVIDER-LAN-ONLY'
	elif imagecode == 'p9':
		subdirectory = 'SERVICE-PROVIDER-PLUS'
	elif imagecode == 'k8p9':
		subdirectory = 'SERVICE-PROVIDER-PLUS-IPSEC-3DES'
	elif imagecode == 'k9p9':
		subdirectory = 'SERVICE-PROVIDER-PLUS-IPSEC-3DES'
	elif imagecode == 'k9p9u2':
		subdirectory = 'SERVICE-PROVIDER-PLUS-IPSEC-3DES-LAWFUL-INTERCEPT'
	elif imagecode == 'k9p':
		subdirectory = 'SERVICE-PROVIDER-SSH-3DES'
	elif imagecode == 'pk2s':
		subdirectory = 'SERVICE-PROVIDER-SSH-3DES-LAN-ONLY'
	elif imagecode == 'k9p12':
		subdirectory = 'SERVICE-PROVIDER-WITH-CRYPTO'
	elif imagecode == 'po3sv':
		subdirectory = 'SERVICE-PROVIDER-WITH-FW-AND-VIP'
	elif imagecode == 'pk2o3sv':
		subdirectory = 'SERVICE-PROVIDER-WITH-FW-AND-VIP-3DES'
	elif imagecode == 'p7':
		subdirectory = 'SERVICE-PROVIDER-WITH-PT-TARP'
	elif imagecode == 'psv':
		subdirectory = 'SERVICE-PROVIDER-WITH-VIP'
	elif imagecode == 'pk2sv':
		subdirectory = 'SERVICE-PROVIDER-WITH-VIP-3DES'
	elif imagecode == 'k91p':
		subdirectory = 'SERVICE-PROVIDER-SECURE-SHELL-3DES'
	elif imagecode == 'k3pv':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-3DES'
	elif imagecode == 'k4p':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-3DES'
	elif imagecode == 'k4p10':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-3DES'
	elif imagecode == 'k91pv':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-3DES'
	elif imagecode == 'k9p11':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-3DES'
	elif imagecode == 'k3p':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-56'
	elif imagecode == 'k4pv':
		subdirectory = 'SERVICE-PROVIDER-SECURED-SHELL-56'
	elif imagecode == 'k1o3sv4y556i':
		subdirectory = 'SMALL-OFFICE+-VOICE-FW-IDS-IPSEC-56-(SGCP-and-H.323)'
	elif imagecode == 'k1k2o3sv4y5':
		subdirectory = 'SMALL-OFFICE+-VOICE-FW-IPSEC-3DES-(SGCP-and-H.323)'
	elif imagecode == 'k1o3v4y5':
		subdirectory = 'SMALL-OFFICE-VOICE-FW-IDS-(SGCP-and-H.323)'
	elif imagecode == 'ipss7':
		subdirectory = 'SS7-SIGNALING-LINK'
	elif imagecode == 'c3h2':
		subdirectory = 'STANDARD-COMMAND-CAPABLE'
	elif imagecode == 'sup':
		subdirectory = 'SUP1'
	elif imagecode == 'supk8':
		subdirectory = 'SUP1'
	elif imagecode == 'supcv':
		subdirectory = 'SUP1-WITH-CISCOVIEW'
	elif imagecode == 'supcvk8':
		subdirectory = 'SUP1-WITH-CISCOVIEW'
	elif imagecode == 'supcvk9':
		subdirectory = 'SUP1-WITH-CISCOVIEW-AND-SSH'
	elif imagecode == 'supk9':
		subdirectory = 'SUP1-WITH-SSH'
	elif imagecode == 'sup2':
		subdirectory = 'SUP2'
	elif imagecode == 'sup2k8':
		subdirectory = 'SUP2'
	elif imagecode == 'sup2cv':
		subdirectory = 'SUP2-WITH-CISCOVIEW'
	elif imagecode == 'sup2cvk8':
		subdirectory = 'SUP2-WITH-CISCOVIEW'
	elif imagecode == 'sup2cvk9':
		subdirectory = 'SUP2-WITH-CISCOVIEW-AND-SSH'
	elif imagecode == 'sup2k9':
		subdirectory = 'SUP2-WITH-SSH'
	elif imagecode == 'sup32pfc3k8':
		subdirectory = 'SUP32'
	elif imagecode == 'sup32pfc3cvk8':
		subdirectory = 'SUP32-WITH-CISCOVIEW'
	elif imagecode == 'sup32pfc3cvk9':
		subdirectory = 'SUP32-WITH-CISCOVIEW-AND-SSH'
	elif imagecode == 'sup32pfc3k9':
		subdirectory = 'SUP32-WITH-SSH'
	elif imagecode == 'sup720k8':
		subdirectory = 'SUP720'
	elif imagecode == 'sup720cvk8':
		subdirectory = 'SUP720-WITH-CISCOVIEW'
	elif imagecode == 'sup720cvk9':
		subdirectory = 'SUP720-WITH-CISCOVIEW-AND-SSH'
	elif imagecode == 'sup720k9':
		subdirectory = 'SUP720-WITH-SSH'
	elif imagecode == 'telco':
		subdirectory = 'TELCO-FEATURE-SET'
	elif imagecode == 'telcoent':
		subdirectory = 'TELCO-PLUS-FEATURE-SET'
	elif imagecode == 'telcoentk9':
		subdirectory = 'TELCO-PLUS-FEATURE-SET-IPSEC-3DES'
	elif imagecode == 'k1k2sv4y5':
		subdirectory = 'TELECOMMUTER+-VOICE-IPSEC-3DES-(SGCP-and-H.323)'
	elif imagecode == 'k1sv4y556i':
		subdirectory = 'TELECOMMUTER-VOICE-IPSEC-56-(SGCP-and-H.323)'
	elif imagecode == 'universalk9':
		subdirectory = 'UNIVERSAL'
	elif imagecode == 'universalk9_noli':
		subdirectory = 'UNIVERSAL-NO-LAWFUL-INTERCEPT'
	elif imagecode == 'universalk9_npe':
		subdirectory = 'UNIVERSAL-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'universalk9ldpe':
		subdirectory = 'UNIVERSAL-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'universalk9npe':
		subdirectory = 'UNIVERSAL-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'universalk9_npe_noli':
		subdirectory = 'UNIVERSAL-NO-PAYLOAD-ENCRYPTION-NO-LAWFUL-INTERCEPT'
	elif imagecode == 'universal':
		subdirectory = 'UNIVERSAL-DATA-NO-CRYPTO'
	elif imagecode == 'universalk9_iox':
		subdirectory = 'UNIVERSAL-IOX'
	elif imagecode == 'universalk9_iox_npe':
		subdirectory = 'UNIVERSAL-IOX-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'universalk9_lite':
		subdirectory = 'UNIVERSAL-LITE'
	elif imagecode == 'universalk9npe_lite':
		subdirectory = 'UNIVERSAL-LITE-NO-PAYLOAD-ENCRYPTION'
	elif imagecode == 'universal_lite':
		subdirectory = 'UNIVERSAL-LITE-NO-CRYPTO'
	elif imagecode == 'k91p11':
		subdirectory = 'UP-TO-8K-SUBSCRIBERS-WITH-3DES'
	elif imagecode == 'p11u2':
		subdirectory = 'UP-TO-8K-SUBSCRIBERS-WITH-LAWFUL-INTERCEPT'
	elif imagecode == 'k91p11u2':
		subdirectory = 'UP-TO-8K-SUBSCRIBERS-WITH-LAWFUL-INTERCEPT-3DES'
	elif imagecode == 'js2':
		subdirectory = 'VOICE-IP-TO-IP-VOICE-GATEWAY'
	elif imagecode == 'jk9s2':
		subdirectory = 'VOICE-IP-TO-IP-VOICE-GATEWAY-IPSEC-3DES'
	elif imagecode == 'k8o3v9y5':
		subdirectory = 'VOICE-H323-MGCP-SIP-FW-IPSEC56'
	elif imagecode == 'sipspawmak9':
		subdirectory = 'WEBEX-NODE'
	elif imagecode == 'w1is':
		subdirectory = 'WIMAX-ASNGW-1.0-CRYPTO'
	elif imagecode == 'k9w7':
		subdirectory = 'WIRELESS-LAN-AUTONOMOUS'
	elif imagecode == 'k9w8':
		subdirectory = 'WIRELESS-LAN-LIGHTWEIGHT-FULL'
	elif imagecode == 'rcvk9w8':
		subdirectory = 'WIRELESS-LAN-LIGHTWEIGHT-RECOVERY'
	else:
		subdirectory = 'UNKNOWN'
	return subdirectory

def product (prodcode):
	#Returns a Image Model based on the following if/elseif table below.
	if prodcode == 'c10k':
		prodname = '10000-PRE1'
	elif prodcode == 'c10k2':
		prodname = '10000-PRE2'
	elif prodcode == 'c10k3':
		prodname = '10000-PRE3'
	elif prodcode == 'c10k4':
		prodname = '10000-PRE4'
	elif prodcode == 'c1004':
		prodname = '1004'
	elif prodcode == 'c1005':
		prodname = '1005'
	elif prodcode == 'c10700':
		prodname = '10700'
	elif prodcode == 'c12k':
		prodname = '12000'
	elif prodcode == 'c12kprp':
		prodname = '12000'
	elif prodcode == 'gsr':
		prodname = '12000'
	elif prodcode == 'XR12000':
		prodname = '12000-XR'
	elif prodcode == 'c1400':
		prodname = '1400'
	elif prodcode == 'c1600':
		prodname = '1600'
	elif prodcode == 'c1600':
		prodname = '1600'
	elif prodcode == 'c1700':
		prodname = '1700'
	elif prodcode == 'c1700':
		prodname = '1700'
	elif prodcode == 'c1700':
		prodname = '1700'
	elif prodcode == 'c1710':
		prodname = '1710'
	elif prodcode == 'c1710':
		prodname = '1710'
	elif prodcode == 'c1711':
		prodname = '1711'
	elif prodcode == 'c1720':
		prodname = '1720'
	elif prodcode == 'c1720':
		prodname = '1720'
	elif prodcode == 'c1721':
		prodname = '1721'
	elif prodcode == 'c180x':
		prodname = '1800'
	elif prodcode == 'c1805':
		prodname = '1805'
	elif prodcode == 'c181x':
		prodname = '1810'
	elif prodcode == 'c1841':
		prodname = '1841'
	elif prodcode == 'c1841c':
		prodname = '1841-CHINA'
	elif prodcode == 'c1841ve':
		prodname = '1841-VE'
	elif prodcode == 'c1861':
		prodname = '1861'
	elif prodcode == 'c1900':
		prodname = '1900'
	elif prodcode == 'c2420':
		prodname = '2420-IAD'
	elif prodcode == 'c2430':
		prodname = '2430-IAD'
	elif prodcode == 'c2435':
		prodname = '2435-IAD'
	elif prodcode == 'c2500':
		prodname = '2500'
	elif prodcode == 'igs':
		prodname = '2500'
	elif prodcode == 'c25fx':
		prodname = '2500'
	elif prodcode == 'c2511':
		prodname = '2500'
	elif prodcode == 'c2600':
		prodname = '2600'
	elif prodcode == 'c2691':
		prodname = '2691'
	elif prodcode == 'c2800nm':
		prodname = '2800nm'
	elif prodcode == 'c2800nmc':
		prodname = '2800nm-CHINA'
	elif prodcode == 'c2800nmve':
		prodname = '2800nmve'
	elif prodcode == 'c2801':
		prodname = '2801'
	elif prodcode == 'c2801c':
		prodname = '2801-CHINA'
	elif prodcode == 'c2900':
		prodname = '2900'
	elif prodcode == 'c2911a':
		prodname = '2911a'
	elif prodcode == 'c2951':
		prodname = '2951'
	elif prodcode == 'c3201':
		prodname = '3201-AP'
	elif prodcode == 'c3202':
		prodname = '3202-AP'
	elif prodcode == 'c3205':
		prodname = '3205-AP'
	elif prodcode == 'c3220':
		prodname = '3220'
	elif prodcode == 'c3230':
		prodname = '3230'
	elif prodcode == 'c3250':
		prodname = '3250'
	elif prodcode == 'c3270':
		prodname = '3270'
	elif prodcode == 'c3620':
		prodname = '3620'
	elif prodcode == 'c3620':
		prodname = '3620'
	elif prodcode == 'c3631':
		prodname = '3631'
	elif prodcode == 'c3631':
		prodname = '3631'
	elif prodcode == 'c3640':
		prodname = '3640'
	elif prodcode == 'c3660':
		prodname = '3660'
	elif prodcode == 'c3660':
		prodname = '3660'
	elif prodcode == 'c3660':
		prodname = '3660'
	elif prodcode == 'c3660':
		prodname = '3660'
	elif prodcode == 'c3660':
		prodname = '3660'
	elif prodcode == 'c3725':
		prodname = '3725'
	elif prodcode == 'c3745':
		prodname = '3745'
	elif prodcode == 'c3825':
		prodname = '3825'
	elif prodcode == 'c3825c':
		prodname = '3825-CHINA'
	elif prodcode == 'c3825nv':
		prodname = '3825-NO VPN'
	elif prodcode == 'c3845':
		prodname = '3845'
	elif prodcode == 'c3845c':
		prodname = '3845-CHINA'
	elif prodcode == 'c3845nv':
		prodname = '3845-NO VPN'
	elif prodcode == 'c3900':
		prodname = '3900'
	elif prodcode == 'c3900e':
		prodname = '3900E'
	elif prodcode == 'c4000':
		prodname = '4000'
	elif prodcode == 'c4500':
		prodname = '4700M'
	elif prodcode == 'c6400r':
		prodname = '6400-NSP'
	elif prodcode == 'c6400r2sp':
		prodname = '6400-NSP'
	elif prodcode == 'c6400s':
		prodname = '6400-NSP'
	elif prodcode == 'ni2':
		prodname = '6XXX DSL Switch'
	elif prodcode == 'c7000':
		prodname = '7000'
	elif prodcode == 'c7100':
		prodname = '7100'
	elif prodcode == 'c7200':
		prodname = '7200'
	elif prodcode == 'c7200p':
		prodname = '7200-NPEG2'
	elif prodcode == 'c7300':
		prodname = '7300'
	elif prodcode == 'c7301':
		prodname = '7301'
	elif prodcode == 'c7304':
		prodname = '7304'
	elif prodcode == 'spa':
		prodname = '7304'
	elif prodcode == 'c7400':
		prodname = '7400'
	elif prodcode == 'rsp':
		prodname = '7500'
	elif prodcode == 'c7600':
		prodname = '7600'
	elif prodcode == 'c7600rsp72043':
		prodname = '7600-RSP720'
	elif prodcode == 'rsp72043':
		prodname = '7600-RSP720'
	elif prodcode == 'c7svcsami':
		prodname = '7600-SAMI'
	elif prodcode == 'c7600s3223':
		prodname = '7600-SUP32'
	elif prodcode == 'c7600s72033':
		prodname = '7600-SUP720'
	elif prodcode == 'c800':
		prodname = '800'
	elif prodcode == 'c800m':
		prodname = '800m'
	elif prodcode == 'c805':
		prodname = '805'
	elif prodcode == 'c806':
		prodname = '806'
	elif prodcode == 'c815':
		prodname = '815'
	elif prodcode == 'c820':
		prodname = '820'
	elif prodcode == 'c827v':
		prodname = '827'
	elif prodcode == 'c828':
		prodname = '828'
	elif prodcode == 'c831':
		prodname = '831'
	elif prodcode == 'c831':
		prodname = '831'
	elif prodcode == 'c836':
		prodname = '836'
	elif prodcode == 'c837':
		prodname = '837'
	elif prodcode == 'c850':
		prodname = '850'
	elif prodcode == 'c857':
		prodname = '857'
	elif prodcode == 'c860':
		prodname = '860'
	elif prodcode == 'c860vae':
		prodname = '860-VAE'
	elif prodcode == 'c860vae2':
		prodname = '860-VAE2'
	elif prodcode == 'c860vaej':
		prodname = '860-VAEJ'
	elif prodcode == 'c860vaew':
		prodname = '860-VAEW'
	elif prodcode == 'c870':
		prodname = '870'
	elif prodcode == 'c871':
		prodname = '871'
	elif prodcode == 'c880data':
		prodname = '880'
	elif prodcode == 'c880voice':
		prodname = '880-CUBE'
	elif prodcode == 'c890':
		prodname = '890'
	elif prodcode == 'c1100':
		prodname = 'Aironet 1100'
	elif prodcode == 'c1130':
		prodname = 'Aironet 1130'
	elif prodcode == 'c1140':
		prodname = 'Aironet 1140'
	elif prodcode == 'c1200':
		prodname = 'Aironet 1200'
	elif prodcode == 'c1240':
		prodname = 'Aironet 1240'
	elif prodcode == 'c1250':
		prodname = 'Aironet 1250'
	elif prodcode == 'c1310':
		prodname = 'Aironet 1310'
	elif prodcode == 'c1520':
		prodname = 'Aironet 1500 Mesh AP'
	elif prodcode == 'c350':
		prodname = 'Aironet 350'
	elif prodcode == 'c520':
		prodname = 'Aironet 521'
	elif prodcode == 'ap1g1':
		prodname = 'Aironet AP1G1 (700)'
	elif prodcode == 'ap1g2':
		prodname = 'Aironet AP1G2 (1600)'
	elif prodcode == 'ap1g3':
		prodname = 'Aironet AP1G3 (IR829)'
	elif prodcode == 'ap1g4':
		prodname = 'Aironet AP1G4 (1800)'
	elif prodcode == 'ap3g1':
		prodname = 'Aironet AP3G1 (1260,3500)'
	elif prodcode == 'ap3g2':
		prodname = 'Aironet AP3G2 (1600,1700,2600,2700,3600,3700)'
	elif prodcode == 'c3700':
		prodname = 'Aironet AP3G2 (1600,1700,2600,2700,3600,3700)'
	elif prodcode == 'ap3g3':
		prodname = 'Aironet AP3G3 (2800,3800)'
	elif prodcode == 'ap801':
		prodname = 'Aironet AP801 (861W,88xW,1911W Routers)'
	elif prodcode == 'ap802':
		prodname = 'Aironet AP802 (812,819,886VA-W,887VA-W,89xW Routers)'
	elif prodcode == 'c5200':
		prodname = 'AS 5200'
	elif prodcode == 'c5300':
		prodname = 'AS 5300'
	elif prodcode == 'c5300XM':
		prodname = 'AS 5300XM'
	elif prodcode == 'c5350':
		prodname = 'AS 5350'
	elif prodcode == 'c5350XM':
		prodname = 'AS 5350XM'
	elif prodcode == 'c5400':
		prodname = 'AS 5400'
	elif prodcode == 'c5400XM':
		prodname = 'AS 5400XM'
	elif prodcode == 'c5800':
		prodname = 'AS 5800'
	elif prodcode == 'c5850':
		prodname = 'AS 5850'
	elif prodcode == 'c5850tb':
		prodname = 'AS 5850ERSC'
	elif prodcode == 'asr1000':
		prodname = 'ASR 1000'
	elif prodcode == 'asr1000rp1':
		prodname = 'ASR 1000-RP1'
	elif prodcode == 'asr1000rp2':
		prodname = 'ASR 1000-RP2'
	elif prodcode == 'asr1000rpx86':
		prodname = 'ASR 1000-RPX86'
	elif prodcode == 'asr1001':
		prodname = 'ASR 1001'
	elif prodcode == 'asr1001x':
		prodname = 'ASR 1001X'
	elif prodcode == 'asr1002':
		prodname = 'ASR 1003'
	elif prodcode == 'asr1002x':
		prodname = 'ASR 1003X'
	elif prodcode == 'asr900rsp1':
		prodname = 'ASR 900-RSP1'
	elif prodcode == 'asr900rsp2':
		prodname = 'ASR 900-RSP2'
	elif prodcode == 'asr901':
		prodname = 'ASR 901'
	elif prodcode == 'asr901rsp1':
		prodname = 'ASR 901-RSP1'
	elif prodcode == 'asr901rsp2':
		prodname = 'ASR 901-RSP2'
	elif prodcode == 'asr901_sat':
		prodname = 'ASR 901-SAT'
	elif prodcode == 'asr901sec':
		prodname = 'ASR 901-SEC'
	elif prodcode == 'asr903rsp1':
		prodname = 'ASR 903-RSP1'
	elif prodcode == 'asr903rsp2':
		prodname = 'ASR 903-RSP2'
	elif prodcode == 'asr920':
		prodname = 'ASR 920'
	elif prodcode == 'c2350':
		prodname = 'Catalyst 2350'
	elif prodcode == 'c2360':
		prodname = 'Catalyst 2360'
	elif prodcode == 'c29atm':
		prodname = 'Catalyst 2900-ATM'
	elif prodcode == 'c2900XL':
		prodname = 'Catalyst 2900XL'
	elif prodcode == 'c2900xl':
		prodname = 'Catalyst 2900XL'
	elif prodcode == 'c2918':
		prodname = 'Catalyst 2918'
	elif prodcode == 'c2928':
		prodname = 'Catalyst 2928'
	elif prodcode == 'c2940':
		prodname = 'Catalyst 2940'
	elif prodcode == 'cat2948g':
		prodname = 'Catalyst 2948G'
	elif prodcode == 'c2950':
		prodname = 'Catalyst 2950'
	elif prodcode == 'c2950lre':
		prodname = 'Catalyst 2950 LRE'
	elif prodcode == 'c2955':
		prodname = 'Catalyst 2955'
	elif prodcode == 'c2960':
		prodname = 'Catalyst 2960'
	elif prodcode == 'c2960sm':
		prodname = 'Catalyst 2960 SERVICE MODULE'
	elif prodcode == 'c2960c405':
		prodname = 'Catalyst 2960C'
	elif prodcode == 'c2960c405ex':
		prodname = 'Catalyst 2960CG'
	elif prodcode == 'c2960cx':
		prodname = 'Catalyst 2960CX'
	elif prodcode == 'c2960l':
		prodname = 'Catalyst 2960L'
	elif prodcode == 'c2960s':
		prodname = 'Catalyst 2960S'
	elif prodcode == 'c2960x':
		prodname = 'Catalyst 2960X'
	elif prodcode == 'c2970':
		prodname = 'Catalyst 2970'
	elif prodcode == 'c2975':
		prodname = 'Catalyst 2975'
	elif prodcode == 'c3kx':
		prodname = 'Catalyst 3000 SERVICE MODULE'
	elif prodcode == 'c3500xl':
		prodname = 'Catalyst 3500XL'
	elif prodcode == 'c3500XL':
		prodname = 'Catalyst 3500XL'
	elif prodcode == 'c3550':
		prodname = 'Catalyst 3550'
	elif prodcode == 'c3560':
		prodname = 'Catalyst 3560'
	elif prodcode == 'c3560c':
		prodname = 'Catalyst 3560C'
	elif prodcode == 'c3560c405':
		prodname = 'Catalyst 3560C'
	elif prodcode == 'c3560c405ex':
		prodname = 'Catalyst 3560CG'
	elif prodcode == 'c3560cx':
		prodname = 'Catalyst 3560CX'
	elif prodcode == 'c3560e':
		prodname = 'Catalyst 3560E'
	elif prodcode == 'c3560x':
		prodname = 'Catalyst 3560X'
	elif prodcode == 'c3750':
		prodname = 'Catalyst 3750'
	elif prodcode == 'c3750e':
		prodname = 'Catalyst 3750E'
	elif prodcode == 'c3750me':
		prodname = 'Catalyst 3750ME'
	elif prodcode == 'c3750x':
		prodname = 'Catalyst 3750X'
	elif prodcode == 'cat3k_caa':
		prodname = 'Catalyst 3850'
	elif prodcode == 'cat4000':
		prodname = 'Catalyst 4000'
	elif prodcode == 'cat4000':
		prodname = 'Catalyst 4000-Hybrid Mode'
	elif prodcode == 'cat4000':
		prodname = 'Catalyst 4000-SUP-III'
	elif prodcode == 'c4224':
		prodname = 'Catalyst 4224'
	elif prodcode == 'cat4232':
		prodname = 'Catalyst 4232'
	elif prodcode == 'cat4500':
		prodname = 'Catalyst 4500'
	elif prodcode == 'c4gwy':
		prodname = 'Catalyst 4500-Access Gateway Module'
	elif prodcode == 'c4500e':
		prodname = 'Catalyst 4500E'
	elif prodcode == 'cat4500e':
		prodname = 'Catalyst 4500E'
	elif prodcode == 'cat4500es8':
		prodname = 'Catalyst 4500E-SUP8E'
	elif prodcode == 'cat5000':
		prodname = 'Catalyst 5000'
	elif prodcode == 'c5atm':
		prodname = 'Catalyst 5000-ATM'
	elif prodcode == 'c5rsfc':
		prodname = 'Catalyst 5000-Route Switch Feature Card'
	elif prodcode == 'c5rsm':
		prodname = 'Catalyst 5000-Route Switch Module'
	elif prodcode == 'ce500':
		prodname = 'Catalyst 500E'
	elif prodcode == 'c6500':
		prodname = 'Catalyst 6500'
	elif prodcode == 'c6atm':
		prodname = 'Catalyst 6500-ATM'
	elif prodcode == 'wscmm':
		prodname = 'Catalyst 6500-CMM'
	elif prodcode == 'cat6000':
		prodname = 'Catalyst 6500-Hybrid Mode'
	elif prodcode == 's6523':
		prodname = 'Catalyst 6500ME'
	elif prodcode == 'c6msfc':
		prodname = 'Catalyst 6500-MSFC1'
	elif prodcode == 'c6msfc2':
		prodname = 'Catalyst 6500-MSFC2'
	elif prodcode == 'c6msfc2a':
		prodname = 'Catalyst 6500-MSFC2A'
	elif prodcode == 'c6msfc3':
		prodname = 'Catalyst 6500-MSFC3'
	elif prodcode == 'c6svc5fmwam':
		prodname = 'Catalyst 6500-MWAM'
	elif prodcode == 'c6svc6fmwam':
		prodname = 'Catalyst 6500-MWAM'
	elif prodcode == 'c6svcimwam':
		prodname = 'Catalyst 6500-MWAM'
	elif prodcode == 'svcmwam':
		prodname = 'Catalyst 6500-MWAM'
	elif prodcode == 'c6sup11':
		prodname = 'Catalyst 6500-SUP1-MSFC1'
	elif prodcode == 'c6sup12':
		prodname = 'Catalyst 6500-SUP1-MSFC2'
	elif prodcode == 'c6k222':
		prodname = 'Catalyst 6500-SUP2-MSFC2'
	elif prodcode == 'c6sup22':
		prodname = 'Catalyst 6500-SUP2-MSFC2'
	elif prodcode == 's222':
		prodname = 'Catalyst 6500-SUP2-MSFC2'
	elif prodcode == 's2t54':
		prodname = 'Catalyst 6500-SUP2T'
	elif prodcode == 's3223':
		prodname = 'Catalyst 6500-SUP32-MSFC2'
	elif prodcode == 's32p3':
		prodname = 'Catalyst 6500-SUP32-PISA'
	elif prodcode == 's72033':
		prodname = 'Catalyst 6500-SUP720-MSFC3'
	elif prodcode == 's6t64':
		prodname = 'Catalyst 6800-SUP6T'
	elif prodcode == 'c6848x':
		prodname = 'Catalyst 6840-X'
	elif prodcode == 'c6880x':
		prodname = 'Catalyst 6880-X'
	elif prodcode == 'cat8510c':
		prodname = 'Catalyst 8510CSR'
	elif prodcode == 'cat8510m':
		prodname = 'Catalyst 8510MSR'
	elif prodcode == 'cat8540c':
		prodname = 'Catalyst 8540CSR'
	elif prodcode == 'cat8540m':
		prodname = 'Catalyst 8540MSR'
	elif prodcode == 'cbs30x0':
		prodname = 'Catalyst Blade Switch-30x0'
	elif prodcode == 'cbs31x0':
		prodname = 'Catalyst Blade Switch-31x0'
	elif prodcode == 'cdb':
		prodname = 'Catalyst Digital Building'
	elif prodcode == 'cgr2010':
		prodname = 'CGR 2010'
	elif prodcode == 'cgs2520':
		prodname = 'CGS 2520'
	elif prodcode == 'grwicdes':
		prodname = 'CGS Module'
	elif prodcode == 'csr1000v':
		prodname = 'CSR-1000V'
	elif prodcode == 'cva120':
		prodname = 'CVA-120'
	elif prodcode == 'cva120cvc':
		prodname = 'CVA-120'
	elif prodcode == 'cigesm':
		prodname = 'IBM Blade Switch'
	elif prodcode == 'ics7700':
		prodname = 'ICS-7700'
	elif prodcode == 'ie2000':
		prodname = 'IE-2000'
	elif prodcode == 'ie2000u':
		prodname = 'IE-2000U'
	elif prodcode == 'ies':
		prodname = 'IE-3000'
	elif prodcode == 'ie3010':
		prodname = 'IE-3010'
	elif prodcode == 'ie4000':
		prodname = 'IE-4000'
	elif prodcode == 'ie4010':
		prodname = 'IE-4010'
	elif prodcode == 'ie5000':
		prodname = 'IE-5000'
	elif prodcode == 'igs':
		prodname = 'IGS'
	elif prodcode == 'urm':
		prodname = 'IGX 8400'
	elif prodcode == 'vios':
		prodname = 'IOS-V'
	elif prodcode == 'iosxrv':
		prodname = 'IOS-XRV'
	elif prodcode == 'ir800':
		prodname = 'IR-800'
	elif prodcode == 'isr4200':
		prodname = 'ISR 4200'
	elif prodcode == 'isr4300':
		prodname = 'ISR 4300'
	elif prodcode == 'isr4400':
		prodname = 'ISR 4400'
	elif prodcode == 'ls1010':
		prodname = 'Lightspeed 1010'
	elif prodcode == 'mc3810':
		prodname = 'MC 3810'
	elif prodcode == 'mc3810':
		prodname = 'MC 3810'
	elif prodcode == 'm9100':
		prodname = 'MDS 9100'
	elif prodcode == 'm9200':
		prodname = 'MDS 9200'
	elif prodcode == 'm9250':
		prodname = 'MDS 9250'
	elif prodcode == 'm9500':
		prodname = 'MDS 9500'
	elif prodcode == 'm9700':
		prodname = 'MDS 9700'
	elif prodcode == 'me1200':
		prodname = 'ME 1200'
	elif prodcode == 'me240x':
		prodname = 'ME 2400'
	elif prodcode == 'me2600x':
		prodname = 'ME 2600X'
	elif prodcode == 'me340x':
		prodname = 'ME 3400'
	elif prodcode == 'me360x':
		prodname = 'ME 3600'
	elif prodcode == 'me380x':
		prodname = 'ME 3800'
	elif prodcode == 'rpm':
		prodname = 'MGX 8850'
	elif prodcode == 'rpmxf':
		prodname = 'MGX 8850'
	elif prodcode == 'mwr1900':
		prodname = 'MWR 1900'
	elif prodcode == 'mwr1941':
		prodname = 'MWR 1941'
	elif prodcode == 'mwr2941':
		prodname = 'MWR 2941'
	elif prodcode == 'n4000':
		prodname = 'Nexus 4000'
	elif prodcode == 'n5000':
		prodname = 'Nexus 5000'
	elif prodcode == 'n7000':
		prodname = 'Nexus 7000'
	elif prodcode == 'n7700':
		prodname = 'Nexus 7700'
	elif prodcode == 'ni2':
		prodname = 'NI-2'
	elif prodcode == 'ons15530':
		prodname = 'ONS 15530'
	elif prodcode == 'ons15540':
		prodname = 'ONS 15540'
	elif prodcode == 'rfgw':
		prodname = 'RF Gateway'
	elif prodcode == 'sb101':
		prodname = 'SB 101'
	elif prodcode == 'sb107':
		prodname = 'SB 107'
	elif prodcode == 'soho70':
		prodname = 'SOHO 70'
	elif prodcode == 'soho71':
		prodname = 'SOHO 71'
	elif prodcode == 'soho78':
		prodname = 'SOHO 78'
	elif prodcode == 'soho91':
		prodname = 'SOHO 91'
	elif prodcode == 'soho97':
		prodname = 'SOHO 97'
	elif prodcode == 'ubr10k':
		prodname = 'UBR 10000'
	elif prodcode == 'ubr7100':
		prodname = 'UBR 7100'
	elif prodcode == 'ubr7200':
		prodname = 'UBR 7200'
	elif prodcode == 'ubr7200p':
		prodname = 'UBR 7200-NPEG2'
	elif prodcode == 'ubr920':
		prodname = 'UBR 920'
	elif prodcode == 'ubr925':
		prodname = 'UBR 925'
	elif prodcode == 'ubr10k':
		prodname = 'UBR10000-PRE1'
	elif prodcode == 'ubr10k2':
		prodname = 'UBR10000-PRE2'
	elif prodcode == 'uc500':
		prodname = 'UC-500'
	elif prodcode == 'vg200':
		prodname = 'VG 200'
	elif prodcode == 'vg20x':
		prodname = 'VG 202'
	elif prodcode == 'vg20xxm':
		prodname = 'VG 20x XM'
	elif prodcode == 'vg224':
		prodname = 'VG 224'
	elif prodcode == 'vg3x0':
		prodname = 'VG 310-320'
	elif prodcode == 'vg350':
		prodname = 'VG 350'
	elif prodcode == 'vgd':
		prodname = 'VGD'
	else:
		prodname = 'UNKNOWN'
	return prodname


'''
Not Yet Implemented
def scriptusage ():
	print ("-h: This Help Messagen")
	print ("-d: Directory\n")
	print ("-m: Compute MD5 hash \(NYI\)\n")
'''


'''
Last Subroutine Called.
Should only be called by the various pathbuilder subroutines.
Used to Move the current file
from the current location to the final location
'''
def filemove (newpath, filename):
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	try:
		shutil.move(filename, newpath)
	except:
		print("There is a file with the same name at the destination!.")
'''
Subroutine that builds the final directory paths.
The various pathbuilder subroutines are the only subroutines that should
be calling filemove.
'''
def pathbuilder_mainver_fullver_imagecode (filename, model, mainver, fullver, imagecode):
	filepath = model + '/' + mainver + '/' + fullver + '/' + imagecode
	filemove (filepath, filename)

def pathbuilder_mainver_fullver (filename, model, mainver, fullver):
	filepath = model + '/' + mainver + '/' + fullver
	filemove (filepath, filename)

def pathbuilder_fullver (filename, model, fullver):
	filepath = model + '/' + fullver
	filemove (filepath, filename)


#Used to join four separate strings into one string.
#Produces the following format
# A.B(C)D
def stitch_4_cisco_standard (a,b,c,d):
	version = a + '.' + b + '(' + c + ')' + d
	return version

#Used to join four separate strings into one string.
#Produces the following format
# A.B.C.D
def stitch_4_dot (a,b,c,d):
	version = a + '.' + b + '.' + c + '.' + d
	return version

#Used to join four separate strings into one string.
#Produces the following format
# A.B(C)
def stitch_3_cisco_standard (a,b,c):
	version = a + '.' + b + '(' + c + ')'
	return version

#Used to join three separate strings into one string.
#Produces the following format
# ABC
def stitch_3_whole (a,b,c):
	version = a + b + c
	return version

#Used to join three separate strings into one string.
#Produces the following format
# A.B.C
def stitch_3_dot (a,b,c):
	version = a + '.' + b + '.' + c
	return version

#Used to join two separate strings into one string.
#Produces the following format
# A.B
def stitch_2_dot (a,b):
	version = a + '.' + b
	return version

#Used to join two separate strings into one string.
#Produces the following format
# AB
def stitch_2_whole (a,b):
	version = a + b
	return version


def asamastersub(filename):
	
	#Determining which ASA Sub function to send to the file to for processing.
	if filename.startswith('asa-restapi'):
		asarestapisub(filename)
	elif filename.startswith('asav'):
		asavsub(filename)
	elif filename.endswith('lfbff-k8.SPA'):
		asafpsub(filename)

#All Other ASA Code
def asasub(filename):
	splitbydash = filename.split('-')


#ASA with Firepower Services
def asafpsub(filename):
	name = filename.lstrip('asa')
	name = name.rstrip('-lfbff-k8.SPA')
	#print (name, end='\n')
	namenumbers = list(name)
	if len (name) == 5:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		fullversion = stitch_4_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2],namenumbers[4])
		pathbuilder_mainver_fullver (filename,"ASA/ASA-Firepower-Services",twoversion,fullversion)
	elif len (name) == 6:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		buildversion = stitch_2_whole (namenumbers[4],namenumbers[5])
		fullversion = stitch_2_whole (threeversion,buildversion)
		pathbuilder_mainver_fullver (filename,"ASA/ASA-Firepower-Services",twoversion,fullversion)
	elif len (name) == 3:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		pathbuilder_mainver_fullver (filename,"ASA/ASA-Firepower-Services",twoversion,threeversion)
	elif len (name) == 7:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		buildversion = stitch_3_whole (namenumbers[4],namenumbers[5],namenumbers[6])
		fullversion = stitch_2_whole (threeversion,buildversion)
		pathbuilder_mainver_fullver (filename,"ASA/ASA-Firepower-Services",twoversion,fullversion)


#ASA Virtual
def asavsub(filename):
	name = filename.lstrip('asav')
	name = name.rstrip('vhdx')
	name = name.rstrip('zip')
	name = name.rstrip('qcow2')
	name = name.rstrip('ova')
	name = name.rstrip('.')
	name = name.strip()
	namenumbers = list(name)
	if len (name) == 5:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		fullversion = stitch_4_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2],namenumbers[4])
		pathbuilder_mainver_fullver (filename,"ASA/ASAV",twoversion,fullversion)
	elif len (name) == 6:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		buildversion = stitch_2_whole (namenumbers[4],namenumbers[5])
		fullversion = stitch_2_whole (threeversion,buildversion)
		pathbuilder_mainver_fullver (filename,"ASA/ASAV",twoversion,fullversion)
	elif len (name) == 3:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		pathbuilder_mainver_fullver (filename,"ASA/ASAV",twoversion,threeversion)
	elif len (name) == 7:
		twoversion = stitch_2_dot (namenumbers[0],namenumbers[1])
		threeversion = stitch_3_cisco_standard (namenumbers[0],namenumbers[1],namenumbers[2])
		buildversion = stitch_3_whole (namenumbers[4],namenumbers[5],namenumbers[6])
		fullversion = stitch_2_whole (threeversion,buildversion)
		pathbuilder_mainver_fullver (filename,"ASA/ASAV",twoversion,fullversion)


def asarestapisub(filename):
	splitbydash = filename.split('-')
	#splitbydash should now have 5 entries (0-4)
	versionlist = list(splitbydash[2])
	if len (versionlist) == 6:
		buildstring = stitch_3_whole (versionlist[3],versionlist[4],versionlist[5])
		mainver = stitch_2_dot (versionlist[0],versionlist[1])
		fullver = stitch_4_dot (versionlist[0],versionlist[1],versionlist[2],buildstring)
		pathbuilder_fullver(filename,"ASA/REST-API",fullver)
	elif len (versionlist) == 3:
		mainver = stitch_2_dot (versionlist[0],versionlist[1])
		fullver = stitch_3_dot (versionlist[0],versionlist[1],versionlist[2])
		pathbuilder_fullver(filename,"ASA/REST-API",fullver)


def asdmsub(filename):
	splitbydash = filename.split('-')


def mainloop (sourcedir):
	#Main Subroutine
	#Classifies Files based on name 
	#and information returned from the three lookups.
	
#	src = sys.argv[1]
	names = os.listdir(sourcedir)
	os.chdir(sourcedir)
	for name in names:
		if os.path.isdir(name):
			continue
		name = name.rstrip()
			
		if name.endswith('.part'):
			continue
		elif name == "Thumbs.db":
			continue
		elif name == ".DS_Store":
			continue
		elif name == ".DS_Store.hash":
			continue
		elif name.endswith('pdf'):
			continue
		
		print(name)
		
		#Split Filename to permit classification
		splitbydot = name.split('.')
		splitbydash = name.split('-')
		
		#Gather the First 3 Characters of the filname to 
		#detect platforms that don't have an easy method of spliting filenames.
		#e.g Cisco ASA
#		chars3 = name[0:3]
		#e.g Cisco ASAv
#		chars4 = name[0:4]
		
		if name.startswith('asa'):
			asamastersub(name)
		elif name.startswith('asdm'):
			asamastersub(name)

if __name__ == "__main__":
	mainloop(sys.argv[1])
