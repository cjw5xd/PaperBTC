import hashlib

import base58
import ecdsa


# Using the 0x00 prefix specifies the P2PKH locking script.
PREFIX = b'\x00'


def sha256(data):
    return hashlib.sha256(data).digest()


def ripemd160(data):
    return hashlib.new('ripemd160', data).digest()


if __name__ == '__main__':
    # Generate an ECDSA key pair.
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()

    # Calculate the public key hash, also known as the HASH160.
    public_key_hash = ripemd160(sha256(public_key._compressed_encode()))

    # Calculate the checksum for the extended public key hash.
    checksum = sha256(sha256(PREFIX + public_key_hash))[:4]

    # Determine the address in base58 format.
    address = base58.b58encode(PREFIX + public_key_hash + checksum).decode()

    print('Address:', address)
    print('Public Key:', public_key._compressed_encode().hex())
    print('Public Key Hash:', public_key_hash.hex())
    print('Private Key:', private_key.to_string().hex())
