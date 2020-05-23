# Cisco-Firmware-Sort
Python Script for sorting Cisco IOS Images

When initialize with a directory name, this script will read the given directory
and attempt to organize the Cisco firmware files with in.

A rough work in progress.

Usage: iossort.py (options)

Required Argument
  -d DIRECTORY, --directory DIRECTORY
                        Directory to sort

Optional Arguments (Any or all arguments accepted)
  -hs, --hashsha512     Hash File using the SHA 512 Algorithm
  -hs1, --hashsha256    Hash File using the SHA 256 Algorithm
  -hs2, --hashsha1      Hash File using the SHA1 Algorithm
  -hs3, --hashmd5       Hash File using the MD5 Algorithm

Options Arguments (Not Yet Implemented)
(Only Supports MD5 and SHA512)
(The CSV file you can obtain from the Cisco Trust Center meets this format)
  -hf, --hashfile       File with Hash Info. Format is
                        FILENAME,MD5HASH,SHA512HASH. Additional columns are
                        ignored
