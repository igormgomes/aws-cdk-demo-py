#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_demo_py.aws_cdk_demo_py_stack import AwsCdkDemoPyStack


app = cdk.App()
AwsCdkDemoPyStack(app, "aws-cdk-demo-py", env={'region': 'us-east-1'})

app.synth()
