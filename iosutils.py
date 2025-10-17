import os
import re
import shutil
import logging
import warnings
from typing import Optional

def filemove(new_path, file_name):
    """Move a file to a new directory, creating the directory if it doesn't exist."""
    os.makedirs(new_path, exist_ok=True)
    
    try:
        shutil.move(file_name, new_path)
        logging.debug(f"File '{file_name}' to '{new_path}'")
    except Exception as e:
        logging.debug(f"Unable to move file '{file_name}' to '{new_path}': {e}")


def iostrain(train, version):
    prefixes = [
        "AA", "AX", "AY", "AZ", "BC", "BT", "BW", "BX", "BY", "B",
        "CX", "CY", "CZ", "DA", "DB", "DC", "DD", "DX",
        "EA", "EB", "EC", "ED", "EH", "EJ", "EK", "EO", "EU", "EV", "EWA", "EW", "EX", "EY", "EZ", "E",
        "FX", "FY", "FZ",
        "GA", "GB", "GCA", "GC",
        "IRA", "IRB", "IRC", "IRD", "IRE", "IRF", "IRG", "IRH", "IRI",
        "IXA", "IXB", "IXC", "IXD", "IXE", "IXF", "IXG", "IXH",
        "JAL", "JAM", "JAN", "JAO", "JAX", "JAY", "JAZ", "JAB", "JA",
        "JBA", "JBB", "JBC", "JBD", "JBE", "JB",
        "JCA", "JCB", "JCC", "JCD", "JCE", "JC",
        "JDA", "JDB", "JDC", "JDD", "JD",
        "JEA", "JEB", "JEC", "JED", "JEE", "JE",
        "JFA", "JFB", "JFC", "JFD", "JF",
        "JGA", "JGB", "JGC", "JGD", "JG",
        "JHA", "JHB", "JHC", "JH",
        "JI", "JJ", "JK", "JL",
        "JMA", "JMB", "JMC", "JM",
        "JN", "JX",
        "JPA", "JPB", "JPC", "JPD", "JPE", "JPF", "JPG", "JPH", "JPI", "JPJ", "JPK", "JPL", "JPM", "JPN", "JPO", "JPP", "JPQ", "JPR", "JPS", "JPT", "JPU", "JPV", "JPW", "JPX", "JPY", "JPZ", "JP",
        "JY",
        "L",
        "MB", "MC", "MDA", "MDB", "MD",
        "MIG", "MRA", "MRB", "MR", "MX", "M",
        "NA", "N",
        "PBAS", "PBA", "PBS", "PB", "PC", "PIX", "PI", "P",
        "SBA", "SBB", "SBC", "SBY", "SB",
        "SCA", "SCB", "SCC", "SCD", "SCE", "SCF", "SCG", "SCH", "SCI", "SCJ", "SCK", "SCL", "SCM", "SC",
        "SEA", "SEB", "SEC", "SED", "SEE", "SEF", "SEG", "SE",
        "SGA", "SG",
        "SRA", "SRB", "SRC", "SRD", "SRE", "SR",
        "SL", "SM",
        "SNG", "SNH", "SNI", "SN", "SO", "SP", "SQ",
        "SS",
        "STE", "ST",
        "SU",
        "SVA", "SVB", "SVC", "SVD", "SVE", "SVF", "SV",
        "SW",
        "SXA", "SXB", "SXD", "SXE", "SXF", "SXH", "SXI", "SXJ", "SX",
        "SYA", "SYL", "SY", "SZ", "S",
        "TPC", "TO", "T",
        "UZ", "VZ",
        "WC", "WO", "WX",
        "XA", "XB", "XC", "XD", "XE", "XF", "XG", "XH", "XI", "XJ", "XK", "XL", "XM",
        "XNA", "XNB", "XNC", "XND", "XNE",
        "XO", "XP", "XQ", "XR", "XS", "XT", "XU", "XV", "XW", "XX", "XY", "XZ",
        "YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YI", "YJ", "YK", "YL", "YM", "YN", "YO", "YP", "YQ", "YR", "YS", "YT", "YU", "YV", "YW", "YX", "YZ",
        "ZYA", "ZY", "ZZ",
        "ZA", "ZB", "ZC", "ZD", "ZE", "ZF", "ZG", "ZH", "ZI", "ZJ", "ZK", "ZL", "ZN", "ZO", "ZP", "ZQ", "ZR", "ZS", "ZT", "ZU", "ZV", "ZW", "ZX"
    ]

    for prefix in prefixes:
        if train.startswith(prefix):
            return version + prefix
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
        "cisco9k_iosxe": "UNIVERSAL",
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
        "install-esxi":  "INSTALL-ESXi",
        "install-nfvis": "INSTALL-NFVIS",
        "install-kvm":   "INSTALL-KVM",
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
        "pagent": "PACKET GENERATOR",
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
        "y7": "IP-ADSL",
        "ncs500x-nV": "NCS500x-SATELLITE",
        "vsm": "Virtual Services Module",
    }
    return imagecode_to_subdirectory.get(imagecode, "UNKNOWN")

