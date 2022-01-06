import time

from utils.Waiting import waiting


class demo:

    @waiting(color='red')
    def long_method(self, timer):
        time.sleep(timer)
        return "Terminé"