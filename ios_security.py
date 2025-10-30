import os
import re
import logging
import iosutils

# Import all functions that don't start with underscore
for name in dir(iosutils):
    if not name.startswith("_"):
        globals()[name] = getattr(iosutils, name)

_LOG = logging.getLogger(__name__)

def process_anyconnect_file(filename, match_result, product_lookup, image_lookup, platform):
    _LOG.debug("Sub:    process_security_file")

    if not match_result:
        raise ValueError(f"No match result provided for file: {filename}")

    # --- Normalize via lookup functions
    productcode     = product(product_lookup)
    imagecode       = imagelookup(image_lookup)
    platform_result = imagelookup(platform)

    # --- Extract version properly
    ver_match = re.search(r'(\d+\.\d+\.\d+(?:\.\d+)?)', filename)
    if ver_match:
        full_version = ver_match.group(1)
        # Split for 2-part and 3-part versions
        parts = full_version.split('.')
        version_2 = '.'.join(parts[0:2])           # 5.1
        version_3 = '.'.join(parts[0:3])           # 5.1.2
    else:
        version_2 = "unknown"
        version_3 = "unknown"

    # --- Build destination path (no SMU/bug ID concept for AnyConnect)
    dest_path = filepath(productcode, imagecode, platform_result, version_2, version_3)

    # --- Move file to destination
    filemove(dest_path, filename)

def fileprocessorsecurity (filename):
    logging.debug("Module: ios_security")
    logging.debug("Sub:    fileprocessorsecurity")

    firmware_matching = [
        #Anyconnect / Cisco Secure Client (Windows)
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "nvm",            'platform': "windows",  'split_type': "dot",  'suffix': "-nvm-standalone-k9.msi"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "vpnapi",         'platform': "windows",  'split_type': "dot",  'suffix': "-vpnapi.zip"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "client",         'platform': "windows",  'split_type': "dot",  'suffix': "-predeploy-k9.zip"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "client",         'platform': "windows",  'split_type': "dot",  'suffix': "-predeploy-k9.pkg"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "client",         'platform': "windows",  'split_type': "dot",  'suffix': "-webdeploy-k9.pkg"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "isecompliance",  'platform': "windows",  'split_type': "dot",  'suffix': "-isecompliance-predeploy-k9.msi"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "isecompliance",  'platform': "windows",  'split_type': "dot",  'suffix': "-isecompliance-predeploy-k9.pkg"},
        {'prefix': "cisco-secure-client-win-",          'productcode': "anyconnect",  'imagecode': "isecompliance",  'platform': "windows",  'split_type': "dot",  'suffix': "-isecompliance-webdeploy-k9.pkg"},
        {'prefix': "cisco-secure-client-win-arm64-",    'productcode': "anyconnect",  'imagecode': "client",         'platform': "windows",  'split_type': "dot",  'suffix': "-webdeploy-k9.pkg"},
        {'prefix': "cisco-secure-client-win-arm64-",    'productcode': "anyconnect",  'imagecode': "isecompliance",  'platform': "windows",  'split_type': "dot",  'suffix': "-isecompliance-webdeploy-k9.pkg"},
        #Anyconnect / Cisco Secure Client (MacOS)
        {'prefix': "cisco-secure-client-macos-",        'productcode': "anyconnect",  'imagecode': "nvm",            'platform': "macos",    'split_type': "dot",  'suffix': "-nvm-standalone.dmg"},
        {'prefix': "cisco-secure-client-macos-",        'productcode': "anyconnect",  'imagecode': "vpnapi",         'platform': "macos",    'split_type': "dot",  'suffix': "-vpnapi.tar.gz"},
        {'prefix': "cisco-secure-client-macos-",        'productcode': "anyconnect",  'imagecode': "client",         'platform': "macos",    'split_type': "dot",  'suffix': "-predeploy-k9.dmg"},
        {'prefix': "cisco-secure-client-macos-",        'productcode': "anyconnect",  'imagecode': "client",         'platform': "macos",    'split_type': "dot",  'suffix': "-webdeploy-k9.pkg"},
        #Anyconnect / Cisco Secure Client (Linux)
        {'prefix': "acnvmcollector-",                   'productcode': "anyconnect",  'imagecode': "nvm",            'platform': "linux",    'split_type': "dot",  'suffix': ".zip"},
        {'prefix': "cisco-secure-client-linux-arm64-",  'productcode': "anyconnect",  'imagecode': "vpnapi",         'platform': "linux",    'split_type': "dot",  'suffix': "-vpnapi.tar.gz"},
        {'prefix': "cisco-secure-client-linux-arm64-",  'productcode': "anyconnect",  'imagecode': "client",         'platform': "linux",    'split_type': "dot",  'suffix': "-predeploy-deb-k9.tar.gz"},
        {'prefix': "cisco-secure-client-linux-arm64-",  'productcode': "anyconnect",  'imagecode': "client",         'platform': "linux",    'split_type': "dot",  'suffix': "-predeploy-k9.tar.gz"},
        {'prefix': "cisco-secure-client-linux-arm64-",  'productcode': "anyconnect",  'imagecode': "client",         'platform': "linux",    'split_type': "dot",  'suffix': "-predeploy-rpm-k9.tar.gz"},
        {'prefix': "cisco-secure-client-linux-arm64-",  'productcode': "anyconnect",  'imagecode': "client",         'platform': "linux",    'split_type': "dot",  'suffix': "-webdeploy-k9.pkg"},
        #Anyconnect / Cisco Secure Client (Android)
        {'prefix': "anyconnect-android-",               'productcode': "anyconnect",  'imagecode': "client",         'platform': "android",  'split_type': "dot",  'suffix': "-release.apk"},
    ]










    # --- Try firmware matching by prefix/suffix
    for entry in firmware_matching:
        if filename.startswith(entry['prefix']) and filename.endswith(entry['suffix']):
            matchtype   = "firmware"
            productcode = entry['productcode']
            imagecode   = entry['imagecode']
            platform    = entry['platform']
            process_anyconnect_file(filename, matchtype, productcode, imagecode, platform)



    if (
        filename.startswith("anyconnect") or
        filename.startswith("cisco-secure-client") or
        filename.startswith("csd") or
        filename.startswith("external-sso") or
        filename.startswith("hostscan") or
        filename.startswith("sampleTransforms") or
        filename.startswith("secure-firewall-posture") or
        filename.startswith("thirdparty") or
        filename.startswith("tools-anyconnect") or
        filename.startswith("tools-cisco-secure-client")
        ):
        sec_anyconnect (filename)

    elif (
        filename.startswith ("ise-apply-") or
        filename.startswith ("ise-rollback-")
    ):
        sec_ise_hotfix (filename)

    elif filename == "release_duration_tool.tar":
        prodname = product ("firepower")
        imagecode = imagelookup("fmc")
        filepath = filepath4 (prodname,imagecode,"5.4.0","5.4.0.9")
        filemove (filepath, filename)

    elif (
    filename.startswith("asacx-5500x-boot") or 
    filename.startswith("asacx-boot")
    ):
        prodname = product ("asacx")
        imagecode = imagelookup("boot")
        sec_asacx (filename,prodname,imagecode)

    elif filename.startswith("asacx-sys-"):
        prodname = product ("asacx")
        imagecode = imagelookup("system")
        sec_asacx (filename,prodname,imagecode)

    elif (
    filename.startswith("sg") and filename.endswith("zip") or 
    filename.startswith("sg") and filename.endswith("adi") or 
    filename.startswith("sg") and filename.endswith("adi-gz") or 
    filename == "cvdm-css-1.0_K9.zip" or 
    filename == "cvdm-css-1.0.zip"
    ):
        sec_css (filename)

    elif(
    filename == "vpn30xxboot-4.0.Rel.hex"
    ):
        prodname = product("vpn3000")
        imagecode = imagelookup("boot")
        utilssinglemove (filename,prodname,imagecode)

    elif(
    filename == "vpn3000-4.7.Rel-k9.bin"
    ):
        prodname = product("vpn3000")
        filepath = filepath3(prodname,"4.7","4.7")
        filemove (filepath, filename)

    elif(
    filename == "vpn3000-4.7.1.Rel-k9.bin"
    ):
        prodname = product("vpn3000")
        filepath = filepath3(prodname,"4.7","4.7.1")
        filemove (filepath, filename)

    elif(
    filename == "vpn3000-4.7.2.Rel-k9.bin"
    ):
        prodname = product("vpn3000")
        filepath = filepath3(prodname,"4.7","4.7.2")
        filemove (filepath, filename)

    elif(
    filename == "vpn3000events-4.1.7.E.zip" or 
    filename == "vpn3000events-4.7.Rel.zip"
    ):
        prodname = product("vpn3000")
        imagecode = imagelookup("events")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("VPN3000") or 
    filename.startswith("vpn3000") or 
    filename.startswith("vpn3002") or 
    filename.startswith("vpn3005")
    ):
        sec_vpn3000 (filename)

    elif(
    filename == "vpn30xxboot-4.0.Rel.hex"
    ):
        prodname = product("vpn3000")
        imagecode = imagelookup("boot")
        utilssinglemove (filename,prodname,imagecode)

    elif(
    filename.startswith("FMT-CP-Config-Extractor") or 
    filename.startswith("Firepower_Migration_Tool") or 
    filename.startswith("Firewall_Migration_Tool")
    ):
        prodname = product("firepower")
        imagecode = imagelookup("configconvert")
        utilssinglemove (filename,prodname,imagecode)

    elif(
    filename.startswith("np") and filename.endswith(".bin") or 
    filename.startswith("pdm") and filename.endswith(".bin") or 
    filename == "PIXtoASA_1_0.zip" or 
    filename == "PIX_to_ASA_1_0.dmg" or 
    filename == "PIXtoASAsetup_1_0.exe" or 
    filename == "rawrite.exe" or 
    filename == "occ-121.zip" or 
    filename == "occ-121.gz" or 
    filename == "README-occ-121.rtf" or 
    filename.startswith("pix") and filename.endswith(".bin") or 
    filename.startswith("PIX") and filename.endswith(".bin")
    ):
        prodname = product("pix")
        sec_pix (filename,prodname)

    elif(
    filename == "fwsm_migration_mac-1.0.18.zip" or 
    filename == "fwsm_migration_win-1.0.18.zip"
    ):
        prodname = product("asa")
        imagecode = imagelookup("fwsmtoasasm")
        utilssinglemove (filename,prodname,imagecode)

    elif(
    filename.startswith ("coeus") or 
    filename.startswith ("phoebe") or 
    filename.startswith ("zeus")
    ):
        sec_ironportv (filename)

    elif (
        filename.startswith ("Cisco_FTD_SSP_FP1K_Hotfix") or
        filename.startswith ("Cisco_FTD_SSP_FP2K_Hotfix") or
        filename.startswith ("Cisco_FTD_SSP_FP3K_Hotfix") or
        filename.startswith ("Cisco_FTD_SSP_Hotfix")
        ):
        sec_fpr_hotfixes (filename)

    elif (
        filename.startswith ("cisco-asa-fp1k.") or
        filename.startswith ("cisco-ftd-fp1k") or
        filename.startswith ("Cisco_FTD_SSP_FP1K_Upgrade-") or
        filename.startswith ("Cisco_FTD_SSP_FP1K_Patch-") or
        filename.startswith ("fxos-mibs-fp1k") 
    ):
        sec_fp1k (filename)

    elif (
        filename.startswith ("cisco-asa-fp2k.") or
        filename.startswith ("cisco-ftd-fp2k") or
        filename.startswith ("Cisco_FTD_SSP_FP2K_Upgrade-") or
        filename.startswith ("Cisco_FTD_SSP_FP2K_Patch-") or
        filename.startswith ("fxos-mibs-fp2k") 
    ):
        sec_fp2k (filename)

    elif (
        filename.startswith ("cisco-asa-fp3k.") or
        filename.startswith ("cisco-ftd-fp3k") or
        filename.startswith ("Cisco_FTD_SSP_FP3K_Upgrade-") or
        filename.startswith ("Cisco_FTD_SSP_FP3K_Patch-") or
        filename.startswith ("fxos-mibs-fp3k") 
    ):
        sec_fp3k (filename)

    elif (
        filename.startswith ("cisco-asa-fp4200") or
        filename.startswith ("Cisco_Secure_FW_TD_4200_Patch-") or
        filename.startswith ("Cisco_Secure_FW_TD_4200-") or
        filename.startswith ("fxos-mibs-fp4200.")
    ):
        sec_fp4200 (filename)

    elif (
        filename.startswith ("cisco-asa.") or
        filename.startswith ("cisco-ftd.") or
        filename.startswith ("Cisco_FTD_SSP_Upgrade-") or
        filename.startswith ("Cisco_FTD_SSP_Patch-") or
        filename.startswith ("fxos-mibs") 
    ):
        sec_fp4k_9k (filename)

    elif(
    filename.startswith ("cisco-asa")
    ):
        sec_fp_asa_module (filename)

    elif(
    filename.startswith ("cisco-ftd.") and     filename.endswith ("csp")
    ):
        sec_fp_ftd_module (filename)

    elif(
    filename == "firepower-mibs.zip"
    ):
        prodname = product("firepower")
        imagecode = imagelookup("mibs")
        utilssinglemove (filename,prodname,imagecode)

    elif filename in {"BOOTX64.EFI", "grub.efi"}:
        prodname = product("ise")
        imagecode = "2.4/APPLIANCE-BOOT-SECTOR"
        utilssinglemove(filename, prodname, imagecode)

    elif filename.startswith(("SNS-35x5-BIOS", "SNS-35xx-BIOS", "SNS-35x5-firmware", "SNS-35xx-firmware",
                              "upd-pkg-SNS-35x5-cimc", "upd-pkg-SNS-35xx-cimc")):
        prodname = product("ise")
        imagecode = imagelookup("sns35xx")
        sec_ise_bios(filename, prodname, imagecode)

    elif filename.startswith(("SNS-36xx-BIOS", "SNS-36xx-firmware", "upd-pkg-SNS-36xx-cimc", "SNS-36xx-HUU")):
        prodname = product("ise")
        imagecode = imagelookup("sns36xx")
        sec_ise_bios(filename, prodname, imagecode)

    elif filename.startswith("SNS-37xx-"):
        prodname = product("ise")
        imagecode = imagelookup("sns37xx")
        sec_ise_bios(filename, prodname, imagecode)

    elif filename.startswith("SNS-38xx-"):
        prodname = product("ise")
        imagecode = imagelookup("sns38xx")
        sec_ise_bios(filename, prodname, imagecode)

    elif (
        filename.startswith(("ise-pic", "pic", "Cisco-ISE-PIC"))
        or filename in {"pic-2.2.0.470.SPA.x86_64.iso", "pic-2.4.0.357.SPA.x86_64.iso"}
    ):
        sec_ise_pic(filename)

    elif (
        filename in {"README_ISE_20_201_21_22"}
        or filename.startswith(("PI", "Cisco-vISE", "Cisco-ISE", "ISE", "ise", "mac-spw-dmg", "webagent", "win_spw", "ACS-MigrationApplication"))
    ):
        sec_ise(filename)

    elif filename.startswith("asdm"):
        sec_asa_asdm (filename)

    elif filename.startswith("c6svc-fwm-k9"):
        sec_fwsm (filename)

    elif filename.startswith("csd"):
        sec_csd (filename)

    elif filename.startswith("asasfr"):
        sec_asa_fp_sys (filename)

    elif (
    filename.startswith("asac") or
    filename.startswith("asav") or
    filename.startswith("asa")
    ):
        sec_asa_firmware (filename)

    elif filename.startswith("Cisco_Firepower_SRU") or filename.startswith("Sourcefire_Rule_Update"):
        sec_fp_rules (filename)

    elif filename.startswith("Cisco_Firepower_GEODB") or filename.startswith("Sourcefire_Geodb"):
        sec_fp_geodb (filename)

    elif filename.startswith("lsp-rel-"):
        sec_fp_lsp (filename)

    elif filename.startswith("Cisco_Firepower_NGIPS_Appliance_Patch-"):
        prodname = product("firepower")
        imagecode = imagelookup("sourcefiredev")
        splitbydash = filename.split("-")
        workname = splitbydash[1]
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif filename.startswith("Cisco_VDB_Fingerprint_Database") or filename.startswith("Sourcefire_VDB"):
        sec_fp_vdb (filename)

    elif filename.startswith("hostscan_"):
        sec_hostscan (filename)

    elif (
    filename.startswith("fxos") or 
    filename.startswith("firepower")
    ):
        sec_fxos (filename)

    elif (
    filename.startswith("Sourcefire_3D_Defense_Center_S3_Patch") or 
    filename.startswith("Sourcefire_3D_Defense_Center_S3_Hotfix")
    ):
        sec_sourcefire_fmc_patch (filename)

    elif (
    filename.startswith("Sourcefire_3D_Device_S3_Patch") or 
    filename.startswith("Sourcefire_3D_Device_VMware_Patch")
    ):
        sec_sourcefire_device (filename)

    elif filename.startswith("Cisco_Network_Sensor"):
        sec_fp_asa_mode (filename)

    elif (
        filename.startswith("ACS") or 
        filename.startswith("Acs") or 
        filename.startswith("Clean") or 
        filename.startswith("UCP") or 
        filename.startswith("applAcs") or 
        filename.startswith("5-") or 
        filename == "ACS57BasePatch.tar.gz" or 
        filename == "ReadMe_for_ACS_5.6_Upgrade_Package-txt"
    ):
        sec_acs (filename)

    elif (
        filename.startswith ("csmars")
    ):
        sec_mars_os (filename)

    elif (
        filename == "pnLogAgent_1.1.zip" or 
        filename == "pnLogAgent_4-1-3.zip" or 
        filename == "pnLogAgent_4-1-3.zip.txt" or 
        filename == "README_WebAgent.txt" or 
        filename == "webAgent_1-0.zip" or 
        filename == "webAgent_1-0.zip.txt" or 
        filename == "webAgent_1-1.zip" or 
        filename == "webAgent_1-1.zip.txt"
    ):
        prodname = product("mars")
        imagecode = imagelookup("logagent")
        utilssinglemove (filename,prodname,imagecode)

    elif (
        filename.startswith ("fcs-csm") or 
        filename.startswith ("fcs-CSM") or 
        filename.startswith ("fcs-cms") or 
        filename.startswith ("fcs-mcp") or 
        filename.startswith ("csm") or 
        filename.startswith ("CSM") or 
        filename.startswith ("fcs-mcp") or
        filename.startswith ("fcs-rme")
    ):
        sec_csm (filename)

    elif (
        filename.startswith ("UTD-STD-SIGNATURE")
    ):
        sec_utd_signature (filename)

    elif (
    filename.startswith("iosxe-utd") or 
    filename.startswith("iox-iosxe-utd") or 
    filename.startswith("secapp-ucmk9") or 
    filename.startswith("secapp-utd") or
    filename.startswith("iosxe-utd-ips")
    ):
        sec_utd_engine (filename)

    elif (
    filename.startswith("Sourcefire_Defense_Center_S3") or 
    filename.startswith("Sourcefire_Defense_Center_Virtual64_VMware") or 
    filename.startswith("Cisco_Firepower_Management_Center_Virtual_VMware") or 
    filename.startswith("Cisco_Firepower_Management_Center_Virtual") or 
    filename.startswith("Cisco_Firepower_Management_Center_VMware")
    ):
        sec_fp_mgmt (filename)

    elif (
        filename.startswith ("IPS") or 
        filename.startswith ("IDS") or 
        filename.startswith("128MB.sdf") or 
        filename.startswith("256MB.sdf") or 
        filename.startswith ("IOS") and filename.endswith ("-CLI.pkg")
    ):
        sec_classic_ips (filename)

    elif (
        filename.startswith ("fcs-csamc-") or 
        filename == "fcs-csa-hotfix-5.2.0.238-w2k3-k9-CSM.zip"
    ):
        workname = filename.replace("fcs-csamc-hotfix-","")
        workname = workname.replace("fcs-csamc-","")
        workname = workname.replace("fcs-csa-hotfix-","")
        workname = workname.replace("-w2k-k9.zip","")
        workname = workname.replace("-w2k3r2-k9.zip","")
        workname = workname.replace("-w2k3-k9.zip","")
        workname = workname.replace("-w2k3-k9-CSM.zip","")
        workname = workname.replace("-CSA-Policy-Descriptions.zip","")
        prodname = product("csa")
        utils_dev_v2_vf (filename,prodname,workname)

    elif (
        filename.startswith ("CiscoCM-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CiscoCVP-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CiscoICM-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CiscoISN-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CiscoPA-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CiscoUnity-CSA-") and filename.endswith (".export") or 
        filename.startswith ("CUCM-CSA-") and filename.endswith (".export")
    ):
        imagecode = imagelookup("templates")
        prodname = product("csa")
        utilssinglemove (filename,prodname,imagecode)

    elif (
        filename.startswith ("vpnclient") or 
        filename == "VPN-5.0.00.0340-MSI.exe" or 
        filename == "Vista-VPN-Troubleshooting.txt" or 
        filename == "VPN_Client_Support_Matrix2.txt" or 
        filename.startswith ("update-") and filename.endswith ("-major-K9.zip")
    ):
        sec_ipsec_client (filename)

    elif (
        filename.startswith ("SSM_On-Prem") 
    ):
        sec_ssm_onprem (filename)

    else:
        messageunknownfile()
        
        
