from logging import getLogger

from PyInstaller.utils.hooks import collect_data_files, get_hook_config

import pyopenjtalk

logger = getLogger(__name__)

# tqdm exclud by default.
# If you want to download dictionaries at runtime, add them manually.
excludedimports = ["tqdm"]


def hook(hook_api):
    """
    # ref: https://pyinstaller.org/en/stable/hooks-config.html
    # exsample
    hooksconfig={
        "pyopenjtalk": {
            "collect_dictionary": True,
            "collect_htsvoice": False
        }
    },
    """
    datas = []
    collect_dictionary = get_hook_config(hook_api, "pyopenjtalk", "collect_dictionary")
    if collect_dictionary is None or collect_dictionary is True:
        datas += collect_data_files("pyopenjtalk", includes=[pyopenjtalk._dic_dir_name])
        if len(datas) == 0:
            if collect_dictionary is True:
                pyopenjtalk._lazy_init()
                datas += collect_data_files(
                    "pyopenjtalk", includes=[pyopenjtalk._dic_dir_name]
                )
            else:
                logger.warning("Failed to collect dictionary")

    collect_htsvoice = get_hook_config(hook_api, "pyopenjtalk", "collect_htsvoice")
    if collect_htsvoice is None or collect_htsvoice is True:
        datas += collect_data_files("pyopenjtalk.htsvoice")

    hook_api.add_datas(datas)
