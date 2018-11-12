@pytest.fixture()
def setup():
    w = cardgames.War()
    w.handOne.add_card(cardgames.Card())
    return w

def test_equal_hands(setup):
    setup.deal()
    assert len(setup.handOne.cards) == len(setup.handTwo.cards)