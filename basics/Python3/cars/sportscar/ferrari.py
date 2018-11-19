class Ferrari():
    def __init__(self, color='red', power=1000):
        self.color = color
        self.power = power

    @classmethod
    def drives(cls):
        print('It\'s a ferrari, it drives  very fast!')


if __name__ == "__main__":
    f = Ferrari('green', 500)
    print(f.color)
    Ferrari.drives()
    f.drives()
