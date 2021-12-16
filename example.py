import experiment
import os
from AR_CPO import arcpo
from PDO import pdo

#===============Conduct experiments and Save results==============================================#
repeat_times = 10

ARCPO = experiment.Experiment_result('ARCPO')

for i in range(repeat_times):
    ARCPO.append(arcpo(1, 0.01, 0.0003, 1, 25))

ARCPO.save()

PDO = experiment.Experiment_result('PDO')
for i in range(repeat_times):
    PDO.append(pdo(0.0005))
PDO.save()

#===============Load results and plot images======================================================#
repeat_times = 10
dir = os.getcwd() +'\\plots'
experiment.mkdir(dir)
PDO = experiment.Experiment_result('PDO')
PDO.load('PDO', repeat_times)
ARCPO = experiment.Experiment_result('ARCPO')
ARCPO.load(ARCPO.name, repeat_times)

ARCPO.plotsave(dir + '\\Reward.pdf', repeat_times, 1, ARZCPO=ARCPO.reward_list,
                   PDO=PDO.reward_list, position='lower right')
ARCPO.plotsave(dir + '\\Cost.pdf', repeat_times, 2, ARZCPO=ARCPO.cost_list, PDO=PDO.cost_list, constraint1=50)
ARCPO.plotsave(dir + '\\Cost2.pdf', repeat_times, 2, ARZCPO=ARCPO.cost2_list, PDO=PDO.cost2_list, constraint2=50)