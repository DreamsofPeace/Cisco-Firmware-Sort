"""
Refactored ios_iosxe file processor.

Major changes:
- Grouped repetitive startswith/equals patterns into tuples and helper functions.
- Introduced small helper wrappers to reduce duplicate code paths.
- Added type hints and docstrings.
- Preserved original logic and external calls to iosutils functions.
"""

from typing import Tuple
import logging

# Import iosutils functions into current namespace.
# Original code imported iosutils then exported non-underscore attributes to globals().
# For readability we import everything from iosutils (keeps same function names as before).
# NOTE: keep the iosutils module on PYTHONPATH.
from iosutils import *  # noqa: F401,F403

_LOG = logging.getLogger(__name__)

def split_filename(filename: str, delimiter: str = ".") -> list[str]:
    """Split filename by the given delimiter and return the resulting list."""
    return filename.split(delimiter)

def _do_single_move(filename: str, prod_key: str, image_key: str) -> None:
    """Helper wrapper for the common utilssinglemove usage."""
    prodname = product(prod_key)
    imagecode = imagelookup(image_key)
    utilssinglemove(filename, prodname, imagecode)

def _do_single_prodname(filename: str, prod_key: str) -> None:
    """Helper wrapper for the common utilssingleprodname usage."""
    prodname = product(prod_key)
    utilssingleprodname(filename, prodname)

