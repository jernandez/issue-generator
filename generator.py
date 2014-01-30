'''
	generator.py
	usage: python generator.py

	Generates a set of issues within Jira related to Data Lifecycle project.
	All issues are assigned to the Automatic assignee for the ticket type
	Issues created are pulled from the data structure listed in config.py

'''
from jira.client import JIRA
from optparse import OptionParser
import config, sys

def update_versions(jira, options):

	version_list = []
	project_versions = jira.project_versions(options.project)

	for v in project_versions:
		version_list.append(v.name)

	if options.version not in version_list:
		new_version = jira.create_version(name=options.version, project=options.project)
		print 'New version ' + options.version + ' added to ' + options.project
	else:
		print 'Version ' + options.version + ' already exists within ' + options.project +'. Not addding.'

def generate_issue(options, jira, issue, parent_key):

	issue_dict = {
    	'project': {'key': options.project},
	    'summary': issue['summary'],
	    'issuetype': {'name': issue['issuetype']},
	    'fixVersions': [{'name': options.version}]
	}

	#if a parent key is present, add it to the issue_dict
	if parent_key is not None:
		issue_dict['parent'] = {'key': parent_key}

	issue_resource = jira.create_issue(fields=issue_dict)

	#if this issue has sub-tasks, create all sub-tasks and link them to its parent
	if 'sub-tasks' in issue:
		for subtask in issue['sub-tasks']:
			subtask_resource = generate_issue(options, jira, subtask, issue_resource.key)

	return issue_resource

#####################
#main#
#####################

def main(argv):

	usage = 'usage: %prog [options] arg'
	parser = OptionParser(usage)
	parser.add_option('-u', '--username', help='Your Jira username', action='store', dest='username')
	parser.add_option('-p', '--password', help='Your Jira password', action='store', dest='password')
	parser.add_option('-v', '--version', help='The Fix/Version for all tickets generated', action='store', dest='version')
	parser.add_option('-d', '--destinationProject', help='The destination project for the tickets generated', action='store', dest='project')
	
	(options, args) = parser.parse_args()

	jira_options = {'server': 'https://jira.drillmap.com'}

	jira = JIRA(jira_options, basic_auth=(options.username, options.password))

	update_versions(jira,options)

	for issue in config.issues:
		new_issue = generate_issue(options, jira, issue, None)
		print 'http://jira.drillmap.com/browse/' + new_issue.key

if __name__ == "__main__":
	main(sys.argv[1:])