#!/usr/bin/python
# -*- coding: utf-8 -*-

# Futures

# Generic/Built-in
import argparse
import getopt
import hashlib
import json
import os
import re
import shutil
import sys
import logging
# Other Libs

# Owned
from iosutils     import *
from ios_nexus    import fileprocessornxos
from ios_voice    import fileprocessorvoice
from ios_security import fileprocessorsecurity
from ios_iosxe    import fileprocessor_iosxe
from ios_iosxr    import fileprocessor_iosxr
from ios_servers  import file_proc_servers
from ios_ios      import fileprocessorios
from ios_wireless import fileprocessor_wireless

#Credits
__author__ = ""
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = ""

def setup_logging(debug: bool):
    """Configure logging for the whole project."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
    )

def is_wireless_file(name: str) -> bool:
    logging.debug("Sub:    is_wireless_file")
    """
    Detects wireless/Cisco AP related images or upgrade tools
    and processes them.
    """
    wireless_files = {
        "AP350-Cisco-IOS-Upgrade-Image-v2.img",
        "AP1200-Cisco-IOS-Upgrade-Image-v3.img",
        "Aironet-AP-Cisco-IOS-Conversion-Tool-v2.1.exe",
        "webauth_bundle-1.0.2.zip"
    }

    wireless_prefixes = (
        "c1100", "AIR", "SWISMK9", "SWLC3750K9", "AIR_CTVM_LARGE-K9",
        "AIR_CTVM-K9", "AIR_CTVM", "MFG_CTVM", "AP_BUNDLE_CTVM",
        "AP_BUNDLE", "WCS-STANDARD-K9", "ISR-AP1100AC", "AS_7500",
        "CiscoAironet-AP-to-LWAPP-Upgrade-Tool"
    )

    wireless_exe_prefixes = ("BR350", "WGB350")

    if (
        name in wireless_files
        or name.startswith(wireless_prefixes)
        or any(name.startswith(prefix) and name.endswith("exe") for prefix in wireless_exe_prefixes)
    ):
        fileprocessor_wireless(name)
        return True

    return False

def toplevel(filename):
    src = filename
    names = os.listdir(src)
    os.chdir(src)
    
    logging.debug("Module: iossort")
    logging.debug("Sub:    toplevel")

    for name in names:
        if os.path.isdir(name):
            continue
        logging.info(f"{name}")

        splitbydot = name.split(".")
        splitbydash = name.split("-")
        splitbydashsub = splitbydot[0].split("-")

        thisstring = splitbydot.pop()
        splitbydot.append(thisstring)

        if (
            name == "Thumbs.db" or
            name.endswith("DS_Store") or
            name.endswith("hash") or
            name.endswith("part") or
            name.endswith("crdownload")
        ):
            continue
        elif name == "cat9k_fpga_upgrade_utility.pdf":
            fileprocessor_iosxe(name)
        elif name == "Exp_V3_11_Release_Note.pdf":
            fileprocessorios(name)
        elif (
            name == "C9100-ME-BetaGuide-v6.pdf" or
            name == "C9100-ME-EFT-Beta Guide.pdf"
            ):
            prodname = product("C9800-AP")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)
        elif (
            name in [
                "ucsm_object_docs.zip",
                "UCSPE 3.1(2e) 6248 1340 export.txt",
                "export_6248_ch1_b200m5.xml",
                "swift_stack_3260_cfg_export.xml",
                "export_6248_ch1_b200m5.xml.txt",
                "swift_stack_3260_cfg_export.xml.txt",
                "ucspe_6296_chassis1_export.xml.txt",
                "ucspe_6454_chassis1_export.xml.txt"
                ] or
            "Cisco UCS Platform Emulator" in name and name.endswith("pdf") or
            "Cisco_UCS_Platform_Emulator" in name and name.endswith("pdf") or
            "UCSPE" in name and name.endswith("pdf") or 
            name.startswith("UCSPE") or
            name.startswith("UCSM") and name.endswith("stripped-firmware.zip") or
            name.startswith("Cisco_UCS_Platform_Emulator_") or
            name.startswith("cimc_emulator-") or
            name.startswith("c220-m4-emu-cimc.") or
            name.startswith("c240-m4-emu-cimc.") or
            name.startswith("c460-m4-emu-cimc.")
            ):
            ucspe (name)
        elif name.endswith("pdf"):
            continue

        elif (
            name == "Upgrade instructions.txt" or 
            name == "ucd-update.tar" or 
            name == "nuova-or-dplug-mzg.6.0.2.N2.7.bin"
        ):
            prodname = product("n5000")
            imagecode = imagelookup ("specialbuildfwupgrade")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
                "cat9k.16121.0911.bin",
                "cat9k.16121_au.bin",
                "cat9k_iosxe.V171_1S_TES2.SPA.bin",
                "cat9k_bidir_updated.bin",
                "cat9k_fraport_bidir.bin",
                "cat9k_iosxe.V1611_1S_ES4.SPA.bin",
                "cat9k_iosxe.16.12-xFSU-eft1.bin",
                "cat9k_iosxe.16.12-xFSU-eft2.bin",
                "cat9k_iosxe.16.12-xFSU-eft3.bin",
                "cat9k_private_image_802.3bt.bin",
                "cat9k_iosxe.BLD_V171_EFT-1.SSA.bin",
                "cat9k_iosxe.BLD_V171_EFT-2.SSA.bin",
                "cat9k_iosxe.16.09.01.CSCvk69552.SPA.smu.bin",
                "cat9k_iosxe.16.09.01.CSCvk69552.SPA.smu.txt",
                "cat9k_iosxe.16.09.01.CSCvk69552.txt"
                ] or
            name.startswith("cat9k") and "THROTTLE_LATEST" in name or
            name.startswith("cat9k") and "prd" in name or
            name.startswith("cat9k") and "eft" in name or
            name.startswith("cat9k") and "SSA" in name
        ):
            prodname = product("cat9k")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name.startswith("csr1000v") and "eft" in name or
            name.startswith("csr1000v") and "prd" in name
        ):
            prodname = product("csr1000v")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "sf-linux-1017.SSA"
        ):
            prodname = product("cat9k")
            imagecode = imagelookup ("hdiag")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "s2t54-adventerprisek9-mz.SSA"
        ):
            prodname = product("s2t54")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "s72033-adventerprisek9_wan_dbg-mz.CSCsv69594_sxf"
        ):
            prodname = product("s72033")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "c2600-p-mz.991126"
        ):
            prodname = product("c2600")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "c3620-i-mz.bin"
        ):
            prodname = product("c3620")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "c3620-i-mz.bin"
        ):
            prodname = product("c3620")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "c5350-boot-mz.12-1.bin"
        ):
            prodname = product("c5350")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "c5800-p4scgen-3101m-mz.sit"
        ):
            prodname = product("c5800")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("c7200-i12o3s-mz.2005-04-14.BROILER2_BLUEWIN_EFT_REL") or 
        name.startswith("c7200-i12s-mz.2005-04-14.BROILER2_BLUEWIN_EFT_REL") or 
        name.startswith("c7200-i12o3s-mz.2005-07-16.BSNOP4_DAILY_BUILD") or 
        name.startswith("c7200-i12o3s-mz.2005-07-15.BSNOP4_DAILY_BUILD") or 
        name.startswith("c7200-p-mz_ccassar-conn_isp-l3vpn") or 
        name == "c7200-js-mz" or 
        name == "c7200-js-mz.symbols.gz" or 
        name == "c7200-p-mz" or 
        name == "c7200-is-mz.123-3.20040113"
        ):
            prodname = product ("c7200")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("c7301-i12o3s-mz.2005-04-13.BROILER2_BLUEWIN_EFT_REL") or 
        name.startswith("c7301-i12s-mz.2005-04-13.BROILER2_BLUEWIN_EFT_REL") or 
        name.startswith("c7301-i12o3s-mz.2005-07-15.BSNOP4_DAILY_BUILD") or 
        name.startswith("c7301-i12o3s-mz.2005-07-16.BSNOP4_DAILY_BUILD")
        ):
            prodname = product ("c7301")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("c2800nm-ipvoice-mz.v124_9")
        ):
            prodname = product ("c2800nm")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c3640-js-mz" or 
        name == "c3640-js-mz.symbols.gz"
        ):
            prodname = product ("c3640")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c800-nsy6-mw.120-4.0.2.T1" or 
        name == "c800-g3x-mw.120-3.4.T"
        ):
            prodname = product ("c800")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "rsp-jsv-mz.infonet.uk35278" or 
        name == "rsp-pv-mz_ccassar-conn_isp-l3vpn" or 
        name == "rsp-jsv-mz" or 
        name == "rsp-jsv-mz.symbols.gz"
        ):
            prodname = product ("rsp")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c7300-js-mz.debug"
        ):
            prodname = product ("c7300")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c3745.CSCse01847"
        ):
            prodname = product ("c3745")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("C9800-40-") and "THROTTLE" in name
        ):
            prodname = product ("C9800-40")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("C9800-80-") and "THROTTLE" in name
        ):
            prodname = product ("C9800-80")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("C9800-L-") and "THROTTLE" in name
        ):
            prodname = product ("C9800-L")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("C9800-L-") and "THROTTLE" in name
        ):
            prodname = product ("C9800-L")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
                "C9800-CL-universalk9.2019-04-26_10.55_bachidam.0.CSCvo94596.SSA.apdp.bin",
                "C9800-CL-universalk9.2019-05-13_15.09_sisharm2.SSA.bin",
                "C9800-CL-universalk9.2019-05-16_19.27_sisharm2.SSA.bin",
                "C9800-CL-universalk9.2019-07-09_07.29_ghalwasi.SSA.bin",
                "C9800-CL-universalk9.2019-08-07_14.47_raghasin.SSA.bin",
                "C9800-CL-universalk9.2019-09-16_14.42_gbks.SSA.bin"
                ] or
        name.startswith("C9800-CL-") and "THROTTLE" in name or
        name.startswith("C9800-CL-") and "eft" in name or
        name.startswith("C9800-CL-") and "prd" in name or
        name.startswith("C9800-CL-") and "SSA" in name
        ):
            prodname = product ("C9800-CL")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("C9800-SW-") and "THROTTLE" in name or
        name == "C9800-SW-iosxe-wlc.V171_1S_TES2.SPA.bin"
        ):
            prodname = product ("C9800-SW")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c1100-universalk9.V16_12_0_136.SSA.bin" or
        name.startswith("c1100-") and "prd" in name or
        name.startswith("c1100-") and "eft" in name
        ):
            prodname = product ("c1100router")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "asr1000rp1-adventerprisek9.BLD_V122_33_XNC_ASR_RLS3_THROTTLE_LATEST_20090513_080032.bin" or
        name == "asr1000rp1-advipservicesk9.V152_1_S1_CSCTR15153_3.bin"
        ):
            prodname = product ("asr1000rp1")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "asr1000rpx86-universalk9.V1612_1_CVE_2019_1649.SPA.bin"
        ):
            prodname = product ("asr1000rpx86")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name == "c180x-advipservicesk9-mz.V124_15_T1-CSCsk94464-ES.bin"
        ):
            prodname = product ("c180x")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
                "c3900e-universalk9-mz.SSA.152-4.M.CSCtw93694.bin",
                "c3900e-universalk9-mz.SSA.152-4.M.CSCtw93694_Feb16.bin",
                "c3900e-universalk9-mz.SSA.154-20160808061644.skaliath-NIGHTLY_V154_3_M_THROTTLE_201608041309-104-CSCva77149.bin",
                "c3900e-universalk9-mz.SSA.154-20160819103204.skaliath-PRE_RELEASE_FC1_V154_3_M6-105-CSCva77149.bin"
                ]
        ):
            prodname = product ("c3900")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "n7000-s1-epld.5.2.0.266.gimg" or
            name.startswith("dino-lisp")
        ):
            prodname = product ("n7000")
            imagecode = imagelookup ("specialbuildlisp")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "C9100-universalk9_me.BLD_V1612_THROTTLE_LATEST_20190619_023732.zip" or
            name == "C9100_ME_Site_Survey.zip"
        ):
            prodname = product ("C9800-AP")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name.startswith("C9800-universalk9_wlc") and "THROTTLE_LATEST" in name or
            name.startswith("C9800-universalk9_wlc") and "SSA" in name or
            name.startswith("C9800-universalk9_wlc") and "prd" in name or
            name == "coral-coral" and "THROTTLE_LATEST" in name
        ):
            prodname = product ("C9800-AP")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "PI-Upgrade-35x_36x_to_3.7.0.0.124.tar.gz" or
            name == "PI-Upgrade-3.5_to_3.6.0.0.129.tar.gz" or
            name == "PI-Upgrade-3.5_to_3.6.0.0.172.tar.gz" or
            name == "PI-Upgrade-3.5_to_3.7.0.0.45.tar.gz" or
            name == "PI-Upgrade-3.X_to_3.5.0.0.550.tar.gz" or
            name == "PI-Upgrade-35x_36x_to_3.7.0.0.124.tar.gz" or
            name == "PI-Upgrade-35x_36x_to_3.7.0.0.88.tar.gz" or
            name == "PI-VA-3.7.0.0.88-flex.ova"
        ):
            prodname = product ("cpi")
            imagecode = imagelookup ("specialbuild")
            utilssinglemove (name,prodname,imagecode)

        elif (
        ".cv50." in name and name.endswith(".zip")  or
        ".cv50." in name and name.endswith(".readme")  or
        ".cv53." in name and name.endswith(".zip")  or
        ".cv53." in name and name.endswith(".readme")  or
        ".cv61." in name and name.endswith(".zip")  or
        ".cv61." in name and name.endswith(".readme")  or
        "nmidb." in name and name.endswith(".zip")  or
        "nmidb." in name and name.endswith(".readme")  or
        "cvw6.1" in name and name.endswith(".tar")  or
        "cvw6.1" in name and name.endswith(".zip")  or
        ".RME43." in name and name.endswith(".zip") or
        name in [
            "Mwr1900.zip",
            "CVCrossLaunch.zip",
            "psumeta_cwcv6_1_5.xml",
            "Cat6000IOS.zip"
        ]
        ):
            prodname = product ("cworks")
            imagecode = imagelookup ("rme")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "VMS_2_3_DST_Patch_Windows_K9.tar"
        ):
            prodname = product ("cworks")
            imagecode = imagelookup ("patch")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name == "Patch-CSCsc85405.tar.gz"
        ):
            prodname = product ("perfigocca")
            imagecode = imagelookup ("patch")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
                "c3750-dmon-mz.122-25r.SEC",
                "c3750-dmon-mz-122-25r.SEE4",
                ]
        ):
            prodname = product ("c3750")
            imagecode = imagelookup ("hdiag")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
                "AnyConnect-CSA.zip",
                "CSD-for-CSA-updates.zip",
                ]
        ):
            prodname = product ("csa")
            imagecode = imagelookup ("export")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("i86bi") or
        name.startswith("I86BI")
        ):
            prodname = product ("iou")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("vios") or
        name.startswith("vIOS")
        ):
            prodname = product("vios")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("ata") or
        name.startswith("cmterm") or
        name.startswith("vgc-main") or
        name.startswith("CME") or
        name.startswith("cme")
        ):
            fileprocessorvoice(name)

        elif (
        "tsjspgen" in name or
        "tpcgen" in name or
        "tpgen" in name or
        "tpcgenx" in name or
        "tscgen" in name or
        "tscgenx" in name or
        "tipv6" in name
        ):
            prodname = product ("routers")
            imagecode = imagelookup ("pagent")
            utilssinglemove (name,prodname,imagecode)


        elif (
            name in [
            "np.0.8.11.1.spe",
            "np.0.8.11.2.spe",
            "np.0.10.8.0.spe",
            "np.6.106.spe",
            "np.6.93.spe",
            "np.7.16.spe",
            "np.7.9.spe",
            "np.8.8.1.spe",
            "np.spe"
            ]
        ):
            prodname = product ("mica-modem")
            imagecode = imagelookup ("np")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("adsl_alc")
        ):
            prodname = product ("ISRG1GENERIC")
            imagecode = imagelookup ("DSLFIRMWARE")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("8705_") or
        name.startswith("8775_") or
        name.startswith("8790_")
        ):
            prodname = product ("ISRG1GENERIC")
            imagecode = imagelookup ("HWIC3GGSM")
            utilssinglemove (name,prodname,imagecode)

        elif name.startswith("vcw-vfc-mz"):
            prodname = product ("c5350")
            imagecode = imagelookup (splitbydot[0])
            utilssinglemove (name,prodname,imagecode)

        elif name.startswith("c3600-2600-analog-fw"):
            prodname = product ("branchmodules")
            imagecode = imagelookup ("analogmodem")
            utilssinglemove (name,prodname,imagecode)

#Process ROMMON Files
        elif is_rommon_file(name):
            fileprocessorrommon(name)

#Process Nexus Files
        elif is_nxos_file(name):
            fileprocessornxos(name)

#Process Security Files
        elif is_iosxe_file(name):
            fileprocessor_iosxe(name)

#Process Security Files
        elif is_security_file(name):
            fileprocessorsecurity(name)

#Process Server Files
        elif is_server_file(name):
            file_proc_servers(name)

#Process IOS XR Files
        elif is_iosxr_file(name):
            fileprocessor_iosxr(name)

#Process Classical IOS Files
        elif is_ios_file(name):
            fileprocessorios(name)

#Process CatOS Files
        elif is_cat_file(name):
            continue  # already handled inside helper

#Process Wireless Files
        elif is_wireless_file(name):
            pass  # already handled inside helper

        elif (
        name.startswith("CUMC")
        ):
            continue

        elif (
            name in [
            "Cisco_usbconsole_driver.zip",
            "Cisco_usbconsole_driver_3_1.zip",
            "asr-9xx_usbconsole_drivers.zip"
            ]
        ):
            prodname = product ("usbconsole")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("8705_") or
        name.startswith("8775_") or
        name.startswith("8790_")
        ):
            continue

        elif (
        name.startswith("vios")
        ):
            continue

        elif (
        name == "p1021_c800.V1.1.0.bin" or
        name == "PRL_60779.prl"
        ):
            continue

        elif (
        name == "all-in-one-VM-1.2.1-194.ova" or
        name == "all-in-one-VM-1.3.0.181.ova"
        ):
            prodname = product ("onepk")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("cat1900")
        ):
            prodname = product ("cat1900")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("cat2800") or
        name.startswith("cat2820")
        ):
            prodname = product ("cat2800")
            utilssingleprodname (name,prodname)

        elif (
        name == "README.SWT"
        ):
            prodname = product ("cat1600")
            utilssingleprodname (name,prodname)

        elif (
        name == "epsboot.ima"
        ):
            prodname = product ("cat3000")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("c6svc-mp")
        ):
            fileprocessorios (name)

        elif (
        name.startswith("CPO") and name.endswith("zip") or
        name.startswith("MIBS") or
        name.startswith("SDM-V25.zip") or
        name.startswith("c6svc-nam") or
        name.startswith("ciscocm") or
        name.startswith("copfiles_iOS96.zip") or
        name.startswith("s52000tc") or
        name.startswith("sdmv10.zip") or
        name.startswith("uccx")
        ):
            continue

        elif (
        name.startswith("axsm_") or
        name.startswith("axsmxg_") or
        name.startswith("pxm45_") or
        name == "mgx8880rel5600mib.tar"
        ):
            #MGX8850
            continue

        elif (
        name.startswith("Sx500") or
        name.startswith("Sx350") or
        name.startswith("Sx300") or
        name.startswith("Sx250") or
        name.startswith("Sx220") or
        name.startswith("Sx200") or
        name.startswith("MIBs_Sx500") or
        name.startswith("SPA30x_SPA50x_") or
        name.startswith("AP541N-K9")
        ):
            prodname = product ("smallbusiness")
            utilssingleprodname (name,prodname)

        elif (
        name.startswith("c1200-k9") or
        name.startswith("c1200-rcvk9w8") or
        name.startswith("c1100-k9") or
        name.startswith("c1100-rcvk9w8")
        ):
            fileprocessorios (name)

        elif (
        name.startswith("c1200") or
        name.startswith("dmp") or
        name.startswith("nmp")
        ):
            prodname = product ("cat1200")
            utilssingleprodname (name,prodname)
            
        elif (
            name.startswith ("c627") or
            name.startswith ("c633") or
            name.startswith ("c673") or
            name.startswith ("c675") or
            name.startswith ("c676") or
            name.startswith ("c677") or
            name.startswith ("c677i") or
            name.startswith ("c678cap") or
            name.startswith ("c678dmt") or
            name.startswith ("nsrouter")
        ):
            prodname = product ("c600")
            utilssingleprodname (name,prodname)

        elif (
        name == "c3750-dmon-mz-122-25r.SEE4" or
        name == "c3750-dmon-mz.122-25r.SEC"
        ):
            prodname = product ("c3750")
            imagecode = imagelookup ("hdiag")
            utilssinglemove (name,prodname,imagecode)

        elif (
            name in [
            "17_1_1t_mib.zip",
            "17_2_1_mib.zip",
            "17_2_1a_mib.zip",
            "mibs_1610.zip",
            "mibs_1611.zip",
            "mibs_16121.zip",
            "mibs_16121s.zip",
            "mibs_16121t.zip",
            "mibs_16122s.zip",
            "mibs_16123.zip",
            "mibs_16124a.zip",
            "mibs_16125.zip"
            ] or
        name.startswith ("Standard-MIBS-Cisco_")
        ):
            prodname = product ("wireless")
            imagecode = imagelookup ("mibs")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith ("m9000") or
        name.startswith ("m9100") or
        name.startswith ("m9200") or
        name.startswith ("m9250") or
        name.startswith ("m9300") or
        name.startswith ("m9500") or
        name.startswith ("m9700")
        ):
            fileprocessornxos(name)

        elif (
        name == "CPUpdate.xml" or
        name.startswith("Cisco-config-pro") or
        name.startswith("cisco-config-pro")
        ):
            prodname = product ("ccp")
            utilssingleprodname (name,prodname)

        elif (
        name == "cna-1_0-windows-k9-installer.1-0-1a.exe" or
        name.startswith("cna-mac-k9") or
        name.startswith("cna-windows-k9")
        ):
            prodname = product ("cna")
            utilssingleprodname (name,prodname)

#        elif (
#        name == "SDM-V25.zip"
#        ):
#            continue
#            prodname = product ("ccp")
#            utilssingleprodname (name,prodname)

        elif (
        name.startswith("c1000-cwml") or
        name.startswith("c2960-cwml") or
        name.startswith("c2960c405-cwml") or
        name.startswith("c2960cx-cwml") or
        name.startswith("c2960l-cwml") or
        name.startswith("c2960x-cwml") or
        name.startswith("c3560cx-cwml") or 
        name.startswith("cdb-cwml")
        ):
            prodname = product ("ccpc")
            utilssingleprodname (name,prodname)

        elif splitbydot[0] == "c675" or splitbydot[1] == "c675":
            filepath = "Other"
            filemove (filepath, name)

        elif splitbydot[0] == "c678cap" or splitbydot[1] == "c678cap":
            filepath = "Other"
            filemove (filepath, name)

        elif splitbydot[0] == "c678dmt" or splitbydot[1] == "c678dmt":
            filepath = "Other"
            filemove (filepath, name)

        elif splitbydot[0] == "spa-fpd":
            thistemp = splitbydot[0]
            splitbydashsub = thistemp.split("-")
            imagecode = imagelookup (splitbydashsub[1])
            prodname = product (splitbydashsub[0])
            fileprocessorios (name)

        elif splitbydot[0] == "dsc-c5800-mz":
            imagecode = imagelookup (splitbydash[0])
            prodname = product (splitbydash[1])
            fileprocessorios (name)

        elif splitbydot[0] == "c10k-fpd-pkg":
            prodname = product ("c10k")
            imagecode = imagelookup (splitbydash[1])
            fileprocessorios (name)

        elif (
        name.startswith("pp-adv")
        ):
            nbar (name)

        elif (
        name.startswith("xcpa")
        ):
            nbar (name)

        elif (
        name.startswith("s6523-mp001")
        ):
            prodname = product ("s6523")
            imagecode = imagelookup ("mpatch")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("s3223-mp001")
        ):
            prodname = product ("s3223")
            imagecode = imagelookup ("mpatch")
            utilssinglemove (name,prodname,imagecode)

        elif (
        name.startswith("s72033-mp001")
        ):
            prodname = product ("s72033")
            imagecode = imagelookup ("mpatch")
            utilssinglemove (name,prodname,imagecode)

        elif name.startswith("cat4500e"):
            if "SPA" in name:
                fileprocessor_iosxe(name)
            else:
                fileprocessorios (name)

        elif name.startswith("mre_workflow_signed"):
            continue

        else:
            fileprocessorios (name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to sort", required=True)
    parser.add_argument("-d1", "--debug1", help="Enable debug logging", action="store_true", required=False)

    args = parser.parse_args()

    setup_logging(args.debug1)

    toplevel(args.directory)