def fileprocessor_iosxe(filename: str) -> None:
    """Main file processing entry point for IOS XE artifacts."""
    _LOG.debug("Module: ios_iosxe")
    _LOG.debug("Sub:    fileprocessor_iosxe")

    """
    Determines which product/image a given filename belongs to.
    Returns a dict with productcode and imagecode.
    """
    firmware_matching = [
        #ASR 1000
        {'prefix': "asr1000-universalk9.",               'imagecode': "universalk9",          'productcode': "asr1000",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "asr1000",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9_noli.",          'imagecode': "universalk9_noli",     'productcode': "asr1000",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9_npe_noli.",      'imagecode': "universalk9_npe_noli", 'productcode': "asr1000",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8200/8300
        {'prefix': "c8000be-universalk9.",               'imagecode': "universalk9",          'productcode': "c8000be",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000be-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "c8000be",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8500
        {'prefix': "c8000aep-universalk9.",              'imagecode': "universalk9",          'productcode': "c8000aep",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_npe.",          'imagecode': "universalk9_npe",      'productcode': "c8000aep",    'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8500L
        {'prefix': "c8000aes-universalk9.",              'imagecode': "universalk9",          'productcode': "c8000aes",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aes-universalk9_npe.",          'imagecode': "universalk9_npe",      'productcode': "c8000aes",    'split_type': "dot", 'suffix': ".SPA.bin"},
        #IR 1101
        {'prefix': "ir1101-universalk9.",                'imagecode': "universalk9",          'productcode': "ir1101",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ir1101-universalk9_npe.",            'imagecode': "universalk9_npe",      'productcode': "ir1101",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #1100 ISR
        {'prefix': "c1100-universalk9.",                 'imagecode': "universalk9",          'productcode': "c1100router", 'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9_npe.",             'imagecode': "universalk9_npe",      'productcode': "c1100router", 'split_type': "dot", 'suffix': ".SPA.bin"},
        #1100X ISR
        {'prefix': "isr1100be-universalk9.",             'imagecode': "universalk9",          'productcode': "isr1100be",   'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr1100be-universalk9_npe.",         'imagecode': "universalk9_npe",      'productcode': "isr1100be",   'split_type': "dot", 'suffix': ".SPA.bin"},
        #4200 ISR
        {'prefix': "isr4200-universalk9_ias.",           'imagecode': "universalk9",          'productcode': "isr4200",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4200-universalk9_ias_npe.",       'imagecode': "universalk9_npe",      'productcode': "isr4200",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #4300 ISR
        {'prefix': "isr4300-universalk9.",               'imagecode': "universalk9",          'productcode': "isr4300",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4300-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "isr4300",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #4400 ISR
        {'prefix': "isr4400-universalk9.",               'imagecode': "universalk9",          'productcode': "isr4400",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4400-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "isr4400",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #4400v2 ISR
        {'prefix': "isr4400v2-universalk9.",             'imagecode': "universalk9",          'productcode': "isr4400v2",   'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4400v2-universalk9_npe.",         'imagecode': "universalk9_npe",      'productcode': "isr4400v2",   'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8000 Virtual
        {'prefix': "c8000v-universalk9.",                'imagecode': "install",              'productcode': "c8000v",      'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "c8000v-universalk9.",                'imagecode': "install",              'productcode': "c8000v",      'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "c8000v-universalk9_vga.",            'imagecode': "install",              'productcode': "c8000v",      'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "c8000v-universalk9_vga.",            'imagecode': "install",              'productcode': "c8000v",      'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "c8000v-universalk9_16G_serial_efi.", 'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_vga.",        'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_vga_efi.",    'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_serial.",      'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_serial_efi.",  'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_vga.",         'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_vga_efi.",     'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_serial.",     'imagecode': "universal_kvm",        'productcode': "c8000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_serial.",     'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_serial_efi.", 'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_vga.",        'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_vga_efi.",    'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_serial.",      'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_serial_efi.",  'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_vga.",         'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_vga_efi.",     'imagecode': "universal_nfvis",      'productcode': "c8000v",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9.",                'imagecode': "upgrade",              'productcode': "c8000v",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #CSR 1000V
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install",              'productcode': "csr1000v",      'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "upgrade",              'productcode': "csr1000v",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",          'productcode': "csr1000v",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",          'productcode': "csr1000v",      'split_type': "dot", 'suffix': ".efi.qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",          'productcode': "csr1000v",      'split_type': "dot", 'suffix': "-serial.efi.qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",          'productcode': "csr1000v",      'split_type': "dot", 'suffix': "-serial.qcow2"},
        #1100 Terminal Services Gateway
        {'prefix': "c1100tg-universalk9.",               'imagecode': "universalk9",          'productcode': "c1100tg",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "c1100tg-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "c1100tg",       'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 9800 Virtual Controller
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install",              'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install",              'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install-kvm",          'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install-nfvis",        'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "C9800-CL-universalk9_esxi.",         'imagecode': "install-esxi" ,        'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9_nfvis.",        'imagecode': "install-nfvis",        'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9_kvm.",          'imagecode': "install-kvm",          'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "upgrade",              'productcode': "C9800-CL",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9800 Controllers
        {'prefix': "C9800-40-universalk9_wlc.",          'imagecode': "system",               'productcode': "C9800-40",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-80-universalk9_wlc.",          'imagecode': "system",               'productcode': "C9800-80",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "CW9800H-wlc-universalk9.",           'imagecode': "system",               'productcode': "CW9800H",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "CW9800M-wlc-universalk9.",           'imagecode': "system",               'productcode': "CW9800M",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-L-universalk9_wlc.",           'imagecode': "system",               'productcode': "C9800-L",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-SW-iosxe-wlc.",                'imagecode': "system",               'productcode': "C9800-L",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",               'productcode': "C9800-AP",      'split_type': "dot", 'suffix': ".zip"},
        #Catalyst Cellular Gateway
        {'prefix': "cg-ipservices-",                     'imagecode': "system",               'productcode': "cg",            'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cg-ipservices.",                     'imagecode': "system",               'productcode': "cg",            'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst Wireless Gateway
        {'prefix': "ccg110-universalk9.",                'imagecode': "system",               'productcode': "ccg110",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #Voice Gateway
        {'prefix': "vg400-universalk9.",                 'imagecode': "universalk9",          'productcode': "vg400",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg420-universalk9.",                 'imagecode': "universalk9",          'productcode': "vg420",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg450-universalk9.",                 'imagecode': "universalk9",          'productcode': "vg450",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 3850/3650
        {'prefix': "cat3k_caa-universalk9.",             'imagecode': "universalk9",          'productcode': "cat3k_caa",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat3k_caa-universalk9ldpe.",         'imagecode': "universalk9_npe",      'productcode': "cat3k_caa",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat3k_caa-universalk9.SPA.",         'imagecode': "universalk9",          'productcode': "cat3k_caa",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat3k_caa-universalk9ldpe.SPA.",     'imagecode': "universalk9ldpe",      'productcode': "cat3k_caa",     'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 4500E
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",            'productcode': "cat4500e",      'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",          'productcode': "cat4500e",      'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 9000
        {'prefix': "cat9k_iosxe.",                       'imagecode': "universalk9",          'productcode': "cat9k",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat9k_iosxe_npe.",                   'imagecode': "universalk9_npe",      'productcode': "cat9k",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9200
        {'prefix': "cat9k_lite_iosxe.",                  'imagecode': "universalk9",          'productcode': "cat9k_lite",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat9k_lite_iosxe_npe.",              'imagecode': "universalk9_npe",      'productcode': "cat9k_lite",    'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9350
        {'prefix': "cisco9k_iosxe.",                     'imagecode': "universalk9",          'productcode': "cisco9k_iosxe", 'split_type': "dot", 'suffix': ".SPA.bin"},
        #NCS 520
        {'prefix': "ncs520-universalk9_npe.",            'imagecode': "universalk9_npe",      'productcode': "ncs520",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #8100 Secure Router Gen2
        {'prefix': "c81g2be-universalk9.",               'imagecode': "universalk9",          'productcode': "c81g2be",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c81g2be-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "c81g2be",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #8200-8300 Secure Router Gen2
        {'prefix': "c8kg2be-universalk9.",               'imagecode': "universalk9",          'productcode': "c81g2be",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8kg2be-universalk9_npe.",           'imagecode': "universalk9_npe",      'productcode': "c81g2be",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #8400 Secure Router Gen2
        {'prefix': "c84g2aes-universalk9.",              'imagecode': "universalk9",          'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_npe.",          'imagecode': "universalk9_npe",      'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_noli.",         'imagecode': "universalk9_noli",     'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_npe_noli.",     'imagecode': "universalk9_npe_noli", 'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #8500 Secure Router Gen2
        {'prefix': "c8000aep-universalk9.",              'imagecode': "universalk9",          'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_npe.",          'imagecode': "universalk9_npe",      'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_noli.",         'imagecode': "universalk9_noli",     'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_npe_noli.",     'imagecode': "universalk9_npe_noli", 'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #IE 9K
        {'prefix': "ie9k_iosxe.",                        'imagecode': "universalk9",          'productcode': "ie9k",           'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ie9k_iosxe_npe",                     'imagecode': "universalk9_npe",      'productcode': "ie9k",           'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 4500e
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",            'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",            'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        #Catalyst 4500e Sup8/9
        {'prefix': "cat4500es8-universal.SPA.",            'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universal.SPA.",            'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500es8-universalk9.SPA.",          'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universalk9.SPA.",          'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500es8-universalk9npe.",           'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universalk9npe.",           'imagecode': "universal",          'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
    ]

    filename_exact = [
        #Catalyst 9xxx
        {'filename': "cat9k_iosxe.16.00.00fpgautility.SPA.bin",                                                    'imagecode': "fpga",          'productcode': "cat9k"},
        {'filename': "cat9k_fpga_upgrade_utility.pdf",                                                             'imagecode': "fpga",          'productcode': "cat9k"},
        #Catalyst ASR 1xxx
        {'filename': "asr903rsp1-universalk9_npe.V154_3_S3_SR637267017_1.bin",                                     'imagecode': "specialbuild",  'productcode': "asr903rsp1"},
        {'filename': "asr1000rp1-advipservicesk9.V152_1_S1_CSCTR15153_3.bin",                                      'imagecode': "specialbuild",  'productcode': "asr1000rp1"},
        {'filename': "asr1000rp1-adventerprisek9.BLD_V122_33_XNC_ASR_RLS3_THROTTLE_LATEST_20090513_080032.bin",    'imagecode': "specialbuild",  'productcode': "asr1000rp1"},
        {'filename': "sr1000rpx86-universalk9.V1612_1_CVE_2019_1649.SPA.bin",                                      'imagecode': "fpga",          'productcode': "asr1000rpx86"},
    ]

    filename_single_move = [
        #1100 ISR
        {'prefix': "C1100-rommon-",                  'imagecode': "rommon",        'productcode': "c1100router"},
        {'prefix': "isr1100-bootloader.",            'imagecode': "rommon",        'productcode': "c1100router"},
        #8200
        {'prefix': "C8000-2N2S",                     'imagecode': "rommon",        'productcode': "c8000be"},
        {'prefix': "C8000-1N",                       'imagecode': "rommon",        'productcode': "c8000be"},
        #Catalyst 3850/3650
        {'prefix': "CAT3650_WEBAUTH_BUNDLE",         'imagecode': "webauth",       'productcode': "cat3k_caa"},
        {'prefix': "CAT3850_WEBAUTH_BUNDLE",         'imagecode': "webauth",       'productcode': "cat3k_caa"},
        #ISR 4200
        {'prefix': "isr4200-firmware_nim_xdsl",      'imagecode': "dslfirmware",   'productcode': "isr4200"},
        {'prefix': "isr4200_cpld_update",            'imagecode': "cpld_update",   'productcode': "isr4200"},
        #ISR 4300
        {'prefix': "nim_vab_phy_fw_",                'imagecode': "dslfirmware",   'productcode': "isr4300"},
        {'prefix': "nim_vab_phy_fw_",                'imagecode': "dslfirmware",   'productcode': "isr4300"},
        {'prefix': "isr4300-hw-programmables",       'imagecode': "hardware",      'productcode': "isr4300"},
        {'prefix': "isr4300_cpld_update",            'imagecode': "cpld_update",   'productcode': "isr4300"},
        #ISR 4400
        {'prefix': "isr-hw-programmables",           'imagecode': "hardware",      'productcode': "isr4400"},
        {'prefix': "isr4400-firmware_nim_xdsl",      'imagecode': "dslfirmware",   'productcode': "isr4400"},
        {'prefix': "isr4400_cpld_update",            'imagecode': "cpld_update",   'productcode': "isr4400"},
        #ISR 4400v2
        {'prefix': "isr4400v2-firmware_nim_xdsl",    'imagecode': "dslfirmware",   'productcode': "isr4400v2"},
        {'prefix': "isr4400v2_cpld_update",          'imagecode': "cpld_update",   'productcode': "isr4400v2"},
        {'prefix': "isr4400v2-hw-programmable",      'imagecode': "cpld_update",   'productcode': "isr4400v2"},
        #ASR1000RPX86
        {'prefix': "asr1000rpx86-hw-programmables",  'imagecode': "hardware",      'productcode': "asr1000rpx86"},
        #ASR1000
        {'prefix': "asr1000-hw-programmables",       'imagecode': "hardware",      'productcode': "asr1000"},
        {'prefix': "asr1002x-hw-programmables",      'imagecode': "hardware",      'productcode': "asr1000"},
        {'prefix': "ASR1K-fpga_prog",                'imagecode': "hardware",      'productcode': "asr1000"},
        #SD-WAN
        {'prefix': "appqoe-dre",                     'imagecode': "appqoe",        'productcode': "sdwan"},
    ]

    if filename.startswith("cat4500es8"):
        mdash = splitbydot[0].split("-")
        prodname = product (mdash[0])
        imagecode = imagelookup(mdash[1])
        fileproc_iosxe_3 (filename,prodname,imagecode)

    elif filename.startswith("ct5760"):
        mdash = splitbydot[0].split("-")
        prodname = product (mdash[0])
        imagecode = imagelookup(mdash[1])
        fileproc_iosxe_3 (filename,prodname,imagecode)





    elif filename.startswith("cat4500e"):
        prodname = product (splitbydash[0])
        mdash = splitbydot[0].split("-")
        imagecode = imagelookup(mdash[1])
        if (
        filename.startswith("cat4500e-universalk9") or 
        filename.startswith("cat4500e-universal") or 
        filename.startswith("cat4500e-universalk9_lite") or 
        filename.startswith("cat4500e-universal_lite")
        ):
            fileproc_iosxe_3 (filename,prodname,imagecode)
        else:
            fileproc_iosxe (filename,prodname,imagecode)

    elif (
        filename.startswith("C9800-") or 
        filename.startswith("CW9800H") or
        filename.startswith("CW9800M")
        ):
        fileproccontroller (filename)




def fileproc_iosxe_noimagecode (filename,prodname):
    logging.debug("Sub:    fileproc_iosxe_noimagecode")
    splitbydot = filename.split(".")
    splitbydot[3] = splitbydot[3].replace("-serial", "")
    splitbydot[3] = splitbydot[3].replace("-nfvis", "")
    splitbydot[3] = splitbydot[3].replace("-esxi", "")
    splitbydot[3] = splitbydot[3].replace("-kvm", "")
    #Checks to make sure that it is a regular firmware image, not a SMU
    if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
        iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4(prodname,"SMU",iosfull,splitbydot[4])
        filemove (filepath, filename)
    else:
        iosmain = util2digit(splitbydot[1],splitbydot[2])
        iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath3(prodname,iosmain,iosfull)
        filemove (filepath, filename)

def fileproc_iosxe_3 (filename,prodname,imagecode):
    logging.debug("Sub:    fileprocessor_iosxe")
    splitbydot = filename.split(".")
    if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
        imagecode2 = imagelookup("smu")
        iosmain = util2digit(splitbydot[1],splitbydot[2])
        iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath5(prodname,iosmain,iosfull,imagecode2,splitbydot[4])
        filemove (filepath, filename)
    else:
        iosmain = util2digit(splitbydot[2],splitbydot[3])
        iosfull = util3digit(splitbydot[2],splitbydot[3],splitbydot[4])
        filepath = filepath4(prodname,iosmain,iosfull,imagecode)
        filemove (filepath, filename)

def fileproc_iosxe (filename,prodname,imagecode):
    logging.debug("Sub:    fileproc_iosxe")
    splitbydot = filename.split(".")
    splitbydot[3] = splitbydot[3].replace("-serial", "")
    splitbydot[3] = splitbydot[3].replace("-nfvis", "")    
    splitbydot[3] = splitbydot[3].replace("-esxi", "")
    splitbydot[3] = splitbydot[3].replace("-kvm", "")
    #Checks to make sure that it is a regular firmware image, not a SMU
    if splitbydot[4].startswith("CSC") and splitbydot[6]  == "smu":
        imagecode2 = imagelookup("smu")
        iosmain = util2digit(splitbydot[1],splitbydot[2])
        iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath5(prodname,iosmain,iosfull,imagecode2,splitbydot[4])
        filemove (filepath, filename)
    else:
        iosmain = util2digit(splitbydot[1],splitbydot[2])
        iosfull = util3digit(splitbydot[1],splitbydot[2],splitbydot[3])
        filepath = filepath4(prodname,iosmain,iosfull,imagecode)
        filemove (filepath, filename)

def file_prepare_standard_iosxe (filename,prodname,imagecode,workname):
    logging.debug("Sub:    file_prepare_standard_iosxe")
    splitbydot = workname.split(".")
    if len(splitbydot) == 3:
        version_main = util2digit(splitbydot[0],splitbydot[1])
        version_full = util3digit(splitbydot[0],splitbydot[1],splitbydot[2])
        filepath = filepath4(prodname,version_main,version_full,imagecode)
        filemove (filepath, filename)
    