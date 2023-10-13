from wa_services.main import wa_receiver2


def test_wa_receiver():
    response = wa_receiver2()
    assert response == None
    pass
