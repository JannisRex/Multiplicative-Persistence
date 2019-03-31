class A:
    def CalculatePersistence(self, x, iterations=0):
        if len(str(x)) == 1:
            print(x)
            print('Multiplicative Persitence of: ', str(iterations))
            return "No more Multiplications possible"

        items = [int(i) for i in str(x)]

        product = 1

        for j in items:
            product *= j

        if len(str(product)) > 1:
            print(product)

        iterations += 1

        self.CalculatePersistence(product, iterations)


abc = A()
# abc.CalculatePersistence(77)
abc.CalculatePersistence(679)
