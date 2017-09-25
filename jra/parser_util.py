import re
from datetime import datetime
import boto3
import json
import os

BACKET_NAME = 'jradatabucket'

class parse_error(Exception):
	def __init__(self):
		pass

class parser_storage:
	def folder_check(self, root, date, place, no, category):
		pass
	
	def final_odds_exist(self, root, date, place, no, category):
		return False

	def put_data(self, root, date, place, no, category, filename, data):
		pass

class s3_parser_storage(parser_storage):
	def __init__(self):
			self.s3_client = boto3.client('s3')
			self.s3 = boto3.resource('s3')

	def folder_check(self, root, date, place, no, category):
		response = self.s3_client.list_objects(Bucket= BACKET_NAME)

		exist = False
		folder_name = '{}/{}/{}/{}/{}/'.format(root, date, place,no,category)
		for content in response['Contents']:
			if content['Key'] == folder_name:
				exist = True
				break
	
		if exist == False:
			bucket = self.s3.Bucket(BACKET_NAME)
			bucket.put_object(Key=folder_name)
		else:
			pass

	def s3_file_check(self, key):
		response = self.s3_client.list_objects(
			Bucket= BACKET_NAME,
			Prefix=key)
		
		if 'Contents' in response:
			return True
		else :
			return False

	def final_odds_exist(self, root, date, place, no, category):
		key = '{}/{}/{}/{}/{}/9999999999.9.json'.format(root, date, place,no,category)
		return self.s3_file_check(key)

	def put_data(self, root, date, place, no, category, filename, data):
		key = '{}/{}/{}/{}/{}/{}.json'.format(root, date, place,no,category, filename)
		wobj = self.s3.Object(BACKET_NAME, key)
		wobj.put(Body = json.dumps(data, ensure_ascii=False,))

class local_parser_storage(parser_storage):
	def folder_check(self, root, date, place, no, category):
		elements = [root, date, place, str(no), category]
		path = './'

		for element in elements:
			path = path + '/' + element
			if os.path.isdir(path) == False:
				os.mkdir(path)
	
	def final_odds_exist(self, root, date, place, no, category):
		path = '{}/{}/{}/{}/{}/9999999999.9.json'.format(root, date, place,no,category)
		
		return os.path.isfile(path)

	def put_data(self, root, date, place, no, category, filename, data):
		filename = 'tmp/{}/{}/{}/{}/{}.json'.format(date, place, no, category,filename)
		with open(filename, 'w') as wfp:
			json.dump(data, wfp, ensure_ascii = False)

class parser_util:
	def __init__(self):
		self.func_patern = re.compile(r'\(.*\)')
		self.split_pattern = re.compile(r'[\(\)\']')
		self.time_pattern = re.compile(r'[0-9]{2}:[0-9]{2}')
		self.kaisuu_pattern = re.compile(r'[0-9]回')
		self.nichisuu_pattern = re.compile(r'[0-9]日')

		if os.getenv('JRA_PRS_USE_LOCAL', '0') == '1':
			print("Use Local Storage")
			self.storage_controller = local_parser_storage()
		else:
			print("Use S3 Storage")
			self.storage_controller = s3_parser_storage()
		
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

	def parse_time(self, str):
		try:
			searched = re.search(self.time_pattern, str)
			time = re.sub(r'[\(\)]', '', searched[0])
		except:
			raise ValueError

		return searched[0]

	def parse_kaisai(self, str):
		try :
			searched = re.search(self.kaisuu_pattern, str)
			#print(searched[0])
			kaisuu = int(re.sub(r'回', '', searched[0]))
			searched = re.search(self.nichisuu_pattern, str)
			#print(searched[0])
			nichisuu = int(re.sub(r'日', '', searched[0]))
			place = re.sub(self.kaisuu_pattern, '', str)
			place = re.sub(self.nichisuu_pattern, '', place)
			#print(place)
		except:
			raise ValueError

		return kaisuu, nichisuu,place

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

	def folder_check(self, root, date, place, no, category):
		self.storage_controller.folder_check(root, date, place, no, category)

	def final_odds_exist(self, root, date, place, no, category):
		return self.storage_controller.final_odds_exist(root, date, place, no, category)

	def put_data(self, root, date, place, no, category, filename, data):
		self.storage_controller.put_data(root, date, place, no, category, filename, data)

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

def parser_util_convert_timestr_full_and_stamp(time_str):
	try:
		today = datetime.now()
		converted = '{}/{}/{} {}'.format(today.year, today.month, today.day, time_str)
		stamp = datetime.strptime(converted, '%Y/%m/%d %H:%M').timestamp()
	except:
		raise ValueError

	return(converted, stamp)

func_parser = parser_util()
