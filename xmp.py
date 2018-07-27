"""An example showing how the XMP
(https://en.wikipedia.org/wiki/Extensible_Metadata_Platform) metadata
can be read.
"""

import json
# import os

from libxmp import XMPFiles
from libxmp.utils import object_to_dict

EQUALS = '=' * 78
DASHES = '-' * 78


# def touch(fname, mode=0o666, dir_fd=None, **kwargs):
#     """https://stackoverflow.com/a/1160227/3249688"""
#     flags = os.O_CREAT | os.O_APPEND
#     with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
#         os.utime(f.fileno() if os.utime in os.supports_fd else fname,
#                  dir_fd=None if os.supports_fd else dir_fd, **kwargs)


if __name__ == '__main__':

    xmpf = XMPFiles()
    xmpf.open_file("eric_john_berquist_etd.pdf")
    xmp = xmpf.get_xmp()
    xmpf.close_file()

    # Inspect the formatted XMP.
    xmpfilename = "eric_john_berquist_etd.xmp"
    with open(xmpfilename, 'w') as xmpfile:
        xmpfile.write(str(xmp))

    d = object_to_dict(xmp)
    d_json = dict()

    for k in d:
        print(EQUALS)
        print(k)
        print(DASHES)
        for subheader in d[k]:
            key, value = subheader[:2]
            print(key, value)
            assert len(subheader) == 3
            # This part is metadata about the metadata.
            assert isinstance(subheader[2], dict)

        # Make a JSON representation.
        d_json[k] = dict()
        for subheader in d[k]:
            key, value = subheader[:2]
            d_json[k][key] = value
    print(json.dumps(d_json))
