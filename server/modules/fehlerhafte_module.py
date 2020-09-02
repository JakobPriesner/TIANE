
def isValid(text):
	text = text.lower()
	if 'module' in text and 'fehlerhaft' in text:
		return True
	elif 'module' in text and 'funktionieren' in text and 'nicht' in text:
		return True

def handle(text, tiane, profile):
	faulty_list = []
	for module in tiane.local_storage['modules'].values():
		if module['status'] == 'error':
			faulty_list.append(module['name'])
	print(faulty_list)
	tiane.say('Folgende Module konnten nicht geladen werden: ')
	tiane.say(tiane.enumerate(faulty_list))
	

def enumerate(self, array):
            new_array = [] # array=['Apfel', 'Birne', 'Gemüse', 'wiederlich']
            for item in array:
                new_array.append(item.strip(' '))
                
            ausgabe = ''
            if len(new_array) == 0:
                pass
            elif len(new_array) == 1:
                ausgabe = array[0]
            else:
                for item in range(len(new_array) - 1):
                    ausgabe += new_array[item] + ', '
                ausgabe = ausgabe.rsplit(', ', 1)[0]
                ausgabe = ausgabe + ' und ' + new_array[-1]
            return ausgabe