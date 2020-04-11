import maya.cmds as ma
#Created by Simon Paul Mills
#www.simonpaulmills.com

version = 2.0
createOn = '04/20/17'
lastUpdate = '06/17/17'


#allows automation of the maya motion path tool.

toolName = 'motionChain'

axis = [ 'x', 'y', 'z' ]

cycleAttributeDefaultName = 'cycle'

info = '\nThis tool will setup multiple motionPath nodes at once.\nEach node is driven by a "cycle" attribute on the up object.\n\n'

usage = '\nSelect all objects to be evenly aligned along the curve path.\n'

warning01 = 'Nothing selected. Select objects to be aligned on curve path.'

warning02 = 'No valid curve path specified. Select curve path and hit the "set curve path" button.'

warning03 = 'No valid up object specified. Select up object and hit the "set up object" button.'

warning04 = 'Nothing selected. Select curve path.'

warning05 = 'Nothing selected. Select up object.'

pathSuffix = "motionPath"



class ui():
	def __init__( self ):
		self.uiLocation = ( 350, 350 )
		self.topbar = 1
		self.autoSize = 1
		self.sizable = 0
		self.size = [ 300, 80 ]
		self.buttonSize = [ 150, 25]
		# self.inputSize = [ 160, 30 ]
		self.name = toolName
		self.title = self.name + ' v' + str(version) + ' - www.simonpaulmills.com'
		self.button_label1 = 'set curve path'
		self.button_label2 = 'set up object'
		self.button_label3 = 'Populate Curve'

	def build( self ):
		if ma.window( self.name, q=1, ex=1 ):
			ma.deleteUI( self.name )
		ma.window( self.name, t=self.title, dtg='', ip=0, rtf=0, tb=self.topbar, s=self.sizable, ret=0 )
		self.layout()
		self.show()
	
	def kill( self ):
		if ma.window( self.name, q=1, ex=1 ):
			ma.deleteUI( self.name )

	def show( self ):
		ma.showWindow( self.name )
		ma.window( self.name, e=1, tlc=self.uiLocation, wh=self.size, mnb=0, mxb=0, rtf=self.autoSize )

	def layout( self ):
		ma.frameLayout( lv=0, mw = 6, mh = 6 )
		ma.rowColumnLayout( nc=1 )
		ma.text( 'text01', l=info )
		ma.frameLayout( lv=0, mw = 6, mh = 6 )
		ma.rowColumnLayout( nc=3 )
		ma.textField( "textFieldInput_attribute", w = self.size[0] / 2.0, tx=cycleAttributeDefaultName )
		ma.text( '   ' ) #space
		ma.text( '   cycle attribute name  ' ) #space
		ma.setParent( '..' )
		ma.rowColumnLayout( nc=3 )
		ma.textField( "textFieldInput_curvePath", w = self.size[0] / 2.0, tx="curve path" )
		ma.text( '   ' ) #space
		ma.nodeIconButton( 'button_curvePath"', l=self.button_label1, w=self.buttonSize[0], h=self.buttonSize[1], fn='boldLabelFont', st='textOnly', c=lambda x=None: self.setCurvePath() )
		ma.setParent( '..' )
		ma.rowColumnLayout( nc=3 )
		ma.textField( "textFieldInput_upObject", w = self.size[0] / 2.0, tx="up object" )
		ma.text( '   ' ) #space
		ma.nodeIconButton( 'button_upObject', l=self.button_label2, w=self.buttonSize[0], h=self.buttonSize[1], fn='boldLabelFont', st='textOnly', c=lambda x=None: self.setUpObject() )
		ma.setParent( '..' )
		ma.rowColumnLayout( nc = 3 )
		ma.radioButtonGrp( 'radioButtonGrp_curvePath', l='Front axis: ', la3=axis, nrb=3, cw4= [ self.size[0] / 3 , self.size[0] / 12 , self.size[0] / 12, self.size[0] / 3 ], sl=3 )
		ma.text( '   ' ) #space
		ma.checkBox( 'checkBox_curvePath', l='Inverse     ', v=0 )
		ma.radioButtonGrp( 'radioButtonGrp_upObject', l='Up axis: ', la3=axis, nrb=3, cw4= [ self.size[0] / 3 , self.size[0] / 12 , self.size[0] / 12, self.size[0] / 3 ], sl=2 )
		ma.text( '   ' ) #space
		ma.checkBox( 'checkBox_upObject', l='Inverse     ', v=0 )
		ma.setParent( '..' )
		ma.frameLayout( lv=0, mw = 6, mh = 6 )
		ma.rowColumnLayout( nc=1 )
		ma.text( 'text02', l=usage )
		ma.nodeIconButton( 'button03', l=self.button_label3, w=self.size[0] / 1.75, h=self.buttonSize[1], fn='boldLabelFont', st='textOnly', c=lambda x=None: self.command() )
		ma.setParent( '..' )

	def setCurvePath( self ):
		selected = ma.ls( sl=1 )
		if selected != []:
			ma.textField( 'textFieldInput_curvePath', e=1, tx=selected[-1] )
		else:
			cmdWarn( warning04 )

	def setUpObject( self ):
		selected = ma.ls( sl=1 )
		if selected != []:
			ma.textField( 'textFieldInput_upObject', e=1, tx=selected[-1] )
		else:
			cmdWarn( warning05 )

	def command( self ):
		itemList = ma.ls( sl=1 )
		curvePath = ma.textField( 'textFieldInput_curvePath', q=1, tx=1 )
		upObject = ma.textField( 'textFieldInput_upObject', q=1, tx=1 )
	
		if itemList == []:
			cmdWarn( warning01 )

		elif not ma.objExists( curvePath ):
			cmdWarn( warning02 )
		
		elif not ma.objExists( upObject ):
			cmdWarn( warning03 )

		else:
			frontAxis =  axis[ ma.radioButtonGrp( 'radioButtonGrp_curvePath', q=1, sl=1 ) -1 ]
			invertFront = ma.checkBox( 'checkBox_curvePath', q=1, v=1 )
			upAxis =  axis[ ma.radioButtonGrp( 'radioButtonGrp_upObject', q=1, sl=1 ) -1 ]
			invertUp = ma.checkBox( 'checkBox_upObject', q=1, v=1 )
			cycleAttributeName = ma.textField( 'textFieldInput_attribute', q=1, tx=1 )
			motionPath( itemList, curvePath, upObject, frontAxis, invertFront, upAxis, invertUp, cycleAttributeName )




