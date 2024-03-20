name=input("Enter your name: ")
print(f"Hello {name}")

print(f"\n Now {name} ,we are going to play KBC!! ")

ques=[["which language is used to create facebook?","java","french","javascript","php",4],
      ["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
      [ "Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism",4],
      [" September 27 is celebrated every year as","International Literacy Day","National Integration Day","World Tourism Day","Teachers' Day",3],
      ["Who is the author of the epic 'Meghdoot'?","Vishakadatta","Valmiki","Banabhatta","Kalidas",4],
      ["Who is the author of the book 'Amrit Ki Ore'?","Mukesh Kumar","Narendra Mohan","Upendra Nath","Nirad",2],
      ["World Health Day is observed on","Apr 7","Mar 6","Mat I5","Apr 28",1],
      ["Pongal is a popular festival of which state?","Kerala","Tamil Nadu","Andhra Pradesh","Karnataka",2],
      ["Which is the capital of India?","New Delhi","Mumbai","Chennai","Bangalore",1],
      ["Which is the largest state in India?","Telangana","Tamil Nadu","Karnataka","Andhra Pradesh",3],
      ["Which of the following Muslim festivals is based on the 'Holy Quran' ?","Id -ul-Zuha","Id -ul-Fitr","Bakri-id","Moharram",1],
      ["The first month of the Indian national calendar is","Magha","Chaitrera","Ashadha","Vaishakha",2],
      ["Which of the following is not a dance from Kerala?","Kathakali","Mohiniattam","Ottan Thullal","Yaksha Gana",4],
      ["Rath Yatra is famous festival" ,"Ayodhya","Mathura","Dwaraka","Puri",4],
      ["Central Salt and Marine Chemicals Research Institute is located at","Ahmedabad","Bhavnagar","Gandhinagar","Panaji",4],
      ["Nandyal is situated in","Karnataka","AndhraPradesh","Maharashtra","Madhya Pradesh",1],
]

levl=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]

for i in range(len(ques)):
    que=ques[i]
    print(f"\nQues is for Rs.{levl[i]}")
    print(f"\nQuestion {i+1}: {ques[i][0]}")
    print(f"a.{que[1]}     b.{que[2]} ")
    print(f"c.{que[3]}     d.{que[4]}")
    reply=int(input("\nEnter your answer(1-4) or 0 to quit: "))
    if(reply==0):
        money=levl[i-1]
        break
    if(reply==que[-1]):
        print(f"\nCorrect Answer,You have won Rs.{levl[i]}")
        if i==0:
            money=1000
        elif i==1:
            money=2000
        elif i==2:
            money=3000
        elif i==3:
            money=5000
        elif i==4:
            money=10000 
        elif i==9:
            money=320000
        elif i==14:
            money=7500000
        elif i==16:
            money=75000000
    else:
        print("Wrong Answer")
        break

print(f"\n\nThe money that you will be credited is {money}")