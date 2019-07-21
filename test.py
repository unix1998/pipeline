from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('results'))
template = env.get_template('test.j2')
content = template.render(name='test_name', age='18', country='China')

print(content)