def cmdPrint( info ):
	from maya.OpenMaya import MGlobal; MGlobal.displayInfo( '%s' % ( info ) )


def cmdWarn( info ):
	from maya.OpenMaya import MGlobal; MGlobal.displayWarning( '%s' % ( info ) )


def getConnection( item ):
	return list( set( getConnectionIn( item ) + getConnectionOut( item ) ) )


def getConnectionIn( item, plugs = 0 ):
	inConnection =  ma.listConnections( item, d=0, s=1, scn=1, p=plugs )
	return [] if inConnection == None else list( set( inConnection ) )


def getConnectionOut( item, plugs = 0 ):
	outConnection =  ma.listConnections( item, d=1, s=0, scn=1, p=plugs )
	return [] if outConnection == None else list( set( outConnection ) )


def getConnectionByType( item, nodeType ):
	# returns list of all connected history of given type, newest first
	connectionList = []
	for connection in getConnection( item ):
		if ma.nodeType( connection ) == nodeType:
			connectionList.append( connection )
	connectionList.sort()
	connectionList.reverse()
	return connectionList


def motionPath( itemList, curvePath, upObject, frontAxis, invertFront, upAxis, invertUp, cycleAttributeName ):
	attributeList = [ cycleAttributeName, 'frontTwist', 'upTwist', 'sideTwist' ]
	for attr in attributeList:
		if not ma.objExists( upObject + '.' + attr ):
			ma.addAttr( upObject, ln=attr, at='double' )
			ma.setAttr( upObject + '.' + attr, e=1, k=1, cb=0 )

	offset = 1.0 / float( len( itemList ) ) if len( itemList ) > 1 else 0.5
	for i in range( 0, len( itemList ) ):
		#create motionpath
		path = ma.pathAnimation( itemList[i], c=curvePath, n=itemList[i] + '_' + pathSuffix, fm=1, f=1, fa=frontAxis, ua=upAxis, wut='object', wuo=upObject, iu=invertUp, inverseFront=invertFront, b=0 )
		ma.cutKey( path )
		driven = path + '.' + 'uValue'

		#setDrivenKeys
		ma.setDrivenKeyframe( driven, cd=upObject + '.' + attributeList[0], dv= i * offset, v=0, itt = 'linear', ott = 'linear' )
		ma.setDrivenKeyframe( driven, cd=upObject + '.' + attributeList[0], dv=( i * offset ) + 1, v=1, itt = 'linear', ott = 'linear' )
		ma.setInfinity( driven, pri='cycle', poi='cycle' )
		for attr in attributeList:
			if attr != attributeList[0]:
				ma.connectAttr( upObject + '.' + attr, path + '.' + attr )
		#cleanup
		convertDoubleLinear( path )


def convertDoubleLinear( curvePathNode ):
	#removes doubleLinear nodes and connects them using "allCoordinates" to translation
	dblLinearList, outList = getConnectionByType( curvePathNode, 'addDoubleLinear' ), []
	for dl in dblLinearList:
		outList += getConnectionOut( dl )
	outList = list( set( outList ) )
	outList.sort()
	ma.delete( dblLinearList )
	for o in outList:
		for ax in axis:
			ma.connectAttr( curvePathNode + '.' + ax.lower() + 'Coordinate', o + '.translate' + ax.upper() )




ui().build()
