#to practice encapsulation and composition

import time as t
import os

UP = 1
DOWN = -1

class Counter:

    def __init__(self, start=0, end=9, current=0, carry_value=1):
        self._start = start
        self._end = end
        self._current = current
        self._up_or_down = UP if self._start < self._end else DOWN
        self._carry_value = carry_value

    @property
    def current_value(self):
        return self._current

    def _rollover(self):
        self._current = self._start
        return self._carry_value
        
    def count_one(self, step=1):
        
        self._current += step * self._up_or_down

        must_rollover = False
        if (self._up_or_down == UP and self._current > self._end) or (self._up_or_down == DOWN and self._current < self._end):
            must_rollover = True
        if must_rollover: return self._rollover()
    
class Clock:

    def __init__(self, current_hour=0, current_minute=0, current_second=0):
        self._hours = Counter(start=0, end=23, current=current_hour, carry_value=1)
        self._minutes = Counter(start=0, end=59, current=current_minute, carry_value=1)
        self._seconds = Counter(start=0, end=59, current=current_second, carry_value=1)

    def __str__(self):
        formatted_str = ""
        aux_ls = [self._hours, self._minutes, self._seconds]
        for aux in aux_ls:
            formatted_str += f"{aux.current_value}" if (aux.current_value >= 10) else f"0{aux.current_value}"
            formatted_str += ':'
        return formatted_str[:-1] #returning representation without exceeding ':' char

   
    def tick(self):
        if self._seconds.count_one(step=1) == 1:
            if self._minutes.count_one(step=1) == 1:
                if self._hours.count_one(step=1) == 1:
                    return 1
"""
class Calendar:

    def _generate_day_counter(day=1, month=1, year=2000):
        pass
        

    def __init__(self, current_day=1, current_month=1, current_year=2000):
        self._days = self._generate_day_counter(current_day, current_month, current_year)
        self._months = Counter(start=1, end=12, current=current_month, carry_value=1)
        self._years = Counter(start=1, end=3000, current=current_year, carry_value=1)

    def _rollover(self):
"""

def main():
    
    regular_clock = Clock(12, 22, 30)

    while(True):

        os.system('clear')
        print(regular_clock)

        t.sleep(1)
        
        regular_clock.tick()

if __name__ == "__main__":
    main()