word = 'hdfhiotrh,hdgdguyhajhsa,gfufgggrfffgffgfgfigbbfwf '
def Parag():
    #word = value.count('')
    if word.count() > 300 :
        return word[:300]
    else:    
        return word[0:]

Parag(word)