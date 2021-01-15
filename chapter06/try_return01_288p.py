def test():
    print("test(0 first line")
    try: 
        print("try syntax execute")
        return
        print("after return keyword in try syntax")
    except:
        print("except syntax execute")
    finally:
        print("finally syntax execute")
    print("test() last line")

test() 
