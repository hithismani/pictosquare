# -*- coding: utf-8 -*-
#! /usr/bin/env python
import sys
import argparse
from pictosquare import folderfetcher

def run(args):
	colour = ""
	if args.color:
		if args.color.lower() == "white":
			colour = "#ffffff"
		elif args.color.lower() == "black":
			colour = "#000000"
		elif len(args.color) == 6:
			colour = "#"+args.color
		elif args.color.lower() == "thief":
			colour = "thief"
		else:
			print("Colour not found. Defaulting to white.")
			colour = "#ffffff"
	folderfetcher.folderSquarer(args.dir, colour)

def main():
	parser=argparse.ArgumentParser(description="picToSquare")
	parser.add_argument("-dir",help="Set Input Directory. Set 'currentdir' for current directory." ,dest="dir", type=str, required=True, default="currentdir")
	parser.add_argument("-color",help="Set Background Colour" ,dest="color", type=str, default = "white", required=False)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__ == '__main__':
    main()