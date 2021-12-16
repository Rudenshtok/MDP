import matplotlib.pyplot as plt
import numpy as np
import os

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print (path+' created sucessful')
        return True
    else:
        print (path+' already exists')
        return False

class Experiment_result (object):
    def __init__(self, name):
        self.name = name
        self.reward_list = []
        self.cost_list = []
        self.cost2_list = []
        self.lagranges1_list = []
        self.lagranges2_list = []
        self.upper_lagranges1_list = []
        self.upper_lagranges2_list = []
        self.lower_lagranges1_list = []
        self.lower_lagranges2_list = []

    def append(self, result):
        reward = result[0]
        cost = result[1]
        cost2 = result[2]
        lagranges1 = result[3]
        lagranges2 = result[4]
        upper_lagranges1 = result[5]
        upper_lagranges2 = result[6]
        lower_lagranges1 = result[7]
        lower_lagranges2 = result[8]

        self.reward_list.append(reward)
        self.cost_list.append(cost)
        self.cost2_list.append(cost2)
        self.lagranges1_list.append(lagranges1)
        self.lagranges2_list.append(lagranges2)
        self.lower_lagranges1_list.append(lower_lagranges1)
        self.lower_lagranges2_list.append(lower_lagranges2)
        self.upper_lagranges1_list.append(upper_lagranges1)
        self.upper_lagranges2_list.append(upper_lagranges2)

    def save(self):
        dir = os.getcwd()  + '\\' +self.name
        mkdir(dir)
        for i in range(len(self.reward_list)):
            path = dir + '\\reward' + str(i) + '.txt'
            np.savetxt(path, self.reward_list[i])

        for i in range(len(self.cost_list)):
            path = dir + '\\cost' + str(i) + '.txt'
            np.savetxt(path, self.cost_list[i])

        for i in range(len(self.cost2_list)):
            path = dir + '\\cost2' + str(i) + '.txt'
            np.savetxt(path, self.cost2_list[i])

        for i in range(len(self.lagranges1_list)):
            path = dir + '\\lagrange1' + str(i) + '.txt'
            np.savetxt(path, self.lagranges1_list[i])

        for i in range(len(self.lagranges2_list)):
            path = dir + '\\lagrange2' + str(i) + '.txt'
            np.savetxt(path, self.lagranges2_list[i])

        for i in range(len(self.upper_lagranges1_list)):
            path = dir + '\\upper_lagrange1' + str(i) + '.txt'
            np.savetxt(path, self.upper_lagranges1_list[i])

        for i in range(len(self.upper_lagranges2_list)):
            path = dir + '\\upper_lagrange2' + str(i) + '.txt'
            np.savetxt(path, self.upper_lagranges2_list[i])

        for i in range(len(self.lower_lagranges1_list)):
            path = dir + '\\lower_lagrange1' + str(i) + '.txt'
            np.savetxt(path, self.lower_lagranges1_list[i])

        for i in range(len(self.lower_lagranges2_list)):
            path = dir + '\\lower_lagrange2' + str(i) + '.txt'
            np.savetxt(path, self.lower_lagranges2_list[i])


    def load(self, dir, num):
        dir =  os.getcwd()  + '\\' + dir
        isExists = os.path.exists(dir)

        if isExists:
            for i in range(num):
                path = dir + '\\reward' + str(i) + '.txt'
                self.reward_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\cost' + str(i) + '.txt'
                self.cost_list.append(np.loadtxt(path))

            for i in range(num):
                path = dir + '\\cost2' + str(i) + '.txt'
                self.cost2_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\lagrange1' + str(i) + '.txt'
                self.lagranges1_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\lagrange2' + str(i) + '.txt'
                self.lagranges2_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\upper_lagrange1' + str(i) + '.txt'
                self.upper_lagranges1_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\upper_lagrange2' + str(i) + '.txt'
                self.upper_lagranges2_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\lower_lagrange1' + str(i) + '.txt'
                self.lower_lagranges1_list.append(np.loadtxt(path))
            for i in range(num):
                path = dir + '\\lower_lagrange2' + str(i) + '.txt'
                self.lower_lagranges2_list.append(np.loadtxt(path))

    def plotsave(self, dir, repeat_times, modenum, **kwargs):
        STEPS = 100
        iterations = [i*10 for i in range(STEPS)]
        colormap = ['firebrick', 'darkred', 'slateblue', 'darkslateblue',  'olivedrab', 'yellowgreen', 'purple', 'darkviolet', 'pink', 'lightpink']
        num = 0
        SMALL_SIZE = 12
        MEDIUM_SIZE = 13
        BIGGER_SIZE = 14

        plt.rc('font', size=BIGGER_SIZE)  # controls default text sizes
        plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
        plt.rc('axes', labelsize=BIGGER_SIZE)  # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('legend', fontsize=BIGGER_SIZE)  # legend fontsize
        plt.rc('figure', titlesize=MEDIUM_SIZE)
        linewidth = 3
        Alpha = 0.5
        if modenum == 1:
            position = 'upper right'
            plt.figure(figsize=(4, 3))

            for name, showitem in kwargs.items():

                if 'position' == name:
                    position = showitem
                    continue
                if repeat_times > 1:
                    finalshow = np.array(showitem[repeat_times -1])
                    devia = np.std(a=np.array(showitem), axis=0)
                    devia = devia[range(STEPS)]
                    for i in range(repeat_times -1):
                        finalshow = finalshow + np.array(showitem[i])
                    finalshow = finalshow / float(repeat_times)
                    finalshow = finalshow.tolist()
                else:
                    finalshow = np.array(showitem[0])
                    devia = np.zeros(finalshow.shape)

                finalshow = finalshow[slice(STEPS)]
                plt.plot(iterations, finalshow, color=colormap[num*2], linestyle='-', label=str(name).replace('_', " ").replace('Z', '-').replace('Y', '.'), linewidth = linewidth)
                plt.fill_between(iterations, (np.array(finalshow) - devia).tolist(), (np.array(finalshow) + devia).tolist(),
                                alpha=Alpha, edgecolor=colormap[num*2], facecolor=colormap[num * 2])
                num = num + 1

            plt.legend(loc=position)
            plt.xlabel('# of Episodes')
            plt.ylabel('Accumulated Reward')
            plt.savefig(dir)

        elif modenum == 2:
            plt.figure(figsize=(4, 3))
            position = 'upper right'
            for name, showitem in kwargs.items():
                if 'position' == name:
                    position = showitem
                    continue
                if 'constraint' ==name:
                    constraint = [showitem for i in range(STEPS)]
                    plt.plot(iterations, constraint, color=colormap[num], linestyle='dashdot', linewidth=linewidth)
                    continue
                if 'constraint1' == name:
                    constraint1 = [showitem for i in range(STEPS)]
                    plt.plot(iterations, constraint1, color=colormap[num], linestyle='dashdot', linewidth=linewidth)
                    continue
                elif 'constraint2' == name:
                    constraint2 = [showitem for i in range(STEPS)]
                    plt.plot(iterations, constraint2, color=colormap[num + 1], linestyle='dotted', linewidth=linewidth)
                    continue

                if repeat_times > 1:
                    finalshow = np.array(showitem[repeat_times - 1])
                    devia = np.std(a=np.array(showitem), axis=0)
                    devia = devia[range(STEPS)]
                    for i in range(repeat_times - 1):
                        finalshow = finalshow + np.array(showitem[i])
                    finalshow = finalshow / float(repeat_times)

                    finalshow = finalshow.tolist()
                else:
                    finalshow = np.array(showitem[0])
                    devia = np.zeros(finalshow.shape)

                finalshow = finalshow[slice(STEPS)]
                if num % 2 == 0:
                    linestylename = 'solid'
                else:
                    linestylename = 'dashed'
                plt.plot(iterations, finalshow, color=colormap[num*2], linestyle=linestylename,
                         label=str(name).replace('_', " ").replace('Z', '-').replace('Y', '.'), linewidth=linewidth)
                plt.fill_between(iterations, (np.array(finalshow) - devia).tolist(),
                                 (np.array(finalshow) + devia).tolist(),
                                 alpha=Alpha, edgecolor=colormap[num * 2], facecolor=colormap[num * 2])
                num = num + 1

            plt.ylim((0, 200))
            plt.legend(loc=position)
            plt.xlabel('# of Episodes')
            plt.ylabel('Accumulated Cost')
            plt.savefig(dir)
        else:
            plt.figure(figsize=(4, 3))
            for name, showitem in kwargs:
                if repeat_times > 1:
                    finalshow = np.array(showitem[repeat_times -1])
                    for i in range(repeat_times -1):
                        finalshow = finalshow + np.array(showitem[i])

                    finalshow = finalshow / float(repeat_times)

                    finalshow = finalshow.tolist()
                else:
                    finalshow = showitem

                finalshow = finalshow[slice(STEPS)]

                plt.plot(iterations, finalshow, color=colormap[num], linestyle='-', label=str(name).replace('_', " ").replace('Z', '-').replace('Y', '.'), linewidth=linewidth)
                num = num + 1

            plt.ylim((0, 200))
            plt.legend(loc='upper left')
            plt.xlabel('# of Episodes')
            plt.ylabel('Dual variable')
            plt.savefig(dir)