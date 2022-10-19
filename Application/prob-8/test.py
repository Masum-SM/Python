import main
string = main.string
def test_script():
    up = main.make_upper(string)
    assert up == string
def lower_test():
    lw = main.make_lower(string)
    assert lw == string

def captilized_test():
    cp = main.make_capital(string)
    assert cp == string
