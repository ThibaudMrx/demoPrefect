# deployment.py

from flow_docker_launch import docker_flow
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=docker_flow,
    name="deployment-docker-k8s",
    parameters={},
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="kubernetes",
)

if __name__ == "__main__":
    deployment.apply()
