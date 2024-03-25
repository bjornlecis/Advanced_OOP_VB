class buiten:

    def __init__(self,naam):
        self.naam = naam
        self.var = "Test"
        self.inner = self.binnen("Test")

    def __str__(self):
        return self.naam
    class binnen:

        def __init__(self,naam):
            self.naam = naam
        def __str__(self):
            return self.naam

o = buiten("Buiten_class")
i = buiten.binnen("Binnen")
print(o)
print(i)


