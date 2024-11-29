
def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class FSM:
    def __init__(self):
        self.st = self.state_init()
        self.state_from = self.state_from()

    @prime
    def state_init(self):
        while(True):
            tok = yield
            if (tok == "select"):
                self.st = self.state_from
            else:
                print('BAD')
                break

    @prime
    def state_from(self):
        while(True):
            tok = yield
            if (tok == "from"):
                print("[from] OK")
            else:
                print('[from] BAD')
                break

    def send(self, token):
        try:
            self.st.send(token)
        except StopIteration:
            self.stopped = True

def foo():
    while(True):
        try:
            t = yield
            print(t)
        except Exception as exp:
            print(exp)

g = foo()
g.send(None)
g.send("Tr")
