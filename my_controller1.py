from controller import Robot

robot = Robot()

timestep = 160
flag = 0 

motorRPC = robot.getDevice("RPC")
motorRPF = robot.getDevice("RPF")
motorRMC = robot.getDevice("RMC")
motorRMF = robot.getDevice("RMF")
motorRAC = robot.getDevice("RAC")
motorRAF = robot.getDevice("RAF")

motorLPC = robot.getDevice("LPC")
motorLPF = robot.getDevice("LPF")
motorLMC = robot.getDevice("LMC")
motorRMF = robot.getDevice("LMF")
motorLAC = robot.getDevice("LAC")
motorLAF = robot.getDevice("LAF")

while robot.step(timestep) != -1:
    pass