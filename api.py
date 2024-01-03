import requests

# Replace 'YOUR_API_KEY' with your Etherscan API key
api_key = 'Y3KP9FTYHW7VZ2513ZIS22SKVH6T2H8IGS'

# Ethereum address for which you want to retrieve transaction details
address = '0x1E42286dEB33E88e0a9E7Bf7eFFD713c4Dc2c378'

# Etherscan API endpoint for getting transaction list
url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey={api_key}'

# Fetching data from Etherscan API
response = requests.get(url)

if response.status_code == 200:
    transactions = response.json()['result']
    print(f"Transactions for address {address}:")

    for tx in transactions:
        tx_hash = tx['hash']
        tx_from = tx['from']
        tx_to = tx['to']
        tx_value = float(tx['value']) / 1e18  # Convert value from Wei to Ether
        print(f"Tx Hash: {tx_hash}, From: {tx_from}, To: {tx_to}, Value: {tx_value} Ether")
else:
    print("Failed to fetch data. Status code:", response.status_code)
