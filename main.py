class A:
    def CalculatePersistence(self, x, x_, iterations=0):
        if len(str(x)) == 1:
            print(x)
            print('\nThe Number \'', str(x_),
                  '\' has a Multiplicative Persistence of: ', str(iterations))
            return "No more Multiplications possible"

        items = [int(i) for i in str(x)]

        product = 1

        for j in items:
            product *= j

        if len(str(product)) != 1:
            print(product)

        iterations += 1

        self.CalculatePersistence(product, x_, iterations)


abc = A()
# abc.CalculatePersistence(77, 77)
abc.CalculatePersistence(679, 679)
