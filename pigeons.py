import random
import mimesis

#make red recessive in the future
colors = ['grey', 'white', 'blue', 'black', 'red']
patterns = ['bar', 'barless', 'tchecker', 'checker']
langofnames = ['en']
class pigeon:
    def __init__(self, color1, color2, wingpattern, namey):
        self.color1 = color1
        self.color2 = color2
        self.pattern = wingpattern
        self.name = namey

data = mimesis.Generic('en')
x = pigeon(colors[random.randrange(0,len(colors))],
           colors[random.randrange(0,len(colors))],
           patterns[random.randrange(0,len(patterns))],
           data.personal.full_name())
print ('a {} {} pigeon with {} {} pattern, named {}'.format(data.personal.gender(0,1),x.color1,x.color2,x.pattern,x.name))
print ('they have this to say: \n\n{}: {}'.format(x.name, data.text.quote()))
print ('they drive a {} {}'.format(data.datetime.year(1935,2018),data.transport.car()))
print ('{} runs {}'.format(x.name, data.business.company(),data.business.company_type()))
