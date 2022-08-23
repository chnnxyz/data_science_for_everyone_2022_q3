def log_as_error(func):
    def inner(*args, **kwargs):
        print("#"*30 + "ERROR LOG" + 30*"#")
        func(*args, **kwargs)
        print("#"*80)
    return inner

def console_log(msg):
    print(msg)

@log_as_error
def error_log(msg):
    print(msg)
    
