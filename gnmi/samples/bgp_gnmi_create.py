"""
Read all data for model openconfig-bgp.
usage: nc-read-oc-bgp-10-ydk.py [-h] [-v] device
positional arguments:
  device         gNMI device (ssh://user:password@host:port)
optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urllib.parse import urlparse
from ydk.path import Repository
from ydk.services import CRUDService
from ydk.providers import gNMIServiceProvider
from ydk.models.openconfig import openconfig_bgp as oc_bgp
from ydk.models.openconfig import openconfig_bgp_types
import logging


def config_bgp(bgp_cfg):
    """Process data in bgp object."""
    bgp_cfg.global_.config.as_ = 65001
    # Global config done

    # IPv4 Neighbor instance config
    nbr_ipv4 = bgp_cfg.neighbors.Neighbor()
    nbr_ipv4.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.peer_as = 65002

    bgp_cfg.neighbors.neighbor.append(nbr_ipv4)
    nbr_ipv4.parent = bgp_cfg.neighbors

    # IPv4 Neighbor instance config done

if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="gNMI device (ssh://user:password@host:port)")
    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create gNMI provider
    repository = Repository('/home/ygorelik/ydk-gen/scripts/samples/repository/192.168.122.107")
    provider = gNMIServiceProvider(repo=repository,
                                      address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password)    
    # create CRUD service
    crud = CRUDService()
    bgp = oc_bgp.Bgp() 
    config_bgp(bgp) 
    bgp = crud.create(provider, bgp)

    exit()
# End of script
