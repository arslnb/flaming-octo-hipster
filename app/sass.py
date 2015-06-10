import os
def foo():
	sass_file = os.path.join(os.path.dirname(__file__), 'sass/_home.sass')
	css_file = os.path.join(os.path.dirname(__file__), 'static/css_home.css')
	shell_cmd = 'sass '+ sass_file +' > ' + css_file
	os.system(shell_cmd)