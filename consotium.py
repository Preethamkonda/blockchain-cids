import hashlib
import datetime as date

# Simulated Block in a Blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha.hexdigest()

# Simulated Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Example Usage
if __name__ == "__main__":
    # Create a simulated consortium blockchain
    consortium_chain = Blockchain()

    # Simulated IDS hosts contributing blocks to the blockchain
    # Add blocks to simulate the exchange of rule sets between hosts
    block_data = [
        {"host_id": "Host1", "rule_set": ["Rule A", "Rule B"]},
        {"host_id": "Host2", "rule_set": ["Rule C", "Rule D"]},
        # Add more block data representing exchanges between IDS hosts
    ]

    for data in block_data:
        new_block = Block(len(consortium_chain.chain), date.datetime.now(), data, consortium_chain.get_latest_block().hash)
        consortium_chain.add_block(new_block)

    # Print the blocks in the simulated blockchain
    for block in consortium_chain.chain:
        print(f"Block #{block.index} | Timestamp: {block.timestamp} | Data: {block.data} | Hash: {block.hash}")
