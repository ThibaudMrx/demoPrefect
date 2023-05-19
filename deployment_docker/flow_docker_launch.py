import sys
from prefect import flow, get_run_logger
from prefect_docker.images import pull_docker_image
from prefect_docker.containers import (
    create_docker_container,
    start_docker_container,
    get_docker_container_logs,
    stop_docker_container,
    remove_docker_container,
)
from prefect_docker import DockerHost


@flow
def docker_flow():
    logger = get_run_logger()
    # Image de base
    pull_docker_image("localhost:32000/thibaudmerieux/hello-world-perso" , "latest")
    print("@@@@@@@@@@@@@@@@@@ Debut du fetch d'image @@@@@@@@@@@@@@@@@@@@@@ docker_flow_launch")
    container = create_docker_container(
       image="localhost:32000/thibaudmerieux/hello-world-perso" 
       #command="echo 'HELLO WORLD THIBAUD DOCKER'"
    )
    print("@@@@@@@@@@@@@@@@@@ Fin du fetch d'image @@@@@@@@@@@@@@@@@@@@@@ docker_flow_launch")
    start_docker_container(container_id=container.id)
    logs = get_docker_container_logs(container_id=container.id)
    logger.info(logs)
    stop_docker_container(container_id=container.id)
    remove_docker_container(container_id=container.id)
    return container


if __name__ == "__main__":
    docker_flow()