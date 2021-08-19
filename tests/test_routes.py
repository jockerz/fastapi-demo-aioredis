import pytest


# make sure pytest-asyncio is installed

@pytest.mark.asyncio
class TestRoutes:
	async def test_post_success(self, http_client):
		async with http_client as http:
			resp = await http.post('/post', params={
				'key': 'test_key', 'value': 'test_value'
			})

		assert resp.status_code == 200
		assert resp.json()['success'] == True
		assert resp.json()['data'] == {'test_key': 'test_value'}

	async def test_get_success(self, http_client, redis):
		await redis.set('test_get_key', 'test_get_value')

		async with http_client as http:
			resp = await http.get('/get', params={'key': 'test_get_key'})
		
		assert resp.status_code == 200
		assert resp.json()['success'] == True
		assert resp.json()['data'] == {'test_get_key': 'test_get_value'}

	async def test_get_not_found(self, http_client):
		async with http_client as http:
			resp = await http.get('/get', params={'key': 'test_not_avail'})
		
		assert resp.status_code == 200
		assert resp.json()['success'] == False
