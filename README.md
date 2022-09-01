# technical-interview-apprentices

You will find the resources needed for this technical test in this archive. We expect you to provide the results as a GitHub repository. 

*Hint*: you can begin by creating the repo with this archive content. 
*Hint*: Don't hesitate to ask question, don't worry if something doesn't work and, keep it simple :).  
*Hint*: code enhancement propositions are welcome. 


## school-management

The aim of the first part in this technical test is to implement sound unit-testing for a small toy project. 

**Your mission** is to help the school have a reliable library to compute student's grade at the end of semesters and automate *passes to next year* decisions. To do that, you are in charge of unit testing. 

A student passes a semester if its global mark exceeds a threshold (10). The global mark is computed as the weighted mean of the student's grades in all topics (classes). For instance, if the topic weights for a group `A` are (mathematics : 10, physics: 8, geography: 2) and if student `Alice` of group `A` obtains 13 in mathematics, 12 in physics and 18 in geometry, its global mark is obtained by: $ \frac{13*10 + 12*8 + 18*2}{1*10 + 1*8 + 1*2}$.  

**set-up and structure**
You can find the python project in `school-management` folder . We use `poetry` to initialize it. `poetry` is a tool for dependency management and packaging for `Python projects. **Your first task** is to install poetry on your computer and install the project's dependencies. For that, you need to follow the instructions in the documentation: https://python-poetry.org/docs/

When `poetry` is installed, you can run `make install` at the `school-management` folder to install the project's dependencies. 

As you can remark, the `school-management` project is composed by: 
- A `src` folder containing the sources of the library. The source code is within `src/school-management` that contains two modules:
    - **models** containing classes permitting to describe a class group.
    - **computations** containing modules devised to computations.
- A `test` folder containing unit tests. We will use `pytest` for this library as a testing framework. 

If you had set up `poetry` and correctly installed the dependencies, you can run unit tests by executing `poetry run pytest` at the project root. You will remark that there are two tests. One for `compute_student_topic_grades_mean`, marked as skipped (it is not implemented) and the other for `compute_group_grades` that is not passing. 

- `compute_student_topic_grades_mean` computes the a student's average mark for a given topic. Unfortunately, the developer hasn't implemented the unit test. **Your second task** is to implement **sound** unit tests for this function. Furthermore, we know this function is not robust due to some crashes during execution. **Your third task** is to cover some of its vulnerabilities in the unit test and enhance the function implementation. 
- `compute_group_grades` takes a `Group` object (you can find this class in `src/school-management/models/school.py`) and computes a global mark and a boolean stating that the students pass the semester. This test for this function is not successful. **Your task** is to discover why and fix the function. (Bonus: you enhance the testing with other use cases) 

(Bonus task) As you may have noticed, the models in `src/school-management/models/school.py` use `pydantic` to define Models. `pydantic` is a library devised for data validation using Python type annotation (https://pydantic-docs.helpmanual.io/). For instance, if a base model, `MyModel`, has a positive integer parameter `number: PositiveInt`, `pydantic` will check its type during instantiation. If one writes `MyModel(number= "string")`, `pydantic` raises a `ValidationError` stating that parameter `number` is not well typed. As you can see, `compute_group_grades` returns a dictionary containing the necessary caution. Can you come up with a class, a BaseModel, for this function's results? (i.e. a class containing the necessary parameters for the function's results.) You can take inspiration from the already implemented BaseModels. 

(Bonus task) Can you amend the `Makefile` file to run:
- `make pytest` to run tests. Reminder: you can run pytest tests executing `poetry run pytest` in your terminal.
- `make hard-install` to have a fresh install of the library (i.e., delete the local virtual environment (i.e., delete the `.venv` folder) and then install dependencies using poetry. 
