#!/usr/bin/python

import sys, os, argparse
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))
import build_support as bs

bs.build(bs.PiglitTester("", _suite="parser", device_override="byt"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="g45"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="g965"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="ilk"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="ivbgt2"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="snbgt2"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="hswgt3"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="bdwgt2"))
bs.build(bs.PiglitTester("", _suite="parser", device_override="chv"))
