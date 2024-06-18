# Mutation Testing Examples
This is the repo for some mutation testing examples.
`.mutmutcache` holds to mutation testing cache for future use.

## Setup
Ensure you have Conda installed on your machine. If you do not have Conda installed, you can download and install it from [Anaconda's official website](https://www.anaconda.com/products/distribution) or [Miniconda's official website](https://docs.conda.io/en/latest/miniconda.html).

### Steps to Set Up the Environment

1. **Clone the Repository**

   ```bash
   git clone git@github.com:neilCrosswaite/mutation-examples.git
   cd mutation-examples

2. **Create the Conda Environment**
    Use the provided environment.yml file to create the environment.

    ```bash
    conda env create -f environment.yml
    ``````
    This will create a new conda environment named mutation_testing (as specified in the environment.yml file) with pytest, and mutmut.

3. **Activate the Environment**
    ```bash
    conda activate mutation_testing
    ```

4. **Verify the Installation**
    ```bash
    pytest --version
    mutmut --version
    ```