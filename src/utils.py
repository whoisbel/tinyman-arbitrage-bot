import json


def load_assets(asset_file_path):
    with open(asset_file_path) as file:
        assets = json.load(file)
    return assets


def save_arbitrage_path(arbitrage_path, file_path="arbitrage_path.txt"):
    with open(file_path, "a") as file:
        if arbitrage_path:
            file.write("Arbitrage Path:\n")
            for i, vertex in enumerate(arbitrage_path, start=1):
                file.write(f"{i}. {vertex}\n")
            file.write("\n")
        else:
            file.write("No arbitrage path found.\n\n")
