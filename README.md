# Tinyman Algorand DEX Arbitrage Scanner Bot

## Introduction

Welcome to the Tinyman Algorand DEX Arbitrage Scanner Bot! This bot was created purely for fun to explore arbitrage opportunities on the Tinyman DEX on the Algorand blockchain. It uses a graph-based approach and the Floyd-Warshall algorithm to find potential arbitrage cycles. Note: This bot is extremely slow and is not intended for actual arbitrage trading.

## Features

- Graph-Based Asset Mapping: Represents assets and trading pairs in a graph.
- Floyd-Warshall Algorithm: Identifies potential arbitrage cycles.
- Educational Tool: Great for learning about arbitrage and graph algorithms in a DEX context.

## Prerequisites

- Python 3.12 or higher
- Algorand SDK for Python
- Network connectivity to the Algorand blockchain

## Installation

Clone the repository:

```bash
git clone https://github.com/whoisbel/tinyman-arbitrage-bot.git
cd tinyman-arbitrage-bot
```

Install the required packages using pipenv:

```bash
pipenv install
```

## Usage

Run the bot:

```bash
pipenv run python arbitrage_scanner.py
```

The bot will output any detected arbitrage opportunities, if found.

## Disclaimer

This project is for educational and experimental purposes only. It is extremely slow and is not suitable for actual arbitrage trading. Use it to learn and have fun!
