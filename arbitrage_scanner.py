from src.arbitrage import detect_arbitrage
from src.tinyman_client import initialize_tinyman_client
from src.utils import load_assets, save_arbitrage_path


def main():
    assets = load_assets("./asset.json")

    ALGOD_URL = "https://mainnet-api.algonode.cloud"
    USER_AGENT = "algosdk"
    tinyman_client = initialize_tinyman_client(ALGOD_URL, USER_AGENT)

    asset_ids = {asset["ticker"]: asset["asset_id"] for asset in assets}

    while True:
        graph, arbitrage_detected, arbitrage_path = detect_arbitrage(
            tinyman_client, asset_ids
        )
        if arbitrage_detected:
            print("Arbitrage opportunity detected!")
            print("Arbitrage path:", arbitrage_path)
            final_value = graph.compute_arbitrage_value(arbitrage_path, 10000)
            print("Final value after arbitrage:", final_value)
            save_arbitrage_path(arbitrage_path)
        else:
            print("No arbitrage opportunity.")


if __name__ == "__main__":
    main()
