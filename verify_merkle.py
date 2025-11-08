import hashlib
import json

# Function to do double SHA-256
def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

# Load the block JSON from lab6.txt
with open("lab6.txt", "r") as f:
    block = json.load(f)

# Extract transaction IDs
txids = [bytes.fromhex(txid)[::-1] for txid in block['tx']]

# Function to compute Merkle Root
def merkle_root(txids):
    current_level = txids
    while len(current_level) > 1:
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])  # duplicate last hash if odd
        next_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i+1]
            next_level.append(double_sha256(combined))
        current_level = next_level
    return current_level[0][::-1].hex()  # reverse bytes to match Bitcoin format

root = merkle_root(txids)
print("Computed Merkle Root:", root)
print("Block's merkleroot:", block['merkleroot'])
print("Match:", root == block['merkleroot'])
