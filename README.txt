Package Requirements:
- NumPy
- PyTorch
- OpenAI Gym
- copy
- collections

AR_CPO.py:
    The *arcpo()* inside is the realization of AR-CPO algorithm. For the *arcpo* function, input arguments --inner_loop, --max_kl, --eta, --s, --stopping_time correspond to the parameters inner_loop, max_KL, $\eta$, $s$, and $H$ in Appendix B.2 in the paper.

    The RegPO subroutine is instantiated through DQN with trust-region policy optimization. The hyperparameters are specified inside *arcpo()* as recommended.

PDO.py:
    The *pdo()* inside is the realization of PDO algorithm. Its input argument --eta corresponds to the stepsize of dual updatas. Its policy optimization is also realized by the same DQN with trust-region policy optimization and hyperparameters as *arcpo()*.

experiment.py:
    The class objective "Experiment_result" provides the container to store repetitive experiment results. Its input argument --name specifies where the results will be saved.

    Description of the methods of "Experiment_result":
        - append(self, result):
            Store the output of arcpo() or pdo()

        - save(self):
            Create a directory named *self.name* under current directory and dump stored results to it

        - load(self, dir, num):
            Load first "num" previous experiment results from "dir". The number of previous logged experiments should be more than "num".



        - plotsave(self, dir, repeat_times, modenum, **kwargs):
            Plot curves of either the value function w.r.t. reward or the value function w.r.t. costs.
            "dir" specifies where the plot will be saved. "plotsave" will create "dir" if it does not exist and then store image to it.
            "repeat_times" specifies how many repetitive experiments are going to generate the plot.
            "modenum": "modenum==1" means we are plotting the reward functions and "modenum==2" means plotting the cost functions.
            **kwargs: key:values corresponds to the curve name versus the numpy array that records the experiment results.


example.py:
    The codes show how we plot the figures in the paper.


