#!/usr/bin/env python3
"""Off-screen studio-style preview renders of draft GLBs; no product claims."""
from __future__ import annotations
from pathlib import Path
import math
import vtk

ROOT=Path(__file__).resolve().parents[1]
GLB=ROOT/'supports/3d/glb'
OUT=ROOT/'supports/3d/previews'
OUT.mkdir(parents=True,exist_ok=True)


def preview(path:Path, angle_deg:int, out:Path):
    ren=vtk.vtkRenderer()
    ren.SetBackground(0.94,0.955,0.966)
    ren.SetBackground2(1.0,1.0,1.0)
    ren.GradientBackgroundOn()
    win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.AddRenderer(ren)
    win.SetSize(880,880)
    win.SetMultiSamples(4)
    importer=vtk.vtkGLTFImporter()
    importer.SetFileName(str(path))
    importer.SetRenderWindow(win)
    importer.Update()
    bounds=ren.ComputeVisiblePropBounds()
    if not all(math.isfinite(b) for b in bounds):
        raise RuntimeError(f'Cannot render {path}')
    ctr=[(bounds[i]+bounds[i+1])/2 for i in [0,2,4]]
    s=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4])
    camera=ren.GetActiveCamera()
    # VTK importer converts glTF camera/coordinates into its Z-up scene.
    a=math.radians(angle_deg)
    camera.SetFocalPoint(*ctr)
    camera.SetPosition(ctr[0]+s*2.25*math.sin(a),ctr[1]-s*2.25*math.cos(a),ctr[2]+s*.78)
    camera.SetViewUp(0,0,1)
    camera.SetViewAngle(33)
    ren.ResetCameraClippingRange()
    # Flat but legible soft two-light scheme.
    for pos,brightness in [((-s*1.8,-s*3.0,s*3.4),1.35),((s*2.2,-s*2.5,s*2.1),.75)]:
        light=vtk.vtkLight();light.SetLightTypeToSceneLight();light.SetPosition(*pos);light.SetIntensity(brightness);ren.AddLight(light)
    win.Render()
    filt=vtk.vtkWindowToImageFilter()
    filt.SetInput(win)
    filt.SetInputBufferTypeToRGB()
    filt.ReadFrontBufferOff()
    filt.Update()
    writer=vtk.vtkPNGWriter();writer.SetFileName(str(out));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
    win.Finalize()

if __name__=='__main__':
    for p in sorted(GLB.glob('*.glb')):
        for angle in (0,30):
            out=OUT/f'{p.stem}-{angle:02d}.png'
            preview(p,angle,out)
            print(out.name,out.stat().st_size)
