import hashlib,re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
def hide_pii(text):
    text=re.sub(r"[a-z]+@[a-z]+\.[a-z]+","***@gmail.com",text)
    text=re.sub(r"\d{10}","*********",text)
    return text
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Eamil PII FOUND"
    elif re.search(phone_pattern,text):
        return "Phone PIII FOUND"
f=open("day22_DSA.txt","w")
f.write("hi\n")
f.write("hello\n")
f.write("1234567890\n")
f.write("hi\n")
f.write("999\n")
f.write("text\n")
f.close()

f=open("day22_DSA.txt","r")
lines=f.readline()
f.close()

seen=[]
count_hidden=0
count_safe=0

for line in lines:
    line=line.strip()
    h=make_hash(line)
    if  h in seen:
        print(line,"--> Duplicate files ")
        count_hidden=count_hidden+1
    else:
        seen.append(h)
        result=check_pii(line)
        hidden=hide_pii(line)
        

        print(line,"--> New",result,"hidden",hidden)
        if result =="safe":
            print

        
        