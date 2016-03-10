def app(env, start_response):
	status = '200 OK'
	query_string = env['QUERY_STRING']
	headers = [
		('Content-Type', 'text/plain')
	]
	args = query_string.replace('&','\n')
	if not args.endswith('\n'):
		args = args + '\n'
	start_response(status, headers)
	return [args]
