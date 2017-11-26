################################################################################
# grbl.py
#
# Post Processor for grbl 0.9f
# It is an ISO machine with a couple of tweaks
#
# ms, 14th July 2014

import nc
import iso_modal
import math

################################################################################
class Creator(iso_modal.Creator):

    def __init__(self):
        iso_modal.Creator.__init__(self)
        
        # optional settings
        self.drillExpanded = True
        self.output_h_and_d_at_tool_change = True
        self.output_comment_before_tool_change = True
        self.output_tool_definitions = True
        self.output_tool_definitions_commented = True
        self.output_g43_on_tool_change_line = False
        self.output_g98_and_g99 = True
        self.output_g43_z_before_drilling_if_g98 = False
        self.output_fixtures = False
            
################################################################################

nc.creator = Creator()