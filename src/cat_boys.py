from requests import get


class CatBoys:
	def __init__(self):
		self.api = "https://api.catboys.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def ping(self):
		return get(
			f"{self.api}/ping", headers=self.headers).json()
	
	def get_endpoints(self):
		return get(
			f"{self.api}/endpoints",
			headers=self.headers).json()
	
	def get_random_image(self):
		return get(
			f"{self.api}/img", headers=self.headers).json()
	
	def get_random_baka_gif(self):
		return get(
			f"{self.api}/baka", headers=self.headers).json()
	
	def get_random_8ball_saying(self):
		return get(
			f"{self.api}/8ball", headers=self.headers).json()
	
	def get_random_number(self):
		return get(
			f"{self.api}/dice", headers=self.headers).json()
	
	def get_random_cat_boy_saying(self):
		return get(
			f"{self.api}/catboy", headers=self.headers).json()
