# pymath - Practice Task

Tasks:
1. Write doc strings for all functions present in basicmath/util.py
2. Write test cases in test_cases.py for all functions present in basicmath/util.py
3. Setup Github actions to run CI pipeline when push event is triggered. Write the workflow in actions.yml.Run below jobs:
    - 3.1 Lint the code
    - 3.2 Run test cases

Note:
1. Use pylint to lint the code.
2. Use pytest to test the code.

Deliverables:
1. Screenshot of commits.
2. Screenshot of workflow output.
3. Repository url

Directory structure:
```
├── basicmath
│   ├── __init__.py
│   └── util.py
├── .github
│   └── workflows
│       └── actions.yml
├── README.md
└── test_cases.py
```