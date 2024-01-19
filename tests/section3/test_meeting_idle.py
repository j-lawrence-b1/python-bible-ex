from app.section3 import meeting_idle

def test_main():
    meeting_idle.main()
    captured = capsys.readouterr()
    assert captured.out == "2\n115\n"