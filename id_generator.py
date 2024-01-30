import base64
import time
import random
import struct
import hashlib

def generate_id(length=12):
    """
    Generates a unique identifier of a specified length.
    The identifier is a URL-safe Base64 encoded string derived from a combination
    of a random integer, the current timestamp, and an MD5 hash.
    """

    # Generate a large random integer
    random_int = random.randint(1000000000000, 10000000000000)

    # Convert the random integer to bytes and encode it using Base64
    random_int_bytes = struct.pack('>Q', random_int)
    encoded_random_int = base64.urlsafe_b64encode(random_int_bytes).decode('utf-8')[3:-1]

    # Get the current timestamp in microseconds and encode it using Base64
    current_timestamp = int(time.time() * 10000000)
    timestamp_bytes = struct.pack('>Q', current_timestamp)
    encoded_timestamp = base64.urlsafe_b64encode(timestamp_bytes).decode('utf-8')

    # Concatenate the encoded random integer and timestamp, and hash them using MD5
    hasher = hashlib.md5()
    hasher.update((encoded_random_int + encoded_timestamp).encode('utf-8'))
    hash_bytes = hasher.digest()

    # Return the output in Base64 encoding, truncate it to specified length
    base64_hash = base64.urlsafe_b64encode(hash_bytes).decode('utf-8')[:-2][:length]

    return base64_hash
