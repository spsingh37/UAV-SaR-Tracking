#!/usr/bin/env python
import gym
import rospy
import mav_env
from gym import wrappers
import gym_gazebo
import time
import random
import time
import liveplot
import qlearn


if __name__ == '__main__':

    rospy.init_node('qlearning', anonymous=True)
    env = gym.make('MavEnv-v0')
    print "Gym Make Done"


    outdir = '~/UAV_SaR_ws/quadrotor_ros/rl_mav_ros/outdir/qlearning'
    env = gym.wrappers.Monitor(env, outdir, force=True)
    print "Monitor Wrapper Started"

    plotter = liveplot.LivePlot(outdir)

    qlearn = qlearn.QLearn(actions=range(env.action_space.n),
                    alpha=0.8, gamma=0.9, epsilon=0)

    epsilon_discount = 0.9
	
    start_time = time.time()
    total_episodes = 10
 
    for x in range(total_episodes):
        done = False

        cumulated_reward = 0 

        print("Episode = " +str(x)+ " started")

        observation, done = env.reset()

	if qlearn.epsilon > 0.01:
            qlearn.epsilon *= epsilon_discount

        state = ''.join(map(str, observation))

	i = 0
	while(True):

            # Pick an action based on the current state
            action = qlearn.chooseAction(state)
            
            # Execute the action and get feedback
            observation, reward, done, info = env.step(action)
            cumulated_reward += reward


            nextState = ''.join(map(str, observation))

            qlearn.learn(state, action, reward, nextState)

            env._flush(force=True)

            if not(done):
                state = nextState
            else:
                break

	    i = i+1

	
	plotter.plot(env)


        m, s = divmod(int(time.time() - start_time), 60)
        h, m = divmod(m, 60)
        print ("EP: "+str(x+1)+"| Reward: "+str(cumulated_reward)+" | Steps: "+str(i+1)+"  | Time: %d:%02d:%02d" % (h, m, s))
	

    #Github table content
    print ("\n|"+str(total_episodes)+"|"+str(qlearn.alpha)+"|"+str(qlearn.gamma)+"|"+str(qlearn.epsilon)+"")

    
    print ("Q table: ")
    print(qlearn.q)
    env.close()
    plotter.show()
