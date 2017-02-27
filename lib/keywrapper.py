"""
Wrapper around keylib
Provides str_to_keypress and release_keys methods
"""

from lib import keylib as _k_lib

_letter_table = {
	"a": _k_lib.KEY_A,
	"b": _k_lib.KEY_B,
	"c": _k_lib.KEY_C,
	"d": _k_lib.KEY_D,
	"e": _k_lib.KEY_E,
	"f": _k_lib.KEY_F,
	"g": _k_lib.KEY_G,
	"h": _k_lib.KEY_H,
	"i": _k_lib.KEY_I,
	"j": _k_lib.KEY_J,
	"k": _k_lib.KEY_K,
	"l": _k_lib.KEY_L,
	"m": _k_lib.KEY_M,
	"n": _k_lib.KEY_N,
	"o": _k_lib.KEY_O,
	"p": _k_lib.KEY_P,
	"q": _k_lib.KEY_Q,
	"r": _k_lib.KEY_R,
	"s": _k_lib.KEY_S,
	"t": _k_lib.KEY_T,
	"u": _k_lib.KEY_U,
	"v": _k_lib.KEY_V,
	"w": _k_lib.KEY_W,
	"x": _k_lib.KEY_X,
	"y": _k_lib.KEY_Y,
	"z": _k_lib.KEY_Z,
}

_number_table = {
	"0": _k_lib.KEY_0,
	"1": _k_lib.KEY_1,
	"2": _k_lib.KEY_2,
	"3": _k_lib.KEY_3,
	"4": _k_lib.KEY_4,
	"5": _k_lib.KEY_5,
	"6": _k_lib.KEY_6,
	"7": _k_lib.KEY_7,
	"8": _k_lib.KEY_8,
	"9": _k_lib.KEY_9,
}

_special_table = {
	" ": _k_lib.VK_SPACE,
	"\n": _k_lib.VK_RETURN,
	"\r": _k_lib.VK_RETURN,
	".": _k_lib.VK_OEM_PERIOD,
	",": _k_lib.VK_OEM_COMMA,
}


def release_keys():
	"""
	Releases all keys that could be used in this library
	Use this method on exit to prevent stuck keys
	"""
	for k in _letter_table:
		_k_lib.ReleaseKey(k)
	for k in _number_table:
		_k_lib.ReleaseKey(k)
	for k in _special_table:
		_k_lib.ReleaseKey(k)
	_k_lib.ReleaseKey(_k_lib.VK_SHIFT)


def str_to_key_press(s):
	"""
	Tries to convert a string to key presses
	Throws RuntimeError if a character could not be converted
	:type s: str
	:param s: the string to convert to key presses
	"""
	for char in s:
		_try_char_to_keypress(char)


def _try_char_to_keypress(c):
	try:
		_char_to_keypress(c)
	except Exception:
		_handle_keypress_exception(c)


def _handle_keypress_exception(c):
	message = "char: {char}({hex}) Can not be translated to keypress or is not implemented"
	raise RuntimeError(message.format(char=c, hex=hex(ord(c))))


def _char_to_keypress(c):
	if c.isdigit():
		_number_char_to_keypress(c)
	elif c.isalpha():
		if c.islower():
			_letter_char_to_keypress(c)
		else:
			_capital_letter_to_keypress(c)
	else:
		_special_to_keypress(c)


def _number_char_to_keypress(c):
	_press(_number_table[c])


def _letter_char_to_keypress(c):
	_press(_letter_table[c])


def _capital_letter_to_keypress(c):
	_k_lib.PressKey(_k_lib.VK_SHIFT)
	_letter_char_to_keypress(c.lower())
	_k_lib.ReleaseKey(_k_lib.VK_SHIFT)


def _special_to_keypress(c):
	_press(_special_table[c])


def _press(key):
	_k_lib.PressKey(key)
	_k_lib.ReleaseKey(key)


if __name__ == '__main__':
	pass
