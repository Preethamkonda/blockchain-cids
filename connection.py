import requests

# Replace 'YOUR_ETHERSCAN_API_KEY' with your Etherscan API key
ETHERSCAN_API_KEY = 'Y3KP9FTYHW7VZ2513ZIS22SKVH6T2H8IGS'

# Ethereum address to check balance (replace with the desired address)
ethereum_address = '0x1234567890123456789012345678901234567890'

# Etherscan API endpoint for getting account balance
url = f'https://api.etherscan.io/api?module=account&action=balance&address={ethereum_address}&tag=latest&apikey={ETHERSCAN_API_KEY}'

# Make a GET request to fetch the account balance
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Handle the retrieved data
    if data['status'] == '1':
        balance_wei = int(data['result'])
        balance_eth = balance_wei / 10**18  # Convert Wei to Ether
        print(f"Ethereum Address {ethereum_address} Balance: {balance_eth} ETH")
    else:
        print("Error:", data['message'])
else:
    print("Failed to fetch data. Check your connection or API key.")
