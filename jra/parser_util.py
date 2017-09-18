import re
from datetime import datetime
import boto3

BACKET_NAME = 'jradatabucket'

class parse_error(Exception):
	def __init__(self):
		pass

class parser_util:
	def __init__(self):
		self.func_patern = re.compile(r'\(.*\)')
		self.split_pattern = re.compile(r'[\(\)\']')
		self.s3_client = boto3.client('s3')	
		self.s3 = boto3.resource('s3')
		
	def parse_func_params(self, str):
		matched = self.func_patern.search(str)
		if matched:
			params = self.split_pattern.sub('',matched[0]).split(',')
			if len(params) > 0:
				return params
			else :
				raise parse_error
		else :
			raise parse_error

	def trim_clean(self, str):
		return str.strip()

	def parse_weight(self, str):
		if str == '':
			raise ValueError
		try:
			searched = re.search(self.func_patern, str)
			diff = re.sub(r'[\(\)]', '', searched[0])
			weight = re.sub(self.func_patern, '', str)
			try:
				diff = int(diff)
			except:
				pass

			weight = int(weight)
		except:
			raise ValueError

		return weight, diff

	def get_number(self, str):
		try:
			return int(self.trim_clean(str))
		except :
			raise

	def get_float(self, str):
		try:
			return float(self.trim_clean(str))
		except:
			raise

	def s3_folder_check(self, key):
		response = self.s3_client.list_objects(Bucket= BACKET_NAME)

		exist = False
		folder_name = '{}{}'.format(key, '/')
		for content in response['Contents']:
			if content['Key'] == folder_name:
				exist = True
				break
	
		if exist == False:
			bucket = self.s3.Bucket(BACKET_NAME)
			bucket.put_object(Key=folder_name)
		else:
			pass


def parser_util_convert_datestr(date_str):
    try:
        date_str = date_str.replace('日','')
        splited = date_str.split('月')
        today = datetime.now()
        month = splited[0].zfill(2)
        day = splited[1].zfill(2)
        
        converted = '{}{}{}'.format(today.year, month, day)
    except:
        raise ValueError

    return(converted)

func_parser = parser_util()
