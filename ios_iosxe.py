import os
import logging
import iosutils
import re
from typing import Tuple
from iosutils import product,imagelookup,filepath

# Import all public functions from iosutils
for name in dir(iosutils):
    if not name.startswith("_"):
        globals()[name] = getattr(iosutils, name)
"""
Refactored ios_iosxe file processor.

Major changes:
- Grouped repetitive startswith/equals patterns into tuples and helper functions.
- Introduced small helper wrappers to reduce duplicate code paths.
- Added type hints and docstrings.
- Preserved original logic and external calls to iosutils functions.
"""

# Import iosutils functions into current namespace.
# Original code imported iosutils then exported non-underscore attributes to globals().
# For readability we import everything from iosutils (keeps same function names as before).
# NOTE: keep the iosutils module on PYTHONPATH.
from iosutils import *  # noqa: F401,F403

_LOG = logging.getLogger(__name__)

def process_iosxe_file(filename, match_result, product_lookup, image_lookup):
    _LOG.debug("Sub:    process_iosxe_file")

    if not match_result:
        raise ValueError(f"No match result provided for file: {filename}")

    # --- Normalize via lookup functions
    productcode = product(product_lookup)
    imagecode = imagelookup(image_lookup)

    # --- Extract IOS XE version properly (e.g., 17.09.08)
#    ver_match = re.search(r'(?<!\d)(\d{2}\.\d{2})(?:\.(\d{2}))?', filename)
    ver_match = re.search(r'(?<!\d)(\d{1,2}\.\d{1,2})(?:\.(\d{1,2}))?', filename)
    if ver_match:
        version_2 = ver_match.group(1)
        patch = ver_match.group(2) or "00"
        version_3 = f"{version_2}.{patch.zfill(2)}"
    else:
        version_2 = "unknown"
        version_3 = "unknown"

    # --- Extract SMU bug ID if present
    bug_match = re.search(r'(CSC[a-zA-Z]{2}\d{5,})', filename)
    bug_id = bug_match.group(1) if bug_match else None

    # --- Build destination path & move file
    if bug_id:
        imagecode = imagelookup("smu")
        dest_path = filepath(productcode, version_2, version_3, imagecode, bug_id)
    elif image_lookup == "none":
        dest_path = filepath(productcode)
    elif match_result == "pattern":
        dest_path = filepath(productcode, imagecode)
    else:
        dest_path = filepath(productcode, version_2, version_3, imagecode)

    filemove(dest_path, filename)

#    # --- Logging output
#    print(f"📦 Processing file: {filename}")
#    print(f"   → Product: {productcode}")
#    print(f"   → Image: {imagecode}")
#    print(f"   → Version (2): {version_2}")
#    print(f"   → Version (3): {version_3}")
#    if bug_id:
#        print(f"   → Bug ID: {bug_id}")
#    print(f"   → Destination Path: {dest_path}")

