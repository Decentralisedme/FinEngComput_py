# Paths Folder
Underlying prices(i.e.stocks Prices) are random and we need probabilistic models to describe their dynamics. We use SDE
- SDE by definition is an equation where one or more of the terms is a stochatic process
- Stochastic process is a collection of random variables:
    - Wiener Process or Brownian Motion
    - Poisson Process or jump process 
- Some Notes on GMB SDE:
![alt text](Images/gbm1.png)

- SDEs are solved via ITOs Lemma:
![alt text](Images/ITOsLemma.png)

The main function to generate GBM paths is in scripts.py file, the function is then imported in other files when needed

The file would contain the description of the process

### Reference:
- LechGrzelak Computetional Finance Course: https://www.youtube.com/watch?v=MhmZaHWGWHc&list=PL6zzGYGhbWrPaI-op1UfNl0uDglxdkaOB&index=4
- Wikipidia: https://en.wikipedia.org/wiki/Stochastic_differential_equation
