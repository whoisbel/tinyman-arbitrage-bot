from src.graph import Graph


def detect_arbitrage(tinyman_client, asset_ids):
    graph = update_graph(tinyman_client, asset_ids)
    graph.display()
    arbitrage_detected, arbitrage_path = graph.detect_arbitrage()
    return graph, arbitrage_detected, arbitrage_path


def update_graph(tinyman_client, asset_ids):
    updated_graph = Graph()
    for ticker1, asset_id1 in asset_ids.items():
        asset_1 = tinyman_client.fetch_asset(asset_id1)
        for ticker2, asset_id2 in asset_ids.items():
            if ticker1 != ticker2:
                try:
                    asset_2 = tinyman_client.fetch_asset(asset_id2)
                    quote = fetch_pool_and_quote_data(tinyman_client, asset_1, asset_2)
                    rate = round(quote.amount_out_with_slippage.amount / 1e6, 6)
                    if rate > 0:
                        updated_graph.add_vertex(ticker1)
                        updated_graph.add_vertex(ticker2)
                        updated_graph.add_edge(ticker1, ticker2, rate)
                except Exception as e:
                    pass
    return updated_graph


def fetch_pool_and_quote_data(tinyman_client, asset_1, asset_2):
    try:
        pool = tinyman_client.fetch_pool(asset_1, asset_2)
        quote = pool.fetch_fixed_input_swap_quote(
            asset_1(1 * pow(10, 6)), slippage=0.001
        )
        return quote
    except Exception as e:
        return None
