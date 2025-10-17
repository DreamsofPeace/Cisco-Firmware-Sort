import os
import logging
import iosutils
import re

# Import all public functions from iosutils
for name in dir(iosutils):
    if not name.startswith("_"):
        globals()[name] = getattr(iosutils, name)


# ---------------- Main File Processor ---------------- #
def fileprocessor_iosxr(filename):
    logging.debug("Module: ios_iosxr")
    logging.debug("Sub:    fileprocessor_iosxr")

    patterns_for_matching = [
        #NCS 540
        {'prefix': "NCS540-docs-",     'imagecode': "docs",     'productcode': "ncs540", 'split_type': "dot"},
        {'prefix': "NCS540-iosxr-k9-", 'imagecode': "corek9",   'productcode': "ncs540", 'split_type': "dot"},
        {'prefix': "NCS540-iosxr-",    'imagecode': "core",     'productcode': "ncs540", 'split_type': "dot"},
        {'prefix': "ncs540-usb_boot-", 'imagecode': "usb_boot", 'productcode': "ncs540", 'split_type': "dot"},
        #NCS 540
        {'prefix': "NCS560-docs-",     'imagecode': "docs",     'productcode': "ncs560", 'split_type': "dot"},
        {'prefix': "NCS560-iosxr-k9-", 'imagecode': "corek9",   'productcode': "ncs560", 'split_type': "dot"},
        {'prefix': "NCS560-iosxr-",    'imagecode': "core",     'productcode': "ncs560", 'split_type': "dot"},
        {'prefix': "ncs560-usb_boot-", 'imagecode': "usb_boot", 'productcode': "ncs560", 'split_type': "dot"},
        #ASR 9000
        {'prefix': "ASR9000-iosxr-k9-",                  'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9000-iosxr-",                     'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-docs-",                        'imagecode': "docs",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-k9-",                    'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-p-",                     'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-",                       'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-p-k9-",                  'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-iosxr-px-k9-",                 'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-px-docs-",                     'imagecode': "docs",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-x64-docs-",                    'imagecode': "docs",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-x64-iosxr-",                   'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-x64-iosxr-px-",                'imagecode': "core",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-x64-iosxr-px-k9-",             'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "ASR9K-x64-iosxr-k9-",                'imagecode': "corek9",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-goldenk9-x64-",                'imagecode': "goldenk9",       'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-mini-",                        'imagecode': "mini",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-mini-x64-",                    'imagecode': "mini-x64",       'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-full-x64-",                    'imagecode': "core64",         'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-x64-usb_boot-",                'imagecode': "usb_boot",       'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-mini-x64-migrate_to_eXR.tar-", 'imagecode': "migrate_to_eXR", 'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-full-x64-migrate_to_eXR.tar-", 'imagecode': "migrate_to_eXR", 'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-mini-x64-migrate_to_eXR.tar.", 'imagecode': "migrate_to_eXR", 'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-mini-x64-migrate_to_eXR.",     'imagecode': "migrate_to_eXR", 'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-ncs500x-nV-px-",               'imagecode': "ncs500x-nV",     'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-vsm-ipsec-fp-CCO-",            'imagecode': "vsm",            'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-vsm-ipsec-hp-CCO-",            'imagecode': "vsm",            'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-vsm-cgv6-",                    'imagecode': "cgv6",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-vsm-cgv6.",                    'imagecode': "cgv6",           'productcode': "asr9k", 'split_type': "dot"},
        {'prefix': "asr9k-vsm-mb-ipsec-fp-CCO-",         'imagecode': "vsm",            'productcode': "asr9k", 'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "asr9k-vsm-mb-ipsec-hp-CCO-",         'imagecode': "vsm",            'productcode': "asr9k", 'split_type': "dot", 'suffix': ".ova"},
        {'prefix': "asr9k-ism-cgv6-install-kit-",        'imagecode': "cgv6",           'productcode': "asr9k", 'split_type': "dot", 'suffix': ".sh"},
        {'prefix': "asr9k-ism-cgv6-install-kit.",        'imagecode': "cgv6",           'productcode': "asr9k", 'split_type': "dot", 'suffix': ".sh"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "bridge_smus",    'productcode': "asr9k", 'split_type': "dot", 'suffix': ".bridge_smus.tar"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "bridge_smus",    'productcode': "asr9k", 'split_type': "dot", 'suffix': "-bridge_smus.tar"},
        {'prefix': "ASR9K-iosxr-",                       'imagecode': "bridge_smus",    'productcode': "asr9k", 'split_type': "dot", 'suffix': "-bridge_smus.tar"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "turboboot",      'productcode': "asr9k", 'split_type': "dot", 'suffix': "-turboboot.tar"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "turboboot",      'productcode': "asr9k", 'split_type': "dot", 'suffix': ".turboboot.tar"},
        {'prefix': "ASR9K-iosxr-px-",                    'imagecode': "turboboot",      'productcode': "asr9k", 'split_type': "dot", 'suffix': "-Turboboot.tar"},
        #XRd Container
        {'prefix': "xrd-control-plane-container-x86.",   'imagecode': "control-plane",  'productcode': "xrvcontainer", 'split_type': "dot"},
        {'prefix': "xrd-vrouter-container-x86.",         'imagecode': "data-plane",     'productcode': "xrvcontainer", 'split_type': "dot"},
    ]

    smu_matching = {
        "asr9k-px-":         "asr9k",
        "asr9k-x64-":        "asr9k",
        "asr9k-sysadmin-":   "asr9k",
        "comp-asr9k-":       "asr9k",
        "asr9k-rout-":       "asr9k",
        "asr9k-os-mbi-":     "asr9k",
        "asr9k-mpls-":       "asr9k",
        "asr9k-lc-":         "asr9k",
        "asr9k-fwdg-":       "asr9k",
        "asr9k-fpd-":        "asr9k",
        "asr9k-base-":       "asr9k",
        "asr9k-p-":          "asr9k",
        "asr9k-admin-":      "asr9k",
        "ncs540-":           "ncs540",
        "ncs540-sysadmin-":  "ncs540",
        "c12k-":             "c12k",
        "xrv9k-sysadmin-":   "iosxrvfull",
        "xrv9k-":            "iosxrvfull",
    }

    #IOS XR SMU Handling
    if (
        "CSC" in filename or 
        filename.endswith("-Optima.tar") or 
        filename.endswith("-srpce-nb-api-extension.tar")
        ):
        # Sort prefixes by length, descending, for longest-match-first
        sorted_prefixes = sorted(smu_matching.keys(), key=len, reverse=True)
        for prefix in sorted_prefixes:
            if filename.startswith(prefix):
                prod_key = smu_matching[prefix]
                # Look up the product object using the prod_key
                prodname = product(prod_key)
                # Look up the image code
                imagecode = imagelookup("smu")
                # Extract the workname by stripping prefix and .tar
                workname = filename[len(prefix):]
                if workname.endswith(".tar"):
                    workname = workname[:-4]
                # Call the function
                iosxr_smu(filename, prodname, imagecode, workname)
                break  # Stop after first match

    # IOS XR REC SMUS Handling (.tar or .tgz)
    elif re.match(r"^\d+\.\d+\.\d+_.*_REC_SMUS_.*\.(tar|tgz)$", filename):
        iosxr_rec_smus(filename)

    #IOS XR SMU Handling
    elif (
        filename.startswith("asr9k-px-") and ".sp" in filename or
        filename.startswith("asr9k-px-") and "-sp" in filename or
        filename.startswith("asr9k-x64-") and "-sp" in filename
        ):
        prodname = product("asr9k")
        iosxr_service_pack(filename, prodname)

    #IOS XR Handler
    elif iosxr_generic_handler(filename, patterns_for_matching):
        logging.debug("Sub:    Returned from iosxr_generic_handler")

    elif filename in ["CSM.zip", "csm-3.5.2.zip", "csm-4.0.zip"]:
        prodname = product("asr9k")
        imagecode = imagelookup("ciscosoftwaremanager")
        utilssinglemove(filename, prodname, imagecode)

    elif filename.startswith(("fullk9", "xrv9k", "XRV9000-docs", "XRV9K-docs")):
        prodname = product("iosxrvfull")
        iosxr_iosxrv(filename, prodname)

    elif filename.startswith(("iosxrv-demo", "iosxrv-k9-demo")):
        iosxr_iosxrv_demo(filename)

    elif filename.startswith("xrd-control-plane-container-"):
        _process_xrd_container(filename, "control-plane")

    elif filename.startswith("xrd-vrouter-container-"):
        _process_xrd_container(filename, "data-plane")

    elif filename.startswith("asr9k-cnbng-x64"):
        _process_asr9k_cnbng(filename)

    elif filename.startswith("asr9k-9000v-nV-x64-"):
        _process_asr9k_9000v_nv_x64(filename)

    else:
        messageunknowndev()

def iosxr_generic_handler(filename, product_patterns):
    logging.debug("Sub:    iosxr_generic_handler")
    """
    Generic IOS-XR handler for ASR9K, NCS540, etc.
    Reads rules from product_patterns (prefix/imagecode/productcode/split_type[/suffix]).
    Gives priority to patterns with longer prefixes and, when equal, longer suffixes.
    """

    # Sort: longest prefix first, then longest suffix
    sorted_patterns = sorted(
        product_patterns,
        key=lambda p: (len(p["prefix"]), len(p.get("suffix", ""))),
        reverse=True,
    )

    for pattern in sorted_patterns:
        prefix = pattern["prefix"]
        suffix = pattern.get("suffix", "")

        # Both prefix and suffix must match
        if not filename.startswith(prefix):
            continue
        if suffix and not filename.endswith(suffix):
            continue

        # ✅ When multiple patterns share prefix but differ by suffix,
        # we already prefer the one with the longest suffix due to sort order.
        # So we can safely pick the first match and stop.
        imagecode = imagelookup(pattern["imagecode"])
        prodname = product(pattern.get("productcode", "unknown"))

        # Remove prefix and optional suffix
        workname = filename[len(prefix):]
        if suffix:
            workname = workname[: -len(suffix)]

        # Remove common file extensions (.tar, .rpm, etc.)
        for ext in (".tar", ".tgz", ".rpm", ".bin", ".iso", ".ova"):
            if workname.endswith(ext):
                workname = workname[: -len(ext)]

        # Handle Golden ISO cleanup
        if pattern["imagecode"] == "goldenk9":
            workname = workname.replace("-SPGISO0001", "")
            workname = workname.replace("-SPGISO0002", "")
            workname = workname.replace("-SPGISO0003", "")

        # Split version number
        split_type = pattern.get("split_type", "dot")
        if split_type == "dot":
            parts = workname.split(".")
        elif split_type == "dash":
            parts = workname.split("-")
        else:
            raise ValueError(f"Unsupported split_type: {split_type}")

        # Validate
        if len(parts) < 3:
            logging.warning(f"Cannot determine version for {filename} (parts={parts})")
            return False

        # Compute version info
        ver2 = util_dot_join(parts[0], parts[1])
        ver3 = util_dot_join(parts[0], parts[1], parts[2])

        logging.debug(f"        imagecode={imagecode}")
        logging.debug(f"        prodname={prodname}")
        logging.debug(f"        ver2={ver2}")
        logging.debug(f"        ver3={ver3}")

        dest = filepath(prodname, ver2, ver3, imagecode)
        filemove(dest, filename)
        return True

    # If no pattern matches
    return False

# ---------------- IOS-XRV Handlers ---------------- #
def iosxr_iosxrv(filename, prodname):
    logging.debug("Sub:    iosxr_iosxrv")

    # Remove known prefixes and suffixes
    prefixes = ["fullk9-R-XRV9000-", "XRV9K-docs-", "XRV9000-docs-", "xrv9k-"]
    suffixes = ["-RRVG", "-RR", "-VG", ".tar", "-Optima", "-srpce-nb-api-extension"]
    
    workname = filename
    for p in prefixes:
        workname = workname.replace(p, "")
    for s in suffixes:
        workname = workname.replace(s, "")

    splitbydot = list(workname) if '.' not in workname else workname.split(".")

    def get_versions(parts):
        """Helper to compute version2 and version3"""
        if len(parts) == 5:
            p1 = collapse_strings(parts[0], parts[1])
            p3 = collapse_strings(parts[3], parts[4])
            version2 = util_dot_join(p1, parts[2])
            version3 = util_dot_join(p1, parts[2], p3)
        elif len(parts) == 4:
            p3 = collapse_strings(parts[2], parts[3])
            version2 = util_dot_join(parts[0], parts[1])
            version3 = util_dot_join(parts[0], parts[1], p3)
        else:
            version2 = util_dot_join(*parts[:2])
            version3 = util_dot_join(*parts[:3])
        return version2, version3

    # Determine imagecode based on filename
    if "CSC" in filename or filename in [
        "xrv9k-6.6.3-Optima.tar", "xrv9k-6.6.3-srpce-nb-api-extension.tar"
    ]:
        imagecode = imagelookup("smu")
        version2, version3 = util_dot_join(splitbydot[0], splitbydot[1]), util_dot_join(splitbydot[0], splitbydot[1], splitbydot[2])
    elif filename.startswith(("XRV9K-docs-", "XRV9000-docs-")):
        imagecode = imagelookup("docs")
        version2, version3 = util_dot_join(splitbydot[0], splitbydot[1]), util_dot_join(*splitbydot[:3])
    else:
        suffix_map = {
            "-RRVG.tar": "rrvga",
            "-RR.tar": "rr",
            "-VG.tar": "basevga"
        }
        imagecode = imagelookup(suffix_map.get(next((s for s in suffix_map if filename.endswith(s)), ""), "base"))
        version2, version3 = get_versions(splitbydot)

    # Move the file
    filepath_final = filepath(prodname, version2, version3, imagecode)
    filemove(filepath_final, filename)

def iosxr_iosxrv_demo(filename):
    logging.debug("Sub:    iosxr_iosxrv_demo")
    prodname = product("iosxrvdemo")
    workname = filename
    for p in ["iosxrv-demo.ova-", "iosxrv-demo.vmdk-", "iosxrv-k9-demo-", "iosxrv-demo-"]:
        workname = workname.replace(p, "")
    for s in [".vmdk", ".ova"]:
        workname = workname.replace(s, "")

    splitbydot = workname.split(".")
    version = util_dot_join(*splitbydot[:3])
    filepath_final = filepath(prodname, version)
    filemove(filepath_final, filename)


# ---------------- Helper Functions ---------------- #
def _process_asr9k_cnbng(filename):
    logging.debug("Sub:    _process_asr9k_cnbng")
    prodname = product("asr9k")
    imagecode = imagelookup("cnbng")

    # Accept: .x86_64.rpm, .x86_64.tar, .tar, .tgz (case-insensitive)
    m = re.match(
        r"^asr9k-cnbng-x64-\d+\.\d+\.\d+\.\d+-r(\d+)(?:\.x86_64)?\.(?:rpm|tar|tgz)$",
        filename,
        re.IGNORECASE,
    )
    if not m:
        logging.warning(f"Unrecognized CNBNG filename format: {filename}")
        return

    build_num = m.group(1)          # e.g. "762", "792", "6515"
    digits = list(build_num)        # ['6','5','1','5'] etc.

    # ver2 = first.two digits, ver3 = first.two digits + remaining digits as third part
    if len(digits) >= 3:
        rem = "".join(digits[2:])   # '2' or '15' etc.
        ver2 = util_dot_join(digits[0], digits[1])
        ver3 = util_dot_join(digits[0], digits[1], rem)
    elif len(digits) == 2:
        ver2 = util_dot_join(digits[0], digits[1])
        ver3 = util_dot_join(digits[0], digits[1], "0")
    else:
        ver2 = util_dot_join(digits[0], "0")
        ver3 = util_dot_join(digits[0], "0", "0")

    logging.debug(f"        CNBNG build_num={build_num}, ver2={ver2}, ver3={ver3}")

    filepath_final = filepath(prodname, ver2, ver3, imagecode)
    filemove(filepath_final, filename)



def iosxr_service_pack(filename, prodname):
    logging.debug("Sub:    iosxr_service_pack")
    suffix_map = {f"sp{i}.tar": f"sp{i}" for i in range(1, 13)}
    suffix_map["sp-1.0.0.tar"] = "sp1"
    imagecode = next((imagelookup(v) for s, v in suffix_map.items() if filename.endswith(s)), None)
    if imagecode is None:
        raise ValueError(f"Unrecognized service pack filename: {filename}")

    splitbydot = filename.split("-")[2].split(".")
    ver2 = util_dot_join(splitbydot[0], splitbydot[1])
    ver3 = util_dot_join(splitbydot[0], splitbydot[1], splitbydot[2])
    filepath_final = filepath(prodname, ver2, ver3, imagecode)
    filemove(filepath_final, filename)

def iosxr_smu(filename, prodname, imagecode, workname):
    logging.debug("Sub:    iosxr_smu")
    splitbydot = workname.split(".")
    version2 = util_dot_join(splitbydot[0], splitbydot[1])
    version3 = util_dot_join(splitbydot[0], splitbydot[1], splitbydot[2])
    if "-Optima" in workname:
        version3 = version3.replace("-Optima", "")
        filepath_final = filepath(prodname, version2, version3, imagecode, "Optima")
        filemove(filepath_final, filename)
    elif "-srpce-nb-api-extension" in workname:
        version3 = version3.replace("-srpce-nb-api-extension", "")
        filepath_final = filepath(prodname, version2, version3, imagecode, "srpce-nb-api-extension")
        filemove(filepath_final, filename)
    else:
        filepath_final = filepath(prodname, version2, version3, imagecode, splitbydot[3])
        filemove(filepath_final, filename)

def _process_asr9k_9000v_nv_x64(filename):
    logging.debug("Sub:    _process_asr9k_9000v_nv_x64")

    prodname = product("asr9k")
    imagecode = imagelookup("ncs500x-nV")

    # Example filenames:
    #   asr9k-9000v-nV-x64-1.0.0.0-r651.x86_64.rpm  → 6.5.1
    #   asr9k-9000v-nV-x64-1.0.0.0-r6515.x86_64.rpm → 6.5.15

    # Strip the fixed parts
    workname = filename
    workname = workname.replace("asr9k-9000v-nV-x64-", "")
    workname = workname.replace(".x86_64.rpm", "")

    # Extract the r#### part
    match = re.search(r"r(\d+)", workname)
    if not match:
        logging.warning(f"Cannot extract version from {filename}")
        return

    version_num = match.group(1)

    # Convert r651 → 6.5.1, r6515 → 6.5.15, etc.
    if len(version_num) == 3:
        version2 = f"{version_num[0]}.{version_num[1]}"
        version3 = f"{version_num[0]}.{version_num[1]}.{version_num[2]}"
    elif len(version_num) == 4:
        version2 = f"{version_num[0]}.{version_num[1]}"
        version3 = f"{version_num[0]}.{version_num[1]}.{version_num[2:]}"
    else:
        logging.warning(f"Unexpected version pattern in {filename}")
        return

    filepath_final = filepath(prodname, version2, version3, imagecode)
    filemove(filepath_final, filename)

def iosxr_rec_smus(filename):
    logging.debug("Sub:    iosxr_rec_smus")

    # Examples:
    # 3.9.1_asr9k_REC_SMUS_2011-12-12.tar
    # 4.2.0_asr9k-px_REC_SMUS_2013-09-05.tgz

    # Normalize filename to strip extensions
    if filename.endswith(".tar"):
        workname = filename[:-4]
    elif filename.endswith(".tgz"):
        workname = filename[:-4]
    else:
        logging.warning(f"Unexpected extension for REC SMU: {filename}")
        return

    # Ensure format matches: version at start, followed by product and REC_SMUS
    if not re.match(r"^\d+\.\d+\.\d+_", workname):
        logging.warning(f"Unrecognized REC SMU format: {filename}")
        return

    # Split version from rest
    try:
        version_part, rest = workname.split("_", 1)
    except ValueError:
        logging.warning(f"Unexpected structure for REC SMU: {filename}")
        return

    # Determine product code from the middle section
    if "asr9k-px" in rest:
        prod_key = "asr9k"
    elif "asr9k-p" in rest:
        prod_key = "asr9k"
    elif "asr9k" in rest:
        prod_key = "asr9k"
    else:
        prod_key = "unknown"

    prodname = product(prod_key)
    imagecode = imagelookup("smu")

    # Extract version info from start (e.g. 4.2.1)
    parts = version_part.split(".")
    if len(parts) < 2:
        logging.warning(f"Invalid version format in {filename}")
        return

    ver2 = util_dot_join(parts[0], parts[1])
    ver3 = util_dot_join(*parts[:3]) if len(parts) >= 3 else ver2

    # Build destination path and move file
    filepath_final = filepath(prodname, ver2, ver3, imagecode)
    filemove(filepath_final, filename)

