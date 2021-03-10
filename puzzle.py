from py532lib.i2c import*
from py532lib.frame import*
from py532lib.constants import*

class Rfid_pn532:
    def read_uid(self):
        pn532 = Pn532_i2c()
        pn532.SAMconfigure()
        card_data = pn532.read_mifare().get_data()
        data = card_data.hex()
        return data
if __name__ == "__main__":
    print('Aproxime la tarjeta',"\t")
    rf = Rfid_pn532()
    
    print('Imprimiendo su ID... '+rf.read_uid())