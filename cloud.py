# you don't have to use the packages below, it is only a suggestion.
# do not use any other python module unless it is explicitly permitted by the instructor.
from Crypto.Util import Counter
import Crypto.Cipher.AES as AES
from Crypto.Random import get_random_bytes


class Cloud:
    """
    the cloud stores your content encrypted.
    you can add variables and methods to this class as you want.
    """
    def __init__(self, filename, key=get_random_bytes(32), nonce=get_random_bytes(8)):
        """
        Encrypt the content of 'filename' and store its ciphertext at self.ciphertext
        The encryption to use here is AES-CTR with 32 byte key.
        The counter should begin with zero.
        """
        self.key = key
        self.nonce = nonce

        with open(filename, mode="rb") as f:
            self.encrypt_given_text(f.read())

    def encrypt_given_text(self, text):
        self.plain_text = text
        count_file = Counter.new(64, self.nonce)
        crypto = AES.new(self.key, AES.MODE_CTR, counter=count_file)
        self.cipher_text = crypto.encrypt(text)

    def Read(self, position=0):
        """
        Returns one byte at 'position' from current self.ciphertext.
        position=0 returns the first byte of the ciphertext.
        """
        if position >= len(self.cipher_text):
            return None
        return self.cipher_text[position]

    def Write(self, position=0, newbyte='\x33'):
        """
        Replace the byte in 'position' from self.ciphertext with the encryption of 'newbyte'.
        Remember that you should encrypt 'newbyte' under the appropriate key (it depends on the position).
        Return the previous byte from self.ciphertext (before the re-write).
        """
        if position >= len(self.cipher_text):
            return None
        prev_byte = self.Read(position)

        txt_char_array = list(self.plain_text)
        txt_char_array[position] = newbyte
        self.encrypt_given_text("".join(txt_char_array))

        return prev_byte
