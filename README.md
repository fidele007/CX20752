# Internal Mic for Conexant CX20751/2

This repo include all patches to get internal microphone working properly for Conexant CX20751/2 on Hackintosh. These patches all require [CodecCommander.kext](https://bitbucket.org/RehabMan/os-x-eapd-codec-commander/downloads/) to be installed to `/Library/Extensions`.

## Patch CodecCommander.kext

```bash
python patch.py [PATH_TO_CodecCommander.kext]
```