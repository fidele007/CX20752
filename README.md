# Internal Mic for Conexant CX20751/2

This repo include all patches to get internal microphone working properly for Conexant CX20751/2 on Hackintosh. These patches all require [CodecCommander.kext](https://bitbucket.org/RehabMan/os-x-eapd-codec-commander/downloads/) to be installed to `/Library/Extensions`.

`SSDT-CX20752.dsl` is also included as an alternative to *CodecCommander.kext* patch, but it doesn't seem to work on Mojave. If anyone knows what's wrong, please let me know.

## Patch CodecCommander.kext

```bash
python patch.py [PATH_TO_CodecCommander.kext]
```
