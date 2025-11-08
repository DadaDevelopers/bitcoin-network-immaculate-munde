from pybloom_live import BloomFilter

# Create a Bloom filter
bf = BloomFilter(capacity=1000, error_rate=0.001)

# Add a sample transaction ID
sample_txid = "ba868a5fb9b959f3596cad36bb4ee20e9c29e0dae2f6bb2649a060e221805787"
bf.add(sample_txid)

# Test probabilistic matching
test_txid = "ba868a5fb9b959f3596cad36bb4ee20e9c29e0dae2f6bb2649a060e221805787"
another_txid = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

with open("lab7.txt", "w") as f:
    f.write("Sample TXID added to Bloom Filter: " + sample_txid + "\n")
    f.write("Bloom Filter bit array: " + str(bf.bitarray) + "\n\n")
    
    # Probabilistic matching results
    if test_txid in bf:
        f.write(f"TXID {test_txid} is probably in the Bloom Filter.\n")
    else:
        f.write(f"TXID {test_txid} is definitely not in the Bloom Filter.\n")
    
    if another_txid in bf:
        f.write(f"TXID {another_txid} is probably in the Bloom Filter.\n")
    else:
        f.write(f"TXID {another_txid} is definitely not in the Bloom Filter.\n")
    
    