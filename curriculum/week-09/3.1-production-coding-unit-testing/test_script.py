import pytest
import examples

def test_area_calculation():
    assert examples.rectangle_area(10,2) == 20

def test_stopwords():
    sentence = "the quick brown fox"
    stopwords = ['the', 'a']
    assert examples.strip_stopwords(sentence, stopwords) != 'the quick brown fox'

# def test_area_type_handling():
#     with pytest.raises(TypeError):
#         examples.rectangle_area(5,'testing')