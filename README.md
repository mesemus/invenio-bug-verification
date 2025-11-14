# invenio-bug-verification

This module provides tools for verifying bugfixes in Invenio-based applications.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/mesemus/invenio-bug-verification.git
   ```

2. Edit the `patches.json` file to specify your patches:

    ```json
    {
         "invenio-db": {
            "url": "https://github.com/oarepo/invenio-db.git",
            "branch": "fix-uow",
         }
    }
    ```

3. Commit and push your changes either directly to a main branch or your branch of choice.

4. Wait for the CI pipeline to run the verification tests.

## How it works

The CI pipeline will:

1. Clone the github.com/zenodo/zenodo-rdm maintrunk repository.
2. Extract all packages from `uv.lock` that start with `invenio-`. Store the result to an output so that it could be used in subsequent matrix build steps.
3. Run a pipeline for each such package (matrix build from the #2 output):
   a. Clone the package:
     - if the mackage is in `patches.json`, clone the specified repository and checkout the specified branch.
     - otherwise, clone the package from github.com/inveniosoftware.
   b. Create a virtualenv using uv --seed
   c. Call the `run-tests.sh` script from this repository to run the tests.
   d. For each of modules inside the packages.json, if the module is inside the venv,
      install the patched branch instead. If there is no such module, skip the rest of the steps and mark the package as "no patch".
   e. Run the tests again
   f. Compare the test results before and after applying the patch, store the outputs and the diff as an artifact.
4. Create a summary report of all packages tested, indicating which patches fixed issues/created new and which did not.
