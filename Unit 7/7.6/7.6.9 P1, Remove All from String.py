def remove_all_from_string(stringa,stingb):
    temp=stringa
    while(temp.find(stingb)!=-1):
        temp = temp[:temp.find(stingb)] + temp[(temp.find(stingb)+1):]
    return temp

print remove_all_from_string("hello","l")
