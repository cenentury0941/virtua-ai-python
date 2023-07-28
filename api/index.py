from http.server import BaseHTTPRequestHandler

import requests
from requests.auth import HTTPDigestAuth

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		response = requests.get('https://eu-central-1.data.tidbcloud.com/api/v1beta/app/dataapp-BSWBoAYM/endpoint/sandbox_state',auth=HTTPDigestAuth('jN3cMFav', '2b229f3c-baa2-4afa-9fb8-337e3b211c1e'),)

		self.wfile.write(response.text.encode('utf-8'))
		return
