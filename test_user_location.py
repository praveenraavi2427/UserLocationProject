import requests
import asyncio
import pytest
import time

@pytest.mark.asyncio
async def test_post_data_positive_case():
	for user_id in range(502,510) :
		response = requests.post("http://0.0.0.0:80/users?userId="+str(user_id)+"&name=The Rock&city=Los Angeles")
		assert response.status_code == 200

@pytest.mark.asyncio
async def test_post_data_2nd_postive_case():
	for user_id in range(502,510):
		response = requests.post("http://0.0.0.0:80/users?userId="+str(user_id)+"&name=The Rock&city=Los Angeles")
		
		assert response.status_code == 200	

@pytest.mark.asyncio
async def test_put_data_postive_case():
	time.sleep(5)
	for user_id in range(502,510):
		response = requests.post("http://0.0.0.0:80/users?userId="+str(user_id)+"&name=The Rock&city=Los Angeles")
		assert response.status_code == 200

@pytest.mark.asyncio
async def test_put_data_postive_case():
	time.sleep(5)
	for user_id in range(502,510):
		response = requests.put("http://0.0.0.0:80/users?userId="+str(user_id)+"&location=0007")
		assert response.status_code == 200



