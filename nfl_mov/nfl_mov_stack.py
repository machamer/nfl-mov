from aws_cdk import (
    aws_lambda as _lambda,
    core
)


class NflMovStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        mov_lambda = _lambda.Function(
            self, 'CalcMov',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda/calculate_mov'),
            handler='calculate_mov.handler',
            timeout=core.Duration.seconds(6)
        )   
