# d={'a':'ش','h':'أ','m':'ة','e':'ث','d':'ي'}
# arabic=list(d.values())
# english=list(d.keys())
# print(arabic)
# print(english)

# user=input('enter arabic letter : ')
# ar_index=arabic.index(user)
# print(english[ar_index])
########################################################

# d={'a':'ش','h':'ا','m':'ة','e':'ث','d':'ي'}
# arabic=list(d.values())
# english=list(d.keys())
# print(arabic)
# print(english)
# en_word=''
# ar_word=input('enter arabic word : ')
# for letter in ar_word:
#     ar_index=arabic.index(letter)
#     en_word+=english[ar_index]
# print(en_word)
###########################################
# d={'a':'ش','h':'ا','m':'ة','e':'ث','d':'ي'}
# arabic=list(d.values())
# english=list(d.keys())
# print(arabic)
# print(english)
# ar_word=''
# en_word=input('enter english word : ')
# for letter in en_word:
#     en_index=english.index(letter)
#     ar_word+=arabic[en_index]
# print(ar_word)
#################################################
d={" ":" ",'q':'ض','Q':'َ','w':'ص','W':'ً','e':'ث','E':'ُ','r':'ق','R':'ٌ','t':'ف','T':'ﻹ','y':'غ','Y':'إ','u':'ع','U':'`','i':'ه','I':'÷','o':'خ','O':'×','p':'ح','P':'؛',
'[':'ج','{':'<',']':'د','}':'>','a':'ش','A':'ِ','s':'س','S':'ٍ','d':'ي','D':']','f':'ب','F':'[','g':'ل','G':'ﻷ','h':'ا','H':'أ','j':'ت','J':'ـ','k':'ن','K':'،',
'l':'م','L':'/',';':'ك',':':':',"'":"ط",'"':'"','z':'ئ','Z':'~','x':'ء','X':'ْ','c':'ؤ','C':'}','v':'ر','V':'{','b':'ﻻ','B':'ﻵ','n':'ى','N':'آ','m':'ة','M':"'",
',':'و','<':',','.':'ز','>':'.','/':'ظ','?':'؟','`':'ذ','~':'ّ'}       
arabic=list(d.values())
english=list(d.keys())
ar_word=''
en_word=''
word=input('enter a word : ')
n=len(word)
counter=0
for letter in word:
    
    if letter in english:
        counter+=1
        en_index=english.index(letter)
        ar_word+=arabic[en_index]
        if counter==n:
            print(ar_word[::-1]) # to reverse arabic word to be spelled from the right
    else:
        ar_index=arabic.index(letter)
        en_word+=english[ar_index]
print(en_word)
        