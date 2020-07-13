import pyostracker


def test_update():
    scores = pyostracker.update("zezima")
    assert scores["hiscores"], "update() did not find hiscores"


def test_scores():
    scores = pyostracker.scores("zezima")
    assert scores["hiscores"], "scores() did not find hiscores"
