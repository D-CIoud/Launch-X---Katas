# def main():
#     try:
#         configuration = open('C:\\Users\\DCloud\\Desktop\\Launch X\\Modulo 10\\config.txt\\config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")

def main():
    try:
        configuration = open('C:\\Users\\DCloud\\Desktop\\Launch X\\Modulo 10\\config.txt\\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()