def product(prodcode):
    prod_map = {
        "apicem": "NETWORK-MANAGEMENT/APIC-EM",
        "cspc": "NETWORK-MANAGEMENT/COMMON-SERVICES-PLATFORM-COLLECTOR",
        "ccp": "NETWORK-MANAGEMENT/CONFIGURATION-PROFESSIONAL",
        "ccpc": "NETWORK-MANAGEMENT/CONFIGURATION-PROFESSIONAL-CATALYST",
        "cpi": "NETWORK-MANAGEMENT/CISCO-PRIME-INFRASTRUCTURE",
        "dnac": "NETWORK-MANAGEMENT/DNA-CENTER",
        "ttam": "NETWORK-MANAGEMENT/DNA-CENTER-TRAFFIC",
        "cna": "NETWORK-MANAGEMENT/NETWORK-ASSISTANT",
        "SSM_On-Prem": "NETWORK-MANAGEMENT/SMART LICENSE ON-PREM",
        "ntwkmgmt": "NETWORK-MANAGEMENT",
        "cworks": "NETWORK-MANAGEMENT/CiscoWorks",
        "c1100tg": "NETWORK-MANAGEMENT/TERMINAL-SERVICES-GATEWAY",
        "perfigocca": "NETWORK-MANAGEMENT/CISCO-CLEAN-ACCESS",
        "cml": "NETWORK-MANAGEMENT/MODELING-LABS",
        "cmlf": "NETWORK-MANAGEMENT/MODELING-LABS-FREE",
        "refplat": "NETWORK-MANAGEMENT/MODELING-LABS-REFERENCE-PLATFORM",
        "cimcs": "SERVERS/CIMC-SUPERVISOR",
        "routers": "ROUTERS",
        "ir1800": "ROUTERS/INDUSTRIAL/IR18XX",
        "ir8100": "ROUTERS/INDUSTRIAL/IR8100",
        "ir8340": "ROUTERS/INDUSTRIAL/IR8340",
        "ons15530": "ROUTERS/OPTICAL/ONS-15530",
        "ons15540": "ROUTERS/OPTICAL/ONS-15540",
        "asr1000": "ROUTERS/ASR/ASR-1000",
        "isrg3moduleslte": "ROUTERS/ISRG3/MODULES/LTE",
        "iosxeissumatrix": "ROUTERS/IOS-XE-ISSU-MATRIX",
        "iou": "ROUTERS/IOU",
        "asr1000rp1": "ROUTERS/ASR/ASR-1000-RP1",
        "asr1000rp2": "ROUTERS/ASR/ASR-1000-RP2",
        "asr1000rpx86": "ROUTERS/ASR/ASR-1000-RP3",
        "asr1000hx": "ROUTERS/ASR/ASR-1000HX",
        "asr1001": "ROUTERS/ASR/ASR-1001",
        "asr1001x": "ROUTERS/ASR/ASR-1001X",
        "asr1002": "ROUTERS/ASR/ASR-1002",
        "asr1002x": "ROUTERS/ASR/ASR-1002X",
        "asr1002hx": "ROUTERS/ASR/ASR-1002HX",
        "asr900": "ROUTERS/ASR/ASR-900",
        "asr9k": "ROUTERS/ASR/ASR-9000",
        "asr900rsp1": "ROUTERS/ASR/ASR-900-RSP1",
        "asr900rsp2": "ROUTERS/ASR/ASR-900-RSP2",
        "asr900rsp3": "ROUTERS/ASR/ASR-900-RSP3",
        "asr901": "ROUTERS/ASR/ASR-901",
        "asr901rsp1": "ROUTERS/ASR/ASR-901-RSP1",
        "asr901rsp2": "ROUTERS/ASR/ASR-901-RSP2",
        "asr901_sat": "ROUTERS/ASR/ASR-901-SAT",
        "asr901sec": "ROUTERS/ASR/ASR-901-SEC",
        "asr903": "ROUTERS/ASR/ASR-903",
        "asr903rsp1": "ROUTERS/ASR/ASR-903-RSP1",
        "asr903rsp2": "ROUTERS/ASR/ASR-903-RSP2",
        "asr920": "ROUTERS/ASR/ASR-920",
        "asr920igp": "ROUTERS/ASR/ASR-920IGP",
        "ncs540": "ROUTERS/NCS/NCS-540",
        "urm": "ROUTERS/ATM/IGX-8400",
        "rpm": "ROUTERS/ATM/MGX-8850",
        "rpmxf": "ROUTERS/ATM/MGX-8850",
        "sdwan": "ROUTERS/SD-WAN",
        "c600": "ROUTERS/BRANCH/600",
        "c800": "ROUTERS/BRANCH/800",
        "c805": "ROUTERS/BRANCH/805",
        "c806": "ROUTERS/BRANCH/806",
        "c815": "ROUTERS/BRANCH/815",
        "c820": "ROUTERS/BRANCH/820",
        "c827v": "ROUTERS/BRANCH/827",
        "c828": "ROUTERS/BRANCH/828",
        "c831": "ROUTERS/BRANCH/831",
        "c836": "ROUTERS/BRANCH/836",
        "c837": "ROUTERS/BRANCH/837",
        "c1004": "ROUTERS/BRANCH/1004",
        "c1005": "ROUTERS/BRANCH/1005",
        "cpa1005": "ROUTERS/BRANCH/1005",
        "c1400": "ROUTERS/BRANCH/1400",
        "c1600": "ROUTERS/BRANCH/1600",
        "c1700": "ROUTERS/BRANCH/1700",
        "c1710": "ROUTERS/BRANCH/1710",
        "c2500": "ROUTERS/BRANCH/2500",
        "igs": "ROUTERS/BRANCH/2500",
        "c25fx": "ROUTERS/BRANCH/2500",
        "c2511": "ROUTERS/BRANCH/2500",
        "c2600": "ROUTERS/BRANCH/2600",
        "c2611": "ROUTERS/BRANCH/2600",
        "c2691": "ROUTERS/BRANCH/2691",
        "c3620": "ROUTERS/BRANCH/3620",
        "c3631": "ROUTERS/BRANCH/3631",
        "c3640": "ROUTERS/BRANCH/3640",
        "c3660": "ROUTERS/BRANCH/3660",
        "c3725": "ROUTERS/BRANCH/3725",
        "c3745": "ROUTERS/BRANCH/3745",
        "c4000": "ROUTERS/BRANCH/4000",
        "c4500": "ROUTERS/BRANCH/4700M",
        "mc3810": "ROUTERS/BRANCH/MC-3810",
        "branchmodules": "ROUTERS/BRANCH/MODULES",
        "ni2": "ROUTERS/BROADBAND/NI-2",
        "rfgw": "ROUTERS/BROADBAND/RF-Gateway 1",
        "rfgwk10": "ROUTERS/BROADBAND/RF-Gateway 10",
        "sb101": "ROUTERS/BROADBAND/SB-101",
        "sb107": "ROUTERS/BROADBAND/SB-107",
        "ubr920": "ROUTERS/BROADBAND/UBR-920",
        "ubr925": "ROUTERS/BROADBAND/UBR-925",
        "ubr10k": "ROUTERS/BROADBAND/UBR-10000/PRE1",
        "ubr10k2": "ROUTERS/BROADBAND/UBR-10000/PRE2",
        "ubr10k3": "ROUTERS/BROADBAND/UBR-10000/PRE3",
        "ubr10k4": "ROUTERS/BROADBAND/UBR-10000/PRE4",
        "ubr10k5": "ROUTERS/BROADBAND/UBR-10000/PRE5",
        "ubr7100": "ROUTERS/BROADBAND/UBR-7100",
        "ubr7200": "ROUTERS/BROADBAND/UBR-7200/NPEG1",
        "ubr7200p": "ROUTERS/BROADBAND/UBR-7200/NPEG2",
        "cva120": "ROUTERS/CABLE/CVA-120",
        "cva120cvc": "ROUTERS/CABLE/CVA-120",
        "esr6300": "ROUTERS/EMBEDDED/ESR-6300",
        "c5915": "ROUTERS/EMBEDDED/5915",
        "c5921i86": "ROUTERS/EMBEDDED/5921",
        "c5921i86v": "ROUTERS/EMBEDDED/5921",
        "c5940": "ROUTERS/EMBEDDED/5940",
        "c5930": "ROUTERS/EMBEDDED/5930",
        "ie9k": "SWITCHES/INDUSTRIAL-ETHERNET/CATALYST-9300-INDUSTRIAL",
        "cgr2010": "ROUTERS/GRID/CGR-2010",
        "soho70": "ROUTERS/HOME-SMALL-BUSINESS/SOHO-70",
        "soho71": "ROUTERS/HOME-SMALL-BUSINESS/SOHO-71",
        "soho78": "ROUTERS/HOME-SMALL-BUSINESS/SOHO-78",
        "soho91": "ROUTERS/HOME-SMALL-BUSINESS/SOHO-91",
        "soho97": "ROUTERS/HOME-SMALL-BUSINESS/SOHO-97",
        "igs": "ROUTERS/IGS",
        "iosxe-sd-avc": "ROUTERS/IOSXE-AVC",
        "iosxe-remote-mgmt": "ROUTERS/IOSXE-REMOTE-MGMT",
        "c180x": "ROUTERS/ISRG1/1800",
        "c1805": "ROUTERS/ISRG1/1805",
        "c181x": "ROUTERS/ISRG1/1810",
        "c1841": "ROUTERS/ISRG1/1841",
        "c1841c": "ROUTERS/ISRG1/1841-CHINA",
        "c1841ve": "ROUTERS/ISRG1/1841-VE",
        "c1861": "ROUTERS/ISRG1/1861",
        "c2800nm": "ROUTERS/ISRG1/2800nm",
        "c2800nmc": "ROUTERS/ISRG1/2800nm-CHINA",
        "c2800nmve": "ROUTERS/ISRG1/2800nmve",
        "c2801": "ROUTERS/ISRG1/2801",
        "c2801c": "ROUTERS/ISRG1/2801-CHINA",
        "c3825": "ROUTERS/ISRG1/3825",
        "c3825c": "ROUTERS/ISRG1/3825-CHINA",
        "c3825nv": "ROUTERS/ISRG1/3825-NO-VPN",
        "c3845": "ROUTERS/ISRG1/3845",
        "c3845c": "ROUTERS/ISRG1/3845-CHINA",
        "c3845nv": "ROUTERS/ISRG1/3845-NO-VPN",
        "c850": "ROUTERS/ISRG1/850",
        "c860": "ROUTERS/ISRG1/860",
        "c870": "ROUTERS/ISRG1/870",
        "c871": "ROUTERS/ISRG1/871",
        "c890": "ROUTERS/ISRG1/890",
        "ISRG1GENERIC": "ROUTERS/ISRG1/MODULES",
        "c1900": "ROUTERS/ISRG2/1900",
        "c1900-2900": "ROUTERS/ISRG2/1900-2900",
        "c1900c":  "ROUTERS/ISRG2/1900-CHINA",
        "c2900":   "ROUTERS/ISRG2/2900",
        "c2911a":  "ROUTERS/ISRG2/2911a",
        "c2951":   "ROUTERS/ISRG2/2951",
        "c3900":   "ROUTERS/ISRG2/3900",
        "c3900e":  "ROUTERS/ISRG2/3900E",
        "c800m":   "ROUTERS/ISRG2/800m",
        "c800j":   "ROUTERS/ISRG2/800J",
        "c860vae": "ROUTERS/ISRG2/860-VAE",
        "c860vae2": "ROUTERS/ISRG2/860-VAE2",
        "c860vaej": "ROUTERS/ISRG2/860-VAEJ",
        "c860vaew": "ROUTERS/ISRG2/860-VAEW",
        "c880data": "ROUTERS/ISRG2/880",
        "c880voice": "ROUTERS/ISRG2/880-CUBE",
        "c890s": "ROUTERS/ISRG2/890",
        "c900": "ROUTERS/ISRG2/900",
        "ISRG2GENERIC": "ROUTERS/ISRG2/MODULES",
        "c800g2": "ROUTERS/ISRG2/800",
        "c800g3": "ROUTERS/ISRG3/800",
        "ir1101": "ROUTERS/INDUSTRIAL/IR-1101",
        "ir800": "ROUTERS/INDUSTRIAL/IR-800",
        "c1000router": "ROUTERS/BRANCH/1000",
        "c1100router": "ROUTERS/ISRG3/ISR-1100",
        "isr1100be": "ROUTERS/ISRG3/ISR-1100X",
        "isr4200": "ROUTERS/ISRG3/ISR-4200",
        "isr4200-4300": "ROUTERS/ISRG3/ISR-4200-4300",
        "isr4300": "ROUTERS/ISRG3/ISR-4300",
        "isr4400": "ROUTERS/ISRG3/ISR-4400",
        "isr4400v2": "ROUTERS/ISRG3/ISR-4461",
        "mwr1900": "ROUTERS/MOBILE/MWR-1900",
        "mwr1941": "ROUTERS/MOBILE/MWR-1941",
        "mwr2941": "ROUTERS/MOBILE/MWR-2941",
        "c3201": "ROUTERS/RUGGED/3201-AP",
        "c3202": "ROUTERS/RUGGED/3202-AP",
        "c3205": "ROUTERS/RUGGED/3205-AP",
        "c3220": "ROUTERS/RUGGED/3220",
        "c3230": "ROUTERS/RUGGED/3230",
        "c3250": "ROUTERS/RUGGED/3250",
        "c3270": "ROUTERS/RUGGED/3270",
        "ncs4201":  "ROUTERS/SP/NCS4201",
        "ncs4202":  "ROUTERS/SP/NCS4202",
        "c81g2be":  "ROUTERS/Secure 8000/Secure 8100 - Gen 2",
        "c8kg2be":  "ROUTERS/Secure 8000/Secure 8200-8300 - Gen 2",
        "c84g2aes": "ROUTERS/Secure 8000/Secure 8400 - Gen 2",
        "c10k":     "ROUTERS/SP/10000/PRE1",
        "c10k2":    "ROUTERS/SP/10000/PRE2",
        "c10k3":    "ROUTERS/SP/10000/PRE3",
        "c10k4":    "ROUTERS/SP/10000/PRE4",
        "c10700":   "ROUTERS/SP/10700",
        "c12k":     "ROUTERS/SP/12000",
        "c12kprp":  "ROUTERS/SP/12000",
        "gsr":      "ROUTERS/SP/12000",
        "XR12000":  "ROUTERS/SP/12000-XR",
        "c7000":    "ROUTERS/SP/7000",
        "c7100":    "ROUTERS/SP/7100",
        "c7200":    "ROUTERS/SP/7200/NPEG1",
        "c7200p":   "ROUTERS/SP/7200/NPEG2",
        "c7300":    "ROUTERS/SP/7300",
        "c7301":    "ROUTERS/SP/7301",
        "c7304":    "ROUTERS/SP/7304",
        "spa":      "ROUTERS/SP/7304",
        "c7400":    "ROUTERS/SP/7400",
        "rsp":      "ROUTERS/SP/7500",
        "c7600":    "ROUTERS/SP/7600",
        "c7600rsp72043": "ROUTERS/SP/7600/RSP720",
        "rsp72043": "ROUTERS/SP/7600/RSP720",
        "c7svcsami": "ROUTERS/SP/7600/SAMI",
        "c7600s3223": "ROUTERS/SP/7600/SUP-32",
        "c7600s72033": "ROUTERS/SP/7600/SUP-720",
        "8000": "ROUTERS/SP/8000",
        "csr1000v": "ROUTERS/VIRTUAL/CSR-1000V",
        "csr1000v_milplr": "ROUTERS/VIRTUAL/CSR-1000V",
        "vios": "ROUTERS/VIRTUAL/IOS-V",
        "iosxrvdemo": "ROUTERS/VIRTUAL/IOS-XRv",
        "iosxrvfull": "ROUTERS/VIRTUAL/IOS-XRv9000",
        "xrvcontainer": "ROUTERS/VIRTUAL/IOS-XRv-CONTAINER",
        "csa":                 "SECURITY/CISCO-SECURITY-AGENT",
        "csm":                 "SECURITY/CISCO-SECURITY-MANAGER",
        "asa":                 "SECURITY/FIREWALL/ASA",
        "asacx":               "SECURITY/FIREWALL/ASA-CX-MODULE",
        "c6svc-fwm":           "SECURITY/FIREWALL/CATALYST-6500-FWSM",
        "firepower":           "SECURITY/FIREWALL/FirePOWER",
        "firepower1k":         "SECURITY/FIREWALL/FirePOWER/FIREPOWER-1xxx",
        "firepower2k":         "SECURITY/FIREWALL/FirePOWER/FIREPOWER-2xxx",
        "firepower3k":         "SECURITY/FIREWALL/FirePOWER/FIREPOWER-3xxx",
        "firepower4k9k":       "SECURITY/FIREWALL/FirePOWER/FIREPOWER-4xxx-9xxx",
        "firepower4200":       "SECURITY/FIREWALL/FirePOWER/FIREPOWER-42xx",
        "firepowerisa3000":    "SECURITY/FIREWALL/FirePOWER/ISA-3000",
        "firepowertd":         "SECURITY/FIREWALL/FirePOWER/VIRTUAL-FIREWALL",
        "firepowerfmc":        "SECURITY/FIREWALL/FirePOWER/FIREPOWER-MANAGEMENT-CENTER",
        "pix":      "SECURITY/FIREWALL/PIX",
        "acs":      "SECURITY/IDENTITY/ACS",
        "ise":      "SECURITY/IDENTITY/IDENTITY-SERVICES-ENGINE",
        "isepic":   "SECURITY/IDENTITY/IDENTITY-SERVICES-ENGINE-PIC",
        "ciscoutd": "SECURITY/IOS-XE-UTD",
        "ipsids":   "SECURITY/IDS-IPS",
        "ipsidsnm": "ROUTER-NM",
        "ipsidsasa5585xssp10": "ASA5585-X-SSP_10",
        "ipsidsasa5585xssp20": "ASA5585-X-SSP_20",
        "ipsidsasa5585xssp40": "ASA5585-X-SSP_40",
        "ipsidsasa5585xssp60": "ASA5585-X-SSP_60",
        "ipsidsasa5512xssp": "ASA5512-X",
        "ipsidsasa5515xssp": "ASA5515-X",
        "ipsidsasa5525xssp": "ASA5525-X",
        "ipsidsasa5545xssp": "ASA5545-X",
        "ipsidsasa5555xssp": "ASA5555-X",
        "ipsidsasassc":   "ASA-AIPSSC",
        "ipsidsasassm10": "ASA-AIPSSM-10",
        "ipsidsasassm20": "ASA-AIPSSM-20",
        "ipsidsasassm40": "ASA-AIPSSM-40",
        "ipsidsipsadsm2": "IPS-Catalyst-6500-IDSM2",
        "ipsidsipsaim":   "IPS-AIM",
        "ipsidsips4215":  "IPS-4215",
        "ipsidsips4240":  "IPS-4240",
        "ipsidsips4255":  "IPS-4255",
        "ipsidsips4260":  "IPS-4260",
        "ipsidsips4270":  "IPS-4270",
        "ipsidsips4345":  "IPS-4345",
        "ipsidsips4360":  "IPS-4360",
        "ipsidsips4510":  "IPS-4510",
        "ipsidsips4520":  "IPS-4520",
        "iosids":         "SECURITY/IOS-IDS",
        "ironport":       "SECURITY/IRONPORT",
        "mars":           "SECURITY/MARS",
        "vpn3000":        "SECURITY/VPN-3000",
        "anyconnect":     "SECURITY/VPN-CLIENTS/ANYCONNECT (CISCO SECURE CLIENT)",
        "vpnclient":      "SECURITY/VPN-CLIENTS/IPSEC-CLIENT",
        "aci":            "SERVERS/APIC",
        "css":            "SERVERS/CSS",
        "dcnm":           "SERVERS/DATA-CENTER-NETWORK-MANAGER",
        "dnac":           "SERVERS/DNAC",
        "hyperflex":      "SERVERS/HYPERFLEX",
        "onepk":          "SERVERS/ONE-PK",
        "ucsgeneric":     "SERVERS/UCS",
        "smallbusiness":  "Small-Business",
        "c125":           "SERVERS/UCS/C-SERIES/C125M5",
        "c200":           "SERVERS/UCS/C-SERIES/C200M1-C200M2-C210M1-C210M2",
        "c220":           "SERVERS/UCS/C-SERIES/C220M3",
        "c220m4":         "SERVERS/UCS/C-SERIES/C220M4",
        "c220m5":         "SERVERS/UCS/C-SERIES/C220M5",
        "c220m6":         "SERVERS/UCS/C-SERIES/C220M6",
        "c220m7":         "SERVERS/UCS/C-SERIES/C220M7",
        "c225m6":         "SERVERS/UCS/C-SERIES/C225M6",
        "c225m8":         "SERVERS/UCS/C-SERIES/C225M8",
        "c2x":            "SERVERS/UCS/C-SERIES/C22M3-C22M4",
        "c240":           "SERVERS/UCS/C-SERIES/C240M3",
        "c240m4": "SERVERS/UCS/C-SERIES/C240M4",
        "c240m5": "SERVERS/UCS/C-SERIES/C240M5",
        "c240m6": "SERVERS/UCS/C-SERIES/C240M6",
        "c240m7": "SERVERS/UCS/C-SERIES/C240M7",
        "c245m6": "SERVERS/UCS/C-SERIES/C245M6",
        "c245m8": "SERVERS/UCS/C-SERIES/C245M8",
        "c250": "SERVERS/UCS/C-SERIES/C250M1-C250M2",
        "c260": "SERVERS/UCS/C-SERIES/C260M2",
        "c2xxm3": "SERVERS/UCS/C-SERIES/C2XXM3",
        "c2xxm4": "SERVERS/UCS/C-SERIES/C2XXM4",
        "c2xxm5": "SERVERS/UCS/C-SERIES/C2XXM5",
        "c2xxm6": "SERVERS/UCS/C-SERIES/C2XXM6",
        "c2xxm7": "SERVERS/UCS/C-SERIES/C2XXM7",
        "c3160": "SERVERS/UCS/C-SERIES/C3160",
        "c3260": "SERVERS/UCS/C-SERIES/C3260",
        "c420": "SERVERS/UCS/C-SERIES/C420M3",
        "c460": "SERVERS/UCS/C-SERIES/C460M1-C460M2",
        "c460m4": "SERVERS/UCS/C-SERIES/C460M4",
        "c480m5": "SERVERS/UCS/C-SERIES/C480M5",
        "ucsbseries": "SERVERS/UCS/B-SERIES/",
        "ucscseries": "SERVERS/UCS/C-SERIES/",
        "ucseseries": "SERVERS/UCS/E-SERIES/",
        "e100": "SERVERS/UCS/E-SERIES/E1XX",
        "ucs": "SERVERS/UCS/",
        "c6400r": "SERVICE-GATEWAY/6400-NSP",
        "c6400r2sp": "SERVICE-GATEWAY/6400-NSP",
        "c6400s":  "SERVICE-GATEWAY/6400-NSP",
        "ni2":     "SERVICE-GATEWAY/6XXX-DSL-Switch",
        "m9100":   "STORAGE/MDS-9100",
        "m9200":   "STORAGE/MDS-9200",
        "m9250":   "STORAGE/MDS-9250",
        "m9500":   "STORAGE/MDS-9500",
        "m9700":   "STORAGE/MDS-9700",
        "ls1010":  "SWITCHES/ATM/Lightspeed-1010",
        "cbs30x0": "SWITCHES/BLADE-SWITCHES/CATALYST-3000-DELL-Blade",
        "cbs31x0": "SWITCHES/BLADE-SWITCHES/CATALYST-3100-DELL-Blade",
        "cigesm":  "SWITCHES/BLADE-SWITCHES/IBM-Blade-Switch",
        "cgesm":   "SWITCHES/BLADE-SWITCHES/IBM-Blade-Switch",
        "cmicr":   "SWITCHES/CATALYST/Catalyst-Micro-Switches",
        "cat1200": "SWITCHES/CATALYST/Catalyst-1200",
        "cat1600": "SWITCHES/CATALYST/Catalyst-1600",
        "cat1900": "SWITCHES/CATALYST/Catalyst-1900",
        "c2350":   "SWITCHES/CATALYST/Catalyst-2350",
        "c2360":   "SWITCHES/CATALYST/Catalyst-2360",
        "cat2800": "SWITCHES/CATALYST/Catalyst-2800",
        "c2800":   "SWITCHES/CATALYST/Catalyst-2800",
        "c29atm":  "SWITCHES/CATALYST/Catalyst-2900-ATM",
        "c2900XL": "SWITCHES/CATALYST/Catalyst-2900XL",
        "c2900xl": "SWITCHES/CATALYST/Catalyst-2900XL",
        "c2918":   "SWITCHES/CATALYST/Catalyst-2918",
        "c2928":   "SWITCHES/CATALYST/Catalyst-2928",
        "c2940":   "SWITCHES/CATALYST/Catalyst-2940",
        "cat2948g": "SWITCHES/CATALYST/Catalyst-2948G",
        "c2950":    "SWITCHES/CATALYST/Catalyst-2950",
        "c2950lre": "SWITCHES/CATALYST/Catalyst-2950-LRE",
        "c2955":   "SWITCHES/CATALYST/Catalyst-2955",
        "c2960":   "SWITCHES/CATALYST/Catalyst-2960",
        "c2960l":  "SWITCHES/CATALYST/Catalyst-2960L",
        "c2960s":  "SWITCHES/CATALYST/Catalyst-2960S",
        "c2960x":  "SWITCHES/CATALYST/Catalyst-2960X",
        "c2970":   "SWITCHES/CATALYST/Catalyst-2970",
        "c2975":   "SWITCHES/CATALYST/Catalyst-2975",
        "cat3000": "SWITCHES/CATALYST/Catalyst-3000",
        "c3500xl": "SWITCHES/CATALYST/Catalyst-3500XL",
        "c3500XL": "SWITCHES/CATALYST/Catalyst-3500XL",
        "c3550":   "SWITCHES/CATALYST/Catalyst-3550",
        "c3560":   "SWITCHES/CATALYST/Catalyst-3560",
        "c3560e": "SWITCHES/CATALYST/Catalyst-3560E",
        "c3560x": "SWITCHES/CATALYST/Catalyst-3560X",
        "c3750": "SWITCHES/CATALYST/Catalyst-3750",
        "c3750e": "SWITCHES/CATALYST/Catalyst-3750E",
        "c3750me": "SWITCHES/METRO/Catalyst-3750ME",
        "c3750x": "SWITCHES/CATALYST/Catalyst-3750X",
        "cat3k_caa": "SWITCHES/CATALYST/Catalyst-3850-3650",
        "cat4000": "SWITCHES/CATALYST/Catalyst-4000",
        "cat4000s12": "SWITCHES/CATALYST/Catalyst-4000-SUP-I-II",
        "c4224": "SWITCHES/CATALYST/Catalyst-4224",
        "cat4232": "SWITCHES/CATALYST/Catalyst-4232",
        "cat4500": "SWITCHES/CATALYST/Catalyst-4500",
        "cat4500e": "SWITCHES/CATALYST/Catalyst-4500E",
        "c4500e": "SWITCHES/CATALYST/Catalyst-4500E",
        "cat4500es8": "SWITCHES/CATALYST/Catalyst-4500E-SUP8E",
        "cat4840g": "SWITCHES/CATALYST/Catalyst-4840G",
        "cat5000": "SWITCHES/CATALYST/Catalyst-5000",
        "ce500": "SWITCHES/CATALYST/Catalyst-500E",
        "c6500": "SWITCHES/CATALYST/Catalyst-6500-6800",
        "cat6000": "SWITCHES/CATALYST/Catalyst-6500-6800",
        "c6sup": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC1",
        "c6sup11": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC1",
        "c6sup12": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-1-MSFC2",
        "c6k222": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2",
        "c6sup22": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2",
        "s222": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2-MSFC2",
        "s2t54": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-2T",
        "s3223": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-32-MSFC2",
        "s32p3": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-32-PISA",
        "s72033": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-720-MSFC3",
        "s6t64": "SWITCHES/CATALYST/Catalyst-6500-6800/SUP-6T",
        "c6848x": "SWITCHES/CATALYST/Catalyst-6840-X",
        "c6880x": "SWITCHES/CATALYST/Catalyst-6880-X",
        "c8000be": "ROUTERS/CATALYST/Catalyst-8300-Edge",
        "c8000aep": "ROUTERS/CATALYST/Catalyst-8500-Edge - 8500 Gen 2",
        "c8000aes": "ROUTERS/CATALYST/Catalyst-8500L-Edge",
        "cat8510c": "SWITCHES/CATALYST/Catalyst-8510CSR",
        "cat8510m": "SWITCHES/CATALYST/Catalyst-8510MSR",
        "cat8540c": "SWITCHES/CATALYST/Catalyst-8540CSR",
        "cat8540m": "SWITCHES/CATALYST/Catalyst-8540MSR",
        "cat9k": "SWITCHES/CATALYST/Catalyst-9000",
        "cat9k_lite": "SWITCHES/CATALYST/Catalyst-9200",
        "cisco9k_iosxe": "SWITCHES/CATALYST/Catalyst-9350",
        "c1000": "SWITCHES/COMPACT/Catalyst-1000",
        "c2960c405": "SWITCHES/COMPACT/Catalyst-2960C",
        "c2960c405ex": "SWITCHES/COMPACT/Catalyst-2960CG",
        "c2960cx": "SWITCHES/COMPACT/Catalyst-2960CX",
        "c3560c": "SWITCHES/COMPACT/Catalyst-3560C",
        "c3560c405": "SWITCHES/COMPACT/Catalyst-3560C",
        "c3560c405ex": "SWITCHES/COMPACT/Catalyst-3560CG",
        "c3560cx": "SWITCHES/COMPACcat9T/Catalyst-3560CX",
        "cdb": "SWITCHES/COMPACT/Catalyst-Digital-Building",
        "c2020": "SWITCHES/EMBEDDED/2020",
        "ess3x00": "SWITCHES/EMBEDDED/3300",
        "cgs2520": "SWITCHES/GRID/CGS-2520",
        "grwicdes": "SWITCHES/GRID/CGS-Module",
        "ie1000": "SWITCHES/INDUSTRIAL-ETHERNET/IE-1000",
        "ie2000": "SWITCHES/INDUSTRIAL-ETHERNET/IE-2000",
        "ie2000u": "SWITCHES/INDUSTRIAL-ETHERNET/IE-2000U",
        "ies": "SWITCHES/INDUSTRIAL-ETHERNET/IE-3000",
        "ie3010": "SWITCHES/INDUSTRIAL-ETHERNET/IE-3010",
        "ie31xx": "SWITCHES/INDUSTRIAL-ETHERNET/IE-3100",
        "ie3x00": "SWITCHES/INDUSTRIAL-ETHERNET/IE-3x00",
        "ie35xx": "SWITCHES/INDUSTRIAL-ETHERNET/IE-3500",
        "ie4000": "SWITCHES/INDUSTRIAL-ETHERNET/IE-4000",
        "ie4010": "SWITCHES/INDUSTRIAL-ETHERNET/IE-4010",
        "ie5000": "SWITCHES/INDUSTRIAL-ETHERNET/IE-5000",
        "ir8340": "ROUTERS/INDUSTRIAL/IR8340",
        "s6523": "SWITCHES/METRO/Catalyst-6500ME",
        "me1200": "SWITCHES/METRO/ME-1200",
        "ucs_ctrlr": "SWITCHES/METRO/ME-1200/UCS-CONTROLLLER",
        "me240x": "SWITCHES/METRO/ME-2400",
        "me2600x": "SWITCHES/METRO/ME-2600X",
        "me340x": "SWITCHES/METRO/ME-3400",
        "me360x": "SWITCHES/METRO/ME-3600",
        "me360x_t": "SWITCHES/METRO/ME-3600",
        "me380x": "SWITCHES/METRO/ME-3800",
        "c2960sm": "SWITCHES/MODULES/Catalyst-2960-SERVICE-MODULE",
        "c3kx": "SWITCHES/MODULES/Catalyst-3000-SERVICE-MODULE",
        "c4gwy": "SWITCHES/CATALYST/Catalyst-4500/ACCESS-GATEWAY-MODULE",
        "c5atm": "SWITCHES/CATALYST/Catalyst-5000/ATM",
        "c5rsfc": "SWITCHES/CATALYST/Catalyst-5000/ROUTE-SWITCH-FEATURE-CARD",
        "c5rsm": "SWITCHES/CATALYST/Catalyst-5000/ROUTE-SWITCH-MODULE",
        "c6atm": "SWITCHES/CATALYST/Catalyst-6500-6800/ATM",
        "wscmm": "SWITCHES/CATALYST/Catalyst-6500-6800/CMM",
        "wsidsm2": "SWITCHES/CATALYST/Catalyst-6500-6800/IDSM2",
        "c6msfc": "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC1",
        "c6msfc2": "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC2",
        "c6msfc2a": "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC2A",
        "c6msfc3": "SWITCHES/CATALYST/Catalyst-6500-6800/MSFC3",
        "c6svc5fmwam": "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM",
        "c6svc6fmwam": "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM",
        "c6svcimwam": "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM",
        "svcmwam": "SWITCHES/CATALYST/Catalyst-6500-6800/MWAM",
        "c8000v": "ROUTERS/VIRTUAL/Catalyst-8000V",
        "Nexus": "SWITCHES/NEXUS/",
        "n1000v": "SWITCHES/NEXUS/Nexus-1000v",
        "n3000": "SWITCHES/NEXUS/Nexus-3000",
        "n3500": "SWITCHES/NEXUS/Nexus-3500",
        "n4000": "SWITCHES/NEXUS/Nexus-4000",
        "n5000": "SWITCHES/NEXUS/Nexus-5000",
        "n6000": "SWITCHES/NEXUS/Nexus-6000-5600",
        "n7000": "SWITCHES/NEXUS/Nexus-7000",
        "n7700": "SWITCHES/NEXUS/Nexus-7700",
        "n9000": "SWITCHES/NEXUS/Nexus-9000",
        "nxos": "SWITCHES/NEXUS/Nexus-9000-3000",
        "nxosv": "SWITCHES/NEXUS/Nexus-9000V",
        "Nexus": "SWITCHES/NEXUS/",
        "nxosgeneric": "SWITCHES/NEXUS/",
        "s5400": "SWITCHES/ROCKWELL-STRATIX/5400",
        "s5410": "SWITCHES/ROCKWELL-STRATIX/5410",
        "s5700": "SWITCHES/ROCKWELL-STRATIX/5700",
        "s5800": "SWITCHES/ROCKWELL-STRATIX/5800-IOS-XE",
        "mica-modem": "UNIVERSAL-GATEWAY/",
        "c5200": "UNIVERSAL-GATEWAY/AS-5200",
        "c5300": "UNIVERSAL-GATEWAY/AS-5300",
        "c5300XM": "UNIVERSAL-GATEWAY/AS-5300XM",
        "c5350": "UNIVERSAL-GATEWAY/AS-5350",
        "c5350XM": "UNIVERSAL-GATEWAY/AS-5350XM",
        "c5400": "UNIVERSAL-GATEWAY/AS-5400",
        "c5400XM": "UNIVERSAL-GATEWAY/AS-5400XM",
        "c5800": "UNIVERSAL-GATEWAY/AS-5800",
        "c5850": "UNIVERSAL-GATEWAY/AS-5850",
        "c5850tb": "UNIVERSAL-GATEWAY/AS-5850ERSC",
        "usbconsole": "USB-CONSOLE",
        "vg200": "VOICE/GATEWAY/VG-200",
        "voice": "VOICE",
        "vg20x": "VOICE/GATEWAY/VG-202",
        "vg20xxm": "VOICE/GATEWAY/VG-20x-XM",
        "vg224": "VOICE/GATEWAY/VG-224",
        "vg248": "VOICE/GATEWAY/VG-248",
        "vg3x0": "VOICE/GATEWAY/VG-310-320",
        "vg350": "VOICE/GATEWAY/VG-350",
        "vg400": "VOICE/GATEWAY/VG-400",
        "vg420": "VOICE/GATEWAY/VG-420",
        "vg450": "VOICE/GATEWAY/VG-450",
        "vgd": "VOICE/GATEWAY/VGD",
        "c2420": "VOICE/IAD/2420-IAD",
        "c2430": "VOICE/IAD/2430-IAD",
        "c2435": "VOICE/IAD/2435-IAD",
        "ics7700": "VOICE/ICS-7700",
        "ipp3905": "VOICE/IP-PHONES/3905",
        "ipp7911_7906": "VOICE/IP-PHONES/7906_7911",
        "ipp7914": "VOICE/IP-PHONES/7914",
        "ipp7915": "VOICE/IP-PHONES/7915",
        "ipp7916": "VOICE/IP-PHONES/7916",
        "ipp7921": "VOICE/IP-PHONES/7921",
        "ipp7931": "VOICE/IP-PHONES/7931",
        "ipp7937": "VOICE/IP-PHONES/7937-CONFERENCE-PHONE",
        "ipp7940_7960": "VOICE/IP-PHONES/7940_7960",
        "ipp7941_7961": "VOICE/IP-PHONES/7941_7961",
        "ipp7942_7962": "VOICE/IP-PHONES/7942_7962",
        "ipp7945_7965": "VOICE/IP-PHONES/7945_7965",
        "ipp7970_7971": "VOICE/IP-PHONES/7970_7971",
        "ipp7975": "VOICE/IP-PHONES/7975",
        "ipp8845_65": "VOICE/IP-PHONES/8845_8865",
        "ipp894x": "VOICE/IP-PHONES/894x",
        "ata187": "VOICE/ATA/ATA-187",
        "ata190": "VOICE/ATA/ATA-190",
        "uc500": "VOICE/UC-500",
        "wireless": "WIRELESS",
        "c1100": "WIRELESS/ACCESS-POINT/AIRONET-1100",
        "c1130": "WIRELESS/ACCESS-POINT/AIRONET-1130",
        "c1140": "WIRELESS/ACCESS-POINT/AIRONET-1140",
        "c1200": "WIRELESS/ACCESS-POINT/AIRONET-1200",
        "c1240": "WIRELESS/ACCESS-POINT/AIRONET-1240",
        "c1250": "WIRELESS/ACCESS-POINT/AIRONET-1250",
        "c1310": "WIRELESS/ACCESS-POINT/AIRONET-1310",
        "c1520": "WIRELESS/ACCESS-POINT/AIRONET-1500-Mesh-AP",
        "c1570": "WIRELESS/ACCESS-POINT/AIRONET-1570",
        "c1550": "WIRELESS/ACCESS-POINT/AIRONET-1550",
        "c350": "WIRELESS/ACCESS-POINT/AIRONET-350",
        "c520": "WIRELESS/ACCESS-POINT/AIRONET-521",
        "ap1g1": "WIRELESS/ACCESS-POINT/AIRONET-AP1G1-(700)",
        "ap1g2": "WIRELESS/ACCESS-POINT/AIRONET-AP1G2-(1600)",
        "ap1g3": "WIRELESS/ACCESS-POINT/AIRONET-AP1G3-(IR829-1530)",
        "ap1g4": "WIRELESS/ACCESS-POINT/AIRONET-AP1G4-(1810-1830-1850)",
        "ap1g5": "WIRELESS/ACCESS-POINT/AIRONET-AP1G5-(1540-1800-1815)",
        "ap1g6": "WIRELESS/ACCESS-POINT/AIRONET-AP1G6-(c9117)",
        "ap1g6a": "WIRELESS/ACCESS-POINT/AIRONET-AP1G6a-(c9130)",
        "ap1g7": "WIRELESS/ACCESS-POINT/AIRONET-AP1G7-(C9115-9120)",
        "ap1g8": "WIRELESS/Access-Point/Aironet-AP1G8 (9105i)",
        "ap3g1": "WIRELESS/ACCESS-POINT/AIRONET-AP3G1-(1260,3500)",
        "ap3g2": "WIRELESS/ACCESS-POINT/AIRONET-AP3G2-(1600,1700,2600,2700,3600,3700)",
        "c3700": "WIRELESS/ACCESS-POINT/AIRONET-AP3G2-(1600,1700,2600,2700,3600,3700)",
        "ap3g3": "WIRELESS/ACCESS-POINT/AIRONET-AP3G3-(2800,3800,4800,1560,6300)",
        "ap801": "WIRELESS/ACCESS-POINT/AIRONET-AP801-(861W,88xW,1911W-Routers)",
        "ap802": "WIRELESS/ACCESS-POINT/AIRONET-AP802-(812,819,886VA-W,887VA-W,89xW-Routers)",
        "AP1540": "WIRELESS/ACCESS-POINT/AP1540",
        "AP1560": "WIRELESS/ACCESS-POINT/AP1560",
        "AP1810w": "WIRELESS/ACCESS-POINT/AP1810w",
        "AP1815": "WIRELESS/ACCESS-POINT/AP1815",
        "AP1830": "WIRELESS/ACCESS-POINT/AP1830",
        "AP1840": "WIRELESS/ACCESS-POINT/AP1840",
        "AP1850": "WIRELESS/ACCESS-POINT/AP1850",
        "AP2800": "WIRELESS/ACCESS-POINT/AP2800",
        "AP3800": "WIRELESS/ACCESS-POINT/AP3800",
        "AP4800": "WIRELESS/ACCESS-POINT/AP4800",
        "AP6300": "WIRELESS/ACCESS-POINT/AP6300",
        "ISR1100AC": "WIRELESS/ACCESS-POINT/ISR-AP1100AC",
        "CT2500": "WIRELESS/CONTROLLER/2500",
        "CT5500": "WIRELESS/CONTROLLER/5500",
        "CT5520": "WIRELESS/CONTROLLER/5520",
        "ct5760": "WIRELESS/CONTROLLER/5760",
        "SWLC3750K9": "WIRELESS/CONTROLLER/CATALYST-3750",
        "SWISMK9": "WIRELESS/CONTROLLER/CATALYST-6500-WISM",
        "WISM": "WIRELESS/CONTROLLER/CATALYST-6500-WISM",
        "WISM2": "WIRELESS/CONTROLLER/CATALYST-6500-WISM2",
        "C9800-40": "WIRELESS/CONTROLLER/CATALYST-9800-40",
        "C9800-80": "WIRELESS/CONTROLLER/CATALYST-9800-80",
        "C9800-AP": "WIRELESS/CONTROLLER/CATALYST EMBEDDED WIRELESS CONTROLLER",
        "C9800-APC": "WIRELESS/CONTROLLER/CATALYST EMBEDDED WIRELESS CONTROLLER",
        "C9800-CL": "WIRELESS/CONTROLLER/CATALYST-9800-CL",
        "C9800-L": "WIRELESS/CONTROLLER/CATALYST-9800-L",
        "CW9800H": "WIRELESS/CONTROLLER/CATALYST-9800H",
        "CW9800M": "WIRELESS/CONTROLLER/CATALYST-9800M",
        "C9800-SW": "WIRELESS/CONTROLLER/CATALYST-9800-SW",
        "CT3504": "WIRELESS/CONTROLLER/3500",
        "CT7500": "WIRELESS/CONTROLLER/CT7500",
        "CT8500": "WIRELESS/CONTROLLER/CT8500",
        "LOC2700": "WIRELESS/CONTROLLER/LOCATION-2700",
        "WLCM": "WIRELESS/CONTROLLER/NM-NME",
        "SRE": "WIRELESS/CONTROLLER/NM-SRE",
        "CTVM": "WIRELESS/CONTROLLER/Virtual",
        "WLC2006": "WIRELESS/CONTROLLER/WLC2006",
        "WLC2100": "WIRELESS/CONTROLLER/WLC2100",
        "WLC4100": "WIRELESS/CONTROLLER/WLC4100",
        "WLC4400": "WIRELESS/CONTROLLER/WLC4400",
        "WLC7500": "WIRELESS/CONTROLLER/WLC7500",
        "CT8540": "WIRELESS/CONTROLLER/WLC8540",
        "wcs": "WIRELESS/CONTROLLER/WCS",
        "ccg110": "WIRELESS/GATEWAYS/CATALYST-WIRELESS-GATEWAY",
        "cg": "WIRELESS/GATEWAYS/CATALYST-CELLULAR-GATEWAY",
        "ucspe": "DEVELOPER-TOOLS/UCS-PLATFORM-EMULATOR"
    }

    return prod_map.get(prodcode, f"UNKNOWN PRODUCT CODE: {prodcode}")

