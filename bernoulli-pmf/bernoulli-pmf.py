import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
  x=np.asarray(x,dtype=float)
  p=np.asarray(p,dtype=float)
  pmf=np.where(x==0,(1-p),p)
  mean= (float(p))
  varrience=float( p*(1-p))
  return  {
      "pmf": pmf, 
      "mean": mean, 
      "variance": varrience
  }