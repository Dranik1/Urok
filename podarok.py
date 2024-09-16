class davana():
    def info(self, nosaukums, cena):
        self.nosaukums=nosaukums
        self.cena=cena

    def output(self):
        print( self.nosaukums, self.cena)

d=davana()
d.info('Lego', 29.99)
d.output()
 