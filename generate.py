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
        
- name: here is category 3
  children:
    - name: here is group header in cagetory 2
      children: 
        - here is an element in category 2
        - data
        - data
        
- name: here is category 1
  children:
    - name: here is a group header 1
      children:
        - here is a group element in group header 1
        - here is a third group element in group header 1
      
    - name: here is group header 2
      children:
        - element
        - element
        - element
        - element
      
    - name: here is group header 2
      children:
        - element
        - element
        - element
      
    - name: here is a group header 3
      children:
        - element
        
"""



template = """
<html>
    <head>
        <script type="text/javascript" src="zoom.js"  ></script>
        <style>
            body { background: #000e15; padding-left: 30px; padding-bottom: 30px; }
            h1 { background-color: #FF69B4; margin: 0; padding: 0; margin-left: -5px;}
            .groupings { display: inline-block; }
            .grouptitle { background-color: #B0E0E6;}
            .elements { display: inline-block; }
            .element { background-color: #FCF0AD; }
            
            ul, li { margin: 0; padding: 0; }
            li { list-style: none }
            
            h1, .grouptitle, .element {
                width: 90px;
                height: 85px;
                padding: 14px;
                box-sizing: border-box;
                font-family: sans-serif;
                margin-top: 5px;
                box-shadow: 0px 2px 4px rgba(0,0,0,.5);
                font-size: 8px;
                font-weight: normal;
            }
            
            h1 { margin: 0 auto; }
            
            .category { background: rgba(255,255,255,.1); box-shadow: 0px 3px 5px rgba(0, 0, 0, .5); padding: 6px; min-width: 90px; display: inline-block; margin-right: 30px; margin-top: 40px; vertical-align: top; }
            .group { width: 90px; display: inline-block; vertical-align: top; }
            .clearfix { clear: both; }
        </style>
    </head>
    
    <body>
        <div id="affinity">
           % for cat in categories:
              ${category(cat)}
           % endfor
        </div>
    </body>
    <script type="text/javascript" src="zoom.js"></script>
    <script>
        document.querySelector('#affinity').addEventListener( 'click', function( event ) {
            event.preventDefault();
            zoom.magnify({ element: event.target });
        });
    </script>        
<%def name="category(cat)">
    <div class="category">
        <h1>${cat['name']}</h1>
        <ul class="groupings">
        % for group in cat['children']:
            <li class="group">${grouping(group)}</li>
        % endfor
        </ul>
    </div>
</%def>
<%def name="grouping(group)">
    <div class="grouptitle">${group['name']}</div>
    <ul class="elements">
    % for element in group['children']:
        <li class="element">${element}</li>
    % endfor
    </ul>
</%def>
</html>
"""


def main():
    doc = yaml.load(testyaml)
    print mako.template.Template(template).render(categories = doc)

    

if __name__ == "__main__":
    main()
