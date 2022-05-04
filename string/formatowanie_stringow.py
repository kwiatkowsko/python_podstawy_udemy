helloMessage = "Hello %s!"
print(helloMessage % ("Kate"))
print(helloMessage % ("Chirs"))
helloMessage = "Hello {0:s}!"
print(helloMessage.format("Kate"))
print(helloMessage.format("Chirs"))
helloMessage = "%s has %d %s"
print(helloMessage %("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))
helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))