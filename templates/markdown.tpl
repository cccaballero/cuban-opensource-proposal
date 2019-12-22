{% set ns = namespace(category=None, subcategory=None) %} 
# Cuban Open Source Projects

![Cuban Open Source Projects](https://repository-images.githubusercontent.com/192082154/31c31d80-8f7f-11e9-95d0-3cd6467c8181)

[Guide to publish in the list](publish.md)

Awesome list of Cuban open source projects. Just to know what is being openly developed in Cuba...

{%- for project in projects: %}
{%- if project.category != ns.category: %}
{%- set ns.category = project.category %}

## {{project.category}}
{% endif %}
{%- if project.subcategory and project.subcategory != ns.subcategory: %}
{%- set ns.subcategory = project.subcategory %}

### {{project.subcategory}}
{% endif %}
- [{{project.name}}]({{project.url}}): {{project.description}}
{%- endfor %}
