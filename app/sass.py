import os
def foo():
	sass_file = os.path.join(os.getcwd(), 'app/sass/_home.sass')
	css_file = os.path.join(os.getcwd(), 'app/static/css_home.css')
	shell_cmd = 'sass '+ sass_file +' > ' + css_file
	os.system(shell_cmd)