import serial
import hashpumpy
ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)


# function to keep reading the serial until completion (final character is >>)
def read_terminal():
    end_symbol= '>>'
    buff =''
    while end_symbol not in buff:
        buff +=str(ser.readline().decode('utf-8'))
    return buff

# print the first prompt
print(read_terminal())

# write a command to require the cat file and the passwd file, no prompt answer because the value is incorrect
#ser.write(str.encode("#fac1d7b8276cf5c2907dcfa92d5f48607fde0db8#cat.txt:passwd\r\n"))
#print(read_terminal())

for i in range(1,10):

    hash_value,txt = hashpumpy.hashpump('96103df3b928d9edc5a103d690639c94628824f5', 'cat.txt', ':passwd',i)
    #print('message = ',type(txt)) # message is of type byte
    #print('hash = ',type(hash_value)) #i hash of type string
    
    #All strings are converted in one long command of bytes format to be sent as serial write command
    print("Command sent for key length = "+ str(i)) 
    print(hash_value.encode('utf-8') + '#'.encode('utf-8') + txt +'\r\n'.encode('utf-8'))
    #encode everything to type "BYTE" before sending over the command line to the UART
    ser.write((hash_value + '#').encode('utf-8') + txt +'\r\n'.encode('utf-8'))
    
    print(read_terminal())
