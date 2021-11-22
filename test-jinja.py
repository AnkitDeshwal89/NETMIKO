from jinja2 import Template

bgp_config = """
router bgp {{local_as}}
  bgp router-id {{router_id}}
  {% for ip in peer1 %}
  neighbor {{ip}} remote-as {{remote_as}}
  {% endfor %}
"""
myiplist = []
for ip in range(1,253):
    myiplist.append("10.1.1."+str(ip))
varforjinja = {
        'local_as':42,
        'router_id':"1.1.1.1",
        'peer1':myiplist,
        'remote_as':44
              }

j2_template = Template(bgp_config)
output = j2_template.render(**varforjinja)
print(output)
