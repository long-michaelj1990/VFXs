# Copyright 2009 Autodesk, Inc.  All rights reserved.
# Use of this software is subject to the terms of the Autodesk license agreement 
# provided at the time of installation or download, or which otherwise accompanies
# this software in either electronic or hard copy form.
#
# Topic: FBRenderer, FBVideoGrabber, FBVideoRenderDepth, FBVideoRenderDepth, FBVideoCodecManager, FBVideoCodecMode
#
from pyfbsdk import *
#from pyfbsdk import FBMessageBox, FBApplication, FBVideoGrabber, FBVideoRenderDepth, FBVideoRenderDepth, FBVideoCodecManager, FBVideoCodecMode
import sys, os
from os import environ, listdir
from PySide import QtGui
import time

# We take for granted that the folder containing the FBX files is
# indicated with the environment variable 'RENDER_SRC_FOLDER'.
lRenderSrcFolder = QtGui.QFileDialog.getExistingDirectory()
lRenderSrcFolder=lRenderSrcFolder    
# And the place where to store the rendered scene is indicated by
# the environment variable 'RENDER_DST_FOLDER'.
lRenderDstFolder = QtGui.QFileDialog.getExistingDirectory()
lRenderDstFolder=lRenderDstFolder+'\\'
# The file format of the render is indicated by 'RENDER_FILE_FORMAT'.
lRenderFileFormat = 'mov'

file_directory=[]
file_directory_filt=[]
fbx_files=[]

for root,dirs,files in os.walk(lRenderSrcFolder): 
    # Iterate in the list
    for lFileName in files:
        # Ensure that we handle only FBX files.
        if lFileName.endswith('.fbx'):
            fbx_files.append(lFileName)
            for i in range(len(files)):
              file_directory.append(root+'\\'+files[i])
                
for i in range(len(file_directory)):
    if file_directory[i].endswith('.fbx'):
        file_directory_filt.append(file_directory[i])

file_directory_filt=set(file_directory_filt)
fbx_files_str=str(fbx_files)

for lFileName in file_directory_filt:
    filename=os.path.basename(lFileName) 
    # Create an application object.
    lApp = FBApplication()                 
    # We need the full path of the FBX file to load it.
    lSrcFileName = os.path.join(lRenderSrcFolder, lFileName)
    lSrcFileName=str(lSrcFileName)
    # We also need the full path of the output file.
    lDstFileName = os.path.join(lRenderDstFolder, filename.replace( 'fbx', lRenderFileFormat ))
    lDstFileName=str(lDstFileName)        
    # Open the file in the application.
    lApp.FileOpen(lSrcFileName)    
    # Get the default rendering options, which are saved in the FBX file.
    lOptions = FBVideoGrabber().GetOptions()

    # Set VideoCodec Option:
    VideoManager = FBVideoCodecManager()
   # VideoManager.VideoCodecMode = FBVideoCodecMode.FBVideoCodecUncompressed
   # VideoManager.VideoCodecMode = FBVideoCodecMode.FBVideoCodecAsk 
   
    VideoManager.VideoCodecMode =FBVideoCodecMode.FBVideoCodecStored
             
    # Set the name of the rendered file.
    lOptions.OutputFileName = lDstFileName
    
    # hide Axis and grid from renders
##    for lCamera in FBSystem().Scene.Cameras:
##        lCamera.ViewShowAxis = False
##        lCamera.ViewShowGrid = False
    camera = "Producer Perspective"
    cameraType = None
    for cam in FBSystem().Scene.Cameras:
        if cam.Name == camera:
            cameraType = cam
            cam.FieldOfView = 100
        break
        if cameraType is not None:
            FBSystem().Renderer.CurrentCamera = cameraType
        # Only windows supports mov.
    if lRenderFileFormat == '.mov' and os.name != 'nt':
        lOptions.BitsPerPixel = FBVideoRenderDepth.FBVideoRender32Bits                   
   # Do the render. This will always be done in uncompressed mode.
    lApp.FileRender( lOptions )
    
   # Clear the scene.
    lApp.FileNew()
    print("finished file")
print("no FBX files")
                