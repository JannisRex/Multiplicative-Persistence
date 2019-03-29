class A:
    def CalculatePersistence(self, x):
        if len(str(x)) == 1:
            print(x)
            return "abc"

        items = [int(i) for i in str(x)]

        product = 1

        for j in items:
            product *= j

        print(product)

        self.CalculatePersistence(product)


abc = A()
abc.CalculatePersistence(77)
