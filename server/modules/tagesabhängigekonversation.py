import datetime
import random



def get_time(i):
    now = datetime.datetime.now()
    stunde = now.hour
    nÃ¤chste_stunde = now.hour + 1
    if nÃ¤chste_stunde == 24:
        nÃ¤chste_stunde = 0
    minute = now.minute
    if minute == 0:
        ausgabe = 'Es ist ' + stunde + ' Uhr.'
    elif minute == 5:
        ausgabe = 'Es ist fÃ¼nf nach ' + stunde + '.'
    elif minute == 10:
        ausgabe = 'Es ist zehn nach ' + stunde + '.'
    elif minute == 15:
        ausgabe = 'Es ist viertel nach ' + stunde + '.'
    elif minute == 20:
        ausgabe = 'Es ist zwanzig nach ' + stunde + '.'
    elif minute == 25:
        ausgabe = 'Es ist fÃ¼nf vor halb ' + stunde + '.'
    elif minute == 30:
        ausgabe = 'Es ist halb ' + nÃ¤chste_stunde + '.'
    elif minute == 35:
        ausgabe = 'Es ist fÃ¼nf nach halb ' + nÃ¤chste_stunde + '.'
    elif minute == 40:
        ausgabe = 'Es ist zwanzig vor ' + nÃ¤chste_stunde + '.'
    elif minute == 45:
        ausgabe = 'Es ist viertel vor ' + nÃ¤chste_stunde + '.'
    elif minute == 50:
        ausgabe = 'Es ist zehn vor ' + nÃ¤chste_stunde + '.'
    elif minute == 55:
        ausgabe = 'Es ist fÃ¼nf vor ' + nÃ¤chste_stunde + '.'
    else:
        ausgabe = 'Es ist ' + str(stunde) + ' Uhr ' + str(minute) + '.'
    return ausgabe

def get_day(i):
    now = datetime.datetime.now()
    wochentag = datetime.datetime.today().weekday()
    tage = {0: 'Montag', 1: 'Dienstag', 2: 'Mittwoch', 3: 'Donnerstag', 4: 'Freitag', 5: 'Samstag', 6: 'Sonntag'}
    nummern = {1: 'erste', 2: 'zweite', 3: 'dritte', 4: 'vierte', 5: 'fÃ¼nfte',
                6: 'sechste', 7: 'siebte', 8: 'achte', 9: 'neunte', 10: 'zehnte',
                11: 'elfte', 12: 'zwÃ¶lfte', 13: 'dreizehnte', 14: 'vierzehnte', 15: 'fÃ¼nfzehnte',
                16: 'sechzehnte', 17: 'siebzehnte', 18: 'achtzehnte', 19: 'neunzehnte', 20: 'zwanzigste',
                21: 'einundzwanzigste', 22: 'zweiundzwanzigste', 23: 'dreiundzwanzigste', 24: 'vierundzwanzigste',
                25: 'fÃ¼nfundzwanzigste', 26: 'sechsundzwanzigste', 27: 'siebenundzwanzigste', 28: 'achtundzwanzigste',
                29: 'neunundzwanzigste', 30: 'dreiÃŸigste', 31: 'einunddreiÃŸigste', 32: 'zweiunddreiÃŸigste'}
    ausgabe = 'Heute ist ' + tage.get(wochentag) + ' der ' + nummern.get(now.day) + ' ' + nummern.get(now.month) + '.'
    return ausgabe



