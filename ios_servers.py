import os
import logging
import iosutils

# Import all functions that don't start with underscore
for name in dir(iosutils):
    if not name.startswith("_"):
        globals()[name] = getattr(iosutils, name)

def file_proc_servers (filename):
    logging.debug("Module: ios_servers")
    logging.debug("Sub:    file_proc_servers")
    if (
    filename == "B57BCMCD_v15.2.4.1.tgz" or 
    filename == "B57CiscoCD_T6.4.4.3-57712.zip" or 
    filename == "Intel_Windows_drv_MR_6.714.18.00_pv.zip" or 
    filename == "LSI_x64_Signed_Driver_5.2.116.64.zip" or 
    filename == "MR_WINDOWS_DRIVER-6.506.02.00-WHQL.zip" or 
    filename == "intel9.2.3.1023.tar" or 
    filename == "rste_4.5.0.1335_install.zip"
    ):
        prodname = product("ucseseries")
        imagecode = imagelookup("driverseseries")
        utilssinglemove (filename,prodname,imagecode)

    elif (
        filename.startswith("CatC") or 
        filename.startswith("DNAC") or 
        filename.startswith("dnac") or 
        filename.startswith("trustidevcodesigning5")
        ):
        file_proc_servers_catc (filename)

    elif filename.startswith("ucs-catalog"):
        prodname = product("ucsgeneric")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif filename.startswith("pid-ctlg"):
        prodname = product("c2xxm3")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("delnorte") or 
    filename.startswith("delnorte2")
    ):
        prodname = product("c2xxm4")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("plumas1") or 
    filename.startswith("UCSC-C220-M5-")
    ):
        prodname = product("c220m5")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("plumas2") or 
    filename.startswith("UCSC-C240-M5-")
    ):
        prodname = product("c240m5")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("UCSC-C220-M6-")
    ):
        prodname = product("c220m6")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("UCSC-C225-M6-")
    ):
        prodname = product("c225m6")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("UCSC-C240-M6-")
    ):
        prodname = product("c240m6")
        imagecode = imagelookup("catalog")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith ("Collector") or 
    filename.startswith ("collector") or 
    filename == "JeOS_Patch_To_Enable_ASD.zip" or 
    filename == "cspc28backupscript.zip" or 
    filename == "cspc210backupscript.zip"
    ):
        file_proc_servers_cspc (filename)

    elif (
    filename == "efi-obd-v12-07-18.diag" or 
    filename == "efi-obd-v13-10-15.diag" or 
    filename == "efi-obd-v13-7-3.diag"
    ):
        prodname = product("ucseseries")
        imagecode = imagelookup("hdiag")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith ("ucs-cxxx-diag") or
    filename.startswith ("ucs-cxx-diag") or
    filename.startswith ("ucs-cxxx-sdu")
    ):
        prodname = product("ucscseries")
        imagecode = imagelookup("hdiag")
        workname = filename.replace("ucs-cxxx-diag-", "")
        workname = workname.replace("ucs-cxxx-sdu-", "")
        workname = workname.replace("ucs-cxx-diag-", "")
        workname = workname.replace(".iso", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif (
    filename.startswith ("ucs-cxxx-scu") or 
    filename.startswith ("ucs-cxx-scu") or 
    filename.startswith ("ucs-cxx-scu")
    ):
        prodname = product("ucs")
        imagecode = imagelookup("scu")
        workname = filename.replace("ucs-cxxx-scu-", "")
        workname = workname.replace("ucs-cxx-scu-", "")
        workname = workname.replace(".iso", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif (
    filename.startswith ("ucs-scu-")
    ):
        prodname = product("ucs")
        imagecode = imagelookup("scu")
        workname = filename.replace("ucs-scu-", "")
        workname = workname.replace(".iso", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif (
    filename.startswith ("ucs-uefi-diag-") or 
    filename.startswith ("ucs-diag-")
    ):
        prodname = product("ucs")
        imagecode = imagelookup("hdiag")
        workname = filename.replace("ucs-diag-", "")
        workname = workname.replace("ucs-uefi-diag-", "")
        workname = workname.replace(".iso", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    elif (
    filename == "huu-2.3.1.iso" or 
    filename == "huu-2.3.2.iso" or 
    filename == "huu-2.3.3.iso" or 
    filename == "huu-2.4.1.iso" or 
    filename == "huu-3.0.1.iso" or 
    filename == "huu-3.1.1.iso" or 
    filename == "huu_3.1.2.iso" or 
    filename == "huu_3.1.3.iso" or 
    filename == "huu_3.1.4.iso" or 
    filename == "huu_3.2.6.v3.iso" or 
    filename == "ucse-huu-2.1.1.iso" or 
    filename == "ucs-e100-huu-2.2.1.iso"
    ):
        prodname = product("ucseseries")
        imagecode = imagelookup("huu")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename == "DW_16MB_release_1029.bin" or 
    filename == "DW_BIOS.bin.SPA" or 
    filename == "DW_Signed_Bios_Image.bin.SPA" or 
    filename == "1X0DBIOSv4.8" or 
    filename == "1X0SBIOSv4.8" or 
    filename == "Signed_EN_BIOS_1.5.0.4.bin.SPA" or 
    filename.startswith("CIMC_") and filename.endswith(".bin") or 
    filename == "Signed_DW_M1M2_BIOS_2.5.0.4.bin.SPA" or 
    filename == "Signed_DW_M1M2_BIOS_2.5.0.5.bin.SPA" or 
    filename == "Signed_DW_M1M2_BIOS_2.5.0.6.bin.SPA" or 
    filename == "Signed_DW_M1M2_Bios_Image_041015.bin.SPA" or 
    filename == "Signed_EN_BIOS_1.5.0.5.bin.SPA" or 
    filename == "Signed_EN_BIOS_1.5.0.6.bin.SPA" or 
    filename == "Signed_SW_M2_BIOS_1.5.0.6.bin.SPA" or 
    filename == "Signed_SW_M2_BIOS_1.5.0.7.bin.SPA" or 
    filename == "Signed_SW_M2_BIOS_1.5.0.8.bin.SPA" or 
    filename == "Signed_SW_M2_Bios_1.5.0.5.bin.SPA" or 
    filename == "UCSEDM3_BIOS_2.4.SPA" or 
    filename == "UCSEDM3_BIOS_2.5.SPA" or 
    filename == "UCSEDM3_BIOS_2.6.SPA" or 
    filename == "UCSE_CIMC_2.3.1.bin" or 
    filename == "UCSE_CIMC_2.3.2.bin" or 
    filename == "UCSE_CIMC_2.3.3.bin" or 
    filename == "UCSE_CIMC_2.3.5.bin" or 
    filename == "update_pkg-Mar-22-MR-rebuild.bin" or 
    filename == "update_pkg-ucse.combined.120808.bin" or 
    filename == "update_pkg-ucse.combined.REL.2.2.2.bin" or 
    filename == "update_pkg-ucse.combined.REL.2.2.1.bin" or 
    filename == "update_pkg-ucse.combined.REL.bin" or 
    filename == "SW_16MB_release_1102.bin" or 
    filename == "SW_Signed_Bios_Image.bin.SPA"
    ):
        prodname = product("ucseseries")
        imagecode = imagelookup("firmwareeseries")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename == "UCS_docs_20110510.iso"
    ):
        prodname = product("ucsgeneric")
        imagecode = imagelookup("docs")
        utilssinglemove (filename,prodname,imagecode)

    elif (
    filename.startswith("ucs") or 
    filename == "b2xx-m1-drivers-1.1.1j.iso" or 
    filename == "c2xx-m1-utils-1.0.2.iso"
    ):
        file_proc_servers_ucs (filename)

    elif (
    filename == "BashFix-update-0-x86_64.tar.gz" or 
    filename == "Datacenter_Technology_Pack-1.0.53.ubf" or 
    filename == "Datacenter_Technology_Pack_Update_1_Patch-1.0.58.ubf" or 
    filename == "GlibcFix-pi22-update-0-x86_64.tar.gz" or 
    filename == "PrimeInfra.pem" or 
    filename == "ca_technology_package-2.1.0.0.41.ubf" or 
    filename == "operations_center_pi_2_1_2_enable_update.ubf" or 
    filename == "rhel-vulnerability-patch-pnp-2.2.0.14.tar.gz" or 
    filename == "InstallerUpdateBE-1.0.5.tar.gz" or 
    filename.startswith ("CiscoPI") or 
    filename.startswith ("Device-Pack") or 
    filename.startswith ("PI") or 
    filename.startswith ("pi") or 
    filename.startswith ("PNP-GATEWAY-VM-") or 
    filename.startswith ("cisco-prime-pnp") or 
    filename.startswith ("pnp-") or 
    filename.startswith ("DnacPreCheckASSESMENTUbf")
    ):
        file_proc_servers_primeinfra (filename)

    elif (
    filename.startswith ("Cisco_ACI") or 
    filename.startswith ("acisim") or 
    filename.startswith ("aci-simulator") or 
    filename.startswith ("aci-apic") or 
    filename.startswith ("aci-msft-pkg") or 
    filename.startswith ("aci-n9000-dk9") or 
    filename.startswith ("apic-vrealize") or 
    filename.startswith ("esx-msc") or 
    filename.startswith ("msc") or 
    filename.startswith ("vcenter-plugin") or 
    filename.startswith ("tools-msc")
    ):
        prodname = product("aci")
        file_proc_servers_aci(debug1,filename,prodname)

    elif (
    filename.startswith ("storfs-packages") or 
    filename.startswith ("HX-ESXi") or 
    filename.startswith ("HX-Kubernetes") or 
    filename.startswith ("Cisco-HX-Data-Platform-Installer") or
    filename.startswith ("cisco-HX-Data-Platform-Installer") or
    filename.startswith ("HyperFlex-VC-HTML") or 
    filename.startswith ("hxcsi") or 
    filename.startswith ("HyperFlex-Witness-") or 
    filename.startswith ("HxClone-HyperV")
    ):
        prodname = product("hyperflex")
        file_proc_servers_hyperflex(debug1,filename,prodname)

    elif (
    filename.startswith ("DCNM") or 
    filename.startswith ("dcnm")
    ):
        prodname = product("dcnm")
        file_proc_servers_dcnm(debug1,filename,prodname)

    elif filename == "readme_10.2.1.ST.1":
        prodname = product("dcnm")
        filepath = filepath3(prodname,"10.2","10.2.1")
        filemove (filepath, filename)

    elif (
    filename.startswith ("apic_em_update-apic-") or 
    filename.startswith ("APIC-EM-")
    ):
        file_proc_servers_apicem(debug1,filename)

    elif (
    filename.startswith ("CIMCS_") or 
    filename.startswith ("cimcs_")
    ):
        file_proc_servers_cimcsup (filename)

    elif (
    filename.startswith ("cml2") or 
    filename.startswith ("refplat")
    ):
        file_proc_servers_cml (filename)

    else:
        messageunknownfile()

def file_proc_servers_cspc (filename: str) -> str:
    logging.debug("Sub:    file_proc_servers_cspc")
    """
    Extract the core version number from Cisco Collector filenames,
    stripping 'Collector-', 'collector_', '-B-*', '_Build-*', and anything after.

    Examples:
        Collector-2.11-B-16_SHA1_signed.ova -> 2.11
        collector_2.11.0.1_Build-4.zip -> 2.11.0.1
    """
    #logging.debug(f"Extracting version from: {filename}")
    prodname = product("cspc")
    # Remove leading Collector- or collector_
    cleaned = re.sub(r"^(Collector-|collector_)", "", filename, flags=re.IGNORECASE)

    # Remove anything starting with -B- or _Build and beyond
    cleaned = re.split(r"-B-|_Build", cleaned, maxsplit=1)[0]

    # Remove any trailing non-version characters (like underscores, hyphens, etc.)
    match = re.search(r"(\d+(?:\.\d+)+)", cleaned)
    if match:
        finalfilepath = filepath(prodname,cleaned)
        filemove (finalfilepath, filename)
    else:
        logging.warning(f"Unrecognized filename format: {filename}")


def file_proc_servers_cml (filename):
    logging.debug("Sub:    file_proc_servers")
    if filename.startswith("cml2_f_"):
        prodname = product("cmlf")
        workname = filename.replace("cml2_f_", "")
        workname = workname.replace("_amd64-32-iso.zip", "")
        workname = workname.replace("_amd64-32-pkg.zip", "")
        workname = workname.replace("_amd64-32.ova", "")
        workname = workname.replace("_amd64-32-iso.zip", "")
        splitbydot = workname.split(".")
        version2 = util2digit(splitbydot[0],splitbydot[1])
        version4 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        filepath = filepath3(prodname,version2,version4)
        filemove (filepath, filename)
    elif filename.startswith("cml2_"):
        prodname = product("cml")
        workname = filename.replace("cml2_", "")
        workname = workname.replace("_amd64-32-iso.zip", "")
        workname = workname.replace("_amd64-32-pkg.zip", "")
        workname = workname.replace("_amd64-32.ova", "")
        workname = workname.replace("_amd64-32-iso.zip", "")
        splitbydot = workname.split(".")
        version2 = util2digit(splitbydot[0],splitbydot[1])
        version4 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        filepath = filepath3(prodname,version2,version4)
        filemove (filepath, filename)
    elif filename.startswith("refplat"):
        prodname = product("refplat")
        workname = filename.replace("refplat-", "")
        workname = workname.replace("-freetier-iso.zip", "")
        workname = workname.replace("-supplemental-iso.zip", "")
        workname = workname.replace("-fcs-iso.zip", "")
        workname = workname.replace("-fcs.iso", "")
        splitbydot = list(workname)
        versionyear = splitbydot[0] + splitbydot[1] + splitbydot[2] + splitbydot[3]
        versionmon = splitbydot[4] + splitbydot[5]
        versionday = splitbydot[6] + splitbydot[7]
        version = versionyear + "-" + versionmon + "-" + versionday
        filepath = filepath2(prodname,version)
        filemove (filepath, filename)
        

def file_proc_servers_cimcsup (filename): 
    logging.debug("Sub:    file_proc_servers_cimcsup")
    prodname = product("cimcs")
    workname = filename.replace("CIMCS_", "")
    workname = workname.replace("cimcs_patch_", "")
    workname = workname.replace("_eval_signed.zip", "")
    workname = workname.replace("_signed.zip", "")
    workname = workname.replace(".zip", "")
    workname = workname.replace("_VMWARE_EVAL", "")
    workname = workname.replace("_VMWARE_GA", "")
    workname = workname.replace("_HYPERV_EVAL", "")
    workname = workname.replace("_HYPERV_GA", "")
    workname = workname.replace("_HYPERV_SIGNED_EVAL", "")
    workname = workname.replace("_VMWARE_SIGNED_EVAL", "")
    workname = workname.replace("_VMWARE", "")
    workname = workname.replace("_HYPERV", "")
    splitbyuscore= workname.split("_")
    version2 = util2digit(splitbyuscore[0],splitbyuscore[1])
    version4 = util4digit(splitbyuscore[0],splitbyuscore[1],splitbyuscore[2],splitbyuscore[3])
    filepath = filepath3(prodname,version2,version4)
    filemove (filepath, filename)

def file_proc_servers_catc (filename): 
    logging.debug("Sub:    file_proc_servers_catc")
    prodname = product("dnac")
    workname = filename.replace("trustidevcodesigning5-", "")
    workname = workname.replace("CatC-SW-Launcher-", "")
    workname = workname.replace("DNAC-SW-Launcher-", "")
    workname = workname.replace("CatC-SW-", "")
    workname = workname.replace("CatC-witness-", "")
    workname = workname.replace("CatC-", "")
    workname = workname.replace("dnac", "")
    workname = workname.replace("DNAC-SW-", "")
    workname = workname.replace("-upgrade.tar.gz.sig", "")
    workname = workname.replace("-upgrade.tar.gz", "")
    workname = workname.replace("_MigrationScript_v1.tar.gz.sig", "")
    workname = workname.replace("_MigrationScript_v1.tar.gz", "")
    workname = workname.replace("_cisco_image_verification_key.pub", "")
    workname = workname.replace(".tar.gz.sig", "")
    workname = workname.replace(".tar.gz", "")
    workname = workname.replace(".iso.part1.rar", "")
    workname = workname.replace(".iso.part2.rar", "")
    workname = workname.replace(".iso.part2.rar", "")
    workname = workname.replace(".iso", "")
    workname = workname.replace(".sig", "")
    workname = workname.replace(".ova", "")
    splitbydot = workname.split(".")
    version2 = util2digit(splitbydot[0],splitbydot[1])
    try:
        versionfull = util4digit(splitbydot[0],splitbydot[1],splitbydot[2],splitbydot[3])
    except:
        versionfull = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
    
    if "MigrationScript" in filename:
        imagecode = imagelookup("migration")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)
    elif "Launcher" in filename:
        imagecode = imagelookup("launcher")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)
    elif "trustidevcodesigning5" in filename:
        imagecode = imagelookup("certs")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)
    elif "CatC-witness-" in filename:
        imagecode = imagelookup("witness")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)
    elif "-upgrade.tar.gz" in filename:
        imagecode = imagelookup("upgrade")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)
    elif (
        "_cisco_image_verification_key.pub" in filename or 
        ".ova" in filename or
        ".iso.sig" in filename or
        ".iso" in filename 
        ):
        imagecode = imagelookup("system")
        filepath = filepath4(prodname,version2,versionfull,imagecode)
        filemove (filepath, filename)

