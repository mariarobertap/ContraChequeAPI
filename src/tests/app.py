from server.instace import server

app = server.app
def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Testing, Flask!'

test_index_route()