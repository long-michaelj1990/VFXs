from pyfbsdk import *
MyScene = FBSystem ().Scene
foundComponents = FBComponentList()
for component in FBSystem().Scene.Components:
   #  print(component.LongName)
     if component.LongName == 'Reference':
         component.Name='root'
     if component.LongName == 'Hips':
         component.Name='pelvis'
     if component.LongName == 'Spine':
         component.Name='spine_01'
     if component.LongName == 'Spine1':
         component.Name='spine_02'
     if component.LongName == 'Spine2':
         component.Name='spine_03'
     if component.LongName == 'LeftShoulder':
         component.Name='clavicle_l'
     if component.LongName == 'LeftArm':
         component.Name='upperarm_l'
     if component.LongName == 'LeftForeArm':
         component.Name='lowerarm_l'
     if component.LongName == 'LeftHand':
         component.Name='hand_l'
     if component.LongName == 'LeftHandIndex1':
         component.Name='index_01_l'
     if component.LongName == 'LeftHandIndex2':
         component.Name='index_02_l'
     if component.LongName == 'LeftHandIndex3':
         component.Name='index_03_l'
     if component.LongName == 'LeftHandMiddle1':
         component.Name='middle_01_l'
     if component.LongName == 'LeftHandMiddle2':
         component.Name='middle_02_l'
     if component.LongName == 'LeftHandMiddle3':
         component.Name='middle_03_l'
     if component.LongName == 'LeftHandPinky1':
         component.Name='pinky_01_l'
     if component.LongName == 'LeftHandPinky2':
         component.Name='pinky_02_l'
     if component.LongName == 'LeftHandPinky3':
         component.Name='pinky_03_l'
     if component.LongName == 'LeftHandRing1':
         component.Name='ring_01_l'
     if component.LongName == 'LeftHandRing2':
         component.Name='ring_02_l'
     if component.LongName == 'LeftHandRing3':
         component.Name='ring_03_l'
         
     if component.LongName == 'RightHandThumb1':
         component.Name='thumb_01_l'
     if component.LongName == 'RightHandThumb2':
         component.Name='thumb_02_l'
     if component.LongName == 'RightHandThumb3':
         component.Name='thumb_03_l'
     if component.LongName == 'RightShoulder':
         component.Name='clavicle_r'
     if component.LongName == 'RightArm':
         component.Name='upperarm_r'
     if component.LongName == 'RightForeArm':
         component.Name='lowerarm_r'
     if component.LongName == 'RightHand':
         component.Name='hand_r'
     if component.LongName == 'RightHandIndex1':
         component.Name='index_01_r'
     if component.LongName == 'RightHandIndex2':
         component.Name='index_02_r'
     if component.LongName == 'RightHandIndex3':
         component.Name='index_03_r'
     if component.LongName == 'RightHandMiddle1':
         component.Name='middle_01_r'
     if component.LongName == 'RightHandMiddle2':
         component.Name='middle_02_r'
     if component.LongName == 'RightHandMiddle3':
         component.Name='middle_03_r'
     if component.LongName == 'RightHandPinky1':
         component.Name='pinky_01_r'
     if component.LongName == 'RightHandPinky2':
         component.Name='pinky_02_r'
     if component.LongName == 'RightHandPinky3':
         component.Name='pinky_03_r'
     if component.LongName == 'RightHandRing1':
         component.Name='ring_01_r'
     if component.LongName == 'RightHandRing2':
         component.Name='ring_02_r'
     if component.LongName == 'RightHandRing3':
         component.Name='ring_03_r'
     if component.LongName == 'RightHandThumb1':
         component.Name='thumb_01_r'
     if component.LongName == 'RightHandThumb2':
         component.Name='thumb_02_r'
     if component.LongName == 'RightHandThumb3':
         component.Name='thumb_03_r'
     if component.LongName == 'Neck':
         component.Name='neck_01'
     if component.LongName == 'Head':
         component.Name='head'
     if component.LongName == 'LeftUpLeg':
         component.Name='thigh_l'
     if component.LongName == 'LeftLeg':
         component.Name='calf_l'
     if component.LongName == 'LeftFoot':
         component.Name='foot_l'
     if component.LongName == 'RightUpLeg':
         component.Name='thigh_r'
     if component.LongName == 'RightLeg':
         component.Name='calf_r'
     if component.LongName == 'RightFoot':
         component.Name='foot_r'
         
