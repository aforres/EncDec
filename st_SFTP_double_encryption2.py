# st_SFTP_double_encryption.py ver:001
# 20240617 aforres@gmail.com
# 20240707
import pyAesCrypt
import os
import paramiko
from path import Path
import datetime
import streamlit as st

st.title("AES-256 Encryption")
st.write("Wait until 'Finished.... ' appears on the screen in just a few seconds")
def run_func():
    
    paramiko.util.log_to_file("paramiko.log")
    host,port = "ssh.pythonanywhere.com",22
    
    #host = st.text_input("host address",placeholder="ssh.pythonanywhere.com")
    #port = int(22)  ##st.number_input("port") #"ssh.pythonanywhere.com")
    
    transport = paramiko.Transport(host,port)
    username = "alastair"
    password = 'q548*"rBa)kC>6xZ;VPFp-'  #changed 20240628
    
    #username = st.text_input("username")
    #password = st.text_input("password")

    transport.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Upload from my desktop to pythonanywhere, London, UK
    bufferSize = 64 * 1024
    key = "Qa23cf542!28&^9856"
    pyAesCrypt.encryptFile("outward_bound.txt", "outward_bound.txt.aes", key)
    
    file = "outward_bound.txt.aes"
    localpath = "C:/Users/aforr/Thonny/MM/" + file
    filepath = "/home/alastair/encrypted/" + file
    sftp.put(localpath,filepath)
    
    #
    # Download from pythonanywhere, London, UK to my desktop
    #pyAesCrypt.encryptFile("/home/alastair/encrypted/southward_bound.txt", "/home/alastair/encrypted/southward_bound.txt.aes", encpassword)    
    #file = "/home/alastair/encrypted/southward_bound.txt.aes"

#     filepath = "/home/alastair/encrypted/" + file
#     localpath = "C:/Users/aforr/Thonny/MM/" + file
#     sftp.get(filepath,localpath)
#     
#     pyAesCrypt.encryptFile("southward_bound.txt", "southward_bound.txt.aes", encpassword)    
#     file = "southward_bound.txt.aes"

    
    # 
    # # Close
    if sftp: sftp.close()
    if transport: transport.close()
    
if __name__ == "__main__":
    run_func()
    st.markdown("Finished encrypting (AES-256) then SFTP-ing that now double-encrypted file 'outward_bound' from Australia to the UK")
    #st.write("also finished encrypting (AES-256) and SFTPing another file from London back to Australia")
