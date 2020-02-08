import game


def test_hangman(monkeypatch):
    monkeypatch.setattr(game, "words", ["please"])
    iplease = iter("eesalp")
    game.input = lambda s: next(iplease)
    assert game.hangman()
