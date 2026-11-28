import hashlib, re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def hide_pii(text):
    text=re.sub(r"[a-z]+@[a-z]+\.[a-z]+","***@gmail.com",text)
    text=re.sub(r"\d{10}","**********",text)
    return text
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII FOUND"
    elif re.search(phone_pattern,text):
        return " Phone PII FOUND"
    else:
        return "Safe"
def log(massage):
    f=open("day22_projectLog.txt","a")
    f.write(massage +"\n")
    f.close()
f=open("day22_Project.txt","w")
f.write("hi\n")
f.write("x@y.com\n")
f.write("9999999999\n")
f.write("hi\n")
f.write("1111\n")
f.close()

f=open("day22_project.txt","r")
lines=f.readlines()
f.close()
seen=[]
total_save=0
total_spend=0
count=0
safe_count=0
for line in lines:
    line=line.strip()
    h= make_hash(line)
    if h in seen:
        print(line,"---> DUPLICATE SAVE 0.05")
        total_save=total_save+0.5
        count=count+1
        log(f"lines: {line},Total Save:{total_save},count:{count}")
    else:
        seen.append(h)
        result=check_pii(line)
        hidden=hide_pii(line)
        print(line,"--New spend 0.05--",result,"Hidden-->",hidden)
        total_spend=total_spend+0.05
        safe_count=safe_count+1
        log(f"lines:{line},Total spend:{total_spend},Result:{result},Hidden:{hidden},safe count:{safe_count}")

print("Total save",round(total_save,2))
print("Toatl spend",round(total_spend,2))
print("count:",count)
print("safe count",safe_count)