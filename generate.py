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
    <div class="category">${cat.name}</div>
    <ul class="groupings">
    % for group in cat.children:
        <li class="group">${grouping(group)}</li>
    % endfor
    </ul>
</%def>
<%def name="grouping(group)">
    <div class="grouptitle">${group.name}</div>
    <ul class="elements">
    % for element in group.children:
        <li class="element">${element}</li>
    % endfor
    </ul>
</%def>

</body>
</html>
"""

#hocked from
#http://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
class DictWrap(object):
  """ Wrap an existing dict, or create a new one, and access with dot notation

  The attribute _data is reserved and stores the underlying dictionary

  args:
    d: Existing dict to wrap, an empty dict created by default
    create: Create an empty, nested dict instead of raising a KeyError

  """

  def __init__(self, d=None, create=True):
    if d is None:
      d = {}
    supr = super(DictWrap, self)  
    supr.__setattr__('_data', d)
    supr.__setattr__('__create', create)

  def __getattr__(self, name):
    if name.startswith('__'):
      return super(DictWrap, self).__getattribute__(name)

    try:
      value = self._data[name]
    except KeyError:
      if not super(DictWrap, self).__getattribute__('__create'):
        raise
      value = {}
      self._data[name] = value

    if hasattr(value, 'items'):
      create = super(DictWrap, self).__getattribute__('__create')
      return DictWrap(value, create)

    return value

  def __setattr__(self, name, value):
    self._data[name] = value

  def __delattr__(self, name):
    if name == '_data':
      self._data = {}
    else:
      del self._data[name]


def main():
    doc = yaml.load(testyaml)
    print mako.template.Template(template).render(categories = [DictWrap(cat) for cat in doc])

    

if __name__ == "__main__":
    main()
