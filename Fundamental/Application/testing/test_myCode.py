import my_code
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
def test_getResponse():
    receive = my_code.get_response(api_url)
    assert receive.status_code == 200

def test_sum():
    assert 3 == 3