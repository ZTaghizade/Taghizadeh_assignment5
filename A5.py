from datetime import datetime
import csv
devices=[]
i=0
i=int(i)
file='Devices.csv'
with open(file, 'w') as f:
    while(True):
        print("Enter the number of your sellection:")
        print("1. list of devices")
        print("2. add new device")
        print("3. edit")
        print("4. delete")
        print("5. Search")
        print("6. Buy device")
        print("0. Exit")
        n=int(input())
        if(n==1):
            if(i==0):
                print("List is empty")
            else:
                print("DEVICES:\n")
                for x in range(i):
                    print("CODE:",devices[x][0],"NAME:",devices[x][1],"PRICE:",devices[x][2])
        elif(n==2):
            flag=True
            devicecode=input("Enter the code of device: ")
            for x in range(i):
                if(devicecode in devices[x][0]):
                    print("This device is exist!")
                    flag=False
            if(flag==True):
                devicecolor=input("Enter the number of device: ")
                deviceprice=input("Enter its price: ")
                devices.append([])
                devices[i].append(devicecode)
                devices[i].append(devicecolor)
                devices[i].append(deviceprice)
                        #f.writelines(devices[i])
                i+=1
        elif(n==3):
            devicecode=input("Enter the code of device: ")
            for x in range(i):
                if(devicecode in devices[x][0]):
                    print(devices[x])
                    print("Enter the number of your sellection: ")
                    print("1. Code")
                    print("2. Name")
                    print("3. Price")
                    n=int(input())
                    if(n==1):
                        devices[x][0]=input("Enter new code: ")
                    elif(n==2):
                        devices[x][1]=input("Enter new name: ")
                    elif(n==3):
                        devices[x][2]=input("Enter new price: ")
        elif(n==4):
            devicecode=input("Enter the code of device: ")
            for x in range(i):
                if(devicecode in devices[x][0]):
                    devices.remove(devices[x])
                    i-=1
                    break
        elif(n==5):
            devicecode=input("Enter the code of device: ")
            for x in range(i):
                if(devicecode in devices[x][0]):
                    print(devices[x])
        elif(n==6):
            devicecode=input("Enter the code of device: ")
            for x in range(i):
                if(devicecode in devices[x][0]):
                    buyername=input("Enter your name please: ")
                    buyerphone=input("Enter your phonenumber: ")
                    print("Name: ",buyername)
                    print("Phonenumber: ",buyerphone)
                    print("Device:\nCODE:",devices[x][0],"NAME:",devices[x][1],"PRICE:",devices[x][2])
                    print("Time: ", datetime.now().time())
                    devices.remove(devices[x])
                    i-=1
                    break
        elif(n==0):
            wr=csv.writer(f,quoting=csv.QUOTE_ALL)
            wr.writerows(devices)
            break