def file_proc_servers_apicem (filename):
    logging.debug("Sub:    file_proc_servers_apicem")
    splitbydash = filename.split("-")
    if debug1:
        print("\tSubroutine#\tfile_proc_servers_apicem")
    prodname = product("apicem")
    if filename.startswith ("apic_em_update-apic"):
        splitbydash = filename.split("-")
        splitbydot = splitbydash[3].split(".")
    elif filename.startswith ("APIC-EM"):
        splitbydash = filename.split("-")
        splitbydot = splitbydash[2].split(".")
    vertwo = util2digit(splitbydot[0],splitbydot[1])
    verthree = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
    filepath = filepath3(prodname,vertwo,verthree)
    filemove (filepath, filename)

def file_proc_servers_dcnm (filename,prodname):
    logging.debug("Sub:    file_proc_servers_dcnm")
    splitbydot = filename.split(".")
    vertwo = util2digit (splitbydot[1],splitbydot[2])
    verthree = util3digit (splitbydot[1],splitbydot[2],splitbydot[3])
    if filename.startswith ("dcnm-installer-x64-windows"):
        imagecode = imagelookup("installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-installer-windows"):
        imagecode = imagelookup("installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-installer-x64-linux"):
        imagecode = imagelookup("installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-installer-linux"):
        imagecode = imagelookup("installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-installer-solaris"):
        imagecode = imagelookup("installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("DCNMUpgradeTool"):
        imagecode = imagelookup("upgrade")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif (
    filename.startswith ("dcnm-va-templates") or 
    filename.startswith ("dcnm_fabricpath_fabric_templates") or 
    filename.startswith ("dcnm_deprecated_templates") or 
    filename.startswith ("dcnm_ip_vxlan_fabric_templates")
    ):
        imagecode = imagelookup("templates")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-va"):
        imagecode = imagelookup("va")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-se"):
        imagecode = imagelookup("installer-ase")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-se"):
        imagecode = imagelookup("installer-ase")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-silent-installer-properties"):
        imagecode = imagelookup("silent-installer")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-san-client"):
        imagecode = imagelookup("san-client")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-device-pack"):
        imagecode = imagelookup("device-pack")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("dcnm-va-ovf-kvm-files"):
        imagecode = imagelookup("virtual-ovf")
        filepath = filepath4(prodname,vertwo,verthree,imagecode)
        filemove (filepath, filename)

def file_proc_servers_hyperflex (filename,prodname):
    logging.debug("Sub:    file_proc_servers_hyperflex")
    if filename.startswith ("storfs-packages"):
        workname = filename.replace("storfs-packages-", "")
        workname = workname.replace(".tgz", "")
        splitbydot = workname.split(".")
        vertwo = util2digit (splitbydot[0],splitbydot[1])
        verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
        imagecode = imagelookup("upgrade")
        filepath = filepath4(prodname,imagecode,vertwo,verthree)
        filemove (filepath, filename)
    elif filename.startswith ("HX-ESXi"):
        workname = filename.replace("HX-ESXi-", "")
        splitbydash = workname.split("-")
        imagecode = imagelookup("vmware")
        filepath = filepath3(prodname,imagecode,splitbydash[0])
        filemove (filepath, filename)
    elif filename.startswith ("HX-Kubernetes"):
        workname = filename.replace("HX-Kubernetes-", "")
        splitbydot = workname.split(".")
        vertwo = util2digit (splitbydot[0],splitbydot[1])
        verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
        imagecode = imagelookup("kubernetes")
        filepath = filepath4(prodname,imagecode,vertwo,verthree)
        filemove (filepath, filename)
    elif (
        filename.startswith ("Cisco-HX-Data-Platform-Installer") or 
        filename.startswith ("cisco-HX-Data-Platform-Installer")
    ):
        workname = filename.replace("Cisco-HX-Data-Platform-Installer-v", "")
        workname = workname.replace("cisco-HX-Data-Platform-Installer-v", "")
        workname = workname.replace("p1-esx.ova", "")
        workname = workname.replace("-esx.ova", "")
        workname = workname.replace("-hyperv.vhdx.zip", "")
        splitbydot = workname.split(".")
        vertwo = util2digit (splitbydot[0],splitbydot[1])
        verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
        imagecode = imagelookup("install")
        filepath = filepath4(prodname,imagecode,vertwo,verthree)
        filemove (filepath, filename)
    elif filename.startswith ("HyperFlex-VC-HTML"):
        imagecode = imagelookup("vchtmlplug")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("hxcsi"):
        imagecode = imagelookup("kubernetes")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("HyperFlex-Witness-"):
        imagecode = imagelookup("witness")
        filepath = filepath2(prodname,imagecode)
        filemove (filepath, filename)
    elif filename.startswith ("HxClone-HyperV"):
        workname = filename.replace("HxClone-HyperV-v", "")
        workname = workname.replace(".ps1", "")
        splitbydot = workname.split(".")
        vertwo = util2digit (splitbydot[0],splitbydot[1])
        verthree = util3digit (splitbydot[0],splitbydot[1],splitbydot[2])
        imagecode = imagelookup("install")
        filepath = filepath4(prodname,imagecode,vertwo,verthree)
        filemove (filepath, filename)


def file_proc_servers_aci (filename,prodname):
    logging.debug("Sub:    file_proc_servers_aci")
    if (
    filename.startswith("tools-msc-") or 
    filename.startswith("esx-msc-") or 
    filename.startswith("msc-")
    ):
        imagecode = imagelookup("mso")
        workname = filename.replace("tools-msc-", "")
        workname = workname.replace("esx-msc-", "")
        workname = workname.replace("msc-", "")
        workname = workname.replace(".ova", "")
        workname = workname.replace(".tar.gz", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("Cisco_ACI_Virtual_Edge_")
    ):
        imagecode = imagelookup("acive")
        workname = filename.replace("Cisco_ACI_Virtual_Edge_", "")
        workname = workname.replace("-pkg.zip", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("aci-apic-dk9.")
    ):
        imagecode = imagelookup("apic")
        workname = filename.replace("aci-apic-dk9.", "")
        workname = workname.replace(".iso", "")
        workname = workname.replace(".ova", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("aci-msft-pkg-")
    ):
        imagecode = imagelookup("aciplgms")
        workname = filename.replace("aci-msft-pkg-", "")
        workname = workname.replace(".zip", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("vcenter-plugin-")
    ):
        imagecode = imagelookup("aciplgvc")
        workname = filename.replace("vcenter-plugin-", "")
        workname = workname.replace(".tgz", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("apic-vrealize-")
    ):
        imagecode = imagelookup("aciplgvs")
        workname = filename.replace("apic-vrealize-", "")
        workname = workname.replace(".tgz", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("aci-n9000-dk9.")
    ):
        imagecode = imagelookup("n9kacim")
        workname = filename.replace("aci-n9000-dk9.", "")
        workname = workname.replace(".bin", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("acisim-")
    ):
        imagecode = imagelookup("acisim")
        workname = filename.replace("acisim-", "")
        workname = workname.replace("_part1.ova", "")
        workname = workname.replace("_part2.ova", "")
        workname = workname.replace("_part3.ova", "")
        workname = workname.replace("_part4.ova", "")
        workname = workname.replace("_part5.ova", "")
        workname = workname.replace("_part6.ova", "")
        workname = workname.replace("_part7.ova", "")
        workname = workname.replace("_part8.ova", "")
        workname = workname.replace("_part9.ova", "")
        workname = workname.replace("-",".")
        splitbydot = workname.split(".")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)
    elif (
    filename.startswith("aci-simulator-dk9.")
    ):
        imagecode = imagelookup("acisim")
        workname = filename.replace("aci-simulator-dk9.", "")
        workname = workname.replace(".iso", "")
        utils_dev_imagecode_v2_vf (filename,prodname,imagecode,workname)

    else:
        messageunknownfile()

