# st_SFTP_encdec1.py ver:001
# 20240617 alpha aforres@gmail.com
# 20240707 beta
# 20240721 ver:1

import pyAesCrypt
import os
import paramiko
from path import Path
import datetime
import streamlit as st

st.title("test")
paramiko.util.log_to_file("paramiko.log")
host,port = "ssh.pythonanywhere.com",22
    
transport = paramiko.Transport(host,port)
username = "alastair"
password = 'q548*"rBa)kC>6xZ;VPFp-'  #changed 20240628

#bufferSize = 64 * 1024
#key = "Qa23cf542!28&^9856"

#pyAesCrypt.encryptFile("/mount/src/northward_bound.txt", "/mount/src/EncDec/northward_bound.txt.aes", key)

transport.connect(username=username,password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Upload from my desktop to pythonanywhere, London, UK
uploaded_file = st.file_upload("Choose a file")
if uploaded_file is not None:
    string_data = uploaded_file.getvalue()
    st.write(string_data)
#uploaded_file = "northward_bound.txt.aes"
localpath = uploaded_file
filepath = "/home/alastair/encrypted/" + uploaded_file
sftp.put(localpath,filepath)
#
# Download from pythonanywhere, London, UK to my desktop
#file2 = "southward_bound.txt"
#filepath = "/home/alastair/encrypted/" + file2
#localpath = file2
#sftp.get(filepath,localpath)

# Upload from my desktop to pythonanywhere, London, UK
#bufferSize = 64 * 1024
#key = "Qa23cf542!28&^9856"
#pyAesCrypt.encryptFile("southward_bound.txt", "southward_bound.txt.aes", key)
# 
# # Close
if sftp: sftp.close()
if transport: transport.close()
    

    