def sec_ise_bios(filename, prodname, imagecode):  # ISE BIOS / Firmware
    logging.debug("Sub: sec_ise_bios")

    # Map versions to the set of filenames that belong to them
    VERSION_MAP = {
        "3.0.3f": {
            "SNS-35x5-BIOS-3-0-3c-0_ISE1_signed.cap",
            "upd-pkg-SNS-35x5-cimc.full.3.0.3f.bin",
        },
        "3.0.4j": {
            "SNS-35x5-BIOS-3-0-4b-0_ISE2a_signed.cap",
            "upd-pkg-SNS-35x5-cimc.full.3.0.4j.bin",
            "SNS-35x5-firmware-3-0-4j_upgrade_guide.zip",
        },
        "2.0.9c": {
            "SNS-35x5-BIOS-2-0-9a-0_ISE1a_signed.cap",
            "upd-pkg-SNS-35x5-cimc.full.2.0.9c.bin",
        },
        "4.0.2h": {
            "upd-pkg-SNS-35xx-cimc.full.4.0.2h.bin",
            "SNS-35xx-BIOS-4-0-2d-0_ISE.cap",
            "SNS-35xx-firmware-4-0-2h_upgrade_guide.zip",
        },
        "4.0.2n": {
            "upd-pkg-SNS-35xx-cimc.full.4.0.2n.bin",
            "SNS-35xx-BIOS-4-0-2f-0_ISE.cap",
            "SNS-35xx-firmware-4-0-2n_upgrade_guide.zip",
        },
        "4.1.2m": {
            "upd-pkg-SNS-35xx-cimc.full.4.1.2m.bin",
            "SNS-35xx-firmware-4-1-2m_upgrade_guide.zip",
        },
        "4.3.2b": {
            "SNS-36xx-BIOS-4-3-2b_ISE.cap",
            "SNS-36xx-HUU-4.3.2.240053_ISE.iso",
            "SNS-36xx-HUU-4.3.2.240077_ISE.iso",
        },
        "4.2.3g": {
            "SNS-37xx-BIOS-4-2-3c-0_ISE.pkg",
            "SNS-37xx-HUU-4.2.3g_ISE.iso",
        },
        "4.3.2e": {
            "SNS-37xx-BIOS-4-3-2e_ISE.pkg",
            "SNS-37xx-HUU-4.3.2.240009_ISE.iso",
        },
        "4.3.2c": {
            "SNS-37xx-BIOS-4-3-2c_ISE.pkg",
            "SNS-37xx-HUU-4.3.2.230207_ISE.iso",
            "SNS-36xx-BIOS-4-3-2c_ISE.cap",
            "SNS-36xx-HUU-4.3.2.240107_ISE.iso",
        },
        "4.3.4a": {
            "SNS-37xx-BIOS-4-3-4a_ISE.pkg",
            "SNS-37xx-HUU-4.3.4.240152_ISE.iso",
            "SNS-37xx-HUU-4.3.4.241063_ISE.iso",
        },
        "4.3.4b": {
            "SNS-37xx-BIOS-4-3-4b_ISE.pkg",
            "SNS-37xx-HUU-4.3.4.242038_ISE.iso",
        },
        "4.3.4d": {
            "SNS-37xx-BIOS-4-3-4d_ISE.pkg",
            "SNS-37xx-HUU-4.3.5.250001_ISE.iso",
        },
        "4.3.6a": {
            "SNS-37xx-BIOS-4-3-6a_ISE.pkg",
            "SNS-37xx-HUU-4.3.6.250040_ISE.iso",
        },
        "4.3.2a": {
            "SNS-36xx-BIOS-4-3-2a_ISE.cap",
            "SNS-36xx-HUU-4.3.2.230207_ISE.iso",
            "SNS-36xx-HUU-4.3.2.240009_ISE.iso",
        },
        "4.2.3d": {
            "SNS-36xx-BIOS-4-2-3c-0_ISE.cap",
            "SNS-36xx-HUU-4.2.3d_ISE.iso",
        },
        "4.2.2a": {
            "SNS-36xx-BIOS-4-2-2b-0_ISE.cap",
            "SNS-36xx-HUU-4.2.2a_ISE.iso",
        },
        "4.1.3i": {
            "SNS-36xx-BIOS-4-1-3m-0_ISE.cap",
            "SNS-36xx-HUU-4.1.3i_ISE.iso",
        },
        "4.1.3b": {
            "SNS-36xx-BIOS-4-1-3e-0_ISE.cap",
            "SNS-36xx-HUU-4.1.3b_ISE.iso",
        },
        "4.0.4m": {
            "SNS-36xx-firmware-4-0-4m_upgrade_guide.zip",
            "SNS-36xx-BIOS-4-0-4q-0_ISE.cap",
            "upd-pkg-SNS-36xx-cimc.full.4.0.4m.bin",
        },
        "4.0.1g": {
            "SNS-36xx-firmware-4-0-1g_upgrade_guide.zip",
            "SNS-36xx-BIOS-4-0-1i-0_ISE.cap",
            "upd-pkg-SNS-36xx-cimc.full.4.0.1g.bin",
        },
        "4.0.4h": {
            "SNS-36xx-firmware-4-0-4h_upgrade_guide.zip",
            "upd-pkg-SNS-36xx-cimc.full.4.0.4h.bin",
            "SNS-36xx-BIOS-4-0-4i-0_ISE.cap",
        },
        "4.3.2f": {
            "SNS-36xx-BIOS-4-3-2f_ISE.cap",
            "SNS-36xx-HUU-4.3.2.250045_ISE.iso",
        },
        "6.0.1a": {
            "SNS-38xx-BIOS-6-0-1a_ISE.pkg",
            "SNS-38xx-HUU-6.0.1.250127_ISE.iso",
        },
    }

    # Build reverse map: filename -> version
    filename_to_version = {
        fname: ver for ver, files in VERSION_MAP.items() for fname in files
    }

    version = filename_to_version.get(filename, "UNKNOWN")

    if version == "UNKNOWN":
        messageunknownversion()
    else:
        filepath = filepath3(prodname, imagecode, version)
        filemove(filepath, filename)

def sec_ise_hotfix (filename): #ISE Hotfixes
    logging.debug("Sub:    sec_ise_hotfix")
    prodname = product("ise")
    if (
        filename == "ise-apply-CSCwb29140_2.7.0.356_patch7-SPA.tar.gz" or
        filename == "ise-rollback-CSCwb29140_2.7.0.356_patch7-SPA.tar.gz"
    ):
        version = "3.2"
        patchversion = "7"
        imagecode1 = imagelookup("patch")
        imagecode2 = imagelookup("hotfix")
        final = patchversion + "-" + imagecode2
        filepath = filepath43(prodname,version,imagecode1,final)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCwi06794_3.0.0.458_patch8-SPA.tar.gz"
    ):
        version = "3.0"
        patchversion = "8"
        imagecode1 = imagelookup("patch")
        imagecode2 = imagelookup("hotfix")
        final = patchversion + "-" + imagecode2
        filepath = filepath4(prodname,version,imagecode1,final)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_1.4_common_1-SPA.tar.gz"
    ):
        version = "1.4"
        imagecode = imagelookup("universal")
        filepath = filepath3(prodname,version,imagecode)
        filemove (filepath, filename)

    elif (
        filename == "ise-apply-CSCvm14030_2.0.0.306_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.0.0.306_common_1-SPA.tar.gz"
    ):
        version = "2.0"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_2.0.1.130_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.0.1.130_common_1-SPA.tar.gz"
    ):
        version = "2.0.1"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_2.1.0.474_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.1.0.474_common_1-SPA.tar.gz"
    ):
        version = "2.1"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_2.2.0.470_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.2.0.470_common_1-SPA.tar.gz"
    ):
        version = "2.2"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_2.3.0.298_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.3.0.298_common_1-SPA.tar.gz"
    ):
        version = "2.3"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCvm14030_2.4.0.357_common_1-SPA.tar.gz" or
        filename == "ise-rollback-CSCvm14030_2.4.0.357_common_1-SPA.tar.gz"
    ):
        version = "2.4"
        imagecode = imagelookup("universal")
        imagecode2  = "CSCvm14030"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCwm88519_3.3.0.430_patch4-SPA.tar.gz" or
        filename == "ise-rollback-CSCwm88519_3.3.0.430_patch4-SPA.tar.gz"
    ):
        version = "3.3"
        imagecode = imagelookup("patch")
        imagecode2 = "4-" + imagelookup("hotfix") + "-CSCwm88519"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCwo99449_3.3.0.430_patch4-SPA.tar.gz" or
        filename == "ise-rollback-CSCwo99449_3.3.0.430_patch4-SPA.tar.gz"
    ):
        version = "3.3"
        imagecode = imagelookup("patch")
        imagecode2 = "4-" + imagelookup("hotfix") + "-CSCwo99449"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-rollback-CSCwk61938_3.1_patchall-SPA.tar.gz" or
        filename == "ise-apply-CSCwk61938_3.1_patchall-SPA.tar.gz"
    ):
        version = "3.1"
        imagecode = imagelookup("patch")
        imagecode2 = imagelookup("universal")
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-rollback-CSCwk61938_3.2_patchall-SPA.tar.gz" or
        filename == "ise-apply-CSCwk61938_3.2_patchall-SPA.tar.gz" or
        filename == "ise-apply-CSCwf02093_3.2.x_patchall-SPA.tar.gz"
    ):
        version = "3.2"
        imagecode = imagelookup("patch")
        imagecode2 = imagelookup("universal")
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCwi47249_3.2.0.542_patch7-SPA.tar.gz"
    ):
        version = "3.2"
        imagecode = imagelookup("patch")
        imagecode2 = "7-" + imagelookup("hotfix")
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)
    elif (
        filename == "ise-apply-CSCwo99449_3.4.0.608_patch1-SPA.tar.gz" or
        filename == "ise-rollback-CSCwo99449_3.4.0.608_patch1-SPA.tar.gz"
    ):
        version = "3.4"
        imagecode = imagelookup("patch")
        imagecode2 = "1-" + imagelookup("hotfix") + "CSCwo99449"
        filepath = filepath4(prodname,version,imagecode,imagecode2)
        filemove (filepath, filename)


