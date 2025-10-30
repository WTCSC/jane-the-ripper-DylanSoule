import hashlib

def crack_passwords(hash_path, wordlist_path):
    hash_set = {}
    with open(hash_path,'r') as hashes:
        for line in hashes:
            hash_set.add(line.strip('\n'))
    print (hash_set)

def main():
    print("dae")

# if "__name__" == "__main__":
#     main()

crack_passwords('/home/souled@CSGP.EDU/CodingWarrenTech/hashes.txt', 'tsdontmatteryet')