def file_proc_servers_primeinfra (filename):
    logging.debug("Sub:    file_proc_servers_primeinfra")
    splitbydash = filename.split("-")
    prodname = product("cpi")

    if (
    filename == "PrimeInfra.pem" or 
    filename == "PI_3_2_FIPS_Update_01-1.0.0.ubf" or 
    filename == "PI-APL-3.2.50.0.70-1-K9.iso.signature" or 
    filename == "PI-APL-3.2.50.0.70-1-K9.iso" or 
    filename == "PI-VA-3.2.50.0.70.ova"
    ):
        utilssinglemove (filename,prodname,"3.2-FIPS")

    elif (
    filename == "PI_1.4_0_45_Update_1-39.tar.gz" or 
    filename == "PI_1_4_0_45-CSCui77571-2.tar.gz" or 
    filename == "PI_1_4-CSCum71308-0.tar.gz" or 
    filename == "PI-upgrade-bundle-1.4.0.45-2.tar.gz" or 
    filename == "PI-VA-1.4.0.45-2-large.ova" or 
    filename == "PI-VA-1.4.0.45-2-medium.ova" or 
    filename == "PI-VA-1.4.0.45-2-small.ova" or 
    filename == "PI-VA-1.4.0.45-2-xl.ova"
    ):
        utilssinglemove (filename,prodname,"1.4")


    elif (
    filename == "pi_2.0device_packs_5-39.ubf" or 
    filename == "PI_2_0-CSCum71308-0.tar.gz" or 
    filename == "pi_update_2.0-3.zip" or 
    filename == "PI-APL-2.0.0.0.294-2-K9.iso" or 
    filename == "PI-Upgrade-2.0.0.0.294-2.tar.gz" or 
    filename == "PI-VA-2.0.0.0.294-2-Express.ova" or 
    filename == "PI-VA-2.0.0.0.294-2-Pro.ova" or 
    filename == "PI-VA-2.0.0.0.294-2-Standard.ova" or 
    filename == "PI-VA-2.0.0.0.294-Pro.ova" or 
    filename == "PI-VA-2.0.0.0.294-Standard.ova"
    ):
        utilssinglemove (filename,prodname,"2.0")


    elif (
    filename == "pi_2.1device_packs_5-45.ubf" or 
    filename == "ca_technology_package-2.1.0.0.41.ubf" or 
    filename == "operations_center_pi_2_1_2_enable_update.ubf" or 
    filename == "pi_2.1device_packs_8-56.ubf" or 
    filename == "pi212_20141118_01.ubf" or 
    filename == "pi212_PIGEN_CSCur43834_01.ubf" or 
    filename == "Datacenter_Technology_Pack-1.0.53.ubf" or 
    filename == "Datacenter_Technology_Pack_Update_1_Patch-1.0.58.ubf" or 
    filename == "PI-APL-2.1.0.0.87-1-K9.iso" or 
    filename == "PI-Upgrade-2.1.0.0.87.tar.gz" or 
    filename == "PI-VA-2.1.0.0.87-Express.ova" or 
    filename == "PI-VA-2.1.0.0.87-Pro.ova" or 
    filename == "PI-VA-2.1.0.0.87-Standard.ova"
    ):
        utilssinglemove (filename,prodname,"2.1")


    elif (
    filename == "GlibcFix-pi22-update-0-x86_64.tar.gz" or 
    filename == "pi_2.2_device-pack_10-72.ubf" or 
    filename == "pi22_disable3des-1.ubf" or 
    filename == "pi222_Update_04-3.ubf" or 
    filename == "pi223_Update_06-8.ubf" or 
    filename == "pi223-26.ubf" or 
    filename == "PI-APL-2.2.0.0.158-1-K9.iso" or 
    filename == "PI-UCS-APL-2.2.0.0.158-1-K9.iso" or 
    filename == "PI-UCS-APL-2.2.0.0.158-1-K9-usb.img" or 
    filename == "PI-VA-2.2.0.0.158.ova"
    ):
        utilssinglemove (filename,prodname,"2.2")

    elif (
    filename == "PI-Upgrade-3.0.X_to_3.1.0.0.132.tar.gz" or 
    filename == "PI-VA-3.1.0.0.132.ova" or 
    filename == "Device-Pack-16-PI3.1-133.ubf" or 
    filename == "PI_3_1_7_update_05-1.0.11.ubf" or 
    filename == "PI_3_1_7-1.0.16.ubf" or 
    filename == "PI-APL-3.1.0.0.132-1-K9.iso" or 
    filename == "PI_3_1_7-1.0.16.ubf" or 
    filename == "PI_3_1_7-1.0.16.ubf"
    ):
        utilssinglemove (filename,prodname,"3.1")

    elif (
    filename == "Device-Pack-4-PI3.2-12.ubf" or 
    filename == "PI_3_2_2-1.0.13.ubf" or 
    filename == "PI_3_2_2_update_05-1.0.5.ubf" or 
    filename == "PI-VA-3.2.0.0.258.ova" or 
    filename == "PI-APL-3.2.0.0.258-1-K9.iso.signature" or 
    filename == "PI-APL-3.2.0.0.258-1-K9.iso" or 
    filename == "PI-Upgrade-3.X_to_3.2.0.0.258.tar.gz" or 
    filename == "CiscoPI3.2.pem" or 
    filename == "InstallerUpdateBE-1.0.5.tar.gz"
    ):
        utilssinglemove (filename,prodname,"3.2")

    elif (

    filename == "PI-Upgrade-3.3.0.0.342.tar.gz" or
    filename == "PI-APL-3.3.0.0.342-1-K9.iso" or
    filename == "PI-VA-3.3.0.0.342.ova" or
    filename == "PI-APL-3.3.0.0.342-1-K9.iso.signature" or
    filename == "CiscoPI3.3.pem" or
    filename == "PI_3_3_1-1.0.15.ubf" or
    filename == "PI_3_3_1_update_04-1.0.4.ubf" or
    filename == "PI_3_3_1_update_04-1.0.5.ubf" or
    filename == "Device-Pack-4-Update-03-PI3.3-2.ubf" or
    filename == "Device-Pack-4-PI3.3-11.ubf"
    ):
        utilssinglemove (filename,prodname,"3.3")

    elif (
    filename == "PI_3_4_2_Update_01-1.0.2.ubf" or
    filename == "PI_3_4_2-1.0.23.ubf" or
    filename == "PI_3_4_1_Update_02-1.0.9.ubf" or
    filename == "PI_3_4_1-1.0.27.ubf" or
    filename == "PI-VA-3.4.0.0.348.ova" or
    filename == "PI-APL-3.4.0.0.348-1-K9.iso" or
    filename == "CiscoPI3.4.pem" or
    filename == "PI_BUNDLE-3.4.0.0.348-Upgrade.tar.gz" or
    filename == "PI-APL-3.4.0.0.348-1-K9.iso.signature" or
    filename == "Device-Pack-2-PI3.4-07.ubf" or
    filename == "Device-Pack-4-PI3.4-11.ubf" or
    filename == "Device-Pack-9-PI3.4-09.ubf" or
    filename == "Device-Pack-11-PI3.4-09.ubf"
    ):
        utilssinglemove (filename,prodname,"3.4")

    elif (
    filename == "PI-Upgrade-3.X_to_3.5.0.0.550.tar.gz" or
    filename == "PI-APL-3.5.0.0.550-1-K9.iso.signature" or
    filename == "PI_3_5_Update_01-1.0.10.ubf" or
    filename == "PI-APL-3.5.0.0.550-1-K9.iso" or
    filename == "CiscoPI3.5.pem" or
    filename == "PI-VA-3.5.0.0.550.ova" or
    filename == "PI_3_5_1-1.0.22.ubf" or
    filename == "PI_3_5_1_Security_Update_02_Part_02of02-1.0.7.ubf" or
    filename == "PI_3_5_1_Security_Update_02_Part_01of02-1.0.4.ubf" or
    filename == "PI_3_5_1_Update_02-1.0.21.ubf" or
    filename == "Device-Pack-1-PI3.5-29.ubf" or
    filename == "Device-Pack-4-PI3.5-21.ubf" or
    filename == "DnacPreCheckASSESMENTUbf_3_5-1.0.3.ubf"
    ):
        utilssinglemove (filename,prodname,"3.5")

    elif (
    filename == "Device-Pack-1-PI3.6-13.ubf" or
    filename == "PI_3_6_Update_03-1.0.2.ubf" or
    filename == "PI-VA-3.6.0.0.172.ova" or
    filename == "PI-Upgrade-3.4_to_3.6.0.0.172.tar.gz" or
    filename == "PI-APL-3.6.0.0.172-1-K9.iso.signature" or
    filename == "PI-APL-3.6.0.0.172-1-K9.iso" or
    filename == "CiscoPI3.6.pem" or
    filename == "PI-Upgrade-3.5_to_3.6.0.0.172.tar.gz" or
    filename == "DnacPreCheckASSESMENTUbf_3_6-1.0.5.ubf"
    ):
        utilssinglemove (filename,prodname,"3.6")

    elif (
    filename == "Device-Pack-2-PI3.7-17.ubf" or
    filename == "PI_3_7_1_Update_04-1.0.4.ubf" or
    filename == "PI_3_7_1-1.0.36.ubf" or
    filename == "PI_3_7_Update_03-1.0.2.ubf" or
    filename == "PI-VA-3.7.0.0.159.ova" or
    filename == "PI-Upgrade-31x_32x_33x_34x_to_3.7.0.0.159.tar.gz" or
    filename == "PI-Upgrade-35x_36x_to_3.7.0.0.159.tar.gz" or
    filename == "CiscoPI3.7.pem" or
    filename == "PI-APL-3.7.0.0.159-1-K9.iso.signature" or
    filename == "PI-APL-3.7.0.0.159-1-K9.iso" or
    filename == "DnacPreCheckASSESMENTUbf_3_7-1.0.4.ubf"
    ):
        utilssinglemove (filename,prodname,"3.7")

    elif (
    filename == "Device-Pack-1-PI3.8-22.ubf" or
    filename == "PI_3_8_1-1.0.26.ubf" or
    filename == "PI_3_8_Update_02-1.0.15.ubf" or
    filename == "PI-APL-3.8.0.0.310-1-K9.iso" or
    filename == "PI-APL-3.8.0.0.310-1-K9.iso.signature" or
    filename == "CiscoPI3.8.pem" or
    filename == "PI-VA-3.8.0.0.310.ova" or
    filename == "PI-Upgrade-36x_37x_to_3.8.0.0.310.tar.gz" or
    filename == "DnacPreCheckASSESMENTUbf_3_8-1.0.3.ubf"
    ):
        utilssinglemove (filename,prodname,"3.8")

    elif (
    filename == "PI_3_9_Oct_Oracle_patch-1.0.8.ubf" or
    filename == "PI-APL-3.9.0.0.219-1-K9.iso" or
    filename == "PI-APL-3.9.0.0.219-1-K9.iso.signature" or
    filename == "CiscoPI3.9.pem" or
    filename == "PI-Upgrade-37x_38x_to_3.9.0.0.219.tar.gz" or
    filename == "PI-VA-3.9.0.0.219.ova" or
    filename == "DnacPreCheckASSESMENTUbf_3_9-1.0.5.ubf"
    ):
        utilssinglemove (filename,prodname,"3.9")

    elif (
    filename == "PNP-GATEWAY-VM-2.2.0.15.ova" or 
    filename == "pnp-kickstart-2.2.0.15-K9.iso" or 
    filename == "pnp-packaging-2.2.0.15.tar.gz"
    ):
        utilssinglemove (filename,prodname,"PNP/3.1")

    elif (
    filename == "PNP-GATEWAY-VM-2.0.0.28.ova" or 
    filename == "pnp-packaging-2.0.0.30.tar.gz" or 
    filename == "pnp-gateway-patch-2.0.0.28.tar.gz" or 
    filename == "cisco-prime-pnp-app-k9-2.0.0.28.zip"
    ):
        utilssinglemove (filename,prodname,"PNP/2.0")

    elif (
    filename == "PNP-GATEWAY-VM-2.2.0.9.ova" or 
    filename == "pnp-packaging-2.2.0.10.tar.gz" or 
    filename == "pnp-packaging-2.2.0.9.tar.gz" or 
    filename == "rhel-vulnerability-patch-pnp-2.2.0.14.tar.gz"
    ):
        utilssinglemove (filename,prodname,"PNP/2.2")

    elif (
    filename == "pnp-kickstart-2.2.0.14-K9.iso" or 
    filename == "pnp-packaging-2.2.0.14.tar.gz"
    ):
        utilssinglemove (filename,prodname,"PNP/2.2")

    elif (
    filename == "cisco-prime-pnp-app-k9-2.0.1.2.zip"
    ):
        utilssinglemove (filename,prodname,"PNP/3.0-3.1")


    else:
        utilssingleprodname (filename,prodname)

