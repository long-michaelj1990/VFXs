from pyfbsdk import *
MyScene = FBSystem ().Scene
foundComponents = FBComponentList()
for component in FBSystem().Scene.Components:
   #  print(component.LongName)
     if component.LongName == 'Character1_Reference':
         component.Name='Reference'
     if component.LongName == 'Character1_Hips':
         component.Name='Hips'
     if component.LongName == 'Character1_Spine':
         component.Name='Spine'
     if component.LongName == 'Character1_Spine1':
         component.Name='Spine1'
     if component.LongName == 'Character1_Spine2':
         component.Name='Spine2'
     if component.LongName == 'Character1_LeftShoulder':
         component.Name='LeftShoulder'
     if component.LongName == 'Character1_LeftArm':
         component.Name='LeftArm'
     if component.LongName == 'Character1_LeftForeArm':
         component.Name='LeftForeArm'
     if component.LongName == 'Character1_LeftHand':
         component.Name='LeftHand'
     if component.LongName == 'Character1_LeftHandIndex1':
         component.Name='LeftHandIndex1'
     if component.LongName == 'Character1_LeftHandIndex2':
         component.Name='LeftHandIndex2'
     if component.LongName == 'Character1_LeftHandIndex3':
         component.Name='LeftHandIndex3'
     if component.LongName == 'Character1_LeftHandIndex4':
         component.Name='LeftHandIndex4'
         
     if component.LongName == 'Character1_LeftHandMiddle1':
         component.Name='LeftHandMiddle1'
     if component.LongName == 'Character1_LeftHandMiddle2':
         component.Name='LeftHandMiddle2'
     if component.LongName == 'Character1_LeftHandMiddle3':
         component.Name='LeftHandMiddle3'
     if component.LongName == 'Character1_LeftHandMiddle4':
         component.Name='LeftHandMiddle4'
         
     if component.LongName == 'Character1_LeftHandPinky1':
         component.Name='LeftHandPinky1'
     if component.LongName == 'Character1_LeftHandPinky2':
         component.Name='LeftHandPinky2'
     if component.LongName == 'Character1_LeftHandPinky3':
         component.Name='LeftHandPinky3'
     if component.LongName == 'Character1_LeftHandPinky4':
         component.Name='LeftHandPinky4'
     if component.LongName == 'Character1_LeftHandRing1':
         component.Name='LeftHandRing1'
     if component.LongName == 'Character1_LeftHandRing2':
         component.Name='LeftHandRing2'
     if component.LongName == 'Character1_LeftHandRing3':
         component.Name='LeftHandRing3'
     if component.LongName == 'Character1_LeftHandRing4':
         component.Name='LeftHandRing4'
    
     if component.LongName == 'Character1_LeftHandThumb1':
         component.Name='LeftHandThumb1'
     if component.LongName == 'Character1_LeftHandThumb2':
         component.Name='LeftHandThumb2'
     if component.LongName == 'Character1_LeftHandThumb3':
        component.Name='LeftHandThumb3'
     if component.LongName == 'Character1_LeftHandThumb4':
        component.Name='LeftHandThumb4'
         
         
     if component.LongName == 'Character1_RightHandThumb1':
         component.Name='RightHandThumb1'
     if component.LongName == 'Character1_RightHandThumb2':
         component.Name='RightHandThumb2'
     if component.LongName == 'Character1_RightHandThumb3':
         component.Name='RightHandThumb3'
     if component.LongName == 'Character1_RightHandThumb4':
         component.Name='RightHandThumb4'
     if component.LongName == 'Character1_RightShoulder':
         component.Name='RightShoulder'
     if component.LongName == 'Character1_RightArm':
         component.Name='RightArm'
     if component.LongName == 'Character1_RightForeArm':
         component.Name='RightForeArm'
     if component.LongName == 'Character1_RightHand':
         component.Name='RightHand'
     if component.LongName == 'Character1_RightHandIndex1':
         component.Name='RightHandIndex1'
     if component.LongName == 'Character1_RightHandIndex2':
         component.Name='RightHandIndex2'
     if component.LongName == 'Character1_RightHandIndex3':
         component.Name='RightHandIndex3'
     if component.LongName == 'Character1_RightHandIndex4':
         component.Name='RightHandIndex4'
     if component.LongName == 'Character1_RightHandMiddle1':
         component.Name='RightHandMiddle1'
     if component.LongName == 'Character1_RightHandMiddle2':
         component.Name='RightHandMiddle2'
     if component.LongName == 'Character1_RightHandMiddle3':
         component.Name='RightHandMiddle3'
     if component.LongName == 'Character1_RightHandMiddle4':
         component.Name='RightHandMiddle4'
     if component.LongName == 'Character1_RightHandPinky1':
         component.Name='RightHandPinky1'
     if component.LongName == 'Character1_RightHandPinky2':
         component.Name='RightHandPinky2'
     if component.LongName == 'Character1_RightHandPinky3':
         component.Name='RightHandPinky3'
     if component.LongName == 'Character1_RightHandPinky4':
         component.Name='RightHandPinky4'
     if component.LongName == 'Character1_RightHandRing1':
         component.Name='RightHandRing1'
     if component.LongName == 'Character1_RightHandRing2':
         component.Name='RightHandRing2'
     if component.LongName == 'Character1_RightHandRing3':
         component.Name='RightHandRing3'
     if component.LongName == 'Character1_RightHandRing4':
         component.Name='RightHandRing4'
     if component.LongName == 'Character1_RightHandThumb1':
         component.Name='RightHandThumb1'
     if component.LongName == 'Character1_RightHandThumb2':
         component.Name='RightHandThumb2'
     if component.LongName == 'Character1_RightHandThumb3':
         component.Name='RightHandThumb3'
     if component.LongName == 'Character1_RightHandThumb4':
         component.Name='RightHandThumb4'

     if component.LongName == 'Character1_Neck':
         component.Name='Neck'
     if component.LongName == 'Character1_Head':
         component.Name='Head'
     if component.LongName == 'Character1_LeftUpLeg':
         component.Name='LeftUpLeg'
     if component.LongName == 'Character1_LeftLeg':
         component.Name='LeftLeg'
     if component.LongName == 'Character1_LeftFoot':
         component.Name='LeftFoot'
     if component.LongName == 'Character1_RightUpLeg':
         component.Name='RightUpLeg'
     if component.LongName == 'Character1_RightLeg':
         component.Name='RightLeg'
     if component.LongName == 'Character1_RightFoot':
         component.Name='RightFoot'
         