#def iosxe_postprocessing(filename,product,imagecode,version2,version3,bug_id,destination):
#    _LOG.debug("Sub:    iosxe_postprocessing")

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
        {'prefix': "asr1000-universalk9.",                'imagecode': "universalk9",           'productcode': "asr1000",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9.",                'imagecode': "smu",                   'productcode': "asr1000",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "asr1000-universalk9_npe.",            'imagecode': "universalk9_npe",       'productcode': "asr1000",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9_noli.",           'imagecode': "universalk9_noli",      'productcode': "asr1000",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000-universalk9_npe_noli.",       'imagecode': "universalk9_npe_noli",  'productcode': "asr1000",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #ASR 1000-RP1
        {'prefix': "asr1000rp1-adventerprise.",           'imagecode': "adventerprise",         'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-adventerprisek9.",         'imagecode': "adventerprisek9",       'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-adventerprisek9_noli.",    'imagecode': "adventerprisek9_noli",  'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-advipservices.",           'imagecode': "advipservices",         'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-advipservicesk9.",         'imagecode': "advipservicesk9",       'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-advipservicesk9.",         'imagecode': "smu",                   'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "asr1000rp1-advipservicesk9_noli.",    'imagecode': "advipservicesk9_noli",  'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-ipbase.",                  'imagecode': "ipbase",                'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-ipbasek9.",                'imagecode': "ipbasek0",              'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp1-sipspawmak9.",             'imagecode': "sipspawmak9",           'productcode': "asr1000rp1",     'split_type': "dot", 'suffix': ".bin"},
        #ASR 1000-RP2
        {'prefix': "asr1000rp2-adventerprise.",           'imagecode': "adventerprise",         'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-adventerprise.",           'imagecode': "adventerprise",         'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-adventerprisek9.",         'imagecode': "adventerprisek9",       'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-adventerprisek9.",         'imagecode': "smu",                   'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "asr1000rp2-adventerprisek9_noli.",    'imagecode': "adventerprisek9_noli",  'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-advipservices.",           'imagecode': "advipservices",         'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-advipservicesk9.",         'imagecode': "advipservicesk9",       'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-advipservicesk9_noli.",    'imagecode': "advipservicesk9_noli",  'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-ipbase.",                  'imagecode': "ipbase",                'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-ipbasek9.",                'imagecode': "ipbasek0",              'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr1000rp2-sipspawmak9.",             'imagecode': "sipspawmak9",           'productcode': "asr1000rp2",     'split_type': "dot", 'suffix': ".bin"},
        #ASR 1000-RPX86
        {'prefix': "asr1000rpx86-universalk9.",           'imagecode': "universalk9",           'productcode': "asr1000rpx86",   'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000rpx86-universalk9.",           'imagecode': "smu",                   'productcode': "asr1000rpx86",   'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "asr1000rpx86-universalk9_noli.",      'imagecode': "universalk9_noli",      'productcode': "asr1000rpx86",   'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000rpx86-universalk9_npe.",       'imagecode': "universalk9_npe",       'productcode': "asr1000rpx86",   'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr1000rpx86-universalk9_npe_noli.",  'imagecode': "universalk9_npe_noli",  'productcode': "asr1000rpx86",   'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8200/8300
        {'prefix': "c8000be-universalk9.",               'imagecode': "universalk9",            'productcode': "c8000be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000be-universalk9.",               'imagecode': "smu",                    'productcode': "c8000be",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c8000be-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "c8000be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8500
        {'prefix': "c8000aep-universalk9.",              'imagecode': "universalk9",            'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9.",              'imagecode': "smu",                    'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c8000aep-universalk9_npe.",          'imagecode': "universalk9_npe",        'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8500L
        {'prefix': "c8000aes-universalk9.",              'imagecode': "universalk9",            'productcode': "c8000aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aes-universalk9.",              'imagecode': "smu",                    'productcode': "c8000aes",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c8000aes-universalk9_npe.",          'imagecode': "universalk9_npe",        'productcode': "c8000aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #IR 1101
        {'prefix': "ir1101-universalk9.",                'imagecode': "universalk9",            'productcode': "ir1101",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ir1101-universalk9.",                'imagecode': "smu",                    'productcode': "ir1101",         'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "ir1101-universalk9_npe.",            'imagecode': "universalk9_npe",        'productcode': "ir1101",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #1100 ISR
        {'prefix': "c1100-universalk9.",                 'imagecode': "universalk9",            'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9.",                 'imagecode': "smu",                    'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c1100-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        #1100X ISR
        {'prefix': "isr1100be-universalk9.",             'imagecode': "universalk9",            'productcode': "isr1100be",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr1100be-universalk9.",             'imagecode': "smu",                    'productcode': "isr1100be",      'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "isr1100be-universalk9_npe.",         'imagecode': "universalk9_npe",        'productcode': "isr1100be",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #4200 ISR
        {'prefix': "isr4200-universalk9_ias.",           'imagecode': "universalk9",            'productcode': "isr4200",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4200-universalk9_ias.",           'imagecode': "smu",                    'productcode': "isr4200",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "isr4200-universalk9_ias_npe.",       'imagecode': "universalk9_npe",        'productcode': "isr4200",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #4300 ISR
        {'prefix': "isr4300-universalk9.",               'imagecode': "universalk9",            'productcode': "isr4300",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4300-universalk9.",               'imagecode': "smu",                    'productcode': "isr4300",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "isr4300-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "isr4300",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #4400 ISR
        {'prefix': "isr4400-universalk9.",               'imagecode': "universalk9",            'productcode': "isr4400",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4400-universalk9.",               'imagecode': "smu",                    'productcode': "isr4400",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "isr4400-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "isr4400",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #4400v2 ISR
        {'prefix': "isr4400v2-universalk9.",             'imagecode': "universalk9",            'productcode': "isr4400v2",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "isr4400v2-universalk9.",             'imagecode': "smu",                    'productcode': "isr4400v2",      'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "isr4400v2-universalk9_npe.",         'imagecode': "universalk9_npe",        'productcode': "isr4400v2",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 8000 Virtual
        {'prefix': "c8000v-universalk9.",                'imagecode': "install",                'productcode': "c8000v",         'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "c8000v-universalk9.",                'imagecode': "install",                'productcode': "c8000v",         'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "c8000v-universalk9.",                'imagecode': "smu",                    'productcode': "c8000v",         'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c8000v-universalk9_vga.",            'imagecode': "install",                'productcode': "c8000v",         'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "c8000v-universalk9_vga.",            'imagecode': "install",                'productcode': "c8000v",         'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "c8000v-universalk9_16G_serial_efi.", 'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_vga.",        'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_vga_efi.",    'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_serial.",      'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_serial_efi.",  'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_vga.",         'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_8G_vga_efi.",     'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_serial.",     'imagecode': "universal_kvm",          'productcode': "c8000v",         'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "c8000v-universalk9_16G_serial.",     'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_serial_efi.", 'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_vga.",        'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_16G_vga_efi.",    'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_serial.",      'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_serial_efi.",  'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_vga.",         'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9_8G_vga_efi.",     'imagecode': "universal_nfvis",        'productcode': "c8000v",         'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "c8000v-universalk9.",                'imagecode': "upgrade",                'productcode': "c8000v",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #CSR 1000V
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "smu",                    'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "upgrade",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",            'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",            'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".efi.qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",            'productcode': "csr1000v",       'split_type': "dot", 'suffix': "-serial.efi.qcow2"},
        {'prefix': "csr1000v-universalk9.",              'imagecode': "install-kvm",            'productcode': "csr1000v",       'split_type': "dot", 'suffix': "-serial.qcow2"},
        {'prefix': "csr1000v-adventerprisek9.",          'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "csr1000v_milplr-universalk9.",       'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "csr1000v_milplr-universalk9.",       'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "csr1000v_milplr-universalk9.",       'imagecode': "upgrade",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "csr1000v-universalk9milplr.",        'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "csr1000v-universalk9milplr.",        'imagecode': "install",                'productcode': "csr1000v",       'split_type': "dot", 'suffix': ".ova"},
        #1100 Terminal Services Gateway
        {'prefix': "c1100tg-universalk9.",               'imagecode': "universalk9",            'productcode': "c1100tg",        'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "c1100tg-universalk9.",               'imagecode': "smu",                    'productcode': "c1100tg",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "c1100tg-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "c1100tg",        'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 9800 Virtual Controller
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install",                'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".iso"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "smu",                    'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "apdp",                   'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".SPA.apdp.bin"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install",                'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install-kvm",            'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".qcow2"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "install-nfvis",          'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".tar.gz"},
        {'prefix': "C9800-CL-universalk9_esxi.",         'imagecode': "install-esxi" ,          'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9_nfvis.",        'imagecode': "install-nfvis",          'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9_kvm.",          'imagecode': "install-kvm",            'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".run"},
        {'prefix': "C9800-CL-universalk9.",              'imagecode': "upgrade",                'productcode': "C9800-CL",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9800 Controllers
        {'prefix': "C9800-40-universalk9_wlc.",          'imagecode': "system",                 'productcode': "C9800-40",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-40-universalk9_wlc.",          'imagecode': "system",                 'productcode': "C9800-40",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-80-universalk9_wlc.",          'imagecode': "system",                 'productcode': "C9800-80",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-80-universalk9_wlc.",          'imagecode': "system",                 'productcode': "C9800-80",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "CW9800H-wlc-universalk9.",           'imagecode': "system",                 'productcode': "CW9800H",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "CW9800H-wlc-universalk9.",           'imagecode': "system",                 'productcode': "CW9800H",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "CW9800M-wlc-universalk9.",           'imagecode': "system",                 'productcode': "CW9800M",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "CW9800M-wlc-universalk9.",           'imagecode': "system",                 'productcode': "CW9800M",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-L-universalk9_wlc.",           'imagecode': "system",                 'productcode': "C9800-L",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-L-universalk9_wlc.",           'imagecode': "system",                 'productcode': "C9800-L",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-SW-iosxe-wlc.",                'imagecode': "system",                 'productcode': "C9800-L",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "C9800-SW-iosxe-wlc.",                'imagecode': "system",                 'productcode': "C9800-L",        'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",                 'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".zip"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",                 'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",                 'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".single.ap1g6.img"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",                 'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".single.ap1g6a.img"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "system",                 'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".single.ap1g7.img"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "apsp",                   'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".SPA.apsp.zip"},
        {'prefix': "C9800-AP-universalk9.",              'imagecode': "apsp",                   'productcode': "C9800-AP",       'split_type': "dot", 'suffix': ".SPA.apsp.bin"},
        #5760 Controllers
        {'prefix': "ct5760-ipservicesk9.SPA.",           'imagecode': "system",                 'productcode': "ct5760",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ct5760-ipservicesk9ldpe.SPA.",       'imagecode': "systemldpe",             'productcode': "ct5760",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst Cellular Gateway
        {'prefix': "cg-ipservices-",                     'imagecode': "system",                 'productcode': "cg",             'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cg-ipservices.",                     'imagecode': "system",                 'productcode': "cg",             'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst Wireless Gateway
        {'prefix': "ccg110-universalk9.",                'imagecode': "system",                 'productcode': "ccg110",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #Voice Gateway
        {'prefix': "vg400-universalk9.",                 'imagecode': "universalk9",            'productcode': "vg400",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg400-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "vg400",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg4x0-universalk9.",                 'imagecode': "universalk9",            'productcode': "vg4x0",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg4x0-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "vg4x0",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg420-universalk9.",                 'imagecode': "universalk9",            'productcode': "vg420",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg420-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "vg420",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg450-universalk9.",                 'imagecode': "universalk9",            'productcode': "vg450",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "vg450-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "vg450",          'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 3850/3650
        {'prefix': "cat3k_caa-universalk9.",             'imagecode': "universalk9",            'productcode': "cat3k_caa",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat3k_caa-universalk9.",             'imagecode': "smu",                    'productcode': "cat3k_caa",      'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "cat3k_caa-universalk9ldpe.",         'imagecode': "universalk9_npe",        'productcode': "cat3k_caa",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat3k_caa-universalk9.SPA.",         'imagecode': "universalk9",            'productcode': "cat3k_caa",      'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat3k_caa-universalk9ldpe.SPA.",     'imagecode': "universalk9ldpe",        'productcode': "cat3k_caa",      'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 4500E
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",            'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        #Catalyst 9000
        {'prefix': "cat9k_iosxe.",                       'imagecode': "universalk9",            'productcode': "cat9k",          'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat9k_iosxe.",                       'imagecode': "smu",                    'productcode': "cat9k",          'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "cat9k_iosxe.",                       'imagecode': "smu",                    'productcode': "cat9k",          'split_type': "dot", 'suffix': ".SPA.apsp.bin"},
        {'prefix': "cat9k_iosxe_npe.",                   'imagecode': "universalk9_npe",        'productcode': "cat9k",          'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9200
        {'prefix': "cat9k_lite_iosxe.",                  'imagecode': "universalk9",            'productcode': "cat9k_lite",     'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cat9k_lite_iosxe.",                  'imagecode': "smu",                    'productcode': "cat9k_lite",     'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "cat9k_lite_iosxe_npe.",              'imagecode': "universalk9_npe",        'productcode': "cat9k_lite",     'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 9350
        {'prefix': "cisco9k_iosxe.",                     'imagecode': "universalk9",            'productcode': "cisco9k_iosxe",  'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "cisco9k_iosxe.",                     'imagecode': "smu",                    'productcode': "cisco9k_iosxe",  'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        #NCS 520
        {'prefix': "ncs520-universalk9_npe.",            'imagecode': "universalk9_npe",        'productcode': "ncs520",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #8100 Secure Router Gen2
        {'prefix': "c81g2be-universalk9.",               'imagecode': "universalk9",            'productcode': "c81g2be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c81g2be-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "c81g2be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #8200-8300 Secure Router Gen2
        {'prefix': "c8kg2be-universalk9.",               'imagecode': "universalk9",            'productcode': "c81g2be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8kg2be-universalk9_npe.",           'imagecode': "universalk9_npe",        'productcode': "c81g2be",        'split_type': "dot", 'suffix': ".SPA.bin"},
        #8400 Secure Router Gen2
        {'prefix': "c84g2aes-universalk9.",              'imagecode': "universalk9",            'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_npe.",          'imagecode': "universalk9_npe",        'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_noli.",         'imagecode': "universalk9_noli",       'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c84g2aes-universalk9_npe_noli.",     'imagecode': "universalk9_npe_noli",   'productcode': "c84g2aes",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #8500 Secure Router Gen2
        {'prefix': "c8000aep-universalk9.",              'imagecode': "universalk9",            'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_npe.",          'imagecode': "universalk9_npe",        'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_noli.",         'imagecode': "universalk9_noli",       'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c8000aep-universalk9_npe_noli.",     'imagecode': "universalk9_npe_noli",   'productcode': "c8000aep",       'split_type': "dot", 'suffix': ".SPA.bin"},
        #IE 9K
        {'prefix': "ie9k_iosxe.",                        'imagecode': "universalk9",            'productcode': "ie9k",           'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ie9k_iosxe.",                        'imagecode': "smu",                    'productcode': "ie9k",           'split_type': "dot", 'suffix': ".SPA.smu.bin"},
        {'prefix': "ie9k_iosxe_npe",                     'imagecode': "universalk9_npe",        'productcode': "ie9k",           'split_type': "dot", 'suffix': ".SPA.bin"},
        #Catalyst 4500e
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universal.SPA.",            'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",            'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500e-universalk9.SPA.",          'imagecode': "universalk9",            'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        #Catalyst 4500e Sup8/9
        {'prefix': "cat4500es8-universal.SPA.",          'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universal.SPA.",          'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500es8-universalk9.SPA.",        'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universalk9.SPA.",        'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        {'prefix': "cat4500es8-universalk9npe.",         'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "cat4500es8-universalk9npe.",         'imagecode': "universal",              'productcode': "cat4500e",       'split_type': "dot", 'suffix': ".tar"},
        #IE31xx
        {'prefix': "ie31xx-universalk9.",                'imagecode': "universalk9",            'productcode': "ie31xx",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #IE3x00
        {'prefix': "ie3x00-universalk9.",                'imagecode': "universalk9",            'productcode': "ie3x00",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ie3x00-universalk9_npe.",            'imagecode': "universalk9_npe",        'productcode': "ie3x00",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #IE35xx
        {'prefix': "ie35xx-universalk9.",                'imagecode': "universalk9",            'productcode': "ie35xx",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #ASR900RSP2
        {'prefix': "asr900rsp2-universalk9_npe.",        'imagecode': "universalk9_npe",        'productcode': "asr900rsp2",     'split_type': "dot", 'suffix': ".bin"},
        #ASR900RSP3
        {'prefix': "asr900rsp3-universalk9.",            'imagecode': "universalk9",            'productcode': "asr900rsp3",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr900rsp3-universalk9_npe.",        'imagecode': "universalk9_npe",        'productcode': "asr900rsp3",     'split_type': "dot", 'suffix': ".bin"},
        #ASR903RSP1
        {'prefix': "asr903rsp1_sat-universalk9_npe.",    'imagecode': "universalk9_npe",        'productcode': "asr903rsp1_sat", 'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr903rsp1-universal.",              'imagecode': "universalk9",            'productcode': "asr903rsp1",     'split_type': "dot", 'suffix': ".bin"},
        {'prefix': "asr903rsp1-universalk9_npe.",        'imagecode': "universalk9_npe",        'productcode': "asr903rsp1",     'split_type': "dot", 'suffix': ".bin"},
        #ASR920
        {'prefix': "asr920-universalk9_npe.",            'imagecode': "universalk9_npe",        'productcode': "asr920",         'split_type': "dot", 'suffix': ".SPA.bin"},
        #ASR920IGP
        {'prefix': "asr920igp-universalk9.",             'imagecode': "universalk9",            'productcode': "asr920igp",      'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "asr920igp-universalk9_npe.",         'imagecode': "universalk9_npe",        'productcode': "asr920igp",      'split_type': "dot", 'suffix': ".SPA.bin"},
        #1100 Series Routers
        {'prefix': "c1100-ucmk9.",                       'imagecode': "ucmk9",                  'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9.",                 'imagecode': "universalk9",            'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9_ias.",             'imagecode': "universalk9_ias",        'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9_ias_npe.",         'imagecode': "universalk9_ias_npe",    'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "c1100-universalk9_npe.",             'imagecode': "universalk9_npe",        'productcode': "c1100router",    'split_type': "dot", 'suffix': ".SPA.bin"},
        #IE1000
        {'prefix': "ie1000-universalk9-mz.SPA.",         'imagecode': "universalk9",            'productcode': "ie1000",         'split_type': "dot", 'suffix': ".bin"},
        #IR1800
        {'prefix': "ir1800-universalk9.",                'imagecode': "universalk9",            'productcode': "ir1800",         'split_type': "dot", 'suffix': ".SPA.bin"},
        {'prefix': "ir1800-universalk9.",                'imagecode': "smu",                    'productcode': "ir1800",         'split_type': "dot", 'suffix': ".SPA.smu.bin"},
    ]

    filename_exact = [
        #Catalyst 9xxx
        {'filename': "cat9k_iosxe.16.00.00fpgautility.SPA.bin",                                                  'imagecode': "fpga",          'productcode': "cat9k"},
        {'filename': "cat9k_fpga_upgrade_utility.pdf",                                                           'imagecode': "fpga",          'productcode': "cat9k"},
        #Catalyst ASR 1xxx
        {'filename': "asr903rsp1-universalk9_npe.V154_3_S3_SR637267017_1.bin",                                   'imagecode': "specialbuild",  'productcode': "asr903rsp1"},
        {'filename': "asr1000rp1-advipservicesk9.V152_1_S1_CSCTR15153_3.bin",                                    'imagecode': "specialbuild",  'productcode': "asr1000rp1"},
        {'filename': "asr1000rp1-adventerprisek9.BLD_V122_33_XNC_ASR_RLS3_THROTTLE_LATEST_20090513_080032.bin",  'imagecode': "specialbuild",  'productcode': "asr1000rp1"},
        {'filename': "sr1000rpx86-universalk9.V1612_1_CVE_2019_1649.SPA.bin",                                    'imagecode': "fpga",          'productcode': "asr1000rpx86"},
        #CSR 1000v
        {'filename': "csr1000v-universalk9.16.09.01.CSCvk69552.SPA.smu.bin",                                     'imagecode': "specialbuild",  'productcode': "csr1000v"},
        {'filename': "csr1000v-universalk9.16.09.01.CSCvk69552.txt",                                             'imagecode': "specialbuild",  'productcode': "csr1000v"},
    ]

    filename_pattern_match = [
        #IOS XE Compatability Matrix
        {'prefix': "17.",                        'pattern': "comp_matrix",      'imagecode': "none",          'productcode': "iosxeissumatrix"},
        #Catalyst 3850/3650
        {'prefix': "cat3k_caa",                  'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "cat3k_caa"},
        #ISR 4300
        {'prefix': "isr4300",                    'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "isr4300"},
        {'prefix': "isr4300",                    'pattern': "CSCWF02225",       'imagecode': "specialbuild",  'productcode': "isr4300"},
        #ISR 4400
        {'prefix': "isr4400",                    'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "isr4400"},
        #CSR 1000v
        {'prefix': "csr1000v",                   'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "csr1000v"},
        #ASR 1000
        {'prefix': "asr1000",                    'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "asr1000"},
        #ASR 1001x
        {'prefix': "asr1001x",                   'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "asr1001x"},
        {'prefix': "asr1001x",                   'pattern': "prd",              'imagecode': "specialbuild",  'productcode': "asr1001x"},
        {'prefix': "asr1001x",                   'pattern': "eft",              'imagecode': "specialbuild",  'productcode': "asr1001x"},
        #ASR 1002x
        {'prefix': "asr1002x",                   'pattern': "THROTTLE_LATEST",  'imagecode': "specialbuild",  'productcode': "asr1002x"},
        #Catalyst 8500 
        {'prefix': "c8000aep",                   'pattern': "CSCWF02225",       'imagecode': "specialbuild",  'productcode': "c8000aep"},
        #Catalyst Access Points
        {'prefix': "C9800-AP-universalk9.",      'pattern': "prd",              'imagecode': "specialbuild",  'productcode': "C9800-AP"},
        {'prefix': "C9800-AP-universalk9.",      'pattern': "eft",              'imagecode': "specialbuild",  'productcode': "C9800-AP"},
        {'prefix': "C9800-AP-universalk9.",      'pattern': "ESW",              'imagecode': "specialbuild",  'productcode': "C9800-AP"},
        #Wireless Controllers
        {'prefix': "C9800-L-universalk9_wlc.",   'pattern': "prd",              'imagecode': "specialbuild",  'productcode': "C9800-L"},
        {'prefix': "C9800-L-universalk9_wlc.",   'pattern': "eft",              'imagecode': "specialbuild",  'productcode': "C9800-L"},
        {'prefix': "C9800-L-universalk9_wlc.",   'pattern': "ESW",              'imagecode': "specialbuild",  'productcode': "C9800-L"},
        {'prefix': "C9800-CL-universalk9.",      'pattern': "prd",              'imagecode': "specialbuild",  'productcode': "C9800-CL"},
        {'prefix': "C9800-CL-universalk9.",      'pattern': "eft",              'imagecode': "specialbuild",  'productcode': "C9800-CL"},
        {'prefix': "C9800-CL-universalk9.",      'pattern': "ESW",              'imagecode': "specialbuild",  'productcode': "C9800-CL"},
        {'prefix': "C9800-L-rommon.",            'pattern': "rommon",           'imagecode': "rommon",        'productcode': "C9800-L"},
        {'prefix': "C9800-L-hw-programmables.",  'pattern': "programmables",    'imagecode': "hardware",      'productcode': "C9800-L"},
        {'prefix': "C9800-40-rommon.",           'pattern': "rommon",           'imagecode': "rommon",        'productcode': "C9800-40"},
        {'prefix': "C9800-80-rommon.",           'pattern': "rommon",           'imagecode': "rommon",        'productcode': "C9800-80"},
        {'prefix': "C9800-universalk9_wlc.",     'pattern': "ESW",              'imagecode': "specialbuild",  'productcode': "C9800-80"},
        {'prefix': "CW9800-rommon.",             'pattern': "rommon",           'imagecode': "rommon",        'productcode': "CW9800H"},
    ]

    filename_single_move = [
        #1100 ISR
        {'prefix': "C1100-rommon-",                                                'imagecode': "rommon",             'productcode': "c1100router"},
        {'prefix': "isr1100-bootloader.",                                          'imagecode': "rommon",             'productcode': "c1100router"},
        {'prefix': "c1100_gfast_phy_fw_",                                          'imagecode': "dslfirmware",        'productcode': "c1100router"},
        {'prefix': "c1100_phy_fw_",                                                'imagecode': "dslfirmware",        'productcode': "c1100router"},
        #ISR G3 DSL Modules
        {'prefix': "nim_vab_phy_fw_",                                              'imagecode': "dslfirmware",        'productcode': "isrg3modulesdsl"},
        #8200
        {'prefix': "C8000-2N2S",                                                   'imagecode': "rommon",             'productcode': "c8000be"},
        {'prefix': "C8000-1N",                                                     'imagecode': "rommon",             'productcode': "c8000be"},
        #Catalyst 3850/3650
        {'prefix': "CAT3650_WEBAUTH_BUNDLE",                                       'imagecode': "webauth",            'productcode': "cat3k_caa"},
        {'prefix': "CAT3850_WEBAUTH_BUNDLE",                                       'imagecode': "webauth",            'productcode': "cat3k_caa"},
        {'prefix': "cat3k_caa-universalk9.2017-04-24_21.14_phkotamr.SSA.bin",      'imagecode': "specialbuild",       'productcode': "cat3k_caa"},
        {'prefix': "cat3k_caa-universalk9.2017-05-26_21.07_phkotamr.SSA.bin",      'imagecode': "specialbuild",       'productcode': "cat3k_caa"},
        {'prefix': "cat3k_caa-universalk9.2017-06-13_16.05_phkotamr.SSA.bin",      'imagecode': "specialbuild",       'productcode': "cat3k_caa"},
        {'prefix': "cat3k_caa-universalk9.SSA.03.07.05.E5.662.152-3.6.62.E5.bin",  'imagecode': "specialbuild",       'productcode': "cat3k_caa"},
        {'prefix': "cat3k_caa-universalk9.SSA.03.07.05.E5.662.152-3.6.62.E5.txt",  'imagecode': "specialbuild",       'productcode': "cat3k_caa"},
        #ISR 4200
        {'prefix': "isr4200-firmware_nim_xdsl",                                    'imagecode': "dslfirmware",        'productcode': "isr4200"},
        {'prefix': "isr4200_cpld_update",                                          'imagecode': "cpld_update",        'productcode': "isr4200"},
        #ISR 4300
        {'prefix': "nim_vab_phy_fw_",                                              'imagecode': "dslfirmware",        'productcode': "isr4300"},
        {'prefix': "isr4300-firmware_nim_xdsl.",                                   'imagecode': "dslfirmware",        'productcode': "isr4300"},
        {'prefix': "isr4300-hw-programmables",                                     'imagecode': "hardware",           'productcode': "isr4300"},
        {'prefix': "isr4300_cpld_update",                                          'imagecode': "cpld_update",        'productcode': "isr4300"},
        #ISR 4400
        {'prefix': "isr-hw-programmables",                                         'imagecode': "hardware",           'productcode': "isr4400"},
        {'prefix': "isr4400-firmware_nim_xdsl",                                    'imagecode': "dslfirmware",        'productcode': "isr4400"},
        {'prefix': "isr4400_cpld_update",                                          'imagecode': "cpld_update",        'productcode': "isr4400"},
        #ISR 4400v2
        {'prefix': "isr4400v2-firmware_nim_xdsl",                                  'imagecode': "dslfirmware",        'productcode': "isr4400v2"},
        {'prefix': "isr4400v2_cpld_update",                                        'imagecode': "cpld_update",        'productcode': "isr4400v2"},
        {'prefix': "isr4400v2-hw-programmable",                                    'imagecode': "cpld_update",        'productcode': "isr4400v2"},
        #ASR1000RPX86
        {'prefix': "asr1000rpx86-hw-programmables",                                'imagecode': "hardware",           'productcode': "asr1000rpx86"},
        #ASR1000
        {'prefix': "asr1000-hw-programmables",                                     'imagecode': "hardware",           'productcode': "asr1000"},
        {'prefix': "asr1002x-hw-programmables",                                    'imagecode': "hardware",           'productcode': "asr1000"},
        {'prefix': "ASR1K-fpga_prog",                                              'imagecode': "hardware",           'productcode': "asr1000"},
        #SD-WAN
        {'prefix': "appqoe-dre",                                                   'imagecode': "appqoe",             'productcode': "sdwan"},
        #IOS-XE Remote Management
        {'prefix': "iosxe-remote-mgmt",                                            'imagecode': "iosxe-remote-mgmt",  'productcode': "iosxe-remote-mgmt"},
        #ASR920
        {'prefix': "asr920_15_6_",                                                 'imagecode': "rommon",             'productcode': "asr920"},
        {'prefix': "asr920-rommon",                                                'imagecode': "rommon",             'productcode': "asr920"},
        #ASR920IGP
        {'prefix': "asr920igp-",                                                   'imagecode': "rommon",             'productcode': "asr920igp"},
        {'prefix': "asr920igp-rommon-",                                            'imagecode': "rommon",             'productcode': "asr920igp"},
        {'prefix': "asr920igp_",                                                   'imagecode': "rommon",             'productcode': "asr920igp"},
    ]

    """
    Determines which product/image a given filename belongs to.
    Returns a dict with productcode and imagecode.
    """
    # --- Try pattern filename match
    for entry in filename_pattern_match:
        if filename.startswith(entry['prefix']):
            if entry['pattern'] in filename:
                matchtype   = "pattern"
                productcode = entry['productcode']
                imagecode   = entry['imagecode']
                process_iosxe_file(filename, matchtype, productcode, imagecode)

    # --- Try exact filename match
    for entry in filename_exact:
        if filename == entry['filename']:
            matchtype   = "exact"
            productcode = entry['productcode']
            imagecode   = entry['imagecode']
            process_iosxe_file(filename, matchtype, productcode, imagecode)

    # --- Try single-move prefix match
    for entry in filename_single_move:
        if filename.startswith(entry['prefix']):
            matchtype   = "single_move"
            productcode = entry['productcode']
            imagecode   = entry['imagecode']
            process_iosxe_file(filename, matchtype, productcode, imagecode)

    # --- Try firmware matching by prefix/suffix
    for entry in firmware_matching:
        if filename.startswith(entry['prefix']) and filename.endswith(entry['suffix']):
            matchtype   = "firmware"
            productcode = entry['productcode']
            imagecode   = entry['imagecode']
            process_iosxe_file(filename, matchtype, productcode, imagecode)
