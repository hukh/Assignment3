# Assignment3: efficient exploration of an unknown environment

## Objective

To implement algorithms that can explore, for the purposes of reconstructing or finding the maximum, in a realistic data example. We will utilize data-driven models of an environment to make predictions and pair these learned models with planning methods that explicitly seek to gain new information, or to maximize a quantity given the current estimate.

## Provided Resources

A provided simulator, found in `simulate_exploration.py`  allows the robot to move in a perfect straightline to any chosen location, and sense perfectly, but you must not assume only a very minimal knowledge of the underlying data. You are allowed to consider:

- The range of the data is [0,255]
- The environment is a finite sized rectangle. You can access the size with the `getLimits` command
- The data comes from an environmental process which changes somewhat smoothly

## Getting started:

It's very simple to run the example code this time. From the top level of the Assignment3 folder:

- $ python src/exploration_gazebo/src/exploration_node.py

You should see several iterations pass by quickly, and then the code reports some filenames to check that hold results. View these to see how the current method works. 

Check the code to see that this method is a naive random explorer that does not use any learning to model the data. It simply picks a random point, moves there and copies the exact observations into the reconstruction result. Any pixel that has not net been visited is given the guess 0, and the data observed does not change the exploration path at all. 

## Aims for your code

Try to reconstruct the environment and find maxima as rapidly as possible. You have some freedom to try ideas that you find interesting (especially if you check them with Dave during office hours). The recommended path is:

- Implement a Gaussian Process to make generalized predictions away from the observed data. This can be tested quickly by keeping the same random exploration path, but feeding the observed data into your GP and using it to make predictions everywhere. Can you make this give better reconstructions than the provided code? Better predictions of the max?
    - You will likely find that the hyper-parameters of the Gaussian Process have a big impact on whether it makes effective predictions or not. You may optimize these by hand or using an optimization on offline data if you wish.
    - Advanced feature: consider optimizing the hyper-parameters *online* from the data the robot sees while exploring, as would have to be done in a real robotics situation.

- Implement an exploration planner by coding an acquisition function (Expected Improvement is recommended, but you can try others) and an optimization routine to choose new target locations based on the maximum of this function. Does this improves your reconstructions and predictions of the max?
    - In class we saw the DIRECT method. You could also use a gradient-based method if you want to get very modern. These are efficient, but more involved to implement than I'd planned. 
    - Instead, it should work quite fine to take a number of random samples and compute the maximum over them, or else to form a coarse grid and take the max. 

- In many cases, the point above will not actually help, because the maxima of the acquisition function can be far from the robot's current location, so it is inefficient to always go to the global maximum. Consider a change to this strategy that will make more efficient use of the robot's motions:
    - Idea 1: Search for the acquisition function maximum only locally and make a partially greedy motion each time.
    - Idea 2: Modify the acquisition function to account for the distance that must be travelled to arrive at each location.
    - Idea 3: Find a way to optimize longer trajectories (parameterized exploration paths - a spiral, a square, etc)

## Reporting

Discuss what you learned while implementing your method. Show that you achieved efficient exploration by including the graphs produced by your best code in the document. Try to include answers to as many of these questions as is appropriate for your implementation:
-  What were the big keys to achieving efficiency? 
- Did you use learning? 
- If you used a GP, how did you select the parameters of your learning model?
- How did you exploit the smoothness assumption in the underlying data?
- Is your method robust to the random initial positions selected in the code? Does it always converge to the same global optimum, or ever gets stuck in a local opt?
