# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests
import re


# def io_func(logfile_path, result_file_path):
def io_func():
    write_to_file(get_ips(get_failures(read_from_file())))


def write_to_file(content):
    with open("failures.txt", "a") as myfile:
        myfile.writelines(s + '\n' for s in content)


def read_from_file():
    file = open("log_file").read()
    return file.split("\n", -1)


def get_failures(content):
    return [x for x in content if 'HTTP/1.1" 304' in x]


def get_ips(content):
    return [get_ip(line) for line in content]


def get_ip(line):
    return re.search("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", line).group()


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert get_ip(line) == "218.30.103.62"


def test_myfunc_negative():
    # put some logic here that checks that line without 304 code is not goes into filter return
    fails = get_failures(read_from_file())
    error_list = list(filter(lambda x: 'HTTP/1.1" 304' not in x, fails))
    assert len(error_list) == 0

io_func()
test_myfunc_negative()
