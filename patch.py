import plistlib
import os
import sys

def patch_codec_commander(kext_path):
    info_path = os.path.join(kext_path, 'Contents', 'Info.plist')

    if not os.path.exists(info_path):
        print('Cannot find Info.plist')
        return

    with open(info_path, 'rb') as fp:
        plist = plistlib.load(fp)

    # Add profile for CX20752
    plist['IOKitPersonalities']['CodecCommander']['Codec Profile']['14f1_510f'] = 'CX20752'

    # Configure CX20752 profile
    custom_command_1 = {'Command': '0x01970724',
                        'Comment': '0x19 SET_PIN_WIDGET_CONTROL 0x24',
                        'On Init': True,
                        'On Sleep': False,
                        'On Wake': True
                       }
    custom_command_2 = {'Command': '0x01a70724',
                        'Comment': '0x1a SET_PIN_WIDGET_CONTROL 0x24',
                        'On Init': True,
                        'On Sleep': False,
                        'On Wake': True
                       }
    conexant_dict = {'Custom Commands': [custom_command_1, custom_command_2],
                     'Perform Reset': False,
                     'Perform Reset on External Wake': False
                    }
    plist['IOKitPersonalities']['CodecCommander']['Codec Profile']['CX20752'] = conexant_dict

    with open(info_path, 'wb') as fp:
        plistlib.dump(plist, fp)

    print('Patch done.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: patch.py <path_to_codec_commander_kext>')
        sys.exit(2)

    patch_codec_commander(sys.argv[1])
