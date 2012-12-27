import os

import six


# Under Python 2, define our own abspath function that can handle joining
# unicode paths to a current working directory that has non-ASCII characters
# in it.  This isn't necessary on Windows since the Windows version of abspath
# handles this correctly. It also handles drive letters differently than the
# pure Python implementation, so it's best not to replace it.
if six.PY3 or os.name == "nt":
    abspathu = abspath
else:
    def abspathu(path):
        """
        Version of os.path.abspath that uses the unicode representation
        of the current working directory, thus avoiding a UnicodeDecodeError
        in join when the cwd has non-ASCII characters.
        """
        if not os.path.isabs(path):
            path = os.path.join(os.getcwdu(), path)
        return os.path.normpath(path)
