import base64

def encode_16(text):
    Msg = text.encode()
    bytedata = base64.b16encode(Msg)
    result = bytedata.decode()
    return result

def decode_16(text):
    Msg = text.encode()
    bytedata = base64.b16decode(Msg)
    result = bytedata.decode()
    return result

def encode_32(text):
    Msg = text.encode()
    bytedata = base64.b32encode(Msg)
    result = bytedata.decode()
    return result

def decode_32(text):
    Msg = text.encode()
    bytedata = base64.b32decode(Msg)
    result = bytedata.decode()
    return result

def encode_64(text):
    Msg = text.encode()
    bytedata = base64.b64encode(Msg)
    result = bytedata.decode()
    return result

def decode_64(text):
    Msg = text.encode()
    bytedata = base64.b64decode(Msg)
    result = bytedata.decode()
    return result

def encode_85(text):
    Msg = text.encode()
    bytedata = base64.b85encode(Msg)
    result = bytedata.decode()
    return result

def decode_85(text):
    Msg = text.encode()
    bytedata = base64.b85decode(Msg)
    result = bytedata.decode()
    return result

message = input("Enter your message here: ")
action = input("For encode = e or for decode = d: ").lower()
if action == "e":
    alg = input("Base16 = 16, Base32 = 32, Base64 = 64, Base85 = 85 : ")
    if alg == "16":
        text = f" Your hash is here : \n {encode_16(message)}"
        print(text)
    elif alg == "32":
        text = f" Your hash is here : \n {encode_32(message)}"
        print(text)
    elif alg == "64":
        text = f" Your hash is here : \n {encode_64(message)}"
        print(text)
    elif alg == "85":
        text = f" Your hash is here : \n {encode_85(message)}"
        print(text)
    else:
        print("Did't worked")
elif action == "d":
    alg = input("Base16 = 16, Base32 = 32, Base64 = 64, Base85 = 85 : ")
    if alg == "16":
        text = f" Your hash is here : \n {decode_16(message)}"
        print(text)
    elif alg == "32":
        text = f" Your hash is here : \n {decode_32(message)}"
        print(text)
    elif alg == "64":
        text = f" Your hash is here : \n {decode_64(message)}"
        print(text)
    elif alg == "85":
        text = f" Your hash is here : \n {decode_85(message)}"
        print(text)
    else:
        print("Did't worked")
else:
    print("It's not working")