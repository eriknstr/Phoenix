#---------------------------------------------------------------------------
# Name:        etg/aboutdlg.py
# Author:      Robin Dunn
#
# Created:     22-Mar-2012
# Copyright:   (c) 2013 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_adv"
NAME      = "aboutdlg"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ "wxAboutDialogInfo",
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode('#include <wx/generic/aboutdlgg.h>')

    c = module.find('wxAboutDialogInfo')
    assert isinstance(c, etgtools.ClassDef)

    # Add some aliases for the non-UK spelling
    c.addPyCode("""\
        AboutDialogInfo.HasLicense = AboutDialogInfo.HasLicence
        AboutDialogInfo.GetLicense = AboutDialogInfo.GetLicence
        AboutDialogInfo.License = AboutDialogInfo.Licence
        """)


    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

