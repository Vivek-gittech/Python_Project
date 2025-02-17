import ast
Library_Dict={
    "Title":"1984",
    "Author":"Abc",
    "Member":"3"
}
# with open("E:\Python\Library_system.txt","a")as f:
#         f.write(str(Library_Dict))
def Library_add():
    for i in Library_Dict:
        user=input(f"Enter The {i}")
        Library_Dict[i]=user
    with open("E:\Python\Library_system.txt","w")as f:
        f.write(str(Library_Dict))


def Library_Search(choice,user):
    with open("E:\Python\Library_system.txt","r")as f:
        data=f.readlines()
        for i in data:
            a=ast.literal_eval(i)

            title=a.get("Title")
            author=a.get("Author")
            member=a.get("Member")
            print(title,"\n")

            if(choice=="Title"):
                    if(title==user):
                        print(title)
                        print(author)
                        print(member)
                        break
                    else:
                        print("Not found")
            elif(choice=="Author"):
                    if(author==user):
                        print("Title:",title)
                        print("Author:",author)
                        print("Member:",member)
                        break
                    else:
                        print("Not found")
            else:
                print("Valid Choice")


# def delete():
#     with open("E:\Python\Library_system.txt","r")as f:
#         data=f.readlines()
#         for i in data:
#             a=ast.literal_eval(i)
#             # print(a)
#             title=a.get("Title")
#             author=a.get("Author")
#             member=a.get("Member")
#             # print(title,"\n")
#         if(title=="title"):
#             x=a.title=" "
#             with open("E:\Python\Library_system.txt","w")as f:
#                 f.write(x)
#             print(x)

# delete()


us=input("Enter the Add,Search")
if(us=="Library_add"):
    Library_add()
elif(us=="Library_Search"):
    Ch=input("Enter the Choice:")
    User=input("Enter the Title\ author::")
    Library_Search(Ch,User)