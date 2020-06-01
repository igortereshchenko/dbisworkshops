class TestIndexView:
    @staticmethod
    def test_get_index_html(test_client):
        resp = test_client.get('/')
        assert resp.status_code == 200
        assert resp.data
