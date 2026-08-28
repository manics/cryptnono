#!/usr/bin/env python3
# Run the right version of monero.bt depending on kernel version
# https://github.com/cryptnono/cryptnono/pull/38

import platform
import re
from os import execl

machine = platform.machine()
if machine != "x86_64":
    raise NotImplementedError(f"Architecture {machine} not supported")

# Linux 5.14 refactored struct fpu (asm/fpu/internal.h -> asm/fpu/api.h)
release = platform.release()
match = re.match(r"^(\d+)\.(\d+)", release)
if match:
    major, minor = int(match.group(1)), int(match.group(2))
    if (major, minor) < (5, 14):
        v = "v1"
    else:
        v = "v2"
else:
    v = "v2"

script = f"/scripts/monero-{v}.bt"
print(f"Running {script}")
execl(script, script)
