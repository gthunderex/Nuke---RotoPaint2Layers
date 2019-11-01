import nuke.rotopaint as rp

n = nuke.selectedNode()
n2 = nuke.nodes.RotoPaint(name=n.name()+'_Layers')
n2.setXYpos(n.xpos()+150,n.ypos()+150)

c = n['curves']
mainRoot = c.rootLayer
n2_curves = n2['curves']

shapeArray = []
for shape in mainRoot:
    shapeArray.append(shape)

frameArray = []
for shape in shapeArray:
    attrs = shape.getAttributes()
    firstF = attrs.getValue(0,'ltn')
    lastF = attrs.getValue(0,'ltm')
    typeF = str(attrs.getValue(0,'ltt'))
    if typeF=='0.0':
        frame = 'all'
    elif typeF=='1.0':
        frame = 'start-' + str(firstF)
    elif typeF=='2.0':
        frame = str(firstF)
    elif typeF=='3.0':
        frame = str(firstF) + '-end'
    elif typeF=='4.0':
        frame = str(firstF)+'-'+str(lastF)
    if frame not in frameArray:
        frameArray.append(frame)

for i in frameArray:
    layer = rp.Layer(n2_curves)
    layer.name = 'frame_' + str(i)
    n2_curves.rootLayer.append(layer)
    for shape in shapeArray:
        attrs = shape.getAttributes()
        firstF = attrs.getValue(0,'ltn')
        lastF = attrs.getValue(0,'ltm')
        typeF = str(attrs.getValue(0,'ltt'))
        if typeF=='0.0':
            frame = 'all'
        elif typeF=='1.0':
            frame = 'start-' + str(firstF)
        elif typeF=='2.0':
            frame = str(firstF)
        elif typeF=='3.0':
            frame = str(firstF) + '-end'
        elif typeF=='4.0':
            frame = str(firstF)+'-'+str(lastF)
        if frame not in frameArray:
            frameArray.append(frame)
        if frame==i:
            getShape = shape.clone()
            addLayer = n2_curves.toElement('frame_' + str(i))
            addLayer.append(getShape)
