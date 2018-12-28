'''
   CHECK if the string is palindrome 
   eg = "civic" , "Level"
'''
#!/usr/bin/python

from argparse import ArgumentParser

class palindrome():
    def is_palindrome(self, s1):
    	list1=list(s1)
    	list1.reverse()
    	s2=''.join(list1)
    	if s1==s2:
            return True
        else:
            return False

def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--string",dest="string1",
                        help="please provide string to check palindrome")
    args = parser.parse_args()
    m1 = palindrome()
    print m1.is_palindrome(args.string1)
if __name__=='__main__':
    main()
