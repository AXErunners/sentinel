import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from axed import AxeDaemon
from axe_config import AxeConfig


def test_axed():
    config_text = AxeConfig.slurp_config_file(config.axe_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000c33631ca6f2f61368991ce2dc03306b5bb50bf7cede5cfbba6db38e52e6'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c'

    creds = AxeConfig.get_rpc_creds(config_text, network)
    axed = AxeDaemon(**creds)
    assert axed.rpc_command is not None

    assert hasattr(axed, 'rpc_connection')

    # Axe testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = axed.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert axed.rpc_command('getblockhash', 0) == genesis_hash
