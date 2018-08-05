import random 

def get_word():
	words = ['aatrox',
		'ahri',
		'akali',
		'alistar',
		'amumu',
		'anivia',
		'annie',
		'ashe',
		'aurelionsol',
		'azir',
		'bard',
		'blitzcrank',
		'brand',
		'braum',
		'caitlyn',
		'camille',
		'cassiopeia',
		'chogath',
		'corki',
		'darius',
		'diana',
		'draven',
		'ekko',
		'elise',
		'evelynn',
		'ezreal',
		'fiddlesticks',
		'fiora',
		'fizz',
		'galio',
		'gangplank',
		'garen',
		'gnar',
		'gragas',
		'graves',
		'hecarim',
		'heimerdinger',
		'illaoi',
		'irelia',
		'ivern',
		'janna',
		'jarvan',
		'jax',
		'jayce',
		'jhin',
		'jinx',
		'kaisa',
		'kalista',
		'karma',
		'karthus',
		'kassadin',
		'katarina',
		'kayle',
		'kayn',
		'kennen',
		'khazix',
		'kindred',
		'kled',
		'kogmaw',
		'leblanc',
		'leesin',
		'leona',
		'lissandra',
		'lucian',
		'lulu',
		'lux',
		'malphite',
		'malzahar',
		'maokai',
		'masteryi',
		'missfortune',
		'mordekaiser',
		'morgana',
		'mundo',
		'nami',
		'nasus',
		'nautilus',
		'nidalee',
		'nocturne',
		'nunu',
		'olaf',
		'orianna',
		'ornn',
		'pantheon',
		'poppy',
		'pyke',
		'quinn',
		'rakan',
		'rammus',
		'reksai',
		'renekton',
		'rengar',
		'riven',
		'rumble',
		'ryze',
		'sejuani',
		'shaco',
		'shen',
		'shyvana',
		'singed',
		'sion',
		'sivir',
		'skarner',
		'sona',
		'soraka',
		'swain',
		'syndra',
		'tahmkench',
		'taliyah',
		'talon',
		'taric',
		'teemo',
		'thresh',
		'tristana',
		'trundle',
		'tryndamere',
		'twistedfate',
		'twitch',
		'udyr',
		'urgot',
		'varus',
		'vayne',
		'veigar',
		'velkoz',
		'vi',
		'viktor',
		'wladimir',
		'wolibear',
		'warwick',
		'wukong',
		'xayah',
		'xerath',
		'xinzhao',
		'yasuo',
		'yorick',
		'zac',
		'zed',
		'ziggs',
		'zilean',
		'zoe',
		'zyra',]
	return random.choice(words).upper()
	
def check(word,guesses,guess):
	status = ''
	matches = 0
	for letter in word:
		if letter in guesses:
			status += letter
		else:
			status += '*'
		
		if letter == guess:
			matches += 1
	if matches > 1:
		print ('Yeah! The word contains', matches,'"' + guess + '"' + 's')
	elif matches == 1:
		print('Yeah! The word contains the letter "' + guess + '"')
	else:
		print('Sorry. The name does not contain the letter "' + guess + '"')

	return status

def main():
  word = get_word()
  #print(word)
  guesses = []
  guessed = False
  print ('The name contains', len(word), 'letters.')
  while not guessed:
		text = 'Please enter one letter or a {}-letter name. '.format (len(word))
		guess = input(text)
		guess = guess.upper()
		if guess in guesses:
			print ('You already guessed "' + guess + '"')
		elif len(guess) == len(word):
			guesses.append(guess)
			if guess == word:
				guessed = True
			else:
				print('Sorry, that is incorrect.')
		elif len(guess) == 1:
			guesses.append(guess)
			result = check(word,guesses,guess)
			if result == word:
				guessed = True
			
			else:
				print (result)
		else:
			print('You WRONG')
			print('Yes, the name is', word + '! You got it in', len(guesses), 'tries.')
main()