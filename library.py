import mysql.connector as msql
cn=msql.connect(host='localhost',
                user='root',
                passwd='')
cur=cn.cursor()
cur.execute("create database if not exists library")
cur.execute("use library")
cur.execute("create table book(bname varchar(50),bcode varchar(50),total int,subject varchar(50))")
cur.execute("create table issue(name varchar(50),rno int,bcode varchar(50),idate varchar(50))")
cur.execute("create table submit(name varchar(50),rno int,bcode varchar(50),sdate varchar(50))")
cn.commit()
print("""------------------------------------------
              LIBRARY MANAGEMENT SYSTEM
      ---------------------------------------------""")
print("WELCOME TO OUR LIBRARY")
def addbook():
    bname=input("Enter name of the book")
    bcode=input("Enter book code")
    tl=int(input("Total books"))
    sub=input("Enter subject")
    cur.execute("insert into book values ('{}','{}',{},'{}')".format(bname,bcode,tl,sub))
    cn.commit()
    print("Data entered successfully")
    main()

def issuebook():
    name=input("Enter your name")
    rno=int(input("Enter roll number"))
    code=input("Enter book code")
    date=input("Enter date(Year-Month-Day)")
    cur.execute("insert into issue values ('{}',{},'{}','{}')".format(name,rno,code,date)) 
    cn.commit()
    print("Book issued to",name)
    bookup(code,-1)
    main()

def submit():
    name=input("Enter your name")
    rno=int(input("Enter roll number"))
    code=input("Enter book code")
    date=input("Enter date(Year-Month-Day)")
    cur.execute("insert into submit values ('{}',{},'{}','{}')".format(name,rno,code,date))
    cn.commit()
    print("Book submitted from",name)
    bookup(code,1)
    main()
    
def bookup(code,u):
    cur.execute("select TOTAL from book where BCODE=%s",(code,))
    myresult=cur.fetchone()
    t=myresult[0]+u
    cur.execute("update book set TOTAL = %s where BCODE = %s",(t,code))
    cn.commit()
    main()
    
def deletebook():
    ac=input("Enter book code")
    cur.execute("delete from book where BCODE=%s",(ac,))
    cn.commit()
    print("Data deleted successfully")
    main()
    
def dispbook():
    cur.execute("select * from book")
    myresult=cur.fetchall()
    for i in myresult:
        print("Book Name:",i[0])
        print("Book Code:",i[1])
        print("Total:",i[2])
        print("Subject:",i[3])
    main()
    
def main():
    print("1.Add Book")
    print("2.Issue Book")
    print("3.Submit Book")
    print("4.Delete Book")
    print("5.Display Book")
    print("6.Exit program")
    choice=int(input("Enter your choice:"))
    if choice==1:
        addbook()
    elif choice==2:
        issuebook()
    elif choice==3:
        submit()
    elif choice==4:
        deletebook()
    elif choice==5:
        dispbook()
    elif choice==6:
        print("Thank you and have a great day ahead")
    else: 
        print("Invalid choice")
        main()
        
def password():
    import random
    ps=random.randint(000000,100000)
    user=input("Enter Username")
    print("Your password is:",ps)
    verify=int(input("Enter password"))
    if verify==ps:
        print("WELCOME USER")
        main()
    else:
        print("Wrong password,TRY AGAIN!")
        password()
password()
