from urllib.parse import parse_qs

parameters = parse_qs('q=free+code+repository&oq=free+code+repository', '')
print(parameters)
