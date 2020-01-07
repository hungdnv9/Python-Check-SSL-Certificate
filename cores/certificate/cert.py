import ssl
import json
import datetime

class Certificate(object):

	def __init__(self, domain):
		self.domain = domain
		self.error = None
		self.exception = ""

	def get(self, timeout=3, port=443):
		""" Return SSL information in JSON format """
		try:
			connector = ssl.create_connection((self.domain, port), timeout)
			context = ssl.create_default_context()
			sock = context.wrap_socket(connector, server_hostname=self.domain)
			self.cert = json.loads(json.dumps(sock.getpeercert()))
			connector.close()

		except Exception as err:
			self.exception = err			
			self.error = True

	def get_exception(self):
		return self.exception
		
	def notBefore(self):
		return "Not Available" if self.error else self.cert["notBefore"]

	def notAfter(self):
		return "Not Available" if self.error else self.cert["notAfter"]

	def remaining(self):
		""" Return the number of remaining days of cert """
		if self.error:
			return "Not Available"
		else:
			gmt_datetime_format = r'%b %d %H:%M:%S %Y %Z'
			expire_datetime = datetime.datetime.strptime(self.notAfter(), gmt_datetime_format)
			current_datetime = datetime.datetime.utcnow()

			remaining = expire_datetime - current_datetime
			return remaining.days




