import re
tm = {}

tm['__manifest__.py']="""
{
    'name': 'NAME',
    'description': '''DESCRIPTION''',
    'category': 'CATEGORY',
    'version': 'VERSION',
    'depends': [DEPENDS],
    'data': [DATA]
}

"""

def replace_template(**kwargs):
    """
    replace_templace(template=template, replacers=(('a','A'),('b','B')))
    """
    for x in replacers:
        template = re.sub(x[0], x[1], template)
    return template
