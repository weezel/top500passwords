## Compare against TOP 500 passwords
This is a small Python hack up to generate message digests from the passwords
found from the TOP 500 passwords at
[whatsmypass.com] (http://www.whatsmypass.com/the-top-500-worst-passwords-of-all-time).

## Requirements
* Python 3.x

## Usage
Quite simple, clone the repository and run `python checktop500passwords.py
password_digest > pass.txt`.

**NOTE**: This won't work against the salted passwords!

### Example
Optimistic user has encrypted a password with sha512 hash but unfortunately the
password is one of the most common ones. The digest of the password is

`8a7bf780e30b6105a4869220dfe1589753b43705c1a6c695fefbb7dc6`
`fac0506395a9b7d30abfd7d11dc50ea541005c0bfc4316c4b609acd76`
`b4e007fd5c4d01`

It would be troublesome to try to solve the password with a bruteforce method -
well practically impossible. But with a bit of luck it might be one of the most
popular ones, hereby it is easier to count a message digest for each
password that is found from the TOP 500 list. Compare is done against the
message digests and therefore a clear text password can be gained without heavy
calculations. In the end, following trick reveals the password:

	grep -n 8a7bf780...<hash continues>... pass.txt

	457:tomcat (md5)042d39e062dd4bf342e088dc832526f9

	(sha1)774de2048394b163cf701afecba5c8042b146e7e

	(sha224)4cb3e42469212203f3b765cd3517611565213b97e35b4eb5a48a8928

	(sha256)4c506d91e8be149ef009596e2a298df926f4c77c5566e9d170d26547b1caae98

	(sha384)d6472c71292e52b693fdea0f35d9efddaab619749368ed26ff46b712862440
	c856c8904fad309bb8131e65d795ff635d

	(sha512)8a7bf780e30b6105a4869220dfe1589753b43705c1a6c695fefbb7dc6fac0506
	395a9b7d30abfd7d11dc50ea541005c0bfc4316c4b609acd76b4e007fd5c4d01

Therefore, from the line 457 we found the matching message digest, thus the
clear text password is `tomcat`.

## TODO
* Implement password compare to the program

