def Parag(value,arg):
    word = value.count('')
    if word > 300 :
        return word[:300]
    else:    
    return word[0:]
#width == 30
string1 = 'titus njguna njonjo was born in garissa county 2 yeats ago with a profoicgdjhbvb hfgee gettin 330 marks in kcpe and 400 in kcsew'
pass
print(string1[:99])
class dog():
    #global attribute
    species = "canine"
    #instance accessible attribute
    def __init__(self,breed,name):
        self.name = name
        self.breed = breed
doty = dog("husky","sammi")
pass

#print(doty.breed, doty.name)        

class person():
    def __init__(self,name):
        self.name = input("Whats your name?:")
pass
    
#person1 =person()  
  
#print(person1.name )

#getters and setters
class dog():
    name = 'kartelo'
        
    def setName(self,new_name):
        self.name = new_name
    def getName(self):
        self.name 
        pass
#antelo = dog()
#antelo.setName("niggah")
#print (antelo.getName())
#class animal():
#     species = 'Fedora'
#     def setName(self,New_Species):
 #        self.species = New_Species
#     def getName(self):
 #        self.species
#lion = animal()
#lion.setName("feline")
#print(lion.getName())      

#class person():
#   age = 0
 #   def __init__(self,age,name):
#        self.name = name
 ##   def setName(self,New_age):
   #     self.age =New_age
 #   def getName(self):
   #     self.age
#persona2 = person(0,"Peter")

#persona2.setName(input("Age:"))
#print ("You are",persona2.getName(),"Years old")       

#inheritance from multiple classes
class DtDobie():
    price = "500usd"
    pass
class Automibe():
    def __init__(self,year,models,color):
        self.year,self.models,self.color = year, models,color
class merc(DtDobie, Automibe):
    def __init__(self,year,models,color,engine):
        self.engine = engine
        Automibe.__init__(self,"merc",year,models)
toyota = merc("2015","E350","blue","three liters")
print(toyota.price, toyota.year,toyota.engine,toyota.color) 
