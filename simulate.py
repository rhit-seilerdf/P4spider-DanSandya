import pybullet as p  
import time   
import pyrosim
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath(), 0)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0, -9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")
# box = p.loadSDF("box.sdf")

duration = 5000

for i in range(duration):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect() 