import hashlib

def crack_passwords(hash_path, wordlist_path, hash_type):
    hash_set = set()
    cracked = {}
    try:
        with open(hash_path,'r') as hashes:
            for line in hashes:
                hash_set.add(line.strip('\n'))
    except:
        return "Wrong Path to Hash File, Please Try Again"
    
    try:
        with open(wordlist_path, 'r') as passwords:
            for line in passwords:
                hasher = hashlib.new(hash_type)
                hasher.update(line.strip('\n').encode())
                encoded_line = hasher.hexdigest()
                if encoded_line in hash_set:
                    cracked[encoded_line] = line.strip('\n')
                    hash_set.remove(encoded_line)
    except:
        return "Wrong Path to Wordlist, or hashing algorithm is not supported by hashlib, Please Try Again"
    for h in hash_set:
        cracked[h] = 'Password not found in wordlist'
    return cracked


def main():
    hash_path = input("What is the path to the hash list file ")
    wordlist_path = input("What is the path to the wordlist file ")
    hash_type = input("What type of hash is used in the hash file ").lower()
    got_returned = crack_passwords(hash_path,wordlist_path, hash_type)
    if isinstance(got_returned, str):
        print(got_returned)
    else:
        for keys,values in got_returned.items():
            print(f"{keys}: {values}")


if __name__ == "__main__":
    main()
