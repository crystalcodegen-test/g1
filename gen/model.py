#
# {{model.name}} model
# @author {{author.name}} <{{author.email}}>
#

from django.db import models

class {{name}}(models.Model):
	{{*details}}
	{{name}} = models.{{type}}({{model}})
	{{/details}}
