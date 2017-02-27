"""
	Example on how to use the lib to annoy *insert friends name here* on chat
"""

import random
import time
import traceback

from lib.keywrapper import str_to_key_press, release_keys

# messages you want to spam
_messages = [
	"Wat is het probleem niels\n",
	"Niels kan het niet aan, hij is mentaal te zwak, wenen wenen\n",
	"Dude, zeg het nu gewoon\n",
	"Komt het uit de tent gesprekken\n"
	"NIELS\n",
	"Niels\n",
	"niels\n",
	"hallo\n",
	"psst\n",
	"psst\n",
	"attack\n",
	"kerel\n",
	"doe normaal\n",
	"doe nen salto\n",
	"een vuste in je gat\n",
	"komt nu eindelijk uit die kast\n",
	"Kom uit die kast af, k vraagt nu ni meer\n",
]

if __name__ == '__main__':
	try:
		time.sleep(5)  # give yourself some time to prepare
		while True:
			# time.sleep((random.randrange(1, 1)))
			time.sleep(0.5)
			str_to_key_press(random.choice(_messages))

	except Exception as e:
		traceback.print_exc()
		release_keys()  # prevents stuck keys
