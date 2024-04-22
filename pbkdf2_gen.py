import os
import argparse
from hashlib import pbkdf2_hmac
from getpass import getpass

def main():
	parser = argparse.ArgumentParser(description="PBKDF2 Hash Generator. Run without arguments so the Password does not show.")
	parser.add_argument('-p','--password', required=False, help='Password to hash')
	parser.print_help()
	args = parser.parse_args()

	if not args.password:
        	args.password = getpass('Type the password: ')

	iterations = 10000
	dklen = 64
	salt = os.urandom(16)
	password_to_hash = f"{args.password}"
	hash = pbkdf2_hmac('sha3_384', password_to_hash.encode('utf-8'), salt, iterations, dklen)
	pbkdf2_hash = f'pbkdf2:{iterations}:{salt.hex()}:{hash.hex()}'
	print('\n')
	print('The hash comes in the next format.')
	print('pbkdf2:iterations:salt hash:password hash')
	print('\n')
	print(pbkdf2_hash)
	file_hash = open("pbkdf2_hash.txt", "w")
	file_hash.write(pbkdf2_hash)
	file_hash.close()
	print('\n')
	print('A file within this script same folder, named pbkdf2_hash.txt, contains the whole hash generated.')
    

if __name__ == "__main__":
	main()
