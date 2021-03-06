import re
from collections import Counter
import csv


def reader(filename): #prinimaet imya faila

	regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

	with open(filename) as f: #pichem dannye v f
		log = f.read()

		ips_list = re.findall(regexp, log)

	return ips_list



def count(ips_list):
	count = Counter(ips_list)

	return count


def write_csv(count):

	with open('output.csv', 'w') as csvfile:
		writer = csv.writer(csvfile) #pisatel

		header = ['IP', 'Frequency']
		writer.writerow(header)

		for item in count:
			writer.writerow( (item, count[item]))





if __name__ == '__main__':

	write_csv(count(reader('access.log')))