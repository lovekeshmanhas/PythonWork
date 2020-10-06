# Multilevel inheritance

class Dad:
    baskeball = 1

class Son(Dad):
    dance = 1
    baskeball = 4
    def isDance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    def isDance(self):
        return f"Jackson yeah!" \
                f"Yes I dance very awesomely {self.dance} no of times"


darry = Dad()
larry = Son()
garry = Grandson()

print(garry.isDance())
print(garry.baskeball)

