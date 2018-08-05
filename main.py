import random 

def get_word():
	words = ['Aatrox',
		'Ahri',
		'Akali',
		'Alistar',
		'Amumu',
		'Anivia',
		'Annie',
		'Ashe',
		'AurelionSol',
		'Azir',
		'Bard',
		'Blitzcrank',
		'Brand',
		'Braum',
		'Caitlyn',
		'Camille',
		'Cassiopeia',
		'ChoGath',
		'Corki',
		'Darius',
		'Diana',
		'Draven',
		'Ekko',
		'Elise',
		'Evelynn',
		'Ezreal',
		'Fiddlesticks',
		'Fiora',
		'Fizz',
		'Galio',
		'Gangplank',
		'Garen',
		'Gnar',
		'Gragas',
		'Graves',
		'Hecarim',
		'Heimerdinger',
		'Illaoi',
		'Irelia',
		'Ivern',
		'Janna',
		'Jarvan',
		'Jax',
		'Jayce',
		'Jhin',
		'Jinx',
		'KaiSa',
		'Kalista',
		'Karma',
		'Karthus',
		'Kassadin',
		'Katarina',
		'Kayle',
		'Kayn',
		'Kennen',
		'KhaZix',
		'Kindred',
		'Kled',
		'KogMaw',
		'LeBlanc',
		'LeeSin',
		'Leona',
		'Lissandra',
		'Lucian',
		'Lulu',
		'Lux',
		'Malphite',
		'Malzahar',
		'Maokai',
		'MasterYi',
		'MissFortune',
		'Mordekaiser',
		'Morgana',
		'Mundo',
		'Nami',
		'Nasus',
		'Nautilus',
		'Nidalee',
		'Nocturne',
		'Nunu',
		'Olaf',
		'Orianna',
		'Ornn',
		'Pantheon',
		'Poppy',
		'Pyke',
		'Quinn',
		'Rakan',
		'Rammus',
		'RekSai',
		'Renekton',
		'Rengar',
		'Riven',
		'Rumble',
		'Ryze',
		'Sejuani',
		'Shaco',
		'Shen',
		'Shyvana',
		'Singed',
		'Sion',
		'Sivir',
		'Skarner',
		'Sona',
		'Soraka',
		'Swain',
		'Syndra',
		'TahmKench',
		'Taliyah',
		'Talon',
		'Taric',
		'Teemo',
		'Thresh',
		'Tristana',
		'Trundle',
		'Tryndamere',
		'TwistedFate',
		'Twitch',
		'Udyr',
		'Urgot',
		'Varus',
		'Vayne',
		'Veigar',
		'VelKoz',
		'Vi',
		'Viktor',
		'Vladimir',
		'Volibear',
		'Warwick',
		'Wukong',
		'Xayah',
		'Xerath',
		'XinZhao',
		'Yasuo',
		'Yorick',
		'Zac',
		'Zed',
		'Ziggs',
		'Zilean',
		'Zoe',
		'Zyra',]
	return random.choice(words).upper()
	
def check(word,guesses,guess):
	status = ''
	matches = 0
	for letter in word:
		if letter in guesses:
			status += letter
		else:
			status += '_'
		
		if letter == guess:
			matches += 1
	if matches > 1:
		print ('Yeah! The word contains', matches,'"' + guess + '"' + 's')
	elif matches == 1:
		print('Yeah! The word contains the letter "' + guess + '"')
	else:
		print('Sorry. The word does not contain the letter "' + guess + '"')

	return status

def main()
  word = get_word
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
	elif len(guess) == 1":
		guesses.append(guess)
		result = check(word),guesses,guess)
		if result == word:
			guessed = True
		else:
			print (result)
	else:
		print('You WRONG')
print('Yes, the name is', word + '! You got it in', len(guesses), 'tries')

main()