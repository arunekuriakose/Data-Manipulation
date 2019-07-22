#..............................................................................
#PREDICTLY TECH LABS CODING TEST
import csv
import re
import fileinput
#..............................................................................
#Creating email template and writing it to demo.txt file:
with open('sample_email.csv', mode='r') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=','))
    with open("EMAIL_TEMPLATE.txt",'w',encoding='utf-8')as f:
        for i in range(1,50):
            s=reader[i]
            f.write(f'Email To:{s[10]}\n')
            f.write(f'Subject Line:{s[11]}\n')
            f.write(f'Hi {s[0]} {s[1]},\n')
            f.write(f'{s[12]}\n')
            f.write('Thanks,\nRob Willison.\n')
            f.write('\n')
#..............................................................................
#Creating temp file containing email body for manipulation:
    with open("temp1.txt",'w',encoding='utf-8')as f1:
        for i in range(1,50):
            s=reader[i]
            f1.write(f'{s[12]}\n')  
#..............................................................................
#Manipulating email and number for extraction:          
with fileinput.FileInput("temp1.txt", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("[at]",'@'), end='')
        print(line.replace(" [at] ",'@'), end='')
        print(line.replace(" [at] ",'@'), end='')
        print(line.replace("(",''), end='')
        print(line.replace(") ",'-'), end='')
#..............................................................................
#Deleting of duplicate data from temp file:
lines_seen=set()
outfile=open("tempdata.txt","w")
for line in open("temp1.txt","r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
#..............................................................................  
#Extracting email number and writing to EMAIL_NUMBERS.csv:
re_pattern=re.compile(r'[\d]{3}-[\d]{3}-[\d]{4}')
with open("tempdata.txt") as ph_in:
    with open('EMAIL_NUMBERS.csv', 'w') as ph_out:
        writer = csv.writer(ph_out)
        for pline in ph_in:
            phone_list = re_pattern.findall(pline)
            if phone_list:    
                writer.writerow(phone_list)
#..............................................................................                
#Extracting email addresses and writing to EMAIL_ADDRESSES.csv:
re_pattern=re.compile(r'[\w\.-]+@[\w\.-]+')
with open("tempdata.txt") as em_in:
    with open('EMAIL_ADDRESSES.csv', 'w') as em_out:
        writer = csv.writer(em_out)
        for line in em_in:
            match_list = re_pattern.findall(line)
            if match_list:    
                writer.writerow(match_list)
#..............................................................................
#Console Verification:
#Display:Email Template                
f=open("EMAIL_TEMPLATE.txt")
print(f.read())

#Display:Email Addresses 
with open('EMAIL_ADDRESSES.csv', mode='r') as emailout:
    email = list(csv.reader(emailout, delimiter=','))
    print(email)
    
#Display:Email Numbers 
with open('EMAIL_NUMBERS.csv', mode='r') as phoneout:
    phone = list(csv.reader(phoneout, delimiter=','))
    print(phone)
    
#..............................................................................          