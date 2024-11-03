# DSSS Homework 2
Exercise 2 of Data Science Survival Skills course at FAU Erlangen-Nürnberg


## Tasks 1/5
   ● Create your first GitHub repository with a name of your choice (e.g.,“dsss_homework_2”).
   
   ● Make sure it is publicly available so we can check the repo.
   
   ● You should tick the “Add a README file” cell, use a .gitignore template for Python and a license, e.g., Apache License.
   
   **→ Slide**: Link to your GitHub repository.

## Task 2/5
   ● Clone your repository to your local machine.
   
   ● Copy&Paste the "math_quiz" folder that we provided to you via StudOn to your repository folder.
   
   ● Add, commit and push the folder and the files on the main branch.

## Task 3/5
   ● Create a new branch called “code_cleanup”. Checkout to this branch and modify the “math_quiz.py” file:

     ○ Better readability: Change variable names, function names, etc.
     
     ○ Comments: Add a sufficient amount of comments to the code
     
     ○ Docstrings: For every function (free choice of formatting type)
     
     ○ Error handling (at least one meaningful try-except statement): For example, check whether the user input is valid, otherwise handle the error
     
     ○ Fix bugs (you maybe want to use unit tests for that → see next task)

   ● Add, commit and push the file.
   
   ● Checkout to the main branch again and merge your “code_cleanup” branch to the main branch.
   
   **→ Slide**: Screenshots of your modified code.
   
   **→ Slide**: Screenshot of the output after running “git merge” command.

## Task 4/5
   ● Write three unit tests in the file “tests_math_quiz.py” for the three functions from “math_quiz.py” (function_A, function_B, function_C → the functions will probably no longer be called like this at this point)
   
   ● Add, commit and push the file to your GitHub repository.
   
   **→ Slide**: Screenshots of your unit tests code.

## Task 5/5
   ● Make your repository pip installable. Therefore, you need the following structure. Add all of the missing files to your repository with a meaningful commit message.

   ● Run `pip install git+<link-to-repository.git>`.

   ● Afterwards, run “math_quiz” in your command line and solve some math tasks :)

   **→ Slide**: Screenshot of terminal output of pip install git.
