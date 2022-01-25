import sys, rsa

def hextoint(s):
    return int(s, 16)

def main():

    print("Usage:")
    print("python test.py make-keys [name]")
    print("python test.py encrypt [infile] from [name] to [outfile]")
    print("python test.py decrypt [infile] as [name] to [outfile]")



    if sys.argv[1] == 'make-keys':
        name = sys.argv[2]
        print("Computing...")
        k2, k1 = rsa.create_keys()
        print("pubkey", k1)
        print("privatekey", k2)
        pubf = open(name + '.pub', 'w')
        privf = open(name + '.priv', 'w')
        pubf.write(hex(k1[0]) + ':' + hex(k1[1]))
        privf.write(hex(k2[0]) + ':' + hex(k2[1]))
        pubf.close()
        privf.close()
        print('Done!')

    elif sys.argv[1] == 'encrypt':
        if sys.argv[3] != 'from':
            print('Error: specify for whom you are encrypting. (Which public key to use)')
            exit(1)
        if sys.argv[5] != 'to':
            print('Error: specify to which file you want the output saved.')
        pubf = open(sys.argv[4] + '.pub', 'r')
        msgf = open(sys.argv[2], 'rb')
        pubkey = tuple(map(hextoint, pubf.read().split(':')))
        msg = msgf.read()
        pubf.close()
        msgf.close()
        print("msg=",msg)
        enc_data = rsa.encrypt_bytes(msg, pubkey)
        with open(sys.argv[6],"w") as writer:
            for ed in enc_data:
                writer.write(hex(ed))
                writer.write(",")
        print("Done!")
    elif sys.argv[1] == 'decrypt':
        if sys.argv[3] != 'as':
            print('Error: specify which private key to use.')
            exit(1)
        if sys.argv[5] != 'to':
            print('Error: specify to which file you want the output saved.')
        privf = open(sys.argv[4] + '.priv', 'r')
        privkey = tuple(map(hextoint, privf.read().split(':')))
        msg = []
        with open(sys.argv[2],"r") as reader:
            for m in reader.read().strip().split(","):
                if m:
                    msg.append(hextoint(m))
        privf.close()
        dec = rsa.decrypt_bytes(msg, privkey)
        with open(sys.argv[6], 'wb') as writer:
            writer.write(bytes(dec))
        print("Done!")
    else:
        print("Usage:")
        print("python test.py make-keys [name]")
        print("python test.py encrypt [infile] from [name] to [outfile]")
        print("python test.py decrypt [infile] as [name] to [outfile]")

if __name__ == '__main__':
    main()
    
