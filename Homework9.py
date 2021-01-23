import random
import logging
from datetime import datetime


logging.basicConfig(filename = "module.log", level = logging.DEBUG, filemode = "w", datefmt = datetime.now().strftime('%d/%m/%y %H:%M:%S.%f'), format="%(asctime)s - %(levelname)s: %(message)s")
	
for i in range(10):
	number = random.randint(0, 50)
	if number >= 0 and number <= 9:
		logging.debug(f"The randomly generated number is {number} and it is between 0 and 9.")
	elif number >= 10 and number <= 19:
		logging.info(f"The randomly generated number is {number} and it is between 10 and 19.")
	elif number >= 20 and number <= 29:
		logging.warning(f"The randomly generated number is {number} and it is between 20 and 29.")
	elif number >= 30 and number <= 39:
		logging.error(f"The randomly generated number is {number} and it is between 30 and 39.")
	elif number >= 40 and number <= 50:
		logging.critical(f"The randomly generated number is {number} and it is between 40 and 50.")