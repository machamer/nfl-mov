#!/usr/bin/env python3

from aws_cdk import core

from nfl_mov.nfl_mov_stack import NflMovStack


app = core.App()
NflMovStack(app, "nfl-mov")

app.synth()