def file_proc_servers_ucs (filename):
    logging.debug("Sub:    file_proc_servers_ucs")

    splitbydash = filename.split("-")

    if filename.startswith("ucs-utils"):
        prodname = product("ucsgeneric")
        imagecode = imagelookup("utils")

    elif (
    filename.startswith("ucs-drivers") or 
    filename.startswith("ucs-b2xx-drivers") or 
    filename.startswith("ucs-bxxx-drivers") or 
    filename.startswith("ucs-c2xx-drivers") or 
    filename.startswith("ucs-cxxx-drivers") or 
    filename.startswith("ucs-cxxx-fw") or 
    filename == "b2xx-m1-drivers-1.1.1j.iso"
    ):
        if filename == "ucs-drivers.1.0.2.iso":
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsb")
            file_proc_servers_p2_d3 (filename,prodname,imagecode)
        elif filename == "b2xx-m1-drivers-1.1.1j.iso":
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsc")
            file_proc_servers_p3_d3 (filename,prodname,imagecode)
        elif filename.startswith("ucs-cxxx-drivers") or filename.startswith("ucs-c2xx-drivers"):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsc")
            file_proc_servers_p2_d3 (filename,prodname,imagecode)
        elif filename.startswith("ucs-cxxx-fw"):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsc")
            file_proc_servers_p2_d3 (filename,prodname,imagecode)
        elif filename.startswith("ucs-bxxx-drivers"):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsb")
            file_proc_servers_p2_d3 (filename,prodname,imagecode)
        elif filename.startswith("ucs-b2xx-drivers"):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("driversucsb")
            file_proc_servers_p2_d3 (filename,prodname,imagecode)

    elif (
    filename.startswith("ucs_k9_bundle") or 
    filename.startswith("ucs-k9-bundle") or 
    filename.startswith("ucs-k9-bundle-b-series") or 
    filename.startswith("ucs-k9-bundle-c-series") or 
    filename.startswith("ucs-k9-bundle-infra") or 
    filename.startswith("ucs-k9-bundle-m-series") or 
    filename.startswith("ucs-mini-k9-bundle-infra") or 
    filename.startswith("ucs-6300-k9-bundle-infra") or 
    filename.startswith("ucs-6400-k9-bundle-infra")
    ):
        prodname = product("ucsgeneric")
        imagecode = imagelookup("ucsbundle")
        file_proc_servers_p2_d3 (filename,prodname,imagecode)

    elif (
    filename.startswith("ucs-b2xx-utils") or 
    filename.startswith("ucs-bxxx-utils") or 
    filename.startswith("ucs-c2xx-utils") or 
    filename.startswith("ucs-cxxx-utils") or 
    filename == "c2xx-m1-utils-1.0.2.iso"
    ):
        if (
        filename.startswith("ucs-b2xx-utils-") and filename.endswith("-vmware.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("vmware")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename == "c2xx-m1-utils-1.0.2.iso"
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            utilssinglemove (filename,prodname,imagecode)

        elif (
        filename.startswith("ucs-b2xx-utils-") and filename.endswith("-windows.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("windows")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-b2xx-utils-") and filename.endswith("-linux.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("ucslinux")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-c2xx-utils-") and filename.endswith("-vmware.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("vmware")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-c2xx-utils-") and filename.endswith("-windows.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("windows")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-c2xx-utils-") and filename.endswith("-linux.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("ucslinux")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-c2xx-utils-") and filename.endswith("-efi.iso")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("efi")
            file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2)

        elif (
        filename.startswith("ucs-bxxx-utils-vmware") or 
        filename.startswith("ucs-b2xx-utils-vmware")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("vmware")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-cxxx-utils-vmware") or 
        filename.startswith("ucs-c2xx-utils-vmware")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("vmware")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-bxxx-utils-windows") or 
        filename.startswith("ucs-b2xx-utils-windows")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("windows")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-cxxx-utils-windows") or 
        filename.startswith("ucs-c2xx-utils-windows")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("windows")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-bxxx-utils-linux") or 
        filename.startswith("ucs-b2xx-utils-linux")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilsbseries")
            imagecode2 = imagelookup("ucslinux")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-cxxx-utils-linux") or 
        filename.startswith("ucs-c2xx-utils-linux")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("ucslinux")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)
        elif (
        filename.startswith("ucs-cxxx-utils-efi") or 
        filename.startswith("ucs-c2xx-utils-efi")
        ):
            prodname = product("ucsgeneric")
            imagecode = imagelookup("utilscseries")
            imagecode2 = imagelookup("efi")
            file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2)


    elif splitbydash[0] == "ucs" and splitbydash[2] == "huu":
        prodname = product(splitbydash[1])
        imagecode = imagelookup(splitbydash[2])
        file_proc_servers_p3_d3 (filename,prodname,imagecode)

def file_proc_servers_p2_d3 (filename,prodname,imagecode):
    logging.debug("Sub:    file_proc_servers_p2_d3")
    splitbydot = filename.split(".")
    ver2 = util2digit(splitbydot[1],splitbydot[2])
    ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
    filepath = filepath4(prodname,imagecode,ver2,ver3)
    filemove (filepath, filename)

def file_proc_servers_p2_d3_utils (filename,prodname,imagecode,imagecode2):
    logging.debug("Sub:    file_proc_servers_p2_d3_utils")
    splitbydot = filename.split(".")
    ver2 = util2digit(splitbydot[1],splitbydot[2])
    ver3 = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
    filepath = filepath5(prodname,imagecode,ver2,ver3,imagecode2)
    filemove (filepath, filename)

def file_proc_servers_p3_d3 (filename,prodname,imagecode):
    logging.debug("Sub:    file_proc_servers_p3_d3")
    splitbydash = filename.split("-", 3)
    splitbydot = splitbydash[3].split(".")
    ver2 = util2digit(splitbydot[0],splitbydot[1])
    ver3 = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
    filepath = filepath4(prodname,imagecode,ver2,ver3)
    filemove (filepath, filename)

def file_proc_servers_p3_d3_utils (filename,prodname,imagecode,imagecode2):
    logging.debug("Sub:    file_proc_servers_p3_d3_utils")
    splitbydash = filename.split("-", 3)
    splitbydot = splitbydash[3].split(".")
    workname = splitbydot[2].replace("-vmware.iso", "")
    workname = workname.replace("-efi.iso", "")
    workname = workname.replace("-linux.iso", "")
    workname = workname.replace("-windows.iso", "")
    ver2 = util2digit(splitbydot[0],splitbydot[1])
    ver3 = util3digit(splitbydot[0],splitbydot[1],workname)
    filepath = filepath5(prodname,imagecode,ver2,ver3,imagecode2)
    filemove (filepath, filename)