def handle(txt, tiane, profile):
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    text = tt.lower()
    now = datetime.datetime.now()
    wochentag = datetime.datetime.today().weekday()
    uhrzeit = now.hour
    if 'wie viel uhr ist es' in text or 'wie spÃ¤t ist es' in text:
        tiane.say(get_time(text))
    if 'welchen tag haben wir' in text or 'welcher tag ist es' in text or 'welcher wochentag ist es' in text or 'welchen wochentag haben wir' in text or 'welches datum haben wir' in text or 'welches datum ist es' in text or 'den wievielten haben wir heute' in text or 'der wievielte ist es' in text:
        tiane.say(get_day(text))
    if uhrzeit >= 19 and uhrzeit <= 23:
        if 'guten morgen' in text:
            tiane.say('Bist du etwa gerade erst aufgewacht?')
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'ja' in antwort_eins or 'ich war mÃ¼de' in antwort_eins or 'ich war halt mÃ¼de' in antwort_eins or 'jetzt bin ich ja wach' in antwort_eins or 'jetzt bin ich jedenfalls wach' in antwort_eins:
                tiane.say('Du solltest wirklich nachts schlafen, sonst bringst du noch deinen Schlafrhytmus durcheinander')
        elif 'guten abend' in text:
            tiane.say('Guten Abend, {}. Hast du heute noch was vor?'.format(tiane.user))
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'TIMEOUT_OR_INVALID' in antwort_eins:
                tiane.say('Ich konnte deine PlÃ¤ne leider nicht verstehen.')
            elif 'nein' in antwort_eins or 'nicht wirklich' in antwort_eins or 'ich bleibe lieber' in antwort_eins or 'ich habe nichts' in antwort_eins:
                tiane.say('Dann genieÃŸe den freien Abend!')
            else:
                tiane.say('Das klingt toll! Ich wÃ¼nsche dir viel SpaÃŸ dabei!')
        elif 'gute nacht' in text:
            tiane.say('Soll ich dich morgen wecken?')
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'TIMEOUT_OR_INVALID' in antwort_eins:
                tiane.say('Ich fÃ¼rchte, ich habe dich nicht ganz verstanden. Soll ich dich morgen frÃ¼h wecken?')
                antwort_zwei = tiane.listen()
                antwort_zwei = tiane_zwei.lower()
                if 'ja' in antwort_zwei or 'weck mich' in antwort_zwei or 'wecke mich' in antwort_zwei or 'ich mÃ¶chte um' in antwort_zwei or 'ich will um' in antwort_zwei or 'bitte um' in antwort_zwei:
                    tiane.start_module(text=antwort_zwei)
                elif 'nein' in antwort_zwei or 'nicht' in antwort_zwei:
                    tiane.say('In Ordnung. Schlaf gut, {}'.format(tiane.user))
            elif 'ja' in antwort_eins or 'weck mich' in antwort_eins or 'wecke mich' in antwort_eins or 'ich mÃ¶chte um' in antwort_eins or 'ich will um' in antwort_eins or 'bitte um' in antwort_eins:
                tiane.start_module(text=antwort_eins)
            elif 'nein' in antwort_eins or 'nicht' in antwort_eins:
                tiane.say('In Ordnung. Schlaf gut, {}'.format(tiane.user))
    if uhrzeit >= 5 and uhrzeit <= 9:
        if 'guten morgen' in text:
            tiane.say('Guten Morgen, {}. Hast du gut geschlafen?'.format(tiane.user))
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'ja' in antwort_eins or 'ich habe gut' in antwort_eins or 'das habe ich' in antwort_eins:
                tiane.say('Das freut mich! Kann ich etwas fÃ¼r dich tun?')
                antwort_zwei = tiane.listen()
                antwort_zwei = antwort_zwei.lower()
                tiane.start_module(text=antwort_zwei)
            elif 'TIMEOUT_OR_INVALID' in antwort_eins:
                tiane.say('Ich hoffe, du bist nicht allzu mÃ¼de.')
            elif 'wie viel uhr ist es' in antwort_zwei or 'wie spÃ¤t ist es' in antwort_zwei:
                tiane.say(get_time(antwort_eins))
        elif 'guten abend' in text or 'gute nacht' in text:
            tiane.say('Hast du etwa noch nicht geschlafen?')
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'nein' in antwort_eins or 'ich hatte besseres zu tun' in antwort_eins or 'ich bin nicht dazu gekommen' in antwort_eins or 'ich bin noch nicht dazu gekommen' in antwort_eins or 'ich bin zu beschÃ¤ftigt' in antwort_eins or 'schlaf ist fÃ¼r die schwachen' in antwort_eins:
                tiane.say('Du solltest wirklich ins Bett gehen! 23 Stunden ohne Schlaf sind nicht gut fÃ¼r deinen KÃ¶rper!')
    elif uhrzeit >= 2 and uhrzeit <= 4:
        if 'guten morgen' in text:
            tiane.say('Schlaf ruhig weiter, es ist noch mitten in der Nacht!')
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            antwort = antwort_eins.replace('aber', (''))
            if 'ich bin wach' in antwort or 'etwas vor' in antwort or 'muss los' in antwort or 'mÃ¼ssen los' in antwort or 'jetzt stehe ich auf' in antwort or 'egal' in antwort:
                tiane.say('Alles klar! Wie wÃ¤re es mit Kaffee oder Tee?')
                antwort_zwei = tiane.listen()
                antwort_zwei = antwort_zwei.lower()
                if 'ja' in antwort_zwei or 'stÃ¼ck bitte' in antwort_zwei or 'mal bitte' in antwort_zwei or 'gerne' in antwort_zwei or 'wÃ¤re jetzt gut' in antwort_zwei:
                    tiane.say('Das ist gut, er wird dich aufwecken.')
                elif 'nein' in antwort_zwei or 'nicht' in antwort_zwei:
                    tiane.say('In Ordnung')
                else:
                    tiane.say('Ich konnte dich leider nicht verstehen. Bist du doch noch zu mÃ¼de?')
        elif 'gute nacht' in text or 'guten abend' in text:
            tiane.say('Hast du etwa noch nicht geschlafen?')
            antwort_eins = tiane.listen()
            antwort_eins = antwort_eins.lower()
            if 'nein' in antwort_eins or 'ich hatte besseres zu tun' in antwort_eins or 'ich bin nicht dazu gekommen' in antwort_eins or 'ich bin noch nicht dazu gekommen' in antwort_eins or 'ich bin zu beschÃ¤ftigt' in antwort_eins or 'schlaf ist fÃ¼r die schwachen' in antwort_eins:
                tiane.say('Du solltest wirklich ins Bett gehen! 23 Stunden ohne Schlaf sind nicht gut fÃ¼r deinen KÃ¶rper!')
            

                              

                
            
        

def isValid(txt):
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    text = tt.lower()
    if 'guten abend' in text or 'guten morgen' in text or 'gute nacht' in text or 'welches datum' in text or 'wie spÃ¤t' in text or 'wie viel uhr' in text or 'wochentag' in text or 'welcher tag' in text or 'welchen tag' in text:
        return True

class Tiane:
    def __init__(self):
        self.local_storage = {}
        self.user = 'Baum'
        self.analysis = {'room': 'None', 'time': {'month': '10', 'hour': '19', 'year': '2018', 'minute': '47', 'day': '19'}, 'town': 'None'}

    def say(self, text):
        print(text)
    def listen(self):
        neuertext = input()
        return neuertext

def main():
    profile = {}
    tiane = Tiane()
    handle('Welcher Tag ist es heute', tiane, profile)

if __name__ == '__main__':
    main()
    
