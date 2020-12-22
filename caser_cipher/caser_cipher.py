import nltk
nltk.download('words')
words = nltk.corpus.words.words()
print(type(words))
def count_(sentences):
    w = sentences.split()
    c = 0
    for i in w:
        if i in words or i.upper() in words or i.lower() in words:
            c += 1
    return c

print(count_('hi from the  hello word'))

def encrypt(str, key):
    all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = [(char.lower())for char in all]
    alpha2 = [(char.upper())for char in all]
    tup = tuple(alpha)
    
    stg = ''
    for i in str:
        if int(alpha.index(i))+key >= len(all):
            
            stg += tup.__getitem__(int(0)+key-1)
        
        
        else:
            # print(tup.__getitem__(int(alpha.index(i))+key))

            
            stg += tup.__getitem__(int(alpha.index(i))+key)
        
        if i==' ' or i in['*','-','/','&','^','%','$','#','@','!',':','~']:
            stg+=i
    return stg


def decrypt(str_shiffted, key):
    return encrypt(str_shiffted,-1*key)


# print(encrypt('aa  #@%% @', 5))
print(encrypt('xyz', 2))
# print(encrypt('hello',4))



# print(decrypt('mjqqt', 5))

def hacked(sentence):
    #  encrypted from 1 to 26 
    # for i in range(26):
    pass



if __name__ == "__main__":
    c=0
    for i in range(5):
        x=encrypt(words[i].lower(), i)
        print()
        print( 'Encrypt :',x ,i)
        print('Decrypt ',decrypt(x,i) ,i)
        print('***********')


