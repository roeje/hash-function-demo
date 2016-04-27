import hashlib
import sys

# Simple hash function demo that uses various hashlib functions to hash user input

def main():

	typesOfHashes = "md4, md5, sha1, sha256, sha512, or dsa"

	print "\n\nWelcome to HashDemo!\n\n"

	# print hashlib.algorithms_available

	while(1):
			
		print "Please enter a hash function that you would like to use.\n"
		print "Your options are: " + typesOfHashes + "\n"
		htype = raw_input("Enter one of the above: ")
		htype = htype.lower()		

		if htype == "quit":
			break

		if htype == "md5" or htype == "md4" or htype == "sha1" or htype == "sha256" or htype == "sha512" or htype == "dsa":
			print "\nYou have selected the " + htype + " hashing algorithm.\n"
		else:
			print "You have entered a hash function that we do not support. Please try again. \n"
			continue

		# Switch to setup correct hash algorithm
		if htype == "md5" :
			m = hashlib.md5()
		elif htype == "sha1":
			m = hashlib.sha1();
		elif htype == "sha256":
			m = hashlib.sha256();
		elif htype == "sha512":
			m = hashlib.sha512()
		elif htype == "md4":
			m = hashlib.new("md4")
		elif htype == "dsa":
			m = hashlib.new("DSA")

		print "Now please enter the message that you would like to hash. \n"
		msg = raw_input("Enter your message here: ")

		print "Creating hash...\n\n"

		# m = getattr(hashlib, htype)
		m.update(msg)

		print "    Your message: %s" % (msg)		

		print "    hashes to: " + m.hexdigest()
		print "    with a hash size of: " + str(m.digest_size) + " bytes.\n\n"

		c = raw_input("Hit enter to try again, or quit to close the demo: ")
		c = c.lower()

		if c == "quit":
			break
		if c == "":
			continue;

if __name__ == "__main__":
   main()