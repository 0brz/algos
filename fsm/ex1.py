"""

3 states:
    wake_up->need_homework
    need_homework -> [lunch, homework_done, homework_fail]
    lunch -> need_homework
    homework_done -> school
    homework_fail -> playing_pc
    
    school -> bed
    playing_pc -> bed

    bed->wake_up
    
"""

class fsm3:
    __bed = ('bed', ['school'])
    __school = ('school', ['home'])
    __home = ('home', ['bed'])

    def __init__(self):
        self.home = 5

    def next(self, state):
        if (state == self.__bed):
            return self.__bed[1][0]
        elif (state == self.__school):
            return self.__school[1][0]
        elif (state == self.__home):
            return self.__home[1][0]

def prime_wrap(fn):
    def wrapper(*args, **kwargs):
        v = fn(args, kwargs)
        #v.send(None)
        return v

    return wrapper

class fsm_t:
    def __init__(self):
        print("fsm_t.init")
        self.state_home = self._create_home_state()
        self.state_bed = self._create_bed_state
        self.state_school = self._create_school_state()
        self.current_state = self.state_home
        
        self.wakeup_state = self._create_wakeup_state()
        self.need_homework_state = self._create_needhomework_state()
        self.lunch_state = self._create_lunch_state()
        self.homework_done_state = self._create_needhomework_done_state()

    def send(self, token):
        self.cur_state.send(token)

    def is_valid(self):
        t = 5

    def current(self):
        return 

    @prime_wrap
    def _create_lunch_state(self):
        while(True):
            token = yield
            if (token == 'lunch'):
                self.current_state = self.lunch_state
            else: break

    @prime_wrap
    def _create_lunch_state(self):
        while(True):
            token = yield
            if (token == 'lunch'):
                self.current_state = self.lunch_state
            # !!!!
            if (token == 'need_homework'):
                self.current_state = self.need_homework_state
            else: break
    
    @prime_wrap
    def _create_needhomework_done_state(self):
        while(True):
            token = yield
            if (token == 'homework_done'):
                self.current_state = self.homework_done_state
            else: break

    @prime_wrap
    def _create_needhomework_state(self):
        while(True):
            token = yield
            if (token == 'need_homework'):
                self.current_state = self.need_homework_state
            else: break

    @prime_wrap
    def _create_wakeup_state(self):
        while(True):
            token = yield
            if (token == 'wake_up'):
                self.current_state = self.wakeup_state
            else: break

    @prime_wrap
    def _create_school_state(self):
        while(True):
            token = yield
            if (token == 'school'):
                self.current_state = self.state_school
            else: break

f = fsm3()
print(f.next('home'))