def sec_anyconnect (filename): #Anyconnect / Cisco Secure Client
    logging.debug("Sub:    sec_anyconnect")
    prodcode = product("anyconnect")
    if (
        filename.startswith("hostscan_") or
        filename.startswith("hostscan-posture-linux-x64-") or
        filename.startswith("hostscan-posture-macosx-i386-") or
        filename.startswith("hostscan-win-")
    ):
        workname = filename.replace("hostscan_","")
        workname = workname.replace("hostscan-posture-linux-x64-","")
        workname = workname.replace("hostscan-posture-macosx-i386-","")
        workname = workname.replace("hostscan-win-","")
        workname = workname.replace("-k9.pkg","")
        workname = workname.replace("-pre-deploy-k9.tar.gz","")
        workname = workname.replace("-pre-deploy-k9.dmg","")
        workname = workname.replace("-pre-deploy-k9.msi","")
        imagecode = imagelookup("hostscan")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath4(prodcode,imagecode,versionmain,workname)
        filemove (filepath, filename)
    elif (
        filename.endswith("-isecompliance-webdeploy-k9.pkg") or
        filename.endswith("-isecompliance-predeploy-k9.tar.gz")
    ):
        workname = filename.replace("-isecompliance-predeploy-k9.tar.gz","")
        workname = workname.replace("-isecompliance-webdeploy-k9.pkg","")
        workname = workname.replace("-k9.pkg","")
        workname = workname.replace("-k9.tar.gz","")
        imagecode = imagelookup("isecompliance")
        if filename.startswith("cisco-secure-client-linux64-"):
            imagecode2 = imagelookup("linux")
            workname = workname.replace("cisco-secure-client-linux64-","")
            filepath = filepath4(prodcode,imagecode,imagecode2,workname)
            filemove (filepath, filename)
    #Cisco Secure Client Posture Module
    elif (
        filename.startswith("secure-firewall-posture-")
    ):
        workname = filename.replace("secure-firewall-posture-","")
        workname = workname.replace("-k9.pkg","")
        imagecode = imagelookup("anyconnect_posture")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath4(prodcode,imagecode,versionmain,workname)
        filemove (filepath, filename)
    #Cisco Secure Client Profile Editor
    elif (
        filename.startswith("tools-cisco-secure-client-win-") and
        filename.endswith("-profileeditor-k9.msi")
        
    ):
        workname = filename.replace("tools-cisco-secure-client-win-","")
        workname = workname.replace("-profileeditor-k9.msi","")
        imagecode = imagelookup("profileeditor")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath4(prodcode,imagecode,versionmain,workname)
        filemove (filepath, filename)
    #Cisco Secure Client Transforms
    elif (
        filename.startswith("tools-cisco-secure-client-win-") and
        filename.endswith("-transforms.zip")
        
    ):
        workname = filename.replace("tools-cisco-secure-client-win-","")
        workname = workname.replace("-transforms.zip","")
        imagecode = imagelookup("transforms")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath4(prodcode,imagecode,versionmain,workname)
        filemove (filepath, filename)
    #Cisco Secure Client SSO Module
    elif (
        filename.startswith("external-sso-") and
        filename.endswith("-webdeploy-k9.pkg")
        
    ):
        workname = filename.replace("external-sso-","")
        workname = workname.replace("-webdeploy-k9.pkg","")
        imagecode = imagelookup("external-sso")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath4(prodcode,imagecode,versionmain,workname)
        filemove (filepath, filename)
    elif (
        filename.startswith("anyconnect-win-") or
        filename.startswith("anyconnect-gina-win-") or
        filename.startswith("anyconnect-wince-ARMv4I-")
    ):
        workname = filename.replace("anyconnect-win-","")
        workname = workname.replace("anyconnect-gina-win-","")
        workname = workname.replace("anyconnect-wince-ARMv4I-","")
        workname = workname.replace("activesync-","")
        workname = workname.replace("-k9.pkg","")
        workname = workname.replace("-k9.cab","")
        workname = workname.replace("-k9.msi","")
        workname = workname.replace("-pre-deploy-k9.msi","")
        workname = workname.replace("-pre-deploy-k9-lang.zip","")
        workname = workname.replace("-web-deploy-k9-lang.zip","")
        workname = workname.replace("-web-deploy-k9.exe","")
        imagecode = imagelookup("client")
        imagecode2 = imagelookup("windows")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath5(prodcode,imagecode,imagecode2,versionmain,workname)
        filemove (filepath, filename)
    elif (
        filename.startswith("anyconnect-linux-") or
        filename.startswith("cisco-secure-client-linux64-")
    ):
        workname = filename.replace("anyconnect-linux-","")
        workname = workname.replace("cisco-secure-client-linux64-","")
        workname = workname.replace("-webdeploy-k9.pkg","")
        workname = workname.replace("-predeploy-deb-k9.tar.gz","")
        workname = workname.replace("-predeploy-rpm-k9.tar.gz","")
        workname = workname.replace("-predeploy-k9.tar.gz","")
        workname = workname.replace("-k9.pkg","")
        workname = workname.replace("-k9.tar.gz","")
        imagecode = imagelookup("client")
        imagecode2 = imagelookup("linux")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath5(prodcode,imagecode,imagecode2,versionmain,workname)
        filemove (filepath, filename)
    elif (
        filename.startswith("anyconnect-macosx-powerpc-") or
        filename.startswith("anyconnect-macosx-i386-")
    ):
        workname = filename.replace("anyconnect-macosx-powerpc-","")
        workname = workname.replace("anyconnect-macosx-i386-","")
        workname = workname.replace("-k9.pkg","")
        workname = workname.replace("-k9.tar.gz","")
        imagecode = imagelookup("client")
        imagecode2 = imagelookup("macintosh")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        filepath = filepath5(prodcode,imagecode,imagecode2,versionmain,workname)
        filemove (filepath, filename)



