#!/bin/env/python3
# -*- coding: UTF-8 -*- 
import yaml
import os
import jinja2
from dataclasses import dataclass

@dataclass
class Project:
    '''Project representation.'''
    name: str
    description: str
    category: str
    url:str
    subcategory: str = None

def load_project(path:str):
    f = open(path)
    data = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return Project(**data)

def renderMd(path, projects):
    with open(path) as file_:
        template = jinja2.Template(file_.read())
    return template.render(projects=projects)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    projects_path = os.path.join(path, 'projects')
    file_list=os.listdir(projects_path)
    markdown_template = os.path.join(path, 'templates', 'markdown.tpl')
    projects = []
    
    for project_file in file_list:
        if project_file.endswith('.yaml'):
            project = load_project(os.path.join(projects_path, project_file))
            projects.append(project)

    sorted_projects = sorted(projects, key=lambda project: (project.category, project.subcategory, project.name))

    md = renderMd(markdown_template, sorted_projects)

    with open(os.path.join(path, 'README.md'), "w+") as fh:
        fh.write(md)
