import getpass

i = 1;

n = ['Batman', 'Superman', 'Matt Heafy', 'James Hetfield', 'Michael Jordan', 'Muhammed Ali', 'Martin Luther King', 'Sherlock Holmes','Benedict Cumberbach']

print n
print 'Type your selection exactly as shown in the list above.'

response = ['Y','N','y','n']
correct = ['Correct','correct']

r = getpass.getpass("Select from the list above: ")

while (i<21):
	c = raw_input('%d. '%i);
	d = raw_input(' ');
	if d in response:
		i = i+1;
	elif d in correct:
		print "Bingo!"
		break;
	else: 
		print "Incorrect input!";
			
print "The answer was : %s"%r

score = 21 - i;
print "Your score for this round is %d"%score