def sec_fp1k (filename): #Firepower 1010/11xx Firewalls
    logging.debug("Sub:    sec_fp1k")
    prodname = product("firepower1k")
    if filename.startswith("fxos-mibs-fp1k"):
        imagecode = imagelookup("mibs")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("cisco-ftd-fp1k"):
        imagecode = imagelookup("fpftdmodule")
        workname = filename.replace("cisco-ftd-fp1k.","")
        workname = workname.replace(".SPA","")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("cisco-asa-fp1k."):
        imagecode = imagelookup("fpasamodule")
        workname = filename.replace("cisco-asa-fp1k.","")
        workname = workname.replace(".SPA","")
        aftersplit = workname.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP1K_Patch"):
        imagecode = imagelookup("patch")
        workname = filename.replace("Cisco_FTD_SSP_FP1K_Patch-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP1K_Upgrade"):
        imagecode = imagelookup("upgrade")
        workname = filename.replace("Cisco_FTD_SSP_FP1K_Upgrade-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)

def sec_fp2k (filename): #Firepower 21xx Firewalls
    logging.debug("Sub:    sec_fp2k")
    prodname = product("firepower2k")
    if filename.startswith("fxos-mibs-fp2k"):
        imagecode = imagelookup("mibs")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("cisco-ftd-fp2k"):
        imagecode = imagelookup("fpftdmodule")
        workname = filename.replace("cisco-ftd-fp2k.","")
        workname = workname.replace(".SPA","")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("cisco-asa-fp2k."):
        imagecode = imagelookup("fpasamodule")
        workname = filename.replace("cisco-asa-fp2k.","")
        workname = workname.replace(".SPA","")
        aftersplit = workname.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP2K_Patch"):
        imagecode = imagelookup("patch")
        workname = filename.replace("Cisco_FTD_SSP_FP2K_Patch-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP2K_Upgrade"):
        imagecode = imagelookup("upgrade")
        workname = filename.replace("Cisco_FTD_SSP_FP2K_Upgrade-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)

def sec_fp3k (filename): #Firepower 31xx Firewalls
    logging.debug("Sub:    sec_fp3k")
    prodname = product("firepower3k")
    if filename.startswith("fxos-mibs-fp3k"):
        imagecode = imagelookup("mibs")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("cisco-ftd-fp3k"):
        imagecode = imagelookup("fpftdmodule")
        workname = filename.replace("cisco-ftd-fp3k.","")
        workname = workname.replace(".SPA","")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("cisco-asa-fp3k."):
        imagecode = imagelookup("fpasamodule")
        workname = filename.replace("cisco-asa-fp3k.","")
        workname = workname.replace(".SPA","")
        aftersplit = workname.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP3K_Patch"):
        imagecode = imagelookup("patch")
        workname = filename.replace("Cisco_FTD_SSP_FP3K_Patch-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_FP3K_Upgrade"):
        imagecode = imagelookup("upgrade")
        workname = filename.replace("Cisco_FTD_SSP_FP3K_Upgrade-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)

def sec_fp4k_9k (filename): #Firepower 31xx Firewalls
    logging.debug("Sub:    sec_fp4k_9k")
    prodname = product("firepower4k9k")
    if filename.startswith("fxos-mibs"):
        imagecode = imagelookup("mibs")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("cisco-ftd"):
        imagecode = imagelookup("fpftdmodule")
        workname = filename.replace("cisco-ftd.","")
        workname = workname.replace(".SPA.csp","")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("cisco-asa."):
        imagecode = imagelookup("fpasamodule")
        workname = filename.replace("cisco-asa.","")
        workname = workname.replace(".SPA.csp","")
        aftersplit = workname.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_Patch"):
        imagecode = imagelookup("patch")
        workname = filename.replace("Cisco_FTD_SSP_Patch-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
    elif filename.startswith("Cisco_FTD_SSP_Upgrade"):
        imagecode = imagelookup("upgrade")
        workname = filename.replace("Cisco_FTD_SSP_Upgrade-","")
        aftersplit = workname.split(".")
        head, sep, tail = workname.partition('-')
        aftersplit = head.split(".")
        ver2 = util2digit (aftersplit[0],aftersplit[1])
        if len(aftersplit) == 3:
            verfull = util3digit (aftersplit[0],aftersplit[1],aftersplit[2])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)
        elif len(aftersplit) == 4:
            verfull = util4digit (aftersplit[0],aftersplit[1],aftersplit[2],aftersplit[3])
            filepath = filepath4(prodname,imagecode,ver2,verfull)
            filemove (filepath, filename)

def sec_fp4200 (filename): #Firepower 4200 Firewalls
    logging.debug("Sub:    sec_fp4200")
    prodname = product("firepower4200")
    if filename.startswith("fxos-mibs-fp4200"):
        imagecode = imagelookup("mibs")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("cisco-asa-fp4200."):
        imagecode = imagelookup("fpasamodule")
        workname = filename.replace("cisco-asa-fp4200.","")
        workname = workname.replace(".SPA","")
        splitbydot = workname.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        if len(splitbydot) == 3:
            versionfull = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
        elif len(splitbydot) == 4:
            versionfull = util4digit (splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4(prodname,imagecode,versionmain,versionfull)
        filemove (filepath, filename)
    elif filename.startswith("Cisco_Secure_FW_TD_4200-"):
        imagecode = imagelookup("fpftdsoftware")
        workname = filename.replace("Cisco_Secure_FW_TD_4200-","")
        workname = workname.replace(".sh.REL.tar","")
        version, dash, throwaway = workname.partition('-')
        splitbydot = version.split(".")
        versionmain = util2digit (splitbydot[0],splitbydot[1])
        if len(splitbydot) == 3:
            versionfull = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        elif len(splitbydot) == 4:
            versionfull = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4(prodname,imagecode,versionmain,versionfull)
        filemove (filepath, filename)

def sec_fpr_hotfixes (filename): #Hotfixes
    logging.debug("Sub:    sec_fpr_hotfixes")
    filename_map = {
        "Cisco_Secure_FW_TD_4200_Patch-7.4.1.1-12.sh.REL.tar": {
            "prodname": "firepower4200", "imagecode": "fpftdsoftware", "versionmain": "7.4", "versionfull": "7.4.1"
        },
        "Cisco_FTD_SSP_FP1K_Hotfix_P-7.1.0.2-2.sh.REL.tar": {
            "prodname": "firepower1k", "imagecode": "fpftdsoftware", "versionmain": "7.1", "versionfull": "7.1.0.1"
        },
        "Cisco_FTD_SSP_FP2K_Hotfix_P-7.1.0.2-2.sh.REL.tar": {
            "prodname": "firepower2k", "imagecode": "fpftdsoftware", "versionmain": "7.1", "versionfull": "7.1.0.1"
        },
        "Cisco_FTD_SSP_Hotfix_P-7.1.0.2-2.sh.REL.tar": {
            "prodname": "firepower4k9k", "imagecode": "fpftdsoftware", "versionmain": "7.1", "versionfull": "7.1.0.1"
        },
        "Cisco_FTD_Hotfix_P-7.1.0.2-2.sh.REL.tar": {
            "prodname": "firepowertd", "imagecode": "fpftdsoftware", "versionmain": "7.1", "versionfull": "7.1.0.1"
        },
        "Cisco_FTD_SSP_FP3K_Hotfix_Q-7.1.0.3-2.sh.REL.tar": {
            "prodname": "firepower3k", "imagecode": "fpftdsoftware", "versionmain": "7.1", "versionfull": "7.1.0.1"
        }
    }
    details = filename_map.get(filename)
    if not details:
        logging.warning(f"Unrecognized filename in sec_fpr_hotfixes: {filename}")
        return

    prodname = product(details["prodname"])
    imagecode = imagelookup(details["imagecode"])
    filepath = filepath4(prodname, imagecode, details["versionmain"], details["versionfull"])
    filemove(filepath, filename)

def sec_ssm_onprem(filename):  
    """Process Cisco Smart License On-Prem Server filenames and move files accordingly."""
    logging.debug("Sub: sec_ssm_onprem")

    prodname = product("SSM_On-Prem")

    # Patterns to strip from filename
    patterns = [
        r"^SSM_On-Prem[_-]?",  # leading prefix with _ or -
        r"\.iso$",             # file extension
        r"_(Full|[Uu]pgrade|Documentation|Supplementary_Patch|AlmaLinux)\.zip$"
    ]

    workname = filename
    for pattern in patterns:
        workname = re.sub(pattern, "", workname)

    finalpath = filepath(prodname, workname)
    filemove(finalpath, filename)

def sec_ipsec_client (filename):
    logging.debug("Sub:    sec_ipsec_client")
    prodname = product("vpnclient")
    if filename.endswith(".txt"):
        imagecode = imagelookup("docs")
        utilssinglemove (filename,prodname,imagecode)
    elif filename.startswith ("update-") and filename.endswith ("-major-K9.zip"):
        imagecode = imagelookup("windows")
        workname = filename.replace("update-","")
        workname = workname.replace("-major-K9.zip","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif filename == "VPN-5.0.00.0340-MSI.exe":
        imagecode = imagelookup("windows")
        workname = filename.replace("VPN-","")
        workname = workname.replace("-MSI.exe","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif filename == "vpnclient-beta-rc-5.0.00.0320.exe":
        imagecode = imagelookup("windows")
        workname = filename.replace("vpnclient-beta-rc-","")
        workname = workname.replace(".exe","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("vpnclient-win-is-") or 
    filename.startswith("vpnclient-winx64-msi-") or 
    filename.startswith("vpnclient-win-msi-")
    ):
        imagecode = imagelookup("windows")
        workname = filename.replace("vpnclient-win-is-","")
        workname = workname.replace("vpnclient-win-msi-","")
        workname = workname.replace("vpnclient-winx64-msi-","")
        workname = workname.replace("-BETA-k9.exe","")
        workname = workname.replace("-k9-BETA.exe","")
        workname = workname.replace("-RC-k9.exe","")
        workname = workname.replace("-k9-BETA.exe","")
        workname = workname.replace("-k9-bundle.exe","")
        workname = workname.replace("-k9-jp_wohelp.exe","")
        workname = workname.replace("-k9-x86.exe","")
        workname = workname.replace("-k9.exe","")
        workname = workname.replace("-k9.zip","")
        workname = workname.replace(".Rel-k9.exe","")
        workname = workname.replace(".k9.exe","")
        workname = workname.replace(".k9.zip","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("vpnclient-darwin-")
    ):
        imagecode = imagelookup("macintosh")
        workname = filename.replace("vpnclient-darwin-","")
        workname = workname.replace("-GUI-k9.dmg","")
        workname = workname.replace("-universal-k9.dmg","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("vpnclient-linux-")  or 
    filename.startswith("vpnclient-linux-x86_64-")
    ):
        imagecode = imagelookup("linuxbare")
        workname = filename.replace("vpnclient-linux-x86_64-","")
        workname = workname.replace("vpnclient-linux-","")
        workname = workname.replace("-k9.tar.gz","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif (
    filename.startswith("vpnclient-solaris-")
    ):
        imagecode = imagelookup("solaris")
        workname = filename.replace("vpnclient-solaris-","")
        workname = workname.replace("-k9.tar.gz","")
        workname = workname.replace("-k9.tar.Z","")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

def sec_classic_ips (filename):
    logging.debug("Sub:    sec_classic_ips")
    prodname = product("ipsids")
    if (
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.0-1.pkg") or 
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.0-1.zip") or 
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.0-6.pkg") or 
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.0-5.pkg") or 
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.1-2.pkg") or 
    filename.startswith("IPS-sig-") and filename.endswith("-minreq-5.1-4.pkg")
    ):
        imagecode = imagelookup("signatures")
        engine = imagelookup("engine0")
        workname = filename.replace("IPS-sig-","")
        workname = workname.replace("-minreq-5.0-1.pkg","")
        workname = workname.replace("-minreq-5.0-1.zip","")
        workname = workname.replace("-minreq-5.0-5.pkg","")
        workname = workname.replace("-minreq-5.0-6.pkg","")
        workname = workname.replace("-minreq-5.1-2.pkg","")
        workname = workname.replace("-minreq-5.1-4.pkg","")
        filepath = filepath4(prodname,imagecode,engine,workname)
        filemove (filepath, filename)
    elif (
    filename.startswith("IDS-sig-4.1-5-") and filename.endswith(".zip")
    ):
        imagecode = imagelookup("signatures")
        engine = imagelookup("engine0")
        workname = filename.replace("IDS-sig-4.1-5-","")
        workname = workname.replace(".zip","")
        workname = workname.replace(".readme.txt","")
        filepath = filepath4(prodname,imagecode,engine,workname)
        filemove (filepath, filename)
    elif (
    filename.startswith("IPS-sig-")
    ):
        imagecode = imagelookup("signatures")
        workname = filename.replace("IPS-sig-","")
        if filename.endswith("-req-E1.pkg"):
            engine = imagelookup("engine1")
            workname = workname.replace("-req-E1.pkg","")
        elif filename.endswith("-req-E2.pkg"):
            engine = imagelookup("engine2")
            workname = workname.replace("-req-E2.pkg","")
        elif filename.endswith("-req-E3.pkg"):
            engine = imagelookup("engine3")
            workname = workname.replace("-req-E3.pkg","")
        elif filename.endswith("-req-E4.pkg"):
            engine = imagelookup("engine4")
            workname = workname.replace("-req-E4.pkg","")
        else:
            engine = imagelookup("engine0")
            workname = workname.replace(".readme.txt","")
        filepath = filepath4(prodname,imagecode,engine,workname)
        filemove (filepath, filename)
    elif (
    filename.startswith("IPS-CS-MARS-Sig-")
    ):
        imagecode = imagelookup("signatures")
        prodname = product("mars")
        workname = filename.replace("IPS-CS-MARS-Sig-","")
        workname = workname.replace(".zip","")
        filepath = filepath3(prodname,imagecode,workname)
        filemove (filepath, filename)
    elif (
    filename.startswith("IPS-CS-MGR-sig-")
    ):
        imagecode = imagelookup("signatures")
        prodname = product("csm")
        workname = filename.replace("IPS-CS-MGR-sig-","")
        workname = workname.replace("IPS-CS-MGR-Sig-","")
        if filename.endswith("-req-E1.zip"):
            engine = imagelookup("engine1")
            workname = workname.replace("-req-E1.zip","")
            filepath = filepath4(prodname,imagecode,engine,workname)
        elif filename.endswith("-req-E2.zip"):
            engine = imagelookup("engine2")
            workname = workname.replace("-req-E2.zip","")
            filepath = filepath4(prodname,imagecode,engine,workname)
        elif filename.endswith("-req-E3.zip"):
            engine = imagelookup("engine3")
            workname = workname.replace("-req-E3.zip","")
            filepath = filepath4(prodname,imagecode,engine,workname)
        elif filename.endswith("-req-E4.zip"):
            engine = imagelookup("engine4")
            workname = workname.replace("-req-E4.zip","")
            filepath = filepath4(prodname,imagecode,engine,workname)
#        else:
#            workname = workname.replace("zip","")
#            filepath = filepath3(prodname,imagecode,workname)
        filemove (filepath, filename)
    elif filename.startswith("IPS-CSM-K9-patch-"):
        prodname1 = product("csm")
        if filename == "IPS-CSM-K9-patch-7.3-5p1-E4.zip":
            imagecode = imagelookup("patch")
            version = "7.3.5.E4"
            filepath = filepath4(prodname1,"IPS",version,imagecode)
            filemove (filepath, filename)
        elif filename == "IPS-CSM-K9-patch-7.1-11p1-E4.zip":
            imagecode = imagelookup("patch")
            version = "7.1.11.E4"
            filepath = filepath4(prodname1,"IPS",version,imagecode)
            filemove (filepath, filename)
    elif filename.startswith("IPS-K9-r-1.1-a-"):
        imagecode = imagelookup("rcv")
        workname = filename.replace(".pkg","")
        workname = workname.replace("IPS-K9-r-1.1-a-","")
        workname = workname.replace("-",".")
        filepath = filepath3(prodname,workname,imagecode)
        filemove (filepath, filename)
    elif (
    filename == "IPS-4270_20-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-4345-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-4360-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-4510-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-4520-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_10-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_20-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_40-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_60-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_5512-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_5515-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_5525-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_5545-K9-patch-7.1-11p1-E4.pkg" or 
    filename == "IPS-SSP_5555-K9-patch-7.1-11p1-E4.pkg"
    ):
        imagecode = imagelookup("system")
        version = "7.1.11.E4"
        if filename.startswith("IPS-SSP_10-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp10")
        elif filename.startswith("IPS-SSP_20-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp20")
        elif filename.startswith("IPS-SSP_40-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp40")
        elif filename.startswith("IPS-SSP_60-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp60")
        elif filename.startswith("IPS-SSP_5512-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5512xssp")
        elif filename.startswith("IPS-SSP_5515-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5515xssp")
        elif filename.startswith("IPS-SSP_5525-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5525xssp")
        elif filename.startswith("IPS-SSP_5545-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5545xssp")
        elif filename.startswith("IPS-SSP_5555-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5555xssp")
        elif filename.startswith("IPS-4240-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4240")
        elif filename.startswith("IPS-4255-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4255")
        elif filename.startswith("IPS-4260-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4260")
        elif filename.startswith("IPS-4270_20-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4270")
        elif filename.startswith("IPS-4345-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4345")
        elif filename.startswith("IPS-4360-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4360")
        elif filename.startswith("IPS-4510-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4510")
        elif filename.startswith("IPS-4520-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4520")
        #filepath = filepath3(prodname,version,imagecode)
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif (
    filename == "IPS-4345-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-4360-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-4510-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-4520-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_10-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_20-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_40-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_5512-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_5515-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_5525-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_5545-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_5555-K9-patch-7.3-5p1-E4.pkg" or 
    filename == "IPS-SSP_60-K9-patch-7.3-5p1-E4.pkg"
    ):
        imagecode = imagelookup("system")
        version = "7.3.5.E4"
        if filename.startswith("IPS-SSP_10-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp10")
        elif filename.startswith("IPS-SSP_20-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp20")
        elif filename.startswith("IPS-SSP_40-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp40")
        elif filename.startswith("IPS-SSP_60-"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5585xssp60")
        elif filename.startswith("IPS-SSP_5512-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5512xssp")
        elif filename.startswith("IPS-SSP_5515-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5515xssp")
        elif filename.startswith("IPS-SSP_5525-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5525xssp")
        elif filename.startswith("IPS-SSP_5545-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5545xssp")
        elif filename.startswith("IPS-SSP_5555-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsasa5555xssp")
        elif filename.startswith("IPS-4240-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4240")
        elif filename.startswith("IPS-4255-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4255")
        elif filename.startswith("IPS-4260-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4260")
        elif filename.startswith("IPS-4270_20-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4270")
        elif filename.startswith("IPS-4345-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4345")
        elif filename.startswith("IPS-4360-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4360")
        elif filename.startswith("IPS-4510-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4510")
        elif filename.startswith("IPS-4520-K9"):
            prodname1 = product("ipsids")
            prodname2 = product("ipsidsips4520")
        #filepath = filepath3(prodname,version,imagecode)
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4215-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4215")
        if filename.startswith("IPS-4215-K9-sys"):
            imagecode = imagelookup("system")
        elif filename.startswith("IPS-4215-K9-r"):
            imagecode = imagelookup("rcv")
        else:
            imagecode = imagelookup("patch")
        if imagecode == "PATCH":
            splitbydash = filename.split("-",3)
            version = splitbydash[3].replace(".pkg","")
            version = version.replace("-",".")
            filepath = filepath4(prodname1,version,prodname2,imagecode)
            filemove (filepath, filename)
        else:
            splitbydash = filename.split("-",6)
            version = splitbydash[6].replace(".img","")
            version = version.replace("-",".")
            filepath = filepath4(prodname1,version,prodname2,imagecode)
            filemove (filepath, filename)

    elif filename.startswith("IPS-4240-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4240")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4255-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4255")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4260-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4260")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4270_20-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4270")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4345-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4345")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4360-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4360")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4510-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4510")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4520-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4520")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-AIM-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsaim")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-IDSM2-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("system")
        workname = filename.replace("IPS-IDSM2-K9-sys-1.1-a-","")
        version = workname.replace(".bin.gz","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM-CIDS-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("system")
        workname = filename.replace("IPS-NM-CIDS-K9-sys-1.1-a-","")
        version = workname.replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NME-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM_CIDS-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSC_5-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassc")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_10-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_20-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm20")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_40-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm40")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_10-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp10")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_20-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp20")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_40-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp40")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_60-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp60")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5512-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5512xssp")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5515-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5515xssp")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5525-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5525xssp")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5545-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5545xssp")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5555-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5555xssp")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("WS-SVC-IDSM2-K9-sys"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("system")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".img","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4240-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4240")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4255-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4255")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4260-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4260")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4270_20-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4270")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4345-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4345")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4360-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4360")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4510-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4510")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4520-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4520")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-AIM-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsaim")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-IDSM2-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM-CIDS-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NME-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM_CIDS-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSC_5-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassc")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_10-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_20-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm20")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_40-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm40")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_10-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp10")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_20-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp20")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_40-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp40")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_60-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp60")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5512-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5512xssp")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5515-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5515xssp")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5525-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5525xssp")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5545-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5545xssp")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5555-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5555xssp")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("WS-SVC-IDSM2-K9-r"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("rcv")
        splitbydash = filename.split("-",6)
        version = splitbydash[6].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4240-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4240")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4255-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4255")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4260-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4260")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4270_20-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4270")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4345-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4345")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4360-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4360")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4510-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4510")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-4520-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsips4520")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-AIM-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsaim")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-IDSM2-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM-CIDS-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NME-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-NM_CIDS-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsnm")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSC_5-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassc")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_10-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm10")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_20-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm20")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSM_40-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasassm40")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_10-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp10")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_20-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp20")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_40-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp40")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_60-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5585xssp60")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5512-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5512xssp")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5515-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5515xssp")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5525-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5525xssp")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5545-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5545xssp")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("IPS-SSP_5555-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsasa5555xssp")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("WS-SVC-IDSM2-K9"):
        prodname1 = product("ipsids")
        prodname2 = product("ipsidsipsadsm2")
        imagecode = imagelookup("patch")
        splitbydash = filename.split("-",3)
        version = splitbydash[3].replace(".pkg","")
        version = version.replace("-",".")
        filepath = filepath4(prodname1,version,prodname2,imagecode)
        filemove (filepath, filename)
    elif (
        filename.startswith("IOS-S") and filename.endswith("-CLI.pkg") or 
        filename.startswith("IOS-S") and filename.endswith(".zip") or 
        filename.startswith("128MB.sdf") or 
        filename.startswith("256MB.sdf")
        
        ):
            prodname = product ("iosids")
            imagecode = imagelookup ("signatures")
            utilssinglemove (filename,prodname,imagecode)
