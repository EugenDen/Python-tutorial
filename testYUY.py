import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox_2"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Script1]


class Script1(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Script1"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName= u"Параметр 1".encode('cp1251'),
            name="parameter_1",
            datatype="String",
            parameterType="Required",
            direction="Input")
        param1 = arcpy.Parameter(
            displayName=u"Параметр 2".encode('cp1251'),
            name="parameter_2",
            datatype="String",
            parameterType="Required",
            direction="Input")
        parameters = [param0, param1]
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        parameters[0].filter.list = ["continents", "oceans"]
        parameters[1].filter.list = [[5, 6, 7], [3, 4, 5]][parameters[0].valueAsText == "oceans"]
        # if parameters[0].valueAsText == "oceans":
        #     parameters[1].filter.list = [3, 4, 5]
        # else:
        #     parameters[1].filter.list = [5, 6, 7]
        # return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.AddMessage("Number of %s is %s" % (parameters[0].valueAsText, parameters[1].valueAsText))
        return
