#import getpass
import random
i = 1;

n = ['Marilyn Monroe', 'Abraham Lincoln', 'Mother Teresa', 'John F. Kennedy', 'Martin Luther King', 'Nelson Mandela','Winston Churchill', 'Bill gates', 'Mahatma Gandhi', 'Margaret Thatcher','Christopher Columbus', 'Charles Darwin', 'Elvis Presley','Albert Einstein','Paul McCartney','Mikhail Gorbachev', 'Jawaharlal Nehru', 'Leonardo Da Vinci', 'Leo Tolstoy', 'Pablo Picasso', 'Vincent Van Gogh','Louis Pasteur','Thomas Edison','Indira Gandhi', 'Oprah Winfrey', 'Benazir Bhutto', 'Ludwig Beethoven']

randomList = random.sample(n,8)
# The 8 in random.sample(n,8) is to be able to represent a word list in binary
# 000; 001; 010; 011; 100; 101; 110; 111

print randomList
print 'Type your selection exactly as shown in the list above.'

response = ['Y','N','y','n']
correct = ['Correct','correct']

#r = getpass.getpass("Select from the list above: ")

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