'''
    elif (
    filename.startswith("IPS-4510-K9-") and filename.endswith("-E4.pkg")
    ):
        imagecode = imagelookup("system")
        engine = imagelookup("engine4")
        filepath = filepath4(prodname,imagecode,engine,workname)
        filemove (filepath, filename)


        elif (
        name.startswith("IDS-sig-") and name.endswith(".zip") or 
        name.startswith("IDS-sig-") and name.endswith(".readme.txt")
        ):
            prodname = product ("ipsids")
            imagecode = imagelookup ("signatures")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("IPS-4240-K9-") and name.endswith("-E4.pkg") or
        name.startswith("IPS-4255-K9-") and name.endswith("-E4.pkg") or
        name.startswith("IPS-4260-K9-") and name.endswith("-E4.pkg") or
        name.startswith("IPS-SSM_10-K9-") and name.endswith("-E4.pkg") or
        name.startswith("IPS-SSM_20-K9-") and name.endswith("-E4.pkg") or
        name.startswith("IPS-SSM_40-K9-") and name.endswith("-E4.pkg")
        ):
            prodname = product ("ipsids")
            imagecode = imagelookup ("engine")
            utilssinglemove (name,prodname,imagecode)
'''

def sec_fp_mgmt (filename):
    logging.debug("Sub:    sec_fp_mgmt")
    prodname = product("firepower")
    imagecode = imagelookup("fmc")
    splitbydash = filename.split("-")
    if (
    filename.startswith("Sourcefire_Defense_Center_S3") or 
    filename.startswith("Sourcefire_Defense_Center_Virtual64_VMware") or 
    filename.startswith("Cisco_Firepower_Management_Center_Virtual_VMware") or 
    filename.startswith("Cisco_Firepower_Management_Center_Virtual") or 
    filename.startswith("Cisco_Firepower_Management_Center_VMware")
    ):
        version = splitbydash[1]
        filepath = filepath3(prodname,imagecode,version)
        filemove (filepath, filename)

def sec_asa_fp_sys (filename):
    logging.debug("Sub:    sec_asa_fp_sys")
    prodname =  product("firepower")
    imagecode = imagelookup("fpasasystem")
    splitbydash = filename.split("-")
#    splitbydot = splitbydash[2].split(".")
    if filename.startswith("asasfr-5500x-boot"):
        imagecode2 = imagelookup("boot")
        filepath = filepath4(prodname,imagecode,splitbydash[3],imagecode2)
        filemove (filepath, filename)
    elif filename.startswith("asasfr-boot"):
        imagecode2 = imagelookup("boot")
        filepath = filepath4(prodname,imagecode,splitbydash[2],imagecode2)
        filemove (filepath, filename)
    elif filename.startswith("asasfr-sys"):
        imagecode2 = imagelookup("system")
        filepath = filepath4(prodname,imagecode,splitbydash[2],imagecode2)
        filemove (filepath, filename)
    
def sec_utd_engine (filename):
    logging.debug("Sub:    sec_utd_engine")
    prodname =  product("ciscoutd")
    imagecode = imagelookup("engine")
    filepath = filepath2(prodname,imagecode)
    filemove (filepath, filename)

def sec_utd_signature (filename):
    logging.debug("Sub:    sec_utd_signature")
    splitbydash = filename.split("-")
    prodname =  product("ciscoutd")
    imagecode = imagelookup("signatures")
    filepath = filepath4(prodname,imagecode,splitbydash[3],splitbydash[4])
    filemove (filepath, filename)

def sec_ironportv (filename):
    logging.debug("Sub:    sec_ironportv")
    splitbydash = filename.split("-")
    if filename.startswith ("coeus"):
        prodname = product("ironport")
        imagecode = imagelookup("websecurity")
    elif filename.startswith ("phoebe"):
        prodname = product("ironport")
        imagecode = imagelookup("emailsecurity")
    elif filename.startswith ("zeus"):
        prodname = product("ironport")
        imagecode = imagelookup("mgmtctr")
    verfour = util4digit(splitbydash[1],splitbydash[2],splitbydash[3],splitbydash[4])
    filepath = filepath3 (prodname,imagecode,verfour)
    filemove (filepath, filename)

def sec_fp_asa_mode (filename):
    logging.debug("Sub:    sec_fp_asa_mode")
    prodname = product("firepower")
    imagecode = imagelookup("fpasamode")
    if filename == "Cisco_Network_Sensor_Patch-6.0.1-29.sh":
        filepath = filepath4 (prodname,imagecode,"6.0.1","6.0.1.0")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_A-6.2.0.1-10.sh":
        filepath = filepath4 (prodname,imagecode,"6.2.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_AF-6.1.0.2-1.sh":
        filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_DK-5.4.0.10-1.sh":
        filepath = filepath4 (prodname,imagecode,"5.4.0","5.4.0.9")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_O-6.0.0.999-1.sh":
        filepath = filepath4 (prodname,imagecode,"6.0.0","6.0.0.1")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_H-6.2.3.999-5.sh.REL.tar":
        filepath = filepath4 (prodname,imagecode,"6.2.3","6.2.3.3")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_BN-6.2.2.999-5.sh.REL.tar":
        filepath = filepath4 (prodname,imagecode,"6.2.2","6.2.2.4")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_Hotfix_BW-6.2.0.999-6.sh":
        filepath = filepath4 (prodname,imagecode,"6.2.0","6.2.0.5")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.0.999-1.sh":
        filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.0.999-2.sh":
        filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.0.0_Pre-install-5.4.1.999-1.sh":
        filepath = filepath4 (prodname,imagecode,"6.0.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-29.sh":
        filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-30.sh":
        filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
        filemove (filepath, filename)
    elif filename == "Cisco_Network_Sensor_6.1.0_Pre-install-6.0.1.999-32.sh":
        filepath = filepath4 (prodname,imagecode,"6.1.0","INSTALL")
        filemove (filepath, filename)
    elif filename.startswith("Cisco_Network_Sensor_Upgrade"):
        splitbydash = filename.split("-")
        filepath = filepath4 (prodname,imagecode,splitbydash[1],"INSTALL")
        filemove (filepath, filename)
    else:
        splitbydash = filename.split("-")
        splitbydot = splitbydash[1].split(".")
        verthree = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4 (prodname,imagecode,verthree,verfour)
        filemove (filepath, filename)

def sec_fp_asa_module (filename):
    prodname = product("firepower")
    imagecode = imagelookup("fpasamodule")
    splitbydot = filename.split(".")
    if splitbydot[4] == "SPA":
        verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4 (prodname,imagecode,verthree,verthree)
        filemove (filepath, filename)
    else:
        verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        verfour = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
        filepath = filepath4 (prodname,imagecode,verthree,verfour)
        filemove (filepath, filename)

def sec_fp_ftd_module (filename):
    prodname = product("firepower")
    imagecode = imagelookup("fpftdmodule")
    splitbydot = filename.split(".")
    if splitbydot[4] == "SPA":
        verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4 (prodname,imagecode,verthree,verthree)
        filemove (filepath, filename)
    else:
        verthree = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        verfour = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
        filepath = filepath4 (prodname,imagecode,verthree,verfour)
        filemove (filepath, filename)

def sec_csm (filename):
    logging.debug("Sub:    sec_csm")
    prodname = product ("csm")
    if filename.startswith("csm-maxmind-geolitecity"):
        imagecode = imagelookup("csmgeoip")
        sec_csm_geoip (filename,prodname,imagecode)
    elif filename.startswith("CSM"):
        workname = filename.replace("CSM","")
        workname = workname.replace(".exe","")
        if workname.endswith("Service_Pack1"):
            workname = workname.replace("Service_Pack1","")
            imagecode = imagelookup("sp1")
        elif workname.endswith("Service_Pack2"):
            workname = workname.replace("Service_Pack2","")
            imagecode = imagelookup("sp2")
        elif workname.endswith("Service_Pack3"):
            workname = workname.replace("Service_Pack3","")
            imagecode = imagelookup("sp3")
        elif workname.endswith("Service_Pack4"):
            workname = workname.replace("Service_Pack4","")
            imagecode = imagelookup("sp4")
        filepath = filepath3 (prodname,workname,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-410-win-k9.zip":
        file_size = os.path.getsize(filename)
        if file_size == 2204951112:
            version = "4.10.0"
            imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-41-win-k9.zip":
        version = "4.1.0"
        imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-420-win-k9.zip":
        file_size = os.path.getsize(filename)
        if file_size == 1393471048:
            version = "4.2.0"
            imagecode = imagelookup("install")
        elif file_size == 2447689726:
            version = "4.20.0"
            imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-421-win-k9.zip":
        version = "4.21.0"
        imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-422-win-k9.zip":
        version = "4.22.0"
        imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-40-win-k9.zip":
        version = "4.0.0"
        imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-40-sp1-win-k9.exe":
        version = "4.0.0"
        imagecode = imagelookup("sp1")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-mcp-40-win-k9.exe":
        version = "4.0.0"
        imagecode = imagelookup("mcp")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-401-win-k9.zip":
        version = "4.0.1"
        imagecode = imagelookup("install")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-cms-401-sp2-win-k9.exe":
        version = "4.0.1"
        imagecode = imagelookup("sp2")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-mcp-401-win-k9.exe":
        version = "4.0.1"
        imagecode = imagelookup("mcp")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-410-mcp-410-win-k9.exe":
        version = "4.1.0"
        imagecode = imagelookup("mcp")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-410-rme-430-win-k9.exe":
        version = "4.1.0"
        imagecode = imagelookup("rme")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-42-sp1-win-k9.exe":
        version = "4.2.0"
        imagecode = imagelookup("sp1")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-420-mcp-420-win-k9.exe":
        version = "4.2.0"
        imagecode = imagelookup("mcp")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-csm-420-rme-430-win-k9.exe":
        version = "4.2.0"
        imagecode = imagelookup("rme")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-rme-430-win-k9.exe":
        version = "4.3.0"
        imagecode = imagelookup("rme")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-CSM-440-sp1-win-k9.exe":
        version = "4.4.0"
        imagecode = imagelookup("sp1")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename == "fcs-CSM-440-sp1-win-k9.exe":
        version = "4.4.0"
        imagecode = imagelookup("sp1")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("fcs-csm-41") and filename.endswith("-win-k9.zip"):
        workname = filename.replace("fcs-csm-","")
        workname = workname.replace("-win-k9.zip","")
        imagecode = imagelookup("install")
        myver = list(workname)
        mv = myver[1] + myver[2]
        version = util3digit(myver[0],mv,"0")
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("fcs-csm-") and filename.endswith("-sp1-win-k9.exe"):
        workname = filename.replace("fcs-csm-","")
        workname = workname.replace("-sp1-win-k9.exe","")
        imagecode = imagelookup("sp1")
        myver = list(workname)
        version = util3digit(myver[0],myver[1],myver[2])
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("fcs-csm-") and filename.endswith("-sp2-win-k9.exe"):
        workname = filename.replace("fcs-csm-","")
        workname = workname.replace("-sp2-win-k9.exe","")
        imagecode = imagelookup("sp2")
        myver = list(workname)
        version = util3digit(myver[0],myver[1],myver[2])
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
    elif filename.startswith("fcs-csm-") and filename.endswith("-win-k9.zip"):
        workname = filename.replace("fcs-csm-","")
        workname = workname.replace("-win-k9.zip","")
        imagecode = imagelookup("install")
        myver = list(workname)
        version = util3digit(myver[0],myver[1],myver[2])
        filepath = filepath3 (prodname,version,imagecode)
        filemove (filepath, filename)
#    else:
#        file_size = os.path.getsize(filename)

def sec_csm_geoip (filename,prodname,imagecode):
    logging.debug("Sub:    sec_csm_geoip")
    workname = filename.replace("csm-maxmind-geolitecity-","")
    workname = workname.replace(".zip","")
    mylist = list(workname)
    myyear = mylist[0] + mylist[1] + mylist[2] + mylist[3]
    mymonth = mylist[4] + mylist[5]
    myday = mylist[6] + mylist[7]
    releasedate = myyear + "-" + mymonth + "-" + myday
    filepath = filepath3 (prodname,imagecode,releasedate)
    filemove (filepath, filename)

def sec_pix (filename,prodname):
    logging.debug("Sub:    sec_pix")

    if filename.startswith("np") and filename.endswith(".bin"):
        imagecode = imagelookup("pixpasswordrecovery")
        utilssinglemove (filename,prodname,imagecode)
    elif filename.startswith("pdm") and filename.endswith(".bin"):
        imagecode = imagelookup("pdm")
        utilssinglemove (filename,prodname,imagecode)
    elif filename == "PIXtoASA_1_0.zip":
        imagecode = imagelookup("PIXtoASA")
        utilssinglemove (filename,prodname,imagecode)
    elif filename == "PIX_to_ASA_1_0.dmg":
        imagecode = imagelookup("PIXtoASA")
        utilssinglemove (filename,prodname,imagecode)
    elif filename == "PIXtoASAsetup_1_0.exe":
        imagecode = imagelookup("PIXtoASA")
        utilssinglemove (filename,prodname,imagecode)
    elif filename == "rawrite.exe":
        imagecode = imagelookup("imgwrt")
        utilssinglemove (filename,prodname,imagecode)
    elif (
    filename == "occ-121.zip" or 
    filename == "occ-121.gz" or 
    filename == "README-occ-121.rtf"
    ):
        imagecode = imagelookup("occtoacl")
        utilssinglemove (filename,prodname,imagecode)
    elif (
    filename.startswith("pix") and filename.endswith(".bin") or 
    filename.startswith("PIX") and filename.endswith(".bin")
    ):
        workname = filename.replace("PIX", "")
        workname = workname.replace("pix", "")
        workname = workname.replace(".bin", "")
        splitbydash = workname.split("-")
        #e.g. pix635.bin
        if len(splitbydash) == 1:
            mylist = list(splitbydash[0])
#            if len(mylist) == 4:
#                myver2 = util2digit(mylist[0],mylist[1])
#                myverf = util4digit(mylist[0],mylist[1],mylist[2],mylist[3])
            if len(mylist) == 3:
                myver2 = util2digit(mylist[0],mylist[1])
                myverf = util3digit(mylist[0],mylist[1],mylist[2])
                filepath = filepath3 (prodname,myver2,myverf)
                filemove (filepath, filename)
        else:
            verlist = list(splitbydash[0])

def sec_asa_firmware (filename):
    logging.debug("Sub:    sec_asa_firmware")

    if (
    filename.startswith("asa9") or 
    filename.startswith("asav9") or 
    filename.startswith("asac9") or 
    filename.startswith("asac-9") or 
    filename.startswith("asa871")
    ):
        prodname = product ("asa")
        sec_asa_firmware_v9 (filename,prodname)

    elif (
    filename.startswith("asa7") or 
    filename.startswith("asa8")
    ):
        prodname = product ("asa")
        sec_asa_firmware_v7_8 (filename,prodname)

    elif (
    filename.startswith("asa-restapi")
    ):
        prodname = product ("asa")
        sec_asa_rest_api (filename,prodname)
    else:
        messageunknownfile()

def sec_asa_rest_api (filename,prodname):
    logging.debug("Sub:    sec_asa_rest_api")
    splitbydash = filename.split("-")
    imagecode = imagelookup("restapi")
    mylist = list(splitbydash[2])
    if len(mylist) == 3:
        myver = util3digit(mylist[0],mylist[1],mylist[2])
    elif len(mylist) == 4:
        myver = util4digit(mylist[0],mylist[1],mylist[2],mylist[3])
    elif len(mylist) == 6:
        v3 = mylist[3] + mylist[4] + mylist[5]
        myver = util4digit(mylist[0],mylist[1],mylist[2],v3)
    filepath = filepath3 (prodname,imagecode,myver)
    filemove (filepath, filename)

def sec_asa_firmware_v9 (filename,prodname):
    logging.debug("Sub:    sec_asa_firmware_v9")
    splitbydash = filename.split("-")

    if (
    filename == "asa9101-smp-k8.bin" or 
    filename == "asav9101.vhdx" or 
    filename == "asav9101.qcow2" or 
    filename == "asav9101.zip"
    ):
        filepath = filepath3 (prodname,"9.10","9.10.1")
        filemove (filepath, filename)

    elif (
        filename.startswith("asac")
    ):
        workname = filename.replace("asac-", "")
        workname = workname.replace("asac", "")
        workname = workname.replace("-app-SPA.tar", "")
        workname = workname.replace(".tar", "")
        workname = workname.replace("-", ".") #converting all dashes to dots to simplify logic
        splitbydot = filename.split(".")
        vertwo = util2digit(splitbydot[0],splitbydot[1])
        filepath = filepath3 (prodname,vertwo,workname)
        filemove (filepath, filename)

    elif len(splitbydash) == 1:
        workname = filename.replace("asav", "")
        workname = workname.replace("asac", "")
        workname = workname.replace("asa", "")
        splitbydot = workname.split(".")
        verlist = list(splitbydot[0])
        vertwo = util2digit(verlist[0],verlist[1])
        verthree = util3digit(verlist[0],verlist[1],verlist[2])
        filepath = filepath3 (prodname,vertwo,verthree)
        filemove (filepath, filename)

    elif (
    len(splitbydash) == 2
    ):
        if (
        filename.endswith(".ova") or
        filename.endswith(".qcow2") or
        filename.endswith(".vmdk") or
        filename.endswith(".vhdx") or
        filename.endswith(".zip") or
        filename.endswith(".vhd.bz2")
        ):
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            workname = workname.replace(".qcow2", "")
            workname = workname.replace(".vhd.bz2", "")
            workname = workname.replace(".ova", "")
            workname = workname.replace(".vmdk", "")
            workname = workname.replace(".vhdx", "")
            workname = workname.replace(".zip", "")
            workname = workname.replace(".tar", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verfour = util4digit(verlist[0],verlist[1],verlist[2],mysplitdashworkname[1])
            filepath = filepath3 (prodname,vertwo,verfour)
            filemove (filepath, filename)
        else:
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verthree = util3digit(verlist[0],verlist[1],verlist[2])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)

    elif (
    len(splitbydash) == 3
    ):
        if (
        filename == "asa9101-lfbff-k8.SPA"
        ):
            imagecode = imagelookup("lfbff")
            filepath = filepath4 (prodname,imagecode,"9.10","9.10.1")
            filemove (filepath, filename)

        elif (
        splitbydash[1] == "smp" and
        splitbydash[2] == "k8.bin"
        ):
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verthree = util3digit(verlist[0],verlist[1],verlist[2])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)

        elif (
        splitbydash[2] == "k8.bin"
        ):
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
            filepath = filepath3 (prodname,vertwo,verfour)
            filemove (filepath, filename)

        elif (
        splitbydash[1] == "lfbff" or
        splitbydash[2] == "k8.SPA"
        ):
            imagecode = imagelookup("lfbff")
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verthree = util3digit(verlist[0],verlist[1],verlist[2])
            filepath = filepath4 (prodname,imagecode,vertwo,verthree)
            filemove (filepath, filename)
        elif (
        splitbydash[0] == "asav9" or
        splitbydash[0] == "asac9" or
        splitbydash[0] == "asa9"
        ):
            workname = filename.replace(".qcow2", "")
            workname = workname.replace(".vhdx", "")
            workname = workname.replace(".zip", "")
            workname = workname.replace(".tar", "")
            workname = workname.replace(".vhd.bz2", "")
            workname = workname.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            workname = workname.replace("-smp-k8.bin", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)

    elif (
    len(splitbydash) == 4
    ):
        if (
        splitbydash[2] == "smp" and
        splitbydash[3] == "k8.bin"
        ):
            workname = filename.replace(".qcow2", "")
            workname = workname.replace(".vhdx", "")
            workname = workname.replace(".zip", "")
            workname = workname.replace(".tar", "")
            workname = workname.replace(".vhd.bz2", "")
            workname = workname.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            workname = workname.replace("-smp-k8.bin", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
            filepath = filepath3 (prodname,vertwo,verfour)
            filemove (filepath, filename)
        elif (
        splitbydash[2] == "lfbff" and
        splitbydash[3] == "k8.SPA"
        ):
            imagecode = imagelookup("lfbff")
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(verlist[0],verlist[1])
            verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
            filepath = filepath4 (prodname,imagecode,vertwo,verfour)
            filemove (filepath, filename)
        elif (
        splitbydash[0] == "asav9" or
        splitbydash[0] == "asac9" or
        splitbydash[0] == "asac-" or
        splitbydash[0] == "asa9"
        ):
            workname = filename.replace(".qcow2", "")
            workname = workname.replace(".vhdx", "")
            workname = workname.replace(".zip", "")
            workname = workname.replace(".tar", "")
            workname = workname.replace(".vhd.bz2", "")
            workname = workname.replace("asav", "")
            workname = workname.replace("asac-", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            workname = workname.replace("-smp-k8.bin", "")
            mysplitdashworkname = workname.split("-")
            verlist = list(mysplitdashworkname[0])
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verthree = util4digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2],mysplitdashworkname[3])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)

    elif (
    len(splitbydash) == 5
    ):
        if (
        splitbydash[3] == "smp" and
        splitbydash[4] == "k8.bin"
        ):
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)
        elif (
        splitbydash[3] == "lfbff" and
        splitbydash[4] == "k8.SPA"
        ):
            imagecode = imagelookup("lfbff")
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verthree = util3digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2])
            filepath = filepath4 (prodname,imagecode,vertwo,verthree)
            filemove (filepath, filename)

    elif (
    len(splitbydash) == 6
    ):
        if (
        splitbydash[4] == "smp" and
        splitbydash[5] == "k8.bin"
        ):
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verthree = util4digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2],mysplitdashworkname[3])
            filepath = filepath3 (prodname,vertwo,verthree)
            filemove (filepath, filename)
        elif (
        splitbydash[4] == "lfbff" and
        splitbydash[5] == "k8.SPA"
        ):
            imagecode = imagelookup("lfbff")
            workname = filename.replace("asav", "")
            workname = workname.replace("asac", "")
            workname = workname.replace("asa", "")
            mysplitdashworkname = workname.split("-")
            vertwo = util2digit(mysplitdashworkname[0],mysplitdashworkname[1])
            verfour = util4digit(mysplitdashworkname[0],mysplitdashworkname[1],mysplitdashworkname[2],mysplitdashworkname[3])
            filepath = filepath4 (prodname,imagecode,vertwo,verfour)
            filemove (filepath, filename)
            
    
    else:
        messageunknownfile()

