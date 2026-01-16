from question2_part1 import write_to_file
def read_content_from_file(filename):
    write_to_file("write.txt")
    try:
        file=open(filename,"r")
        content=file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)

read_content_from_file("write.txt")