"""Setup for rezoning-api."""

from setuptools import find_packages, setup

# Runtime requirements.
inst_reqs = [
    "fastapi",
    "pydantic",
    "jinja2",
    "geojson_pydantic",
    "shapely",
    "xarray",
    "aiofiles",
]

dependency_links = [
    "https://github.com/cogeotiff/rio-tiler/tarball/master#egg=209db52bc6fee1fa74611f7c92bf3f5ad161813d"
]

extra_reqs = {
    "dev": ["pytest", "pytest-benchmark", "pytest-asyncio"],
    "server": ["uvicorn"],
    "deploy": [
        "docker",
        "attrs",
        "aws-cdk.core==1.72.0",
        "aws-cdk.aws_lambda==1.72.0",
        "aws-cdk.aws_apigatewayv2==1.72.0",
        "aws-cdk.aws_ecs==1.72.0",
        "aws-cdk.aws_ec2==1.72.0",
        "aws-cdk.aws_autoscaling==1.72.0",
        "aws-cdk.aws_ecs_patterns==1.72.0",
        "aws-cdk.aws_iam==1.72.0",
        "aws-cdk.aws_elasticache==1.72.0",
        "aws-cdk.aws_logs==1.72.0",
        "aws-cdk.aws_ecr==1.72.0",
    ],
    "test": ["moto", "mock", "pytest", "pytest-cov", "pytest-asyncio", "requests"],
}

setup(
    name="rezoning-api",
    version="0.1.30",
    python_requires=">=3",
    description=u"""API for the REZoning project""",
    dependency_links=dependency_links,
    packages=find_packages(exclude=["tests"]),
    package_data={
        "rezoning_api": [
            "templates/*.html",
            "db/countries.geojson",
            "db/layers.json",
            "db/cf.json",
        ]
    },
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