def sec_asa_firmware_v7_8 (filename,prodname):
    logging.debug("Sub:    sec_asa_firmware_v7_8")
    workname = filename.replace("asa", "")
    splitbydash = workname.split("-")

    if (
    len(splitbydash) == 2 or 
    len(splitbydash) == 3 and 
    filename.endswith("-smp-k8.bin")
    ):
        verlist = list(splitbydash[0])
        vertwo = util2digit(verlist[0],verlist[1])
        verthree = util3digit(verlist[0],verlist[1],verlist[2])
        filepath = filepath3 (prodname,vertwo,verthree)
        filemove (filepath, filename)

    elif (
    filename.startswith("asa871") and
    filename.endswith(".ova")
    ):
        verlist = list(splitbydash[0])
        splitbydash[1] = splitbydash[1].replace(".ova", "")
        verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
        filepath = filepath3 (prodname,vertwo,verfour)
        filemove (filepath, filename)
    else:
        verlist = list(splitbydash[0])
        vertwo = util2digit(verlist[0],verlist[1])
        verfour = util4digit(verlist[0],verlist[1],verlist[2],splitbydash[1])
        filepath = filepath3 (prodname,vertwo,verfour)
        filemove (filepath, filename)


def sec_acs(filename):
    logging.debug("Sub:    sec_acs")
    prodname = product("acs")

    # Prefix-based rules
    if filename.startswith("Clean-"):
        _handle_vfour_patch(filename, prodname, "clean")
        return

    if filename.startswith("5-"):
        _handle_patch(filename, prodname, "patch")
        return

    # Special-case exact filenames (different filepath functions)
    special_cases = {
        "ACS57BasePatch.tar.gz": ("patch", filepath4, ("5.7.0.15", "0")),
        "ACS_5.0.0.21_ADE_OS_1.2_upgrade.tar.gpg": ("upgrade", filepath3, ("5.0.0.21",)),
        "ReadMe_for_ACS_5.6_Upgrade_Package-txt": ("upgrade", filepath3, ("5.6.0.22",)),
        "applAcs_4.1.1.23_ACS-4.1-CSTacacs-CSCsg97429.zip": ("patch", filepath4, ("4.1.1.23", "CSTacacs-CSCsg97429")),
        "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429.zip": ("patch", filepath4, ("4.1.1.23", "CSTacacs-CSCsg97429")),
        "ACS-4.1.1.23-CSTacacs-SW-CSCsg97429-Readme.txt": ("patch", filepath4, ("4.1.1.23", "CSTacacs-CSCsg97429")),
    }
    if filename in special_cases:
        image_type, func, args = special_cases[filename]
        imagecode = imagelookup(image_type)
        filepath = func(prodname, *args, imagecode) if func is filepath4 else func(prodname, *args, imagecode)
        filemove(filepath, filename)
        return

    # Version 5 installers/upgrades (large table)
    if filename in V5_FILE_MAP:
        sec_acs_vfiveinstall(filename, prodname)
        return

    # Version 4.x family
    if filename.startswith(("ACS-4", "Acs-4", "Acs_4", "applAcs_4")):
        sec_acs_vfour(filename, prodname)
        return

    messageunknownfile()


# -------------------------------
# v5.x installer/upgrader handler
# -------------------------------

V5_FILE_MAP = {
    # USB Installers
    "ACS_55_USB_Installation_tool.zip":  ("install", "5.5.0.46"),
    "ACS_56_USB_Installation_tool.zip":  ("install", "5.6.0.22"),
    "ACS_57_USB_Installation_tool.zip":  ("install", "5.7.0.15"),
    "ACS_58_USB_Installation_tool.zip":  ("install", "5.8.0.32"),
    "ACS_581_USB_Installation_tool.zip": ("install", "5.8.1.4"),

    # Tar Upgrades
    "ACS_5.1.0.44.tar.gz":    ("upgrade", "5.1.0.44"),
    "ACS_5.2.0.26.tar.gz":    ("upgrade", "5.2.0.26"),
    "ACS_5.3.0.40.tar.gz":    ("upgrade", "5.3.0.40"),
    "ACS_5.4.0.46.0a.tar.gz": ("upgrade", "5.4.0.46"),
    "ACS_5.5.0.46.tar.gz":    ("upgrade", "5.5.0.46"),
    "ACS_5.6.0.22.tar.gz":    ("upgrade", "5.6.0.22"),
    "ACS_5.7.0.15.tar.gz":    ("upgrade", "5.7.0.15"),
    "ACS_5.8.0.32.tar.gz":    ("upgrade", "5.8.0.32"),
    "ACS_5.8.1.4.tar.gz":     ("upgrade", "5.8.1.4"),

    # ISOs
    "ACS-5.0.0.21.iso":     ("install", "5.0.0.21"),
    "ACS_v5.1.0.44.iso":    ("install", "5.1.0.44"),
    "ACS_v5.2.0.26.iso":    ("install", "5.2.0.26"),
    "ACS_v5.3.0.40.iso":    ("install", "5.3.0.40"),
    "ACS_v5.4.0.46.0a.iso": ("install", "5.4.0.46"),
    "ACS_v5.5.0.46.iso":    ("install", "5.5.0.46"),
    "ACS_v5.6.0.22.iso":    ("install", "5.6.0.22"),
    "ACS_v5.7.0.15.iso":    ("install", "5.7.0.15"),
    "ACS_v5.8.0.32.iso":    ("install", "5.8.0.32"),
    "ACS_v5.8.1.4.iso":     ("install", "5.8.1.4"),
}

def sec_acs_vfiveinstall(filename, prodname):
    logging.debug("Sub:    sec_acs_vfiveinstall")

    if filename not in V5_FILE_MAP:
        messageunknownfile()
        return

    image_type, version = V5_FILE_MAP[filename]
    imagecode = imagelookup(image_type)
    filepath = filepath3(prodname, version, imagecode)
    filemove(filepath, filename)


# -------------------------------
# v4.x handlers
# -------------------------------

def sec_acs_vfour(filename, prodname):
    logging.debug("Sub:    sec_acs_vfour")

    if filename.endswith("-DOCs.zip"):
        _handle_vfour_software(filename, prodname, "docs")
    elif filename.endswith("-BIN-K9.zip"):
        _handle_vfour_software(filename, prodname, "install")
    elif (
        filename.endswith(("-SW.zip", "-RA.zip", "-SW.exe", "-SW-Readme.txt", ".txt", "-Clean.zip"))
        or (filename.startswith("applAcs_") and filename.endswith(".zip"))
    ):
        _handle_vfour_patch(filename, prodname, "patch")


def _handle_vfour_software(filename, prodname, image_type):
    logging.debug("Sub:    sec_acs_vfour_software")
    imagecode = imagelookup(image_type)
    workname = filename.replace("-BIN-K9.zip", "").replace("-DOCs.zip", "").replace("ACS-", "")
    verfour = _extract_ver_from_name(workname)
    filepath = filepath3(prodname, verfour, imagecode)
    filemove(filepath, filename)


def _handle_vfour_patch(filename, prodname, image_type):
    logging.debug("Sub:    sec_acs_vfour_patch")
    imagecode = imagelookup(image_type)
    cleanups = [
        "-SW.zip", "-SW.exe", "-RA.zip", "-K9.zip", "-Clean.zip",
        "-SW-Readme.txt", "Acs-", "ACS-", "Acs_", "ACS_", "Clean-"
    ]
    workname = filename
    for c in cleanups:
        workname = workname.replace(c, "")
    verfour = _extract_ver_from_name(workname)
    splitbydot = workname.split(".")
    filepath = filepath4(prodname, verfour, imagecode, splitbydot[4])
    filemove(filepath, filename)


# -------------------------------
# patch handler
# -------------------------------

def _handle_patch(filename, prodname, image_type):
    logging.debug("Sub:    sec_acs_patch")
    imagecode = imagelookup(image_type)
    workname = filename.replace(".tar.gpg", "")
    splitbydash = workname.split("-")
    verfour = util4digit(splitbydash[0], splitbydash[1], splitbydash[2], splitbydash[3])
    filepath = filepath4(prodname, verfour, imagecode, splitbydash[4])
    filemove(filepath, filename)


# -------------------------------
# helpers
# -------------------------------