def fileprocessorrommon(filename):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    fileprocessorrommon")

    basepath = "ROMMON"

    pattern_map = [
        # Direct filename matches for asr900
        (["asr900_15_6_43r_s_rommon.pkg", "rsp2_15_6_15r_s_rommon.pkg", "rsp2_15_6_19r_s_rommon.pkg",
          "rsp2_15_6_30r_s_rommon.pkg", "rsp2_rommon_15_4_3r_S5.pkg"], "asr900"),

        # ASR1000
        (["asr1000", "ASR1000_RM_16_3_2R.bin"], "asr1000"),

        # Catalyst 6500
        (["c6msfc2", "c6msfc2a", "c6msfc3", "c6ksup32", "c6ksup3", "c6dfc", "c6dfc3", "c2lc", "c6ksup720",
          "sup6t_rm", "pyramid_rm2", "cat6000-CPBOOT", "cat6000-sup2-rm2"], "c6500"),

        # c6848x
        (["transformer_rm.bin.SPA.152-02r.SYS1", "c6840x_rm"], "c6848x"),

        # c6880x
        (["governator_rm", "c6880x_rm"], "c6880x"),

        # Individual platforms
        (["C1800_RM2"], "c180x"),
        (["C1841_RM2"], "c1841"),
        (["C2800NM_RM2"], "c2800nm"),
        (["c805u"], "c805"),
        (["C820_RM_ALT"], "c820"),
        (["C860_RM2"], "c860"),
        (["C860VAE2_RM2"], "c860vae2"),
        (["C870_RM_ALT"], "c870"),
        (["C880_RM2"], "c880data"),
        (["C880s_RM"], "c800g2"),
        (["C890_RM2", "C891x_RM2"], "c890"),
        (["C890s_RM2"], "c890s"),
        (["C2801_RM2"], "c2801"),
        (["C1100-rommon"], "c1100router"),
        (["C3631_RM2"], "c3631"),
        (["C2691_RM2"], "c2691"),
        (["C2951_RM2"], "c2951"),
        (["C3725_RM2"], "c3725"),
        (["C3745_RM2"], "c3745"),
        (["C7200"], "c7200"),
        (["C7301"], "c7301"),
        (["C7304"], "c7304"),
        (["firmwareupgrade"], "cat4500es8"),
        (["cat4000"], "cat4000"),
        (["cat4500"], "cat4500"),
        (["asr903-rommon"], "asr903"),
        (["asr920"], "asr920"),
        (["AS5400XM_RM"], "c5400XM"),
        (["COUGAR_RM"], "cat8540c"),
        (["C3945E_RM2"], "c3900e"),
        (["C3800_RM2"], "c3845"),
        (["MANOPT_RM"], "ons15540"),
        (["C3900_RM2"], "c3900"),
        (["VG3X0_RM"], "vg3x0"),
        (["VG224_RM2"], "vg224"),
        (["RPMXF_RM"], "rpm"),
        (["MWR1900_RM2"], "mwr1900"),
        (["C2400_RM2"], "c2430"),
        (["C3200_RM_ALT"], "c3230"),
        (["C1900_2900_RM2"], "c1900-2900"),
        (["C10700_RM2"], "c10700"),
        (["isr4200_4300_rommon"], "isr4200-4300"),
        (["isr4300-rommon"], "isr4300"),
        (["isr4400_rommon", "isr4400-rommon"], "isr4400"),
        (["isr4400v2_rommon"], "isr4400v2"),

        # ASR9K rommon tarballs
        (["ROMMON", "rommon"], "asr9k"),

        # RSP720
        (["rsp720_10ge_rp-rm2", "rsp720_10ge_sp-rm2", "rsp720_rp-rm2", "rsp720_sp-rm2"], "c7600"),

        # C5940 and C5915
        (["C5940_RM_ALT"], "c5940"),
        (["C5915_RM"], "c5915"),

        # C9800-80
        (["C9800-80-rommon"], "C9800-80"),

        # Notes files — no product name needed
        (["Rommon-123-8r.YH13-notes", "Rommon-124-22r.YB5-notes",
          "Rommon-151-1r.T4-notes", "Rommon-151-1r.T5-notes",
          "Rommon-150-1r.M12-notes"], None),
    ]

    for patterns, prod in pattern_map:
        if any(filename == pat or filename.startswith(pat) for pat in patterns):
            if prod is not None:
                if prod == "asr9k" and not filename.endswith(".tar"):
                    continue
                prodname = product(prod)
                filepath = filepath2(prodname, basepath)
                filemove(filepath, filename)
            else:
                filemove(basepath, filename)
            return
        
    logging.debug(f"No match for filename {filename}")

