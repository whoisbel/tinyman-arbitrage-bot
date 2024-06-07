from algosdk.v2client.algod import AlgodClient
from tinyman.v2.client import TinymanV2MainnetClient


def initialize_tinyman_client(algod_url, user_agent):
    algod = AlgodClient("", algod_url, headers={"User-Agent": user_agent})
    tinyman_client = TinymanV2MainnetClient(algod)
    return tinyman_client
