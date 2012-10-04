import yaml
import mako.template

testyaml = """
---
- name: here is category 1
  children:
    - name: here is a group header 1
      children:
        - here is a group element in group header 1
        - here is another group element in group header 1
        - here is a third group element in group header 1
      
    - name: here is group header 2
      children:
        - element
        - element
        - element
      
    - name: here is a group header 3
      children:
        - element

- name: here is category 2
  children:
    - name: here is group header in cagetory 2
      children: 
        - here is an element in category 2
"""



template = """
<html>
<head>
<style>
.category { background-color: #FF69B4;}
.groupings { display: block; }
.grouptitle { background-color: #B0E0E6;}
.elements { display: block; }
.element { background-color: #FCF0AD; }
</style>

</head>
<body>
<div id="affinity">
   % for cat in categories:
      ${category(cat)}
   % endfor
</body>
<%def name="category(cat)">
    <div class="category">${cat['name']}</div>
    <ul class="groupings">
    % for group in cat['children']:
        <li class="group">${grouping(group)}</li>
    % endfor
    </ul>
</%def>
<%def name="grouping(group)">
    <div class="grouptitle">${group['name']}</div>
    <ul class="elements">
    % for element in group['children']:
        <li class="element">${element}</li>
    % endfor
    </ul>
</%def>

</body>
</html>
"""


def main():
    doc = yaml.load(testyaml)
    print mako.template.Template(template).render(categories = doc)

    

if __name__ == "__main__":
    main()
