SECURE = True # Damit es von fortlaufenden module naufgerufen werden kann

def handle(text, tiane, profile):
    user = text.get('Benutzer')
    tx = text.get('Text')
    tiane.say(tx, user=user)

def isValid(txt):
    return False
