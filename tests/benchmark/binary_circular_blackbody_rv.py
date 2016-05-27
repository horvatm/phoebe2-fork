
import numpy as np
import phoebe2

b = phoebe2.Bundle.default_binary()

b.add_dataset('rv', time=np.linspace(0,3,101), dataset='rv01')

b.run_compute()