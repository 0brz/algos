
def prime(fn):
    def wrappep(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
    return wrappep

class FSM_QueryValidator:
    def __init__(self):
        self.init = self.__create_init()

        self.current_state = self.init

    @prime
    def __create_init(self):
        while (True):
            token = yield
            if (token == "select"):
                print("Good")
            else: 
                print("Bad token")

            