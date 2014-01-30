Instructions
===============
This issue-generator is used to create Tasks and Sub-Tasks within Jira. The script uses config.py to determine the task/sub-task hierarchy and will generate issues in the Project/FixVersion indicated by the options provided by the user.

##Options
-u: the Jira username of the person generating the tickets

-p: the Jira password for the user

-d: the destination project for the generated tickets

-v: the Fix/Version for each ticket


##Usage
```
	python generator.py -u <username> -p <password> -v <projectversion> -d <destinationProject>
```

##Example

```
	python generator.py -u <username> -p <password> -v projectVersion -d TEST
```