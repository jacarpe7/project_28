### Quality Policy

**GitHub Workflow** 
  > We will maintain a develop branch. The develop branch will be the branch where we merge all completed UserStories by a pull request. This will be enforced by github settings. Each user story will have its own branch, each task  will be created on its associated story branch. When a task is complete, it is then PR'd on github (with no review required). This is to ensure that github will mark the branch as 'merged', and better facilitate organization.

>The name of the branch will follow 'US#', where the # will be the one assigned on the taiga board. When a developer assigns themselves a task, they then branch from the UserStory branch, and follows the convention of 'US#-Task#', where the numbers also correspond with the taiga board. 

>We will try to ensure develop doesn't break, but when it does, a seperate branch in the form of Fix-#, where # is the current bug fix.

>Each commit message needs to describe what you are working on with US# and Task # (also include things like "Unit Test", be descriptive). Read the following for more information on commit messages: https://chris.beams.io/posts/git-commit/

>At least one team member should approve a PullRequest, review it, and the reviewer should not be the member who started
>the pull request.

>Only one team member (Git master) is allowed to do the merge into Master (different person for each Sprint)! In case that person is not available for some reason, someone else is allowed to do it, but please provide a comment in the pull request for it. The Git master is the one who should make sure that all Pull Requests are fast forwards and that all pull requests are approved by someone. Thus, talking to the team and making sure Pull Requests are done correctly. Then the Git master should only push the "merge" button on GitHub.

>Branches will not be deleted after they are completed.


**Unit Tests Blackbox** 
  > Unit Tests will be conducted on a task while the task is in the "ready for test" phase on Taiga (Waiting to be merged into develop)
  
  > All unit tests will be placed in the src.test.java folder.
  
  > Each member will conduct at least 4 unit tests per sprint. (on your code or other people's code)
  
  > Whe committing a Unit Test to a task, you will commit it via 'US# Task# Unit Test: ...'
  
  > Unit tests will be setup to produce jacoco reports
  
  > Unit tests will be focused on areas that are no related to UI elements.


 **Unit Tests Whitebox**
  > Unit Tests will be conducted on a task while the task is in the "ready for test" phase on Taiga (Waiting to be merged into develop)
  
  > All unit tests will be placed in the src.test.java folder.
  
  > Each member will conduct at least 4 unit tests per sprint. (on your code or other people's code)
  
  > Whe committing a Unit Test to a task, you will commit it via 'US# Task# Unit Test: ...'
  
  > Unit tests will be setup to produce jacoco reports
  
  > Unit tests will be focused on areas that are no related to UI elements.
  

**Code Review** 
  #### Developer Review Checklist
  
  Developer Name: _______________________
  
- [ ] My code compiles
- [ ] My code has been developer-tested and includes unit tests that do not fail, if unit testing makes sense
- [ ] My code is properly commented according to Coding Standards
     - [ ] All source code files/class files have banner comments present and filled in
- [ ] All public methods have a method banner comment and/or javadoc comment present and filled in
- [ ] My code is stylistically consistent
     - [ ] Indentations are consistent
     - [ ] Bracket use is consistent (All { appear at the end of a line and } on its own line)
     - [ ] Line length is not excessive (Does not exceed 120 characters)
     - [ ] There is no leftover commented-out code
     - [ ] There are no spelling mistakes
- [ ] I use proper naming conventions
     - [ ] Constants and Enums are in all CAPS
     - [ ] Class names are in upper CamelCase
     - [ ] Variable, Parameter, and Method names are camelCase (Java)
	  OR
     - [ ] Variable, Parameter, and Method names are lowercase with words separated by underscores as necessary to improve readability (Python)
     - [ ] Non-public methods, variables, and constants are prefixed by an underscore _
- [ ] I use exceptions properly where necessary
- [ ] I have eliminated unused imports
- [ ] All class member variables are private
- [ ] I have no duplicate or repetitive code
- [ ] All literal values, except loop indices, are declared as constants (no hard coding)

  > Include a checklist/question list which every reviewer will need to fill out/anser when conducting a review, this checklist (and the answers of course) need to be put into the Pull Request review.
  
#### Reviewer Checklist

Reviewer Name: ________________

- [ ] The code compiles
- [ ] Unit tests are present and correct (do not fail), if unit testing makes sense
- [ ] Comments are comprehensible and appropriate (there are no trivial comments)
- [ ] Comments are neither too numerous nor verbose
- [ ] Comments follow proper Coding Standards 
     - [ ] All source code files/class files have banner comments present and filled in
     - [ ] All public methods have a method banner comment and/or javadoc comment present and filled in
- [ ] The code is stylistically consistent
     - [ ] Indentations are consistent
     - [ ] Bracket use is consistent (All { appear at the end of a line and } on its own line)
     - [ ] Line length is not excessive (Does not exceed 120 characters)
     - [ ] There is no leftover commented-out code
     - [ ] There are no spelling mistakes
- [ ] Proper naming conventions are used
     - [ ] Constants and Enums are in all CAPS
     - [ ] Class names are in upper CamelCase
     - [ ] Variable, Parameter, and Method names are in lower camelCase
     - [ ] Non-public methods, variables, and constants are prefixed by an underscore _
- [ ] Variables, methods, and classes are named appropriately and are self-explanatory
- [ ] Parameterized types have been used appropriately
- [ ] Exceptions have been used appropriately
- [ ] There is no duplicate or repetitive code
- [ ] Frameworks have been used appropriately – methods have all been defined appropriately


**Static Analysis**  
  > Team members will contribute to the massive backlog of StaticAnaylsis bugs by submitting at least 20 SA fixes caught by checkstyle and 20 SA fixes to spotbugs. If there aren't any bugs, then team members will obviously not need to contribute to fixing any more. The dedicated SA fixes will be created on a seperate branch with SA-Task#, where the task number is created with a storyless task on the taiga board. This will be done so that we can accruately show off our progression as we tackle these bugs.
  
**Continuous Integration**  
  > For continuous integration, we will make sure that the Travis CI develop build passes with each pull into the develop branch. At the end of the sprint, we will also make sure that the build passes for the pull into the master branch.
