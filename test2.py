from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("test.j2")  

content = template.render(name='test_name', age='18', country='China')

with open('./test.conf','w') as fp:
	fp.write(content)
