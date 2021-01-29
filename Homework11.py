import time
import os


file_path = os.path.join(os.getcwd(), "funcresult.txt")

def timecalc(func):
    start = time.time()
    func()
    end = time.time()
    duration = end - start
    return f"Your function has worked {round(duration,2)} seconds."

@timecalc
def my_func():
    for i in range(10):
        print(i)
        time.sleep(1)

with open("funcresult.txt", "w") as text_file:
    text_file.write(str(my_func))
