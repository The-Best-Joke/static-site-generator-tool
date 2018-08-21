from jinja2 import Environment, FileSystemLoader
import os, json, sys, re

class Generator():
	def __init__(self):
		self.this_dir = os.path.dirname(os.path.abspath(__file__))
		self.environment = Environment(loader=FileSystemLoader(self.this_dir + "/templates"),trim_blocks=True)
		self.config = {}

	def include_configs(self, command_set, command_dict):
		self.include_config("configs/main.json", "main", command_dict, command_set)
		# No Education condition
		if ('noeducation' in command_set):
			self.include_config("configs/education.json", "noeducation")
		else:
			self.include_config("configs/education.json")
		# No Employment condition
		if ('noemployment' in command_set):
			self.include_config("configs/employment.json", "noemployment")
		else:
			self.include_config("configs/employment.json")
		# No Projects condition
		if ('noprojects' in command_set):
			self.include_config("configs/projects.json", "noprojects")
		else:
			self.include_config("configs/projects.json")
		# No Awards condition
		if ('noawards' in command_set):
			self.include_config("configs/awards.json", "noawards")
		else:
			self.include_config("configs/awards.json")
		# No Activities condition
		if ('noactivities' in command_set):
			self.include_config("configs/activities.json", "noactivities")
		else:
			self.include_config("configs/activities.json")
		# No Experience condition
		if ('noexperience' in command_set):
			self.include_config("configs/experience.json", "noexperience")
		else:
			self.include_config("configs/experience.json")

	def include_config(self, path, command=None, command_dict=None, command_set=None):
		with open(path) as config:
			data = json.load(config)
		if (command == "main"):
			if ("color_code" in command_dict):
				data['color'] = command_dict['color_code']
				print(data['color'])
			if ("title" in command_dict):
				data['title'] = command_dict['title']
			if ("subtitle" in command_dict):
				data['subtitle'] = command_dict['subtitle']
			if ("noabout" in command_set):
				data['about'] = ""
		elif (command == "noabout"):
			data['about'] = ""
		elif (command == "noeducation"):
			data['schools'] = ""
		elif (command == "noemployment"):
			data['jobs'] = ""
		elif (command == "noprojects"):
			data['projects'] = ""
		elif (command == "noawards"):
			data['awards'] = ""
		elif (command == "noactivities"):
			data['activities'] = ""
		elif (command == "noexperience"):
			data['experiences'] = ""
		self.config.update(data)

	def generate_resume(self):
		html = self.environment.get_template('template.html').render(self.config)
		with open("resume.html", "w") as index:
			index.write(html)

def initialize(command_set, command_dict):
	b = Generator()
	b.include_configs(command_set, command_dict)
	b.generate_resume()

if __name__ == '__main__':

	command_set = set()
	command_dict = {}

	for i in sys.argv:
		if re.match('^resume-color=[?#][0-9a-fA-F]+', i):
			color_code = i[13:]
			command_dict['color_code'] = color_code
			command_set.add('color_code')
		elif re.match('^font-family=[a-fA-F_]+', i):
			font_family = i[12:]
			command_dict['font_family'] = font_family
			command_set.add('font_family')
		elif re.match('^title=[a-fA-F_]*', i):
			title = i[6:]
			command_dict['title'] = title
			command_set.add('title')
		elif re.match('^subtitle=[a-fA-F_]*', i):
			subtitle = i[9:]
			command_dict['subtitle'] = subtitle
			command_set.add('subtitle')
		elif re.match('^noabout', i):
			command_set.add('noabout')
		elif re.match('^noeducation', i):
			command_set.add('noeducation')
		elif re.match('^noemployment', i):
			command_set.add('noemployment')
		elif re.match('^noprojects', i):
			command_set.add('noprojects')
		elif re.match('^noawards', i):
			command_set.add('noawards')
		elif re.match('^noactivities', i):
			command_set.add('noactivities')
		elif re.match('^noexperience', i):
			command_set.add('noexperience')


	initialize(command_set, command_dict)
