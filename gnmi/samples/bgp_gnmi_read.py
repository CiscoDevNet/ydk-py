"""
Read all data for model openconfig-bgp.
usage: nc-read-oc-bgp-10-ydk.py [-h] [-v] device
positional arguments:
  device         NETCONF device (ssh://user:password@host:port)
optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urllib.parse import urlparse
from ydk.path import Repository
from ydk.services import CRUDService
from ydk.providers import gNMIServiceProvider
from ydk.models.openconfig import openconfig_bgp
import logging


def process_bgp(bgp):
    """Process data in bgp object."""
    pass


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

    repo = Repository("/usr/local/share/ydk/0.0.0.0:50051/")
    # create gNMI provider
    provider = gNMIServiceProvider(repo, address="pavarotti:57400")
    # create CRUD service
    crud = CRUDService()

    bgp = openconfig_bgp.Bgp()  # create object

    # read data from gNMI device
    bgp = crud.read_config(provider, bgp)
    process_bgp(bgp)  # process object data

    exit()
# End of script