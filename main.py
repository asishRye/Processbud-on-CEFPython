
import sys
import os
import subprocess
from cefpython3 import cefpython as cef
import threading, multiprocessing

CURRENT_DIR = os.path.dirname(__file__)


def pyAlert(msg, _):
    try:
        if _ == "another me":
            subprocess.Popen("core\\tagui\\src\\tagui.cmd flowfiles//amazon.tag ", shell=True)
        else:
            subprocess.call("cd core\\tagui\\src  && end_processes.cmd ", shell=True)
    except Exception as error:
        print("Something went wrong", error)

def launch_cef():
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    browser = cef.CreateBrowserSync(url="file://"+os.path.join(CURRENT_DIR, "build/index.html"), window_title="Processbud")

    # Binding
    bindings = cef.JavascriptBindings(
                bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("mySpecfificFn", pyAlert)
    browser.SetJavascriptBindings(bindings)


    cef.MessageLoop()
    cef.Shutdown()


if __name__ == "__main__":
    launch_cef()




# print("run tagui here and here are some passed parameters", msg, _ )
#     # print("Does it retain type or is it a string??", type(msg), type(_))
#     if _ == "another me":
#         try:
#             p1.start()
#         except Exception:
#             print("Error occured while running your job", Exception)
#     else:
#         try:
#             p2.start()
#         except Exception:
#             print("Error occured while stopping your job", Exception)


# def startProcess():
#     subprocess.call("tagui flowfiles//amazon.tag ", shell=True)

# def stopProcess():
#     subprocess.call("end_processes.cmd", shell=True)

# p1 = multiprocessing.Process(startProcess())
# p2 = multiprocessing.Process(startProcess())
