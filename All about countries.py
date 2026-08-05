class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most spoken language in India")

    def type(self):
        print("India is a developing country")

class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan")

    def language(self):
        print("Urdu is the most spoken language in Pakistan")

    def type(self):
        print("Pakistan is a developing country")

obj_ind = India()
obj_pak = Pakistan()

for country in (obj_ind, obj_pak):
    country.capital()
    country.language()
    country.type()
    print("-----------------------------") 
