import os
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file name{filename}: created successfully!")
    except FileExistsError:
        print(f'File name {filename} already exists!')

    except Exception as E:
        print('an error occured!')

def view_all_files():
    files = os.listdir()
    if not files:
        print('no file found!')
    else:
        print('file in directory!')
        for file in files:
            print(file)    

def delete_file(filename):
    try:
        os.remove(filename)
        print('f{filename} has been deleted successfully!')
    except FileNotFoundError:
        print('file not found')

    except Exception as e:
        print ('an error occured!')

def read_file(filename):
   
   try:
       with open('sample.txt', 'r')as f:
           content = f.read()
           print(f"content of '{filename}':\n{content}")

   except FileNotFoundError:
        print('an error occured!')

   except Exception as e:
       print('an error occured!')

def edit_file(filename):   
    try:
        with open('sample.txt',"a")as f:
            content = input('enter data to add = ')
            f.write(content + "\n")
            print('content added to {filename} successfully!')

    except FileNotFoundError:
         print(f'File name {filename} already exists!')

    except Exception as e:
       print('an error occured!') 

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: creat file')
        print('2: view all file')
        print('3: delete file')
        print('4: read file')
        print('5: edit file')
        print('6: exit ')

        choice = input("Enter your choice(1-6)= ")

        if choice =='1':
            filename = input("Enter the filename to creat = ")
            create_file(filename)

        elif choice =='2': 
            view_all_files

        elif choice =='3':
            filename = input('Enter the name of file you want to delete =')
            read_file(filename)

        elif choice =='4':
            filename = input('enter filename to read= ')
            read_file(filename)

        elif choice =='5':
            filename = input('enter file name to edit=')
            edit_file(filename) 

        elif choice =='6': 
            print('closing the app...')
            break

        else:
            print('in-valid syntax')

if __name__ == "__main__":
    main()           



        






                 

                  