import os
def get_template_path(path):
        filepath = os.path.join(os.getcwd() ,path)
        if not os.path.isfile(filepath):
                raise Exception("Invalid template path:",filepath)
        return filepath

def get_template(path):
        filepath = get_template_path(path)
        template = open(filepath).read()
        return template

def render_template(template,context):
        return template.format(**context) #kwarg i.e dictioanry


file_ = "templates\email_message.txt"
template = get_template(file_)
context = {
        "name":"Akhil",
        "amount":45,
        "date":None
        }

print(render_template(template,context))