def _extract_ver_from_name(workname: str) -> str:
    """Turn ACS-style name fragments into 4-digit version string."""
    splitbydot = workname.split(".")
    return util4digit(splitbydot[0], splitbydot[1], splitbydot[2], splitbydot[3])


def sec_ise(filename):
    logging.debug("Sub: sec_ise")
    prodname = product("ise")

    # Lookup tables for specific static filenames -> (image_type, version)
    file_map = {
        # struts
        "CSCvn17524_20_P7_HotPatch_ReadMe": ("struts", "2.0"),
        "ise-apply-CSCvn17524_2.0.0.306_common_1-SPA.tar.gz": ("struts", "2.0"),
        "ise-rollback-CSCvn17524_2.0.0.306_common_1-SPA.tar.gz": ("struts", "2.0"),

        "CSCvn17524_201_P7_HotPatch_ReadMe": ("struts", "2.0.1"),
        "ise-apply-CSCvn17524_2.0.1.130_common_1-SPA.tar.gz": ("struts", "2.0.1"),
        "ise-rollback-CSCvn17524_2.0.1.130_common_1-SPA.tar.gz": ("struts", "2.0.1"),

        "CSCvn17524_21_P7_HotPatch_ReadMe": ("struts", "2.1"),
        "ise-apply-CSCvn17524_2.1.0.474_common_1-SPA.tar.gz": ("struts", "2.1"),
        "ise-rollback-CSCvn17524_2.1.0.474_common_1-SPA.tar.gz": ("struts", "2.1"),

        "CSCvn17524_23_P5_HotPatch_ReadMe": ("struts", "2.3"),
        "ise-apply-CSCvn17524_2.3.0.298_common_1-SPA.tar.gz": ("struts", "2.3"),
        "ise-rollback-CSCvn17524_2.3.0.298_common_1-SPA.tar.gz": ("struts", "2.3"),

        "README_ISE_20_201_21_22": ("struts", None),
        "ise-applystrutsfix-signed.x86_64.tar.gz": ("struts", None),
        "ise-rollbackstrutsfix-signed.x86_64.tar.gz": ("struts", None),

        # log4j
        "ise-apply-CSCwa47133_Ver_24_30_allpatches-SPA.tar.gz": ("log4j", "2.4-3.0"),
        "ise-rollback-CSCwa47133_Ver_24_30_allpatches-SPA.tar.gz": ("log4j", "2.4-3.0"),

        "ise-rollback-CSCwa47133_3.1.0.518_patch0-SPA.tar.gz": ("log4j", "3.1"),
        "ise-rollback-CSCwa47133_3.1.0.518_patch1-SPA.tar.gz": ("log4j", "3.1"),
        "ise-apply-CSCwa47133_3.1.0.518_patch0-SPA.tar.gz": ("log4j", "3.1"),
        "ise-apply-CSCwa47133_3.1.0.518_patch1-SPA.tar.gz": ("log4j", "3.1"),

        # upgrade (special formatting order is reversed)
        "ise-upgradebundle-1.2.x-to-1.4.0.253.x86_64.tar.gz": ("upgrade", "1.4"),
        "ise-upgradebundle-1.4.0.253.x86_64.tar.gz": ("upgrade", "1.4"),
        "ise-upgradebundle-1.3.x-and-1.4.x-to-2.0.0.306.x86_64.tar.gz": ("upgrade", "2.0"),
        "ise-upgradebundle-2.4.x-2.7.x-to-3.0.0.458.SPA.x86_64.tar.gz": ("upgrade", "3.0"),
        "ise-upgradebundle-2.6.x-3.0.x-to-3.1.0.518.SPA.x86_64.tar.gz": ("upgrade", "3.1"),
        "ise-upgradebundle-2.7.x-3.1.x-to-3.2.0.542.SPA.x86_64.tar.gz": ("upgrade", "3.2"),
        "ise-upgradebundle-2.7.x-3.1.x-to-3.2.0.542a.SPA.x86_64.tar.gz": ("upgrade", "3.2"),
        "ise-upgradebundle-2.7.x-3.1.x-to-3.2.0.542c.SPA.x86_64.tar.gz": ("upgrade", "3.2"),
        "ise-upgradebundle-3.0.x-3.2.x-to-3.3.0.430.SPA.x86_64.tar.gz": ("upgrade", "3.3"),
        "ise-upgradebundle-3.0.x-3.2.x-to-3.3.0.430b.SPA.x86_64.tar.gz": ("upgrade", "3.3"),
        "ise-upgradebundle-3.1.x-3.3.x-to-3.4.0.608.SPA.x86_64.tar.gz": ("upgrade", "3.4"),
    }

    if filename in file_map:
        image_type, version = file_map[filename]
        imagecode = imagelookup(image_type)
        if version:
            if image_type in ["struts", "log4j"]:
                imagecode = f"{imagecode}/{version}"
            elif image_type == "upgrade":
                imagecode = f"{version}/{imagecode}"
        utilssinglemove(filename, prodname, imagecode)
        return

    # Pattern-based matches
    if filename.startswith("ise-patchbundle-"):
        imagecode = imagelookup("patch")
        sec_ise_patch(filename, prodname, imagecode)

    elif ((filename.startswith("Cisco-vISE") and filename.endswith("ova")) or
          (filename.startswith("Cisco-ISE-") and filename.endswith("iso")) or
          (filename.startswith("ISE-") and filename.endswith("ova")) or
          (filename.startswith("ise-") and filename.endswith("iso"))):
        imagecode = imagelookup("install")
        sec_ise_install(filename, prodname, imagecode)

    elif (filename.startswith("ise-upgradebundle-") or
          filename.startswith("ise-appbundle-")):
        imagecode = imagelookup("upgrade")
        sec_ise_upgrade(filename, prodname, imagecode)

    elif filename.startswith("ise-urtbundle-"):
        imagecode = imagelookup("urtbundle")
        sec_ise_urtbundle(filename, prodname, imagecode)

    elif ((filename.startswith("win_spw-") and (filename.endswith("-isebundle.zip") or filename.endswith("-isebundle-v1.zip"))) or
          (filename.startswith("mac-spw-dmg-") and (filename.endswith("-isebundle.zip") or filename.endswith("-isebundle-v1.zip")))):
        imagecode = imagelookup("supplicantpw")
        sec_ise_spw(filename, prodname, imagecode)

    elif filename.startswith("ACS-MigrationApplication-"):
        imagecode = imagelookup("acs_mig")
        sec_ise_acs_mig(filename, prodname, imagecode)

    else:
        messageunknownfile()

def sec_ise_acs_mig (filename,prodname,imagecode):
    logging.debug("Sub:    sec_ise_acs_mig")
    workname = filename.replace("ACS-MigrationApplication-","")
    splitbydot = workname.split(".")
    vertwo = util2digit(splitbydot[0],splitbydot[1])
    filepath = filepath3 (prodname,vertwo,imagecode)
    filemove (filepath, filename)

def sec_ise_spw(filename, prodname, imagecode):
    logging.debug("Sub: sec_ise_spw")

    # cleanup common prefixes/suffixes
    workname = filename.replace("win_spw-", "")
    workname = workname.replace("mac-spw-dmg-", "")
    workname = workname.replace("-isebundle.zip", "")
    workname = workname.replace("-isebundle-v1.zip", "")
    splitbydot = workname.split(".")
    vertwo = util2digit(splitbydot[0], splitbydot[1])

    # Explicit version overrides for special filenames
    spw_map = {
        # 1.1.1 group
        ("win_spw-1.0.0.23-isebundle.zip",
         "mac-spw-1.0.0.11.zip",
         "win_spw-1.0.0.22-isebundle.zip"): "1.1.1",

        # 1.1.3 group
        ("win_spw-1.0.0.33-isebundle.zip",
         "mac-spw-1.0.0.18.zip",
         "win_spw-1.0.0.28-isebundle.zip"): "1.1.3",

        # 1.2 group
        ("mac-spw-1.0.0.21.zip",
         "mac-spw-dmg-1.0.0.27-isebundle.zip",
         "mac-spw-dmg-1.0.0.29-isebundle.zip",
         "spw-1.2.39.apk",
         "win_spw-1.0.0.34-isebundle.zip",
         "win_spw-1.0.0.35-isebundle.zip",
         "win_spw-1.0.0.41-isebundle.zip"): "1.2",

        # 1.3 group
        ("mac-spw-dmg-1.0.0.30-isebundle.zip",
         "spw-1.2.40.apk",
         "win_spw-1.0.0.43-isebundle.zip"): "1.3",

        # 2.0 group
        ("mac-spw-dmg-1.0.0.36-isebundle.zip",
         "mac-spw-dmg-2.0.2.37-isebundle.zip",
         "win_spw-2.0.1.46-isebundle.zip",
         "spw-1.2.46.apk"): "2.0",

        # 2.1 group
        ("mac-spw-dmg-2.1.0.42-isebundle.zip",
         "mac-spw-dmg-2.1.0.40-isebundle.zip",
         "win_spw-2.1.0.51-isebundle.zip"): "2.1",

        ("win_spw-2.2.0.52-isebundle.zip",): "2.2",
        ("win_spw-2.2.1.53-isebundle.zip",
         "mac-spw-dmg-2.2.1.43-isebundle.zip"): "2.3",
        ("win_spw-2.4.0.1-isebundle.zip",): "2.4",
        ("mac-spw-dmg-2.6.0.2-isebundle.zip",
         "mac-spw-dmg-2.6.0.1-isebundle.zip",
         "mac-spw-dmg-2.5.0.7-isebundle.zip"): "2.6",
        ("mac-spw-dmg-3.1.0.2-isebundle.zip",
         "mac-spw-dmg-3.1.0.1-isebundle.zip",
         "win_spw-3.0.0.2-isebundle.zip",
         "win_spw-2.7.0.1-isebundle.zip",
         "mac-spw-dmg-2.7.0.1-isebundle.zip"): "2.7",
        ("mac-spw-dmg-2.7.0.1-isebundle-v1.zip",
         "win_spw-3.0.0.2-isebundle-v1.zip"): "3.0",
        ("mac-spw-dmg-3.2.0.1-isebundle.zip",): "3.1",
        ("mac-spw-dmg-3.4.0.0-isebundle.zip",
         "win_spw-3.0.0.2-isebundle-v1.zip"): "3.3",
    }

    for files, version in spw_map.items():
        if filename in files:
            vertwo = version
            break

    filepath = filepath3(prodname, vertwo, imagecode)
    filemove(filepath, filename)



def sec_ise_upgrade(filename, prodname, imagecode):
    logging.debug("Sub: sec_ise_upgrade")

    upgrade_map = {
        "ise-appbundle-1.1.1.268.i386.tar.gz": "1.1.1",
        "ise-appbundle-1.1.2.145.i386.tar.gz": "1.1.2",
        "ise-appbundle-1.1.3.124.i386.tar.gz": "1.1.3",
        "ise-appbundle-1.1.4.218.i386.tar.gz": "1.1.4",

        "ise-upgradebundle-1.1.x-to-1.2.0.899.i386.tar.gz": "1.2",
        "ise-upgradebundle-1.2.0.899.x86_64.tar.gz": "1.2",

        "ise-upgradebundle-1.1.x-to-1.2.1.198.i386.tar.gz": "1.2.1",
        "ise-upgradebundle-1.2.1.198.x86_64.tar.gz": "1.2.1",

        "ise-upgradebundle-1.2.x-to-1.3.0.876.repackaged.x86_64.tar.gz": "1.3",

        "ise-upgradebundle-1.2.x-to-1.4.0.253.x86_64.tar.gz": "1.4",
        "ise-upgradebundle-1.4.0.253.x86_64.tar.gz": "1.4",

        "ise-upgradebundle-1.3.x-1.4.x-to-2.1.0.474.1808.x86_64.tar.gz": "2.1",
        "ise-upgradebundle-2.0.x-to-2.1.0.474.SPA.x86_64.tar.gz": "2.1",

        "ise-upgradebundle-1.4.x-to-2.2.0.470.1808.x86_64.tar.gz": "2.2",
        "ise-upgradebundle-2.0.x-to-2.2.0.470.1808.SPA.x86_64.tar.gz": "2.2",
        "ise-upgradebundle-2.0.x-to-2.2.0.470.SPA.x86_64.tar.gz": "2.2",
        "ise-upgradebundle-2.2.0.470.1808.SPA.x86_64.tar.gz": "2.2",
        "ise-upgradebundle-2.2.0.470.SPA.x86_64.tar.gz": "2.2",

        "ise-upgradebundle-2.0.x-to-2.3.0.298.1808.SPA.x86_64.tar.gz": "2.3",
        "ise-upgradebundle-2.3.0.298.SPA.x86_64.tar.gz": "2.3",

        "ise-upgradebundle-2.0.x-2.3.x-to-2.4.0.357.SPA.x86_64.tar.gz": "2.4",
        "ise-upgradebundle-2.1.x-2.4.x-to-2.6.0.156.SPA.x86_64.tar.gz": "2.6",
        "ise-upgradebundle-2.2.x-2.6.x-to-2.7.0.356.SPA.x86_64.tar.gz": "2.7",
        "ise-upgradebundle-2.6.x-3.0.x-to-3.1.0.518b.SPA.x86_64.tar.gz": "3.1",
        "ise-upgradebundle-2.7.x-3.1.x-to-3.2.0.542b.SPA.x86_64.tar.gz": "3.2",
        "ise-upgradebundle-3.0.x-3.2.x-to-3.3.0.430b.SPA.x86_64.tar.gz": "3.3",
        "ise-upgradebundle-3.1.x-3.3.x-to-3.4.0.608a.SPA.x86_64.tar.gz": "3.4",
    }

    vertwo = upgrade_map.get(filename)
    if not vertwo:
        messageunknownfile()
        return

    filepath = filepath3(prodname, vertwo, imagecode)
    filemove(filepath, filename)

def sec_ise_install(filename, prodname, imagecode):
    logging.debug("Sub: sec_ise_install")
    workname = filename
    for prefix in ["Cisco-vISE-2400-", "Cisco-vISE-1800-", "Cisco-vISE-1200-",
                   "Cisco-vISE-600-", "Cisco-vISE-300-", "Cisco-ISE-", "ISE-", "ise-"]:
        workname = workname.replace(prefix, "")
    workname = workname.replace(".ova", "").replace(".iso", "")

    splitbydot = workname.split(".")
    vertwo = util2digit(splitbydot[0], splitbydot[1])
    filepath = filepath3(prodname, vertwo, imagecode)
    filemove(filepath, filename)

def sec_ise_patch (filename,prodname,imagecode):
    logging.debug("Sub:    sec_ise_patch")
    workname = filename.replace("ise-patchbundle-","")
    splitbydot = workname.split(".")
    splitbydash = workname.split("-")
    patchnum = splitbydash[1].replace("Patch","")
    vertwo = util2digit(splitbydot[0],splitbydot[1])
    filepath = filepath4 (prodname,vertwo,imagecode,patchnum)
    filemove (filepath, filename)

def sec_ise_urtbundle(filename, prodname, imagecode):
    logging.debug("Sub: sec_ise_urtbundle")
    splitbydash = filename.split("-")
    splitbydot = splitbydash[2].split(".")
    vertwo = util2digit(splitbydot[0], splitbydot[1])
    filepath = filepath3(prodname, vertwo, imagecode)
    filemove(filepath, filename)

