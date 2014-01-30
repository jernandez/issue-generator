'''
	config.py
	configuration file for jira issue generator
	
	Issues Generated:
		Task: "Identify and acquire datasets"
			Sub-task: "Metadata Creation"
		Task: "Parse and load data into staging area"
			Sub-task: "Build parsing schema"
			Sub-task: "Build staging area tables"
			Sub-task: "Write/Run data parser"
			Sub-task: "Verify parsed data"
		Task: "Prepare datasets for loading into dev/production"
			Sub-task: "Identify table relationships within staging area"
			Sub-task: "Map staging area tables to current dev/prod data model"
		Task: "Deploy to Development Database"
		Task: "Deploy to Production Database"
'''
issues = [
	{
		'issuetype': 'Task',
		'summary': 'Identify and acquire datasets',
		'sub-tasks': [
			{
				'issuetype': 'Sub-task',
				'summary': 'Metadata Creation'
			}
		]
	},
	{
		'issuetype': 'Task',
		'summary': 'Parse and load data into staging area',
		'sub-tasks': [
			{
				'issuetype': 'Sub-task',
				'summary': 'Build parsing schema'
			},
			{
				'issuetype': 'Sub-task',
				'summary': 'Build staging area tables'
			},
			{
				'issuetype': 'Sub-task',
				'summary': 'Write/Run data parser'
			},
			{
				'issuetype': 'Sub-task',
				'summary': 'Verify parsed data'
			}
		]
	},
	{
		'issuetype': 'Task',
		'summary': 'Prepare datasets for loading into dev/production',
		'sub-tasks': [
			{
				'issuetype': 'Sub-task',
				'summary': 'Identify table relationships within staging area'
			},
			{
				'issuetype': 'Sub-task',
				'summary': 'Map staging area tables to current dev/prod data model'
			}
		]
	},
	{
		'issuetype': 'Task',
		'summary': 'Deploy to Development Database'
	},
	{
		'issuetype': 'Task',
		'summary': 'Deploy to Production Database'
	}
]