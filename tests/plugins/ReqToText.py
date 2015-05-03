"""
Writes output of ReqTracer class to a file
"""

from nose2.events import Plugin
from tests.ReqTracer import Requirements

class ReqToText(Plugin):

    configSection = 'ReqTraceOutput'
    alwaysOn = True

    def afterSummaryReport(self, event):
        f = open("ReqTracingOutput.csv", 'w')
        f.write("Requirement ID, Requirement Description," + " Requirement Method\n\n")

        for item in Requirements:
            f.write(item + ", ")
            f.write('"' + Requirements[item].req_text.replace('"', '""').replace("\n", "") + '", ')
            for func in Requirements[item].func_name:
                f.write(func + " ")

            f.write("\n")

        f.close()