def sec_ise_pic(filename):
    """Process Cisco ISE PIC image filenames and move them to the correct path."""
    logging.debug("Sub: sec_ise_pic")

    prodname = product("isepic")
    workname = filename

    # Strip common prefixes
    # Prefixes (sorted longest → shortest)
    prefixes = [
        "ise-pic-patchbundle-",
        "Cisco-ISE-PIC-",
        "ise-pic-",
        "pic-",
    ]
    for prefix in sorted(prefixes, key=len, reverse=True):
        if workname.startswith(prefix):
            workname = workname[len(prefix):]  # remove only leading prefix
            break  # stop after first match

    # Suffixes (sorted longest → shortest)
    suffixes = [
        ".SPA.x86_64.tar.gz",
        ".SPA.x86_64.iso",
    ]
    for suffix in sorted(suffixes, key=len, reverse=True):
        if workname.endswith(suffix):
            workname = workname.removesuffix(suffix)
            break

    splitbydash = filename.split("-")

    if filename.startswith("ise-pic-patchbundle-"):
        # Example: ise-pic-patchbundle-<something>-<version>-Patch<num>-...
        version = splitbydash[3]
        patchnum = splitbydash[4].replace("Patch", "")
        imagecode = imagelookup("patch")
        filepath = filepath4(prodname, version, imagecode, patchnum)
    else:
        # Workname looks like: <major>.<minor>.<rest>
        splitbydot = workname.split(".")
        version = util2digit(splitbydot[0], splitbydot[1])
        imagecode = imagelookup("install")
        filepath = filepath3(prodname, version, imagecode)

    filemove(filepath, filename)


def sec_sourcefire_fmc_patch(filename):
    logging.debug("Sub: sec_sourcefire_fmc_patch")
    prodname = product("firepower")
    imagecode = imagelookup("fmc")

    # Explicit filename -> (base_version, patch_version) map
    patch_map = {
        "Sourcefire_3D_Defense_Center_S3_Patch-5.4.1-59.sh": ("5.4.1", "5.4.1"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_A-6.2.0.1-10.sh": ("6.2.0", "6.2.0"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_AJ-6.1.0.2-1.sh": ("6.1.0", "6.1.0.1"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_AZ-6.1.0.3-1.sh": ("6.1.0", "6.1.0.2"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_BN-6.2.2.999-5.sh.REL.tar": ("6.2.0", "6.2.2.4"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_BS-6.2.2.5-3.sh.REL.tar": ("6.2.0", "6.2.2.4"),
        "Sourcefire_3D_Defense_Center_S3_Hotfix_K-6.0.0.2-3.sh": ("6.0.0", "6.0.0.1"),
    }

    if filename in patch_map:
        base_version, patch_version = patch_map[filename]
    else:
        # fallback parsing for new / unknown filenames
        workname = filename.replace(".sh.REL.tar", "").replace(".sh", "")
        splitbydash = workname.split("-")
        splitbydot = splitbydash[1].split(".")
        base_version = util3digit(splitbydot[0], splitbydot[1], splitbydot[2])
        patch_version = util4digit(
            splitbydot[0], splitbydot[1], splitbydot[2], splitbydot[3]
        )

    filepath = filepath4(prodname, imagecode, base_version, patch_version)
    filemove(filepath, filename)

def sec_sourcefire_device(filename):
    logging.debug("Sub: sec_sourcefire_device")
    prodname = product("firepower")
    imagecode = imagelookup("sourcefiredev")

    # Explicit filename -> version map
    device_map = {
        "Sourcefire_3D_Device_S3_Patch-6.0.1-29.sh": "6.0.1",
    }

    if filename in device_map:
        version = device_map[filename]
        filepath = filepath3(prodname, imagecode, version)
    else:
        splitbydash = filename.split("-")
        splitbydot = splitbydash[1].split(".")
        vertwo = util2digit(splitbydot[0], splitbydot[1])
        verfour = util4digit(splitbydot[0], splitbydot[1], splitbydot[2], splitbydot[3])
        filepath = filepath4(prodname, imagecode, vertwo, verfour)

    filemove(filepath, filename)

def sec_fp_vdb(filename):
    logging.debug("Sub: sec_fp_vdb")
    prodname = product("firepower")
    
    # Map prefixes to image codes
    prefix_map = {
        "Cisco_VDB_Fingerprint_Database": "csfvdb",
        "Sourcefire_VDB": "sfvdb",
    }

    imagecode = None
    for prefix, code in prefix_map.items():
        if filename.startswith(prefix):
            imagecode = imagelookup(code)
            break
    if imagecode is None:
        messageunknownfile()
        return

    splitbydash = filename.split("-")
    splitbydash[2] = splitbydash[2].replace(".sh.REL.tar", "").replace(".sh", "")
    ver = util2digit(splitbydash[1], splitbydash[2])

    filepath = filepath4(prodname, imagecode, splitbydash[1], ver)
    filemove(filepath, filename)

def sec_fp_rules(filename):
    logging.debug("Sub: sec_fp_rules")
    prodname = product("firepower")
    
    prefix_map = {
        "Cisco_Firepower_SRU": "csfrules",
        "Sourcefire_Rule_Update": "sfrules",
    }

    imagecode = None
    for prefix, code in prefix_map.items():
        if filename.startswith(prefix):
            imagecode = imagelookup(code)
            break
    if imagecode is None:
        messageunknownfile()
        return

    splitbydash = filename.split("-")
    ver = util4digit(splitbydash[1], splitbydash[2], splitbydash[3], splitbydash[4])

    filepath = filepath4(prodname, imagecode, splitbydash[1], ver)
    filemove(filepath, filename)

def sec_fp_lsp(filename):
    logging.debug("Sub: sec_fp_lsp")
    prodname = product("firepower")
    imagecode = imagelookup("lsprel")

    workname = filename.replace(".tar.xz.REL.tar", "").replace("lsp-rel-", "")
    splitbydash = workname.split("-")
    
    year, month, day = workname[0:4], workname[4:6], workname[6:8]
    version = util4digit(year, month, day, splitbydash[1])

    filepath = filepath4(prodname, imagecode, year, version)
    filemove(filepath, filename)

def sec_fp_geodb(filename):
    logging.debug("Sub: sec_fp_geodb")
    prodname = product("firepower")
    
    prefix_map = {
        "Cisco_Firepower_GEODB": "csfgeodb",
        "Sourcefire_Geodb": "sfgeodb",
    }

    imagecode = None
    for prefix, code in prefix_map.items():
        if filename.startswith(prefix):
            imagecode = imagelookup(code)
            break
    if imagecode is None:
        messageunknownfile()
        return

    splitbydash = filename.split("-")
    splitbydash[4] = splitbydash[4].replace(".sh.REL.tar", "").replace(".sh", "")
    ver = util4digit(splitbydash[1], splitbydash[2], splitbydash[3], splitbydash[4])

    filepath = filepath4(prodname, imagecode, splitbydash[1], ver)
    filemove(filepath, filename)

def sec_fxos_firmware (filename,prodname,imagecode):
    logging.debug("Sub:    sec_fxos_firmware")
    splitbydot = filename.split(".")
    version = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
    filepath = filepath3 (prodname,imagecode,version)
    filemove (filepath, filename)

def sec_fxos_firmware_recovery (filename,prodname,imagecode):
    logging.debug("Sub:    sec_fxos_firmware_recovery")
    splitbydot = filename.split(".")
    splitbydot[4] = splitbydot[4].strip("N")
    versiontwo = util2digit(splitbydot[4],splitbydot[5])
    versionfull = util4digit(splitbydot[4],splitbydot[5],splitbydot[6],splitbydot[7])
    filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
    filemove (filepath, filename)

def sec_fxos_firmware_d4_1_4 (filename,prodname,imagecode):
    logging.debug("Sub:    sec_fxos_firmware_d4_1_4")
    splitbydot = filename.split(".")
    versiontwo = util2digit(splitbydot[1],splitbydot[2])
    versionfull = util4digit(splitbydot[1],splitbydot[2],splitbydot[3],splitbydot[4])
    filepath = filepath4 (prodname,imagecode,versiontwo,versionfull)
    filemove (filepath, filename)

def sec_fxos (filename):
    logging.debug("Sub:    sec_fxos")
    prodname = product("firepower")
    splitbydot = filename.split(".")

    if splitbydot[0] == "fxos-k9-fpr4k-firmware":
        imagecode = imagelookup(splitbydot[0])
        sec_fxos_firmware (filename,prodname,imagecode)

    elif splitbydot[0] == "fxos-k9-fpr9k-firmware":
        imagecode = imagelookup(splitbydot[0])
        sec_fxos_firmware (filename,prodname,imagecode)

    elif splitbydot[0] == "fxos-k9-manager" or splitbydot[0] == "fxos-k9":
        imagecode = imagelookup(splitbydot[0])
        sec_fxos_firmware_d4_1_4 (filename,prodname,imagecode)

    elif splitbydot[0] == "fxos-k9-system" or splitbydot[0] == "fxos-k9-kickstart":
        imagecode = imagelookup(splitbydot[0])
        sec_fxos_firmware_recovery (filename,prodname,imagecode)

    elif (
        splitbydot[0] == "fxos-mibs-fp3k" or 
        splitbydot[0] == "fxos-mibs-fp9k-fp4k" or 
        splitbydot[0] == "firepower-mibs"
    ):
        imagecode = imagelookup(splitbydot[0])
        sec_fxos_firmware_d4_1_4 (filename,prodname,imagecode)

def sec_asa_asdm (filename):
    logging.debug("Sub:    sec_asa_asdm")

    if (
    filename.endswith("f.bin") or 
    filename.endswith("f.msi")
    ):
        prodname = product("asa")
        imagecode = imagelookup("asdmf")
    else:
        prodname = product("asa")
        imagecode = imagelookup("asdm")

    workname = filename.replace("asdm-openjre-","")
    workname = workname.replace("asdm-demo-","")
    workname = workname.replace("asdm-","")
    workname = workname.replace("asdm","")
    workname = workname.replace("f.bin","")
    workname = workname.replace(".bin","")
    workname = workname.replace(".msi","")
    splitbydash = workname.split("-")
    if filename == "asdm-61551.bin":
        vertwo = "6.1"
        verfour = "6.1.5.51"
        filepath = filepath4(prodname,imagecode,vertwo,verfour)
        filemove (filepath, filename)
    elif filename == "asdm-61557.bin":
        vertwo = "6.1"
        verfour = "6.1.5.57"
        filepath = filepath4(prodname,imagecode,vertwo,verfour)
        filemove (filepath, filename)
    elif filename == "asdm-77170.bin":
        vertwo = "7.7"
        verfour = "7.7.1.70"
        filepath = filepath4(prodname,imagecode,vertwo,verfour)
        filemove (filepath, filename)
    #ASDM images that are three or four digits only.
    elif len(splitbydash) == 1:
        asaver = list(splitbydash[0])
        if len(asaver) == 4:
            asamiddle = asaver[1] + asaver[2]
            vertwo = util2digit(asaver[0],asamiddle)
            verthree = util3digit(asaver[0],asamiddle,asaver[3])
            filepath = filepath4(prodname,imagecode,vertwo,verthree)
            filemove (filepath, filename)
        elif len(asaver) == 3:
            vertwo = util2digit(asaver[0],asaver[1])
            verthree = util3digit(asaver[0],asaver[1],asaver[2])
            filepath = filepath4(prodname,imagecode,vertwo,verthree)
            filemove (filepath, filename)
    #ASDM images that are three or four digit with a sub-version.
    elif len(splitbydash) == 2:
        asaver = list(splitbydash[0])
        if len(asaver) == 4:
            asamiddle = asaver[1] + asaver[2]
            vertwo = util2digit(asaver[0],asamiddle)
            verfour = util4digit(asaver[0],asamiddle,asaver[3],splitbydash[1])
            filepath = filepath4(prodname,imagecode,vertwo,verfour)
            filemove (filepath, filename)
        elif len(asaver) == 3:
            vertwo = util2digit(asaver[0],asaver[1])
            verfour = util4digit(asaver[0],asaver[1],asaver[2],splitbydash[1])
            filepath = filepath4(prodname,imagecode,vertwo,verfour)
            filemove (filepath, filename)

    else:
        messageunknownfile ()

def sec_fwsm (filename):
    logging.debug("Sub:    sec_fwsm")
    splitbydot = filename.split(".")
    splitbydash = splitbydot[1].split("-")
    vertwo = util2digit(splitbydash[0],splitbydash[1])
    verthree = util3digit(splitbydash[0],splitbydash[1],splitbydash[2])
    prodname = product("c6svc-fwm")
    filepath = filepath3(prodname,vertwo,verthree)
    filemove (filepath, filename)

def sec_css (filename):
    logging.debug("Sub:    sec_css")
    workname = filename.strip("sg")
    workname = workname.strip("adi-gz")
    workname = workname.strip("adi")
    workname = workname.strip("zip")
    verarray = list(workname)
    prodname = product("css")
    if filename == "cvdm-css-1.0_K9.zip":
        imagecode = imagelookup("devicemgr")
        filepath = filepath2 (prodname,imagecode)
        filemove (filepath, filename)
    if filename == "cvdm-css-1.0.zip":
        imagecode = imagelookup("devicemgr")
        filepath = filepath2 (prodname,imagecode)
        filemove (filepath, filename)
    if len(verarray) == 7:
        verp3 = verarray[5] + verarray[6] + verarray[7]
    else:
        verp3 = verarray[5] + verarray[6]
    verp1 = verarray[0] + verarray[1]
    verp2 = verarray[2] + verarray[3]
    verfull = util4digit(verp1,verp2,verarray[4],verp3)
    filepath = filepath4 (prodname,verp1,verp2,verfull)
    filemove (filepath, filename)

def sec_vpn3000 (filename):
    logging.debug("Sub:    sec_vpn3000")
    prodname = product("vpn3000")
    splitbydash = filename.split("-")
    splitbydot = splitbydash[1].split(".")
    vertwo = util2digit(splitbydot[0],splitbydot[1])
    verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
    filepath = filepath3(prodname,vertwo,verfour)
    filemove (filepath, filename)

def sec_mars_os (filename):
    logging.debug("Sub:    sec_asacx")
    if debug1:
        print("\tSubroutine#\tsec_mars_os")
    prodname = product("mars")
    workname = filename.replace("csmars-","")
    splitbydot = workname.split(".")
    vertwo = util2digit(splitbydot[0],splitbydot[1])
    verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
    filepath = filepath3(prodname,vertwo,verfour)
    filemove (filepath, filename)

def sec_asacx (filename,prodname,imagecode):
    logging.debug("Sub:    sec_asacx")
    workname = filename.replace(".pkg","")
    workname = workname.replace(".img","")
    workname = workname.replace("asacx-sys-","")
    workname = workname.replace("asacx-5500x-boot-","")
    workname = workname.replace("asacx-boot-","")
    splitbydot = workname.split(".")
    if len (splitbydot) == 3:
        verfour = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        filepath = filepath2(prodname,verfour)
        filemove (filepath, filename)
    elif len (splitbydot) == 4:
        verfour = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath2(prodname,verfour)
