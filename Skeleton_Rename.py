from pyfbsdk import *
MyScene = FBSystem ().Scene
foundComponents = FBComponentList()
for component in FBSystem().Scene.Components:
   #  print(component.LongName)
     if component.LongName == 'Root':
         component.Name='Reference'
     if component.LongName == 'pelvis':
         component.Name='Hips'
     if component.LongName == 'spine_01':
         component.Name='Spine'
     if component.LongName == 'spine_02':
         component.Name='Spine1'
     if component.LongName == 'spine_03':
         component.Name='Spine2'
     if component.LongName == 'clavicle_l':
         component.Name='LeftShoulder'
     if component.LongName == 'upperarm_l':
         component.Name='LeftArm'
     if component.LongName == 'lowerarm_l':
         component.Name='LeftForeArm'
     if component.LongName == 'hand_l':
         component.Name='LeftHand'
     if component.LongName == 'index_01_l':
         component.Name='LeftHandIndex1'
     if component.LongName == 'index_02_l':
         component.Name='LeftHandIndex2'
     if component.LongName == 'index_03_l':
         component.Name='LeftHandIndex3'
     if component.LongName == 'middle_01_l':
         component.Name='LeftHandMiddle1'
     if component.LongName == 'middle_02_l':
         component.Name='LeftHandMiddle2'
     if component.LongName == 'middle_03_l':
         component.Name='LeftHandMiddle3'
     if component.LongName == 'pinky_01_l':
         component.Name='LeftHandPinky1'
     if component.LongName == 'pinky_02_l':
         component.Name='LeftHandPinky2'
     if component.LongName == 'pinky_03_l':
         component.Name='LeftHandPinky3'
     if component.LongName == 'ring_01_l':
         component.Name='LeftHandRing1'
     if component.LongName == 'ring_02_l':
         component.Name='LeftHandRing2'
     if component.LongName == 'ring_03_l':
         component.Name='LeftHandRing3'
         
     if component.LongName == 'thumb_01_l':
         component.Name='RightHandThumb1'
     if component.LongName == 'thumb_02_l':
         component.Name='RightHandThumb2'
     if component.LongName == 'thumb_03_l':
         component.Name='RightHandThumb3'
     if component.LongName == 'clavicle_r':
         component.Name='RightShoulder'
     if component.LongName == 'upperarm_r':
         component.Name='RightArm'
     if component.LongName == 'lowerarm_r':
         component.Name='RightForeArm'
     if component.LongName == 'hand_r':
         component.Name='RightHand'
     if component.LongName == 'index_01_r':
         component.Name='RightHandIndex1'
     if component.LongName == 'index_02_r':
         component.Name='RightHandIndex2'
     if component.LongName == 'index_03_r':
         component.Name='RightHandIndex3'
     if component.LongName == 'middle_01_r':
         component.Name='RightHandMiddle1'
     if component.LongName == 'middle_02_r':
         component.Name='RightHandMiddle2'
     if component.LongName == 'middle_03_r':
         component.Name='RightHandMiddle3'
     if component.LongName == 'pinky_01_r':
         component.Name='RightHandPinky1'
     if component.LongName == 'pinky_02_r':
         component.Name='RightHandPinky2'
     if component.LongName == 'pinky_03_r':
         component.Name='RightHandPinky3'
     if component.LongName == 'ring_01_r':
         component.Name='RightHandRing1'
     if component.LongName == 'ring_02_r':
         component.Name='RightHandRing2'
     if component.LongName == 'ring_03_r':
         component.Name='RightHandRing3'
     if component.LongName == 'thumb_01_r':
         component.Name='RightHandThumb1'
     if component.LongName == 'thumb_02_r':
         component.Name='RightHandThumb2'
     if component.LongName == 'thumb_03_r':
         component.Name='RightHandThumb3'
     if component.LongName == 'neck_01':
         component.Name='Neck'
     if component.LongName == 'head':
         component.Name='Head'
     if component.LongName == 'thigh_l':
         component.Name='LeftUpLeg'
     if component.LongName == 'calf_l':
         component.Name='LeftLeg'
     if component.LongName == 'foot_l':
         component.Name='LeftFoot'
     if component.LongName == 'thigh_r':
         component.Name='RightUpLeg'
     if component.LongName == 'calf_r':
         component.Name='RightLeg'
     if component.LongName == 'foot_r':
         component.Name='RightFoot'
         
