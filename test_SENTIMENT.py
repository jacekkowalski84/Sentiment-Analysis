from SENTIMENT import text_conversion

def test_lower ():
    text = "ASDsa"
    got = text_conversion (text)
    expected = ["asdsa"]
    assert got==expected

def test_replace ():
    text = "asd <br /> asd"
    got = text_conversion (text)
    expected = ["asd", "asd"]
    assert got==expected

def test_split ():
    text = "one two\nthree\t"
    got = text_conversion (text)
    expected = ["one","two","three"]
    assert got==expected