def util_dot_join(*args):
    return ".".join(args)

def util2digit(a, b):
    warnings.warn(
    "util2digit(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return util_dot_join(a, b)

def util3digit(a, b, c):
    warnings.warn(
    "util3digit(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return util_dot_join(a, b, c)

def util4digit(a, b, c, d):
    warnings.warn(
    "util4digit(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return util_dot_join(a, b, c, d)

def util5digit(a, b, c, d, e):
    warnings.warn(
    "util5digit(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return util_dot_join(a, b, c, d, e)

def util6digit(a, b, c, d, e, f):
    warnings.warn(
    "util6digit(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return util_dot_join(a, b, c, d, e, f)

def stringtolist (a):
    return list(a)

# New universal function
def filepath(*parts):
    return os.path.join(*parts)

# Legacy-compatible wrappers
def filepath2(a, b):
    warnings.warn(
    "filepath2(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return filepath(a, b)

def filepath3(a, b, c):
    warnings.warn(
    "filepath3(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return filepath(a, b, c)

def filepath4(a, b, c, d):
    warnings.warn(
    "filepath4(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return filepath(a, b, c, d)

def filepath5(a, b, c, d, e):
    warnings.warn(
    "filepath6(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return filepath(a, b, c, d, e)

def filepath6(a, b, c, d, e, f):
    warnings.warn(
    "filepath6(a, b) is deprecated and will be removed in a future release. "
    "Use util_dot_join(*args) instead.",
    DeprecationWarning,
    stacklevel=2,
)
    return filepath(a, b, c, d, e, f)

def filepath(*parts):
    return os.path.join(*parts)

def collapse_strings(*args: Optional[str]) -> str:
    """
    Concatenate multiple strings.

    Args:
        *args: Strings to merge. `None` is allowed and treated as ''.

    Returns:
        A single string that is the concatenation of all arguments.

    Raises:
        TypeError: If any argument is not str or None.
    """
    parts: list[str] = []
    for idx, value in enumerate(args):
        if value is None:
            continue   # treat None as empty
        if not isinstance(value, str):
            raise TypeError(
                f"Argument {idx} must be str or None, got {type(value).__name__}"
            )
        parts.append(value)
    return "".join(parts)


def util2collapse(a: Optional[str], b: Optional[str]) -> str:
    """
    Backward-compatible wrapper for collapse_strings.
    Accepts exactly two arguments like the original function.

    Emits a DeprecationWarning to encourage migration.
    """
    warnings.warn(
        "util2collapse(a, b) is deprecated and will be removed in a future release. "
        "Use collapse_strings(*args) instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return collapse_strings(a, b)


def utilssinglemove(filename=None, prodname=None, imagecode=None):
    if not all([filename, prodname, imagecode]):
        raise ValueError("All of filename, prodname, and imagecode must be provided.")
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utilssinglemove")
    final_filepath = filepath(prodname, imagecode)
    filemove(final_filepath, filename)

def utilssingleprodname (filename,prodname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utilssingleprodname")
    filemove (prodname, filename)

def utils_dev_vf(filename=None, prodname=None, workname=None):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_vf")

    if prodname == "UNKNOWN":
        messageunknowndev()
        return

    parts = workname.split(".")
    length = len(parts)

    if 2 <= length <= 6:
        util_func = {
            2: util2digit,
            3: util3digit,
            4: util4digit,
            5: util5digit,
            6: util6digit,
        }[length]
        version2 = util_func(*parts)
        filepath_full = filepath(prodname, version2)
        filemove(filepath_full, filename)
    else:
        raise ValueError(f"Unsupported version format in workname: '{workname}'")

def utils_dev_v2_vf (filename,prodname,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_v2_vf")

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

def utils_dev_v2_vf_imagecode (filename,prodname,imagecode,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_v2_vf_imagecode")
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

def utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_imagecode_v2_vf")
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

def utils_dev_imagecode_vf (filename,prodname,imagecode,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_imagecode_vf")
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

def utils_dev_v2_vf_imagecode_dash (filename,prodname,imagecode,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_v2_vf_imagecode_dash")
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

def utils_dev_imagecode_v2_vf_dash (filename,prodname,imagecode,workname):
    logging.debug("Module: iosutils")
    logging.debug("Sub:    utils_dev_imagecode_v2_vf_dash")
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

def _log_unknown(thing: str):
    logging.warning(f"Unknown {thing}")

def messageunknowndev():
    _log_unknown("Device Type")

def messageunknownfeat():
    _log_unknown("Feature Set")

def messageunknownfile():
    _log_unknown("File")

def messageunknownversion():
    _log_unknown("Version")

def is_ios_file(name: str) -> bool:
#    logging.debug("Sub:    is_ios_file")
    ios_files = {
        "2730_rel_note",
        "Exp_V3_11.axf",
        "Exp_v10_10.spe",
        "Release-Notes-V3.12.1",
        "Release-Notes-V3.12.2",
        "fw_upgrade.tcl",
        "portware.2730.ios",
        "sconvertit0-11.tar",
        "sconvertit0-12.tar",
        "sprint_v16904_package.tar",
        "wconvertit0-11.zip",
        "wconvertit0-12.zip",
    }

    ios_prefixes = (
        "6509neba", "6516agbic", "6548getx", "66748getx",
        "MC7700", "MC7710", "MC7750",
        "VA_", "c2900XL", "c2900xl", "c3500XL", "c3500xl",
        "epld-6548getx", "epld-sup2", "mica-modem-pw",
        "mica-pw", "sprom", "vdsl.bin",
    )

    ios_mc_spk_prefixes = ("MC7304", "MC7350", "MC7354", "MC735X")

    return (
        name in ios_files
        or name.startswith(ios_prefixes)
        or (name.startswith(ios_mc_spk_prefixes) and name.endswith("spk"))
        or (name.startswith("V3_") and name.endswith("axf"))
        or (name.startswith("VAE2_") and name.endswith("bin"))
        or (name.startswith("VAEW_") and name.endswith("bin"))
    )

def is_iosxr_file(name: str) -> bool:
    logging.debug("Sub:    is_iosxr_file")
    xr_files = [
        "xrvr-fullk9-4.3.2.vmdk",
        "xrvr-full-4.3.2.vmdk",
        "xrv9k-fullk9-x.qcow2-6.0.0",
    ]

    xr_prefixes = (
            "ASR9000", "ASR9K", "ASR9k", "CSM.zip", "Cisco_TMS_", "NCS540", "SP_",
            "Sightline", "TMS_", "XR12000", "XRV9000", "XRV9K", "asr9k", "comp-asr9k",
            "csm-", "csm-3.5.2.zip", "csm-4.0.zip", "ddos_edge_protection_controller",
            "fullk9-R-XRV9000", "iosxrv", "ncs540", "xrd", "xrv9k", "c12k"
        )

    # Matches files like "3.9.1_asr9k_REC_SMUS_2011-12-12.tar"
    recsmu_pattern = re.compile(r"^\d+\.\d+\.\d+_asr9k(-p[x]?)?_REC_SMUS_.*\.(tar|tgz)$", re.IGNORECASE)

    return (
        name in xr_files
        or name.startswith(xr_prefixes)
        or recsmu_pattern.match(name)
    )

def is_server_file(name: str) -> bool:
#    logging.debug("Sub:    is_server_file")
    server_files = {
        "1X0DBIOSv4.8",
        "1X0SBIOSv4.8",
        "B57BCMCD_v15.2.4.1.tgz",
        "B57CiscoCD_T6.4.4.3-57712.zip",
        "BashFix-update-0-x86_64.tar.gz",
        "CSCwb00526.sh",
        "CSCwb00526.sh.zip",
        "DW_16MB_release_1029.bin",
        "DW_BIOS.bin.SPA",
        "DW_Signed_Bios_Image.bin.SPA",
        "Datacenter_Technology_Pack-1.0.53.ubf",
        "Datacenter_Technology_Pack_Update_1_Patch-1.0.58.ubf",
        "GlibcFix-pi22-update-0-x86_64.tar.gz",
        "InstallerUpdateBE-1.0.5.tar.gz",
        "Intel_Windows_drv_MR_6.714.18.00_pv.zip",
        "JeOS_Patch_To_Enable_ASD.zip",
        "LSI_x64_Signed_Driver_5.2.116.64.zip",
        "MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip",
        "PrimeInfra.pem",
        "SW_16MB_release_1102.bin",
        "SW_Signed_Bios_Image.bin.SPA",
        "Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA",
        "Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA",
        "Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA",
        "Signed_DW_M1M2_Bios_Image_041015.bin.SPA",
        "Signed_EN_BIOS_1.5.0.4.bin.SPA",
        "Signed_EN_BIOS_1.5.0.5.bin.SPA",
        "Signed_EN_BIOS_1.5.0.6.bin.SPA",
        "Signed_SW_M2_BIOS_1.5.0.6.bin.SPA",
        "Signed_SW_M2_BIOS_1.5.0.7.bin.SPA",
        "Signed_SW_M2_BIOS_1.5.0.8.bin.SPA",
        "Signed_SW_M2_Bios_1.5.0.5.bin.SPA",
        "UCSEDM3_BIOS_2.4.SPA",
        "UCSEDM3_BIOS_2.5.SPA",
        "UCSEDM3_BIOS_2.6.SPA",
        "UCSE_CIMC_2.3.1.bin",
        "UCSE_CIMC_2.3.2.bin",
        "UCSE_CIMC_2.3.3.bin",
        "UCSE_CIMC_2.3.5.bin",
        "UCS_docs_20110510.iso",
        "b2xx-m1-drivers-1.1.1j.iso",
        "c2xx-m1-utils-1.0.2.iso",
        "ca_technology_package-2.1.0.0.41.ubf",
        "cspc28backupscript.zip",
        "cspc210backupscript.zip",
        "efi-obd-v12-07-18.diag",
        "efi-obd-v13-10-15.diag",
        "efi-obd-v13-7-3.diag",
        "huu-2.3.1.iso",
        "huu-2.3.2.iso",
        "huu-2.3.3.iso",
        "huu-2.4.1.iso",
        "huu-3.0.1.iso",
        "huu-3.1.1.iso",
        "huu_3.1.2.iso",
        "huu_3.1.3.iso",
        "huu_3.1.4.iso",
        "huu_3.2.6.v3.iso",
        "intel9.2.3.1023.tar",
        "operations_center_pi_2_1_2_enable_update.ubf",
        "pi212_20141118_01.ubf",
        "pi212_PIGEN_CSCur43834_01.ubf",
        "readme_10.2.1.ST.1",
        "rhel-vulnerability-patch-pnp-2.2.0.14.tar.gz",
        "rste_4.5.0.1335_install.zip",
        "ucse-huu-2.1.1.iso",
        "update_pkg-Mar-22-MR-rebuild.bin",
        "update_pkg-ucse.combined.120808.bin",
        "update_pkg-ucse.combined.REL.2.2.1.bin",
        "update_pkg-ucse.combined.REL.2.2.2.bin",
        "update_pkg-ucse.combined.REL.bin",
        "Deploy-cisco-dna-center-on-aws-using-aws-marketplace"
    }

    server_prefixes = (
        "APIC-EM-", "C200M1-", "CIMC_", "CSLU_Installer", "Cisco-HX-Data-Platform-Installer",
        "CiscoPI", "CiscoPI3.4.pem", "CiscoPI3.5.pem", "Cisco_ACI", "Collector",
        "DCNM", "DNAC-", "Device-Pack", "DnacPreCheckASSESMENTUbf", "HX-ESXi",
        "HX-Kubernetes", "HxClone-HyperV", "HyperFlex-VC-HTML", "HyperFlex-Witness-",
        "PI", "PI-APL-", "PI-UCS-APL-", "PI-Upgrade-", "PI-VA-", "PNP-GATEWAY-VM-",
        "SSMS", "SSM_On-Prem", "UCSC-C220-M5-", "UCSC-C240-M5-", "UCSC-C220-M6-",
        "UCSC-C240-M6-", "UCSC-C220-M7-", "UCSC-C240-M7-", "UCSC-C225-M6-", "UCSC-C225-M8-",
        "aci-apic", "aci-msft-pkg", "aci-n9000-dk9", "aci-simulator", "aci-vpod", "acisim",
        "apic-vrealize", "apic_em_update-apic-", "cisco-HX-Data-Platform-Installer",
        "cisco-prime-pnp", "cisco-prime-pnp-app-k9-", "collector", "dcnm", "delnorte",
        "delnorte2", "dnac", "esx-msc", "hostUpgrade_v", "hostupgrade_v", "hxcsi",
        "msc", "pi", "pid-ctlg", "plumas", "plumas2", "pnp-", "ssms", "storfs-packages",
        "tools-msc", "ucs", "ucs-cxx", "update_pkg-ucse", "vcenter-plugin",
        "Launchpad-desktop", "DNA_Center_VA", "CIMCS", "cimcs", "CatC", "trustidevcodesigning5",
        "cml2", "refplat"
    )

    return (
        name in server_files
        or name.startswith(server_prefixes)
        or (name.startswith("CIMC_") and name.endswith(".bin"))
    )

def is_security_file(name: str) -> bool:
#    logging.debug("Sub:    is_security_file")
    security_files = {
        "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429-Readme.txt",
        "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429.zip",
        "ACS57BasePatch.tar.gz",
        "APIC_FMC_Remediation_module_1.0.1_7.tgz",
        "APIC_FMC_Remediation_module_1.0.2_1.tgz",
        "APIC_FirePOWER_Remediation_Module_2.0.1.1.tgz",
        "APIC_Secure_Firewall_Remediation_Module_2.0.2.1.tgz",
        "BOOTX64.EFI",
        "PIX_to_ASA_1_0.dmg",
        "PIXtoASA_1_0.zip",
        "PIXtoASAsetup_1_0.exe",
        "README-occ-121.rtf",
        "README_ISE_20_201_21_22",
        "README_WebAgent.txt",
        "ReadMe_for_ACS_5.6_Upgrade_Package-txt",
        "Secure_Workload_Remediation_Module_1.0.3.tgz",
        "VPN-5.0.00.0340-MSI.exe",
        "VPNDisable_ServiceProfile.xml",
        "VPN_Client_Support_Matrix2.txt",
        "Vista-VPN-Troubleshooting.txt",
        "WebSecurityCert.zip",
        "anyconnect_app_selector_1.0.zip",
        "anyconnect_app_selector_2.0.zip",
        "cisco_vpn_auth.jar",
        "citrix_plugin_howto.doc",
        "cvdm-css-1.0.zip",
        "cvdm-css-1.0_K9.zip",
        "fcs-csa-hotfix-5.2.0.238-w2k3-k9-CSM.zip",
        "fcs-csamc-4.5.1.616-CSA-Policy-Descriptions.zip",
        "firepower-mibs.zip",
        "grub.efi",
        "occ-121.gz",
        "occ-121.zip",
        "pnLogAgent_1.1.zip",
        "pnLogAgent_4-1-3.zip",
        "pnLogAgent_4-1-3.zip.txt",
        "pxGrid_Mitigation_Remediation_v1.0.tgz",
        "rawrite.exe",
        "rdp_09.11.2012.jar",
        "release_duration_tool.tar",
        "vpn30xxboot-4.0.Rel.hex",
        "webAgent_1-0.zip",
        "webAgent_1-0.zip.txt",
        "webAgent_1-1.zip",
        "webAgent_1-1.zip.txt",
    }

    security_prefixes = (
        "128MB.sdf", "256MB.sdf", "5-", "ACS", "Acs", "CSCvn17524", "CUCM-CSA-",
        "CiscoCM-CSA-", "CiscoCVP-CSA-", "CiscoICM-CSA-", "Cisco-ISE", "Cisco-vISE",
        "CiscoISE", "CiscoISN-CSA-", "CiscoPA-CSA-", "CiscoUnity-CSA-", "Cisco_FTD",
        "Cisco_Firepower", "Cisco_Firepower_GEODB", "Cisco_Firepower_SRU",
        "Cisco_Firepower_Threat", "Cisco_Network_Sensor", "Cisco_Secure_FW_TD_4200",
        "Cisco_VDB_Fingerprint_Database", "Clean", "FMT-CP-Config-Extractor", "Firepower",
        "Firepower_Migration_Tool", "Firewall_Migration_Tool", "IDS", "IOS-S", "IPS",
        "ISE", "PIX", "SNS-35x5", "SNS-35xx", "SNS-36xx", "SNS-37xx", "SSM_On-Prem",
        "Sourcefire", "UCP", "UTD-STD-SIGNATURE", "VPN3000", "anyconnect",
        "secure-firewall-posture", "applAcs", "asa", "asasfr", "asdm", "c6svc-fwm-k9",
        "cisco-asa", "cisco-ftd", "cisco-secure-client", "coeus", "csd", "csm",
        "csm-maxmind-geolitecity-", "csmars", "external-sso", "fcs-CSM", "fcs-cms",
        "fcs-csamc", "fcs-csm", "fcs-mcp", "fcs-rme", "ftd", "fwsm_migration", "fxos",
        "hostscan", "iosxe-utd", "iosxe-utd-ips", "iox-iosxe-utd", "ise", "ise-pic",
        "pic", "Cisco-ISE-PIC", "lsp-rel-", "mac-spw-dmg", "phoebe", "sampleTransforms",
        "secapp-ucmk9", "secapp-utd", "thirdparty", "tools-anyconnect",
        "tools-cisco-secure-client", "upd-pkg-SNS-35x5-cimc", "upd-pkg-SNS-35xx",
        "upd-pkg-SNS-36xx-cimc", "vpn3002", "vpn3005", "vpnclient", "webagent",
        "win_spw", "zeus",
    )

    # Patterns that require both startswith and endswith
    special_patterns = [
        ("CSM4", "Service_Pack1.exe"),
        ("CSM4", "Service_Pack2.exe"),
        ("IDS-sig-", ".readme.txt"),
        ("IDS-sig-", ".zip"),
        ("IOS-S", "-CLI.pkg"),
        ("IOS-S", ".zip"),
        ("PIX", ".bin"),
        ("bh", ".bin"),
        ("cda", "iso"),
        ("np", ".bin"),
        ("pdm", ".bin"),
        ("pix", ".bin"),
        ("sg", "adi"),
        ("sg", "adi-gz"),
        ("sg", "zip"),
        ("update-", "-major-K9.zip"),
    ]

    if name in security_files:
        return True

    if name.startswith(security_prefixes):
        return True

    for prefix, suffix in special_patterns:
        if name.startswith(prefix) and name.endswith(suffix):
            return True

    return False

def is_iosxe_file(name: str) -> bool:
#    logging.debug("Sub:    is_iosxe_file")

    iosxe_prefixes = (
        "C8000-1N", "C8000-2N2S", "C9800-", "CAT3650_WEBAUTH_BUNDLE",
        "CAT3850_WEBAUTH_BUNDLE", "CW9800H", "CW9800M", "WP7601", "WP7603",
        "WP76xx", "appqoe", "asr1000", "asr1000rp1", "asr1000rp2", 
        "asr1000rpx86", "asr1001", "asr1001x", "asr1002", "asr1002x",
        "asr900rsp1", "asr900rsp2", "asr900rsp3", "asr901", "asr901rsp1",
        "asr901rsp2", "asr903rsp1", "asr903rsp2", "asr920", "asr920igp",
        "c1100-ucmk9", "c1100-universalk9", "c1100_gfast_", "c1100_phy_",
        "c1100tg", "c8000aep", "c8000aes", "c8000be", "c8000v", "c81g2be",
        "c84g2aes", "c8kg2be", "cat3k_caa", "cat4500es8", "cat9k", "ccg110",
        "cisco9k_iosxe", "csr1000v", "csr1000v_milplr", "ct5760", "ess3x00",
        "ie1000", "ie31xx", "ie35xx", "ie3x00", "ie9k", "ie9k_iosxe", 
        "iosxe-remote-mgmt", "iosxe-sd-avc", "ir1101", "ir8340", "isr1100",
        "isr4200", "isr4300", "isr4400", "isr4400v2", "s5800", "ttam", 
        "vg400", "vg420", "vg450", "ie1000", "ASR1K-fpga_prog",
        "isr-hw-programmables", "nim_vab_phy_fw_",
    )

    return name.endswith("comp_matrix.xml") or name.startswith(iosxe_prefixes)

def is_nxos_file(name: str) -> bool:
#    logging.debug("Sub:    is_nxos_file")
    nxos_files = {
        "L2-L3_CT.zip",
        "n3k_bios_release_rn.pdf",
        "ntp-1.0.1-7.0.3.I2.2d.lib32_n9000.rpm",
        "ntp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm",
        "ntp-1.0.2-7.0.3.I2.2e.lib32_n9000.rpm",
        "nxos.nsqos_lc_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm",
        "nxos.nsqos_sup_tor-n9k_TOR-1.0.0-7.0.3.I2.2e.lib32_n9000.rpm",
        "snmp-1.0.1-7.0.3.I2.2e.lib32_n9000.rpm",
        "upgrade_m500_firmware.tar.gz",
        "vxlan-2.0.1.0-9.2.3.lib32_n9000.rpm",
    }

    nxos_prefixes = (
        "Nexus1000V", "Nexus1000V5", "Nexus1000v",
        "guestshell", "n1000vh-dk9",
        "n3000", "n3500", "n4000", "n5000", "n5000_poap_script",
        "n6000", "n6000_poap_script", "n7000", "n7700",
        "n9000", "n9000-epld",
        "nexus-1000v", "nexus9300v", "nexus9500v",
        "nxos", "nxos64", "nxosv",
        "oac", "poap_ng", "poap_script", "ssd_c400_upgrade",
    )

    return name in nxos_files or name.startswith(nxos_prefixes)

def is_rommon_file(name: str) -> bool:
#    logging.debug("Sub:    is_rommon_file")
    rommon_files = {
        "Rommon-123-8r.YH13-notes",
        "Rommon-124-22r.YB5-notes",
        "Rommon-151-1r.T4-notes",
        "Rommon-151-1r.T5-notes",
        "Rommon-150-1r.M12-notes",
        "asr900_15_6_43r_s_rommon.pkg",
        "ASR1000_RM_16_3_2R.bin",
        "C2400_RM2.symbols.123-7r.T2",
        "c6840x_rm.bin.SPA.152-02r.SYS2",
    }

    rommon_substrings = (
        "srec", "rommon", "ROMMON", "promupgrade", "governator",
        "C7200_NPEG1_RM", "C7200_NPEG2_RM", "C7200_NPEG1_BOOT_ROM",
        "c6880x_rm", "cat6000-CPBOOT", "tinyrom"
    )

    rommon_prefixes = (
        "firmwareupgrade", "transformer_rm", "sup6t_rm", "asr920-rommon"
    )

    # Check exact names
    if name in rommon_files:
        return True

    # Check substrings
    if any(sub in name for sub in rommon_substrings):
        return True

    # Check prefixes
    if name.startswith(rommon_prefixes):
        return True

    return False

def is_cat_file(name: str) -> bool:
#    logging.debug("Sub:    is_cat_file")
    """
    Detects if the file belongs to Cat4000/5000/6000 series,
    extracts product name and image code, and processes it.
    """
    cat_image_map = {
        # cat4000
        "cat4000.": "sup",
        "cat4000-cv.": "supcv",
        "cat4000-k8.": "supk8",
        "cat4000-k9.": "supk9",
        # cat5000
        "cat5000-supg.": "supg",
        "cat5000-supgk9.": "supgk9",
        "cat5000-sup.": "sup",
        "cat5000-sup3.": "supg",
        "cat5000-sup8m.": "sup8m",
        "cat5000-atm.": "m",
        "cat5000-sup3cv.": "sup3cv",
        "cat5000-sup3cvk9.": "sup3cvk9",
        "cat5000-sup3k9.": "sup3k9",
        # cat6000
        "cat6000-sup.": "sup",
        "cat6000-supcv.": "supcv",
        "cat6000-supcvk8.": "supcvk8",
        "cat6000-supcvk9.": "supcvk9",
        "cat6000-supk8.": "supk8",
        "cat6000-supk9.": "supk9",
        "cat6000-sup2.": "sup2",
        "cat6000-sup2cv.": "sup2cv",
        "cat6000-sup2cvk8.": "sup2cvk8",
        "cat6000-sup2cvk9.": "sup2cvk9",
        "cat6000-sup2k8.": "sup2k8",
        "cat6000-sup2k9.": "sup2k9",
        "cat6000-sup32pfc3cvk8.": "sup32pfc3cvk8",
        "cat6000-sup32pfc3cvk9.": "sup32pfc3cvk9",
        "cat6000-sup32pfc3k8.": "sup32pfc3k8",
        "cat6000-sup32pfc3k9.": "sup32pfc3k9",
        "cat6000-sup720cvk8.": "sup720cvk8",
        "cat6000-sup720cvk9.": "sup720cvk9",
        "cat6000-sup720k8.": "sup720k8",
        "cat6000-sup720k9.": "sup720k9",
    }

    for prefix, imagecode in cat_image_map.items():
        if name.startswith(prefix):
            # Extract product name: cat4000, cat5000, cat6000
            prodname = prefix.split("-")[0].rstrip(".")
            # Remove prefix and .bin extension
            workname = name.replace(".bin", "").replace(prefix, "")
            # Call the processing function
            utils_dev_imagecode_v2_vf_dash(name, prodname, imagecode, workname)
            return True
    return False

def nbar(filename: str):
    logging.debug("Sub:    nbar")
    """
    Processes NBAR-related files and moves them according to type and version.
    """
    prodname = product("ntwkmgmt")
    imagecode = imagelookup("nbar")

    # Standardize the base workname by removing common suffixes
    workname = clean_workname(
        filename,
        suffixes=[".pack.zip", ".pack"]
    )

    # Special cases with long prefixes
    special_prefixes = [
        "pp-adv-nam-18-",
        "pp-adv-nam-61-18-",
        "pp-adv-csr1000v-153-2-S0a-15-"
    ]

    for pre in special_prefixes:
        if filename.startswith(pre):
            workname = clean_workname(filename, prefixes=[pre], suffixes=[".pack.zip", ".pack"])
            filepath = filepath3(prodname, imagecode, workname)
            filemove(filepath, filename)
            return

    # Default handling using version extracted from the filename
    splitbydash = workname.split("-")
    try:
        myver = splitbydash[6]
    except IndexError:
        myver = splitbydash[5]

    filepath = filepath3(prodname, imagecode, myver)
    filemove(filepath, filename)

def ucspe(filename: str):
    logging.debug("Sub:    ucspe")
    """
    Processes UCSPE-related files and moves them according to type and version.
    """


    prodname = product("ucspe")

    # Special sets for versioned files
    docs_files = {"ucsm_object_docs.zip", "UCSPE 3.1(2e) 6248 1340 export.txt"}
    export_files_323e = {"export_6248_ch1_b200m5.xml", "swift_stack_3260_cfg_export.xml"}
    export_files_412cPE1 = {
        "export_6248_ch1_b200m5.xml.txt",
        "swift_stack_3260_cfg_export.xml.txt",
        "ucspe_6296_chassis1_export.xml.txt",
        "ucspe_6454_chassis1_export.xml.txt",
    }

    # Handle PDF files
    if filename.endswith("pdf"):
        imagecode = imagelookup("docs")
        utilssinglemove(filename, prodname, imagecode)
        return

    # Handle specific version files
    if filename in docs_files:
        utilssinglemove(filename, prodname, "3.1.2e")
        return

    if filename in export_files_323e:
        utilssinglemove(filename, prodname, "3.2.3e")
        return

    if filename in export_files_412cPE1:
        utilssinglemove(filename, prodname, "4.1.2cPE1")
        return

    # Handle stripped firmware files
    if filename.startswith("UCSM") and filename.endswith("stripped-firmware.zip"):
        imagecode = imagelookup("stripped-firmware")
        workname = clean_workname(
            filename,
            prefixes=["UCSM-"],
            suffixes=["-stripped-firmware.zip"],
            char_map={"(": ".", ")": ""}
        )
        utils_dev_imagecode_vf(filename, prodname, imagecode, workname)
        return

    # Default handling for UCSPE OVA/ZIP files
    prefixes = [
        "UCSPE_", "cimc_emulator-", "Cisco_UCS_Platform_Emulator_v",
        "Cisco_UCS_Platform_Emulator_", "c220-m4-emu-cimc.",
        "c240-m4-emu-cimc.", "c460-m4-emu-cimc."
    ]
    suffixes = [".ova.zip", ".ova", ".zip", ".73034.361150.7z"]
    workname = clean_workname(filename, prefixes=prefixes, suffixes=suffixes)
    utils_dev_vf(filename, prodname, workname)

def clean_workname(filename: str, prefixes=None, suffixes=None, char_map=None) -> str:
    """
    Cleans a filename by removing specified prefixes and suffixes and replacing characters.
    
    Args:
        filename (str): The original filename.
        prefixes (list or tuple): Strings to remove from the start of the filename.
        suffixes (list or tuple): Strings to remove from the end of the filename.
        char_map (dict): Optional dictionary mapping characters to replace, e.g., {"(": ".", ")": ""}.
    
    Returns:
        str: The cleaned filename.
    """
    workname = filename
    prefixes = prefixes or []
    suffixes = suffixes or []

    for pre in prefixes:
        if workname.startswith(pre):
            workname = workname[len(pre):]

    for suf in suffixes:
        if workname.endswith(suf):
            workname = workname[:-len(suf)]

    if char_map:
        for old_char, new_char in char_map.items():
            workname = workname.replace(old_char, new_char)

    return workname


