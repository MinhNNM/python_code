# #cách 1 dùng open
# f=open("pi_digits.txt") 
# contents = f.read()
# print(contents.strip())

# #dùng with open
# with open('pi_digits.txt') as fn:
#     lines=fn.readlines()
# print(lines)

# #tạo file
# filename="programming.txt"
# with open(filename, "w") as fn:
#     fn.write("Python is programming\n")
#     fn.write("hello")

# # tạo file dùng writelines lưu nhiều câu sử dụng dưới dạng danh sách
# filename="test.txt"
# list=["python is programming\n", 'hello python']
# with open(filename, 'w') as fn:
#     fn.writelines(list) 

# # thêm tiếp nội dung vào file thay vì xóa file cũ đi

# filename="test.txt"
# list=["python++"]
# with open(filename, 'a') as fn:
#     fn.writelines(list)


## bài 1 "guest.txt"
# while True:
#     name=input()
#     if name=='quit':
#         break
#     print(f'xin chao {name}')
#     filename='guest.txt'
#     with open(filename, 'a') as fn:
#         fn.write(f'{name}\n')

# # bài 2 "responses.txt"
# while True:
#     res=input()
#     if res=='':
#         break
#     filename='responses.txt'
#     with open(filename, 'a') as fn:
#         fn.write(f'{res}\n')

# # Ngoại lệ trong python
# try:
#     print(5/0)
# except ZeroDivisionError:       #ngoại lệ chi cho 0(bỏ cũng đc)
#     print("You can't divide by zero!")

#bài 3
while True:
    n=input()
    try:
        if int(n)==0:
            break
        print(int(n))
    except ValueError:
        print("ValueError")


def count_words()
    s=input()
    try:
        with open(s) as file:
            line=file.readlines()
        print("yes")
    except FileNotFoundError:
        print(f"the file {s} doesn't exist" )