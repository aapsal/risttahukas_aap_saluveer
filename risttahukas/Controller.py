from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def loodud_kujund(self, pikkus, laius, korgus):
        return self.model.loo_kujund(pikkus, laius, korgus)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = Controller()
    app.run()