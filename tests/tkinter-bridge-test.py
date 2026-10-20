# This is the future Chaquopy-side smoke test; it is intentionally not run
# by the standalone AndroWish workflow. It should only be enabled after a
# matching native _tkinter extension and Tcl/Tk libraries are packaged.
import sys
print("Python:", sys.version)
import tkinter
print("Tkinter module:", tkinter.__file__)
root = tkinter.Tk()
root.title("Native Tkinter smoke test")
tkinter.Label(root, text="Tkinter native GUI works").pack(padx=20, pady=12)
entry = tkinter.Entry(root)
entry.pack(padx=20, pady=8)
tkinter.Button(root, text="Close", command=root.destroy).pack(pady=12)
root.mainloop()
